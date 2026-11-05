---
name: slide-software-techniques
description: "Click-level how-to for building slides in PowerPoint, Keynote, Google Slides, Canva and Figma Slides: 1920×1080 file setup, Slide Master and layouts, guides and margins, theme fonts/colors, indent levels as text styles, footers, .potx templates, chart templates (.crtx) and Excel-linked charts; speed (shortcuts, Selection Pane, align/distribute, Change Shape, Merge Shapes masks, recoloring PNG/SVG icons, autofit and 'shrinking text', exact line spacing, tables, SmartArt); Morph / Magic Move / Smart Animate recipes (zoom, slider, horizontal scroll, gallery, cards, glass, loops, text masks, animated timelines, 3D); export and compatibility (Keynote↔PowerPoint, Canva/Google links, PDF backup) and presenting (presenter view, remotes, webinars). Use whenever the user asks how to do something in a presentation app, which menu or setting to use, why PowerPoint is misbehaving, or how to build an effect or template, even if they just say 'ppt' or 'slides'."
allowed-tools:
  - Read
  - Grep
argument-hint: [software, technique, or chapter number]
---

# Slide Software Techniques
**Chapters**: 5 | **Corpus**: ~100 theoretical transcripts on presentation software and animation | **Generated**: 2026-11-05

Companion to `presentation-design` (the *what and why*: process, layout, type, color, data, animation principles). This skill is the *how* in the software. Every size in pt assumes a **1920×1080 px** canvas.

## How to Use This Skill

- Identify the software (and version or OS: Windows/Mac PowerPoint menus differ slightly), then open the chapter from the index.
- Give UI names in English with the Italian in parentheses when the user works in Italian (e.g. *Slide Master (Schema diapositiva)*, *Morph (Morphing)*, *Magic Move (Spostamento magico)*).
- Before suggesting an effect, check the destination: will the deck be presented in the same software and version (ch05)?

---

## Core Techniques

**File setup (ch01)**: Design → Slide Size → Custom **1920×1080 px** (67.73×38.1 cm). Put everything that repeats in the **Slide Master**. Place 4 margin guides on the Master only (≈31 cm left/right and 16 top / 15 bottom from the centre). Set **theme colors** (3–4 real colors, all 12 slots filled, never Recent or More Colors) and **theme fonts**. Body placeholder indent levels act as paragraph styles: apply them with Tab and restyle the whole deck from the Master. Footer: no date, inner margins 0, Header & Footer → Apply to All. Save as **.potx** with an instructions slide. Chart templates (.crtx) are saved on the computer, not in the file, so make one per chart type. Paste Excel charts with the link kept.

**Text handling (ch02)**: three autofit modes. Never use *Shrink text on overflow* (it causes the "randomly shrinking text"). Use *Resize shape to fit text* for free text and *Do not Autofit* for fixed cards, pills and tabs. Anchor titles at the top. Set line spacing to *Exactly* or *Multiple* 1.1–1.15 (big titles 0.8–0.95), and use space after (8–32 pt) instead of empty returns. Type inside the shape instead of laying a box on top, and use **Change Shape** to swap the shape.

**Speed (ch02)**: Ctrl/Cmd+Y repeats the last action. Shift-drag constrains a move, Ctrl+Shift-drag duplicates. Keep the **Selection Pane** open to rename, lock and hide objects. Group each unit, then Align and Distribute. Double-click Format Painter to apply it repeatedly. Use Change Picture. PNG icons: Brightness +100% turns black to white, −100% turns white to black. **Merge Shapes → Subtract** makes text masks and cut-outs. Card shadow: downward, 85–90% transparency.

**Morph / Magic Move (ch03)**: Morph goes on the **second** slide in PowerPoint; Magic Move goes on the **first** slide in Keynote. Build the final composition first, duplicate it, then change the earlier state. Durations: about **1 s** instead of the 2 s default (0.5–0.7 s for small moves, 2 s only for big or 3D travel). Objects must exist on both slides: use **100% transparency** or park them **off-slide** instead of deleting. Morph doesn't see inside groups, so when grouping changes, add an auto-advancing pass-through slide. Animations last 0.3–0.5 s, with delays of 0.1 s (fast fill) or 0.2 s (a sequence that must be noticed). Use *On Click* only for what you're saying right now. Always turn on Smooth Start/End. Focus: active item 100%, others 30%. Loops: motion path + Auto-Reverse + Repeat until end of slide, 5–10 s.

**Other tools (ch04)**: Morph ≈ Magic Move ≈ Canva *Match & Move (Dinamiche combinate)* ≈ Figma *Smart Animate*. Google Slides has none, so duplicate the slide for each state and use a 0.3 s Fade. Google Slides: custom line spacing 1.1–1.2, brand colors in Theme colors, and to link a grouped object put a transparent shape on top. Keynote: *Play in Window* keeps presenter view during calls. Canva: respect a template's line counts and transpose its three colors. Interactive PDF: a clickable index, a home icon and prev/next arrows, with every link tested.

**Export & presenting (ch05)**: design in the destination software. Deliver Canva or Google decks as a **link**, not a .pptx. Keynote → PowerPoint loses Magic Move, transparencies, fonts and arrows. Always keep a **PDF backup**, and check it for builds that stacked images. Present full screen with presenter view and a remote. Online, share only the audience window and keep to one-click appearances. Rehearse alone, then with people, then in the venue.

---

## Chapter Index

| # | Title | Key topics |
|---|---|---|
| [ch01](chapters/ch01-powerpoint-setup.md) | PowerPoint File Setup | slide size, Slide Master, layouts, placeholders, guides, theme colors/fonts, indent-level styles, footer, .potx, chart templates, Excel links |
| [ch02](chapters/ch02-powerpoint-speed-and-text.md) | PowerPoint Speed & Text Handling | shortcuts, Selection Pane, align/distribute, Change Shape, autofit, line spacing, icons recolor, Merge Shapes, tables, SmartArt |
| [ch03](chapters/ch03-powerpoint-animation-recipes.md) | PowerPoint Morph & Animation Recipes | morph rules, durations, transparency vs delete, groups, zoom, slider, scroll, gallery, cards, glass, loops, text mask, timeline, 3D |
| [ch04](chapters/ch04-keynote-google-slides-canva-figma.md) | Keynote, Google Slides, Canva, Figma Slides & Other Tools | Magic Move, Google Slides workarounds, Canva templates/effects, Figma Slides, interactive PDF, AI tools |
| [ch05](chapters/ch05-export-compatibility-presenting.md) | Export, Compatibility & Presenting | cross-software compatibility, fonts, PDF backup, presenter view, remotes, webinars |

## Topic Index

- **3D models** → ch03
- **Animations pane, timings, delays** → ch03
- **Autofit / shrinking text** → ch02
- **Canva** → ch04, ch05
- **Chart templates (.crtx), Excel links** → ch01
- **Figma Slides** → ch04
- **Footer, page numbers** → ch01
- **Glass effect** → ch03
- **Google Slides** → ch04
- **Guides & margins** → ch01
- **Icons (recolor PNG/SVG)** → ch02
- **Interactive slides / PDF** → ch04
- **Keynote / Magic Move** → ch03, ch04, ch05
- **Line spacing, space after** → ch02
- **Loop animation** → ch03
- **Masks (text, image), Merge Shapes** → ch02, ch03
- **Morph recipes (zoom, slider, scroll, gallery, cards)** → ch03
- **Presenter view, remote, webinar setup** → ch05
- **Selection Pane, shortcuts** → ch02
- **Slide Master, layouts, placeholders** → ch01
- **SmartArt** → ch02
- **Tables** → ch02
- **Templates (.potx)** → ch01
- **Theme colors / fonts** → ch01

## Related Skills

- `presentation-design`: design principles, structure, type scale, color, data and animation guidelines.
- `anthropic-skills:pptx`: generating .pptx files programmatically.
- `designcraft-expert`, `vectorcraft-expert`: layout and vector work in ArtCraft apps.

## Scope & Limits

Techniques documented for recent PowerPoint (Microsoft 365), Keynote, Google Slides, Canva and Figma Slides. Menus move between versions: if a command isn't where described, search the app's command box (*Tell me / Search*) for the English or Italian name rather than inventing a path.
