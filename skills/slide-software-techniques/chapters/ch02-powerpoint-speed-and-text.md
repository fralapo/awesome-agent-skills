# Chapter 02: PowerPoint Speed & Text Handling

## Core Idea
People are slow in PowerPoint because they misuse five basic functions — text box options, Change Shape, horizontal/vertical text alignment, Align & Distribute, and Group — and because they fight hidden tools instead of designing. The worst errors are technical, not visual: slides built with extra rectangles behind text, titles centred then dragged left, and autofit that shrinks text at random are slow to update and break when the client edits them. Work clean: one object per element, text typed inside its shape, alignment set by the tool rather than by eye, spacing set numerically (exact line spacing, space after), and repeated actions done with shortcuts (repeat last action, Format Painter, Shift-constrained moves). Then use the few power tools that replace external software: Selection Pane, Merge Shapes, picture corrections and recolor, Change Picture, tables cleaned of fills and borders.

## Frameworks Introduced
**The five base functions**: (1) Text box options (autofit + internal margins), (2) Edit Shape > Change Shape, (3) text alignment horizontal and vertical (anchor), (4) Align & Distribute, (5) Group / Ungroup. Mastering them before hunting "new" features is what makes slides fast and original.
When to use: onboarding a team; diagnosing why a deck takes too long.

**Three autofit modes** (Format Shape > Text Options > Text Box):
- Shrink text on overflow (Adatta testo all'area di riversamento): text shrinks as the box fills — the cause of "text that gets smaller by itself"; never leave it on.
- Do not Autofit (Non adattare): the box keeps its size whatever you type — right for fixed-size cards, pills, tabs, menu boxes.
- Resize shape to fit text (Adatta dimensioni forma al testo): the box follows the content plus its internal margins — right for normal text boxes and template placeholders.
When to use: set it consciously on every text container. Rule of thumb that reconciles the cases: free-flowing text → Resize shape to fit text; designed box with fixed geometry → Do not Autofit; never Shrink.

**Anchor where the text grows from**: a title at the top is anchored top so adding lines does not move the first line; anchoring middle/bottom forces constant re-positioning.
When to use: every placeholder and text box.

**Clean-construction rule**: the colored background of a text is the fill of the text box itself (change its silhouette with Change Shape), not a separate rectangle behind it; left-aligned text is aligned left, not centred and dragged.
When to use: any file another person will edit.

**Contextual tools ranking**: Align & Distribute is the single highest-value command; Selection Pane is the second (kept open while working); Merge Shapes replaces an illustration tool for simple shapes and masks.
When to use: whenever a slide "looks done in a hurry".

## Rules & Numbers
- Horizontal alignment: left or centred only. Right only for small info on the right side of a footer. Justified never (PowerPoint does not hyphenate). Centre only short phrases (a few words); long text always left.
- Line spacing: default single (1.0) is too tight for body text. Use Exactly (e.g. 32 pt text → 42 pt; 36 → 42 in Keynote; 40 Light → 50) or Multiple 1.1–1.15 for paragraphs; big display titles 0.8–0.95. Remove Space Before when using Multiple.
- Paragraph spacing: space after a title/label 8 pt (dense) up to 16–32 pt (airy slides); never an empty return.
- Internal margins: text boxes used as plain text → 0 on all sides (so text aligns to guides exactly). Cards: about 0.7 cm left and bottom, 0 top. Pills/tabs: 0 internal margins with Do not Autofit, or e.g. 1.2 on the side the text hugs, 0 elsewhere. Too large a margin pushes text out of the shape.
- Remove the default outline PowerPoint adds to every new shape (Shape Outline > No Outline).
- Rounded corners: only via the yellow adjustment handle (left = sharp, right = round), no numeric radius. Keep radius small ("too rounded looks childish"); make one master shape and duplicate it so radii stay identical.
- Card shadow: Outer, offset downward, transparency 85–90%, larger blur. On light backgrounds use a much more transparent shadow.
- Letter spacing: never exaggerated on multi-line text; increased spacing only on 2–3 words (labels, eyebrows, a centred title).
- Line breaks: never leave short words (articles, "is", "a") at a line end.
- Emphasis: one device at a time (bold OR italic OR color), never bold + italic together.
- PNG recolor: black logo → white with picture Brightness +100%; white logo → black with Brightness −100% (monochrome PNG only).
- SVG icons: when the perfect icon exists only in black, download the SVG, recolor it in a free SVG colorizer (it lists all colors of the file), export PNG at original size, insert. Use one icon set with one stroke weight and color for the whole deck; credit sources when the site requires it.
- Recolor and duotone with theme colors keep photos coherent; brighten or darken a background photo (e.g. Brightness −40% to −65%) rather than adding an opaque box.
- Glass card on a busy photo: see Chapter 03, Procedure J; text on images must always be legible.
- Images: same aspect ratio for all images of a series (Crop > Aspect Ratio, e.g. 2:3 or 3:2), not random sizes.
- Duotone: Picture Format > Color > Recolor with theme colors keeps photos inside the palette.
- Tables: remove all fills first, then re-apply only horizontal borders in mid grey; no vertical lines (except a 2 pt white divider between column groups); header row in accent color with white text, second header row a lighter HSB tint; header rows lower than data rows; numbers right-aligned; currency label not bold; custom cell margins left/right 0 (there are no vertical lines to clear), top/bottom minimal (about 1 in the field), header column 0.5, then a right margin of 0.3–0.5 on data rows only so values never touch the highlight boxes. Merge cells for group headers (Q1/Q2) instead of repeating them. Semantic emphasis: best value bold green, worst red, optionally a small rectangle behind the number at 85% transparency; add highlight rectangles last (they must be moved by hand). Optional white rounded card behind the table, very soft shadow at 85% transparency.
- SmartArt: acceptable when it saves time, but first decide what the content is (process, cycle, relationship) and pick that visualization, not the prettiest; after typing, restyle colors, fonts and shapes so it no longer looks like default SmartArt. (Earlier advice was to avoid SmartArt altogether; the current position is "use with judgment".) It recolors with the theme, its text is edited in the text pane, and points are reordered with one click.
- Arrow shapes from the default library look cheap; draw your own or use icons.
- Alignment levels: margins set at the start; smart guides visible while placing; Align at the end to fix residual offsets. Elements may break margins or bleed off the slide only with intent.
- Objects that shift a few pixels between consecutive slides signal carelessness: check in Slide Sorter.

## Procedures
**A. Speed shortcuts**
1. Repeat last action: after formatting one object, select another (same or other slide) and press Ctrl+Y (Windows) / Cmd+Y (Mac).
2. Shift + drag: moves an object constrained horizontally or vertically; Ctrl + Shift + drag: duplicates while constrained.
3. Shift while drawing a line: perfectly straight; Shift while resizing: keeps proportions.
4. Right-click a picture > Change Picture (From File / Stock): replaces the image keeping size, crop shape and position.
5. Format Painter: double-click the brush to apply the same formatting to many objects; Esc to stop. Animation Painter works the same for animations.
6. Right-click a slide thumbnail > Hide Slide instead of deleting slides you may need later.
7. View > Slide Sorter at the end of every job to catch inconsistencies across slides.

**B. Selection Pane (Riquadro di selezione)**: Home > Arrange > Selection Pane (or Shape Format > Selection Pane). Keep it open. Select overlapping objects without moving them; drag to change stacking order; lock objects so you can place content on top; hide with the eye icon; double-click names to rename (essential for morph files and for clients editing later).

**C. Align & Distribute**: select objects > Home > Arrange > Align > Align Center/Middle/Left… then Distribute Horizontally/Vertically (uses the first and last object as extremes). With a single object or group selected, Align aligns to the slide (Align Center + Align Middle = slide centre). Group each unit first (icon + label, card + text) so units distribute as wholes. Typical use: a row of logos placed at random.

**D. Group, Change Shape, text inside shapes**
1. Double-click a shape and type: the text lives inside it.
2. Right-click > Group / Ungroup.
3. Shape Format > Edit Shape > Change Shape: swap a rounded rectangle for any other preset (and back) keeping text and formatting.
4. To split a width into equal boxes: duplicate boxes, group, stretch the group to the target width, ungroup.

**E. Fix shrinking text**: select the box > right-click > Format Shape > Text Options > Text Box (third icon, Size & Properties) > choose Resize shape to fit text or Do not Autofit. Set the vertical anchor (Top) in the same panel, and the internal margins.

**F. Line and paragraph spacing**: Home > Line Spacing > Line Spacing Options > Spacing: Before / After (pt) and Line Spacing: Exactly / Multiple.

**G. Custom bullets**: Bullets > Bullets and Numbering > color, size (% of text), Customize symbol; or paste a Unicode symbol copied from a symbols site as the bullet character.

**H. Horizontal cards instead of a vertical bullet list**: light grey background (Design > Format Background); white rounded rectangles with icon + text typed inside; Do not Autofit; margins 0.7 cm left/bottom, 0 top; soft downward shadow (85–90% transparency); group each card; Align Middle + Distribute Horizontally.

**I. Merge Shapes (Unisci forme)**: select two or more shapes > Shape Format > Merge Shapes > Union, Combine, Fragment, Intersect, Subtract. Examples: crescent moon = circle minus circle (Subtract); window frame = full-slide rectangle combined with a smaller rectangle (Combine); a "notch" for a logo in an image mask (Union of rectangles).

**J. Text mask on video or photo**
1. Insert a video (or image) filling the slide.
2. Type one word in a thick, large font.
3. Cover the slide with a rectangle; order so the word is above the rectangle.
4. Select the rectangle and the text > Merge Shapes > Subtract: the word becomes a hole showing the video.
Cut-out cover variant: full-slide white rectangle; subtract a smaller rectangle to open a band at the bottom; subtract the title too; put a stock video (e.g. from Pexels) behind.

**K. Image masks and corrections**: Crop > Crop to Shape (e.g. hexagon, rounded rectangle); Crop > Aspect Ratio; shapes drawn with the pen/freeform as masks via Shape Fill > Picture. Picture Format > Corrections (Sharpen/Soften, Brightness/Contrast) or Format Picture pane > Picture Corrections for sliders; Color > Recolor for duotone.

**L. Overlay for unreadable text on a photo**: full-slide rectangle > Gradient fill: black at 0% transparency where text sits, black at 100% transparency where there is none (or brand dark color).

**M. Charts and tables**
1. Table: right-click > Insert Row Above; select cells > Merge Cells; Table Design > Shading > No Fill on all; Borders: none, then Bottom Border + Inside Horizontal Border; Fill > More Colors > HSB to tint the accent; Table Layout > Cell Margins > Custom Margins.
2. Highlight one data point: click once to select the series, click again for one bar; set other bars to 80% transparency; Data Labels > Outside End only on the key value (e.g. 32 pt bold), labels with no fill; Gap Width to adjust bar thickness.
3. Percent alternative to a pie (bubble chart): Insert > Chart > X Y (Scatter) > Bubble (not 3D). Single %: two rows X=1, Y=0, sizes 100 and 33; X axis 0–2, major unit 1; Y axis min 0 (cuts the bubbles into half circles), max 1; Bubble size scale up to 300 (200–250 when several bubbles side by side); remove axes, gridlines, title; Data Labels showing Bubble Size (untick Y value, untick leader lines). Several %: X = 1…5, X max 6, Y min −1 to see full bubbles. 100% reference bubble as dashed outline with no fill. If bubbles disappear (known bug), recreate the chart. Format small, enlarge to full slide at the end.
4. Custom donut with varying ring thickness: insert a real pie with the data as a hidden reference, overlay Arc shapes of different thickness/colors snapped to the slices, add labels, hide (don't delete) the pie via the Selection Pane so it can be updated.

## Common Mistakes
- Text box on top of a colored rectangle → one shape with fill and text inside.
- Title centred and dragged left → left alignment plus guides.
- Shrink text on overflow everywhere → Resize shape to fit text or Do not Autofit.
- Moving or deleting objects to reach the one underneath → Selection Pane.
- Aligning by eye → Align/Distribute, after grouping units.
- Rebuilding a card because the shape must change → Change Shape.
- Re-inserting and re-cropping a photo to swap it → Change Picture.
- Formatting 30 objects one by one → Ctrl/Cmd+Y or double-click Format Painter.
- Exporting a logo to an image editor just to make it white → Brightness +100%.
- Using SmartArt to decorate a bullet list → choose the diagram from the content's logic and restyle it.
- Default table with fills, vertical lines and repeated headers → strip, re-add horizontal rules, merge group headers.
- Justified paragraphs → left aligned.

## Mental Models
- If you take long to make slides, the cause is almost always a misused base function, not missing talent.
- A slide is well built when it is easy to update, not only when it looks good.
- Highlighting by subtraction: dim the rest (transparency, grey) rather than adding elements.
- The tool should disappear: when you know where things are, attention goes to "how do I design this slide" instead of "where is the command".
- Precision and PowerPoint do not get along natively (no numeric radius, no paragraph styles): compensate with master shapes, duplication and Master styles.

## Examples
- A slide of five vertical bullets turned into four horizontal white cards with icons on a light grey background, built with text inside shapes, Do not Autofit, 0.7 cm margins and Distribute Horizontally.
- A partners slide with randomly placed logos: logos recolored to white with Brightness +100% for a dark background, grouped per row, aligned and distributed.
- A quarterly revenue table: two-level header with merged Q1/Q2 cells, accent header row, no vertical lines, right-aligned numbers, best month green bold, worst red.
- A tax-gap bar chart per country: duplicate info removed, one country highlighted in full color with an outside-end label, others at 80% transparency, average as a labelled line, source at 18 pt grey on the bottom margin.
- An "ice cream flavours" slide: five bubbles at X=1…5 sized by percentage, each colored after its flavour, with a dashed 100% reference.
- A cover with the title cut out of a white plate showing a slow stock video behind.
