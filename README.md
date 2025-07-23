# 💀 Merge Patcher of Doom

**Codex-Powered Mod Conflict Resolver for STALKER: Anomaly (G.A.M.M.A.)**

> Automate the extraction, structuring, and intelligent merging of Mod Organizer 2 (MO2) mod conflicts. Built for Lua, LTX, XML — designed for extensibility (Skyrim, Fallout, etc.).

---

## 🚀 What This Does

When your modpack grows to 500+ mods, manual patching becomes hell. This tool makes it sane.

- Scans a MO2 instance and profile for file conflicts
- Extracts each conflicting file into a structured folder layout
- Copies all mod-contributed versions of that file into one place
- Prepares the entire layout for AI-assisted merge resolution using OpenAI Codex or GPT

Result: A fully structured, ready-to-merge patch workspace.

---

## 🔧 Input

### Required Parameters:
- `--mo2-path`: Absolute path to the Mod Organizer 2 root directory
- `--profile`: The name of the MO2 profile (inside `profiles/`)

---

## 📁 Output

A `merge_work/` folder is generated.

For each conflicting file in the virtual file system (VFS), a subfolder is created. Inside that folder are subfolders named after each mod that contributes a version of the file.

Example:

merge_work/
└── gamedata/
└── configs/
└── st_warfare.xml/
├── base-walo/
│ └── st_warfare.xml
├── gamma_patch/
│ └── st_warfare.xml
└── runtime/
└── st_warfare.xml

yaml
Copy
Edit

This format makes it trivial for AI agents or developers to inspect, diff, and intelligently merge changes.

---

## 🧠 How To Use With Codex

Once your workspace is built, you can prompt Codex (or any LLM dev agent):

Read each folder in merge_work/.
For each conflicting file:

Merge all versions from subfolders (sorted by mod load order)

Preserve core logic unless stability improvements are obvious

Apply nil guards, debug traces, safe iteration (ipairs), and function assertions

Output the final merged file in merged_output/

yaml
Copy
Edit

Want to go wild? Write `agents.md` to define LLM personas with domain logic (e.g. "AI Combat Tuner", "XML Weapon Balance Agent", "LTX Merge Sentinel").

---

## 🛠️ Stack

- **Python 3.10+**
- MO2 VFS resolver
- Lua 5.1 / LTX / XML support
- Optional: Codex API or OpenAI CLI + `agents.md`

---

## 🧩 Use Cases

- STALKER Anomaly / GAMMA mod conflict resolution
- Auto-patching weapon/AI/stat rebalance mods
- Porting Warfare mode into Story mode safely
- Skyrim/Fallout ESP/ESM merges (via future JSON decompiler integration)
- Auto-generating `mod_patch.esm` or `patch_ltx.script` from 500 mods

---

## 🧠 Agent Ideas

- `LuaMergeAgent`: Merges `*.script` files with logic trace safety
- `LTXBalancer`: Analyzes spawn/weapons/config values and merges intelligently
- `SkyrimMergeBot`: Future ESP/ESM AI patcher for load orders
- `CrashFixDaemon`: Adds nil guards and logs to lifecycle points
- `StoryWarfareBridge`: Enables running warfare + story seamlessly

---

## 🧪 Roadmap

- [x] Lua/LTX/XML STALKER merge support
- [ ] Skyrim ESP/ESM merge via JSON decomp pipeline
- [ ] Profile-aware auto-refactor system
- [ ] Fully AI-driven modset autopatcher
- [ ] Web GUI frontend

---

## 🧬 Credits

- 🧠 Project Lead: [@d0pe1](https://github.com/d0pe1)  
- 🤖 AI Architect: Codex + GPT-4o  
- 🔓 License: MIT

---

> The days of dragging files in Windows Explorer are over. Merge your mods like a god.
