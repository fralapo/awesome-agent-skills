# Anti-AI Pitfalls — What Makes FA Look Generic vs Period-Accurate

## The trap

When you ask an LLM (Claude, GPT, etc.) to "build a Frutiger Aero website," default output is **glassmorphism with green accent**:
- Centered hero with orb above headline
- 4-card uniform feature grid
- Generic CTAs ("Get Started", "Learn More")
- Aurora background as decoration
- Uniform spacing throughout
- Generic copy

This is **NOT Frutiger Aero**. This is **AI default glassmorphism with green tint**.

Real Frutiger Aero from period (2005-2013) had specific structural patterns that AI defaults miss. This guide documents them.

## What real period FA looked like

### Reference 1: frutigeraeroarchive.org (Dark Aero, period-accurate revival)

Structure:
- **Window-chrome wrapper** — content lives "inside" a faux window with title bar
- **Asymmetric border-radius** `70px 80px 0 0` (distinctive Aero curve, NOT uniform)
- **Sidebar nav** with categorized sections (Main Content / Entertainment / Community / Website / Options) + icons per link
- **Vista start orb** in nav with green glow
- **Title bars** for sections (metallic black gradient — Vista chrome)
- **Universal text-shadow** for legibility on glossy bg
- **Real content density** — text-heavy intro paragraphs with embedded links
- **Gallery cards** with photo thumbnails + captions (editorial)
- **Background photo** (longhorn.jpg — Vista landscape) — NOT gradient aurora
- **Custom .cur cursors** referenced in CSS

### Reference 2: Vista websites 2007-2009 (Web Design Museum)

Patterns:
- Centered narrow container (700-1080px max, NOT full-bleed)
- Glass-window styling for the whole page container
- Glossy navigation bar
- Drop shadows on container giving "floating window" feel
- Photo-heavy hero (real photos, not gradients)
- Content sections with varied densities
- Footer mimicking Vista taskbar

### Reference 3: Apple.com 2007

Patterns:
- Editorial image-text alternation
- Image-heavy hero with product photo
- Sidebar navigation (categorized)
- Asymmetric layouts (image-left/text-right rotating)
- Glossy UI throughout
- Heavy whitespace BUT structured (not "minimal")

### Reference 4: i-Suite Hotel Rimini (period architecture made web)

Patterns:
- Curved glossy surfaces visible in branding
- Photo galleries laid out asymmetrically
- "Room" navigation metaphor (carries to web nav)
- Italian editorial typography
- Image-led layouts

## The AI-default trap patterns (avoid these)

### ❌ Pattern 1: "Centered hero + orb-above-title"
```
[orb]
[BIG HEADLINE]
[subhead]
[CTA] [CTA-secondary]
```
**Why bad**: textbook AI hero. Every glassmorphism tutorial produces this.

**✅ Fix**: Image-text editorial split, OR window-chrome wrapper, OR scrollytelling intro, OR specific cultural moment (e.g., "[Brand] introduces...")

### ❌ Pattern 2: "4-card uniform feature grid"
```
[card] [card] [card] [card]
```
With identical sizes, identical orbs, identical headings.

**Why bad**: Every SaaS template uses this. Generic.

**✅ Fix**:
- Bento layout (varied card sizes)
- Editorial showcase (alternating image-text rows)
- Gallery with real photos + captions (FA period style)
- ONE big featured project + 3 smaller (asymmetric)
- Linear list with rich detail (no card abstraction)

### ❌ Pattern 3: "Aurora background everywhere"
Aurora gradient → full page → glass cards floating on it.

**Why bad**: aurora was DESKTOP wallpaper behind window chrome, NOT section backgrounds. Modern misuse.

**✅ Fix**:
- Aurora as desktop bg with window-chrome content wrapper on top
- Photo bg (grass macro, Asadal sources) for editorial sections
- Soft tinted backgrounds for content sections (subtle green-tinted white)
- Aurora ONLY in hero, content sections use different bg

### ❌ Pattern 4: "Generic copy"
- "Get Started" / "Learn More" / "Sign Up Free"
- "Built something memorable"
- "The future is here"
- "Beautiful interfaces"

**Why bad**: AI defaults to corporate-SaaS English. No specificity.

**✅ Fix**:
- Specific to project (NOT generic CTAs)
- FA-aware copy: "The future you were promised" / "Optimism, returned"
- Period-correct phrasing: "Welcome to [Site Name]. Enjoy..."
- Editorial voice not corporate

### ❌ Pattern 5: "Skeumorphic orb in every section"
Hero orb. Feature orbs. Footer orb. Orbs everywhere.

**Why bad**: One orb = signature. Many orbs = decoration noise.

**✅ Fix**: ONE memorable orb (hero or nav). Rest of skeumorphism via other elements (3D icons, photo treatments, window chrome).

### ❌ Pattern 6: "Uniform everything"
Same border-radius everywhere. Same spacing scale. Same gloss treatment.

**Why bad**: Period FA had VARIATION:
- Asymmetric Aero curves (70px 80px 0 0) for distinctive elements
- Standard 8-12px radius for buttons
- Sharper edges for tables/lists
- Different gloss intensities for nav vs content vs CTA

**✅ Fix**: Use asymmetric border-radius for ONE signature element (window chrome usually). Standard radius elsewhere.

### ❌ Pattern 7: "Minimal content"
Generic AI sites are minimal — short copy, sparse layouts.

**Why bad**: Period FA was **content-rich**. Vista sites had paragraphs with embedded links. Apple.com had detailed product descriptions. Real FA wasn't minimalist.

**✅ Fix**: Long intro paragraphs with embedded links. Multiple content sections with varied densities. Real text, not "Headline / Subhead / CTA" template.

### ❌ Pattern 8: "Drop shadows uniform everywhere"
Every element gets the same shadow.

**Why bad**: Period FA had elevation hierarchy:
- Page-level window chrome: heavy shadow (`xl`)
- Nav: subtle shadow (`sm`)
- Cards: medium shadow (`md`)
- Buttons: tight close-to-surface shadow (`xs`)

**✅ Fix**: 5-tier elevation system. Match shadow to element importance.

### ❌ Pattern 9: "System font everything"
`font-family: system-ui` or default `Inter`.

**Why bad**: Anti-default principles + period inaccuracy. Real FA used Segoe UI (Vista) which is humanist sans, NOT geometric Inter.

**✅ Fix**:
- Segoe UI stack with humanist fallbacks (Tahoma, Geneva)
- OR characterful display font (Reckless, Clash Display) for headings
- NEVER pure Inter for FA

### ❌ Pattern 10: "Footer with social icons + copyright"
```
[Social icons] [Newsletter] [Copyright 2026]
```
Generic.

**Why bad**: Period FA footers mimicked Vista taskbar (metallic gradient strip with system info echo).

**✅ Fix**:
- Vista taskbar-style footer with metallic gradient
- OR Vista start orb + status info pattern
- OR specific brand voice (NOT corporate footer)
- Footer can also be omitted entirely if window-chrome wraps page

## Period-accurate signature patterns

### ✅ Window-chrome wrapper
Entire page wrapped in faux window with title bar.

```html
<div class="aero-window">
  <div class="aero-window-titlebar">
    <div class="aero-window-controls">
      <button aria-label="Minimize">_</button>
      <button aria-label="Maximize">□</button>
      <button aria-label="Close">✕</button>
    </div>
    <div class="aero-window-title">Site Title</div>
  </div>
  <div class="aero-window-body">
    <!-- content -->
  </div>
</div>
```

```css
.aero-window {
  max-width: 1280px;
  margin: 30px auto;
  border-radius: 70px 80px 0 0;  /* Asymmetric Aero curve */
  background: var(--color-bg-glass);
  backdrop-filter: blur(8px);
  box-shadow: var(--aero-shadow-xl);
  border: 1px solid var(--color-border-glass);
  overflow: hidden;
}

.aero-window-titlebar {
  background: var(--aero-titlebar);  /* metallic black gradient */
  padding: 12px 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid #000;
  color: white;
  text-shadow: 0 1px 2px rgba(0,0,0,0.6);
}
```

### ✅ Sidebar nav with categories
NOT a horizontal top nav. Vista-style left sidebar with grouped sections.

```html
<aside class="aero-sidebar">
  <nav>
    <h3 class="aero-nav-category">Main</h3>
    <a href="/" class="aero-nav-link active">
      <img src="icon-home.png" alt=""> Home
    </a>
    <a href="/work" class="aero-nav-link">
      <img src="icon-work.png" alt=""> Work
    </a>
    <h3 class="aero-nav-category">Resources</h3>
    <a href="/blog" class="aero-nav-link">
      <img src="icon-blog.png" alt=""> Blog
    </a>
  </nav>
</aside>
```

### ✅ Title bars for content sections
Each major section opens with a metallic gradient title bar (echo Vista window chrome at section level).

```html
<section>
  <header class="aero-section-titlebar">
    <h2>Section title</h2>
  </header>
  <div class="aero-section-body">
    <!-- content -->
  </div>
</section>
```

### ✅ Photo background (NOT gradient)
Real photo as desktop wallpaper feel. Aurora is a LAYER, not the whole.

```css
body {
  background:
    /* Subtle aurora overlay */
    radial-gradient(ellipse at 20% 30%, rgba(60, 218, 86, 0.3), transparent 60%),
    radial-gradient(ellipse at 70% 70%, rgba(95, 168, 211, 0.3), transparent 60%),
    /* Real photo */
    url('/img/grass-hill-vista.webp') center / cover fixed,
    /* Fallback color */
    linear-gradient(180deg, hsl(200, 75%, 70%), hsl(140, 50%, 60%));
}
```

### ✅ Editorial layout — image-text alternation
NOT centered cards. Real content alternating.

```html
<section class="aero-showcase">
  <div class="aero-showcase-row">
    <div class="aero-showcase-image"><img src="..."></div>
    <div class="aero-showcase-text">
      <h2>Project name</h2>
      <p>Real description paragraph...</p>
      <a href="...">Read more →</a>
    </div>
  </div>
  <div class="aero-showcase-row aero-showcase-reverse">
    <div class="aero-showcase-text">
      <h2>Another project</h2>
      <p>...</p>
    </div>
    <div class="aero-showcase-image"><img src="..."></div>
  </div>
</section>
```

### ✅ Content-rich intro
NOT "Headline / Subhead / 2 CTAs."

Period intro pattern (from archive site):
> "Welcome to [Brand], a [description]. We do [specific thing], [specific thing], and [specific thing]. You can [action] in our [section], or explore [section]."

Multiple sentences. Embedded links. Specific.

### ✅ Vista start orb (functional)
Round orb at top-left of nav, clickable.

```html
<button class="aero-start-orb" aria-label="Main menu">
  <!-- icon -->
</button>
```

### ✅ Custom cursor (optional signature)
Period sites used `.cur` files.

```css
body { cursor: url('/cursors/aero-normal.cur'), auto; }
a, button { cursor: url('/cursors/aero-link.cur'), pointer; }
```

## Editorial decisions to break AI defaults

### Layout
- ✅ Use asymmetry — image-left or image-right rows
- ✅ Use bento — varied tile sizes
- ✅ Use sidebar — vertical categorized nav
- ❌ Don't use uniform centered grid
- ❌ Don't use Apple-style minimal hero

### Content
- ✅ Write specific copy for fictional brand (Aria Voss, Mira Cloud, etc.)
- ✅ Use specific project names ("Coastline Mapping Project")
- ✅ Use period-specific voice ("Welcome to..." / "Enjoy...")
- ❌ Don't use generic "Get Started" / "Learn More"
- ❌ Don't use lorem ipsum

### Visual
- ✅ One signature orb max
- ✅ Photo as bg (not gradient alone)
- ✅ Window-chrome wrapper for whole page
- ✅ Title bars for section openers
- ✅ Custom cursor reference
- ❌ Don't put orbs in every section
- ❌ Don't repeat same card layout 4x

### Typography
- ✅ Segoe UI stack (period accurate)
- ✅ OR characterful display font for headings (Reckless, Clash Display)
- ❌ Don't use Inter as primary
- ❌ Don't use Roboto

## The "AI generic" smell test

Before shipping FA site, ask:

1. **Could I swap the FA elements for shadcn/ui defaults and the structure would still work?**
   - YES → too generic, fix layout
   - NO → structure is FA-specific, good

2. **Does any individual screen look like it came from a Tailwind glassmorphism tutorial?**
   - YES → fix that screen
   - NO → good

3. **Would a designer who knows Frutiger Aero immediately recognize the period references?**
   - NO → add Vista chrome, sidebar nav, asymmetric radius
   - YES → period-accurate

4. **Is there ONE element no other site has?**
   - NO → add signature (custom cursor, specific orb treatment, distinctive title bar, etc.)
   - YES → good

5. **Could the copy be on any SaaS landing page?**
   - YES → rewrite specific to brand + FA voice
   - NO → good

## See also

- `references/01-aesthetic-variants.md` — choose specific variant first
- `references/03-glossy-buttons.md` — period-accurate CTA recipes
- `references/04-glass-panels.md` — glass treatments
- `examples/01-period-accurate-portfolio.html` — full example with window chrome + sidebar + editorial layout
