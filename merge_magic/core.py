"""Core functions for Merge Patcher of Doom.

Implements Task 01 and Task 02 from codex.md:
1. Scan MO2 mod list for conflicting files.
2. Build a structured merge workspace.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List
import shutil


def read_mod_order(mo2_path: Path, profile: str) -> List[str]:
    """Return the list of enabled mods in load order."""
    modlist_path = mo2_path / "profiles" / profile / "modlist.txt"
    mods: List[str] = []
    with modlist_path.open() as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            enabled = line[0] == '+'
            mod_name = line[1:].strip()
            if enabled:
                mods.append(mod_name)
    return mods


def scan_conflicts(mo2_path: Path, profile: str) -> Dict[str, List[str]]:
    """Return a mapping of file path to the list of mods that provide it."""
    mods = read_mod_order(mo2_path, profile)
    file_map: Dict[str, List[str]] = {}

    for mod in mods:
        mod_dir = mo2_path / "mods" / mod
        if not mod_dir.is_dir():
            continue
        for path in mod_dir.rglob('*'):
            if path.is_file():
                rel_path = path.relative_to(mod_dir).as_posix()
                file_map.setdefault(rel_path, []).append(mod)

    # Filter to only conflicts (files with more than one provider)
    conflicts = {p: m for p, m in file_map.items() if len(m) > 1}
    return conflicts


def save_conflicts(conflicts: Dict[str, List[str]], output_file: Path) -> None:
    with output_file.open('w') as fh:
        json.dump(conflicts, fh, indent=2)


def load_conflicts(input_file: Path) -> Dict[str, List[str]]:
    with input_file.open() as fh:
        return json.load(fh)


def build_workspace(mo2_path: Path, conflicts: Dict[str, List[str]], output_dir: Path) -> None:
    """Create merge workspace folder structure using conflict data."""
    for file_path, mods in conflicts.items():
        dest_root = output_dir / file_path
        for mod in mods:
            src = mo2_path / "mods" / mod / file_path
            if not src.exists():
                continue
            dest = dest_root / mod
            dest.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dest / Path(file_path).name)

