# 14 - Long documents and automation (DesignCraft extras beyond the lessons)

Not a lesson of the book: features the book mentions in passing (TOC, captions, data, books, alternate
layouts) that DesignCraft exposes as commands. Ids from `list_commands` 2026-11-03; ✔ = run.

| Need | Command |
|---|---|
| Table of contents | `toc.generate {entries:[{style:"H1", level:1}, {style:"H2", level:2}], title, titleStyle, page|rect, createBookmarks}`, `toc.update`, `toc.entries` |
| Index | `index.addReference {topic:"Level 1 > Level 2", range}`, `index.generate`, `index.update` |
| Footnotes / endnotes | `footnote.insert {text}`, `footnote.options`, `endnote.insert`, `endnote.options` |
| Cross-references | `anchor.create {name}`, `xref.insert {anchor|paragraph, format}`, `xref.defineFormat {name, definition:"<paraText /> p. <pageNum />"}` |
| Text variables | `variables.define {type:"runningHeader"|"lastPageNumber"|"chapterNumber"|"fileName"|…}`, `variables.insert` ✔ (list) |
| Book (multi-file) | `book.new {path}`, `book.add`, `book.styleSource`, `book.syncStyles`, `book.paginate`, `book.exportPdf` |
| Chapter numbering | `layout.chapterNumbering` |
| Data merge (catalogues, badges, cards) | `data.source.select {path}` → `data.placeholder.add` in a frame → `data.preview` → `data.merge {perPage, arrange, …}` → returns overset stories and missing images |
| Alternate / liquid layouts | `layout.createAlternate {name, width, height, rule}`, `liquid.pageRule`, `liquid.object`, `guide.liquid` |
| Articles (EPUB/HTML reading order) | `article.new`, `article.add` |
| EPUB | `file.exportEpub {title, author, language, coverImage, embedFonts, split}` ✔, `file.exportFixedEpub` |
| XML | `xml.tag`, `xml.mapStyle`, `file.importXml`, `file.exportXml` |
| Scripts | `script.run {text}` (same line syntax as `batch {script}`) |
| Libraries / snippets | `library.*`, `snippet.export`, `snippet.place` |
| Captions from metadata | `object.caption {text:"{name}", live:true}` |
| Spell and font audits | `spelling.check`, `font.list` ✔ |

## Patterns
- Catalogue: CSV with fields + image paths → data merge into a one-record template frame (styles already
  applied) → `preflight.run` → check `missingImages` and `oversetStories` in the merge result.
- Magazine issue: base parent with folio + running header; child parents per column count; sections for
  cover/front matter; TOC from H1/H2 styles; `book.*` only when chapters live in separate files.
- Reports: one primary text frame + smart text reflow so pages follow the text.
