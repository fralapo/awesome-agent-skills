# 07 - Typography: spacing, fonts, glyphs, columns, alignment, drop caps, justification, tabs, rules (lesson 8)

Snapshot of DesignCraft on 2026-11-03: the apps update daily, so re-check absent features with `list_commands {filter}` before using a workaround; the Adobe behaviour described here is the target.

Source: synthesis of *InDesign Classroom in a Book 2026*, lesson 8. ✔ = verified 2026-11-03.

## Concepts
- **Vertical rhythm**: leading + baseline grid + space before/after (never empty paragraphs, which end up
  at column tops). Headings get more space before than after, so they belong to what follows.
- **Fonts**: a family has styles (Regular, Italic, Bold…); bold/italic = choosing a style of the family.
  OpenType features: ligatures, swashes, fractions, old-style/tabular figures, stylistic sets. Special
  characters (©, ™, bullets, dashes) via glyphs; maths via Math Expressions.
- **Readable type** depends on font, size, line length (column width), leading, alignment, hyphenation.
- **Span/split columns**: a headline can span all columns of a multi-column frame; a list can split
  one column into several.
- Avoid manual break characters for layout: text reflows and the break ends up in the wrong place.
- **Alignment**: left, centre, right, justified (with last line options), towards/away from spine;
  **optical margin alignment** hangs punctuation outside (set its size to the body size).
- **Drop caps**: lines + characters, combined with a character style; save it in the paragraph style.
- **Kerning** (pairs) vs **tracking** (ranges); justification settings (word/letter spacing, glyph
  scaling) + paragraph composer + hyphenation control density; balance ragged lines; no-break and
  non-breaking spaces glue words.
- **Tabs** are paragraph-level: each row its own paragraph; leaders fill the gap (menus, price lists).
- Bullets/numbering, paragraph shading and borders, rules above/below.

## DesignCraft (attribute names are exact; full list = error of an invalid attribute ✔)
| Task | Command / attribute |
|---|---|
| Character | `type.char {attrs:{fontFamily, fontStyle, size, leading:{kind:"points",value:14}|{kind:"auto"}, tracking, kerning, baselineShift, hScale, capitalization, position, underline, ligatures, noBreak, fill}}` ✔ |
| Quick | `type.bold|italic|underline|allCaps`, `type.sizeUp|sizeDown`, `type.changeCase` |
| Paragraph | `type.para {attrs:{align, leftIndent, firstLineIndent, rightIndent, spaceBefore, spaceAfter, keepWithNext, keepLinesTogether, keepFirst, keepLast, balanceRagged, hyphenate, composer, wordSpaceMin/Desired/Max, letterSpace*, glyphScale*}}` |
| Span columns | `type.para {attrs:{spanColumns:{kind:"span", columns:0}}}` ✔ (kinds: single, span, split; `spanSpaceBefore/After`) |
| Drop cap | `type.para {attrs:{dropCapLines:3, dropCapChars:1, dropCapStyle:"DropCap"}}` ✔ |
| Optical margin | `story.options {opticalMargin:true, opticalMarginSize:10}` |
| OpenType | `type.openType {feature:"frac"|"dlig"|"swsh"|…, figures:"tabularLining"}` |
| Kerning pair | `type.kernPair` |
| Tabs | `type.tabs.add {position, align:"right"|"char", leader:".", alignOn:","}` (+ get/move/remove/clear) |
| Lists | `list.bullets`, `list.numbers`, `type.para {bulletChar, numberStyle, listTab…}` |
| Shading / border / rules | `type.para {shadingOn:true, shadingColor, borderOn, ruleAbove:{on, weight, color, offset}}` |
| Glyphs panel | **Not available as of 2026-11-03 (re-check `list_commands`)**: insert the Unicode character with `text.insert` (e.g. "½", "©", "–") |
| Math | `math.insert` |

## Starter values (A4/Letter body)
- Body 9.5-11 pt, leading ≈ 120-140% of size, 45-75 characters per line.
- Space after body 0.5 line or use first-line indent (not both). Headings `keepWithNext` 2 ✔.
