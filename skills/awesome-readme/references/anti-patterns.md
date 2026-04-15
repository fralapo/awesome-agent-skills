# README Anti-Patterns

Things that make a README bad, ranked by how much they hurt credibility.

> Prose-level anti-patterns (AI-sounding writing, promotional adjectives, em-dash overuse, significance inflation, etc.) have their own reference: [voice-and-prose.md](voice-and-prose.md). This file focuses on structural and visual mistakes.

---

## Tier 1 — instantly disqualifying

### 1.1 Unfilled template placeholders

```md
# project_title

project_description

- [ ] Feature 1
- [ ] Feature 2
```

Shipping a README with `github_username`, `project_title`, `TODO`, or `project_description` still in it = "nobody bothered to even open the file." Immediate close tab.

**Fix:** grep for placeholder strings before push. `grep -E 'TODO|FIXME|project_title|github_username|XXX' README.md`.

### 1.2 Broken image links

```md
![Logo](images/logo.png)  ← `images/` folder doesn't exist in repo
```

Broken image = broken product, in the visitor's mind.

**Fix:** verify every `<img>` src resolves. `docs/`, `assets/`, `images/` — whichever you use, commit it.

### 1.3 Install command that doesn't work

```md
npm install mypackage   ← package not published
```

Or install command missing prereq (e.g., missing `git clone` before `npm install`), missing env var, wrong package manager.

**Fix:** copy-paste your own install steps into a clean VM/container before shipping.

### 1.4 No description of what the project is

```md
# SuperCoolProject 🚀

## Installation
npm install supercoolproject
```

User has no idea what they'd be installing. Skim past.

**Fix:** first sentence after the title must explicitly state what the thing does. "A CLI for transforming JSON into TypeScript types."

### 1.5 Obviously AI-generated prose

```md
## About

SuperCoolProject is a blazing-fast, cutting-edge library that stands as a testament to modern
software development. Nestled at the intersection of performance and elegance, it empowers
developers to seamlessly transform their workflows — ushering in a new era of productivity.
```

Reader smells slop, assumes the *project* is slop, closes tab.

**Fix:** run the anti-AI audit from [voice-and-prose.md](voice-and-prose.md) on every prose paragraph before publishing. Replace promotional adjectives with specific capabilities. Replace significance inflation with facts. Cut every trailing `-ing` clause that restates the main clause. For long-form prose, hand off to the `humanizer` skill.

---

## Tier 2 — credibility leaks

### 2.1 Badge wall

15+ badges, especially mixed styles, especially vanity badges. Signal → noise.

```md
[![Stars][]][] [![Forks][]][] [![Watchers][]][] [![Issues][]][] [![PRs][]][]
[![License][]][] [![Contributors][]][] [![Made with Love][]][] [![Open Source][]][]
[![awesome][]][] [![Maintained][]][] [![HitCount][]][] [![Discord][]][]
[![Twitter][]][] [![LinkedIn][]][] [![YouTube][]][]
```

**Fix:** cap at 8. Group: identity → health → reach → legal → social.

### 2.2 Mixed badge styles

`flat` + `for-the-badge` + `social` on the same row. Looks sloppy.

**Fix:** pick **one** style for the whole README.

### 2.3 Empty section headers

```md
## Features

## Installation

## Usage

## License
MIT
```

Reader scrolls through three empty headers to find actual content.

**Fix:** delete sections that have no content. Better: remove the header than leave it empty.

### 2.4 Placeholder content

```md
Use this space to show useful examples of how a project can be used.
Additional screenshots, code examples, and demos work well in this space.
```

Straight from Best-README-Template without replacement.

**Fix:** replace every template paragraph with your own content — or delete the section.

### 2.5 "Coming soon" sections

`## API — 🚧 Coming soon`. User thinks: "so this isn't ready."

**Fix:** don't ship the section until it's real. Hide behind `<!-- -->` HTML comment until you have content.

### 2.6 Dead external services

Badges pointing to `http://hits.dwyl.com`, discontinued analytics, etc. Broken badge image makes the whole README look abandoned.

**Fix:** audit badges quarterly. Replace dead services.

### 2.7 Outdated version numbers in prose

README says "Install v1.2.3" but `package.json` says `2.5.0`. Reader assumes the README is stale and stops reading.

**Fix:** use a shields.io version badge that auto-updates. Never hardcode versions in prose.

---

## Tier 3 — minor but common

### 3.1 Walls of text

A README is scanned, not read. Paragraph-only sections die.

**Fix:** bullets, tables, headings every 5–10 lines. Break text with code blocks, images, or `<details>`.

### 3.2 Bare code blocks

````md
```
npm install mypkg
```
````

No language tag = no syntax highlighting = looks amateur.

**Fix:** always tag the fence: `bash`, `ts`, `python`, `yaml`, `json`, `sh`, etc.

### 3.3 `$` prompt prefix in copy-paste blocks

```sh
$ npm install mypkg
$ npm run dev
```

Breaks paste — user copies the `$`.

**Fix:** omit the prompt. Use comments for annotations:

```sh
# install deps
npm install
```

### 3.4 Inline placeholders in commands

```sh
curl -H "Authorization: Bearer <YOUR_TOKEN>" https://api.example.com/v1/foo
```

Readers paste this verbatim and hit an auth error.

**Fix:** split the placeholder onto its own line with a comment:

```sh
# Replace TOKEN with your API key
export TOKEN=sk-...
curl -H "Authorization: Bearer $TOKEN" https://api.example.com/v1/foo
```

### 3.5 Over-emojied headings

```md
## 🚀✨ Installation 🎉🔥
```

Looks like a LinkedIn influencer post. One emoji max per heading, zero if the project is serious.

**Fix:** one tasteful emoji, or none. Never two.

### 3.6 Dogmatic lorem-ipsum pitches

> "A cool project that does awesome things for modern developers"

Says nothing. Reader bounces.

**Fix:** name the specific problem and the specific audience. "A CLI that converts JSON payloads into TypeScript types — for API consumers who want type safety without writing types by hand."

### 3.7 No TOC in a 500-line README

Reader can't navigate. Scrolls. Gives up.

**Fix:** add a TOC (collapsible `<details>`) once README exceeds 100 lines.

### 3.8 No demo visual in a visual project

Web app, UI library, data-viz tool with no screenshot. Missed opportunity to convert.

**Fix:** add at least one screenshot or GIF above the fold.

### 3.9 Absolute GitHub blob URLs instead of relative paths

```md
[Contributing](https://github.com/OWNER/REPO/blob/main/CONTRIBUTING.md)
```

Breaks on fork, on rename, on branch change.

**Fix:** relative path: `[Contributing](CONTRIBUTING.md)`.

### 3.10 Mixing H1s

Multiple `# Heading` instead of one H1 (the title) + H2s for sections.

**Fix:** one H1 total. Everything else `##` or deeper.

---

## Tier 4 — style nits

### 4.1 Trailing "Made with ❤️ by Author"

Fine once. Three times = desperate.

### 4.2 "If you like this, star the repo!"

Mild. Users who want to star will. Loud pleading is off-putting.

### 4.3 Animated banners that autoplay loud video

No autoplay video on open. GIFs yes (they're silent). Embedded video — don't.

### 4.4 Gigantic fonts via HTML `<font size>` hacks

```md
<font size="8">MY PROJECT</font>
```

Use Markdown headings. HTML font tags are deprecated and GitHub strips most of them.

### 4.5 Reference-style links at the top

All the `[shield-url]: https://...` definitions pushed above the prose = reader sees URL noise first.

**Fix:** put reference-style definitions at the **bottom** of the file.

---

## Quick pre-publish checklist

Structural:
- [ ] No placeholders: `grep -E 'TODO|FIXME|project_title|github_username|XXX|Lorem' README.md` is empty
- [ ] Every image loads
- [ ] Every badge URL loads
- [ ] Every internal anchor link (`#section`) resolves
- [ ] Every external link is reachable
- [ ] All code blocks language-tagged
- [ ] Install block works in a clean environment
- [ ] Version references match `package.json` / `pyproject.toml` / `Cargo.toml`
- [ ] Exactly one H1
- [ ] TOC if README > 100 lines
- [ ] Demo GIF/screenshot if project is visual
- [ ] One badge style throughout
- [ ] License section matches the `LICENSE` file

Prose (from [voice-and-prose.md](voice-and-prose.md)):
- [ ] No promotional adjectives (`blazing-fast`, `seamless`, `powerful`, `cutting-edge`, etc.)
- [ ] No significance inflation (`pivotal`, `testament to`, `stands as`, `evolving landscape`)
- [ ] No copula avoidance (`serves as`, `boasts`, `features` used in place of `is` / `has`)
- [ ] No trailing `-ing` clauses that restate the main clause
- [ ] At most one em dash per section
- [ ] No negative parallelism (`It's not just X, it's Y`)
- [ ] No generic uplift conclusions (`the future is bright`)
- [ ] No chatbot artifacts (`Of course!`, `Let me know if`, `I hope this helps`)
- [ ] Varied sentence rhythm (short and long mixed)
- [ ] At least one specific number, date, or named comparison somewhere in the prose
