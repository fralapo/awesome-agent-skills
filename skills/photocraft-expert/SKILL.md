---
name: photocraft-expert
description: "Operational Photoshop know-how mapped to PhotoCraft (the ArtCraft Photoshop-class image editor, driven over MCP via the photocraft tools: doc_open, command_run, command_batch, doc_export) and, for raw development and photo-set correction, to LightCraft (the ArtCraft Lightroom-class app). Use when working in PhotoCraft or LightCraft, or for retouching, photo correction, compositing/photomontage, cut-outs and background removal, selections, layer masks, adjustment layers, smart objects and smart filters, mockups and smart-object replacement, raster graphics for social/web/print, text on images, colour consistency across photos, Camera Raw-style development, or Photoshop techniques in general. Keywords - Photoshop, PhotoCraft, LightCraft, ArtCraft, Lightroom, Camera Raw, MCP, retouch, healing, content-aware fill, select subject, refine edge, mask, curves, levels, smart object, mockup, composite, export, sRGB, CMYK, soft proof."
version: 1.0.0
source: "Informed by Adobe Photoshop Classroom in a Book 2026 Release (Adobe Press); command ids verified against PhotoCraft's live command catalogue on 2026-11-03"
---

# PhotoCraft expert

Photoshop's non-destructive working method, mapped command-by-command to **PhotoCraft** (Photoshop-class
editor) and, for raw files and photo sets, **LightCraft** (Lightroom/Camera Raw-class). Both apps are part of
the ArtCraft suite and are driven by an agent over MCP (`mcp__photocraft__*`, `mcp__lightcraft__*` in Claude
Code; the tool prefix depends on how you named the servers).

**Sources.** The workflow is informed by Adobe's *Photoshop Classroom in a Book 2026 Release* (Adobe Press),
lessons 1–15, and the command ids were verified against PhotoCraft's live command catalogue on 2026-11-03.
This skill is written independently and reproduces no text from the book.

## Verification legend

- ✔ = the command was **run successfully** on a scratch PhotoCraft document (2026-11-03).
- No mark = the id and params were **found in `command_list`** but not executed.
- ⧗ = **not available as of 2026-11-03** (dated snapshot, see rule 1 below).
- **LightCraft (`LC`) entries were not live-tested**: ids come from LightCraft's command catalogue only.
  Check `command_list {filter}` and `list_controls` on your install before relying on them.

## 0. Ground rules for the agent

1. **Re-check before saying "missing".** ArtCraft apps are updated almost daily. Anything marked ⧗ is a
   snapshot of 2026-11-03, not a permanent limit. Before telling the user a feature is missing, and before
   using a workaround, run `command_list {filter:"<keyword>"}` (PhotoCraft or LightCraft) on the live app. If
   the command now exists, read its `params` and use it the Photoshop way described here. The Adobe workflow
   stays the target in every case. Ids and params can also change between releases: if a call fails,
   re-check with `command_list` first.
2. **Pick the right app.** Raw files and batches of photos → LightCraft first; layered/raster design,
   compositing and type → PhotoCraft.
3. **Sandboxed files.** PhotoCraft only reads and writes under the server's allowed read/write root (e.g.
   `~/Craft` in a default install; check the server instructions or the error message). Paths are relative
   to that root, and subfolders must already exist (create them first), or the write fails with `NotFound`.
4. **Path-taking engine commands were disabled in automation as of 2026-11-03** ✔ (re-test)
   (`file.saveACopy`, `layer.exportAs`, `file.export.saveForWebLegacy`, `file.placeEmbedded`, …: "uses
   ambient filesystem paths"). Use the capability-scoped tools instead: `doc_open`, `doc_place`,
   `doc_replace_smart_object`, `doc_save`, `doc_export`, `doc_export_layers`, `doc_import_data_sets`,
   `doc_export_data_sets`.
5. **Never touch originals in place**: open, then `doc_save` a working copy (`.pcraft` lossless native, or
   `.psd`), and export deliverables under a new name.
6. **Discover → act → verify**: `command_list {filter:"…"}` for ids and params, `command_batch` for several
   steps (not atomic: earlier steps stay applied), `doc_inspect` for the layer tree, `render_preview` to look.
7. Long jobs (filters, Content-Aware Fill, Remove, Photomerge) block by default; use `wait:false` +
   `jobs_list`.
8. LightCraft acts on photos already in its library. Do not import into the user's library unless asked.

## 1. Recommended workflow (non-destructive)

1. **Start right**: raw or a batch of photos → develop in LightCraft (profile, WB, tone, sync), export
   16-bit TIFF/PSD for PhotoCraft. Single JPEG/PNG → `doc_open` in PhotoCraft and `doc_save` as `.pcraft`.
2. **Evaluate** before editing: `doc_inspect` (mode, depth, profile, size), `render_preview`,
   `document.pixel` / `view.colorSamplers.add` on highlights, shadows and supposed neutrals.
3. **General to specific**: tone → colour (make neutrals neutral) → remove distractions → creative colour
   → composition/crop → sharpening last, at final size.
4. **Never paint on the original pixels**: retouch on a new empty layer with `sampleAllLayers:true`, tone
   with adjustment layers (`layer.newAdjustmentLayer.*`), filters on Smart Objects (Smart Filters), cut-outs
   with layer masks instead of deleting, vector shapes and live type kept editable until export.
5. **Limit an adjustment** to one layer with a clipping mask (`clipToPrevious` / `layer.createClippingMask`),
   to an area by making a selection first (the selection becomes the adjustment's mask ✔).
6. **Name and group** layers (`layer.renameLayer`, `layer.new.groupFromLayers`), keep the master layered,
   flatten only exported copies.
7. **Check and deliver**: preview at 100%, soft-proof if printing, export per medium (section 4).

## 2. Mapping table: Photoshop → PhotoCraft / LightCraft

`PC` = `mcp__photocraft__command_run {id}` unless a tool is named. `LC` = LightCraft command id (callable as
`command_run` or `cmd_<id with _>`; LightCraft rows are catalogue-checked only, not live-tested). ✔ = executed successfully in a test. ⧗ = not available as of 2026-11-03 (snapshot — re-check with
`command_list {filter}` before saying it is missing or using the workaround).

| Photoshop | PhotoCraft / LightCraft | Notes |
|---|---|---|
| File > New / Open / Save As | `doc_new`, `doc_open`, `doc_save` ✔ | `.pcraft` native; PSD drops filters with no PSD equivalent (Liquify smart filter) ✔ |
| Place Embedded / Linked | `doc_place` ✔ (embedded smart object) | Linked placing via `file.placeLinked` is path-based: not usable from automation |
| Export As / Quick Export / Save for Web | `doc_export {path, quality}` ✔ (jpg, png, webp, pdf, tif, …) | Flattens; CMYK is written as sRGB for web formats ✔ |
| Layer > Export As / Layers to Files | `doc_export_layers {dir}` ✔ | Top-level layers only, skips adjustments |
| Artboards to Files / PDF | `file.export.artboardsToFiles`, `artboardsToPdf` | Path-based: may be blocked like other path commands (not tested) |
| New layer / via copy / via cut | `layer.new.layer` ✔, `layer.new.layerViaCopy`, `layer.new.layerViaCut` | `fillNeutral:true` + `mode:"Overlay"` = dodge & burn layer ✔ |
| Layer opacity, fill, blend, lock | `layer.setProps` | |
| Group / Merge / Stamp visible / Flatten | `layer.groupLayers`, `layer.mergeLayers`, `layer.stampVisible`, `layer.flattenImage` | |
| Adjustment layers (Curves, Levels, Hue/Sat, Color Balance, B&W, Vibrance, Exposure, Photo Filter, Channel Mixer, Selective Color, Gradient Map, Color Lookup, Posterize, Threshold, Invert) | `layer.newAdjustmentLayer.<kind>` ✔ (curves, levels, hueSaturation); edit with `layer.setAdjustment` | Levels/Curves accept `eyedropper` black/gray/white point |
| "Color and Vibrance" adjustment | `layer.newAdjustmentLayer.vibrance` (+ colorBalance / photoFilter for temperature) | No single combined panel |
| Adjustments panel presets | ⧗ | Build the stack by hand |
| Adjustment Brush | ⧗ → selection or painted mask + adjustment layer | |
| Auto Tone / Contrast / Color | `image.autoTone`, `image.autoContrast`, `image.autoColor` | Destructive: run on a copy layer |
| Shadows/Highlights, Match Color, Replace Color, HDR Toning | `image.adjustments.*` | Destructive (no adjustment-layer form) |
| Layer styles | `layer.layerStyle.dropShadow` ✔, `.stroke`, `.innerShadow`, `.satin`, `.gradientOverlay`, … ; copy/paste with `copyLayerStyle`/`pasteLayerStyle` | |
| Clipping mask | `layer.createClippingMask` ✔ | |
| Layer mask from selection / hide all / apply | `layer.layerMask.revealSelection`, `hideAll`, `fromTransparency`, `apply`; paint with `paint.stroke {target:"mask"}` ✔ | Black hides, white shows |
| Vector mask | `layer.vectorMask.add`, `fromPath` | |
| Select Subject / Object Selection / Sky | `select.subject` ✔, `select.object {rect|point}`, `select.sky` ✔ | |
| Remove Background | `layer.removeBackground` | Pixel layers only: fails on a Smart Object ✔ |
| Quick Selection, Magic Wand, Color Range, Focus Area | `select.quick`, `select.magicWand`, `select.colorRange` ✔, `select.focusArea` | |
| Marquee, Lasso, Magnetic Lasso | `select.rect` ✔ (`ellipse:true`, `feather`), `select.lasso`, `select.magneticLasso` | |
| Select and Mask / Refine Edge Brush | `select.refineEdge {radius, smartRadius, smooth, contrast, shiftEdge, decontaminate, output, refineStrokes}` | Output `newLayerWithMask` mirrors the book's recipe |
| Select People | ⧗ → `select.subject` / `select.object` + `select.colorRange {select:"skinTones"}` | |
| Modify (border, smooth, expand, contract, feather), Grow, Similar, Inverse, Transform Selection | `select.modify.*`, `select.grow`, `select.similar`, `select.inverse`, `select.transformSelection` | |
| Save / load selection (alpha channel), Quick Mask | `select.saveSelection`, `select.loadSelection`, `select.editInQuickMaskMode` | |
| Remove tool / Spot Healing / Healing / Patch / Clone / Content-Aware Move | `paint.remove` ✔ (`newLayer:true`), `paint.spotHealing` ✔, `paint.healingBrush`, `paint.patch`, `paint.cloneStamp`, `paint.contentAwareMove` | Remove is a background job |
| Find Distractions (wires, people) | ⧗ | Stroke `paint.remove` over them |
| Content-Aware Fill | `edit.contentAwareFill {output:"new"}` ✔ | Needs a selection |
| Crop / Straighten / Content-Aware crop fill | `image.crop {angle, deleteCroppedPixels:false, contentAware:true}` ✔ | Generative Expand ⧗ |
| Perspective Crop | `image.perspectiveCrop` | |
| Image Size / Canvas Size | `image.imageSize {resample}` ✔, `image.canvasSize` | |
| Free Transform / Warp / Puppet / Perspective Warp | `edit.transform` ✔ (`quad` for corner-pin), `edit.transform.warp`, `edit.puppetWarp`, `edit.perspectiveWarp` | Smart-object variants become smart filters |
| Liquify (manual tools) | `filter.liquify {strokes:[{tool:"bloat"|"pucker"|"forwardWarp"…}]}` ✔ | Face-Aware sliders ⧗ |
| Blur Gallery | `filter.blurGallery.tiltShift`, `irisBlur`, `fieldBlur`, `spinBlur`, `pathBlur` | |
| Lens Correction / Adaptive Wide Angle | `filter.lensCorrection`, `filter.adaptiveWideAngle` | |
| Smart Objects, Smart Filters | `layer.smartObjects.convertToSmartObject` ✔, `filter.convertForSmartFilters`; any filter on an SO becomes a Smart Filter ✔; edit with `layer.smartFilter.setParams` | |
| Replace Contents (mockups) | `doc_replace_smart_object {layer, path}` ✔ | Keeps transform and filters ✔ |
| Camera Raw Filter | `filter.cameraRaw` ✔ (as smart filter on an SO) | Same sliders as ACR Basic/Effects/Grading |
| Red Eye | `paint.redEye {x,y,pupilSize,darken}` | |
| Photomerge, Auto-Align, Auto-Blend (focus stack) | `file.automate.photomerge`, `edit.autoAlignLayers`, `edit.autoBlendLayers {method:"stack"}` | Use `useOpenDocuments:true`; path lists likely blocked |
| Merge to HDR Pro | `file.automate.mergeToHdrPro` / LC `merge.hdr` | |
| Type (point, paragraph, warp, on path, styles) | `type.create` ✔ (`box` = paragraph), `type.setStyle`, `type.warpText` ✔, `type.attachToPath`, `type.paragraphStyle.*`, `type.characterStyle.*` | Match Font ⧗ |
| Pen / paths / shapes / custom shapes | `path.set`, `path.toSelection`, `select.toWorkPath`, `shape.create` ✔, `shape.presets.place`, `edit.defineCustomShape` | Curvature Pen gesture ⧗ (give knots) |
| Patterns, Pattern Fill layer | `edit.definePattern`, `layer.newFillLayer.pattern` | Pattern Preview ⧗ |
| Gradients / fill layers | `gradient.fill.create`, `layer.newFillLayer.gradient`, `layer.newFillLayer.solidColor` | |
| Brush, Mixer Brush, brush presets, symmetry | `paint.stroke`, `paint.mixerBrush` ✔, `brush.presets.*`, `brush.presets.importAbr`, `paint.setSymmetry` | |
| History panel / snapshots / History Brush | `history.selectState`, `history.newSnapshot`, `paint.historyBrush` | |
| Actions / Batch | `actions.record` ✔ / `actions.stop` ✔ / `actions.play`, `file.automate.batch {steps, input, output}` | Remember to delete test actions (they persist) |
| Frame tool | `layer.new.frame` ✔ | Group clipped to a shape |
| Artboards | `layer.new.artboard {preset}` ✔, `layer.artboard.set` | |
| Layer Comps | `layerComp.new` ✔, `layerComp.apply` | |
| Variables / data sets (batch templates) | `image.variables.define`, `doc_import_data_sets`, `image.applyDataSet` | |
| Video timeline | `timeline.create` ✔, `layer.videoLayers.*` ✔, `file.export.renderVideo {dir}` ✔ = PNG frame sequence | Keyframes, audio, transitions, H.264 ⧗ → FilmCraft/EffectCraft |
| Frame animation / tween / GIF | ⧗ | |
| Color Settings, Assign/Convert to Profile | `edit.colorSettings`, `edit.assignProfile`, `edit.convertToProfile` ✔ (`srgb`, `display-p3`, `coated-cmyk`, …) | |
| Proof Colors / Gamut Warning / color samplers | `view.proofSetup`, `view.proofColors` ✔, `view.gamutWarning` ✔ (returns out-of-gamut fraction), `view.colorSamplers.*` | |
| Image > Mode (RGB/CMYK/Lab, 8/16/32 bit) | `image.mode.*` | |
| Print / Photoshop PDF / PDF/X | `file.print`; `doc_export` to `.pdf` ✔ = flattened raster PDF | PDF/X presets ⧗ |
| Generative Fill / Expand / Generate Image / Upscale / Harmonize / Neural Filters / Sky Replacement | ⧗ | Non-generative fallbacks in `references/generative-ai.md` |
| Bridge, Libraries, Cloud Documents, Adobe Stock | ⧗ | Files inside the server's allowed read/write root + LightCraft library |
| ACR profile, WB, Light, Color, Effects, Detail | LC `develop.profile`, `develop.wb`, `develop.wbPick`, `develop.set {values}`, `develop.auto` | Slider ids from `list_controls` (`light.exposure`, `effects.clarity`, …) |
| ACR masks (brush, linear, radial, subject, sky, people/object) | LC `mask.add {kind}`, `mask.addComponent`, `mask.adjust` | AI kinds need the SAM 3 model |
| ACR Remove / heal | LC `spot.add {mode}`, `spot.findDust`, `spot.findBlemishes` | |
| ACR Sync Settings / copy-paste | LC `develop.copy`, `develop.paste`, `develop.sync`, `develop.autoSync`, `develop.matchExposure` | |
| ACR Save Images (JPEG, resize, sRGB) | LC `app.export {format, longEdge, colorSpace, sharpen, metadata}` | |

## 2b. Not available as of 2026-11-03 (snapshot — re-check)

Adobe target → interim workaround. Run `command_list {filter}` with the keyword in brackets before relying on
the workaround.
- Generative Fill / Expand / Generate Image / Upscale (`generat`, `upscale`) → content-aware fill or crop,
  `image.imageSize {resample:"preserveDetails"}`; external generation + `doc_place`.
- Harmonize, Neural Filters, Sky Replacement (`harmon`, `neural`, `sky`) → clipped adjustments, LUT,
  `select.sky` + masked new sky.
- Adjustment Brush, Adjustments-panel presets, Select People, Find Distractions, Face-Aware Liquify sliders,
  Match Font (`adjustment`, `people`, `distract`, `face`, `font`) → selection/mask + adjustment layer,
  subject/object/skin-tone selections, manual `paint.remove` strokes, manual Liquify strokes, manual font ID.
- Pattern Preview, Curvature Pen gestures (`pattern`, `curvature`) → `filter.other.offset` wrap test, knots
  via `path.set`.
- Video keyframes, audio, transitions, frame animation/tween, GIF, H.264 (`keyframe`, `audio`, `tween`,
  `gif`) → EffectCraft/FilmCraft.
- PDF/X presets, Content Credentials, Bridge/Libraries/Cloud docs/Stock → DesignCraft for press PDF, files
  inside the allowed read/write root.
- Path-taking engine commands blocked in automation (`saveACopy`, `exportAs`, `saveForWebLegacy`,
  `placeEmbedded`) → `doc_*` tools; re-test, the sandbox may change.

## 3. Recipes (details in `references/`)

**Basic correction** (photo-corrections.md): curves layer with white/gray eyedropper on a true white and a
true neutral → gentle S → vibrance +10…+20 → `paint.remove` on a new layer → crop at target ratio and ppi →
convert to SO + `filter.sharpen.smartSharpen` last. Raw? same order in LightCraft: profile, `develop.wbPick`
on a lit neutral, Light sliders, vibrance, clarity, detail.

**Retouching** (quick-fixes.md, camera-raw.md): blemishes with `paint.spotHealing` on an empty layer
(`sampleAllLayers:true`); red eye `paint.redEye`; skin with a low-texture LightCraft mask or a frequency-split
style softening on a masked SO; dodge & burn on a 50 % grey Overlay layer; keep moles and identity marks.

**Selection and cut-out** (selections.md, masks-and-patterns.md): `select.subject` (or `select.object` for one
of many) → `select.refineEdge {smartRadius:true, radius:≈8–20, shiftEdge:-10…-15, decontaminate:true,
output:"newLayerWithMask"}` → inspect the mask at 200–400 % → touch up with `paint.stroke {target:"mask"}`.
Sky: `select.sky` then Layer via Copy or adjustment through the selection.

**Compositing** (advanced-compositing.md): place each element as an SO (`doc_place`), scale with
`edit.transform`, match tone with clipped Curves/Hue-Sat, recolour with a Color-mode paint layer, add contact
shadows on Multiply layers, unify with a top Color Lookup / gradient map, grain last.

**Mockup / smart-object swap** (advanced-compositing.md, web-export.md): place a placeholder SO, corner-pin it
with `edit.transform {quad}`, Multiply or a clipped texture for realism, then for each design
`doc_replace_smart_object` ✔ + `doc_export`. For batches use variables/data sets.

**Text** (typography.md): `type.create` point text for headlines, `box` for paragraphs; tracking/leading in
`type.setStyle`; image inside type = type layer + SO above + `layer.createClippingMask`; warp with
`type.warpText`; keep type live until the final export.

**Export for web/social/print** (web-export.md, consistent-color.md): web/social → sRGB, JPEG q≈80 or WebP,
exact pixel size (e.g. 1080×1350 IG portrait), sharpen after resizing; print → ≈300 ppi at final size,
bleed if required, soft-proof with the printer's CMYK profile, convert a *copy*, ask the printer for specs.

**Consistent colour across photos** (consistent-color.md, camera-raw.md): develop one hero image in LightCraft,
`develop.copy` / `develop.sync` (or `autoSync`) to the set, `develop.matchExposure`, then fine-tune each; in
PhotoCraft reuse the same adjustment stack (copy layers between documents or record an action) and check
neutrals with color samplers.

## 4. Common mistakes and pre-delivery checks

- Painting or healing directly on Background; flattening the master; forgetting that a merged/flattened
  stack is irreversible.
- Adjustment layer inserted above the *active* layer (not the top) ✔: select the right layer first, or clip.
- A live selection silently becomes the mask of the next adjustment ✔: `select.deselect` when not intended.
- Adding a filter to a plain layer (destructive) instead of an SO; converting a masked layer to SO hides the
  mask inside it.
- Over-saturation/over-clarity (halos), crushed blacks or clipped whites: check samplers and histogram.
- Sharpening before resizing; exporting web files without sRGB; sending CMYK to a desktop printer.
- Moving a subject without its shadow; mismatched light direction or grain between composited parts.
- Typos and missing fonts: run `type.info` / `edit.checkSpelling`; respect platform safe areas (e.g. keep the
  Instagram carousel's top-right corner free of key content).
- **Before delivery**: `doc_inspect` (no hidden stray layers, names clean), `render_preview` full and at 100 %,
  exact pixel size and colour profile, file size, PDF/print specs, save layered master + flattened export,
  then deliver both wherever the user keeps project files.

## 5. References

`references/`: `workspace.md` (L1), `photo-corrections.md` (L2), `selections.md` (L3), `layers.md` (L4),
`quick-fixes.md` (L5), `masks-and-patterns.md` (L6), `typography.md` (L7), `vector-drawing.md` (L8),
`advanced-compositing.md` (L9), `mixer-brush.md` (L10), `video.md` (L11), `camera-raw.md` (L12),
`web-export.md` (L13), `consistent-color.md` (L14), `generative-ai.md` (L15). Load only the file the task
needs.

## 6. Keeping this skill current

When `command_list` shows that a ⧗ feature has shipped, an id or param changed, or a LightCraft entry
behaves differently from what is written here, update this skill (mapping table, section 2b and the matching
reference file, with the new date) or open an issue on the repository.
