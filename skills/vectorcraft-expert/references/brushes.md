# Brushes and Blob Brush (Lesson 12)

Own-words summary of Classroom in a Book 2026, "Using Brushes to Create a Social Ad".

## Brush types
| Type | What it does | Typical use |
|---|---|---|
| Calligraphic | stroke like an angled pen nib | lettering, ink look |
| Art | stretches artwork along the path | tapered strokes, ribbons, hand-drawn lines |
| Scatter | scatters copies of an object along the path | confetti, leaves, dots |
| Pattern | repeats tiles (side, corners, start, end) along the path | borders, chains, stitches, frames |
| Bristle | simulates a real brush with transparency | painterly strokes (raster-like at export) |

Built-in brushes in VectorCraft (`brush.list`, verified): 3 pt Round, 6 pt Flat, 10 pt Oval (calligraphic); Charcoal, Tapered Stroke, Arrow (art); Dots, Confetti, Leaves (scatter); Chain, Stitches, Diamonds (pattern); Bristle Round, Bristle Flat Fan (bristle). More via `brush.libraries` / `brush.library` / `brush.addFromLibrary`.

## Applying
- Draw a path (`draw_path`, fill `none`), then `brush.apply {name, ids}` (verified: Tapered Stroke on a Bézier curve). Paintbrush equivalent: `brush.freehand`.
- Remove: `brush.remove` (back to a basic stroke).
- Stroke weight scales the brush; path direction decides where an Art brush starts (`path.reverse` to flip).

## Creating brushes
- `brush.new` from selected artwork (Art and Scatter need art selected; Pattern uses the art as side tile by default). Options: `brush.options` (colourisation: none / tints / hue shift — use tints so a single-colour brush follows the stroke colour).
- Duplicate/edit: `brush.duplicate`, `brush.options`; brush made from current selection `brush.selectionArt`.
- Expand to editable shapes: `object.expandBrush` (needed before Pathfinder or before sending to a cutter/plotter).
- Save sets: `brush.saveLibrary` / `brush.loadLibrary`.

## Blob Brush and Eraser
- Blob Brush (`path.blob`) paints **filled shapes**, not strokes; overlapping strokes of the same colour merge into one shape. Good for quick filled drawing and mascots.
- Eraser (`path.eraseRegion`) cuts filled shapes; select the target first so only it is affected (book tip). Use short strokes rather than one long gesture.

## Common mistakes
- Applying brushes to closed filled shapes and getting odd overlaps: brush the outline path, keep fills separate.
- Bristle and some effects rasterise in PDF/SVG: check exports; avoid them for logos.
- Forgetting to expand brushes before a deliverable that must be pure paths.
