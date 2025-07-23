📦 MO2MergeMagic

Automated conflict-aware folder structure generator for Mod Organizer 2 (MO2).

🚀 Overview

MO2MergeMagic parses an MO2 profile and identifies file overrides and conflicts across all installed mods. It then builds a structured workspace where each conflicting file is organized per mod, ready for AI-assisted merging and patching.

This enables:

Clear visibility into conflict sources

Easy integration with tools like ChatGPT/Codex for automated merging

Scalable workflows for massive mod packs (e.g., Skyrim, Anomaly)

⚖️ Features

Recursively scans the given MO2 profile

Detects overridden files and their originating mods

Outputs a structured tree like:

merge_workspace/
└── scripts/st_warfare.lua/
    ├── OldWALO/scripts/st_warfare.lua
    └── GammaPatch/scripts/st_warfare.lua

Each mod’s version of a conflicting file is copied into its own subfolder under the file’s name.

⚙️ Quick Start

# Clone the repository
git clone https://github.com/d0pe1/MO2MergeMagic.git
cd MO2MergeMagic

# Install dependencies
pip install -r requirements.txt

# Run the tool
python mo2_merge_magic.py \
  --mo2-profile "/absolute/path/to/MO2/profiles/YourProfile" \
  --output "merge_workspace"

🧠 Codex Integration

After running the tool, you’ll have a clean structure of conflicting files per mod. From here, Codex or GPT agents can:

Read each subfolder

Compare and merge files safely

Add bugfixes, nil checks, logging, etc.

Output a single final merged file per conflict

Prompt example:“Merge the versions of scripts/st_warfare.lua from each subfolder into one final version, maintaining original logic but applying stability and debug enhancements.”

🚣️ Roadmap

✅ MO2 profile parser

✅ Conflict detection + structure builder

🛠️ Codex merge automation scripts

🛠️ Skyrim ESP/ESM to JSON converter

🛠️ AI-guided balance patch generator

🛠️ In-place mod injector for merged output

🧰 Project Structure

├── mo2_merge_magic.py       # Core logic
├── requirements.txt         # Python deps
├── README.md                # This file
└── ai_merge_agent/          # (planned) Codex helper scripts

📜 License

MIT — use freely, mod wisely, and may the Zone be kind.

🧪 Author

Maintained by @d0pe1AI Whisperer: GPT-4o + Codex

