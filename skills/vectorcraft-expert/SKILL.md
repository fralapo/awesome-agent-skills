---
name: vectorcraft-expert
description: "Professional vector-illustration workflow (informed by Adobe's Illustrator Classroom in a Book 2026) mapped onto the VectorCraft MCP tools (mcp__vectorcraft__*), the ArtCraft Illustrator-class app. Use whenever you work in VectorCraft or are asked for vector graphics: logos, icons, illustrations, social posts and carousels, patterns, packaging, print files (CMYK, bleed, outlined text, PDF/X), SVG/PDF/PNG exports; or when a task is described in Illustrator terms (Pen tool, Pathfinder, Shape Builder, Image Trace, artboards, global swatches, clipping masks, blends, symbols, Recolor Artwork) and must be done in VectorCraft. Keywords - vectorcraft, artcraft, illustrator, vector, svg, logo, icon, pathfinder, shape builder, pen tool, bezier, artboard, swatch, gradient, blend, pattern, brush, image trace, export for screens, pdf/x, bleed, mcp."
version: 1.0.0
source: "Workflow informed by Adobe Illustrator Classroom in a Book 2026 Release (Adobe Press); command mapping verified against VectorCraft's live command catalogue on 2026-11-03"
---

# VectorCraft expert

Illustrator workflows, summarised independently and translated into [VectorCraft](https://getartcraft.com/apps/vectorcraft), the ArtCraft Illustrator-class vector app, driven over MCP (`mcp__vectorcraft__*` in Claude Code; the same tool names in any MCP-capable agent). Every command id below exists in the live catalogue (906 commands, 140 effects, checked 2026-11-03). Read the exact params with `command_list {filter:"<id>"}` before using an id for the first time.

## 0. Rule zero: re-check before you say "missing"
ArtCraft apps are updated almost daily. Every "absent" in this skill is a **snapshot of 2026-11-03**, not a limit. Before telling the user a feature is missing, and before using a workaround, run `command_list {filter:"<keyword>"}` (and `effect.list` / `document.formats` for effects and formats) on the live app. If the command now exists, use it with the Adobe workflow described here (the target behaviour stays documented for that reason), and update this skill (or open an issue on the repository) so the snapshot stays accurate.

## 1. How VectorCraft works (read first)
- **No UI.** Every menu item is a command: `command_list {filter|menu, brief}` → `command_run {id, params}`; several at once with `command_batch`. Convenience tools: `draw_shape`, `draw_path`, `set_paint`, `pathfinder`, `add_text`, `text_wrap`, `transform`, `apply_effect`, `export`, `doc_inspect`, `render_preview`.
- **Coordinates are points**, y down, origin top-left of artboard 0, even in mm documents (1 mm = 2.8346 pt). A4 = 595.28 × 841.89 pt.
- **Work by id.** New objects come back with an id and become the selection. Pass `ids` to commands; for param-less commands (e.g. `type.createOutlines`) call `select.set {ids}` first.
- **New-art default = white fill + 1 pt black stroke.** For flat shapes pass `stroke:"none"`.
- **Look and verify constantly**: `render_preview {max_side}` after each block of work, `doc_inspect` (bounds, fills, layers, `overflow` of text) before delivery.
- Never open or overwrite the user's files unless asked; tests go in a new document (`file.new`) closed with `file.close {index}`.
- **File access is sandboxed.** The server reads and writes only under its allowed root (e.g. `~/Craft` in a default install); check the server instructions or the error message for the actual root and use paths inside it for `open_file`, `file.place`, `save_file` and `export`.

## 2. Vector principles and recommended workflow
Vector art = paths (anchors + Bézier handles) with fill/stroke/appearance; resolution-independent, editable, small. Keep it **live** (live shapes, global swatches, styles, symbols, repeats, effects) as long as possible; expand/outline only for the final deliverable copy.

1. **Brief and setup** — purpose, sizes, output (screen → RGB/px/72 ppi; print → CMYK/mm/300 ppi/bleed). `file.new {width,height,units,colorMode,bleed,artboards}`; one artboard per format/variant (`artboard.new`, `artboard.setProps`).
2. **Structure** — layers before drawing: Background / Artwork / Text / Logo / Notes (`layer.new`, `layer.setCurrent`); guides and safe areas (`guide.add`, `view.guides.make`).
3. **Palette** — global swatches first (`swatch.new {global:true}`, `swatch.newGroup`), type styles (`paraStyle.new`, `charStyle.new`).
4. **Construction** — big shapes first: live shapes, Shape Builder, Pathfinder, Pen paths (`draw_path {d}`); name every object.
5. **Colour and depth** — swatches, gradients, blends, patterns, appearance stacks.
6. **Details** — type, brushes, effects, symbols, masks.
7. **Check** — `render_preview`, `doc_inspect`, preflight (§6).
8. **Export** — source `.vectorcraft` + deliverables (§4 recipes, references/export-and-sharing.md).

## 3. Mapping: Illustrator function → VectorCraft
Legend: ✅ exists (id), ✔ verified with a real call on 2026-11-03, ⏳ not available as of 2026-11-03 (searched in the full catalogue; snapshot — re-check, see §0 and §3b).

| Illustrator | VectorCraft | |
|---|---|---|
| New document / presets / bleed | `file.new`, `file.newPresets`, `document.setup` | ✔ |
| Artboards (new, options, fit, rearrange) | `artboard.new`, `.setProps`, `.fitToArt`, `.rearrange`, `.duplicate` | ✅ |
| Rulers, guides | `document.setRulerOrigin`, `guide.add`, `view.guides.make` | ✅ |
| Zoom, pan, rotate view, Navigator, workspaces, Contextual Task Bar | n/a headless — use `render_preview` | ⏳ |
| Selection / Direct Selection | `select.set`, `select.anchors`, `select.segments` | ✅ |
| Select Same, Magic Wand, Save Selection | `select.same.*`, `select.magicWand`, `select.save` | ✅ |
| Group / Isolation mode | `object.group`, `object.isolate` | ✅ |
| Arrange | `object.arrange.*` | ✅ |
| Align / Distribute (to key, to artboard) | `object.align`, `object.distribute`, `object.distributeSpacing` | ✅ |
| Hide / Lock | `object.hide`, `object.lock`, `object.showAll`, `object.unlockAll` | ✅ |
| Rectangle, Ellipse, Polygon, Star, Line | `draw_shape` | ✔ |
| Arc, Spiral, Flare, grids | `shape.arc`, `shape.spiral`, `shape.flare`, `shape.rectangularGrid`, `shape.polarGrid` | ✅ |
| Live corners / live shape props | `object.setLiveShape`, `object.expandShape` | ✅ |
| Draw Inside / Behind | `view.drawMode` (or explicit clipping mask) | ✅ |
| Scissors | `path.split`, `path.cutAtAnchors` | ✅ |
| Knife / Eraser / Path Eraser | `path.knife`, `path.eraseRegion`, `path.eraseSegments` | ✅ |
| Join (command / tool), Average | `path.join`, `path.joinScrub`, `path.average` | ✅ |
| Compound path | `object.compoundPath.make` | ✅ |
| Outline Stroke / Offset Path / Simplify | `object.path.outlineStroke`, `.offsetPath`, `.simplify` | ✅ |
| Shape Builder | `shapeBuilder.merge`, `shapeBuilder.regions` | ✅ |
| Pathfinder (destructive) | tool `pathfinder` / `object.pathfinder.*` | ✔ minusFront |
| Shape modes (live compound shape) | `object.compoundShape.make` / `pathfinder.*` effects | ✅ |
| Width tool / width profiles | `stroke.widthPoint.set`, `stroke.widthProfile.*`, `stroke.set {profile}` | ✅ |
| Intertwine | `object.intertwine.make` | ✅ |
| Move / Rotate / Scale / Reflect / Shear | `object.move`, `.rotate`, `.scale`, `.reflect`, `.shear`, tool `transform` | ✅ |
| Transform Again / Transform Each | `object.transformAgain`, `object.transformEach` | ✅ |
| Scale Strokes & Effects / Corners | `strokes`, `corners` params of transforms | ✅ |
| Repeat radial / grid / mirror | `object.repeat.radial`, `.grid`, `.mirror` | ✔ radial |
| Puppet Warp | `object.puppetWarp`, `.pins` | ✅ |
| Dimension tool | `dimension.create` | ✅ |
| Pen tool / anchors / handles | `draw_path {d | points}`, `path.setHandle`, `path.convertAnchors`, `path.insertAnchor` | ✔ draw_path |
| Curvature / Pencil / Smooth | `path.curvature`, `path.freehand`, `path.smoothRegion` | ✅ |
| Dashes, caps, arrowheads | `dash`/`cap` on draw tools, `stroke.set {startArrow,endArrow,alignDashes}` | ✅ |
| Fill / stroke colour | `set_paint`, `paint.setFill`, `paint.setStroke` | ✔ |
| Global / spot swatches, tints | `swatch.new {global, spot, tint}`, `swatch.edit` | ✔ global |
| Colour groups, libraries | `swatch.newGroup`, `swatch.library.*` | ✅ |
| Eyedropper | `paint.sampleColor`, `appearance.copyFrom` | ✅ |
| Colour Guide / harmonies | `color.harmony`, `colorTheme.*` | ✅ |
| Recolor Artwork | `recolor.colors`, `recolor.apply`, `recolor.reduce` | ✅ |
| Generative Recolor | — | ⏳ |
| Live Paint | `livePaint.make`, `livePaint.fill`, `livePaint.gapOptions` | ✅ |
| Convert colour mode / overprint | `edit.colors.toCMYK`, `object.setOverprint`, `view.overprintPreview` | ✅ |
| Point / area type | `add_text` (`width/height`, `fit`) | ✔ point |
| Type on a path | `add_text {path, mode:"onPath"}` | ✔ |
| Threaded text / columns | `text.thread.create`, `text.areaOptions` | ✅ |
| Character / paragraph formatting | `text.setStyle`, `text.setRangeStyle` | ✅ |
| Paragraph / character styles | `paraStyle.*`, `charStyle.*` | ✅ |
| Lists, glyphs, find/replace, missing fonts | `text.startList`, `type.insert`, `edit.findReplace`, `text.missingFonts` | ✅ |
| Text wrap | `object.textWrap.make`, tool `text_wrap` | ✅ |
| Envelope warp | `object.envelope.makeWithWarp`, `.makeWithMesh`, `.makeWithTopObject` | ✅ |
| Create Outlines | `type.createOutlines` (on selection) | ✔ |
| Retype | — | ⏳ |
| Layers, sublayers, locate, merge, template | `layer.new`, `layer.newSublayer`, `layer.locate`, `layer.merge`, `layer.template` | ✔ layer.new |
| Clipping mask (object / layer) | `object.clippingMask.make`, `layer.clippingMask.toggle` | ✅ |
| Linear / radial gradient (fill, stroke) | `fill:{gradient}` on any paint param | ✔ linear |
| Freeform gradient | `paint.freeform.*` | ✅ |
| Gradient mesh | `object.mesh.*` | ✅ |
| Blend (steps, smooth, spine) | `object.blend.make`, `.options`, `.replaceSpine` | ✔ steps |
| Patterns (make, edit, apply) | `object.pattern.make/edit/done`, `pattern.options`, `{swatch}` | ✅ |
| Calligraphic / Art / Scatter / Pattern / Bristle brushes | `brush.list`, `brush.apply`, `brush.new`, `brush.options` | ✔ Art brush |
| Paintbrush / Blob Brush | `brush.freehand`, `path.blob` | ✅ |
| Appearance (multiple fills/strokes) | `appearance.addFill`, `appearance.addStroke`, `appearance.*` | ✅ |
| Live effects (Distort, Stylize, Warp, Photoshop effects) | `effect.apply`, `effect.list`, `effect.setParams` | ✔ drop shadow |
| Raster effects resolution | `document.rasterEffectsSettings` | ✅ |
| 3D (extrude, revolve, inflate, lighting) | `threeD.*` effects, `effect.lightingPreset` | ✅ |
| 3D materials (Substance) / 3D export (OBJ, USDZ, GLTF) | — | ⏳ |
| Graphic styles | `graphicStyle.new`, `.apply`, `.redefine` | ✅ |
| Symbols (static/dynamic), Symbol Sprayer | `symbol.new {type}`, `symbol.place`, `symbol.spray`, `symbol.instance.setAppearance` | ✅ |
| Creative Cloud Libraries (cloud sync) | local only: `library.*` (export/import file) | ⏳ cloud sync |
| Global Edit | `select.globalEdit`, `select.globalEditOptions` | ✅ |
| Mockup | — (workaround: envelope/perspective + Multiply) | ⏳ |
| Perspective grid | `perspective.*` | ✅ |
| Place image (link/embed), multi-place | `file.place`, `file.place.queue` | ✔ |
| Crop image / mask image | `object.cropImage`, `object.maskImage` | ✅ |
| Opacity mask | `transparency.makeOpacityMask` and related | ✅ |
| Links panel (relink, embed, update) | `links.*` | ✅ |
| Image Trace | `imageTrace.make`, `imageTrace.makeAndExpand` | ✔ |
| Text to Vector / Gen Shape Fill / Gen Expand | — | ⏳ |
| Package | `file.package` | ✅ |
| Save as PDF / presets / PDF/X | `document.exportPdf`, `pdf.preset.*` | ✔ PDF/X-4 |
| Export As (SVG, PNG, JPG…) | tool `export` | ✔ SVG, PNG |
| Export for Screens / Asset Export | `document.exportForScreens`, `assets.add`, `assets.export` | ✅ |
| Trim marks | `object.createTrimMarks`, PDF `marks` | ✔ PDF marks |
| Invite to Edit / Share for Review / cloud documents | — (share exports manually; comment on the PDF) | ⏳ |

**Count (snapshot 2026-11-03):** 84 rows mapped; 76 available in VectorCraft (20 of them verified with real calls), 8 rows not available yet — see §3b.

## 3b. Not available as of 2026-11-03 (snapshot — re-check)
Re-check each with `command_list {filter}` before saying it is missing (§0). The Adobe behaviour is the target: apply it as soon as the command appears.
| Illustrator feature (target behaviour) | Filter to re-check | Workaround today |
|---|---|---|
| UI navigation: zoom, pan, rotate view, Navigator, workspaces, Contextual Task Bar | `view.`, `zoom` | not needed headless: `render_preview`, `doc_inspect` |
| Generative Recolor — colour variants from a text prompt | `recolor`, `generat` | `color.harmony` + `recolor.apply {map}`, one PNG per variant |
| Retype — identify fonts in outlines/images, make outlined text live again | `retype`, `font` | identify the font by eye, retype with `add_text` |
| 3D materials (Substance) and 3D export OBJ/USDA/USDZ/GLTF | `material`, `document.formats` | `threeD.*` effects with lighting; export 2D (PNG/SVG/PDF) |
| Creative Cloud Libraries cloud sync across apps/devices | `library` | local `library.*`, `library.export`/`import` via a shared folder |
| Mockup — art bent onto product photos automatically | `mockup` | `file.place` photo + envelope mesh/perspective + Multiply + clipping mask; or a raster editor with smart objects |
| Text to Vector Graphic, Generative Shape Fill, Generative Expand | `generat`, `vector`, `expand` | agent draws the art (`draw_path {d}`), clips details into outlines, extends backgrounds by hand (references/generative-ai.md) |
| Invite to Edit / Share for Review (cloud documents, browser comments) | `share`, `invite`, `review` | deliver PNG/PDF through the project's shared folder or channel; collect comments on the exported PDF |

## 4. Recipes
**Logo** — 1) square artboard 1000×1000 pt RGB (or CMYK if print-first); 2) global swatches for 1–3 brand colours; 3) build the mark from live shapes, Shape Builder and Pathfinder, curves with `draw_path {d}` (few anchors); align on geometric bounds; 4) wordmark with `add_text`, kerning/tracking via `text.setStyle`; 5) variants on extra artboards: full colour, one colour, reversed, mark only; 6) delivery copy: `type.createOutlines`, `object.path.outlineStroke`, `object.expandShape`, unite same-colour pieces; 7) export SVG (`outlineText:true`), PNG 2x, PDF; keep the live source.
**Icon set** — grid of artboards (e.g. 24 or 48 pt, `artboard.rearrange`); keyline guides; consistent stroke weight, caps and corner radius; draw on whole/half points; strokes outlined at the end; `document.exportForScreens {formats:[{format:"svg"},{format:"png",scale:"2x"}]}` with artboard names as file names.
**Illustration** — layers per plane (sky, background, midground, subject, foreground); big flat shapes first, then shading with blends/gradients/freeform gradients, texture with brushes or patterns; colour via global swatches so `recolor.apply` can make variants; masks to keep everything inside the frame.
**Social post / carousel** — px document at the platform size (1080×1350 feed, 1080×1920 story), one artboard per slide; keep a consistent grid and safe margins across slides, leave room for platform UI overlays, let photos be large, avoid decorative placeholder icons, and break lines at natural phrase ends rather than mid-sentence; for many similar slides, generating an SVG per slide and opening/placing it is often faster than drawing each by hand; check `overflow`; export PNG with `useArtboards` and `range`.
**Pattern** — motif from a few shapes with global colours → `object.pattern.make {tileType}` → `pattern.options` spacing → `object.pattern.done`; test on a large rectangle with `render_preview`; colourways with `recolor.apply`.
**Print file / packaging** — CMYK document at final size in mm, bleed 3 mm (8.5 pt) or as the printer asks, safe margin guides; backgrounds extended to the bleed; images ≥ 300 ppi effective, embedded or packaged; black text K100, rich black only on big areas; overprint check `view.overprintPreview`; die-cut line on its own non-printing or spot layer (`swatch.new {spot:true}`); `document.exportPdf {standard:"pdfX4" (or pdfX1a), bleed:{useDocument:true}, marks:{trim:true}, advanced:{outlineText:true}}`; read all warnings; `file.package` for the source.
**Exports** — SVG for web/UI (`outlineText:true`, minify), PNG for social and slides (`scale`), JPG for photo-heavy posts, PDF for print/review, `.vectorcraft` always as source. Details: references/export-and-sharing.md.

## 5. Common mistakes
- mm values passed as pt; RGB file sent to print; no bleed.
- Default white fill + black stroke left on shapes.
- Commands applied to the wrong selection (no `ids`).
- Text overflow ignored (`overflow:true`), fallback fonts ignored (`warning` in `text.setStyle`).
- Expanding/outlining the only copy; no live source kept.
- Pathfinder on stroked objects without outlining strokes; open paths that should be closed.
- Raster effects (shadows, glows) assumed to stay vector; low raster-effect ppi for print.
- Gradient `angle:90` runs bottom → top (stop 0 at the bottom).
- Hex values in `doc_inspect` of a CMYK file are previews, not the stored colour.

## 6. Preflight before delivery
1. `doc_inspect {depth:0}` → layers named, nothing unexpected hidden/locked; `doc_inspect {kind:"Type"}` → text content, no overflow.
2. `select.object.strayPoints`, `select.object.openPaths`, `addon.cleanup.check` → delete stray points, fix open shapes.
3. Colours: `swatch.unused`, `recolor.colors` on everything; CMYK only for print, no RGB images (`edit.colors.toCMYK`), K100 text.
4. `links.check` → no missing images; `text.missingFonts` → none.
5. `render_preview` of **every** artboard at `max_side` ≥ 1024; compare with the brief.
6. Export, then reopen/inspect the export (PDF warnings, PNG pixel size, SVG viewBox).
7. Deliver the exports plus the live `.vectorcraft` source together, with clear file names (project, format, variant), to wherever the requester expects them.

## 7. References
- references/workspace-and-document.md — setup, artboards, rulers, guides
- references/selection-and-transform.md — selecting, aligning, transforming, repeats
- references/shapes-and-pathfinder.md — live shapes, cutting/joining, Shape Builder, Pathfinder, width, intertwine
- references/pen-and-curves.md — Bézier paths, Pen/Curvature/Pencil, dashes, arrows
- references/color.md — colour modes, swatches, Recolor, Live Paint
- references/type.md — point/area/path type, styles, wrap, warp, outlines
- references/layers.md — layers and clipping masks
- references/gradients-blends-patterns.md
- references/brushes.md
- references/effects-and-appearance.md — appearance, effects, 3D, graphic styles
- references/time-savers.md — symbols, libraries, global edit, mockups
- references/images-and-image-trace.md — placing, masks, links, Image Trace
- references/export-and-sharing.md — package, PDF, export for screens, collaboration
- references/generative-ai.md — Illustrator AI features and agent substitutes

## Sources
The workflow is informed by Adobe's *Illustrator Classroom in a Book 2026 Release* (Adobe Press) and verified against VectorCraft's live command catalogue on 2026-11-03. It is written independently and reproduces no text from the book.
