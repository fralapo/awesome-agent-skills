# 08 - Styles: object, paragraph, character, nested, table/cell, global updates, loading (lesson 9)

Snapshot of DesignCraft on 2026-11-03: the apps update daily, so re-check absent features with `list_commands {filter}` before using a workaround; the Adobe behaviour described here is the target.

Source: synthesis of *InDesign Classroom in a Book 2026*, lesson 9. ✔ = verified 2026-11-03.

## Concepts
- **Object styles** bundle fill, stroke, corners, effects, text-frame options (and can name a paragraph
  style): sidebars, captions, photo frames. They can be based on each other.
- **Paragraph styles** define the whole paragraph; **character styles** only what differs (emphasis,
  bullets/numbers, lead-ins, drop caps). Build a hierarchy: Body → Body First, Heading 1 → Heading 2…
  ("Based On" propagates changes; "Next Style" chains heading → body).
- **Nested styles**: inside a paragraph style, apply a character style up to/through a delimiter
  (words, characters, a tab, a colon…) N times; **nested line styles** format first lines (small caps
  lead). **GREP styles** apply a character style to pattern matches (prices, phone numbers).
  Prerequisite: create the character style first.
- **Table and cell styles**: table border, alternating fills, header/body/footer cell styles; a cell
  style can include a paragraph style.
- Updating: edit the definition, or format one instance locally and **redefine** the style from it.
  Local overrides (the "+") are the usual culprit when something looks wrong; clear them.
- Break link to style for one-off designs; load styles from other documents to share a house style.

## DesignCraft
| Task | Command |
|---|---|
| Paragraph style | `style.paragraph.create {name, basedOn, nextStyle, para:{…type.para names…}, chars:{…type.char names…}, fromSelection}` ✔ |
| Edit / redefine | `style.paragraph.edit {name, para, chars, rename, resetToBase}`, `style.paragraph.redefine` |
| Apply | select (`text.select`) then `style.paragraph.apply {name, clearOverrides:true}` ✔ |
| Character style | `style.character.create {name, chars:{fontStyle:"Italic", fill}}` ✔, `style.character.apply` |
| Nested style | `para:{nestedStyles:[{style:"Lead-in", delimiter:"words", count:2}]}` ✔ (first two words got the char style); unknown fields are ignored silently, so render to verify |
| GREP style | `para:{grepStyles:[{style:"Price", pattern:"\\d+,\\d{2} €"}]}` (bad pattern = error) |
| Object style | `style.object.create {name, fromSelection:true}` or explicit `fill, dropShadow, …`; `style.object.apply {name, ids}`; `style.object.clearOverrides` |
| Table / cell style | `style.cell.create {name, fill, insets, vj, paragraphStyle, stroke}` ✔; `style.table.create {name, header, body, footer, border, altRows}` ✔; `style.table.apply {name, story, table}` ✔ |
| Break link | `style.breakLink` |
| Groups | `style.group` |
| List styles | `style.list` / `inspect_document.paragraphStyles` |
| Load from file | `style.load {path, paragraph:[…], character:[…], conflicts:"useExisting"}`; `style.load.list` previews |
| Quick Apply, style packs, Auto Style, CC Libraries | **Not available as of 2026-11-03 (re-check `list_commands`)** |

## House-style template (copy and adapt)
```
style.paragraph.create {"name":"Body","chars":{"fontFamily":"Source Serif 4","size":10,"leading":{"kind":"points","value":14}},"para":{"spaceAfter":6}}
style.paragraph.create {"name":"H1","basedOn":"Body","nextStyle":"Body","chars":{"size":28,"leading":{"kind":"points","value":32},"fill":"Brand Blue"},"para":{"spaceBefore":12,"spaceAfter":12,"keepWithNext":2}}
style.character.create {"name":"Emphasis","chars":{"fontStyle":"Italic"}}
```
