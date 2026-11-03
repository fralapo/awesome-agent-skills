---
name: designcraft-expert
description: "Operational InDesign know-how mapped to DesignCraft (the ArtCraft InDesign-class page-layout app driven over MCP through the mcp__designcraft__* tools) and, for interactive PDF, forms and review, to PdfCraft (mcp__pdfcraft__*). Use whenever you work in DesignCraft, or when asked for page layout of any kind: brochures, flyers, leaflets, tri-folds, catalogues, magazines, newsletters, menus, reports, ebooks/EPUB, posters, multi-page documents with parent (master) pages and page numbers/folios, threaded text and overset, paragraph/character/object/table/cell styles, nested and GREP styles, swatches and spot colours, text wrap, preflight, print-ready PDF (PDF/X-4, PDF/X-1a, bleed, crop marks, CMYK, separations, ink limit, package), interactive PDF (hyperlinks, bookmarks, buttons, form fields), IDML export, or PNG/JPEG pages for social media. Keywords - DesignCraft, ArtCraft, InDesign, desktop publishing, DTP, layout, parent page, master page, baseline grid, find change, GREP, preflight, PDF/X, bleed, PdfCraft."
version: 1.0.0
source: "Workflow informed by Adobe InDesign Classroom in a Book 2026 Release (Adobe Press); verified against DesignCraft's live command catalogue on 2026-11-03."
---

# DesignCraft expert

InDesign page-layout method rewritten for DesignCraft, the ArtCraft InDesign-class app, driven over MCP
from Claude Code or any SKILL.md-compatible agent (PdfCraft optional, for interactive PDF post-processing).
Every command id below existed in `list_commands` on 2026-11-03 (545 commands).

**Verification legend:** ✔ = the call was run on a scratch document on 2026-11-03 and behaved as described;
no mark = the command id and params were read from `list_commands` but not exercised. If a call fails, re-read `list_commands {filter:"…"}`:
the `params` field is the contract. Wrong attribute names in `type.char` / `type.para` return the full
list of valid names in the error message - a cheap way to discover them.

## 0. Ground rules for the agent

- **The ArtCraft apps are updated almost daily; every "not available" in this skill is a dated snapshot (2026-11-03).** Before telling the user a feature is missing, or before using a
  workaround, re-check the live app with `list_commands {filter:"<keyword>"}` (and the error-listing trick
  for attributes). If the command now exists, use it and treat §3b as out of date. The Adobe knowledge in
  this skill and in `references/` is the target behaviour even where DesignCraft lacks it today.
- Pick the right app: layout / multi-page / print PDF → DesignCraft; post-processing of an existing PDF
  (forms with logic, comments, accessibility fixes, signatures) → PdfCraft.
- **DesignCraft only writes under a sandbox root** ✔: the server's allowed root (e.g. `~/Craft` in a default
  install; check the server instructions or the error message). `export_png`, `file.exportPdf`,
  `save_document`, etc. refuse other paths, and the target folder must already exist (`mkdir -p` first).
  Keep placed images inside that root too.
- Never open or overwrite the user's originals in place: open, then save a working copy under a new name.
- Coordinates are **points in spread space**, y down ✔. On a facing-pages spread the left page spans
  x 0…W and the right page W…2W (A4: 595.28; Letter: 612). Page 1 of a facing document is alone on spread 0.
  Read `inspect_document` → `spreads[].pages[].bounds` and `columnRects` instead of guessing.
- Loop: `list_commands {filter}` → `batch` (stops at first error, earlier steps stay; `$N.id`, `$last.story`
  pass results forward) → `inspect_document` (overset, ids, styles) → `render_page` to look.
- Outputs that `get_story` / `story.get` return contain the whole text: avoid them on long stories.
- Version deliverables (`job_v01_print.pdf`) and keep the `.designcraft` working file next to the exports.

## 1. Key concepts (what InDesign thinks, what DesignCraft does)

- **Frames are containers**: text frame, graphic frame or unassigned (`frame.create {content}`); the image
  inside is content, positioned with `object.fit`. Effects apply to the whole frame, not to single words.
- **Parent pages** (ex "master pages") carry folios, headers, guides and placeholder frames for every page
  that uses them. Change once, update everywhere. Parents can be based on other parents.
- **Margins and columns** define the live area; **bleed** (usually 3 mm ≈ 8.5 pt, or 9 pt / 0.125 in) is
  where edge-to-edge objects must extend; **slug** is outside the bleed for job info.
- **Baseline grid**: a document-wide grid (leading increment) that body text can lock to, so that lines
  align across columns (`document.preferences {baselineGrid}`, `type.para {gridAlign}`).
- **Stories and threads**: one story can run through many threaded frames; text that does not fit is
  **overset** (red plus in InDesign; `stories[].overset` here). Never deliver with overset.
- **Styles**: paragraph (whole paragraph + its characters), character (runs inside), object (fill, stroke,
  effects, text-frame options), table and cell styles. Base styles on each other; avoid local overrides.
- **Swatches**: named colours (process CMYK, spot, tints, gradients). Edit the swatch → every use updates.
- **Transparency**: opacity, blend modes and soft effects; they interact with what is underneath and get
  flattened in PDF/X-1a.
- **Preflight**: continuous check for overset, missing/low-res images, fonts. Run it early and often.

## 2. Recommended workflow

1. Brief: format, pages, print vs screen, bleed, colour mode, deliverables (PDF/X, interactive, PNG).
2. `new_document` with preset/size, facing pages, margins, columns, bleed, slug, intent ✔.
3. Swatches (`swatch.create`) and styles (`style.paragraph.create`, `style.character.create`,
   `style.object.create`, `style.cell.create`, `style.table.create`) **before** content ✔.
4. Parent pages: folio with page-number marker, header, guides (`layout.parents.*`, `frame.create
   {spread:{kind:"parent",index}}`) ✔.
5. Content: text frames + `set_story_text`, thread/autoflow, images with `place_image`/`file.place`, wrap.
6. Apply styles (select range → `style.paragraph.apply`, or `find.change {paraStyle|charStyle}`) ✔.
7. Check: `inspect_document` (overset), `preflight.run`, `render_page` every page, `ink.separations`.
8. Export: `file.exportPdf` (x4/x1a with bleed+marks for print; tagged/interactive for screen),
   `export_png` for social, `file.package` for the printer; save `.designcraft` working copy.

## 3. Mapping table: InDesign → DesignCraft

| InDesign | DesignCraft (tool / command id) |
|---|---|
| File > New Document, presets | `new_document` / `file.new`; `file.presets`, `file.savePreset` |
| Document Setup / page size | `layout.documentSetup`, per-page `layout.pageSize` |
| Margins and Columns | `layout.marginsAndColumns {pages|parent}` |
| Create Guides / ruler guides | `layout.createGuides {rows,columns,fitTo}`, `guide.add` |
| Parent pages: new / apply / edit / override | `layout.parents.new`, `layout.pages.applyParent`, `frame.create {spread:{kind:"parent"}}`, `layout.overrideParentItems`, `layout.detachAll` |
| Insert/delete/move/duplicate pages | `layout.pages.insert {parent}`, `.delete`, `.move`, `.duplicateSpread` |
| Current Page Number marker | `find.change {find:"<placeholder>", change:"~N", grep:true}` ✔ (no direct insert command as of 2026-11-03 - re-check) |
| Numbering & Section Options | `layout.section {page,startNumber,style,prefix}` |
| Text variables (running header, last page) | `variables.define`, `variables.insert` |
| Type tool frame / placeholder text | `frame.create {content:"text",text}`, `type.fillWithPlaceholder` ✔ |
| Place Word/RTF/text with autoflow | `file.place {path, rect, autoflow, styleMap}` (+ `place.styles`) |
| Thread frames / autoflow / Smart Reflow | `text.thread {from,to|rect,autoflow}` ✔, `prefs.set {smartTextReflow}`, `object.primaryTextFrame` |
| Text Frame Options (columns, inset, auto-size, column rules, balance) | `object.textFrameOptions` ✔ |
| Character / Paragraph panel | `type.char {attrs}`, `type.para {attrs}` ✔ |
| Span/split columns, keep options, drop cap | `type.para {spanColumns:{kind:"span",columns:0}, keepWithNext, dropCapLines}` ✔ |
| Tabs and leaders | `type.tabs.add {position,align,leader}` |
| Bullets / numbering | `list.bullets`, `list.numbers`, `list.define` |
| Paragraph shading / borders / rules | `type.para {shadingOn, borderOn, ruleAbove, ruleBelow}` |
| OpenType, ligatures, fractions | `type.openType {feature}`, `type.char {ligatures}`; `math.insert` |
| Paragraph / character styles | `style.paragraph.create|edit|apply|redefine`, `style.character.*` ✔ |
| Nested styles / GREP styles | `type.para`/style `para.nestedStyles:[{style,delimiter:"words",count}]` ✔, `grepStyles:[{style,pattern}]` |
| Object styles | `style.object.create {fromSelection}`, `.apply`, `.clearOverrides` |
| Table and cell styles | `style.table.create|apply` ✔, `style.cell.create|apply` ✔ |
| Load styles from another document | `style.load {path}` (.designcraft or .idml) |
| Find/Change text + GREP + formats | `find.find`, `find.change {grep, paraStyle, charStyle, attrs}` ✔ |
| Spelling, dictionary, autocorrect | `spelling.check`, `spelling.addWord`, `prefs.set {autocorrect}` |
| Track changes / notes | `changes.track|list|acceptAll`, `note.new|list` |
| Swatches: process, spot, tint, gradient, groups | `swatch.create {color, spot}` ✔, `swatch.options {tint,base}`, `object.gradient` ✔, `swatch.newColorGroup` |
| Apply fill/stroke | `object.fill {swatch,tint}` ✔, `object.stroke`, `object.color` (unnamed) |
| Color theme from image | `color.extractTheme`, `swatch.addColorTheme` |
| Color settings / convert | `color.settings`, `color.convert` |
| Layers | `layer.new|set|activate`, `object.setLayer` |
| Transform / align / distribute / step & repeat | `transform.*`, `object.align`, `object.distribute`, `edit.stepAndRepeat`, `frame.grid` |
| Corner options, pathfinder, convert shape | `object.cornerOptions` ✔, `object.pathfinder`, `object.convertShape` |
| Type on a path, create outlines | `type.onPath`, `type.createOutlines` |
| Flex containers (responsive) | `flex.convert|set|add` |
| Place images / fitting / auto-fit | `place_image`, `file.place {frame}` ✔, `object.fit` ✔, `object.fittingOptions` |
| Links panel: update / relink / embed | `links.list`, `links.update`, `links.relink`, `links.embed` |
| Clipping path from alpha/edges | `object.clippingPath {type}` ✔ |
| Text wrap (box, contour, jump) | `object.textWrap {mode,offset,contour}` ✔ |
| Captions from metadata | `object.caption {text:"{name}", live}` |
| Libraries / snippets / content conveyor | `library.*`, `snippet.export|place`, `conveyor.*` |
| Anchored objects | `anchored.insert {ids,position}` |
| Effects panel: opacity, blend, shadow, feather… | `object.opacity {opacity,blend}` ✔, `object.dropShadow` ✔, `object.effects`, `object.feather`, `object.transparencyGroup` |
| Tables: create / convert / header / merge / cell options | `table.insert`, `table.convertFromText` ✔, `table.convertRowsToHeader` ✔ (after `table.select`), `table.merge`, `table.setCell`, `table.options` |
| Preflight | `preflight.run {minPpi}` ✔ |
| Separations preview / ink limit / ink manager | `ink.separations {page,inkLimit}` ✔, `ink.list` ✔, `ink.options` |
| Export PDF print / PDF/X | `file.exportPdf {standard:"x4"|"x1a", bleed, marks}` ✔ |
| Export PDF interactive / tagged | `file.exportPdf {tagged, bookmarksPanel, pageLayout, media}` ✔ |
| Export PNG/JPEG page | `export_png {page, scale}` ✔ (path ending .jpg → JPEG) |
| Package | `file.package {dir, pdf, idml, instructions}` |
| Hyperlinks, bookmarks, buttons, form fields | `hyperlink.create` ✔, `bookmark.add` ✔, `button.set {action}` ✔, `form.set {kind}` ✔ |
| Multi-state objects, page transitions, video | `states.create`, `page.transition` ✔, `media.options {poster}` |
| TOC, index, footnotes, cross-refs | `toc.generate {styles, createBookmarks}`, `index.*`, `footnote.insert`, `xref.insert` |
| QR code | `object.qrCode {type, content}` |
| Book, data merge, alternate layout | `book.*`, `data.merge`, `layout.createAlternate`, `liquid.pageRule` |
| EPUB / HTML / IDML / PPTX | `file.exportEpub` ✔, `file.exportFixedEpub`, `file.exportHtml`, `file.exportIdml` ✔, `file.exportPptx` |

### 3b. Not available as of 2026-11-03 (snapshot - re-check with `list_commands` before relying on it)

Not found in the 545-command list on 2026-11-03: generative AI (Text to Image,
Generative Expand, Subject-Aware wrap), Adobe Fonts / CC Libraries / Share for Review / Pantone Connect,
style packs and Auto Style, Quick Apply, saved **PDF export presets** (pass the options every time), mixed-ink
swatches, a Glyphs panel (type the Unicode character with `text.insert` instead), Animation panel,
button **Show/Hide** actions (only page/url actions; do popups in PdfCraft), import of PDF comments,
Open PDF as editable objects (place the PDF as a graphic, or paste vector art with `edit.pasteSvg`).
UI-only things (Presentation mode, Story Editor, workspaces) are irrelevant headless: use `render_page`.

## 4. Recipes (details in references/)

**Document setup** ✔ - `new_document {preset:"A4", pages, facingPages:true, margins:{top,bottom,inside,outside},
columns, gutter, bleed:9, slug:18, intent:"print"}`. Screen work: `intent:"web"`, `units:"pixels"`, no bleed.
Reusable spec → `file.savePreset`. → `references/02-document-setup-and-pages.md`

**Flyer / single-sheet** - background frame from `-bleed` to `W+bleed` (it must reach the bleed line) →
headline/body frames inside margins → image `place_image` + `object.fit {mode:"fillProportionally"}` →
`object.textWrap` → styles → `preflight.run` → PDF/X-4 with bleed + crop marks. Brochure (tri-fold):
`new_document {width:842, height:595, columns:3}` or one page per panel; keep folds in mind for margins.

**Multi-page with parents and folios** ✔ - on the parent spread draw one folio frame per side page
(left: x≈outside margin; right: x offset by page width), type a placeholder like `#` and run
`find.change {find:"#", change:"~N", grep:true, scope:"document"}`. Header via `variables.define
{type:"runningHeader", style}` + `variables.insert`. New pages: `layout.pages.insert {count, parent:"A"}`.

**Threaded text** ✔ - frame + `set_story_text` (`\n` = new paragraph) → check `overset` in the result →
`text.thread {from:<frame>, rect:[…], spread, autoflow:true}` adds frames per column and pages as needed.
Multi-column body in one frame: `object.textFrameOptions {columns, gutter}`.

**Consistent typography** ✔ - define `Body` first, base headings on it (`basedOn`, `nextStyle`), use
`spaceBefore/After` instead of empty paragraphs, character styles for emphasis applied with
`find.change {charStyle}`; nested styles for run-in heads; `keepWithNext` on headings. → `07`, `08`.

**Tables** ✔ - tab-separated text → `text.select` → `table.convertFromText` → `table.select {row:0}` +
`table.convertRowsToHeader` → cell styles (header with its own paragraph style, e.g. white text) → table
style with `altRows` → `table.options {repeatHeader}` for long tables. → `09-tables.md`

**Images and wrap** ✔ - `file.place {path, frame}` → `object.fit` → `object.textWrap {mode:"boundingBox"|
"contour", offset}`; cut-outs: `object.clippingPath {type:"alpha"}`; alt text with `object.altText`.
Effective resolution ≥ 300 ppi for print (preflight `minPpi:300`), ~150 ok for screen PDF.

**Colour** ✔ - print: CMYK process swatches `{c,m,y,k}`, spot only for brand inks (`spot:true`, one plate
each, check `ink.list`); tints with `object.fill {tint}`; screen: RGB hex. Rich black only for large areas;
small text in 100K. Check `ink.separations {inkLimit:300}` → `overLimit.pixels` must be 0. → `04-color.md`

**Preflight and export** ✔ - `preflight.run {minPpi:300}` (overset = error, low-res = warning) →
print: `file.exportPdf {standard:"x4", bleed:true, marks:{crop:true,bleed:true}}` (x1a if the printer
wants flattened CMYK) → screen: `{tagged:true, bookmarksPanel:true, pageLayout:"twoUpCover"}` →
social: document in pixels (1080×1350, 1080×1080, 1080×1920) and `export_png {scale:1}` ✔ →
printer handoff: `file.package`. → `12-preflight-print-export.md`

**Interactive PDF** ✔ - links (`hyperlink.create`), nav buttons (`button.set {action:"nextPage"}` → exported
as a link), text fields (`form.set`), bookmarks, TOC with `createBookmarks`, then verify/extend in PdfCraft
(`doc_open` → `link_list`, `form_fields`, `form_set_actions {show,hide}` for popups). →
`13-interactive-pdf-and-pdfcraft.md`

## 5. Common mistakes and delivery checklist

- Coordinates on the wrong page: right-hand pages start at x = page width in spread space.
- Background stops at the trim instead of the bleed → white hairline after cutting.
- Empty paragraphs for spacing, double spaces, manual line breaks to fix rag → use styles/Find-Change.
- Local overrides instead of styles; redefine the style (`style.paragraph.redefine`) when the look changes.
- Overset text hidden in a small frame; tables longer than their frame also go overset.
- Applying a spot colour by accident to a photo-heavy job, or two names for the same spot ink.
- Soft effects/transparency in PDF/X-1a get rasterised (warning in the export result): prefer x4.
- `table.convertRowsToHeader` fails "not in a table cell" unless `table.select` comes first ✔.
- `text.insert` straight quotes: typographer's quotes depend on `prefs.set {typographersQuotes}`.

Before delivery: `inspect_document` (no `overset:true`, no hidden/locked surprises) → `preflight.run`
with 0 errors → `links.list` all `ok` → `font.list` nothing `missing` → `render_page {bleed:true}` on every
page → `ink.separations` for print → export → reopen the PDF in PdfCraft (`print_readiness`, `link_list`,
`form_fields`) → deliver the PDF and keep the working file.

## 6. References, maintenance and sources

`references/`: 01-workspace-and-basics · 02-document-setup-and-pages · 03-objects-layers-wrap ·
04-color · 05-flowing-text · 06-editing-text · 07-typography · 08-styles · 09-tables ·
10-graphics-and-links · 11-transparency-and-effects · 12-preflight-print-export ·
13-interactive-pdf-and-pdfcraft · 14-long-documents-and-automation. Read the matching file before a
non-trivial task in that area.

Related ArtCraft skills (if installed): vectorcraft-expert (logos, vector art), photocraft-expert (image
prep), filmcraft-expert / effectcraft-expert (video and motion).

**Keeping this skill current.** DesignCraft changes almost daily. When a command listed as missing in §3b
appears, a param name changes, or a recipe stops working, update this skill (or open an issue on the
repository) with the date and the `list_commands` evidence.

**Sources.** The workflow is informed by Adobe's *InDesign Classroom in a Book 2026 Release* (Adobe Press)
and verified against DesignCraft's live command catalogue on 2026-11-03. It is written independently and
reproduces no text from the book.
