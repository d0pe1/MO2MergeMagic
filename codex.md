# 🧠 Codex Task List: Merge Patcher of Doom

This file contains modular, trackable task definitions for Codex agents to follow step-by-step while building the auto-patcher. Comment each out once done ✅

---

## ✅ Task 01: Scan MO2 Profile for Conflicts

**Goal:** Read Mod Organizer 2's `modlist.txt` and active `profile` to build a full list of files that would be loaded at runtime. Detect and record all files that are overwritten by multiple mods.

### Steps:
- Load mod order from `<mo2_path>/profiles/<profile_name>/modlist.txt`
- Recursively walk each mod folder and collect file paths
- Track overwrites by file path
- Output JSON structure:
  ```json
  {
    "configs\\st_warfare.xml": ["modA", "modB", "modC"],
    "scripts\\sim_squad.script": ["modX", "modY"]
  }
✅ Task 02: Build Merge Workspace
Goal: For each conflicting file path, create a subfolder in merge_work/ named after the path. Inside, place one subfolder per mod that contributes that file version.

Folder structure:
merge_work/
└── configs/
    └── st_warfare.xml/
        ├── base-walo/
        │   └── st_warfare.xml
        ├── gamma_patch/
        │   └── st_warfare.xml
        └── runtime/
            └── st_warfare.xml
Steps:
For each file path in the JSON from Task 01:

Create the folder path under merge_work/<file_path>/

Copy each mod’s version of that file into a named subfolder

✅ Task 03: Merge Lua Files
Goal: Use Codex’s merge agent to generate hardened, unified versions of all .script files found in merge_work/.

Rules:
Start with the base mod version (usually base-walo/)

Apply changes from higher-priority mods if:

They prevent nil crashes

Add useful debug info (e.g. SendScriptCallback)

Harden iteration (e.g. for k,v in ipairs(list or {}))

Fix real bugs (e.g. typo, missing handler)

Output:
Save all merged Lua files to merged_output/<original_path>.

✅ Task 04: Merge .ltx and .xml Files
Goal: Use LTX/XML-specific logic to combine values from each mod into a single config file. Maintain compatibility while avoiding duplicates or unstable values.

Strategy:
Use lowest common denominator unless a fix is obvious

For spawns, timers, values: lean toward stability or base design

Consider agent support (e.g., LTXBalancer)

Output:
Save to merged_output/<original_path>

