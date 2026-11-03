# Colour, swatches, recolouring and Live Paint (Lesson 8)

Own-words summary of Classroom in a Book 2026, "Using Color to Enhance Artwork".

## Colour modes
- **CMYK** for print (process inks), **RGB** for screens. Set it in `file.new {colorMode}`; convert art with `edit.colors.toCMYK` / `toRGB` / `toGrayscale`, the whole document with `object.convertDocumentColorMode`.
- Colour values everywhere: `"#rrggbb"`, `[r,g,b]` 0..1, `{c,m,y,k}` 0..100, `{gray}`, `{l,a,b}`, `{swatch:"Name"}`.
- In a CMYK document RGB input is stored as CMYK unless `keepModel:true`. `doc_inspect` reports fills as hex previews (verified: K=100 text shows as `#2a2b2c`) — that is display only, not an error.
- Gamut check: `color.gamutCheck`; profiles `edit.colorSettings`, `edit.assignProfile`, `color.convert`.

## Swatches
- `swatch.new {name, color, global:true}` (verified with "Brand Orange"-style global CMYK swatch) → apply with `fill:{swatch:"Name"}` (verified).
- **Global** swatch: editing it (`swatch.edit`) updates every object using it. Spot colours are always global (`swatch.new {spot:true}` or `swatch.setSpot`). Non-global swatches are just stored values.
- **Tints**: `swatch.new {swatch:"Base", tint:40}` → "Base 40%", linked to the base; or `paint.setFill {swatch, tint}`.
- Groups: `swatch.newGroup {name, colors | fromArtwork:true, toGlobal:true}` — turn the colours of finished art into a linked palette in one step.
- Housekeeping: `swatch.list`, `swatch.unused`, `swatch.merge`, `swatch.addUsedColors`, `swatch.sortByName|sortByKind`.
- Libraries: `swatch.library.list` / `get` / `add` (Pantone-style and themed libraries), `swatch.library.save` / `load`.
- Naming (book tip): by values, appearance or role ("text header"). For clients prefer roles: `Brand Primary`, `Text`, `Background`.

## Applying and copying colour
- `set_paint {ids, fill, stroke, strokeWidth}`; low level `paint.setFill`, `paint.setStroke`, `paint.swap`, `paint.none`, `paint.default`.
- Eyedropper: `paint.sampleColor` (+ `eyedropper.setOptions` to choose which attributes it copies); full appearance `appearance.copyFrom`.
- Select everything with a colour: `select.same.fillColor`, `addon.color.select`.

## Colour Guide and harmonies
- `color.harmony` returns harmonies (complementary, analogous, triad…) and tint/shade, warm/cool, vivid/muted variations from a base colour; save as a group with `swatch.newGroup`.
- Themes: `colorTheme.list` / `save` / `addToSwatches`.

## Recolor Artwork
- Read the colours of a selection: `recolor.colors`. Remap: `recolor.apply {map:{"#old":"#new"}, method:"exact"|"preserveTints"|…, limitTo:"document"|library}`.
- Reduce the palette: `recolor.reduce`; explore: `recolor.randomize`.
- Use case from the book: produce colour variants of an illustration without touching shapes; with `limitTo` a library, colours snap to print-safe swatches.

## Live Paint
- `livePaint.make` turns overlapping paths into a Live Paint group; every enclosed area (even made by several paths) becomes fillable: `livePaint.fill` (bucket), `livePaint.strokeEdge`, gap detection `livePaint.gapOptions`, `livePaint.merge` (add paths), `livePaint.expand` / `release`.
- Ideal for colouring line drawings and traced sketches; editing the paths reflows the colour.

## Good practice
- Define the palette as global swatches **before** drawing; apply by swatch, never by loose hex values.
- For print, avoid pure RGB blacks; text black = K100 (rich black only for large areas).
- Check colour contrast for social (text on photos).
