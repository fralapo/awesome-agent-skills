# Glossy Buttons — Period-Accurate Frutiger Aero CTAs

## Why this matters

The **glossy gradient with hard mid-break** is THE signature of Frutiger Aero. Get this wrong and the whole aesthetic falls apart. This is the single most distinctive CSS pattern of the era.

## The hard mid-break (critical)

```css
/* PERIOD ACCURATE — same percentage on both stops = zero transition */
background: linear-gradient(to bottom,
  #fff 0%,
  #82f577 3%,
  #32912a 40%,
  #185815 55%,    /* HARD BREAK starts */
  #0b3112 55%,    /* HARD BREAK ends (SAME %) */
  #1a5c1e 100%);
```

The `55%` to `55%` (zero gap) creates the sharp reflection line that says "glass / polished plastic."

Smooth gradient = "wet paint" feel — wrong era. If revision client wants softer, see "Modern soft variant" below.

## Primary green CTA — complete recipe

```html
<button class="aero-btn aero-btn-primary">
  Get Started
</button>
```

```css
.aero-btn {
  position: relative;
  padding: 12px 24px;
  border: 1px solid #000;
  border-radius: 8px;
  font-family: var(--aero-font-body);
  font-size: 14px;
  font-weight: 500;
  color: white;
  cursor: pointer;
  transition: filter 150ms var(--ease-out);
  text-shadow: 0 1px 1px rgba(0, 0, 0, 0.4);
}

.aero-btn-primary {
  background: var(--aero-gloss-button-green);
  box-shadow:
    1px 1px 5px rgba(0, 0, 0, 0.3),
    inset 0 1px 0 rgba(255, 255, 255, 0.4);
}

/* Reflection sweep on top half */
.aero-btn-primary::before {
  content: '';
  position: absolute;
  top: 1px;
  left: 1px;
  right: 1px;
  height: 45%;
  border-radius: 7px 7px 0 0;
  background: linear-gradient(to bottom,
    rgba(255, 255, 255, 0.4),
    rgba(255, 255, 255, 0.05));
  pointer-events: none;
}

.aero-btn-primary:hover {
  filter: brightness(1.1);
}

.aero-btn-primary:active {
  filter: brightness(0.95);
  transform: translateY(1px);
}

.aero-btn-primary:focus-visible {
  outline: 2px solid var(--aero-green-glow);
  outline-offset: 2px;
}
```

## All button states (mandatory)

Every button MUST have these states defined:

| State | Visual change |
|-------|---------------|
| Default | Base gradient + gloss |
| Hover | `filter: brightness(1.1)` |
| Active | `filter: brightness(0.95) translateY(1px)` |
| Focus | 2px outline with `--aero-green-glow` |
| Disabled | `opacity: 0.5 cursor: not-allowed` + remove ::before |
| Loading | Spinner inside, button non-interactive |

```css
.aero-btn:disabled,
.aero-btn[aria-disabled="true"] {
  opacity: 0.5;
  cursor: not-allowed;
  filter: grayscale(0.3);
}

.aero-btn:disabled::before {
  display: none;
}

.aero-btn[data-loading="true"] {
  pointer-events: none;
  color: transparent;
}

.aero-btn[data-loading="true"]::after {
  content: '';
  position: absolute;
  inset: 0;
  margin: auto;
  width: 16px;
  height: 16px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-top-color: white;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
```

## Secondary button variant (outline glass)

```css
.aero-btn-secondary {
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(8px);
  border: 1px solid var(--color-border-glass);
  color: var(--color-text-primary);
  box-shadow:
    inset 0 1px 0 rgba(255, 255, 255, 0.3),
    0 2px 6px rgba(0, 0, 0, 0.15);
}

.aero-btn-secondary::before {
  /* No reflection sweep on secondary */
  display: none;
}

.aero-btn-secondary:hover {
  background: rgba(255, 255, 255, 0.25);
}
```

## Tertiary button variant (text-only link style)

```css
.aero-btn-tertiary {
  background: transparent;
  border: none;
  color: var(--color-accent);
  padding: 8px 12px;
  box-shadow: none;
  text-shadow: 0 0 3px rgba(0, 0, 0, 0.2);
}

.aero-btn-tertiary::before {
  display: none;
}

.aero-btn-tertiary:hover {
  text-decoration: underline;
  text-underline-offset: 3px;
}
```

## Color variants

### Blue button (alternate primary)
```css
.aero-btn-blue {
  background: var(--aero-gloss-button-blue);
}
```

### Custom colors

To create new button color, follow the gradient pattern:
1. White highlight (top, 0%)
2. Light shade (3%, very bright)
3. Mid shade (40%, base color saturated)
4. Dark shade (55%, HARD BREAK starts)
5. Darker shade (55%, HARD BREAK ends)
6. Bottom shade (100%, slightly lighter than darker)

Example purple:
```css
--aero-gloss-button-purple: linear-gradient(to bottom,
  #fff 0%,
  #d094f5 3%,
  #7d2cb3 40%,
  #4b0d80 55%,
  #2c0454 55%,
  #531a8c 100%);
```

## Modern soft variant (Neo Aero)

If client wants more modern feel (2024+ revival), use 4% transition instead of hard break:

```css
--aero-gloss-button-green-soft: linear-gradient(to bottom,
  #fff 0%,
  #82f577 3%,
  #32912a 40%,
  #185815 52%,
  #0b3112 56%,    /* 4% gap = subtle transition */
  #1a5c1e 100%);
```

Tradeoff: less period-accurate, more "modern revival" feel. Use soft for portfolio/brand work; hard for nostalgic projects.

## Sizes

```css
.aero-btn-sm  { padding: 8px 16px;  font-size: 12px; }
.aero-btn-md  { padding: 12px 24px; font-size: 14px; } /* default */
.aero-btn-lg  { padding: 16px 32px; font-size: 16px; }
.aero-btn-xl  { padding: 20px 40px; font-size: 18px; }
```

## Common mistakes

| ❌ Mistake | ✅ Fix |
|-----------|--------|
| Smooth gradient (no break) | Hard break at 55%/55% or soft at 52%/56% |
| Missing reflection ::before | Add top 45% reflection sweep |
| Generic green (`#10b981` / `#22c55e`) | Use `--aero-green-500` family (specific period palette) |
| No text-shadow on label | Add `0 1px 1px rgba(0,0,0,0.4)` for depth |
| No focus state | Always provide `:focus-visible` outline |
| Border-radius too large (15px+) | Keep 6-10px for period feel |
| Centered button forever | Vary placement — full-width on mobile, contextual on desktop |
| Same gradient for primary + secondary | Secondary should be GLASS (outline) not gloss |

## Accessibility checks

- ✅ Touch target ≥ 44×44px (Fitts's Law)
- ✅ Focus indicator with 3:1 contrast against background
- ✅ Disabled state visually clear (opacity + grayscale)
- ✅ Loading state has accessible label (`aria-busy="true"` + visually hidden "Loading...")
- ✅ Use semantic `<button>` element, not `<div onClick>`
- ✅ Contrast: white text on green gradient mid-tone needs verification — use #1a5c1e+ stops (passing 4.5:1 with white)

## Real component (HTML + all states)

```html
<!-- Primary CTA -->
<button class="aero-btn aero-btn-primary aero-btn-md">
  Sign Up Free
</button>

<!-- Secondary -->
<button class="aero-btn aero-btn-secondary aero-btn-md">
  Learn More
</button>

<!-- Tertiary -->
<button class="aero-btn aero-btn-tertiary aero-btn-md">
  Skip for now
</button>

<!-- Disabled -->
<button class="aero-btn aero-btn-primary" disabled>
  Coming Soon
</button>

<!-- Loading -->
<button class="aero-btn aero-btn-primary" data-loading="true" aria-busy="true">
  Submit
</button>
```
