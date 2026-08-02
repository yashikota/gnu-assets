#!/usr/bin/env python3
"""
Check if a new GNU project version is available on FTP vs. the latest GitHub release.
Writes results to GITHUB_OUTPUT (or stdout with --print).
"""

import argparse
import os
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

import yaml


def load_project(projects_file, project_name):
    with open(projects_file) as f:
        data = yaml.safe_load(f)
    projects = {p["name"]: p for p in data["projects"]}
    if project_name not in projects:
        print(f"::error::Unknown project '{project_name}'. Add it to projects.yml first.", file=sys.stderr)
        sys.exit(1)
    return projects[project_name]


def get_latest_ftp_version(ftp_path, tarball_prefix, force_version=None):
    if force_version:
        return force_version

    candidates = [
        f"https://ftpmirror.gnu.org/{ftp_path}",
        f"https://ftp.gnu.org/gnu/{ftp_path}",
    ]
    html = None
    last_err = None
    for base_url in candidates:
        req = urllib.request.Request(f"{base_url}/", headers={"User-Agent": "Mozilla/5.0"})
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                html = resp.read().decode("utf-8", errors="ignore")
            break
        except Exception as e:
            last_err = e
            continue
    if html is None:
        raise RuntimeError(f"Failed to fetch FTP listing for {ftp_path}: {last_err}") from last_err

    pattern = rf"{tarball_prefix}-([0-9]+(?:\.[0-9]+)*)\.(?:tar\.(?:xz|gz|bz2|lz)|tgz)"
    matches = re.findall(pattern, html)
    if not matches:
        return None

    def parse_ver(v):
        try:
            return [int(x) for x in v.split(".")]
        except ValueError:
            return [0]

    return sorted(set(matches), key=parse_ver)[-1]


def resolve_tarball_url(ftp_path, tarball_prefix, version):
    base_urls = [
        f"https://ftpmirror.gnu.org/{ftp_path}",
        f"https://ftp.gnu.org/gnu/{ftp_path}",
    ]
    for ext in ("tar.xz", "tar.gz", "tar.bz2", "tgz", "tar.lz"):
        name = f"{tarball_prefix}-{version}.{ext}"
        for base_url in base_urls:
            url = f"{base_url}/{name}"
            req = urllib.request.Request(url, method="HEAD")
            try:
                with urllib.request.urlopen(req, timeout=10):
                    return url, name
            except Exception:
                continue
    return None, None


def get_latest_github_release(project_name):
    res = subprocess.run(
        ["gh", "release", "list", "--limit", "1000", "--json", "tagName", "-q", ".[].tagName"],
        capture_output=True, text=True,
    )
    if res.returncode != 0:
        raise RuntimeError(f"gh release list failed: {res.stderr.strip()}")
    if not res.stdout.strip():
        return None
    tags = [
        t.removeprefix(f"{project_name}-v")
        for t in res.stdout.strip().splitlines()
        if t.startswith(f"{project_name}-v")
    ]
    if not tags:
        return None

    def parse_ver(v):
        try:
            return [int(x) for x in v.split(".")]
        except ValueError:
            return [0]

    return sorted(tags, key=parse_ver)[-1]


def write_outputs(outputs, output_file=None):
    lines = "".join(f"{k}={v}\n" for k, v in outputs.items())
    if output_file:
        with open(output_file, "a") as f:
            f.write(lines)
    else:
        print(lines, end="")


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True)
    parser.add_argument("--force-version", default="")
    parser.add_argument("--projects-file", default=str(Path(__file__).parent.parent / "projects.yml"))
    parser.add_argument("--print", action="store_true", help="Print outputs instead of writing to GITHUB_OUTPUT")
    args = parser.parse_args(argv)

    p = load_project(args.projects_file, args.project)
    ftp_path = p.get("ftp_path", args.project)
    tarball_prefix = p.get("tarball_prefix", args.project)

    latest = get_latest_ftp_version(ftp_path, tarball_prefix, args.force_version or None)
    if not latest:
        print(f"::error::No versions found for {args.project}", file=sys.stderr)
        write_outputs({"has_new": "false"}, None if args.print else os.environ.get("GITHUB_OUTPUT"))
        sys.exit(0)

    download_url, tarball_name = resolve_tarball_url(ftp_path, tarball_prefix, latest)
    if not download_url:
        print(f"::error::No tarball found for {args.project} {latest}", file=sys.stderr)
        write_outputs({"has_new": "false"}, None if args.print else os.environ.get("GITHUB_OUTPUT"))
        sys.exit(0)

    current = get_latest_github_release(args.project)

    def _parse_ver(v):
        try:
            return [int(x) for x in v.split(".")]
        except (ValueError, AttributeError):
            return [0]

    if args.force_version:
        has_new = "true"
    else:
        has_new = "true" if (not current or _parse_ver(latest) > _parse_ver(current)) else "false"

    if has_new == "false":
        print(f"Already up to date: {latest}")
    else:
        print(f"New version: {current} -> {latest}")

    outputs = {
        "has_new": has_new,
        "latest_version": latest,
        "download_url": download_url,
        "tarball_name": tarball_name,
        "binary_names": p["binary_names"],
        "configure_args": p.get("configure_args", ""),
        "make_args": p.get("make_args", ""),
        "dependencies_apt": p.get("dependencies_apt", ""),
        "dependencies_apk": p.get("dependencies_apk", ""),
        "dependencies_brew": p.get("dependencies_brew", ""),
        "skip_gpg": "true" if p.get("skip_gpg") else "false",
    }
    write_outputs(outputs, None if args.print else os.environ.get("GITHUB_OUTPUT"))


if __name__ == "__main__":
    main()
