#!/usr/bin/env python3
"""
GNU-Assets Central Watcher
Scrapes ftpmirror.gnu.org for new releases across all configured projects
and triggers build workflows via workflow_dispatch.
"""

import os
import re
import subprocess
import urllib.request

import yaml


def load_projects(projects_file):
    with open(projects_file) as f:
        data = yaml.safe_load(f)
    return data["projects"]


def run_gh(args):
    return subprocess.run(["gh"] + args, capture_output=True, text=True)


def get_latest_ftp_version(project_name, ftp_path, tar_prefix):
    url = f"https://ftpmirror.gnu.org/{ftp_path}/"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode("utf-8", errors="ignore")

        pattern = rf"{tar_prefix}-([0-9]+(?:\.[0-9]+)*)\.(?:tar\.(?:xz|gz|bz2)|tgz)"
        matches = re.findall(pattern, html)
        if not matches:
            return None

        def parse_ver(v):
            return [int(x) for x in v.split(".")]

        valid_versions = []
        for m in matches:
            try:
                valid_versions.append((parse_ver(m), m))
            except ValueError:
                continue

        valid_versions.sort()
        return valid_versions[-1][1] if valid_versions else None
    except Exception as e:
        print(f"Error fetching FTP for {project_name}: {e}")
        return None


def get_latest_github_release(repo, project_name):
    res = run_gh(["release", "list", "--repo", repo, "--json", "tagName", "-q", ".[].tagName"])
    if res.returncode != 0 or not res.stdout.strip():
        return None
    prefix = f"{project_name}-v"
    tags = [
        t.removeprefix(prefix)
        for t in res.stdout.strip().splitlines()
        if t.startswith(prefix)
    ]
    if not tags:
        return None

    def parse_ver(v):
        try:
            return [int(x) for x in v.split(".")]
        except ValueError:
            return [0]

    return sorted(tags, key=parse_ver)[-1]


def main(dry_run=False):
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Check versions only, do not trigger builds")
    args = parser.parse_args()
    dry_run = dry_run or args.dry_run

    repo = os.environ.get("GITHUB_REPOSITORY", "yashikota/gnu-assets")
    projects_file = os.path.join(os.path.dirname(__file__), "..", "projects.yml")

    print("Starting GNU-Assets Central Watcher..." + (" (dry-run)" if dry_run else ""))
    projects = load_projects(projects_file)
    triggered = []

    for p in projects:
        name = p["name"]
        ftp_path = p.get("ftp_path", name)
        tar_prefix = p.get("tarball_prefix", name)

        latest_ftp = get_latest_ftp_version(name, ftp_path, tar_prefix)
        latest_gh = get_latest_github_release(repo, name)

        print(f"[{name}]: FTP={latest_ftp}, GitHub={latest_gh}")

        def _parse_ver(v):
            try:
                return [int(x) for x in v.split(".")]
            except (ValueError, AttributeError):
                return [0]

        ftp_newer = latest_ftp and (not latest_gh or _parse_ver(latest_ftp) > _parse_ver(latest_gh))
        if ftp_newer:
            if dry_run:
                print(f"  -> Would trigger build: {latest_gh} -> {latest_ftp}")
                triggered.append(name)
            else:
                print(f"New version for {name}: {latest_gh} -> {latest_ftp}. Triggering build...")
                res = run_gh(["workflow", "run", "build.yml", "--repo", repo, "-f", f"project={name}"])
                if res.returncode == 0:
                    triggered.append(name)
                else:
                    print(f"Failed to trigger {name}: {res.stderr}")

    label = "Would trigger" if dry_run else "Triggered"
    print(f"Done. {label} {len(triggered)} builds: {triggered}")


if __name__ == "__main__":
    main()
