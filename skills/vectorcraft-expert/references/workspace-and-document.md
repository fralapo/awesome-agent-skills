# Workspace, document setup and artboards (Lesson 1, parts of Lessons 3 and 5)

Own-words summary of Adobe Illustrator Classroom in a Book 2026 (B. Wood): "Getting to Know the Work Area", "Creating a new document", "Creating and editing artboards". VectorCraft equivalents checked with `command_list`.

## Key ideas
- Illustrator routes most work through the Properties panel, the Contextual Task Bar and menus. Headless VectorCraft has **no UI**: every menu item is a command (`command_list {filter|menu}` → `command_run {id, params}`). Panels, workspaces, zoom, pan, view rotation and the Navigator are irrelevant: look with `render_preview`, read with `doc_inspect`.
- Coordinates are **always points**, y down, origin at the top-left of the first artboard. Even in a millimetre document, `draw_shape`/`draw_path` take pt (1 mm = 2.8346 pt; A4 = 595.28 × 841.89 pt; in a pixel document 1 px = 1 pt).
- Document presets: the category (Print, Web, Mobile, Social, Film…) sets units, colour mode (CMYK for print, RGB for screens) and raster-effect resolution (300 ppi print, 72 screen).

## Creating the document
- `file.new {width, height, units, colorMode: "rgb"|"cmyk", bleed, artboards, artboardLayout, rasterEffectsPpi, preset}`; presets via `file.newPresets {category:"Social"}`.
  - Verified: `{"width":"210 mm","height":"210 mm","colorMode":"cmyk","bleed":8.5,"units":"Millimeters"}` → 595.28 pt artboard, colours stored as CMYK.
- Later changes: `document.setup` (bleed, units, white background for rasters, language and quotes); colour mode `file.documentColorMode` / `object.convertDocumentColorMode`.
- Native save: `file.save` / `file.saveAs` (.vectorcraft); `file.saveCopy`; templates `file.saveAsTemplate`, `file.newFromTemplate`.

## Artboards
- `artboard.new`, `artboard.duplicate`, `artboard.setProps` (name, size, position), `artboard.delete`, `artboard.deleteEmpty`.
- Fit: `artboard.fitToArt`, `artboard.fitToSelection`; from objects: `artboard.convertToArtboards`.
- Order and layout: `artboard.reorder`, `artboard.rearrange` (grid, spacing), `artboard.move`.
- `edit.pasteOnAllArtboards`, `edit.pasteInPlace`.
- Book practice: one artboard per variant (front/back, social sizes) in the same file, clear names, sensible order — exports and PDF pages follow artboard order.

## Rulers and guides
- Ruler origin: `document.setRulerOrigin` / `document.resetRulerOrigin`; global rulers `view.globalRulers`.
- Guides: `guide.add`, from objects `view.guides.make`, `view.guides.release`, `view.guides.lock`, `view.guides.clear`.
- Safe-area margins: draw a rectangle and turn it into a guide (`view.guides.make`), as the book does for custom guides.

## Viewing
- Outline vs Preview is unnecessary headless; to find invisible paths use `doc_inspect` (bounds, fill/stroke "None").
- `view.overprintPreview`, `view.separationsPreview`, `view.proofSetup` / `view.proofColors`; pixel preview via `file.new {previewMode:"pixel"}`.

## Common mistakes
- Treating mm values as pt.
- Working in RGB for print (or CMYK for social).
- Not setting bleed at the start, so backgrounds must be enlarged by hand later.
