# Build Workflow — Zero to Complete Frutiger Aero Site

End-to-end process for building a Frutiger Aero site from scratch. Follow phases in order — each phase = "economic moment" where revising is cheap.

## Phase 0 — Project setup (15 min)

```
project/
├── index.html
├── styles/
│   ├── aero-tokens.css      ← copy from this skill's assets/
│   └── main.css             ← your styles
├── assets/
│   ├── img/                 ← real photos / period sources
│   ├── icons/               ← SVG icons
│   └── fonts/               ← if hosting custom font
└── js/
    └── main.js              ← optional interactions
```

Setup commands:
```bash
mkdir -p project/styles project/assets/img project/assets/icons project/js
cd project
# Copy tokens
cp /path/to/skill/assets/css/aero-tokens.css styles/
# Create main HTML
touch index.html styles/main.css js/main.js
```

## Phase 1 — Foundation (30 min)

### 1.1 Pick variant
Read `references/01-aesthetic-variants.md`. Decide:
- Bright Aero / Dark Aero / Eco / Aurora / Aqua / Neo
- Period-accurate or modern revival

Document choice in project README.

### 1.2 Set up CSS architecture

`index.html`:
```html
<!DOCTYPE html>
<html lang="en" data-theme="dark-aero"> <!-- or remove for Bright default -->
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>[Project Name]</title>
  <link rel="stylesheet" href="styles/aero-tokens.css">
  <link rel="stylesheet" href="styles/main.css">
</head>
<body>
  <!-- content -->
</body>
</html>
```

### 1.3 Customize palette for client

In `styles/main.css`:
```css
/* Override accent for this specific client */
:root {
  --color-accent: hsl(...);          /* client's specific green/blue */
  --aero-gloss-button-green: linear-gradient(...);  /* custom CTA gradient */
}
```

Keep base structure intact; only override what's brand-specific.

### 1.4 Typography decision

```css
/* Period-accurate */
--aero-font-body: "Segoe UI", "Frutiger", Tahoma, sans-serif;

/* OR Neo Aero modern */
--aero-font-body: "Inter", system-ui, sans-serif;
--aero-font-display: "Clash Display", "Reckless", serif;
```

If using custom fonts, add `@font-face` declarations.

## Phase 2 — Hero section first (1-2 hours)

Always start with hero. It sets the tone for everything else.

### 2.1 Choose hero background type
Per `references/05-aurora-backgrounds.md`:
- **Static CSS aurora** (5 min) — most cases
- **Animated CSS aurora** (15 min) — for "alive" feel
- **WebGL shader** (1-2h) — premium tier only

### 2.2 Layout hero
```html
<section class="hero">
  <nav class="aero-nav"><!-- ... --></nav>
  <div class="hero-content">
    <div class="aero-orb aero-orb-lg" aria-hidden="true"></div>
    <h1>Bold Headline</h1>
    <p class="hero-subhead">Supporting tagline.</p>
    <div class="hero-actions">
      <button class="aero-btn aero-btn-primary aero-btn-lg">Primary CTA</button>
      <button class="aero-btn aero-btn-tertiary aero-btn-lg">Secondary</button>
    </div>
  </div>
</section>
```

```css
.hero {
  min-height: 90vh;
  background: var(--aero-aurora-bg);
  display: flex;
  flex-direction: column;
  position: relative;
  overflow: hidden;
}

.hero-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: var(--space-7) var(--space-4);
  text-align: center;
  max-width: 720px;
  margin: 0 auto;
  position: relative;
  z-index: 2;
}

.hero h1 {
  font-size: var(--text-6xl);
  font-weight: 700;
  line-height: var(--leading-tight);
  color: white;
  text-shadow: 0 2px 8px rgba(0, 0, 0, 0.5);
  margin-bottom: var(--space-3);
}

.hero-subhead {
  font-size: var(--text-xl);
  color: rgba(255, 255, 255, 0.85);
  margin-bottom: var(--space-6);
}

.hero-actions {
  display: flex;
  gap: var(--space-3);
  flex-wrap: wrap;
  justify-content: center;
}

/* Mobile */
@media (max-width: 767px) {
  .hero h1 { font-size: var(--text-4xl); }
  .hero-subhead { font-size: var(--text-lg); }
}
```

### 2.3 Review hero with client
Cheapest moment to revise. Send screenshot or live preview. Iterate before building rest.

## Phase 3 — Content sections (2-4 hours)

Common Frutiger Aero page sections:

### 3.1 Feature grid (glass cards)
```html
<section class="features">
  <h2>Section title</h2>
  <div class="features-grid">
    <article class="aero-glass-card">
      <div class="aero-orb aero-orb-md"></div>
      <h3>Feature</h3>
      <p>Description.</p>
    </article>
    <!-- repeat -->
  </div>
</section>
```

```css
.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: var(--space-5);
  max-width: 1200px;
  margin: 0 auto;
  padding: var(--space-7) var(--space-4);
}
```

### 3.2 Showcase section (image + text)
Vary layouts to break uniform grid. Alternating image-left / image-right:

```html
<section class="showcase">
  <div class="showcase-row">
    <div class="showcase-image">
      <img src="/img/something.webp" alt="...">
    </div>
    <div class="showcase-content">
      <h2>Title</h2>
      <p>Body.</p>
    </div>
  </div>
  <!-- next row reversed -->
  <div class="showcase-row showcase-row-reverse">
    <!-- ... -->
  </div>
</section>
```

### 3.3 Testimonial (glass quote card)
```html
<section class="testimonials">
  <div class="aero-glass-card aero-glass-card-featured">
    <blockquote>
      "Quote text here."
    </blockquote>
    <cite>— Customer Name, Role</cite>
  </div>
</section>
```

### 3.4 CTA section (full-width feature push)
```html
<section class="cta-section">
  <h2>Final CTA</h2>
  <button class="aero-btn aero-btn-primary aero-btn-xl">Get Started Free</button>
</section>
```

```css
.cta-section {
  text-align: center;
  padding: var(--space-9) var(--space-4);
  background:
    radial-gradient(ellipse at center, rgba(60, 218, 86, 0.2), transparent 70%),
    var(--color-bg-page);
}
```

### 3.5 Footer
```html
<footer class="aero-footer">
  <div class="footer-content">
    <div class="footer-brand">Brand Name</div>
    <nav class="footer-links"><!-- links --></nav>
    <p class="footer-copyright">© 2026</p>
  </div>
</footer>
```

## Phase 4 — Responsive verification (30 min)

Test at each breakpoint:

| Breakpoint | What to check |
|------------|---------------|
| **XS (320-479px)** | Single column, ≥44px touch targets, nav collapsed to menu |
| **SM (480-767px)** | Forms stacked, hero text scaled down |
| **MD (768-1023px)** | 2-col layouts possible, sidebar appears |
| **LG (1024-1439px)** | Multi-col layouts, full nav |
| **XL (1440px+)** | Max-width containers prevent overstretch |

Browser DevTools responsive mode → test each.

### Mobile-specific tweaks
```css
@media (max-width: 767px) {
  /* Reduce backdrop-filter intensity for perf */
  .aero-glass-card {
    backdrop-filter: blur(2px);
  }
  
  /* Disable expensive animations */
  .aero-bubble { animation: none; }
  
  /* Stack hero actions */
  .hero-actions { flex-direction: column; align-items: stretch; }
}
```

## Phase 5 — Imagery (1-2 hours)

### 5.1 Find period imagery
For authentic Frutiger Aero:
- [Asadal](https://asadal.com) — Korean stock library, source of many canonical FA images
- [Frutiger Aero Archive](https://frutigeraeroarchive.org) — community archive with PNG foregrounds
- Wikipedia Commons — Windows Vista screenshots, etc.

For modern interpretation:
- Photograph macro nature yourself (grass, water droplets, bubbles)
- Unsplash with searches: "aurora borealis", "macro grass", "bubbles", "tropical fish"

### 5.2 AI imagery (controversial)
Community is anti-AI per [[Future We Were Promised]]. If client insists:
- Use specifically engineered prompts (not generic)
- Curate output (don't ship raw AI)
- Disclose AI use in project credits
- Consider impact on brand reception

### 5.3 Optimize images
```bash
# AVIF for modern browsers (smallest)
# WebP fallback
# JPG fallback for old browsers

# Tools: squoosh.app, sharp CLI, ImageMagick
```

```html
<picture>
  <source type="image/avif" srcset="hero.avif">
  <source type="image/webp" srcset="hero.webp">
  <img src="hero.jpg" alt="..." width="1920" height="1080" loading="lazy">
</picture>
```

## Phase 6 — Interactions + polish (1-2 hours)

### 6.1 Hover states everywhere
Every interactive element needs hover:
- Buttons: `filter: brightness(1.1)`
- Cards: subtle lift `transform: translateY(-2px)`
- Links: underline appearance
- Orbs: glow intensification

### 6.2 Page load animation (one big moment)
> "Heroic motion > scattered micro-interactions"

Pick ONE big animation:
- Hero stagger reveal
- Logo orb scale-in
- Glass card cascade

Don't animate everything.

```css
@keyframes hero-reveal {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.hero h1 {
  animation: hero-reveal 0.8s var(--ease-out) backwards;
}

.hero-subhead {
  animation: hero-reveal 0.8s var(--ease-out) 0.2s backwards;
}

.hero-actions {
  animation: hero-reveal 0.8s var(--ease-out) 0.4s backwards;
}
```

### 6.3 Cursor (optional signature)
For premium projects, custom cursor:
```css
body {
  cursor: url('/assets/cursors/aero-normal.cur'), auto;
}

a, button, [role="button"] {
  cursor: url('/assets/cursors/aero-link.cur'), pointer;
}
```

(Mobile/tablet ignore cursor — they have system pointer.)

## Phase 7 — Quality check (30 min)

See `references/08-quality-checklist.md` for complete checklist.

Quick summary:
- ✅ All variants verified responsive
- ✅ WCAG AA contrast pass (axe DevTools)
- ✅ Lighthouse score ≥ 90
- ✅ Period-correct aesthetic OR explicit modern revival choice
- ✅ Signature unforgettable element present
- ✅ No AI-default tells (Inter, Roboto, purple gradient)
- ✅ Asset weight reasonable (<300KB JS, <50KB CSS)
- ✅ `prefers-reduced-motion` respected

## Phase 8 — Handoff / launch

### If building yourself (designer-dev)
- Deploy to Vercel/Netlify
- Set up analytics (Plausible, Fathom — privacy-respecting)
- Test cross-browser (Chrome, Firefox, Safari, mobile Safari, mobile Chrome)
- Verify production performance (real device tests)

### If handing to dev team
See [[Design Handoff]] in vault.
- Clean Figma file
- Export all assets
- Annotate behaviors
- Walkthrough call
- Stay engaged for design QA

## Time budgets (rough)

| Project complexity | Total time |
|--------------------|------------|
| Simple landing (1 page) | 6-10 hours |
| Multi-page marketing site (5-10 pages) | 30-50 hours |
| Web app / dashboard with FA aesthetic | 60-120 hours |
| Full brand identity + site | 80-160 hours |

These assume designer-developer (one person). Pure design work without dev = ~half.

## Iteration discipline

Build → review with client → revise → review → revise.

Maximum 2-3 revision rounds per phase. After that, push back politely:
- "I can revise further but the original direction in [Phase 1.1] was approved. What changed?"
- Charge for scope changes beyond agreed revisions.

Client buy-in at Phase 2 hero is critical — that's where direction gets locked.

## When to break workflow

Sometimes client urgency requires shortcuts:

- **Rush projects**: skip Phase 0 setup (use Vite/Astro starter), skip Phase 4 testing rigor (do at end)
- **Brand-only refresh**: skip Phase 5 imagery if existing photos work
- **Component-only work**: only Phase 1 + relevant component reference

But: never skip:
- Phase 1.1 variant decision (otherwise visual chaos)
- Phase 7 quality check (otherwise broken delivery)
- Accessibility (legal + ethical baseline)
