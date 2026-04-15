# agent-skills

Personal collection of **Claude Code skills** — curated, production-grade, ready to drop into any `~/.claude/skills/` directory.

Each skill is a self-contained folder with a `SKILL.md` (frontmatter-declared trigger + workflow) and optional `references/` for deep-dive material. Claude Code auto-loads the skill when its description matches the task at hand.

## Skills in this repo

| Skill | What it does | Trigger keywords |
|-------|-------------|------------------|
| [`seedance-prompts`](./skills/seedance-prompts/) | Write production-grade prompts for ByteDance Seedance 2.0 video generation — 3-shot timecoded storyboards, multi-modal references (`@图片`/`@视频`/`@audio`), 15 category templates, full camera/lens/lighting vocab, 12 curated working examples. Built from 195+ prompts across 3 awesome-lists. | `seedance`, `seedance 2.0`, `bytedance video`, `text-to-video prompt` |
| [`nano-banana-prompts`](./skills/nano-banana-prompts/) | Write production-grade prompts for Google Nano Banana (Gemini 2.5 Flash Image) and Nano Banana Pro image generation/editing — two-tier model guidance, 15 fill-in templates (headshot, bento infographic, 3D diorama, split-view render, etc.), identity-preservation ranking, structured JSON/YAML/XML prompt shapes, text-in-image rendering, 15 curated working examples. Built from ~600 prompts across 5 awesome-lists. | `nano banana`, `nano banana pro`, `gemini 2.5 flash image`, `gemini image gen` |

More skills coming.

## Install

### Option 1 — symlink a single skill (recommended, auto-updates on `git pull`)

```bash
# Windows (PowerShell as admin)
New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.claude\skills\seedance-prompts" -Target "$PWD\skills\seedance-prompts"

# macOS / Linux
ln -s "$PWD/skills/seedance-prompts" ~/.claude/skills/seedance-prompts
```

### Option 2 — copy (static snapshot)

```bash
# Windows
xcopy /E /I skills\seedance-prompts %USERPROFILE%\.claude\skills\seedance-prompts

# macOS / Linux
cp -r skills/seedance-prompts ~/.claude/skills/
```

### Option 3 — clone the whole thing into your skills root

```bash
cd ~/.claude/skills
git clone https://github.com/<your-handle>/agent-skills.git
# then move or symlink the skills/* subfolders up one level
```

## Anatomy of a skill

```
skills/<skill-name>/
├── SKILL.md              # required — frontmatter (name, description) + workflow
└── references/           # optional — deep-dive material loaded on demand
    ├── patterns.md
    ├── templates.md
    └── examples.md
```

The `description` field in the frontmatter is what Claude Code matches against user intent — keep it specific and keyword-rich.

## Contributing

Personal repo. Additions follow the structural conventions above.

## License

MIT — see [LICENSE](./LICENSE).
