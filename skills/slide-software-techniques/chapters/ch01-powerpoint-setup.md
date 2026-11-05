# Chapter 01: PowerPoint File Setup

## Core Idea
Most lost hours and most "PowerPoint-looking" decks come from a badly set-up file, not from the software. Before drawing a single slide, set the document size (1920×1080 px), then open the Slide Master (Schema diapositiva) and fix there, once, everything that repeats: margin guides, theme fonts, theme colors, footer and slide number, a small set of layouts with placeholders, and text styles stored in the bullet indent levels. The hierarchy is strict: the Master controls the layouts, the layout controls the slide. A file built this way is fast for you, impossible to break for the client, and lets you change the typography or palette of 100+ slides in one move. Finish by saving it as a .potx template and saving one chart template per chart type; link data charts to Excel when figures are updated periodically.

## Frameworks Introduced
**Master → Layout → Slide hierarchy**: what you set on the Master (the biggest, top thumbnail in Slide Master view) cascades to every layout under it; what you set on a layout cascades to the slides using it; manual slide edits override both and should be the exception. Guide colors in Slide Master view tell you where a guide lives (red = Master, yellow = layout, grey = slide).
When to use: every new deck or client template; always edit the highest level that applies.

**Template = layouts + theme**: a template is a set of layouts (cover, break/section slide, text only, text + image, image only, data, quote) placed inside a theme that defines colors and fonts. A theme alone is not a template.
When to use: when scoping a template job; a template with only "title + text" layouts makes users produce text-only slides.

**Five Master settings**: (1) guides, (2) theme fonts, (3) theme colors, (4) footer, (5) layouts for recurring slide types. These five give 80% of the speed and consistency gain.
When to use: as the opening checklist of any PowerPoint file, even a 10-slide one (custom layouts are only worth it for long decks; the other four always).

**Indent levels as paragraph styles**: PowerPoint has no paragraph styles (Word does), but each bullet indent level of the Master body placeholder (level 1–5, and beyond) can be formatted as a distinct text style (title, body, caption, label…). Users apply styles with Tab / Shift+Tab or Increase/Decrease List Level; you restyle the whole deck by editing the Master.
When to use: client templates and any deck where text must stay consistent across many slides.

**Locked template, free slides**: saving as .potx means double-clicking the file creates a new untitled .pptx; the template itself is never overwritten. Objects placed in the Master/layouts become background the user cannot select.
When to use: corporate delivery where many people add slides.

## Rules & Numbers
- Slide size: 1920×1080 px (Design > Slide Size > Custom Slide Size / File > Page Setup on Mac). PowerPoint converts it to 67.73 × 38.1 cm. It matches web screens and Keynote's default, and it is the canvas on which all point sizes in this skill are valid. Never 4:3 (looks dated).
- Delete the default placeholders on slide 1 and delete unused layouts in the Master before starting.
- Start from the plainest white theme (Office Theme), never a decorative built-in theme.
- Margin guides: 4 guides on the Master (2 vertical, 2 horizontal), not on individual layouts. Guides are invisible in slideshow but make every slide tidier.
- Guide values on 1920×1080 (PowerPoint shows a guide's position as its distance from the slide centre, in cm): vertical guides at 31 left and 31 right; horizontal guides at 16 top and 15 bottom (the bottom margin is taller because the footer lives there).
- Acceptable variants: 31 / 16.5; about 32.8 for a slightly wider frame. There is no single correct number; consistency across all slides is the rule.
- On the default PowerPoint size (33.87 × 19.05 cm) the equivalent margins were about 15.5 / 8.3, or 15.3 / 8.
- Titles always start at the top-left margin corner; the footer sits inside the bottom margin.
- Add a centre vertical and a centre horizontal guide on the Master; add column guides for a 4-column grid when the content needs it. Different guide colors may carry different meanings.
- Theme colors apply to everything: shape fills, text, charts (Change Colors), picture Recolor. Pick them from the "Theme Colors" row of every color menu, never from Recent Colors.
- Theme colors: define at most 3–4 real colors (white and black/near-black count in addition). The scheme has 12 slots: Text/Background Dark 1, Light 1, Dark 2, Light 2, Accent 1–6, Hyperlink, Followed Hyperlink. Fill all of them deliberately, including hyperlinks.
- Monochrome theme in one minute (generated with a shades tool such as Shadowlord): base hue = accent; 90% darker = text, covers, break slides, back cover; 90% lighter = background of most slides or text on dark. For charts/illustrations keep the 0, 20, 40, 60, 80, 90% steps and put them into Accent 1–6.
- Use near-black (very dark grey) instead of pure #000000 for text, and a very light grey/off-white instead of pure white background when the deck is projected.
- Dark background variant: lower Brightness in the HSB/HSL color dialog of the main color; make a dark layout (Background Styles on the layout) with its own title and footer colors.
- Theme fonts: set Heading and Body fonts in the Master (Slide Master > Fonts > Customize Fonts). Default Microsoft font is now Aptos (replaced Calibri); acceptable pairing out of the box: Aptos Semibold titles + Aptos Regular body. Prefer linear sans fonts that are not defaults (Inter, Roboto, Epilogue, Funnel Sans, IBM Plex Sans).
- Point sizes on 1920×1080 (they are only valid on this canvas; on PowerPoint's default size everything shrinks):
  - big titles 80–88 pt; display words up to 200–300 pt;
  - section/slide titles 40–48 pt; statement phrases 56–64 pt;
  - list text 32 pt with Exactly 42 pt line spacing (or 40 pt Light with Exactly 50); body text 24–32 pt in general, at least 32 pt when slides are read across a classroom or large room (see presentation-design ch04 type scale);
  - labels/eyebrows 24 pt with 16 pt space after;
  - footer and source 18–20 pt Regular (Light becomes invisible at that size).
- Sizes in multiples of 8 (24, 32, 40, 48, 56…) give a coherent scale; it is a guideline, not a law.
- Weight for emphasis: use Medium/Semibold of the family rather than the synthetic Bold button, which is too heavy.
- Footer on the Master: remove the date placeholder; footer text centre or left, slide number right, both inside the bottom margin; footer placeholders with internal margins 0, Resize shape to fit text, text anchored top. Footer grey/dark, number in accent color. A heavy footer (e.g. a full-width photo strip) ruins a template.
- Logo: on the Master only if it works on both light and dark backgrounds; otherwise place it per layout, or build two Masters (light and dark).
- Placeholders: Resize shape to fit text (Adatta dimensioni forma al testo), anchored top, internal margins 0 — so text never shrinks and the first line never moves.
- Text style example on Master level 1 ("title"): no bullet, Semibold, 20 pt (in a dense template), accent color, line spacing Multiple 1.15, space before 0, space after 12 pt. Level 2 ("body"): smaller, Light, grey instead of black, no space before. Spacing between text blocks must live in the styles (space before/after), never in empty returns.
- A placeholder cannot hold two text styles (bold title + regular body) unless you use two indent levels; otherwise use two placeholders.
- Tables or charts placed on the Master/layout become part of the background and are not editable by users: provide them as slides or a "ready elements" slide instead.
- Chart templates (.crtx) are saved on the computer (Chart Templates folder), not inside the .pptx/.potx: deliver them separately with installation instructions; with many users almost nobody installs them.
- On Mac you cannot save table styles, shape styles, or theme fonts (the latter only with a workaround): budget for that gap or deliver instructions.
- Chart templates are tied to one chart type: make one per type (line, column, pie…), prefix the names (e.g. "BRAND line", "BRAND column", "BRAND pie").
- Build the chart to be saved as complete as possible (3+ series, legend, data labels, axes): a one-series column template will not transfer colors to a three-series chart.
- Example chart style: axis text 18–20 pt in deck font, light/mid grey; chart title above at 40 pt (or no chart title if the slide title says it: never both); legend bottom, enlarged; monochrome palette (works especially well for pies).
- Every PowerPoint chart is backed by an Excel sheet; charts pasted from Excel as linked objects update when the workbook changes — the main reason PowerPoint stays the standard for periodic reports.
- Prepare in the template, already restyled to the brand, the SmartArt diagrams the client uses most (process, cycle), plus a "ready elements" slide (tables, charts, shapes, connectors).
- Add an instructions slide/page to every delivered template: which layout for what, how to apply text styles with Tab, text limits, where chart templates go.
- Excel link: enter percentages as decimals (0.82) to apply % formatting; otherwise 82 becomes 8200%. Axis in % with 0 decimals, maximum 1.0, major unit 0.1.

## Procedures
**A. New deck from scratch (PowerPoint)**
1. Delete placeholders; Design > Slide Size > Custom: 1920 × 1080 px.
2. View > tick Guides; View > Slide Master (Visualizza > Schema diapositiva); select the top Master thumbnail.
3. Delete unused layouts (right-click > Delete Layout).
4. Right-click empty slide area > Grid and Guides > Add Vertical Guide / Add Horizontal Guide; drag each to its value (watch the tooltip). Alt/Option + drag duplicates a guide; drag it off the slide to delete it.
5. Slide Master > Colors > Customize Colors: name the palette, set Dark 1/Light 1/Dark 2/Light 2, Accent 1–6, Hyperlink, Followed Hyperlink; Save. Sample colors first with Fill > More Colors > Eyedropper from a pasted screenshot, from a CSS inspector extension (e.g. CSS Peeper shows site fonts and colors) or from a URL color picker.
6. Slide Master > Fonts > Customize Fonts: Heading and Body font; or select title and body placeholders on the Master and set fonts from Home.
7. Footer: in Master Layout uncheck Date; position and format footer and number; Format Shape > Text Options > Text Box: margins 0, Resize shape to fit text.
8. Close Master View. Insert > Header & Footer: tick Slide number and Footer, type the text (e.g. presentation title), Apply to All. Changing the text here later changes every slide. If a layout does not update, untick and re-tick its footer in Master Layout.
9. Create layouts: Duplicate Layout, move placeholders, Insert Placeholder > Picture / Text / Chart. In Normal view, switching layout re-flows the existing content automatically.

**B. Text styles via indent levels**
1. Slide Master, top Master thumbnail, body placeholder.
2. Select levels 1 and 2: Bullets > None; on the ruler drag both indent markers (first-line triangle and hanging triangle+square) fully left.
3. For each level set font weight, size, color, Line Spacing Options (line spacing, space before/after).
4. Rename the sample text of each level ("style 1 title", "style 2 body"…) so users understand.
5. Back in Normal view: new line + Tab (or Increase List Level) switches to the next style. To restyle the deck (bigger title, dark blue, not bold), edit the Master level again; all slides update.
6. Optional box style for a placeholder: light fill, internal margins about 11, rounded corners — make one, then duplicate it, because the corner radius cannot be typed numerically (only the yellow handle).

**C. Automatic presentation title on every slide**: Master > format the footer placeholder (color, font, size) > Normal view > Insert > Header & Footer > Footer: type the title > Apply to All.

**D. Dynamic underline in a Master placeholder**: select the placeholder > Shape Format > Edit Shape > Change Shape > a "No Border" line callout; drag the callout line under the box and stretch it to exactly the box width. The line now follows the placeholder when it grows or shrinks (a grouped text box + line works on normal slides but not inside the Master).

**E. Save and share the template**: File > Save As > PowerPoint Template (.potx). Add a first slide or page of usage instructions (how to add slides, which layout for what, where text limits are).

**F. Chart template (.crtx)**
1. Set theme colors first, so Chart Design > Change Colors already offers the brand palette.
2. Build a full chart; Chart Design > Add Chart Element to choose axes, title, legend, data labels; format fonts and colors.
3. Right-click the chart (or Chart Design > Change Chart Type) > Save as Template; name it with a prefix.
4. Reuse: Insert > Chart > Templates > choose; or insert any chart and Change Chart Type > Templates.

**G. Excel-linked chart**
1. Build the chart in Excel (or right-click a PowerPoint chart > Edit Data in Excel; drag the blue range to exclude label columns).
2. Copy in Excel, paste in PowerPoint keeping the link (Paste Special/Keep source formatting & link data): edits in Excel update the slide.
3. Organise folders before linking: on Mac links cannot be re-pointed if files move (on Windows they can).
4. A constant series (e.g. average) can be turned into a line: select the series > Change Series Chart Type > Line.

**H. Google Slides template (same checklist)**: theme colors from brand identity; footer elements (logo, date, references); layouts with text and image placeholders for frequent slide types (the hardest part); extra ready elements (tables, charts, shapes, connectors); short usage guidelines.

## Common Mistakes
- Picking colors from More Colors / Recent Colors on each object → define Theme Colors; one change then recolors hundreds of objects, charts and image recolor filters.
- Guides drawn on each layout or slide → guides on the Master only.
- Leaving "Shrink text on overflow" on placeholders → set Resize shape to fit text (or Do not Autofit for fixed boxes).
- Spacing with empty returns → Space Before/After in the styles.
- Bullet levels used only to change the font → format every level as a named text style.
- Chart/table inserted in the Master so it repeats → users cannot edit it; provide it on a layout-based slide instead.
- Delivering a template with three layouts and a heavy photo footer → offer text+image, data, quote, section and cover layouts; keep the footer light.
- Delivering a .pptx as the "template" → users overwrite it; deliver .potx.
- Assuming chart templates travel inside the file → ship .crtx separately with instructions.
- Editing in the Master a layout's child placeholder instead of the parent → edit the top Master so all layouts inherit.

## Mental Models
- "The Slide Master is where the magic happens": it looks slower at the start and saves the project later.
- A template has two goals: easy for anyone who touches it, and stylistically harmonious by construction.
- Creating a solid template is the most time-consuming job in presentation work because every layout must be tested with real content.
- Everything that appears on more than one slide belongs one level up.
- In PowerPoint text boxes are shapes and shapes are text boxes: one object per element.

## Examples
- A company file received without any template: rebuilt with a white theme, Master guides, Aptos Semibold/Regular, a petrol-dark layout with light-blue title, centred footer with right slide number, a dummy circular logo, saved as .potx.
- A reference deck built from an encyclopedia text: four slides (intro line, 5-point list with numbers in light circles, "Did you know…" break slide, detail slide with rounded image and two info boxes) on a 1920×1080 file with guides at 31, a 3–4 color palette (near-black, blue, light blue, very light background), Roboto/Inter, list 32/42 pt, titles 88 pt, footer 20 pt.
- A corporate template where labels had a custom underline: solved with the line-callout trick so the underline lives in the Master and still stretches.
- A reporting client: chart templates for line, column and pie charts in a monochrome brand palette plus Excel-linked charts for quarterly updates.
