# 06 - Editing text: Find/Change, GREP, spelling, track changes, notes, fonts (lesson 7)

Snapshot of DesignCraft on 2026-11-03: the apps update daily, so re-check absent features with `list_commands {filter}` before using a workaround; the Adobe behaviour described here is the target.

Source: synthesis of *InDesign Classroom in a Book 2026*, lesson 7. ✔ = verified 2026-11-03.

## Concepts
- Editing techniques apply to any text (placed Word file, pasted email, typed).
- Find/Change works on text, GREP patterns, glyphs, objects and formats; it can also *apply* styles
  or formatting to every match (e.g. turn every "Tip:" into a styled run-in).
- Spelling: decide with the client/editor who owns proofreading; add correct-but-unknown words to the
  document or user dictionary (names → all languages); dynamic spelling; Autocorrect for frequent typos
  or abbreviations to expand.
- Story Editor = plain-text view of a story; Track Changes and Notes support editorial review.
- Missing fonts are highlighted; resolve by activating or replacing them.

## DesignCraft
| Task | Command |
|---|---|
| Find | `find.find {find, grep, caseSensitive, wholeWord, scope:"document"|"story"|"selection", story, findFormat}` ✔ → byte ranges |
| Change | `find.change {find, change, grep, scope}` ✔; `first:true` for one match |
| Apply style to matches | `find.change {find:"concatenazione", change:"", charStyle:"Emphasis"}` ✔ - empty change keeps the text and only applies the format |
| Apply paragraph style to matches | `find.change {find:"^Chapter .*$", grep:true, change:"", paraStyle:"Heading 1"}` |
| GREP special | `~N` current page number ✔; standard regex groups; `"$$1"` in batch for a literal `$1` |
| Select text | `text.select {story, anchor, focus}` (UTF-8 bytes: à/— count 2-3) ✔, `text.selectParagraph`, `text.selectStory` |
| Type at caret | `text.insert {text, raw}` |
| Spelling | `spelling.check {story}` → words + suggestions; `spelling.addWord`, `spelling.setWords`, `spelling.change` |
| Hyphenation exceptions | `hyphenation.addException` |
| Autocorrect | `prefs.set {autocorrect:true, autocorrectList:[["teh","the"]]}` |
| Track changes | `changes.track {on:true}`, `changes.list`, `changes.accept|reject|acceptAll|rejectAll` |
| Notes | `note.new {text, author}`, `note.list`, `note.convertToText` |
| Conditional text | `condition.new {name}`, `condition.apply` (variants, e.g. IT/EN in one file) |
| Fonts | `font.list` ✔ (status `missing`, replacement), `font.replace {family, toFamily, redefineStyles:true}`, `font.reload` |
| Story Editor | **Not available as of 2026-11-03 (re-check `list_commands`)** as a UI; `get_story` gives the plain text (beware: whole text returned) |
| Share / InCopy | **Not available as of 2026-11-03 (re-check `list_commands`)**. |

## Notes
- Byte offsets: compute from `find.find` results rather than counting characters by hand.
- Bundled font verified: "Source Serif 4" (Regular/Italic/Bold) ✔; ask `font.list` before choosing fonts.
