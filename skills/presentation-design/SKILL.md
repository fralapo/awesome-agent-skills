---
name: presentation-design
description: "Complete guidelines for designing effective, beautiful presentations: message-first process (audience, goal, script, storyboard, slide count), deck structure and slide types (cover, index, break, focus, content, back cover with CTA), layout (margins, grids, alignment, proximity, hierarchy, focus by dimming), a type scale for 1920×1080 slides, message titles, bullets and their alternatives, color palettes and roles, images, icons, backgrounds, shadows and text-on-photo, charts, tables, big numbers and timelines, animation and morph principles with timings, contexts (school, thesis, corporate, pitch deck, product launch, portfolio, training, talks, webinars), a before→after redesign method, templates, brand and AI. Use this skill whenever you create, generate, review, redesign or critique a presentation, slide deck, pitch deck, PowerPoint, Keynote, Google Slides or Canva deck (including generating .pptx with code or DeckCraft), or advise on slides, even if the user only says 'make me a ppt'."
allowed-tools:
  - Read
  - Grep
argument-hint: [task, topic, or chapter number]
---

# Presentation Design
**Chapters**: 11 | **Corpus**: ~300 theoretical transcripts on presentation design, distilled | **Generated**: 2026-11-05

The *what and why* of good slides. For click-level how-to in PowerPoint, Keynote, Google Slides, Canva or Figma Slides, use the companion skill `slide-software-techniques`.

## How to Use This Skill

- **Generating or building a deck** → follow the *Deck Generation Workflow* below, then open ch02, ch03, ch04 and ch05 as needed.
- **Reviewing or redesigning slides** → use the *Review Checklist* and ch10 (redesign playbook).
- **A specific question** → find the chapter in the Topic Index and read it before answering.
- Quick lookups: [cheatsheet.md](cheatsheet.md) (all numbers in tables), [patterns.md](patterns.md) (ready-made slide recipes), [glossary.md](glossary.md).
- **Minimum reading per task** (saves context): new deck → cheatsheet + ch02 + the ch09 section for its context; pitch deck → cheatsheet + ch09 (pitch) + ch07, plus `public-speaking-persuasion` ch12 for the *content* sequence of an investor pitch (problem, who, product, competition, business model, resources, capture value); slide review → Review Checklist + ch10; data-heavy deck → ch07; animated deck → ch08.

---

## The Ten Principles

1. **Message before software.** Audience, goal (inform / educate / convince / inspire, plus the action you want), key message and script come first; the slides come last.
2. **Slides support the voice, a document must stand alone.** One idea per slide: a sentence or a few words plus a visual. Everything else goes in the speaker notes. If the deck will be emailed, make a denser second version.
3. **The title is the message.** A small label carries the topic ("Problem") and a large sentence states the takeaway.
4. **Split instead of squeezing.** More slides doesn't mean a longer talk: one event, number or point per slide.
5. **Hierarchy through contrast and space.** If everything is big, nothing is important. Use at most three levels, and create focus by **dimming the rest**: active item 100%, others ~30%.
6. **Margins and alignment are not optional.** Set guides before designing, keep the title in the same place, use one alignment logic per slide, and never justify text.
7. **Consistency over decoration.** One font family, one icon set, one image treatment, one animation style. Any style choice applies to the whole deck or to none. Remove before adding.
8. **Every visual has a function** (evocative, anchor, descriptive, explanatory) or it goes. Images go big; icons are never filler.
9. **Rebuild, don't paste.** Tables, charts and diagrams are redrawn in the deck's style and simplified to the cited datum.
10. **Animate with purpose.** Fade is the default; use Morph / Magic Move for continuity. Durations are short, and content appears on click when you name it.

## Canonical Numbers (1920×1080 px canvas, sizes in pt)

| Element | Value |
|---|---|
| Cover / statement / menu headline | 80–160 (cover display up to 200–300) |
| Message title on content slide | 64–88 |
| Title on list / data / chart slide | 40–48 |
| Body text | 24–32; **≥32** when read across a classroom or large room |
| Data descriptions, secondary text | 24 |
| Key numbers / hero numbers | ≥56 / 120–200 |
| Labels above titles | 20–28 |
| Sources, footnotes, footer | 18–20 |
| Line spacing | titles 0.8–0.95; body 1.1–1.2 multiple (never 1.5) |
| Line length | 40–50 characters on projected slides; 50–80 in documents |
| Bullets | 3 ideal, 5 max, equal length, one level of indent at most, revealed one at a time |
| Fonts | 1 family (2 max, the second only large on 1–2 words); avoid Calibri, Arial, script fonts |
| Colors | 2–3 + neutrals (≤4 theme colors), one accent; off-white and near-black, never pure #FFF/#000 |
| Shadows | 10–20% opacity on light backgrounds, blur proportional to distance; never the default |
| Animation | objects 0.2–0.5 s (0.3 preferred); transitions 0.5–1 s (max 1.5); morph ≈1 s (0.5–0.7 for small moves); delays 0.1–0.2 s |
| Slide count | an outcome of the script; rule of thumb ≈15 per 10 min (a 10-min pitch ≈13) |
| Contrast | check every text/background pair at real size; a light accent (lime, yellow) needs a darker variant for text on off-white. Numeric WCAG targets (4.5:1 body, 3:1 large): `ux-ui-expert` ch21 |

Prefer multiples of 8. The scale is a guide; consistency inside the deck matters more than the exact value.

## Deck Generation Workflow (when you build slides)

1. **Brief**: who is in the audience, how many, what's the room or medium, what's the goal and the desired action, and which software and version will present the file (ch01). If unknown, state your assumptions.
2. **Message & script**: write the key message in one sentence, then a script or outline. Mark where a slide is needed (ch01).
3. **Structure**: apply the slide-type system — cover, (index), break slides for sections, content, focus slides for key moments, back cover with a call to action — and the background rhythm (ch02).
4. **Storyboard**: one line per slide with its message title and the visual that carries it (image, big number, chart, icon cards, timeline). Choose by function (ch06, ch07).
5. **System setup**: 1920×1080 canvas, guides and margins, theme fonts, theme colors (palette roles from ch05), a footer (ch03, ch11). With a brand, sample its colors, fonts and logo rules first.
6. **Build**: one message per slide, the type scale above, left-aligned text, the dim-the-rest focus, data rebuilt minimal (ch03, ch04, ch07).
7. **Motion** (if the medium allows it): fade by default, morph for continuity, on click for what you name (ch08).
8. **QA pass**: run the Review Checklist below, view the deck in grid or slide sorter, check contrast and readability at the real size, and keep a PDF backup (ch01, ch10).

If the deck will also be emailed (pitch decks often are), plan the denser "document" version too (ch01). When the company or data are hypothetical, mark every invented figure or name as a [placeholder].

When generating files programmatically (python-pptx, DeckCraft, etc.), encode the canonical numbers as constants, build masters/layouts first, and render previews to check overflow, alignment and contrast before delivering.

## Review Checklist (audit any slide or deck)

- **Organization**: is there one message per slide? Do the titles state takeaways? Is the deck structured into sections, with a CTA at the end?
- **Text**: are amount, sizes, line length, alignment, emphasis and bullets within the canonical numbers?
- **Color**: does each color have a role and is there one accent? Is the contrast adequate? Is there no pure black or white?
- **Style**: are margins and positions consistent, and are style choices (shadows, corners, icons, image filters) applied to the whole deck?
- **Resources**: are images large and high-resolution, with no watermarks? Do icons come from one set? Are charts and tables rebuilt and simplified?
- For each issue report *problem → why it matters → fix*, and keep–kill–change the elements (ch10).

---

## Chapter Index

| # | Title | Key frameworks |
|---|---|---|
| [ch01](chapters/ch01-process-before-the-software.md) | The Process: Message Before Software | 3 foundation questions, 5-step process, script vs outline, slide count, slides vs document, when not to use slides, delivery & rehearsal |
| [ch02](chapters/ch02-deck-structure-and-slide-types.md) | Deck Structure & Slide Types | 6 slide types, background rhythm, cover, index, break slides, footer, back cover CTA |
| [ch03](chapters/ch03-layout-and-design-principles.md) | Layout & Visual Design Principles | margins & guides, grid, alignment, proximity, hierarchy, dim-the-rest focus, consistency, subtract before adding |
| [ch04](chapters/ch04-text-and-typography.md) | Text & Typography on Slides | message titles, type scale, fonts, line spacing/length, emphasis, bullets & alternatives, autofit |
| [ch05](chapters/ch05-color.md) | Color | palette sizes, HSL thinking, monochrome tints/shades, color roles, background rhythm, red, contrast, tools |
| [ch06](chapters/ch06-images-icons-backgrounds-effects.md) | Images, Icons, Backgrounds & Effects | 4 image functions, big images, filters, text on photos, icons, logos, shadows, backgrounds, glass, screenshots |
| [ch07](chapters/ch07-data-charts-tables-timelines.md) | Data: Charts, Tables, Numbers & Timelines | one chart per slide, highlight the cited datum, pie alternatives, big numbers, minimal tables, timelines, offer & law slides |
| [ch08](chapters/ch08-animation-and-transitions.md) | Animation & Transitions (Principles) | 3 functions, timings, on click vs with previous, one point at a time, morph patterns, loops, corporate constraints |
| [ch09](chapters/ch09-contexts.md) | Presentations by Context | school, thesis, internship report, scientific, corporate, pitch deck slides, product launch, portfolio, training, talks, webinars |
| [ch10](chapters/ch10-redesign-playbook.md) | The Redesign Playbook (Before → After) | 5-area audit, keep/kill/change, split vs squeeze, rebuild pasted content, redesign cases |
| [ch11](chapters/ch11-templates-brand-ai-resources.md) | Templates, Brand, AI and Resources | when to use templates, recoloring by roles, corporate template build, brand rules, AI tools, asset sites |

## Topic Index

- **Agenda / index slide** → ch02, ch10
- **AI for slides** → ch11
- **Alignment, margins, guides, grid** → ch03
- **Animation, transitions, morph** → ch08 (how-to: `slide-software-techniques`)
- **Back cover / closing / "thank you"** → ch02
- **Backgrounds** → ch05, ch06
- **Big numbers, percentages** → ch07
- **Brand guidelines, logos** → ch06, ch11
- **Bullet points and alternatives** → ch04, ch10
- **Charts (pie alternatives, highlighting)** → ch07
- **Color palette, contrast** → ch05
- **Competitor / problem / team / offer slides (pitch)** → ch09, ch07
- **Corporate decks, meetings** → ch09
- **Cover slide** → ch02
- **Delivery: presenter view, remote, PDF backup, rehearsal** → ch01
- **Document vs slides (emailed decks)** → ch01, ch04
- **Fonts, sizes, line spacing** → ch04
- **Hierarchy, focus, whitespace** → ch03
- **Icons** → ch06
- **Images, photos, text on photo** → ch06
- **Inspiration (websites, moodboard)** → ch01, ch11
- **Number of slides** → ch01
- **Pitch deck (investors, startup)** → ch09 (slide design), ch07 (numbers, tables), `public-speaking-persuasion` ch12 (content sequence)
- **Market size, traction, business model numbers** → ch07 (big numbers, charts, highlighting)
- **Portfolio decks** → ch09
- **Redesigning existing slides** → ch10
- **School, thesis, internship (PCTO)** → ch09
- **Shadows, glass, 3D, effects** → ch06
- **Storyboard, script** → ch01
- **Tables** → ch07
- **Talks, TEDx, webinars, training** → ch09
- **Templates (using / building)** → ch11
- **Timelines, Gantt** → ch07

## Related Skills

- `slide-software-techniques`: menus, settings and recipes in PowerPoint, Keynote, Google Slides, Canva, Figma Slides.
- `public-speaking-persuasion`: delivery, voice, storytelling, persuasion.
- `ux-ui-expert`: general visual fundamentals (typography laws, 60-30-10 color, hierarchy) and UX psychology.
- `creative-director`: concepts, copy and visual metaphors.
- `anthropic-skills:pptx`, `designcraft-expert`: producing the actual files.

## Scope & Limits

Design guidance for live-presented and emailed slide decks. Numbers are calibrated on a 1920×1080 canvas: scale proportionally for other sizes. Company or brand rules override these defaults. Say so explicitly when you deviate.
