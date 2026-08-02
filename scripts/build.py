#!/usr/bin/env python3
"""
GNU static binary builder.
Handles: FTP resolution, download, GPG verify, configure/make, package, verify.

Linux:  built with musl-gcc for true static binaries (no glibc dependency).
macOS:  dynamically linked against /usr/lib/libSystem.B.dylib only (unavoidable on Apple platforms).
"""

import argparse
import os
import platform
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path


def run(cmd, check=True, **kwargs):
    print(f"+ {' '.join(str(c) for c in cmd)}")
    return subprocess.run(cmd, check=check, **kwargs)


def resolve_tarball(ftp_path, tarball_prefix, version):
    base_url = f"https://ftpmirror.gnu.org/{ftp_path}"
    for ext in ("tar.xz", "tar.gz", "tar.bz2", "tgz"):
        name = f"{tarball_prefix}-{version}.{ext}"
        url = f"{base_url}/{name}"
        req = urllib.request.Request(url, method="HEAD")
        try:
            with urllib.request.urlopen(req, timeout=10):
                return url, name
        except Exception:
            continue
    raise RuntimeError(f"No tarball found for {tarball_prefix} {version} at {base_url}")


def download(url, dest):
    run(["curl", "-fSL", "--retry", "5", "--retry-delay", "2", "-o", str(dest), url])


def verify_gpg(tarball_path):
    sig_path = Path(str(tarball_path) + ".sig")
    keyring = tarball_path.parent / "gnu-keyring.gpg"
    if not sig_path.exists():
        print(f"WARNING: No .sig for {tarball_path.name}, skipping GPG verification")
        return
    run(["curl", "-fSL", "--retry", "3", "-o", str(keyring), "https://ftp.gnu.org/gnu/gnu-keyring.gpg"])
    run(["gpg", "--import", str(keyring)])
    result = run(["gpg", "--verify", str(sig_path), str(tarball_path)], check=False)
    if result.returncode != 0:
        raise RuntimeError(f"GPG verification FAILED for {tarball_path.name}")
    print(f"GPG verified: {tarball_path.name}")


def _is_alpine():
    try:
        return "Alpine" in Path("/etc/os-release").read_text()
    except OSError:
        return False


def install_deps(deps_apt, deps_brew, deps_apk=""):
    os_name = platform.system().lower()
    if os_name == "linux":
        if _is_alpine():
            base_pkgs = ["build-base", "curl", "gnupg", "texinfo", "bash", "tar", "xz", "gzip"]
            # prefer deps_apk when provided; fall back to deps_apt for Alpine-compatible package names
            extra = (deps_apk or deps_apt).split() if (deps_apk or deps_apt) else []
            run(["apk", "add", "--no-cache"] + base_pkgs + extra)
        else:
            pkgs = ["texinfo", "musl-tools"] + (deps_apt.split() if deps_apt else [])
            run(["sudo", "apt-get", "update", "-qq"])
            run(["sudo", "apt-get", "install", "-y", "-qq"] + pkgs)
    elif os_name == "darwin":
        pkgs = ["texinfo"] + (deps_brew.split() if deps_brew else [])
        run(["brew", "install"] + pkgs)


def _find_musl_gcc():
    for candidate in ("musl-gcc", "x86_64-linux-musl-gcc", "aarch64-linux-musl-gcc"):
        if shutil.which(candidate):
            return candidate
    return None


def build(src_dir, install_dir, configure_args):
    os_name = platform.system().lower()
    env = os.environ.copy()

    if os_name == "linux":
        if _is_alpine():
            # Alpine's system gcc links musl by default — just add -static
            env["CFLAGS"] = f"-O2 {env.get('CFLAGS', '')}"
            env["LDFLAGS"] = f"-static {env.get('LDFLAGS', '')}"
        else:
            musl_gcc = _find_musl_gcc()
            if musl_gcc:
                env["CC"] = musl_gcc
                env["CFLAGS"] = f"-O2 {env.get('CFLAGS', '')}"
                env["LDFLAGS"] = f"-static {env.get('LDFLAGS', '')}"
                # Make system kernel headers available to musl-gcc so that
                # gnulib modules that probe <linux/fs.h> etc. can compile.
                env["CPPFLAGS"] = f"-I/usr/include {env.get('CPPFLAGS', '')}"
            else:
                print("WARNING: musl-gcc not found, falling back to glibc static link")
                env["LDFLAGS"] = f"-static -static-libgcc -static-libstdc++ {env.get('LDFLAGS', '')}"
                env["CFLAGS"] = f"-O2 {env.get('CFLAGS', '')}"
    elif os_name == "darwin":
        # macOS: link only against system libraries (libSystem.B.dylib is always present)
        env["LDFLAGS"] = f"-Wl,-dead_strip {env.get('LDFLAGS', '')} -liconv"
        env["CFLAGS"] = f"-O2 {env.get('CFLAGS', '')}"

    configure = src_dir / "configure"
    Configure = src_dir / "Configure"
    prefix = f"--prefix={install_dir}"
    base_args = [prefix, "--disable-dependency-tracking", "--disable-nls"]
    extra = configure_args.split() if configure_args else []

    if configure.exists():
        run([str(configure)] + base_args + extra, cwd=src_dir, env=env)
    elif Configure.exists():
        run([str(Configure), prefix] + extra, cwd=src_dir, env=env)

    ncpu = os.cpu_count() or 2
    run(["make", f"-j{ncpu}"], cwd=src_dir, env=env)
    run(["make", "install"], cwd=src_dir, env=env)


def verify_binary(binary_path):
    """Check linkage of a built binary and raise if it has unexpected dynamic deps."""
    os_name = platform.system().lower()
    binary_path = Path(binary_path)

    if os_name == "linux":
        result = run(["ldd", str(binary_path)], check=False, capture_output=True, text=True)
        output = result.stdout + result.stderr
        if "not a dynamic executable" in output:
            print(f"  static: {binary_path.name}")
            return
        if result.returncode != 0:
            raise RuntimeError(
                f"{binary_path.name} ldd failed unexpectedly (exit {result.returncode}):\n{output}"
            )
        # ldd succeeded → dynamically linked; vdso is kernel-injected and not a real file dep
        deps = [
            line.strip()
            for line in output.splitlines()
            if "=>" in line or "linux-vdso" in line or "ld-" in line
        ]
        real_deps = [d for d in deps if "linux-vdso" not in d]
        if real_deps:
            raise RuntimeError(
                f"{binary_path.name} is NOT fully static. Dynamic deps:\n" + "\n".join(real_deps)
            )
        print(f"  static (vdso only): {binary_path.name}")

    elif os_name == "darwin":
        result = run(["otool", "-L", str(binary_path)], check=False, capture_output=True, text=True)
        libs = [
            line.strip().split()[0]
            for line in result.stdout.splitlines()[1:]
            if line.strip()
        ]
        allowed_prefixes = ("/usr/lib/libSystem", "/usr/lib/libc++", "/usr/lib/libiconv")
        unexpected = [lib for lib in libs if not any(lib.startswith(p) for p in allowed_prefixes)]
        if unexpected:
            raise RuntimeError(
                f"{binary_path.name} links unexpected libraries:\n" + "\n".join(unexpected)
            )
        print(f"  ok (system libs only): {binary_path.name}")


def package(project, version, binary_names, install_dir, work_dir, src_dir, verify=True):
    os_name = platform.system().lower()
    machine = platform.machine().lower()
    arch = {"x86_64": "amd64", "aarch64": "arm64", "arm64": "arm64"}.get(machine, machine)

    asset_name = f"{project}-{version}-{os_name}-{arch}.tar.gz"
    asset_path = work_dir / asset_name

    with tempfile.TemporaryDirectory() as stage:
        stage = Path(stage)
        for binary in binary_names.split():
            found = next(install_dir.rglob(binary), None)
            if not found or not found.is_file():
                raise RuntimeError(f"Expected binary '{binary}' not found in install tree")
            if verify:
                verify_binary(found)
            shutil.copy2(found, stage / binary)

        for lic in ("COPYING", "COPYING.v3", "COPYING.v2", "LICENSE"):
            lic_path = src_dir / lic
            if lic_path.exists():
                shutil.copy2(lic_path, stage / "COPYING")
                break

        run(["tar", "-czf", str(asset_path), "-C", str(stage), "."])

    print(f"Built: {asset_path}")

    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a") as f:
            f.write(f"asset_name={asset_name}\n")
            f.write(f"asset_path={asset_path}\n")

    return asset_path


def main(args=None):
    parser = argparse.ArgumentParser(description="Build a GNU project as a static binary")
    parser.add_argument("--project", required=True)
    parser.add_argument("--version", required=True)
    parser.add_argument("--binary-names", required=True)
    parser.add_argument("--work-dir", default=os.environ.get("GITHUB_WORKSPACE", str(Path.cwd() / "build")))
    parser.add_argument("--ftp-path", default=None)
    parser.add_argument("--tarball-prefix", default=None)
    parser.add_argument("--configure-args", default="")
    parser.add_argument("--tarball-url", default=None, help="Skip FTP resolution, use this URL directly")
    parser.add_argument("--deps-apt", default="")
    parser.add_argument("--deps-apk", default="")
    parser.add_argument("--deps-brew", default="")
    parser.add_argument("--skip-gpg", action="store_true")
    parser.add_argument("--skip-verify", action="store_true", help="Skip binary linkage verification")
    a = parser.parse_args(args)

    ftp_path = a.ftp_path or a.project
    tarball_prefix = a.tarball_prefix or a.project
    work_dir = Path(a.work_dir)
    work_dir.mkdir(parents=True, exist_ok=True)
    install_dir = work_dir / "_install"
    install_dir.mkdir(exist_ok=True)

    install_deps(a.deps_apt, a.deps_brew, a.deps_apk)

    if a.tarball_url:
        download_url = a.tarball_url
        tarball_name = Path(a.tarball_url).name
    else:
        download_url, tarball_name = resolve_tarball(ftp_path, tarball_prefix, a.version)

    tarball_path = work_dir / tarball_name
    download(download_url, tarball_path)

    sig_url = f"{download_url}.sig"
    sig_path = work_dir / f"{tarball_name}.sig"
    if not a.skip_gpg:
        try:
            download(sig_url, sig_path)
        except subprocess.CalledProcessError:
            raise RuntimeError(
                f"Failed to download signature {sig_url}. Use --skip-gpg to bypass verification."
            )
        verify_gpg(tarball_path)

    run(["tar", "xf", str(tarball_path)], cwd=work_dir)

    # Derive the expected directory name from the tarball stem so we don't
    # accidentally pick up a leftover directory from a previous build run.
    stem = tarball_name
    for suffix in (".tar.xz", ".tar.gz", ".tar.bz2", ".tgz"):
        if stem.endswith(suffix):
            stem = stem[: -len(suffix)]
            break
    src_dir = work_dir / stem
    if not src_dir.is_dir():
        raise RuntimeError(f"Expected source directory '{stem}' not found after extraction")

    build(src_dir, install_dir, a.configure_args)
    package(a.project, a.version, a.binary_names, install_dir, work_dir, src_dir, verify=not a.skip_verify)


if __name__ == "__main__":
    main()
