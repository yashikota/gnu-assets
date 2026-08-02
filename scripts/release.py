#!/usr/bin/env python3
"""
Create GNU GitHub Release
Independent, unit-testable Python script to create immutable GitHub Releases.
"""

import argparse
import os
import subprocess
import sys


def run_gh(args, check=True):
    print(f"Running: gh {' '.join(args)}")
    res = subprocess.run(["gh"] + args, capture_output=True, text=True)
    if check and res.returncode != 0:
        print(f"Error: gh {' '.join(args)}\nStdout: {res.stdout}\nStderr: {res.stderr}")
        sys.exit(res.returncode)
    return res


def download_file(url, output_path, retries=5):
    res = subprocess.run(
        ["curl", "-fSL", "--retry", str(retries), "--retry-delay", "2", "-o", output_path, url],
        capture_output=True,
        text=True,
    )
    return res.returncode == 0


def check_existing_release(tag):
    res = run_gh(["release", "view", tag], check=False)
    return res.returncode == 0


def main():
    parser = argparse.ArgumentParser(description="Create an immutable GNU release on GitHub.")
    parser.add_argument("--project", required=True, help="GNU project name")
    parser.add_argument("--version", required=True, help="Release version")
    parser.add_argument("--assets", required=True, help="Space or newline separated asset file paths")
    parser.add_argument("--download-url", required=True, help="Source tarball download URL")
    parser.add_argument("--tarball-name", required=True, help="Source tarball filename")

    args = parser.parse_args()

    tag = f"{args.project}-v{args.version}"
    print(f"=== Creating Immutable Release for {args.project} {args.version} ({tag}) ===")

    if check_existing_release(tag):
        print(f"::warning::Release {tag} already exists. Skipping (immutable releases).")
        sys.exit(0)

    os.makedirs("source_assets", exist_ok=True)
    source_tarball_path = os.path.join("source_assets", args.tarball_name)
    sig_path = f"{source_tarball_path}.sig"

    print(f"Downloading source tarball from {args.download_url}...")
    if not download_file(args.download_url, source_tarball_path):
        print(f"Failed to download source tarball from {args.download_url}")
        sys.exit(1)

    print(f"Downloading signature from {args.download_url}.sig...")
    download_file(f"{args.download_url}.sig", sig_path)

    asset_files = []
    for asset in args.assets.replace("\n", " ").split():
        if os.path.isfile(asset):
            asset_files.append(asset)
    for src in [source_tarball_path, sig_path]:
        if os.path.isfile(src):
            asset_files.append(src)

    notes = (
        f"Automated build of GNU {args.project} {args.version}. "
        f"Official source: {args.download_url}\n\n"
        f"> [!CAUTION]\n"
        f"> **Unofficial Build**: This repository is an unofficial distribution. "
        f"For official source releases, visit https://ftp.gnu.org/gnu/{args.project}/\n\n"
        f"> Immutable release: This release will not be modified or overwritten once published."
    )

    notes_file = "/tmp/release_notes.md"
    with open(notes_file, "w") as f:
        f.write(notes)

    run_gh(
        ["release", "create", tag, "--title", f"{args.project} {args.version}", "--notes-file", notes_file]
        + asset_files
    )

    print(f"Successfully created immutable release: {tag}")


if __name__ == "__main__":
    main()
