# Frutiger Aero Site Builder — Claude Code Skill

A Claude Code skill for building Frutiger Aero aesthetic websites from scratch.

## Quick start

### Install as Claude Code skill

```bash
# User-level (available across all projects)
cp -r frutiger-aero-site-builder ~/.claude/skills/

# OR project-local
cp -r frutiger-aero-site-builder /path/to/your/project/.claude/skills/
```

### Use in Claude Code session

```
Invoke the frutiger-aero-site-builder skill, then build me a Frutiger Aero landing page for an eco-tech startup.
```

Claude will:
1. Read SKILL.md (variant decision + workflow)
2. Read relevant references based on what you're building
3. Use `assets/css/aero-tokens.css` as foundation
4. Reference `examples/01-hero-landing.html` as starting template

## What's included

```
frutiger-aero-site-builder/
├── SKILL.md                              # Main entry, decision tree, workflow
├── README.md                             # This file
├── assets/
│   └── css/
│       └── aero-tokens.css               # CSS vars (Bright/Dark/Eco/Cream/Peach themes)
├── references/
│   ├── 01-aesthetic-variants.md          # Bright/Dark/Eco/Aurora/Aqua/Cream/Peach selection
│   ├── 02-design-tokens.css              # Token system reference doc
│   ├── 03-glossy-buttons.md              # Period-accurate CTA recipes + all states
│   ├── 04-glass-panels.md                # Backdrop-filter cards, nav, modals
│   ├── 05-aurora-backgrounds.md          # Hero background patterns
│   ├── 06-skeumorphic-orbs.md            # 3D bubble/orb logo treatments
│   ├── 07-build-workflow.md              # Zero-to-complete-site workflow
│   ├── 08-quality-checklist.md           # Pre-launch verification
│   ├── 09-anti-ai-pitfalls.md            # What makes FA look AI-generic (CRITICAL)
│   └── 10-period-layout-patterns.md      # Pattern A/B/C/D/E from 41 oldweb sites (CRITICAL)
└── examples/
    ├── 01-hero-landing.html              # Pattern A: Dark Aero window-chrome + sidebar + editorial
    └── 02-neocities-warm-cream.html      # Pattern A variant: cream palette indie cozy
```

## What this skill produces

Output: production-ready Frutiger Aero websites with:

- **Period-accurate** glossy gradients with hard mid-break
- **Aurora backgrounds** via layered CSS radial gradients
- **Glass panels** with backdrop-filter + inset gloss + drop shadow
- **Skeumorphic 3D orbs** for logos + signature elements
- **6 variants** (Bright, Dark, Eco, Aurora, Aqua, Neo)
- **Accessible** by default (WCAG AA, semantic HTML, keyboard nav)
- **Responsive** mobile-first across 6 breakpoint tiers
- **Performance-conscious** (backdrop-filter throttled on mobile, reduced-motion respected)

## Foundations leveraged from vault

This skill operationalizes knowledge from:
- Frutiger Aero deep documentation (16+ concept pages)
- Refactoring UI Methodology (Wathan + Schoger discipline)
- UX Cognitive Laws (Hicks, Fitts, Miller, Doherty)
- Accessibility WCAG 2.1 AA baseline
- Design Originality (anti-AI-generic discipline)
- 5-source consensus on anti-default frontend

## Variant decision quick reference

| Project type | Variant |
|--------------|---------|
| Eco-tech / sustainability | Frutiger Eco |
| AI wellness / mindfulness | Bright Aero |
| Premium tech / dev tools | Dark Aero |
| Portfolio / creative | Neo Aero |
| Music / nightlife | Frutiger Aurora |
| Beach / wellness / aquatic | Helvetica Aqua Aero |

## Time estimates

| Project | Hours |
|---------|-------|
| Simple landing page | 6-10 |
| Multi-page marketing site | 30-50 |
| Web app with FA aesthetic | 60-120 |

(Designer-developer; pure design ~half.)

## Anti-patterns this skill prevents

❌ Smooth gradients (lose period feel)
❌ Inter/Roboto typography (AI defaults)
❌ AI-generated FA imagery (community anti-AI)
❌ Mixing variants (Bright + Dark = visual chaos)
❌ Skipping accessibility (glossy gradients hurt contrast easily)
❌ Generic "glassmorphism on green gradient" template feel
❌ Heavy backdrop-filter on mobile (perf disaster)

## Author note

Built from research synthesizing:
- 3 local Frutiger Aero reference sites (frutigeraeroarchive.org, frutiger-aero.it, frutiger-aero.neocities.org)
- 6 YouTube videos (Aesthety, Musta, Carson, kandiwuff, Polygon Donut, Pelle Sjöberg) — ~1M combined views
- 8 web design Claude skills (Refactoring UI, Bencium, Owl-Listener, claudekit, Dammyjay93, Leonxlnx, evolv3ai, Anthropic)
- 8 WebSearch queries covering history, revival, characteristics, subgenres, CSS tutorials, portfolio examples, 2026 trend
- Community ethos (Future We Were Promised, anti-AI position)

## License

Use freely. Attribution appreciated.

## Iterate

This is v1 — built as MVP. To expand:
- Add component references (forms, navigation patterns, etc.)
- Add more examples (full multi-page site, dashboard, portfolio)
- Add WebGL aurora shader template
- Add motion library integration patterns
- Add CMS integration guides
