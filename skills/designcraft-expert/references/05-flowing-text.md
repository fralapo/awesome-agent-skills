# 05 - Flowing text, threading, columns, baseline grid, jump lines (lesson 6)

Snapshot of DesignCraft on 2026-11-03: the apps update daily, so re-check absent features with `list_commands {filter}` before using a workaround; the Adobe behaviour described here is the target.

Source: synthesis of *InDesign Classroom in a Book 2026*, lesson 6. ✔ = verified 2026-11-03.

## Concepts
- Text comes in by placing a file (Word/RTF/TXT) into an existing frame, into a new frame, or flowed:
  manually (one frame at a time), semi-automatically, or **autoflow** (adds frames and pages until the
  story fits). Pre-threaded empty frames are a good template technique (catalogues, magazines).
- **Smart Text Reflow** adds/removes pages at the end when a primary story grows or shrinks.
- **Auto-size** text frames grow/shrink with their content: ideal for sidebars, coupons, buttons.
- Columns: either several threaded frames or one frame with columns + gutter (+ optional column rules,
  balanced columns).
- Clean imported text with Find/Change: double returns, double spaces, tabs used for alignment.
- Space between paragraphs comes from space before/after, never from empty paragraphs.
- **Baseline grid**: document grid (start, increment = body leading) or per-frame grid; body paragraphs
  align to it so lines line up across columns. A Basic Text Frame object style can carry it.
- **Jump line** ("continued on page X"): a text frame touching the threaded frame with a "next/previous
  page number" marker.
- Redefine a style from formatted text to update all uses.

## DesignCraft
| Task | Command |
|---|---|
| Place text file | `file.place {path, rect, autoflow:true, removeStyles, styleMap:{"Heading 1":"Title"}}`; inspect incoming styles with `place.styles` |
| Replace whole story | `set_story_text {story|frame, text}` ✔ (returns `overset` byte offset) |
| Edit a range | `story.replaceRange {story, start, end, text}` (UTF-8 byte offsets) |
| Thread / autoflow | `text.thread {from, to}`; `{from, rect, spread, autoflow:true}` ✔ → `{overset, pagesAdded}` |
| Break thread | `text.unthread`, `text.removeFromThread` |
| Smart reflow | `prefs.set {smartTextReflow:true}` + `object.primaryTextFrame {ids}` (or `new_document {primaryTextFrame:true}`) |
| Columns in one frame | `object.textFrameOptions {columns:2, gutter:14, columnRule:true, balanceColumns:true}` ✔ |
| Auto-size | `object.textFrameOptions {autoSize:"heightOnly", autoSizeReference:"topLeft"}` ✔ |
| Vertical justification / insets | `object.textFrameOptions {verticalJustification, inset}` |
| Baseline grid | `document.preferences {baselineGrid:{start, increment, relativeTo}}`; per frame `object.textFrameOptions {baselineGrid:{…}}`; paragraphs `type.para {gridAlign:"allLines"}` (values: none, allLines, firstLineOnly ✔) |
| Force to next column/frame | `type.para {startParagraph:…}` (keep options) - no break-character command as of 2026-11-03 (re-check) |
| Cleanup | `find.change {find:"\\r\\r+", change:"\\r", grep:true}`, `find:"  +"` → `" "` |
| Redefine style | `style.paragraph.redefine` (from the selection) |
| Jump line | not verified: `xref.insert` to a text anchor (`anchor.create`) with a `<pageNum />` format is the robust equivalent |

## Checks
- After every text load: `inspect_document.stories[].overset` must be false (or `null` on the story result) ✔.
- `render_page` the last frame of each thread to see that the story ends where intended.
