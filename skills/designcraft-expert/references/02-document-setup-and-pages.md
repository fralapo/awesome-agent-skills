# 02 - Document setup, pages, parent pages, sections, bleed (lesson 3)

Snapshot of DesignCraft on 2026-11-03: the apps update daily, so re-check absent features with `list_commands {filter}` before using a workaround; the Adobe behaviour described here is the target.

Source: synthesis of *InDesign Classroom in a Book 2026*, lesson 3. ✔ = verified 2026-11-03.

## Concepts
- **New document settings**: intent (print / web / mobile), page size, orientation, number of pages,
  start page, facing pages, columns + gutter, margins (top, bottom, inside, outside when facing),
  bleed and slug. Units can be typed with a suffix (pt, mm, p, px); fields accept arithmetic.
- **Presets** save a recurring spec (e.g. the house newsletter) so new issues start identical.
- **Parent pages** hold everything repeated: folios, headers/footers, guides, placeholder frames.
  A parent can be *based on* another parent: the child inherits margins, folios and header and only
  changes what differs (e.g. 3-column vs 2-column). Editing the base updates the children.
- **Overriding** a parent item on a document page makes it editable locally (InDesign: Shift+Cmd-click).
- **Physical pages vs page labels**: sections restart or restyle numbering (roman numerals for front
  matter, prefix, start number). Folios sit near the outside edge, where a reader flipping pages sees them.
- **Bleed**: anything printing to the paper edge must extend past the trim at least to the bleed guide
  (common: 3 mm / 0.125 in). Plan it from the start (images may need enlarging). Slug: notes outside bleed.
- Page sizes can vary inside one document (e.g. a cover with a flap); spreads can be rotated for editing.

## DesignCraft procedure
1. `new_document {preset:"A4", pages:8, facingPages:true, margins:{top:36,bottom:48,inside:42,outside:30},
   columns:2, gutter:14, bleed:9, slug:18, intent:"print", title}` ✔. Later changes: `layout.documentSetup`.
2. Presets: `file.presets` lists them, `file.savePreset {name, …}` stores one, `file.new {preset:name}` uses it.
3. Guides: `layout.createGuides {rows, columns, rowGutter, columnGutter, fitTo:"margins"}`, `guide.add`.
4. Parent: the default is `A-Parent` (`inspect_document.parents[]` gives id and label ✔). Draw on it with
   `frame.create {spread:{kind:"parent", index:0}, rect, content:"text", text}` ✔. Facing parent spread:
   left page x 0…W, right page W…2W.
5. **Page number marker** ✔: no insert command as of 2026-11-03 (re-check `list_commands {filter:"page number"}`); meanwhile type a placeholder and convert it:
   `find.change {find:"#", change:"~N", grep:true, scope:"document"}` (GREP `~N` = current page number,
   also usable in `find.find` to locate markers). Verified: page 3 renders "Pag. 3".
6. More parents: `layout.parents.new {prefix:"B", name:"2-col"}`; margins/columns of a parent with
   `layout.marginsAndColumns {parent:"B", columns:2}`; assign with `layout.pages.applyParent {pages:[…], parent:"B"}`
   or `layout.pages.insert {count, after, parent:"B"}`.
7. Override: `layout.overrideParentItems {page, ids?}` (returns local copies), `layout.removeOverrides`,
   `layout.detachAll`.
8. Pages: `layout.pages.insert|delete|move|duplicateSpread`, `layout.pageSize {pages:[1-based], preset|width,height}`,
   `layout.rotateSpreadView`.
9. Sections: `layout.section {page:1, style:"lowerRoman"}` then `layout.section {page:5, startNumber:1, style:"arabic"}`.
10. Running headers and "of N": `variables.define {name, type:"runningHeader", style:"Heading 1"}`,
    built-in "Last Page Number" ✔; insert with `variables.insert {name}` at the caret.
11. Snippets (reusable groups): `snippet.export {path}`, `snippet.place`.

## Checks
- `render_page {page, bleed:true}`: background images/colours reach the bleed on every edge they touch.
- `inspect_document.spreads[].pages[].parent` shows which parent each page uses ✔.
