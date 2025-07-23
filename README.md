MO2MergeMagic

💡 Merge Patcher of Doom (Codex-Powered Mod Conflict Resolver)

A Codex-assisted Lua/LTX/XML mod conflict resolver designed for STALKER: Anomaly (G.A.M.M.A.), with future expansion plans for Skyrim. This tool parses Mod Organizer 2 (MO2) profiles, extracts all conflicting files, and generates a merge-ready file structure for AI-assisted patching.

🚀 Purpose

When modpacks grow into hundreds of layered modifications, conflicts become inevitable. Manual resolution is slow, error-prone, and exhausting.

This project aims to:

Extract the entire conflict tree from a MO2 profile.

Build structured folders containing all conflicting file versions.

Feed these folders into Codex agents to merge, harden, and unify the mods.

Output a fully merged patch layer, automatically.

🛠️ Input

You must provide:

--mo2-path: The absolute path to the Mod Organizer 2 root folder.

--profile: The name of the MO2 profile you want to analyze (inside profiles/).

📄 Output

A new merge_work/ folder will be created, containing one folder per mod that contributes to a conflicting file:

merge_work/
└── gamedata/
    └── configs/
        └── st_warfare.xml/
            ├── base-walo/
            │   └── st_warfare.xml
            ├── gamma_patch/
            │   └── st_warfare.xml
            └── runtime/
                └── st_warfare.xml

Each file is copied from its source mod with a prefix indicating its load order in MO2.

Codex can then be instructed to:

"For each folder, merge files in numerical order into a unified patch, keeping logic intact but applying nil-guards, debug logging, and other stability improvements."

🧐 Codex Prompt

Once generated, simply instruct Codex:

Read the README. Perform the task as described:
- For each subfolder in `merge_work/`, merge numbered files into `merged_output/`, using best practices and bugfix hardening logic.
- Maintain original behavior where possible.
- Apply nil guards, safe iteration (`ipairs`), debug logs, and comment all changes.
- Output one final merged file per folder.

You can add more specific guidance via agents.md if needed.

🚣️ Roadmap



🫠 Skill Domains

Lua 5.1 / LTX / XML scripting

Mod Organizer 2 internals

Codex agent orchestration

Conflict resolution logic

Git-based modpack patch management

🦖 Future Extensions

LTX stat rebalance agents

Artifact spawn tuning

Smart AI combat behavior mergers

Skyrim ESP/ESM + Papyrus merge pipelines

In-game runtime crash log linkers

🧪 Credits

Project lead: @d0pe1AI Architect: Codex + GPT-4o, harnessed like a damn daemon.License: MIT
