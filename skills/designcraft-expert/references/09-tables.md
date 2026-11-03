# 09 - Tables (lesson 10)

Snapshot of DesignCraft on 2026-11-03: the apps update daily, so re-check absent features with `list_commands {filter}` before using a workaround; the Adobe behaviour described here is the target.

Source: synthesis of *InDesign Classroom in a Book 2026*, lesson 10. ✔ = verified 2026-11-03.

## Concepts
- Tables beat tabs: cells wrap text, each cell behaves like a small text frame, and styles can target
  cells, rows, columns.
- Create from scratch, convert tab-separated text (one tab per column - Word users often type several
  tabs: clean them first), or import a Word/Excel table.
- Insert/delete/move rows and columns, distribute evenly, merge/split cells (merging hurts screen
  readers in accessible output), fill and stroke per cell or range, insets and vertical alignment.
- **Header rows** repeat on every frame/page the table continues into and are required for
  accessibility; footer rows likewise.
- Graphics in cells: convert a cell to a graphic cell, or anchor an image in the cell text.
- Table and cell styles keep long tables consistent; a table longer than its frame goes overset and
  must be threaded on.

## DesignCraft
| Task | Command |
|---|---|
| New table at caret | `table.insert {rows, cols, headerRows, footerRows, tableStyle, width}` |
| Text → table | `text.select {story, anchor, focus}` → `table.convertFromText {columnSeparator:"tab", rowSeparator:"paragraph", tableStyle}` ✔ → `{table, rows}` |
| Table → text | `table.convertToText` |
| Select | `table.select {story, table, row|rows|col|cols, what:"row"|"column"|"table"}` ✔ - most table commands act on the selection |
| Header/footer | `table.convertRowsToHeader` ✔ (needs a prior `table.select`, else "not in a table cell"), `table.convertRowsToFooter`, `table.options {headerRows, repeatHeader:true}` |
| Rows/cols | `table.insertRow|insertRowAbove|insertRowBelow|insertColumn…`, `table.deleteRow|deleteColumn`, `table.moveRow|moveColumn`, `table.sortRows` |
| Size | `table.setRowHeight`, `table.setColumnWidth`, `table.distributeColumns|distributeRows` |
| Merge/split | `table.merge`, `table.unmerge`, `table.splitHorizontally|splitVertically` |
| Cell look | `table.setCell {fill, tint, insets, vj, stroke:{weight,color,edges}, rows, cols}` |
| Table look | `table.options {border, altRows:{first,firstColor,next,nextColor}, spaceBefore, spaceAfter}` |
| Graphic cell | `table.placeGraphic` then `file.place`, or `anchored.insert` inside the cell |
| Styles | `style.cell.create` ✔, `style.table.create {header:"Head cell", altRows}` ✔, `style.table.apply` ✔ |
| Read back | `table.get` |

## Verified gotcha
- `altRows` with `first:1, next:1` alternated fills ✔, but the header text stayed black on a dark fill:
  give the header cell style a `paragraphStyle` with `[Paper]` text, or set it in the table style.
