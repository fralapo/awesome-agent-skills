# Workspace and document basics (Lesson 1 + Getting Started)

Source: synthesis of *Photoshop Classroom in a Book 2026*, Getting Started and Lesson 1, mapped to PhotoCraft.

## Concepts
- Photoshop is mainly a bitmap (pixel) editor that also holds vector shapes and live type. Keep each element
  on its own layer so the original pixels are never touched.
- 100 % zoom = one image pixel per screen pixel; it says nothing about print size. On HiDPI screens 200 %
  approximates what a browser shows. In PhotoCraft headless mode "zoom" is irrelevant: use
  `render_preview {max_side}` for an overview and crop-like previews by exporting a region if needed.
- Foreground/background colours feed painting tools and fills (`tools.setColors`, `tools.defaultColors`
  = D, `tools.swapColors` = X).
- Place Embedded copies the file into the document as a Smart Object; Place Linked keeps a reference.
- Blend mode and opacity are independent layer properties.
- If the final medium is unknown, build a high-resolution master and derive copies.

## PhotoCraft equivalents
| Task | Call |
|---|---|
| New document from preset size (e.g. HDTV 1080p) | `doc_new {width:1920,height:1080}` or `document.presets.list` / `file.new {preset}` |
| Place an image | `doc_place {path, center, scale}` (path relative to the allowed read/write root) |
| Transform the placed layer | `edit.transform {layer, scaleX, scaleY, dx, dy}` or `rect`/`quad` |
| New/rename layer | `layer.new.layer {name}`, `layer.renameLayer` |
| Rectangle selection and fill | `select.rect {x,y,width,height}` → `edit.fill {contents:"color", color:"#ff7f00"}` → `select.deselect` |
| Layer blend mode | `layer.setProps {layer, blend:"Color", opacity:0.9}` |
| Point type | `type.create {x,y,text,font,size,color,align}`; `type.setStyle {caps:"all"}` |
| Solid colour fill layer | `layer.newFillLayer.solidColor {color}` then blend Hard Light etc. |
| Paint with a brush preset | `brush.presets.list`, `paint.stroke {points, preset|brush, size, color}` |
| Undo / redo / toggle last state | `edit.undo`, `edit.redo`, `edit.toggleLastState`; `history.selectState` |
| Guides / rulers | `view.newGuide`, `view.newGuideLayout`, `prefs.set` for units |
| Export a delivery copy | `doc_export {path:"out/x.jpg", quality:80}` (flattened; sRGB for web formats) |

## Procedure: simple promo graphic (1920×1080)
1. `doc_new` 1920×1080, `doc_save` as `.pcraft`.
2. `doc_place` the photo, `edit.transform` to cover the width.
3. New layer "Rectangles": two `select.rect` + `edit.fill` colour bands; set the layer blend to Color.
4. Headline with `type.create`, all caps, centred; a second line right-aligned on a guide.
5. Solid Color fill layer above the photo (Hard Light, 90 %) to tint it.
6. Optional brush texture on its own layer (spatter preset), opacity to taste.
7. To extend a too-narrow photo: no Generative Fill in PhotoCraft → select the empty area and
   `edit.contentAwareFill {output:"new"}` or `image.crop {contentAware:true}` when enlarging the canvas.
8. Export: `doc_export` JPG q≈60–80 at the target width (resize a duplicate with `image.imageSize` first).

## Shortcuts worth knowing (desktop app)
Z zoom, V move, Shift+letter cycles nested tools, D/X colours, Cmd/Ctrl+Z undo, Cmd+Shift+Z redo,
Cmd+Alt+Z toggle last state, Tab hides panels, Enter commits a transform (not while typing text).

## Pitfalls
- Text is committed with the check mark or by switching tool: Enter only adds a line break.
- A new layer appears above the active one (PhotoCraft: `position:"above"|"below"`).
- Redo is lost as soon as a new action is made.
- With Auto-Select on, the Move tool grabs the top-most layer under the cursor; in automation always pass
  explicit `layer` ids.
- Generative content must not be used for news/documentary images (PhotoCraft had no generative fill as of
  2026-11-03; re-check).
- Always check the destination service's specs (size, weight, format).
