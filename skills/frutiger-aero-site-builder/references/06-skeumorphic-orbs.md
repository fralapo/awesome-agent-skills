# Skeumorphic Orbs — Logo Treatment + 3D Bubble Signatures

The orb is a Frutiger Aero signature element. Use sparingly — one strong orb = memorable; orbs everywhere = noise.

## Where to use orbs

- **Logo treatment** — center your brand mark in a glossy orb
- **Hero element** — large floating orb as visual anchor
- **Navigation start menu** — round home-orb (Vista pattern, replicated by frutiger-aero.neocities.org)
- **Status indicator** — colored orb showing state
- **Section dividers** — subtle small orbs as decoration

## Recipe 1 — Pure CSS orb (no image)

```html
<div class="aero-orb"></div>
```

```css
.aero-orb {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  position: relative;
  
  /* Radial gradient — light hits top-left */
  background: radial-gradient(
    circle at 30% 30%,
    rgba(255, 255, 255, 0.95) 0%,
    var(--aero-green-500) 40%,
    var(--aero-green-700) 100%
  );
  
  /* Multi-layer shadows for depth */
  box-shadow:
    inset 0 -15px 25px rgba(0, 0, 0, 0.3),   /* bottom darkness inside */
    inset 0 10px 20px rgba(255, 255, 255, 0.4), /* top highlight inside */
    0 8px 20px rgba(0, 0, 0, 0.4),           /* drop shadow */
    0 0 0 1px rgba(0, 0, 0, 0.2);            /* edge definition */
}

/* Top reflection highlight */
.aero-orb::before {
  content: '';
  position: absolute;
  top: 8%;
  left: 18%;
  width: 64%;
  height: 30%;
  border-radius: 50%;
  background: linear-gradient(
    to bottom,
    rgba(255, 255, 255, 0.7),
    transparent
  );
  filter: blur(3px);
  pointer-events: none;
}
```

Result: 3D glossy green sphere with realistic highlight + shadow.

## Recipe 2 — Orb with embedded icon/logo

```html
<div class="aero-orb-icon">
  <svg class="aero-orb-svg" viewBox="0 0 24 24">
    <!-- your icon path -->
  </svg>
</div>
```

```css
.aero-orb-icon {
  /* Use base orb styles */
  position: relative;
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: radial-gradient(
    circle at 30% 30%,
    rgba(255, 255, 255, 0.9) 0%,
    var(--aero-green-500) 40%,
    var(--aero-green-700) 100%
  );
  box-shadow:
    inset 0 -10px 20px rgba(0, 0, 0, 0.3),
    inset 0 8px 16px rgba(255, 255, 255, 0.4),
    0 6px 15px rgba(0, 0, 0, 0.4);
  display: flex;
  align-items: center;
  justify-content: center;
}

.aero-orb-svg {
  width: 40%;
  height: 40%;
  color: white;
  /* Slight inset shadow makes icon feel "embedded" in glass */
  filter: drop-shadow(0 1px 2px rgba(0, 0, 0, 0.4));
  position: relative;
  z-index: 1;
}
```

## Recipe 3 — Floating bubble (multiple orbs, decorative)

For aurora hero backgrounds with floating bubbles:

```html
<section class="aero-hero">
  <div class="aero-bubble aero-bubble-1"></div>
  <div class="aero-bubble aero-bubble-2"></div>
  <div class="aero-bubble aero-bubble-3"></div>
  <h1>Hero Content</h1>
</section>
```

```css
.aero-bubble {
  position: absolute;
  border-radius: 50%;
  background: radial-gradient(
    circle at 30% 30%,
    rgba(255, 255, 255, 0.6) 0%,
    rgba(120, 180, 255, 0.4) 40%,
    rgba(60, 100, 200, 0.2) 100%
  );
  box-shadow:
    inset 0 -10px 20px rgba(0, 0, 0, 0.1),
    inset 0 5px 15px rgba(255, 255, 255, 0.3),
    0 4px 20px rgba(255, 255, 255, 0.2);
  pointer-events: none;
}

.aero-bubble::before {
  content: '';
  position: absolute;
  top: 10%;
  left: 15%;
  width: 50%;
  height: 25%;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.5);
  filter: blur(2px);
}

.aero-bubble-1 {
  width: 80px; height: 80px;
  top: 20%; left: 10%;
  animation: float-bubble 8s ease-in-out infinite;
}

.aero-bubble-2 {
  width: 60px; height: 60px;
  top: 60%; right: 15%;
  animation: float-bubble 11s ease-in-out infinite reverse;
}

.aero-bubble-3 {
  width: 40px; height: 40px;
  top: 40%; left: 60%;
  animation: float-bubble 6s ease-in-out infinite;
}

@keyframes float-bubble {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-30px); }
}

@media (prefers-reduced-motion: reduce) {
  .aero-bubble { animation: none; }
}
```

## Recipe 4 — Vista-style Start orb (navigation)

Replicates Windows Vista / Aero archive site start button.

```html
<button class="aero-start-orb" aria-label="Menu">
  <svg viewBox="0 0 32 32" class="aero-start-orb-icon">
    <!-- Windows-style 4-quadrant logo or your mark -->
  </svg>
</button>
```

```css
.aero-start-orb {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  border: 1px solid rgba(0, 0, 0, 0.5);
  background: radial-gradient(
    circle at 30% 25%,
    rgba(255, 255, 255, 0.95) 0%,
    var(--aero-green-400) 40%,
    var(--aero-green-700) 100%
  );
  box-shadow:
    inset 0 -8px 16px rgba(0, 0, 0, 0.3),
    inset 0 5px 12px rgba(255, 255, 255, 0.5),
    0 3px 8px rgba(0, 0, 0, 0.4),
    0 0 12px rgba(60, 218, 86, 0.3);   /* outer green glow */
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 200ms var(--ease-out);
}

.aero-start-orb:hover {
  box-shadow:
    inset 0 -8px 16px rgba(0, 0, 0, 0.3),
    inset 0 5px 12px rgba(255, 255, 255, 0.6),
    0 5px 12px rgba(0, 0, 0, 0.5),
    0 0 24px rgba(60, 218, 86, 0.6);   /* stronger glow on hover */
}

.aero-start-orb:active {
  transform: scale(0.96);
}
```

## Color variants

The recipe pattern with different colors:

| Color | Light stop | Mid stop | Dark stop |
|-------|------------|----------|-----------|
| Green (default) | `rgba(255,255,255,0.95)` | `var(--aero-green-500)` | `var(--aero-green-700)` |
| Blue | `rgba(255,255,255,0.95)` | `var(--aero-blue-500)` | `var(--aero-blue-700)` |
| Red (warning) | `rgba(255,255,255,0.95)` | `hsl(0, 80%, 55%)` | `hsl(0, 80%, 30%)` |
| Yellow | `rgba(255,255,255,0.95)` | `hsl(48, 100%, 60%)` | `hsl(38, 100%, 35%)` |
| Purple | `rgba(255,255,255,0.95)` | `hsl(280, 70%, 60%)` | `hsl(280, 80%, 30%)` |

## Where light comes from

By convention, **light from top-left** (matches Refactoring UI light source).

The `30% 30%` position in radial gradient = highlight origin. Adjust per design but keep consistent across all orbs in same project.

## Sizes by use case

```css
.aero-orb-sm  { width: 32px;  height: 32px; }  /* badge, status */
.aero-orb-md  { width: 64px;  height: 64px; }  /* logo small */
.aero-orb-lg  { width: 120px; height: 120px; } /* hero anchor */
.aero-orb-xl  { width: 200px; height: 200px; } /* signature element */
```

## Animation patterns

### Subtle pulse (status indicator)
```css
.aero-orb-pulse {
  animation: aero-pulse 2s ease-in-out infinite;
}

@keyframes aero-pulse {
  0%, 100% { box-shadow: /* base */, 0 0 0 0 rgba(60,218,86,0.4); }
  50%      { box-shadow: /* base */, 0 0 0 8px rgba(60,218,86,0); }
}
```

### Rotation (logo signature)
```css
.aero-orb-spin:hover {
  transform: rotate(15deg);
  transition: transform 0.4s ease-out;
}
```

### Float (decorative)
See bubble animation above.

## Common mistakes

| ❌ Mistake | ✅ Fix |
|-----------|--------|
| Light highlight from wrong direction | Keep top-left consistency (`30% 30%`) |
| Solid color instead of radial gradient | Always use radial-gradient for 3D feel |
| Missing inset shadows | Need BOTH inset dark (bottom) AND inset light (top) for sphere illusion |
| Skip ::before highlight | The crisp reflective spot is signature |
| Too many orbs everywhere | One signature orb > many decorative orbs |
| Orb as button without keyboard support | Use semantic `<button>`, add focus state |
| Static orbs in animated hero | If bubbles, animate them; or skip entirely |

## Accessibility for orbs

- ✅ Decorative orbs: `aria-hidden="true"` + `pointer-events: none`
- ✅ Functional orbs (buttons): semantic `<button>` + accessible label
- ✅ Status orbs: complement with text label, never color alone
- ✅ Animated orbs: respect `prefers-reduced-motion`
- ✅ Touch targets ≥44px even if visual orb is smaller (use padding)

## Real example — hero with anchor orb

```html
<section class="aero-hero">
  <div class="aero-hero-content">
    <div class="aero-orb aero-orb-lg aero-orb-hero" aria-hidden="true"></div>
    <h1>Welcome to [Brand]</h1>
    <p class="aero-hero-subhead">Optimistic tagline here.</p>
    <button class="aero-btn aero-btn-primary aero-btn-lg">Get Started</button>
  </div>
</section>
```

```css
.aero-orb-hero {
  margin: 0 auto var(--space-5);
  animation: float-bubble 6s ease-in-out infinite;
}
```
