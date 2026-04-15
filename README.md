# agent-skills

Personal collection of **Claude Code skills** — curated, production-grade, ready to drop into any `~/.claude/skills/` directory.

Each skill is a self-contained folder with a `SKILL.md` (frontmatter-declared trigger + workflow) and optional `references/` for deep-dive material. Claude Code auto-loads the skill when its `description` matches the task at hand.

## Skills in this repo

| Skill | What it does | Trigger keywords |
|-------|-------------|------------------|
| [`seedance-prompts`](./skills/seedance-prompts/) | Write production-grade prompts for **ByteDance Seedance 2.0** video generation — 3-shot timecoded storyboards, multi-modal references (`@图片`/`@视频`/`@audio`), 15 category templates, full camera/lens/lighting vocab, 12 curated working examples. Built from 195+ prompts across 3 awesome-lists. | `seedance`, `seedance 2.0`, `bytedance video`, `text-to-video prompt` |
| [`nano-banana-prompts`](./skills/nano-banana-prompts/) | Write production-grade prompts for **Google Nano Banana** (Gemini 2.5 Flash Image) and **Nano Banana Pro** image generation/editing — two-tier model guidance, 15 fill-in templates (headshot, bento infographic, 3D diorama, split-view render, etc.), identity-preservation ranking, structured JSON/YAML/XML prompt shapes, text-in-image rendering, 15 curated working examples. Built from ~600 prompts across 5 awesome-lists. | `nano banana`, `nano banana pro`, `gemini 2.5 flash image`, `gemini image gen` |

More skills coming.

## Install

Replace `<skill-name>` below with the skill you want (e.g. `seedance-prompts` or `nano-banana-prompts`).

### Option 1 — symlink a single skill (recommended, auto-updates on `git pull`)

```bash
# Windows (PowerShell as admin)
New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.claude\skills\<skill-name>" -Target "$PWD\skills\<skill-name>"

# macOS / Linux
ln -s "$PWD/skills/<skill-name>" ~/.claude/skills/<skill-name>
```

### Option 2 — copy (static snapshot)

```bash
# Windows
xcopy /E /I skills\<skill-name> %USERPROFILE%\.claude\skills\<skill-name>

# macOS / Linux
cp -r skills/<skill-name> ~/.claude/skills/
```

### Option 3 — clone the whole thing and symlink every skill

```bash
git clone https://github.com/fralapo/agent-skills.git ~/src/agent-skills

# macOS / Linux — symlink all skills at once
for d in ~/src/agent-skills/skills/*/; do
  ln -s "$d" ~/.claude/skills/
done
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

### Typical authoring flow

1. Mine a corpus (community awesome-lists, docs, internal prompts) for recurring patterns.
2. Draft `SKILL.md` — frontmatter + short overview + quick rules. Keep it short; push detail into `references/`.
3. Split deep material into topical reference files (`patterns.md`, `templates.md`, `examples.md`, etc.).
4. Cite sources in `examples.md` when reproducing community prompts.

## Contributing

Personal repo. Additions follow the structural conventions above.

## License

MIT — see [LICENSE](./LICENSE).
