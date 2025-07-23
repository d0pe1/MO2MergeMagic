# 🧠 MO2MergeMagic

> Automated, conflict-aware folder structure generator for **Mod Organizer 2 (MO2)** profiles.  
> Built for **STALKER Anomaly, Skyrim, Fallout,** and other modding hellscapes.

---

## 🚀 What It Does

MO2MergeMagic parses a given MO2 profile, identifies conflicting files across mods, and exports a neatly organized workspace.  
Each conflicting file is placed into its own folder — with subfolders per mod that contains a version of that file.  
This lets you compare, merge, and resolve conflicts with AI (e.g., ChatGPT / Codex) or by hand — fast.

---

## 🧩 Why This Exists

Mod conflict hell is real.

This tool makes it **visible, structured, and patchable.**

Perfect for:
- 🛠 Building final merged patches for massive load orders
- 🤖 AI-assisted merging (Codex/GPT agents)
- 🔍 Debugging file overrides
- 💥 Surviving G.A.M.M.A., Requiem, or 400+ mod Frankenstein installs

---

## 🧪 Features

- Recursively scans an MO2 profile
- Detects all conflicting files across enabled mods
- Creates a merge workspace like this:

```
merge_workspace/
└── scripts/st_warfare.lua/
    ├── OldWALO/scripts/st_warfare.lua
    └── GammaPatch/scripts/st_warfare.lua
```

---

## ⚙️ How to Use

### 1. Clone the Repo

```bash
git clone https://github.com/d0pe1/MO2MergeMagic.git
cd MO2MergeMagic
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Tool

```bash
python mo2_merge_magic.py \
  --mo2-profile "/absolute/path/to/MO2/profiles/YourProfile" \
  --output "merge_workspace"
```

---

## 🧠 Codex/GPT Workflow

Once the merge workspace is generated:

- Each conflict is isolated in its own folder
- Each mod’s version lives in a separate subfolder
- GPT/Codex agents can:
  - Analyze all versions
  - Merge or rewrite files with logging, fixes, etc.
  - Output a final clean `.lua`, `.ini`, `.xml`, `.txt`, or whatever

Use it as a base for an auto-patching pipeline or AI merge assistant.

---

## 📂 Project Structure

```
MO2MergeMagic/
├── merge_magic/              # Core logic
├── mo2_merge_magic.py        # CLI entry point
├── codex.md                  # Codex prompt templates (optional)
├── README.md
├── pyproject.toml
└── requirements.txt
```

---

## 🧊 Status

> Prototype-quality — works for STALKER Anomaly and similar flat folder structures.  
> Skyrim & Fallout support coming soon. Patches welcome.

---

## 📜 License

MIT. Use, fork, build, AI-patch the planet.

---

## 🙋‍♂️ Author

Nico / `d0pe1` — 🧪 IT DevOps | 🧬 Chaos Gardener | 🛠 Modding Sadist
