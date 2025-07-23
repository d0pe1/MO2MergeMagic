"""Command line interface for Merge Patcher of Doom."""

from __future__ import annotations

import argparse
from pathlib import Path
from .core import scan_conflicts, save_conflicts, load_conflicts, build_workspace


def main() -> None:
    parser = argparse.ArgumentParser(description="MO2 Merge Patcher helper")
    subparsers = parser.add_subparsers(dest="command", required=True)

    scan_p = subparsers.add_parser("scan", help="Scan MO2 profile for conflicts")
    scan_p.add_argument("--mo2-path", required=True, type=Path)
    scan_p.add_argument("--profile", required=True)
    scan_p.add_argument("--out", default="conflicts.json", type=Path)

    build_p = subparsers.add_parser("build", help="Build merge workspace")
    build_p.add_argument("--mo2-path", required=True, type=Path)
    build_p.add_argument("--conflicts", required=True, type=Path)
    build_p.add_argument("--out", default=Path("merge_work"), type=Path)

    args = parser.parse_args()

    if args.command == "scan":
        conflicts = scan_conflicts(args.mo2_path, args.profile)
        save_conflicts(conflicts, args.out)
        print(f"Saved conflicts to {args.out}")
    elif args.command == "build":
        conflicts = load_conflicts(args.conflicts)
        build_workspace(args.mo2_path, conflicts, args.out)
        print(f"Workspace created at {args.out}")


if __name__ == "__main__":
    main()

