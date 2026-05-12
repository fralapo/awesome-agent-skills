# Aesthetic Variants — Which Frutiger Aero?

Frutiger Aero is an umbrella aesthetic. Pick ONE variant per project. Mixing variants confuses the brand.

## Variant comparison

| Variant | Mood | Use case | Theme switch |
|---------|------|----------|--------------|
| **Bright Aero** | Light, optimistic, "summer 2007" | Consumer products, mass market, indie creative | `:root` default |
| **Dark Aero** | Premium, mature, mysterious | Tech/dev tools, premium products, gaming | `data-theme="dark-aero"` |
| **Frutiger Eco** | Sustainable, green-heavy, nature-focused | Eco-tech, climate, wellness | `data-theme="frutiger-eco"` |
| **Frutiger Aurora** | Cosmic, lens-flare, abstract tech | Music, nightlife, sci-fi adjacent | (custom — heavy aurora bg) |
| **Helvetica Aqua Aero** | Sea, tropical, Y2K crossover | Beach, wellness, aquatic | (custom — blue/cyan palette) |
| **Neo Aero (2022+)** | Modern revival, knowing nostalgia | Portfolio, indie projects, brand work | Soft mid-break gradients |

## Detailed variant guides

### 1. Bright Aero (default)

**Mood**: Optimistic, glossy, "summer afternoon Windows Vista 2007"

**Palette**:
- Background: white / light grey (`--grey-50`)
- Primary: Aero green (`--aero-green-500`)
- Secondary: Aero blue (`--aero-blue-500`)
- Text: dark grey (`--grey-900`)

**Hero**: Aurora-into-grass background with floating glass UI

**Best for**:
- Consumer-facing landing pages
- Indie creative portfolios
- Optimistic brand identities
- Eco-tech (combined with Eco variant)

**Avoid for**:
- Conservative B2B
- Finance/legal/medical
- Brands wanting "mature" or "serious"

### 2. Dark Aero

**Mood**: Premium, mysterious, business-oriented (Vista glass + dark mode = Mata Nero / Frutiger Ego)

**Palette**:
- Background: deep grey/black (`--grey-900`)
- Primary: Aero green (`--aero-green-500`) — pops against dark
- Text: light grey (`--grey-50`)
- Accent glow: `--aero-green-glow`

**Hero**: Dark aurora + glass panels with strong gloss highlights

**Best for**:
- Premium tech / dev tools
- Music streaming
- Gaming UI
- High-end portfolios

**Avoid for**:
- Bright sunny content
- Kids products
- Wellness apps (too premium-cold)

### 3. Frutiger Eco

**Mood**: Sustainable, lush, "tech-meets-nature harmony" — peak utopian period feel

**Palette**:
- Background: warm green tint (`hsl(140, 25%, 96%)`)
- Primary: deep green (`--aero-green-700`)
- Imagery: lush greenery, water droplets, blue skies, solar panels
- Avoid: aggressive saturation

**Hero**: Macro grass photo + glass UI overlay + maybe small wind turbine illustration

**Best for**:
- Eco-tech brands
- Climate / sustainability
- AI wellness
- B-Corp / mission-driven

**Avoid for**:
- Aggressively commercial (community will read as greenwashing — see Greenwashing in Frutiger Aero)
- Conservative B2B

**Critical**: substance must match aesthetic. Frutiger Eco visual on non-eco brand = greenwashing trap.

### 4. Frutiger Aurora

**Mood**: Cosmic, abstract-tech, lens-flare-heavy

**Palette**:
- Background: dark navy/midnight purple
- Aurora gradients: green + cyan + magenta layered
- Accents: bright glows, sharp contrast

**Hero**: Full-screen aurora animation + small/centered content

**Best for**:
- Music brands
- Nightlife
- Sci-fi tech
- Album covers

**Avoid for**:
- Daytime / professional contexts
- Content-heavy pages (aurora distracts)

### 5. Helvetica Aqua Aero (Y2K crossover)

**Mood**: Tropical, aquatic, Y2K-summer

**Palette**:
- Background: deep ocean blue → tropical cyan
- Primary: cyan/teal
- Imagery: tropical fish, water droplets, beach scenes

**Hero**: Underwater scene or beach with glass UI

**Best for**:
- Surfing / aquatic
- Wellness (hydration focus)
- Travel / tropical
- Cosmetics

### 6. Neo Aero (2022+ modern revival)

**Mood**: Knowing nostalgia, "we know the 2000s techno-utopia was a lie, but we love the aesthetic"

**Differences from period-accurate**:
- **Soft mid-break** gradients (2-4% transition, not hard 0%)
- Modern typography (Inter + characterful display vs pure Segoe UI)
- Subtler effects (less max-out on every dimension)
- Acknowledging community ethos (anti-AI, anti-corporate)
- Some ironic elements OK (memes, "Evil Frutiger Aero" references)

**Best for**:
- Portfolio sites (signals taste + cultural awareness)
- Indie creative projects
- Brand work for clients who get the cultural moment

**Tradeoff vs period-accurate**: less retro-costume, more modern-relevant.

## Decision quick checklist

Choose your variant by answering:

1. **Light or dark?**
   - Light → Bright Aero / Frutiger Eco / Helvetica Aqua
   - Dark → Dark Aero / Frutiger Aurora

2. **Period-accurate or modern revival?**
   - 2007 feel → use hard mid-break gradients, Segoe UI, period imagery (Asadal)
   - 2026 revival → soft mid-break, modern typography, knowing references

3. **Eco substance?**
   - Genuinely eco brand → Frutiger Eco
   - Not eco → avoid Eco variant (community-read as greenwashing)

4. **Cosmic/music?**
   - Yes → Frutiger Aurora
   - No → other variants

5. **Aquatic theme?**
   - Yes → Helvetica Aqua Aero
   - No → other variants

## Mixing rules

- ✅ Bright Aero + Frutiger Eco: same family, can blend
- ✅ Dark Aero + Frutiger Aurora: both dark, can blend in specific sections
- ❌ Bright Aero + Dark Aero in same site (commit to ONE)
- ❌ Frutiger Aero + Industrial Brutalism (opposite aesthetics)
- ⚠️ Frutiger Aero + Liquid Glass: technically possible (both glass-based), but visually overlapping in confusing ways

## What this changes in your build

Once variant chosen, in your CSS:

```html
<!-- Default Bright Aero -->
<html>

<!-- Dark Aero -->
<html data-theme="dark-aero">

<!-- Frutiger Eco -->
<html data-theme="frutiger-eco">
```

For Aurora/Aqua/Neo variants: also customize background recipes (see `references/05-aurora-backgrounds.md`) and possibly typography stack.
