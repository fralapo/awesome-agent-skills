# Type (Lesson 9)

Own-words summary of Classroom in a Book 2026, "Adding Type to a Project".

## Kinds of type
- **Point type**: a single line that grows as you type; for titles and labels. `add_text {text, x, y, size, font, color, justify}` (x,y = first baseline).
- **Area type**: text flows in a frame; for paragraphs. `add_text {…, width, height, fit:"autoHeight"|"shrinkText"}`. The reply has `overflow:true` when text does not fit (Illustrator's red plus in the out port) — always check it.
- **Type on/in a path**: `add_text {text, path:id, mode:"onPath"|"area", pathEffect: rainbow|skew|3dRibbon|stairStep|gravity}` (verified on an open Bézier path). Path options later: `type.pathOptions`.
- Convert: `type.convertToAreaType` / `type.convertToPointType`; vertical `type.orientation.vertical`.
- Import a .txt: `file.place {path:"x.txt"}` → area type.

## Threading and columns
- `text.thread.create` (link frames), `text.thread.add`, `.break`, `.remove`, `.info`. Only area type or type on a path can thread.
- Columns, inset, first-baseline and vertical alignment: `text.areaOptions`. Reshape the frame: `text.reshapeArea`.

## Formatting
- Character: `text.setStyle {ids, font, style, size, leading, tracking, justify, fill, features:["lnum","-liga"], start, end}` (range in bytes).
- Ranges and paragraphs: `text.setRangeStyle`, `text.setFormat`, `text.editRange`, `text.getRange`; tabs `text.tabs.set`.
- Fonts: `text.fontList`, `text.fonts`, missing fonts `text.missingFonts`, `text.replaceFont`, add files `text.addFontFiles`. A `warning` in the reply means the font fell back — fix it before delivery.
- Fit headline: `type.fitHeadline`; case `type.changeCase`; smart quotes `type.smartPunctuation`; optical margins `type.opticalMarginAlignment`; size steps `type.size.increase|decrease`.
- Lists: `text.startList`, `text.convertListToText`.
- Find/replace: `edit.findReplace`.

## Styles
- Paragraph styles (whole paragraphs: indents, spacing, leading): `paraStyle.new`, `paraStyle.apply`, `paraStyle.redefine`, `paraStyle.setAttrs`.
- Character styles (selected characters only: a bold word, a colour): `charStyle.new`, `charStyle.apply`, `charStyle.redefine`.
- Book rule: build styles once, apply everywhere; editing the style updates every use.

## Wrapping and warping
- Text wrap around an object: `object.textWrap.make` / `.options` / `.release` (or tool `text_wrap`). The wrapping object must be above the text.
- Envelope warp presets on text: `object.envelope.makeWithWarp` (arc, arch, flag, rise…), edit content `object.envelope.editContents`, `object.envelope.expand`. Alternative: live `warp.*` effects (see effects-and-appearance.md).

## Outlines
- `type.createOutlines` (no params: **select the text first** with `select.set`) — verified. Use for logos and final print files: no font dependency, effects that need paths. Keep a live-text copy (hidden layer or separate file) for future edits.
- Exports can outline on the fly instead: SVG `outlineText:true`, PDF `options.advanced.outlineText:true`.

## Not available as of 2026-11-03 (snapshot — re-check with `command_list {filter:"retype"}` / `{filter:"font"}`)
- **Retype** — target behaviour: recognises the fonts used in outlined text or in images, suggests matches, and can turn outlined text back into live editable text. Workaround today: identify the font yourself and retype with `add_text`.
- Adobe Fonts activation from the app — workaround: install font files locally and use `text.addFontFiles` / `text.rescanFonts`.

## Common mistakes
- Line breaks inside a sentence to force layout: let area type wrap; if you must break manually, prefer breaks at the end of a sentence or phrase so lines read naturally.
- Ignoring `overflow:true`: the cut text is simply not drawn.
- Delivering print PDFs with live fonts that are not embeddable.
