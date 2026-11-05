# Chapter 04: Keynote, Google Slides, Canva, Figma Slides & Other Tools

## Core Idea
The software does not design the slides — the head does — but each tool changes what is cheap, what is possible and what survives delivery. Keynote is the most intuitive designer's tool (contextual inspector, numeric precision, the smoothest Magic Move and builds) but lives on Apple devices. Google Slides is free, online and collaborative but has almost no customization, no eyedropper, few non-customizable animations: plan graphic quality first and simulate motion with duplicated slides and fast fades. Canva is the friendliest for non-designers, with a huge free asset library and Match & Move (its morph), but its templates break as soon as you change them and its strength is the share link, not export. Figma Slides suits design teams (auto layout, named theme colors, text styles) but offers only Smart Animate. PowerPoint remains the corporate standard (Excel integration, rigid templates, strongest animation set, Copilot). AI generators produce drafts, not client decks. Choose the tool from the presenting context and the client's ecosystem, then use each tool's specific tricks.

## Frameworks Introduced
**Tool by context**: large companies and consulting → PowerPoint (common language; showing up with Canva in consulting may be frowned upon) or Google Workspace; Mac-only environments → Keynote; very small companies, schools, non-experts → Canva or Google Slides (a deck that takes 1 h in Canva can take 3 h in PowerPoint for a beginner); design teams already in Figma → Figma Slides; interactive non-linear decks → Genially or linked PDFs.
When to use: first conversation with a client: which software, which machine, which delivery format.

**Same principle, different name**: PowerPoint Morph = Keynote Magic Move (Spostamento magico) = Canva Match & Move (Dinamiche combinate) = Figma Slides Smart Animate. Google Slides has no equivalent.
When to use: translating a recipe from Chapter 03 to another tool.

**Simulate, don't fake-spectacularize (Google Slides)**: duplicate the slide per state, change colors/positions, apply a fast Fade (~0.3 s) to all slides. Functional effects beat spectacular ones.
When to use: whenever the client imposes Google Slides.

**Template fidelity (Canva)**: a template works because colors, spaces and elements are calibrated for one visual balance; use it almost as designed, or start from a blank slide.
When to use: before accepting "we'll just fill a Canva template".

**AI as a support, not a designer**: chat models to find a visual metaphor for a concept; image models for style moodboards; slide generators only to unblock a blank page.
When to use: ideation phase; never for final structure of a client deck.

## Rules & Numbers
- Keynote: guides show distance in points and %; titles always in the top-left corner on 4 margin guides + centre guides for a 4-column grid; objects snap automatically.
- Keynote line spacing: Exactly is preferred (36 pt text → 42 pt). Title-to-paragraph space larger than line spacing within the paragraph (use Space After).
- Keynote bullets: indent, bullet-to-text spacing, any symbol/emoji, color, size 50–70% of text, vertical offset (e.g. −2 pt), text indent (e.g. 64).
- Keynote Magic Move recognizes only the same objects; grouped vs ungrouped → it fades. Transition on the first slide; ~0.5–0.8 s; automatic advance = remove On Click, set Automatic with 0 s delay. Builds: Fade and Move (Dissolvi e sposta) 0.3–0.5 s with very short distance (about 3–10), Line Draw (Tracciamento linea) 0.5 s (0.3 risks too fast), Fade and Scale, Blur. Keynote cannot animate a color change of an object: use Magic Move between two slides.
- Keynote has no color-filter function: grayscale image (saturation 0) + colored shape on top at reduced opacity. PowerPoint and Google Slides use Recolor.
- Keynote is smoother than PowerPoint for text builds (by word/character with chosen start and end) and computes delays more intelligently.
- Google Slides: never use preset line spacing (1.15/1.5/double); use Custom spacing 1.1–1.2 and paragraph space before 8–24 pt. Big titles 0.8–0.95.
- Google Slides colors: put brand colors into the 10 Theme colors (hex without #), not into Custom colors; no eyedropper — sample with an online image color picker from a screenshot.
- Google Slides has no transparency field on shapes: create a custom color and drag its transparency (alpha) slider. Focus cover rectangle at ~70% opacity.
- Google Slides cannot link a grouped object: overlay a fully transparent shape as the click area and link that.
- Google Slides animations: use only fades; avoid cube-type transitions.
- Canva: free elements have no crown; crown = Pro. Search elements in both your language and English; don't take the first result (everyone does). Use the "same set" suggestions for coherent variants (two different tape pieces from one set rather than a duplicate).
- Canva effects: outline (Hollow) only on very large text; Neon with an interesting color and reduced intensity; apply one effect consistently to all titles, never to one at random. Letter spacing slider: exaggerate only on 2–3 words.
- Canva template rules: pick by category/goal (a portfolio template has no data layouts); don't lengthen paragraphs, shrink titles, move elements at random, replace the hero image with a random one, or overturn the palette. Transpose the template's 3 colors (white → very light beige, black → dark brown/green, accent → green of similar lightness; or invert light/dark). Change fonts consistently everywhere. More text: first shrink size and narrow the box, then move the image, then remove it — but first ask whether it is a document or a spoken presentation.
- Canva: background video with almost imperceptible movement; animated stickers and illustrations only "with judgment"; handwritten caption fonts must be the most legible ones.
- Canva alignment: File > View settings > Show margins; Canva aligns the text box, not the text, to the margin. Reused sizes on Canva's default canvas: labels ~20 pt, body 26 pt.
- Figma Slides setup: start from a mandatory theme (Light/Dark); layouts per slide type; grid view and slide groups; nearly all Google Fonts incl. variable fonts; line spacing in %.
- Figma Slides precision: named theme colors update every element using them; mandatory text styles (more repeated styles = more coherent slides); shapes already have internal text padding (in PowerPoint you must set it by hand); numeric corner radius; few shapes (a good thing).
- Figma Slides layout: auto layout keeps a fixed gap between title and subtitle even when text wraps; items in a row reorder by dragging.
- Figma Slides motion and presenting: Smart Animate only as a transition (no grouping needed); built-in polls; AI text rewrite (longer/shorter, casual/professional); presenter view with two windows (notes + slides) but no timer at launch; no reusable components at launch. Design Mode features require a Figma Design plan.
- Keynote without a Mac: the iCloud web version works with an Apple account (similar, not identical to the app).
- PowerPoint's five reasons to stay: corporate standard (Microsoft 365), Excel integration with updating data and deeply customizable charts, the most rigid and complete templates (.potx), powerful animation (triggers, motion paths, loops, Morph), Copilot. Its cost is complexity: overkill for school projects.
- Genially: for interactive presentations with buttons and embedded navigable websites.
- AI: chat prompt "How would you visually make a slide expressing the concept of [sentence]?"; image models: add 16:9 and words like "PowerPoint"/"slide deck"; check copyright before reusing generated images. PowerPoint Designer often overturns your layout — ignore it. Copilot can draft slides or rewrite text inside PowerPoint.
- Inspiration sources over other slides: Awwwards (sites of the day, Collections: transitions, cursors, slideshows), Dribbble (Popular view; search "presentation design"), Behance, Pinterest (search by content, e.g. "data viz", "timeline"); palettes via Coolors, Picular (keyword → colors), shade generators (Shadowlord); fonts via Google Fonts and Fontshare; a daily-inspiration browser extension (Designer Daily Report).

## Procedures
**A. Keynote essentials**
1. View > Show Rulers (Cmd+R); drag guides from rulers.
2. Theme palette: sample with the eyedropper, copy hex (Color Sliders > RGB > Hex), generate tints on a shades site, then in Format > Style > Fill drag the "current fill" swatch onto the theme swatch to replace it.
3. Image panel: Exposure, Saturation, Enhance, advanced Adjustments (highlights, shadows, contrast), Reset Image.
4. Masks: double-click an image → black handles resize the mask, click again → white handles move the image inside; zoom slider. Or draw a shape on top, select both > Format > Image > Mask with Selection (points stay editable).
5. Shapes: Arrange > Unite / Intersect / Subtract / Exclude; right-click > Save to My Shapes. Shape > right-click > Make Editable to move points (a drop from a circle). Pen: click = corner, click-drag = curve; Alt/Option removes a handle; trace silhouettes from photos or maps.
6. Text outline: select text > gear (advanced options) > Outline.
7. Stacking for masks: View > Show Object List.
8. Play > Play in Window: share only that window on Meet/Zoom and keep presenter view (current, next, notes) — "two monitors in one".
9. View > Customize Toolbar (icon and text).

**B. Keynote Magic Move recipe (bands transition)**: divide slide width into 6 rectangles; paste them into the next slide off-slide at the top, staggered; create 6 more of another color and park them off-slide on the previous slide; place text and images on top; apply Magic Move to all. Same pattern: index of slanted bars (rectangle > Make Editable > shift the two top points right) entering stepwise; product circle carousel (phones on a reference circle, group, rotate per slide, color selector moves).

**C. Google Slides essentials**
1. View > Show ruler; View > Guides > Show guides; drag from rulers; Alt-drag to duplicate; drag out to delete; build margins + 4 columns.
2. Theme colors: pencil next to theme colors > Choose theme color > replace hex codes.
3. Format options > Recolor (theme colors) and Adjustments (brightness, contrast); heavier edits in an external editor (e.g. Pixlr online).
4. Masks: right-click > Crop image, or the arrow next to Crop > Shapes (e.g. rounded rectangle; the yellow diamond adjusts the radius). A rectangle rounded on one side = rounded rectangle + overlapping normal rectangle, grouped.
5. Bullets: right-click the bullet > More bullets (draw, search by keyword or category, emoji); then color/bold the bullet like text.
6. Format > Line & paragraph spacing > Custom spacing.
7. Fonts: font menu > More fonts (all Google Fonts). Inspect element on a website to find its font.
8. Outline-only title: Insert > Word Art, remove fill, keep a colored border.
9. Extensions/Add-ons: recolorable icons, PNG photos/illustrations, polls, diagrams; credit the source.
10. Sync slides: copy a slide from the main deck, paste into another deck, choose Link to original presentation (a link icon appears); after editing the original, click Update in the copy. Ideal for a big master deck feeding smaller derived decks (agency credentials).
11. Interactive PDF links: Insert > Link on a transparent overlay shape → slide in this presentation or URL.

**D. Google Slides effect recipes (fade only, ~0.3 s on all slides)**
1. List with focus: title left, 3 points right (icon, title, subtitle); highlight the active point in the icon's color; cover the others with a background-colored rectangle at ~70% opacity, no border.
2. Process timeline: points lit one by one with three states — to do (grey), active (filled, attention), done (empty circle); variant with a line as progress bar and a central card with colored border, grey cards at the sides.
3. Image stack: front image + two placeholder boxes; each slide sends the image back and brings a new one; simpler variant: same-size cards rising from below inside the margins.

**E. Canva essentials**
1. Left panel: Templates, Elements (lines, shapes, graphics, tables, photos, videos, audio, charts, stickers, frames, collections), Uploads, Text, Styles; thumbnails at the bottom.
2. Text effects: select text > Effects > Curve (intensity), Neon, Hollow.
3. Colors from photos: text color picker > "Photo colors" (colors of images already in the design).
4. Position: Align top/middle/bottom, Distribute vertically/horizontally; Layer > Send backward; Alt-drag to duplicate; right-click > Group.
5. Masks: Elements > Frames (shapes, laptop, phone, irregular); drop the photo in, double-click to reposition.
6. Edit image: brightness/contrast/saturation, filters, effect apps (pixel, grain…), Duotone with palette colors, Mockups > See all (e.g. minimal phone).
7. Draw app (Apps > Draw): neon brush, highlighter; repeatable across pages.
8. Page menu (three dots) > Hide page.
9. Palette: duplicate an accent rectangle, drag the picker toward bottom-right for darker and top-left for lighter variants.
10. Match & Move: build slide 1 and slide 2 with moved objects; click between them > Add transition > Match & Move; duration ~1 s; limit to one or two moving objects.
11. Present > Presenter view: one window with notes for you, one audience window to share via Share window.
12. Share > Anyone with the link > Can view; save the link somewhere (document, USB stick) so you don't depend on login on the day.

**F. Interactive (non-linear) PDF**: add a legend slide explaining that the PDF is clickable and how to navigate; clickable index; a home/hamburger icon at the top of every slide back to the index; previous/next arrows at the bottom; text links or real buttons that anticipate the destination (never "click here"); external buttons next to the resource (e.g. above a video preview). Design buttons like on a website. Test all links yourself and have someone else test them; Drive/Dropbox links must be public or shared with the recipient. Use links only where needed.

**G. AI drafting**: slide generators (Tome, Gamma, Beautiful.ai) give 10 slides in seconds but mostly re-arranged bullets and document-like structures; useful only with no idea where to start and no ambitions. Refine one slide at a time if at all. Image models replace part of the moodboard search on Dribbble/Behance/Pinterest (better for illustrations and abstract concepts than for slide layouts).

## Common Mistakes
- Expecting PowerPoint animations in Google Slides → design graphics first, simulate states with duplicated slides + fades.
- Brand colors in Google "Custom" colors → Theme colors.
- Linking a group in Google Slides → transparent overlay shape.
- "Breaking" a Canva template with longer text and new images → respect its line counts or start blank.
- Filling a Canva deck with free stickers → elements only to support text, separate content or guide the eye; white space is not an error.
- One Canva text effect on one title → same effect on all titles or none.
- Designing on a phone → use a computer (or iPad for sketching).
- Letting an AI generator define the structure → structure and storyboard by hand, AI for metaphors and moodboards.

## Mental Models
- "The limit is not the software but the head": find the solution mentally, then build it with the tool you have.
- Keynote lets you concentrate on graphics because you find any function in seconds; PowerPoint hides tools and makes you think about where things are.
- Shared resources (Canva libraries, stock) mean shared looks: dig deeper than the first page of results.
- Every tool has its native delivery: a Canva link, a Google Slides URL, a Keynote file on a Mac, a .pptx/.potx in a company.

## Examples
- A deck designed in Keynote and converted for Google Slides had to be largely rebuilt and lose its animations.
- An event that imposed Google Slides: an image-stack effect built only with duplicated slides and 0.3 s fades.
- A mixology community deck built in Canva without brand guidelines: icons and backgrounds from the logo's overlapping translucent shapes, editorial line layout from the blog.
- A school internship report in Canva: content first in a document, a style test slide, reusable component groups, monochrome blues, gradient only on cover and dividers, shared as view-only link.
- A Canva slide with two rounded cards that swap places while rotating with Match & Move on a black background (title 56 pt, card text 72 pt).
- A history topic drafted by a slide generator: usable as an outline only; titles in "persuasive" tone came out too long.
