# Profile README (username/username repo)

GitHub's **profile README** is a special repo named exactly after your username (`username/username`) whose `README.md` renders on your profile page.

This is not a project README — it's a personal landing page. Grammar is different: less installation, more identity.

---

## Core structure

```
1. Greeting / intro card
2. What I'm doing now (1–3 lines)
3. Skills / tech-stack icons
4. GitHub stats widgets
5. Top languages card
6. Streak + trophies (optional)
7. Recent blog posts / now-playing (dynamic, optional)
8. Socials row
9. Contribution snake (easter egg)
10. Visitor counter (optional)
```

Keep total length under one scroll on a laptop screen. Profile READMEs live or die by skimmability.

---

## 1. Starter template

```md
<h1 align="center">Hi 👋, I'm Your Name</h1>
<h3 align="center">A one-line descriptor — e.g. "Backend engineer building tools for developers"</h3>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=YOURUSER&label=Profile%20views&color=0e75b6&style=flat" alt="views" />
</p>

- 🔭 Currently working on **[project name](https://github.com/YOURUSER/project)**
- 🌱 Learning **Rust** and **distributed systems**
- 💬 Ask me about **TypeScript, Postgres, developer tooling**
- 📫 Reach me: **you@example.com**
- ⚡ Fun fact: **I own a 3D printer and no finished prints**

### Connect

<p align="left">
  <a href="https://twitter.com/YOURUSER" target="_blank">
    <img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" alt="twitter"/>
  </a>
  <a href="https://linkedin.com/in/YOURUSER" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="linkedin"/>
  </a>
  <a href="https://yoursite.com" target="_blank">
    <img src="https://img.shields.io/badge/Website-24292E?style=for-the-badge&logo=github&logoColor=white" alt="site"/>
  </a>
</p>

### Tech

<p align="left">
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" />
  <img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white" />
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
</p>

### Stats

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=YOURUSER&show_icons=true&theme=radical" alt="stats"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=YOURUSER&layout=compact&theme=radical" alt="top-langs"/>
</p>
```

---

## 2. Widget library

### GitHub Stats Card — [github-readme-stats](https://github.com/anuraghazra/github-readme-stats)

```md
![Stats](https://github-readme-stats.vercel.app/api?username=YOURUSER&show_icons=true&theme=dark)
```

Theme options: `default`, `dark`, `radical`, `merko`, `tokyonight`, `gruvbox`, `dracula`, `nord`, `transparent`. Full list in the repo.

### Top Languages

```md
![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=YOURUSER&layout=compact&theme=dark)
```

Layouts: `default`, `compact`, `donut`, `donut-vertical`, `pie`.

### Streak

```md
![Streak](https://github-readme-streak-stats.herokuapp.com/?user=YOURUSER&theme=dark)
```

### Trophies — [github-profile-trophy](https://github.com/ryo-ma/github-profile-trophy)

```md
![Trophies](https://github-profile-trophy.vercel.app/?username=YOURUSER&theme=onedark&no-frame=true&row=1)
```

### Typing SVG — [readme-typing-svg](https://github.com/DenverCoder1/readme-typing-svg)

```md
<p align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&color=3BFFC4&center=true&width=500&lines=Backend+engineer;Tool+builder;Open+source+maintainer" alt="Typing SVG"/>
  </a>
</p>
```

### Random quote

```md
![Quote](https://quotes-github-readme.vercel.app/api?type=horizontal&theme=radical)
```

### Spotify now-playing — [spotify-github-profile](https://github.com/kittinan/spotify-github-profile)

```md
<a href="https://spotify-github-profile.kittinanx.com/api/view.svg?uid=YOURSPOTIFYID&redirect=true">
  <img src="https://spotify-github-profile.kittinanx.com/api/view.svg?uid=YOURSPOTIFYID&cover_image=true&theme=default&show_offline=false&background_color=121212&interchange=false" alt="Spotify"/>
</a>
```

### Recent blog posts — [blog-post-workflow](https://github.com/gautamkrishnar/blog-post-workflow)

Driven by a GitHub Action — write a workflow that rewrites the README on schedule. See the repo.

```md
<!-- BLOG-POST-LIST:START -->
<!-- BLOG-POST-LIST:END -->
```

### Contribution snake — [Platane/snk](https://github.com/Platane/snk)

Requires a GitHub Action. Workflow generates a snake that eats your contribution graph.

```md
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/YOURUSER/YOURUSER/output/github-contribution-grid-snake-dark.svg">
  <img alt="snake" src="https://raw.githubusercontent.com/YOURUSER/YOURUSER/output/github-contribution-grid-snake.svg">
</picture>
```

Workflow file (`.github/workflows/snake.yml`):

```yaml
name: generate snake
on:
  schedule: [{cron: "0 */24 * * *"}]
  workflow_dispatch:
jobs:
  generate:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: Platane/snk@v3
        with:
          github_user_name: YOURUSER
          outputs: |
            dist/github-contribution-grid-snake.svg
            dist/github-contribution-grid-snake-dark.svg?palette=github-dark
      - uses: crazy-max/ghaction-github-pages@v3
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### Profile views counter

```md
![Profile views](https://komarev.com/ghpvc/?username=YOURUSER&label=Profile%20views&color=0e75b6&style=flat)
```

### Activity graph — [github-readme-activity-graph](https://github.com/Ashutosh00710/github-readme-activity-graph)

```md
![Activity Graph](https://github-readme-activity-graph.vercel.app/graph?username=YOURUSER&theme=dracula)
```

### Holopin badges (participation)

```md
[![An image of @YOURUSER's Holopin badges](https://holopin.me/YOURUSER)](https://holopin.io/@YOURUSER)
```

---

## 3. Category flavors (from awesome-github-profile-readme)

Pick **one** aesthetic, don't mix.

### Minimalist

Just intro + 2 stats cards + socials row. Under 30 lines.

### Descriptive

Long-form prose. About, what-I'm-working-on, what-I-believe, contact. Closer to an "About" page.

### Code mode

Intro written as a code block:

```md
```javascript
const yourname = {
  pronouns: "they/them",
  code: ["TypeScript", "Rust", "Python"],
  tools: ["React", "Node", "Postgres"],
  architecture: ["event-driven", "microservices", "serverless"],
  askMeAbout: ["web dev", "dev tools", "open source"],
  currentProject: "building X",
  funFact: "...",
};
```
```

### Typing mode

Typing SVG as the centerpiece, minimal other widgets.

### Game mode

Interactive elements driven by issues/actions — chess, tic-tac-toe, hangman. Requires a game-state Action. See [timburgan/timburgan](https://github.com/timburgan/timburgan) for the canonical example.

### Dynamic / real-time

Now-playing, latest blog posts, activity graph, weather, recent commits. Feels "alive" but needs maintenance (broken widget = dead profile).

### Anime / retro / fancy fonts

Visual identity over content. GIFs, anime icons, big ASCII banners. Niche — avoid unless the profile's whole point is personality.

---

## 4. Setup steps (first-time)

1. Create repo named **exactly** your username (`github.com/username/username`)
2. Initialize with a README
3. Make the repo **public** (profile READMEs on private repos don't render)
4. Edit the README → saved = rendered on your profile

---

## 5. Anti-patterns

- **15+ stats widgets** — loads slowly, looks desperate
- **Rainbow of mismatched themes** — pick one palette, stick to it
- **Fake metrics** — "500+ projects shipped" lies are instantly spotted
- **Broken widgets** — external SVG services die. Audit quarterly.
- **"Hi 👋 I'm a passionate developer who loves to code"** — say something specific or nothing
- **Listing every language ever touched** — signal dilution. Top 6 tools max.
- **Unlinked badges** — every badge should link to something (profile, project, site)

---

## 6. Minimal high-quality profile (30-second version)

```md
### Hi, I'm Your Name.

I build **developer tools** in TypeScript and Rust. Currently working on [project](https://github.com/YOURUSER/project).

**Elsewhere:** [site](https://yoursite.com) · [twitter](https://twitter.com/YOURUSER) · [mastodon](https://mastodon.social/@YOURUSER)

![Stats](https://github-readme-stats.vercel.app/api?username=YOURUSER&show_icons=true&theme=transparent&hide_border=true)
```

That's it. Often better than 300-line profiles full of widgets.
