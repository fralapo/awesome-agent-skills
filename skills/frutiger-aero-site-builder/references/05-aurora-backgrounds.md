# Aurora Backgrounds — Hero Background Patterns

## Three approaches by complexity

| Approach | Effort | Look | Use case |
|----------|--------|------|----------|
| **Static CSS** | 5 min | Solid layered gradients | Simple landing pages |
| **Animated CSS** | 15 min | Slow shifting layers | Most Frutiger Aero hero sections |
| **WebGL shader** | 1-2 hours | Real fluid motion | Premium / signature builds |

Start with static, upgrade to animated if budget allows.

## 1. Static CSS aurora (5 min)

The default — works for most projects.

```html
<section class="aero-hero">
  <h1>Hero Headline</h1>
  <p>Subhead supporting text.</p>
</section>
```

```css
.aero-hero {
  min-height: 80vh;
  background: var(--aero-aurora-bg);  /* token from aero-tokens.css */
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: var(--space-8) var(--space-4);
  color: white;
  text-align: center;
  position: relative;
  overflow: hidden;
}
```

The `--aero-aurora-bg` token contains:
```css
radial-gradient(ellipse at 20% 30%, rgba(60, 218, 86, 0.5), transparent 50%),
radial-gradient(ellipse at 70% 60%, rgba(95, 168, 211, 0.5), transparent 50%),
radial-gradient(ellipse at 40% 80%, rgba(190, 80, 220, 0.35), transparent 50%),
linear-gradient(180deg, #0d1b2a, #1b263b);
```

4 layers: green + blue + magenta radial glows + dark base.

## 2. Animated aurora (15 min)

Add slow drift animation to make it feel alive without being distracting.

```css
.aero-hero {
  /* base styles as above */
  background:
    radial-gradient(ellipse at 20% 30%, rgba(60, 218, 86, 0.5), transparent 50%),
    radial-gradient(ellipse at 70% 60%, rgba(95, 168, 211, 0.5), transparent 50%),
    radial-gradient(ellipse at 40% 80%, rgba(190, 80, 220, 0.35), transparent 50%),
    linear-gradient(180deg, #0d1b2a, #1b263b);
  background-size: 200% 200%;
  animation: aero-aurora-drift var(--duration-aurora) ease-in-out infinite;
}

@keyframes aero-aurora-drift {
  0%, 100% {
    background-position: 0% 0%, 0% 0%, 0% 0%, 0% 0%;
  }
  25% {
    background-position: 30% 20%, -20% 30%, 40% -10%, 0% 0%;
  }
  50% {
    background-position: -10% 40%, 30% -20%, -20% 30%, 0% 0%;
  }
  75% {
    background-position: 20% -10%, -30% 40%, 10% 40%, 0% 0%;
  }
}

/* Respect reduced motion */
@media (prefers-reduced-motion: reduce) {
  .aero-hero {
    animation: none;
  }
}
```

20-second cycle = subtle enough that user doesn't notice motion, but adds life.

## 3. Multi-layer with extra bokeh

Add bubble/orb overlays for more depth:

```html
<section class="aero-hero">
  <div class="aero-hero-bokeh"></div>
  <div class="aero-hero-content">
    <h1>Hero Headline</h1>
  </div>
</section>
```

```css
.aero-hero {
  position: relative;
  background: var(--aero-aurora-bg);
}

.aero-hero-bokeh {
  position: absolute;
  inset: 0;
  background:
    radial-gradient(circle at 15% 20%, rgba(255, 255, 255, 0.5) 0%, transparent 6%),
    radial-gradient(circle at 60% 40%, rgba(255, 255, 255, 0.3) 0%, transparent 8%),
    radial-gradient(circle at 80% 75%, rgba(60, 218, 86, 0.4) 0%, transparent 10%),
    radial-gradient(circle at 30% 70%, rgba(85, 168, 211, 0.3) 0%, transparent 12%),
    radial-gradient(circle at 90% 20%, rgba(255, 255, 255, 0.4) 0%, transparent 7%);
  filter: blur(1px);
  pointer-events: none;
}

.aero-hero-content {
  position: relative;
  z-index: 1;
}
```

Result: aurora + scattered light "bokeh" orbs floating in space.

## 4. WebGL shader (premium)

For signature-tier projects, use Three.js or a shader library. Quick recipe with [shadergradient.co](https://shadergradient.co) or similar generator:

Generate gradient → export → embed as canvas.

Or hand-write:

```js
import { createNoise2D } from 'simplex-noise';

const canvas = document.getElementById('aurora-canvas');
const ctx = canvas.getContext('2d');
const noise = createNoise2D();

function animate(time) {
  const w = canvas.width;
  const h = canvas.height;
  const imageData = ctx.createImageData(w, h);
  
  for (let y = 0; y < h; y += 4) {
    for (let x = 0; x < w; x += 4) {
      const n = noise(x * 0.005, y * 0.005 + time * 0.0001);
      const greenChannel = Math.max(0, n * 100 + 50);
      // ... build aurora color per pixel
    }
  }
  
  ctx.putImageData(imageData, 0, 0);
  requestAnimationFrame(animate);
}
```

This is heavy — only justify for premium client work. CSS animated version covers 90% of cases.

## 5. Grass / nature ground layer (Frutiger Eco specific)

For Frutiger Eco variant, replace bottom with grass macro photo:

```css
.aero-hero-eco {
  position: relative;
  min-height: 80vh;
  background:
    /* Aurora layers on top */
    radial-gradient(ellipse at 30% 20%, rgba(60, 218, 86, 0.4), transparent 50%),
    /* Grass photo bottom */
    linear-gradient(to bottom, transparent 60%, rgba(0, 0, 0, 0.4) 100%),
    url('/img/grass-macro.webp') center bottom / cover,
    linear-gradient(180deg, hsl(200, 75%, 65%), hsl(140, 50%, 50%));
}
```

Use period-correct grass macro from Asadal stock library or own photography. Avoid AI-generated.

## 6. Solid-color "Aero ground" for non-hero sections

When hero ends, transition to softer background for content:

```css
.aero-content-section {
  background: linear-gradient(
    180deg,
    var(--grey-50) 0%,
    var(--aero-green-50) 100%
  );
  padding: var(--space-8) var(--space-4);
}
```

Subtle tint maintains aesthetic continuity.

## Variant-specific tweaks

### Bright Aero hero
Lighter aurora — replace dark base with light sky:
```css
linear-gradient(180deg, hsl(200, 80%, 80%), hsl(140, 50%, 90%))
```

### Dark Aero hero
Default `--aero-aurora-bg` works well.

### Frutiger Aurora variant
Push aurora intensity — saturated greens, magentas, lens flares:
```css
background:
  radial-gradient(ellipse at 30% 50%, rgba(60, 218, 86, 0.7), transparent 40%),
  radial-gradient(ellipse at 70% 50%, rgba(255, 80, 200, 0.5), transparent 40%),
  /* lens flare */
  radial-gradient(circle at 80% 30%, rgba(255, 255, 200, 0.6) 0%, transparent 5%),
  radial-gradient(circle at 80% 30%, rgba(255, 200, 100, 0.4) 0%, transparent 12%),
  #0a0a0f;
```

### Helvetica Aqua variant
Underwater feel — deeper blues + cyan:
```css
background:
  radial-gradient(ellipse at 30% 20%, rgba(95, 200, 250, 0.5), transparent 50%),
  radial-gradient(ellipse at 70% 70%, rgba(50, 100, 200, 0.6), transparent 50%),
  linear-gradient(180deg, hsl(200, 70%, 30%), hsl(220, 80%, 15%));
```

## Common mistakes

| ❌ Mistake | ✅ Fix |
|-----------|--------|
| Single linear-gradient as "aurora" | Use 3-4 radial gradients layered |
| Animation too fast (<5s cycle) | 15-25s slow drift, ambient feel |
| No reduced-motion respect | Always include `@media (prefers-reduced-motion: reduce)` |
| Aurora as full background distracting from content | Combine with semi-transparent dark overlay below content |
| Hero text on aurora has low contrast | Add `text-shadow: 0 2px 8px rgba(0,0,0,0.5)` or solid overlay |
| AI-generated aurora as image | Community is anti-AI — use CSS or hand-crafted shader |
| Heavy WebGL on low-end mobile | Test FPS on cheapest phones, downgrade if needed |

## Accessibility on aurora

- ✅ Test all text on aurora for WCAG AA (4.5:1)
- ✅ If contrast borderline, add semi-transparent dark scrim
- ✅ `prefers-reduced-motion` respected
- ✅ Don't auto-play with audio
- ✅ Avoid flashing/strobing patterns

## Text overlay on aurora

```css
.aero-hero h1 {
  font-size: var(--text-6xl);
  font-weight: 700;
  color: white;
  text-shadow:
    0 2px 8px rgba(0, 0, 0, 0.5),
    0 0 24px rgba(0, 0, 0, 0.3);
  line-height: var(--leading-tight);
  max-width: 800px;
}
```

For aurora variant with extreme background, use a scrim card:

```html
<section class="aero-hero">
  <!-- aurora -->
  <div class="aero-hero-scrim">
    <h1>Hero text in scrim</h1>
  </div>
</section>
```

```css
.aero-hero-scrim {
  background: rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: var(--radius-xl);
  padding: var(--space-7);
  max-width: 720px;
}
```
