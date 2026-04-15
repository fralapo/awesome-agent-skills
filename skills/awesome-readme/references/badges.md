# Badge Library (shields.io)

Copy-paste ready. Replace `OWNER/REPO`, package names, and placeholders.

All badges use the `shields.io` service. Style options: `flat` (default), `flat-square`, `plastic`, `for-the-badge`, `social`. Pick **one** style and stick with it across the README.

> Rule: **5–8 badges max**. Group them: identity → health → reach → legal → social.

---

## Badge style selector

| Style | Best for |
|---|---|
| `flat` | Default, understated |
| `flat-square` | Cleaner corners, grid-friendly |
| `for-the-badge` | Big, loud, modern projects |
| `plastic` | Retro, 3D sheen |
| `social` | GitHub social metrics (stars/forks) |

Append as `?style=for-the-badge` to any badge URL.

---

## 1. Identity

### Version (npm)
```md
[![npm version](https://img.shields.io/npm/v/PACKAGE?style=for-the-badge)](https://www.npmjs.com/package/PACKAGE)
```

### Version (PyPI)
```md
[![PyPI version](https://img.shields.io/pypi/v/PACKAGE?style=for-the-badge)](https://pypi.org/project/PACKAGE/)
```

### Version (Cargo)
```md
[![Crates.io](https://img.shields.io/crates/v/CRATE?style=for-the-badge)](https://crates.io/crates/CRATE)
```

### Version (Go)
```md
[![Go Reference](https://pkg.go.dev/badge/github.com/OWNER/REPO.svg)](https://pkg.go.dev/github.com/OWNER/REPO)
```

### Version (GitHub release)
```md
[![Release](https://img.shields.io/github/v/release/OWNER/REPO?style=for-the-badge)](https://github.com/OWNER/REPO/releases/latest)
```

### Version (Maven Central)
```md
[![Maven Central](https://img.shields.io/maven-central/v/GROUP/ARTIFACT?style=for-the-badge)](https://central.sonatype.com/artifact/GROUP/ARTIFACT)
```

### Version (Docker Hub)
```md
[![Docker](https://img.shields.io/docker/v/USER/IMAGE?style=for-the-badge)](https://hub.docker.com/r/USER/IMAGE)
```

---

## 2. Health

### CI — GitHub Actions workflow
```md
[![CI](https://img.shields.io/github/actions/workflow/status/OWNER/REPO/ci.yml?branch=main&style=for-the-badge)](https://github.com/OWNER/REPO/actions/workflows/ci.yml)
```

### Coverage — Codecov
```md
[![Coverage](https://img.shields.io/codecov/c/github/OWNER/REPO?style=for-the-badge)](https://codecov.io/gh/OWNER/REPO)
```

### Coverage — Coveralls
```md
[![Coverage](https://img.shields.io/coveralls/github/OWNER/REPO?style=for-the-badge)](https://coveralls.io/github/OWNER/REPO)
```

### Code quality — Codacy
```md
[![Codacy](https://img.shields.io/codacy/grade/TOKEN?style=for-the-badge)](https://www.codacy.com/gh/OWNER/REPO)
```

### Bundle size (Bundlephobia — npm)
```md
[![Bundle size](https://img.shields.io/bundlephobia/minzip/PACKAGE?style=for-the-badge)](https://bundlephobia.com/package/PACKAGE)
```

### Known vulnerabilities (Snyk)
```md
[![Snyk](https://snyk.io/test/github/OWNER/REPO/badge.svg)](https://snyk.io/test/github/OWNER/REPO)
```

### Last commit
```md
[![Last commit](https://img.shields.io/github/last-commit/OWNER/REPO?style=for-the-badge)](https://github.com/OWNER/REPO/commits/main)
```

### Commit activity
```md
[![Commits/month](https://img.shields.io/github/commit-activity/m/OWNER/REPO?style=for-the-badge)](https://github.com/OWNER/REPO/pulse)
```

---

## 3. Reach

### Downloads — npm
```md
[![npm downloads](https://img.shields.io/npm/dm/PACKAGE?style=for-the-badge)](https://www.npmjs.com/package/PACKAGE)
```

### Downloads — PyPI
```md
[![PyPI downloads](https://img.shields.io/pypi/dm/PACKAGE?style=for-the-badge)](https://pypi.org/project/PACKAGE/)
```

### Downloads — GitHub releases
```md
[![Downloads](https://img.shields.io/github/downloads/OWNER/REPO/total?style=for-the-badge)](https://github.com/OWNER/REPO/releases)
```

### Stars
```md
[![Stars](https://img.shields.io/github/stars/OWNER/REPO?style=for-the-badge)](https://github.com/OWNER/REPO/stargazers)
```

### Forks
```md
[![Forks](https://img.shields.io/github/forks/OWNER/REPO?style=for-the-badge)](https://github.com/OWNER/REPO/network/members)
```

### Issues / PRs
```md
[![Issues](https://img.shields.io/github/issues/OWNER/REPO?style=for-the-badge)](https://github.com/OWNER/REPO/issues)
[![PRs](https://img.shields.io/github/issues-pr/OWNER/REPO?style=for-the-badge)](https://github.com/OWNER/REPO/pulls)
```

### Contributors
```md
[![Contributors](https://img.shields.io/github/contributors/OWNER/REPO?style=for-the-badge)](https://github.com/OWNER/REPO/graphs/contributors)
```

---

## 4. Legal

### License (auto-detect)
```md
[![License](https://img.shields.io/github/license/OWNER/REPO?style=for-the-badge)](LICENSE)
```

### License (explicit)
```md
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue?style=for-the-badge)](https://opensource.org/licenses/Apache-2.0)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue?style=for-the-badge)](https://www.gnu.org/licenses/gpl-3.0)
```

### Conventional Commits
```md
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow?style=for-the-badge)](https://conventionalcommits.org)
```

### Semantic Versioning
```md
[![semver](https://img.shields.io/badge/semver-2.0.0-blue?style=for-the-badge)](https://semver.org)
```

---

## 5. Social

### Twitter / X follow
```md
[![Twitter](https://img.shields.io/twitter/follow/HANDLE?style=social)](https://twitter.com/HANDLE)
```

### Discord
```md
[![Discord](https://img.shields.io/discord/SERVER_ID?label=chat&logo=discord&style=for-the-badge)](https://discord.gg/INVITE)
```

### Mastodon
```md
[![Mastodon](https://img.shields.io/mastodon/follow/USERID?domain=https%3A%2F%2FINSTANCE&style=for-the-badge)](https://INSTANCE/@HANDLE)
```

### LinkedIn
```md
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/HANDLE)
```

### Sponsors
```md
[![Sponsors](https://img.shields.io/github/sponsors/OWNER?style=for-the-badge)](https://github.com/sponsors/OWNER)
```

---

## 6. Tech-stack badges ("Built With")

Static badges with official logos. Use these under "Built With".

```md
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)
![Deno](https://img.shields.io/badge/Deno-000000?style=for-the-badge&logo=deno&logoColor=white)
![Bun](https://img.shields.io/badge/Bun-000000?style=for-the-badge&logo=bun&logoColor=white)

![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)
![Vue](https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D)
![Svelte](https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00)
![Astro](https://img.shields.io/badge/Astro-BC52EE?style=for-the-badge&logo=astro&logoColor=white)

![Tailwind CSS](https://img.shields.io/badge/Tailwind-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
```

Full list: [simple-icons.org](https://simple-icons.org). Use any slug as `logo=SLUG`.

---

## 7. Reference-style (recommended for large badge stacks)

Keeps prose readable. Put definitions at the file bottom.

```md
[![Build][build-shield]][build-url]
[![Version][version-shield]][version-url]
[![License][license-shield]][license-url]

<!-- at the bottom of the README -->
[build-shield]: https://img.shields.io/github/actions/workflow/status/OWNER/REPO/ci.yml?branch=main&style=for-the-badge
[build-url]: https://github.com/OWNER/REPO/actions/workflows/ci.yml
[version-shield]: https://img.shields.io/npm/v/PACKAGE?style=for-the-badge
[version-url]: https://www.npmjs.com/package/PACKAGE
[license-shield]: https://img.shields.io/github/license/OWNER/REPO?style=for-the-badge
[license-url]: LICENSE
```

---

## 8. Custom static badges (the fallback)

For anything shields.io doesn't support natively:

```
https://img.shields.io/badge/{LABEL}-{MESSAGE}-{COLOR}?style={STYLE}&logo={SLUG}&logoColor={HEX}
```

- Spaces → `%20` or `_`
- Colors: named (`green`, `red`, `blue`) or hex (`2ea44f`)
- Logo slug: any from [simple-icons.org](https://simple-icons.org)

Example:

```md
![Status](https://img.shields.io/badge/status-experimental-orange?style=for-the-badge)
```

---

## 9. Anti-patterns

- **Badge wall** (15+ badges): signal-to-noise collapses. Cap at 8.
- **Broken badge** = immediate credibility loss. Verify every URL renders before publishing.
- **Mixed styles** (`flat` + `for-the-badge` + `social` on the same row): looks sloppy.
- **Deprecated badges**: `http://hits.dwyl.com` etc. — dead services, replace or remove.
- **Vanity badges** ("Made with love ❤") — OK sparingly, not 3 in a row.
