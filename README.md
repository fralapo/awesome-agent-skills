<a id="readme-top"></a>

<h1 align="center">awesome-agent-skills</h1>

<p align="center">
  A small, opinionated set of <a href="https://docs.claude.com/en/docs/claude-code/skills">Claude Code skills</a> I actually use.
  Each one is mined from a corpus of 200+ real community examples, not generated from scratch.
</p>

<p align="center">
  <a href="https://github.com/fralapo/awesome-agent-skills/stargazers"><img src="https://img.shields.io/github/stars/fralapo/awesome-agent-skills?style=for-the-badge" alt="Stars"></a>
  <a href="https://github.com/fralapo/awesome-agent-skills/commits/main"><img src="https://img.shields.io/github/last-commit/fralapo/awesome-agent-skills?style=for-the-badge" alt="Last commit"></a>
  <img src="https://img.shields.io/badge/skills-3-2ea44f?style=for-the-badge" alt="Skills count">
  <img src="https://img.shields.io/badge/Claude%20Code-compatible-5A67D8?style=for-the-badge" alt="Claude Code compatible">
  <a href="LICENSE"><img src="https://img.shields.io/github/license/fralapo/awesome-agent-skills?style=for-the-badge" alt="License"></a>
</p>

---

## What's in here

Three skills. Each is a single folder with a `SKILL.md` (frontmatter + workflow) plus a `references/` directory for deep-dive material. Claude Code matches the `description` field against whatever you're asking, and loads the skill only when it's relevant. No eager bloat.

| Skill | What it does | Corpus mined | Typical trigger |
|---|---|---|---|
| [`seedance-prompts`](./skills/seedance-prompts/) | Prompt templates for **ByteDance Seedance 2.0** video generation. Timecoded 3-shot storyboards, camera-move vocab, 15 category templates, multi-modal references (`@图片`/`@视频`/`@audio`), 12 curated examples. | ~195 prompts across 3 awesome-lists | `seedance`, `bytedance video`, `text-to-video prompt` |
| [`nano-banana-prompts`](./skills/nano-banana-prompts/) | Prompt templates for **Google Nano Banana** and **Nano Banana Pro** (Gemini 2.5 Flash Image). Two-tier model guidance, 15 fill-in templates (headshot, bento infographic, 3D diorama, split-view render), identity-preservation ranking, structured JSON/YAML/XML shapes, text-in-image rendering, 15 worked examples. | ~600 prompts across 5 awesome-lists | `nano banana`, `gemini 2.5 flash image`, `gemini image gen` |
| [`awesome-readme`](./skills/awesome-readme/) | Write GitHub READMEs that land on awesome-lists and still sound human. 8 full templates (library/CLI/webapp/desktop/research/template-repo/monorepo/profile), shields.io badge library, banner/logo/GIF recipes, profile-README widget catalog, anti-patterns, and a dedicated anti-AI-slop audit pass integrating the `humanizer` skill's Wikipedia *Signs of AI writing* patterns. | Best-README-Template + ~100 awesome-readme entries + Standard-Readme + Make-a-README + RDD essay | `readme`, `awesome readme`, `github readme`, `humanize readme` |

More coming when I build one that earns its place. I'd rather ship three that work than twenty that almost do.

---

## Install

Pick one. Replace `<skill>` with the skill name (`seedance-prompts`, `nano-banana-prompts`, or `awesome-readme`).

### Symlink one skill (recommended — updates follow `git pull`)

**macOS / Linux:**
```sh
git clone https://github.com/fralapo/awesome-agent-skills.git ~/src/awesome-agent-skills
ln -s ~/src/awesome-agent-skills/skills/<skill> ~/.claude/skills/<skill>
```

**Windows (PowerShell, admin or developer mode):**
```powershell
git clone https://github.com/fralapo/awesome-agent-skills.git $env:USERPROFILE\src\awesome-agent-skills
New-Item -ItemType SymbolicLink `
  -Path "$env:USERPROFILE\.claude\skills\<skill>" `
  -Target "$env:USERPROFILE\src\awesome-agent-skills\skills\<skill>"
```

### Copy (static snapshot, no auto-update)

**macOS / Linux:**
```sh
git clone https://github.com/fralapo/awesome-agent-skills.git
cp -r awesome-agent-skills/skills/<skill> ~/.claude/skills/
```

**Windows:**
```powershell
git clone https://github.com/fralapo/awesome-agent-skills.git
xcopy /E /I awesome-agent-skills\skills\<skill> $env:USERPROFILE\.claude\skills\<skill>
```

### Symlink every skill at once (macOS / Linux)

```sh
git clone https://github.com/fralapo/awesome-agent-skills.git ~/src/awesome-agent-skills
for d in ~/src/awesome-agent-skills/skills/*/; do
  ln -s "$d" ~/.claude/skills/
done
```

Restart Claude Code after install. Skills load at startup.

---

## How a skill is organized

```
skills/<skill-name>/
├── SKILL.md              # required — frontmatter (name, description) + workflow
└── references/           # optional — deep-dive files loaded only when relevant
    ├── patterns.md
    ├── templates.md
    └── examples.md
```

The frontmatter `description` field is the matcher. Keep it specific and keyword-dense; Claude Code uses it to decide whether to load the skill at all.

---

## How I build them

The pattern is consistent across all three skills in this repo:

1. **Mine a real corpus.** Community awesome-lists, vendor docs, internal notes. Several hundred examples minimum. I don't write skills from imagination.
2. **Cluster what actually recurs.** Templates, anti-patterns, category-specific moves. Things a real prompter or writer reaches for ten times a week.
3. **Write `SKILL.md` short.** Frontmatter, when-to-use, quick rules, pointers into references. The agent reads this at load time; every extra paragraph costs context.
4. **Push depth into `references/`.** Topical files. Loaded on demand when the agent follows a link.
5. **Cite sources.** When a template or pattern came from a specific public repo, it gets named in `examples.md` or the frontmatter `analyzed_repos` list.

If you're writing your own Claude Code skills, those five steps are the only ones that have mattered for me. Everything else is decoration.

---

## Contributing

Personal repo, but useful PRs get in. The bar:

- **New skill:** must match the structure above and cite its corpus
- **Skill improvement:** cite the specific pattern that motivated the change
- **Bug fix:** the smallest diff that fixes the thing

Open an issue before a large PR so neither of us wastes time.

---

## License

[MIT](LICENSE).

<p align="right">(<a href="#readme-top">back to top</a>)</p>
