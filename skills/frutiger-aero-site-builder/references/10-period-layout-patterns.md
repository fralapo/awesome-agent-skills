# Period Layout Patterns — Real 2000s + Neocities Indie

Based on analysis of 41 real period + indie revival sites. These are the patterns that distinguish authentic Frutiger Aero from AI-default glassmorphism.

## The 5 dominant patterns

### Pattern A: Container + Sidebar + Main (DEFAULT — use this)

Most common period structure. Examples: frutigeraeroarchive.org, derrek.org, fan.ribo.zone, tackyvillain.

```
+----------------------------------------------------------+
|  [Banner image OR Vista title bar]                       | ← asymmetric border-radius
+----------------------------------------------------------+
|  +-----------+  +--------------------------------------+ |
|  |  SIDEBAR  |  |  MAIN CONTENT                        | |
|  |  - Main   |  |  Multiple sections                   | |
|  |  - Section|  |  Editorial paragraphs                | |
|  |  - Section|  |  Real content                        | |
|  |  - Out    |  |                                      | |
|  +-----------+  +--------------------------------------+ |
+----------------------------------------------------------+
|                  [Footer strip — taskbar style]          |
+----------------------------------------------------------+
```

```html
<div class="container">          <!-- max-width 700-1300px, NOT full-bleed -->
  <header class="banner">         <!-- image OR title-bar -->
    <img src="banner.png">         <!-- asymmetric border-radius -->
  </header>
  <div class="flex">              <!-- display: flex -->
    <aside class="left-sidebar">  <!-- order: 1, width: 145-220px -->
      <nav>
        <div class="nav-category">
          <span class="nav-category-title">Main</span>
          <a class="nav-button"><img src="icon"> Link text</a>
        </div>
      </nav>
    </aside>
    <main>                          <!-- order: 2, flex: 1 -->
      <!-- editorial sections -->
    </main>
  </div>
</div>
```

CSS keys:
```css
.container { max-width: 1080px; margin: 0 auto; }
.banner img {
  border-top-left-radius: 70px;       /* asymmetric Aero curve */
  border-top-right-radius: 70px;
  border-bottom-left-radius: 10px;
  border-bottom-right-radius: 10px;
}
.flex { display: flex; }
.left-sidebar { order: 1; width: 145px; }   /* fixed sidebar */
main { order: 2; flex: 1; }
```

**Use for**: 90% of FA portfolio/personal/marketing sites.

### Pattern B: Layout + Marquee + Body

```html
<div class="layout">
  <a href="/" class="header"></a>        <!-- clickable image as logo+home -->
  <div class="marquee">
    <marquee scrollamount="2">welcome to [site]... enjoy your stay!</marquee>
  </div>
  <div class="content"><!-- main --></div>
</div>
```

**Use for**: Strongly retro personal sites. Marquee is period-authentic, not "wrong".

### Pattern C: Window-CSS Framework

```html
<link rel="stylesheet" href="https://unpkg.com/7.css">

<div class="window active" style="max-width: 800px; margin: 50px auto;">
  <div class="title-bar">
    <div class="title-bar-text">Site Title</div>
    <div class="title-bar-controls">
      <button aria-label="Minimize"></button>
      <button aria-label="Maximize"></button>
      <button aria-label="Close"></button>
    </div>
  </div>
  <div class="window-body has-space">
    <!-- content -->
  </div>
</div>
```

Available frameworks:
- **7.css** — Windows 7 / Aero Glass (best for FA — see `unpkg.com/7.css`)
- **98.css** — Windows 98 (more retro indie)
- **XP.css** — Windows XP (mid-retro)

**Use for**: Fast prototyping, maximum Vista feel, hackable foundation.

### Pattern D: ON-LINE Old-Web (tackyvillain style)

```html
<div class="container">
  <header><h1>SITENAME ON-LINE</h1></header>
  <main class="container-row">
    <nav class="vnav"><!-- vertical nav --></nav>
    <article><!-- main --></article>
  </main>
</div>
```

**Use for**: Self-aware retro homages. "SITE-NAME ON-LINE" framing.

### Pattern E: Modern Desktop UI Metaphor (sharyap.com style)

```html
<div class="desktop" style="background: url(wallpaper.jpg)">
  <div class="window" draggable>
    <div class="window-titlebar">Window 1</div>
    <div class="window-body"><!-- content --></div>
  </div>
  <div class="dock">
    <button class="dock-icon"></button>
    <button class="dock-icon"></button>
  </div>
</div>
```

**Use for**: Premium portfolio differentiator, tech-brand work. Requires JS for window management.

## The asymmetric border-radius signature

THE most distinctive Frutiger Aero CSS pattern. Period sites use deliberately uneven corners.

```css
/* Banner header — big top curve, sharp bottom */
.banner {
  border-radius: 70px 70px 10px 10px;
}

/* Window title bar — asymmetric top */
.window-titlebar {
  border-radius: 70px 80px 0 0;     /* archive site signature */
}

/* Main content — opposite asymmetry */
.main {
  border-radius: 5px 5px 30px 30px;
}

/* Single-property asymmetric (extreme variant) */
.aero-curve {
  border-radius: 70px 80px 10px 30px;  /* all 4 different */
}
```

NOT uniform corners. Period FA = deliberately lopsided.

## Color palettes from real period sites

| Palette | BG | Text | Accent | Vibe |
|---------|-----|------|--------|------|
| **Dark Aero** | `#303030` + longhorn.jpg | `#dadada` | `#3cda56` green | Vista 2007 dark |
| **Cream warm** | bg-photo + `#e8e5dbc2` | `#372e29` | `#e1b63e` yellow | Cozy, derrek.org |
| **Peach soft** | papayawhip | sienna | `#ffd2cd` | cinni light theme |
| **Peachpuff dark** | `#382d2c` | peachpuff | `#e8a0ae` | cinni dark theme |
| **Editorial calm** | `#EBEEE6` | `#22242C` | cadetblue | fan.ribo.zone |

Add these as `data-theme` variants in your token system:

```css
[data-theme="aero-cream"] {
  --color-bg-page: #d4cfc3;
  --color-bg-surface: rgba(232, 229, 219, 0.85);
  --color-text-primary: #372e29;
  --color-text-secondary: #9f9893;
  --color-accent: #6b9a4f;
  --color-accent-hover: #e1b63e;
}

[data-theme="aero-peach"] {
  --color-bg-page: papayawhip;
  --color-bg-surface: rgba(255, 239, 213, 0.9);
  --color-text-primary: sienna;
  --color-accent: #e8a0ae;
}
```

## Background treatment patterns

### NOT pure gradient
Real period sites use **photo backgrounds**, not pure CSS gradients.

```css
body {
  background-image: url("images/desktop-wallpaper.jpg");
  background-size: cover;
  background-attachment: fixed;     /* desktop wallpaper feel */
  background-position: center;
}
```

### Photo + radial-gradient overlay
```css
body {
  background:
    radial-gradient(ellipse at 20% 30%, rgba(60, 218, 86, 0.25), transparent 60%),
    radial-gradient(ellipse at 80% 70%, rgba(95, 168, 211, 0.3), transparent 60%),
    url('grass-hill.jpg') center / cover fixed,
    linear-gradient(180deg, #0d1b2a, #1b263b);
}
```

### Tiled bg (period 2000s — neo2k.neocities.org)
```css
body {
  background-image: url("bg-tile.png");
  background-repeat: repeat;
  background-color: #c8d4e3;  /* fallback if tile fails */
}
```

## Vista chrome elements (key signatures)

### Title bar metallic gradient
```css
.titlebar {
  background: linear-gradient(180deg,
    rgba(148, 148, 148, 0.9) 0%,
    rgba(71, 71, 71, 0.9) 20%,
    rgba(19, 19, 19, 0.9) 40%,
    rgba(7, 7, 7, 0.93) 100%);
  color: white;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.6);
}
```

### Window control buttons
```css
.titlebar-controls button {
  width: 32px;
  height: 22px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  background: linear-gradient(180deg,
    rgba(255, 255, 255, 0.2),
    rgba(0, 0, 0, 0.3) 50%,
    rgba(0, 0, 0, 0.5));
  border-radius: 3px;
}

.titlebar-controls button[aria-label="Close"] {
  background: linear-gradient(180deg,
    rgba(232, 30, 30, 0.7),
    rgba(120, 12, 12, 0.7) 50%,
    rgba(80, 0, 0, 0.8));
}
```

### Section title bars (h1, h2 with metallic gradient — archive site pattern)
```css
h1, h2 {
  background: linear-gradient(to bottom,
    #bebebe 0%, #777 3%, #232323 55%,
    #000 55%, #161616 98%, #000 100%);
  color: white;
  padding: 4px 10px 6px;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.7);
  text-align: center;
  border: 1px solid #4b4b4b;
}
```

## Sidebar nav signature

```css
.nav-category {
  background: rgba(26, 26, 26, 0.35);    /* subtle frame */
  border: 1px solid #424242;
  padding: 3px 5px;
  margin-bottom: 14px;
}

.nav-category-title {
  background: linear-gradient(to bottom,
    rgba(255, 255, 255, 0.75) 0%,
    rgba(129, 129, 129, 0.75) 3%,
    rgba(56, 56, 56, 0.75) 50%,
    rgba(27, 27, 27, 0.75) 50%);          /* mini-titlebar */
  border: 1px solid #000;
  color: #f7f4f4;
  padding: 2px;
  text-align: center;
  font-size: 12px;
}

.nav-link {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 3px 6px;
  width: 93%;
  font-size: 12px;
  color: #eee;
  background: linear-gradient(to bottom,
    rgba(255, 255, 255, 0.25),
    rgba(117, 117, 117, 0.15) 20%,
    rgba(92, 92, 92, 0.15) 60%,
    rgba(0, 0, 0, 0.3) 60%,
    rgba(41, 41, 41, 0.3) 100%);
  border: 1px solid #0f0f0f;
  border-radius: 5px;
}

/* Active state with green glow */
.nav-link.is-active {
  background: linear-gradient(to bottom,
    rgba(255, 255, 255, 0.25),
    rgba(117, 117, 117, 0.2) 20%,
    rgba(92, 92, 92, 0.2) 40%,
    rgba(29, 73, 23, 0.3) 40%,
    rgba(43, 240, 36, 0.7) 100%);
  color: var(--aero-green-glow);
  transform: scale(1.03);
}
```

## Custom cursor reference

```css
* {
  cursor: url('img/cursors/aero-normal.png'), auto;
}

a, button {
  cursor: url('img/cursors/aero-link.png'), pointer;
}
```

Or inline SVG cursor (modern, no .cur file needed):
```css
* {
  cursor: url('data:image/svg+xml;utf8,<svg ...>...</svg>') 10 10, auto;
}
```

## Content density (anti-AI)

Period sites are **content-rich**:
- 2-3 paragraph intros with embedded links
- Multiple content sections per page
- Real text, no placeholder
- Editorial voice (specific, personal, not corporate)

NOT minimal "Headline / Subhead / 2 CTAs" template.

## Anti-pattern detection (5-question test)

Before shipping Frutiger Aero output, check:

1. **Is the container full-bleed?** If YES → BAD. Use max-width 700-1300px.
2. **Is there a 4-card uniform feature grid?** If YES → BAD. Use gallery, bento, or editorial.
3. **Is the nav horizontal centered?** If YES → BAD. Use sidebar nav with categories.
4. **Is the heading text-only?** If YES → BAD. Use banner image OR title-bar metallic gradient.
5. **Is the border-radius uniform everywhere?** If YES → BAD. Asymmetric for at least one signature element.

If 3+ YES → AI-default glassmorphism, not Frutiger Aero. Rebuild.

## See also

- `examples/01-hero-landing.html` — Pattern A (Dark Aero, window chrome)
- `examples/02-neocities-warm-cream.html` — Pattern A variant (cream palette, derrek.org inspired)
- `references/01-aesthetic-variants.md` — variant selection
- `references/09-anti-ai-pitfalls.md` — generic AI-default detection
