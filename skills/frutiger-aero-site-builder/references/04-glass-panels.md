# Glass Panels — Backdrop-filter Cards + Windows

## Core pattern

Frutiger Aero glass = combination of:
1. **Translucent background** (rgba with alpha)
2. **Backdrop filter** (blur + saturate)
3. **Inset gloss highlight** (top edge, white inset shadow)
4. **Inset shadow bottom** (depth)
5. **Drop shadow** (separation from page)
6. **Subtle border** (definition)

## Basic glass card

```html
<div class="aero-glass-card">
  <h3>Card Title</h3>
  <p>Card body content.</p>
</div>
```

```css
.aero-glass-card {
  background: var(--color-bg-glass);
  backdrop-filter: var(--aero-blur-normal);
  -webkit-backdrop-filter: var(--aero-blur-normal);  /* Safari */
  border: 1px solid var(--color-border-glass);
  border-radius: var(--radius-lg);
  padding: var(--space-5);
  box-shadow: var(--aero-shadow-glass-card);
  color: var(--color-text-primary);
}
```

### What `--aero-shadow-glass-card` provides (recap)

```css
box-shadow:
  0 10px 30px rgba(0, 0, 0, 0.25),       /* main drop */
  0 5px 10px rgba(0, 0, 0, 0.15),         /* contact occlusion */
  inset 0 1px 0 rgba(255, 255, 255, 0.2), /* top gloss */
  inset 0 -1px 0 rgba(0, 0, 0, 0.2);      /* bottom shadow */
```

## Glass with gloss overlay (Aero pure style)

For the most period-accurate "Aero Glass" effect, layer the overlay gradient:

```html
<div class="aero-window">
  <div class="aero-window-titlebar">Window Title</div>
  <div class="aero-window-body">
    Window content here.
  </div>
</div>
```

```css
.aero-window {
  position: relative;
  background: var(--color-bg-glass);
  backdrop-filter: var(--aero-blur-normal);
  -webkit-backdrop-filter: var(--aero-blur-normal);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  box-shadow: var(--aero-shadow-glass-card);
  overflow: hidden;
}

/* Top half gloss reflection — period-accurate signature */
.aero-window::before {
  content: '';
  position: absolute;
  inset: 0 0 50% 0;     /* top half only */
  background: var(--aero-glass-overlay);
  pointer-events: none;
  z-index: 1;
}

.aero-window-titlebar {
  position: relative;
  z-index: 2;
  padding: var(--space-3) var(--space-4);
  background: var(--aero-titlebar);
  color: white;
  font-weight: 500;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
  border-bottom: 1px solid #000;
}

.aero-window-body {
  position: relative;
  z-index: 2;
  padding: var(--space-5);
}
```

## Performance considerations

`backdrop-filter` is GPU-heavy. Rules:

| Context | Blur strength | Caveats |
|---------|---------------|---------|
| Mobile XS (<480px) | Skip or `blur(1px)` | Performance |
| Mobile SM (480-767px) | `blur(4px)` max | Performance |
| Tablet+ | Full blur (8-15px) | OK |

```css
.aero-glass-card {
  backdrop-filter: var(--aero-blur-normal);
}

/* Reduce on mobile */
@media (max-width: 767px) {
  .aero-glass-card {
    backdrop-filter: blur(2px);
  }
}

/* Fallback for browsers without backdrop-filter support */
@supports not (backdrop-filter: blur(1px)) {
  .aero-glass-card {
    background: rgba(20, 20, 20, 0.9);  /* solid-ish fallback */
  }
}
```

## Card variants

### Dark Aero card (default in Dark Aero theme)

The `[data-theme="dark-aero"]` already swaps `--color-bg-glass` to `rgba(27, 27, 27, 0.7)`. Component CSS unchanged.

### Featured card (more prominent gloss)

```css
.aero-glass-card-featured {
  /* base card styles */
  /* extra emphasis: */
  border: 1px solid var(--aero-green-500);
  box-shadow:
    0 0 0 1px var(--aero-green-glow),    /* outer glow */
    0 15px 40px rgba(60, 218, 86, 0.3),   /* green tinted shadow */
    var(--aero-shadow-glass-card);
}
```

### Hoverable card (interaction feedback)

```css
.aero-glass-card[role="link"],
.aero-glass-card-hover {
  cursor: pointer;
  transition: transform 200ms var(--ease-out),
              box-shadow 200ms var(--ease-out);
}

.aero-glass-card-hover:hover {
  transform: translateY(-4px);
  box-shadow:
    0 20px 40px rgba(0, 0, 0, 0.3),
    0 10px 15px rgba(0, 0, 0, 0.2),
    inset 0 1px 0 rgba(255, 255, 255, 0.3);
}

.aero-glass-card-hover:focus-visible {
  outline: 2px solid var(--color-accent);
  outline-offset: 4px;
}
```

## Nav bar (glass header)

```html
<header class="aero-nav">
  <a href="/" class="aero-nav-logo">Brand</a>
  <nav class="aero-nav-links">
    <a href="/about">About</a>
    <a href="/services">Services</a>
    <a href="/contact">Contact</a>
  </nav>
</header>
```

```css
.aero-nav {
  position: sticky;
  top: 0;
  z-index: var(--z-nav);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: var(--space-3) var(--space-5);
  background: var(--color-bg-glass);
  backdrop-filter: var(--aero-blur-normal);
  -webkit-backdrop-filter: var(--aero-blur-normal);
  border-bottom: 1px solid var(--color-border-glass);
  box-shadow:
    inset 0 1px 0 rgba(255, 255, 255, 0.2),
    0 4px 12px rgba(0, 0, 0, 0.15);
}

.aero-nav-logo {
  font-size: var(--text-xl);
  font-weight: 600;
  color: var(--color-text-primary);
  text-decoration: none;
}

.aero-nav-links {
  display: flex;
  gap: var(--space-4);
}

.aero-nav-links a {
  color: var(--color-text-secondary);
  text-decoration: none;
  font-size: var(--text-sm);
  font-weight: 500;
  padding: var(--space-2) var(--space-3);
  border-radius: var(--radius-md);
  transition: all 200ms var(--ease-out);
}

.aero-nav-links a:hover {
  color: var(--color-text-primary);
  background: rgba(255, 255, 255, 0.1);
}
```

## Modal / overlay

```html
<div class="aero-modal-backdrop" data-open="true">
  <div class="aero-modal" role="dialog" aria-modal="true" aria-labelledby="modal-title">
    <h2 id="modal-title">Confirm Action</h2>
    <p>Are you sure?</p>
    <div class="aero-modal-actions">
      <button class="aero-btn aero-btn-tertiary">Cancel</button>
      <button class="aero-btn aero-btn-primary">Confirm</button>
    </div>
  </div>
</div>
```

```css
.aero-modal-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(4px);
  z-index: var(--z-modal);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: var(--space-4);
  opacity: 0;
  pointer-events: none;
  transition: opacity var(--duration-normal) var(--ease-out);
}

.aero-modal-backdrop[data-open="true"] {
  opacity: 1;
  pointer-events: auto;
}

.aero-modal {
  max-width: 480px;
  width: 100%;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(15px) saturate(180%);
  border: 1px solid var(--color-border-glass);
  border-radius: var(--radius-xl);
  padding: var(--space-6);
  box-shadow: var(--aero-shadow-xl);
  transform: scale(0.95);
  transition: transform var(--duration-normal) var(--ease-out);
}

.aero-modal-backdrop[data-open="true"] .aero-modal {
  transform: scale(1);
}
```

## Common mistakes

| ❌ Mistake | ✅ Fix |
|-----------|--------|
| `backdrop-filter: blur(50px)` everywhere | 8-15px max — heavy values hurt performance |
| No `-webkit-backdrop-filter` | Always include for Safari |
| No `@supports` fallback | Provide solid background fallback |
| Same glass treatment for nav + cards + modal | Vary intensity: nav subtle, cards mid, modal strong |
| Border in solid color | Use `rgba()` low-opacity for glass borders |
| Forgot inset gloss shadow | The inset white highlight is the "Aero" feel — don't skip |
| Missing keyboard focus on hoverable cards | Add `:focus-visible` outline |

## Accessibility checks

- ✅ Content inside glass has sufficient contrast vs underlying background
- ✅ If using `<dialog>` element, focus trap implemented
- ✅ Hoverable cards have keyboard equivalents
- ✅ Modal: focus first interactive element on open, restore on close
- ✅ ESC closes modal
- ✅ `aria-modal="true"` + `aria-labelledby` on modal

## When NOT to use glass

- **Text-heavy article body** — glass adds visual noise to reading
- **Forms with many inputs** — translucency confuses field boundaries
- **Tables with data** — backgrounds need to be predictable for scanning
- **Charts / data viz** — backdrop unpredictability hurts data perception

Use solid panels for these contexts even in Frutiger Aero design.
