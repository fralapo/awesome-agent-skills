# Chapter 03: Layout & Visual Design Principles

## Core Idea
A slide works when the audience's eye lands where the speaker wants it, at the moment the speaker says it, and the message is understood at a glance before anything is read. That is achieved with a small set of structural principles applied with discipline, not with software tricks: fixed margins and guides set before anything is drawn; a column grid; few, repeated alignments; proximity (things that belong together sit together, groups are separated by more space than their internal gaps); a clear reading hierarchy built from size, weight, color and position; generous white space ("if you fill everything, nothing is important"); and one deliberate point of contrast per moment, often created by dimming everything else rather than adding something new. Consistency across the deck matters as much as quality inside a slide: one stylistic choice (shadow, corner radius, alignment, accent color) is applied everywhere or nowhere. Before adding an element, try removing one. Every content type has its "preferred shape" — a list, a number, a timeline, a comparison each wants a different layout — and a slide carries one message.

## Frameworks Introduced
**Contrast – Emphasis – Breath**: the three-word check for any slide. Contrast = text clearly detached from the background (two very different values, no busy image behind text). Emphasis = a reading order: what is read first, second, third, made with size and color. Breath = white space around elements; filling the slide achieves nothing.
When to use: as the last pass on every slide before delivery.

**Three levels of alignment**: (1) margins set at the start (the empty frame between content and slide edge); (2) smart/magnetic guides while placing objects; (3) Align & Distribute at the end to fix whatever is still a few pixels off.
When to use: every new file; level 3 as a cleanup pass on every slide.

**Master → Layout → Slide hierarchy**: guides, fonts, colors and footer set in the slide master propagate to all layouts, layouts govern slides. Put margins in the master, not in single layouts or slides.
When to use: whenever a deck will exceed a handful of slides or be reused.

**Proximity**: closeness is read as grouping. Space inside a group (icon↔its text, image↔its caption, line↔line of one paragraph) must be smaller than space between groups.
When to use: any slide with more than one element — services, team, products, lists, captions.

**Guiding the eye (difference attracts)**: decide from the spoken script what to highlight, then format it differently from the rest. Levers: size, movement, position/displacement, transparency, color; plus shadow for cards and exposure/blur for images.
When to use: lists, card grids, charts, tables, screenshots — any slide where the speaker talks about one part at a time.

**Focus by subtraction (dim the rest)**: to highlight X, lower the opacity/saturation of everything that is not X instead of adding arrows, boxes or callouts. "Subtracting" also means making something less visible.
When to use: comparison charts, multi-point lists, dashboards, maps, screenshots.

**Four functions of visual elements**: evocative images (large, half slide or more, reinforce a concept), anchoring icons (simple symbols guiding the eye through list items), descriptive images (show the real thing: product, views, gallery), explanatory images (screenshots/diagrams with zooms, circles or callouts on the relevant part). An element that fits none of the four is removed.
When to use: auditing every icon and picture in a deck.

**Technical vs emotional slides**: technical slides (charts, tables, data) build authority and the audience looks at the slide; emotional slides act as scenery and amplify the voice. Too many technical ones bore, too many emotional ones cost credibility; alternate them to set rhythm.
When to use: when sequencing a deck and deciding layouts.

**Visual pattern and pattern break**: a repeated scheme (same background color per slide type, same title position) lets the audience predict and concentrate on content; breaking it on purpose captures attention.
When to use: setting background rules per slide type; marking a key number or takeaway.

## Rules & Numbers
Canvas and margins
- Canvas 16:9, 1920×1080 px (same as web and Keynote default). 4:3 reads as dated; converting is a chance to rework content.
- Set margins first. Everything lives inside the margin rectangle; nothing touches the slide edge. Exceptions only with intent: the footer (sits inside or just below the bottom margin) and images that bleed off the slide.
- Four guides minimum (2 vertical, 2 horizontal) in the master; bottom guide farther from the edge than the others because the footer lives below it. Add a vertical and a horizontal center guide; optionally a 4-column grid.
- Reference values: PowerPoint guide read-outs used in practice are 31 (sides) / 16 (top) / 15 (bottom) on a 1920×1080 page, or 15.5 (sides) / 8.3 (top) on the default 33.87 cm page. Both correspond to side margins ≈4% of width (≈80 px on 1920) and top ≈6–8% of height (≈65–90 px); bottom ≈110–120 px when a footer is present. There is no mandatory number; consistency is mandatory.
- Use differently colored guides for different meanings (master vs layout vs slide).
- Title always in the same position on every content slide; an element that moves a few pixels between slides signals carelessness. Duplicate an existing slide rather than starting from blank.

Grid and columns
- 2 columns for little content; 3–4 columns for a series of points. Equal-width columns: draw a rectangle, duplicate it, use it as a guide.
- Exploit the horizontal format: put list items side by side (cards/columns) instead of stacking them.
- A text column must never span the full slide width: use ~1/2 to 2/3 of the width (title left, content right is a standard split); 40–50 characters per line on projected slides, 50–80 only in documents and emailed decks (see ch04).
- Image + text: image on the left or right, vertical/half slide; never a thin strip at top or bottom. Build the layout around the subject of the photo (subject right → text left) or choose the photo to fit the layout.

Alignment
- Left-align anything longer than 2–3 lines; center only short phrases. Right-align only footer info and page numbers at bottom right. Never justify in slide software (no hyphenation → rivers of white).
- If body text is left-aligned, the title is left-aligned too. If the cover is centered, keep the same logic deck-wide; mixing left/center/right on one slide creates chaos.
- Top-left is read first (left→right, top→bottom): put the title or main element there; secondary info (name, deck title, page) at the bottom, small and peripheral. Main elements left, things to look at later (images) right.
- Don't fill all four corners with info: it creates static symmetry; leave one corner free and keep compositions slightly asymmetric for dynamism.
- Anchor top titles to the top of their box so added lines grow downward without moving the first line.

Hierarchy and size (1920×1080, pt ≈ px)
- Define few text styles (title, subtitle/intro, body) and one font family using its weights; a display/script font only for a single word.
- Reference sizes (the canonical scale, see ch04 type scale): cover / statement / menu headlines 80–160 pt (cover display text up to 200–300 pt); message title on a content slide 64–88 pt; title on list/data/chart slides 40–48 pt; labels/eyebrows above titles 20–28 pt; body 24–32 pt; data descriptions and secondary text 24 pt; key numbers ≥56 pt (hero numbers 120–200 pt with a 24–32 pt caption); sources, footnotes and footer 18–20 pt. Quotes sit at the low end of the statement range, about 80 pt (96–128 is too much for a quote).
- Minimum body size for a slide read across a classroom or large room: 32 pt. Apparent size depends on the font's x-height: equal pt ≠ equal visual size.
- Three-level hierarchy for denser slides: title → intro sentence → detail paragraph (smaller, grey). Classic title+text slide: key message 3 lines at ~80 pt with 2–3 words in the accent color, detail at ~28 pt grey in the same text box, 48 pt space between paragraphs, image covering the right side.
- Large titles: line spacing 0.8–0.95, slightly tightened letter spacing. Body: 1.1–1.2 "multiple" (≈130–140% of font size, since single ≈120%); never 1.5.
- Emphasis must be decisive: Bold vs Regular (Medium vs Bold doesn't read as different). Never bold + italic together; no underline; no ALL CAPS for emphasis. One highlight treatment for large text and one for small text, deck-wide. Don't highlight half a sentence.
- The smaller the text, the subtler the emphasis: small paragraph → bold only; a 2-line/10-word phrase → bold + color or a contrasting font.
- "If everything is big, nothing is important": shrink secondary text rather than inflating everything; size contrast + white space create hierarchy.
- The deck title must never compete with the slide title; repeated nav info stays small.

Spacing and proximity
- Space between items > line spacing inside an item; space between title and body > space between body lines.
- Space comes from "space before/after" and box margins, never from empty returns.
- Caption sits close to its image; icon close to its text; label directly above its value.

Focus and dimming
- Active list item 100% opacity, inactive ~30%. Inactive chart bars ~20% opacity (80% transparency). Progress line 50% opacity with the active segment at 100%.
- Outline-only = background information; solid fill = foreground information.
- Cards: activate one by color (others grey = "off"), elevation (shadow), position or size; combine shadow on the active card with reduced opacity on the others.
- Quick dimming hack: a semi-transparent rectangle in the background color laid over the group to mute.
- Image focus: duplicate the image; bottom copy darker (lower exposure) and blurred; top copy cropped with a circle/rectangle mask on the detail, optionally an outline and a small label.
- Don't over-focus: the rest must remain readable as context.

Consistency
- Any style choice (shadow, corner radius, outline titles, accent color, icon style) is applied to the whole deck or to none. Broken visual coherence breaks attention.
- Corners: rounded but moderate (heavy rounding looks childish). Shadows: light, never default; 10–20% opacity on white, blur proportional to distance and object size.
- One accent color; avoid "rainbow". Off-white background instead of #FFFFFF, very dark grey/brand-dark text instead of pure black.
- Every color in the palette reappears somewhere so the deck feels unified.
- Pasted material (diagrams from the web, Excel tables, other decks' screenshots) is rebuilt in the deck's style; pasted text uses "keep text only"/"use destination formatting" to avoid intruder fonts.

Subtraction and one message
- One concept per slide. A single bullet is not a list: drop the symbol and set the phrase large.
- Before adding, remove: duplicate words (title and subtitle saying the same thing), redundant labels, ornamental shapes, filler icons, filler images ("images are not gap-fillers").
- Prefer one large image over several small ones; half slide, full bleed, or with an even white border.
- Do not repeat speaker name, deck title or audience on every slide; logo full-size only on cover/back cover, small symbol elsewhere.

Proportions
- All images in one set share the same aspect ratio (crop to a fixed ratio, e.g. 2:3) and corner radius; logos placed in identical boxes or a thin-line grid so different proportions look orderly.
- Keep list items similar in length (same number of words/lines); three items is the easiest group to follow and remember.
- Optional harmonic scale: text sizes in multiples of 8 where possible (24, 32, 40, 48, 56, 64, 80…); paragraph space 32 pt. The scale is a guide, not a law.

## Procedures
**Set up a new file (any software)**
1. Set slide size 1920×1080 px; delete placeholders you will not use.
2. Open the master; add 4 margin guides (bottom one higher to host the footer) plus center guides; optionally 4 columns.
3. Set theme fonts and theme colors in the master; build footer/page number inside the bottom band.
4. Duplicate layouts for recurring slide types instead of drawing from scratch.
5. Place objects using smart guides; finish each slide with Group → Align → Distribute.
6. Review the whole deck in grid/sorter/light-table view to catch jumping titles, inconsistent backgrounds and stray styles.

**Hierarchy pass on one slide**
1. Write the spoken message in one sentence; decide the single element that carries it.
2. Assign levels: 1 (message/number), 2 (support), 3 (detail/source). Max three.
3. Make level 1 visibly larger/heavier/colored; shrink level 3 rather than enlarging level 1 indefinitely.
4. Check proximity: group pairs tight, gaps between groups wide.
5. Squint/step back: the eye must land on level 1 first.

**Progressive focus for lists/cards/charts**
1. First slide: overview with all items visible.
2. Duplicate per item: active item at 100%, others ~30% (or grey/outline); optional shift up/right via morph.
3. Transition: Fade (or Morph/Magic Move for movement), quick.
4. Prefer several slides to many animations on one slide.

**Rebuild a pasted diagram**
1. Place it as a reference; trace with basic shapes, lines and text boxes in deck fonts/colors.
2. Remove what the talk doesn't need; delete the reference.

## Common Mistakes
- No margins, content touching edges → set guides first; keep everything inside the rectangle.
- Titles "jumping" between slides → margins in the master, duplicate slides, consistent anchoring.
- Full-width text columns → narrow to 1/2–2/3; use freed space for a visual.
- Justified text → left-align (long) or center (2–3 lines); fix the rag with manual breaks; no orphan short words at line ends.
- Everything the same size, or everything huge → size contrast and white space.
- Text on left, all images on right linked by letters (A↔A) → place each text next to its image.
- Filler icons/images in leftover gaps → each visual tied to a concept or removed; one large image instead.
- Adding arrows/boxes to highlight a data point → dim the other data instead.
- Info on all four corners, speaker name top-left → title top-left, secondary info small at the bottom, one corner free.
- Mixed alignments (left/center/right) on one slide or across slides → one alignment logic.
- Shadows/rounded corners on some slides only → deck-wide or nothing.
- Footer larger than content, giant logo on every slide → small symbol, no filled band.
- Concept-map slides with all boxes and arrows at once → one box per slide, the arrows become spoken transitions.
- Multiple emphasis treatments in one sentence (bold + gradient + italic) → one.

## Mental Models
- The slide amplifies the voice; if it says everything, the speaker is redundant. A slide full of text is a document to email, not to project.
- Eyes scan before reading: give an entry point, then let people go deeper.
- Different attracts: the eye goes to what breaks the pattern — so control what breaks it.
- White space is an element, not empty: it creates focus, order and grouping.
- Every content has a preferred shape, like a dress that fits; a list, a number, a timeline and a comparison each deserve their own layout.
- Care is transferred to the speaker: precision in alignment reads as professionalism even to non-designers.
- Removing is designing: subtract or mute before adding.
- Look for layouts where slides are not: web sections, app screens, dashboards, posters are horizontal compositions already solved by designers.
- Effort scales with stakes: internal updates need care and standard layouts, not fireworks.

## Examples
- Chaotic slide → uniform slide: margins set, smart guides used, final Align/Distribute pass; same content, orderly result.
- Image-and-caption slide with all captions on the left and pictures on the right keyed by letters: regrouped so each picture sits beside its caption, small gap inside pairs, larger gap between pairs.
- European comparison bar chart meant to highlight one country: instead of adding a callout box, other countries' bars set to 80% transparency, only the target bar solid with a 32 pt bold data label.
- Five-point "values" list: big "01/05" counter in a left column (300 pt / 48 pt: a display-size counter, treated as display text rather than as a 120–200 pt hero number), points on the right; active point 100% opacity, others 30%, points shift up one step per slide.
- Dashboard-style slide: dark cards all "off", the card being discussed lights up (color/shadow), mimicking a website hover.
- Cluttered slide with four images and text: everything removed, restarted from a statement title at 120–160 pt across the slide plus one image masked in a circle.
- Partners slide with logos of mixed proportions and colors: identical cells in a thin-line grid, logos converted to all-white or all-black (with brands' approval).
- Product screenshot slide: blurred, darkened full screenshot behind; the relevant panel duplicated sharp in a rounded mask with a thin outline and label.
- Navigation indicator for long decks: small line/circle/number tag at top-left or bottom-left; the current section stays visible, the rest fades.
- Handout version of a talk deck: same design, fixed versatile grid, fewer and clearer groups, denser text meant to be read alone.
