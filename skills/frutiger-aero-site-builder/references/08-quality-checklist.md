# Quality Checklist — Pre-launch Verification

Run all checks before client delivery / production launch.

## Brand authenticity (Frutiger Aero specific)

- [ ] **Variant chosen + consistent** (Bright / Dark / Eco / Aurora / Aqua / Neo — see `references/01-aesthetic-variants.md`)
- [ ] **No mixing** of opposing variants (Bright + Dark in same site = visual chaos)
- [ ] **Glossy gradient with hard mid-break** present on primary CTA (`references/03-glossy-buttons.md`)
- [ ] **Aurora background** properly layered (3+ radial gradients, not single linear)
- [ ] **Period-correct typography** (Segoe UI stack OR explicit modern alternative)
- [ ] **Aero green** is `#3cda56` family, not generic `#22c55e` Tailwind default
- [ ] **Signature element present** (orb, custom cursor, aurora animation, etc.)
- [ ] **Imagery period-authentic** (Asadal sources or own photography, NOT generic stock)

## Anti-default check

- [ ] **NO Inter** as primary font (or explicit justification for Neo Aero variant)
- [ ] **NO Roboto** as primary font
- [ ] **NO purple gradient on white** (Anthropic-warned cliché)
- [ ] **NO generic colored-circle icons everywhere**
- [ ] **NO "diverse team smiling around laptop"** stock photo
- [ ] **NO shadcn/ui default theme** untouched
- [ ] **NO AI-generated FA hero imagery** (community is anti-AI — see [[Future We Were Promised]])
- [ ] **Layout breaks centered-card default** (asymmetry, overlap, or editorial)

## Accessibility (WCAG 2.1 AA)

### Color contrast
- [ ] **Body text** ≥ 4.5:1 against background
- [ ] **Large text** (≥18pt or 14pt bold) ≥ 3:1
- [ ] **UI components** (button borders, icons) ≥ 3:1
- [ ] **Text on aurora bg** verified at all positions (use scrim if needed)
- [ ] **Text on glass panels** verified for various underlying backgrounds

### Keyboard navigation
- [ ] **Tab reaches all interactive elements** in logical order
- [ ] **`:focus-visible` outlines** present everywhere (no `outline: none` without replacement)
- [ ] **Skip link** to main content
- [ ] **No keyboard traps**
- [ ] **Modal focus trap** + ESC closes + restore focus

### Semantic HTML
- [ ] **`<button>` for actions**, NOT `<div onClick>`
- [ ] **`<a href>` for navigation**, NOT `<div onClick>`
- [ ] **Heading hierarchy** sequential (h1 → h2 → h3, no skipping)
- [ ] **Form inputs have `<label>`** (not just placeholder)
- [ ] **Semantic landmarks** (`<header>`, `<nav>`, `<main>`, `<footer>`)
- [ ] **Image alt text** descriptive (or empty for decorative)

### ARIA
- [ ] **`aria-label`** on icon-only buttons
- [ ] **`aria-live`** for dynamic content updates
- [ ] **`aria-modal="true"`** on dialogs
- [ ] **No redundant ARIA** (`<button role="button">` is wrong)

### Touch + motion
- [ ] **Touch targets ≥ 44×44px** (Apple HIG)
- [ ] **`prefers-reduced-motion`** respected (all CSS animations disabled when set)
- [ ] **No autoplay media** without user control
- [ ] **No flashing** > 3 times per second

### Test with assistive tech
- [ ] **Keyboard-only test** (unplug mouse, complete primary tasks)
- [ ] **Screen reader spot-check** (NVDA Windows or VoiceOver Mac)
- [ ] **axe DevTools scan** — 0 violations
- [ ] **Lighthouse a11y score** ≥ 95

## Performance (Core Web Vitals)

| Metric | Target | Tool |
|--------|--------|------|
| **LCP** | < 2.5s | Lighthouse / Web Vitals |
| **INP** | < 200ms | Web Vitals |
| **CLS** | < 0.1 | Web Vitals |
| **FCP** | < 1.5s | Lighthouse |
| **TBT** | < 200ms | Lighthouse |

### Asset budget
- [ ] **JavaScript** < 150KB gzipped (landing) / < 300KB (app)
- [ ] **CSS** < 50KB
- [ ] **Hero image** < 200KB (AVIF/WebP preferred)
- [ ] **Total page weight** < 1MB initial load

### Optimizations
- [ ] **Images**: AVIF + WebP fallback + lazy loading
- [ ] **Fonts**: subset + `font-display: swap` + preload critical
- [ ] **`backdrop-filter`**: reduced on mobile breakpoints
- [ ] **Critical CSS**: inlined for above-fold
- [ ] **Non-critical JS**: deferred or async
- [ ] **No render-blocking resources**

## Responsive (6-tier breakpoints)

Test each:
- [ ] **XS 320-479px** — single column, ≥44px touch, hamburger nav
- [ ] **SM 480-767px** — single column, simplified UI
- [ ] **MD 768-1023px** — 2-col layouts possible
- [ ] **LG 1024-1439px** — multi-col, full nav
- [ ] **XL 1440-1919px** — bounded max-width
- [ ] **2XL 1920px+** — no overstretch

### Mobile-specific
- [ ] **Hover states** have touch equivalents (or removed)
- [ ] **Fixed elements** don't cover content
- [ ] **Forms** stack properly
- [ ] **Modals/dropdowns** fit viewport
- [ ] **No horizontal scroll** (unless intentional)

## Cross-browser

- [ ] **Chrome** (latest)
- [ ] **Firefox** (latest)
- [ ] **Safari** (latest, both desktop + iOS)
- [ ] **Edge** (Chromium-based)

### Safari-specific quirks
- [ ] **`-webkit-backdrop-filter`** prefix present
- [ ] **`-webkit-` prefixes** for transform, transition, animation (if old Safari support needed)
- [ ] **Date inputs** work (Safari renders differently)
- [ ] **No `dialog` element issues** (Safari < 15.4 needs polyfill)

## SEO + meta

- [ ] **`<title>`** descriptive, under 60 chars
- [ ] **`<meta name="description">`** under 160 chars
- [ ] **Open Graph tags** (og:title, og:description, og:image)
- [ ] **Twitter Card meta**
- [ ] **Favicon set** (ico + apple-touch-icon + svg)
- [ ] **`<html lang>`** specified
- [ ] **Canonical URL** if multi-domain
- [ ] **robots.txt + sitemap.xml** if public site
- [ ] **Structured data** (JSON-LD) for relevant content

## Content + UX

- [ ] **No lorem ipsum** remaining
- [ ] **All links work** (no 404s, no `href="#"` placeholders)
- [ ] **All images have alt text**
- [ ] **No spelling errors** (run spellcheck)
- [ ] **Consistent voice/tone** across pages
- [ ] **Error states designed** (404, form errors, network failure)
- [ ] **Loading states designed** (skeleton or spinner)
- [ ] **Empty states designed** (no data scenarios)

## Privacy + legal

- [ ] **Cookie banner** if EU users + tracking
- [ ] **Privacy policy** linked in footer
- [ ] **Terms of service** linked if applicable
- [ ] **GDPR-compliant analytics** (Plausible, Fathom — avoid GA4 without consent)
- [ ] **No third-party trackers** without disclosure
- [ ] **Contact form**: privacy notice next to submit

## Security

- [ ] **HTTPS** only (no mixed content)
- [ ] **Content Security Policy** header configured
- [ ] **`X-Frame-Options`** to prevent clickjacking
- [ ] **No exposed API keys** in client code
- [ ] **Form CSRF protection** for state-changing actions
- [ ] **`rel="noopener noreferrer"`** on `target="_blank"` links

## Production verification

After deploy:
- [ ] **Test from real device** (not just DevTools simulation)
- [ ] **Verify analytics firing**
- [ ] **Test all forms** with real submission
- [ ] **Verify email notifications** (if any)
- [ ] **Check 404 page** displays correctly
- [ ] **Check robots indexing** allowed (or blocked appropriately)
- [ ] **Performance from real users** (RUM data after 1-2 days)

## Frutiger Aero specific gotchas

- [ ] **Glossy gradient** displays correctly on Safari (test specifically)
- [ ] **Backdrop-filter** has fallback for older browsers
- [ ] **Aurora animation** doesn't drain battery (test mobile 30 min)
- [ ] **Text shadow** on glass surfaces hasn't bled (Windows ClearType differences)
- [ ] **Custom cursors** only on desktop (mobile ignores anyway)
- [ ] **Reduced motion** respected — aurora freezes appropriately
- [ ] **Print stylesheet** if relevant (FA aesthetic doesn't print well — provide simplified version)

## Sign-off

Once ALL above checked:
- [ ] **Client demo** (live walkthrough)
- [ ] **Client approval** (written)
- [ ] **Backups created** (Git tagged release)
- [ ] **Documentation handed off** (if dev maintenance separate)
- [ ] **Post-launch monitoring** plan (analytics review schedule)

## If any check fails

Don't skip. Either:
1. **Fix** the issue (most cases)
2. **Document accepted trade-off** in writing with client agreement
3. **Postpone launch** if blocker (a11y violations, perf disasters)

Never ship known critical violations.

## Continuous improvement

After launch, weekly review:
- Real performance data (CWV reports)
- User behavior analytics (where do they drop off?)
- Accessibility complaints
- Cross-browser bug reports

Iterate based on real data, not assumptions.
