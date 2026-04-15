# Annotated Examples

Concrete excerpts from the best-in-class READMEs collected by [matiassingers/awesome-readme](https://github.com/matiassingers/awesome-readme). Each one teaches a specific move you can lift into your own README.

Credits: all examples are cited with their source repo. Excerpts reproduced for study.

---

## Example 1 — [choojs/choo](https://github.com/choojs/choo)

**Move:** *Menu above the fold with useful links + FAQ*

```md
# choo

- [Website](https://choo.io)
- [Handbook](https://handbook.choo.io)
- [Discuss on GitHub](https://github.com/choojs/choo/discussions)
- [Discord](https://discord.gg/...)

### FAQ

<details><summary>Why "choo"?</summary>
Because it's fun to say.
</details>
```

**Why it works:** a user lands, sees four specific places they can go, plus answers to common early questions *before* scrolling. Converts first-time visitors into evaluators instead of bouncers.

---

## Example 2 — [PostHog/posthog](https://github.com/PostHog/posthog)

**Move:** *Custom-made section icons + deploy button*

```md
<h3>🧬 Why PostHog?</h3>

<h3>🚀 Quick Start</h3>

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/PostHog/posthog)
```

**Why it works:** section icons are *custom* (not random emojis) and repeat consistently, giving the README its own visual vocabulary. The one-click deploy button is the highest-converting CTA on a web-app README.

---

## Example 3 — [sindresorhus/pageres](https://github.com/sindresorhus/pageres)

**Move:** *Demo screenshot in the first viewport*

```md
# pageres

Capture screenshots of websites in various resolutions.

<img src="screenshot.gif" width="728">

[![Build](https://img.shields.io/.../build)](...)
[![npm](https://img.shields.io/npm/v/pageres)](...)
```

**Why it works:** the GIF shows the actual output of the tool in the first seconds. The reader understands what the tool *produces* without reading a word.

---

## Example 4 — [httpie/httpie](https://github.com/httpie/httpie)

**Move:** *TOC pointing to both "how to" and "why"*

```md
<details>
<summary>Table of Contents</summary>

- [About](#about)
- [Quick Start](#quick-start)
- [Features](#features)
- [Community & Support](#community--support)
- [Contributing](#contributing)
- [Philosophy](#philosophy)

</details>
```

**Why it works:** includes a **Philosophy** section and surfaces it in the TOC. Opinionated projects that explain *why* get stars; neutral tool descriptions don't.

---

## Example 5 — [release-it/release-it](https://github.com/release-it/release-it)

**Move:** *Animated GIF + expandable TOC*

```md
# release-it

<img src="./docs/assets/release-it.gif" width="100%">

<details>
<summary>Table of Contents</summary>
...
</details>
```

**Why it works:** demo GIF is the entire width of the README, pinned under the title. TOC is collapsed so the GIF stays above the fold.

---

## Example 6 — [sourcerer-io/sourcerer-app](https://github.com/sourcerer-io/sourcerer-app)

**Move:** *Customized call-to-action badge*

```md
[![Sign up](https://img.shields.io/badge/Sign_up-free-ff69b4.svg?style=for-the-badge)](https://sourcerer.io)
```

**Why it works:** one large, visually distinct badge acts as the primary CTA. Doesn't compete with the health/version badges.

---

## Example 7 — [amplication/amplication](https://github.com/amplication/amplication)

**Move:** *Contributor pictures + feature walkthrough*

```md
## Contributors

<a href="https://github.com/amplication/amplication/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=amplication/amplication" />
</a>
```

**Why it works:** the avatar mosaic is social proof: *this is not a one-person project*. Uses zero maintenance — `contrib.rocks` regenerates itself.

---

## Example 8 — [Day8/re-frame](https://github.com/Day8/re-frame)

**Move:** *Long-form essay README*

A 5,000-word README explaining the philosophy, architecture, history, and ecosystem of the library.

**Why it works:** for opinionated technical tools, a long README *is* the sales pitch. Every section links deep into the thinking. Risky — only works when the content is genuinely interesting.

---

## Example 9 — [brenocq/implot3d](https://github.com/brenocq/implot3d)

**Move:** *Dynamic roadmap SVG fed by GitHub Discussions*

```md
<img src="https://implot3d-roadmap.example.com/roadmap.svg" alt="Roadmap">
```

**Why it works:** roadmap updates itself from live discussion data. Reader trusts the roadmap is current (because it is). Requires a custom GitHub Action but pays dividends on projects with active feature requests.

---

## Example 10 — [refinedev/refine](https://github.com/refinedev/refine)

**Move:** *Multi-screenshot grid showing product capabilities*

```md
<table>
  <tr>
    <td><img src="docs/1.png" alt="Dashboard"></td>
    <td><img src="docs/2.png" alt="Form"></td>
  </tr>
  <tr>
    <td><img src="docs/3.png" alt="Table"></td>
    <td><img src="docs/4.png" alt="Auth"></td>
  </tr>
</table>
```

**Why it works:** for meta-frameworks / boilerplates / UI toolkits, a grid of screenshots showing the *range* of what you can build is more persuasive than one hero image.

---

## Example 11 — [iterative/dvc](https://github.com/iterative/dvc)

**Move:** *Hall-of-fame contribution section*

```md
## Contributors

[![Contribute](https://opencollective.com/dvc/tiers/backer.svg?avatarHeight=32)](https://opencollective.com/dvc)
```

**Why it works:** uses Open Collective / Hall-of-fame widget to recognize contributors. Makes contributing feel appreciated = more contributors.

---

## Example 12 — [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)

**Move:** *Super-clear description friendly to newcomers*

```md
# dbt

**dbt** enables data analysts and engineers to transform their data using
the same practices that software engineers use to build applications.
```

**Why it works:** avoids jargon ("materialized views", "DAG orchestration", "SQL transformation framework"). Anchors to what software engineers already know. Friendly to readers *outside* the existing data community.

---

## Example 13 — [Platane/snk](https://github.com/Platane/snk) (profile README widget)

**Move:** *Contribution snake animation*

```md
<picture>
  <source media="(prefers-color-scheme: dark)" srcset=".../snake-dark.svg">
  <img alt="snake" src=".../snake.svg">
</picture>
```

**Why it works:** visual delight — the contribution graph turns into a playable snake game that eats the green squares. Memorable. Users screenshot and share.

---

## Example 14 — [yvann-ba/ft_transcendence](https://github.com/yvann-ba/ft_transcendence)

**Move:** *Minimalist banner + GIF gallery in table layout + team section with avatars*

```md
<p align="center"><img src="banner.png"></p>

<table>
  <tr><td><img src="gif-1.gif"></td><td><img src="gif-2.gif"></td></tr>
</table>

### Team

| <a href="https://github.com/user-a"><img src="https://github.com/user-a.png" width="80"></a> | <a href="https://github.com/user-b"><img src="https://github.com/user-b.png" width="80"></a> |
|:-:|:-:|
| User A | User B |
```

**Why it works:** school/team projects benefit from visible teammate credit. The GIF grid is ideal for gameplay/animation demos. Clean, humble, specific.

---

## Example 15 — [gofiber/fiber](https://github.com/gofiber/fiber)

**Move:** *Language switcher + benchmarks + hide-long-code `<details>`*

```md
<p align="center">
  <a href="README.md">🇺🇸</a>
  <a href="README_fr.md">🇫🇷</a>
  <a href="README_es.md">🇪🇸</a>
  ...
</p>

<details>
<summary>Example: middleware chaining (click to expand)</summary>

```go
// ... 60 lines of code ...
```

</details>
```

**Why it works:** flags = instant i18n signal. Long code examples hidden behind `<details>` keep the README scannable while giving depth-seekers what they want.

---

## Lessons condensed

| Move | When to use |
|---|---|
| Menu above the fold | Project has multiple URLs (docs, demo, discord) |
| Custom section icons | Project has distinct visual identity |
| First-viewport demo GIF | Visual / CLI / UI-heavy project |
| Philosophy section | Opinionated framework or tool |
| One big CTA badge | Hosted / SaaS project with a signup |
| `contrib.rocks` avatars | Project has 3+ contributors |
| Long-form essay README | Thought-leadership project |
| Dynamic roadmap | Project with active feature requests |
| Multi-screenshot grid | UI toolkit / boilerplate / meta-framework |
| Contribution snake | Profile README |
| Language switcher | International / large user base |
| `<details>` for long code | Project with deep API surface |

---

## How to use this reference

When drafting a README:

1. Identify the project type from [templates.md](templates.md)
2. Pick 2–4 moves from this list that fit the project
3. Integrate them — don't just bolt them on
4. Verify each works in GitHub preview (anchors, images, badges)
