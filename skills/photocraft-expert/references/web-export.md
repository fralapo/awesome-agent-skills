# Preparing files for the web and social (Lesson 13)

Source: synthesis of *Photoshop Classroom in a Book 2026*, Lesson 13, mapped to PhotoCraft.

## Concepts
- Frame = vector placeholder that reserves space for a future image (a group clipped to a shape).
- Linked vs embedded placing (only embedded via `doc_place` in automation).
- Layer groups behave as units; a style on a group applies to all its content.
- Actions record command sequences for replay on many files (no zoom/scroll, no timing). Batch runs them on
  folders.
- Image Size resamples; Canvas Size adds/removes area.
- Artboards: several canvases (desktop, mobile) in one document for consistent variants.
- Export As beats legacy Save for Web: artboards, layers and 1x/2x/3x scales.

## PhotoCraft calls
| Task | Call |
|---|---|
| Frame placeholder | `layer.new.frame {x,y,width,height,shape, layer?}` ✔; put content in with `doc_place` then move it into the frame group |
| Button = group of band + label | `shape.create {kind:"rect", rect:[x,y,180,33], fill:"#194879"}` + `type.create` → `layer.groupLayers`; style on the group |
| Duplicate groups | `layer.duplicate`, then `layer.translate {dx,dy}` |
| Copy styles | `layer.layerStyle.copyLayerStyle` / `pasteLayerStyle` |
| Record an action | `actions.record {name}` ✔ → run steps → `actions.stop` ✔ → `actions.play {action}`; delete with `actions.delete` ✔ |
| Batch | `file.automate.batch {steps:[[id,params]…], input:folder, output:folder, format}` (paths: may be blocked by the automation sandbox – otherwise loop `doc_open` → `command_batch` → `doc_export`) |
| Resize / canvas | `image.imageSize {width:180, resample:"bicubicSharper"}` ✔, `image.canvasSize {width:220,height:220,anchor:"center"}` |
| Artboards | `layer.new.artboard {preset:"Web 1920"|"iPhone 14"|…, name}` ✔ (presets in the param doc), `layer.new.artboardFromLayers`, `layer.artboard.set`, `layer.artboard.addBeside` |
| Export whole design | `doc_export {path:"x.jpg"|"x.png"|"x.webp", quality}` ✔ |
| Export each element | `doc_export_layers {dir, format}` ✔ (top-level layers; groups merged; adjustments skipped) |
| Artboards to files | `file.export.artboardsToFiles {dir, format}` (path-based, possibly blocked); fallback: crop a duplicate to each artboard rect and `doc_export` |
| 2x/3x assets | make a resized duplicate (`image.duplicate` + `image.imageSize {percent:200}`) and export with `@2x` suffix; `layer.exportAs {scale}` is blocked in automation ✔ |
| Slices | `slice.*` (legacy) |

## Social/web export checklist
- Exact pixel size per platform (e.g. IG feed 1080×1350 portrait, 1080×1080 square; stories/reels
  1080×1920; LinkedIn/OG 1200×627; web hero 1920 wide + 2x if HiDPI).
- Colour: sRGB. `edit.convertToProfile {profile:"srgb"}` on a duplicate if the master is P3/Adobe RGB/CMYK
  (`doc_export` writes CMYK as sRGB for web formats ✔ but convert explicitly for control).
- Format: JPEG q 70–85 photos; PNG for flat graphics/transparency; WebP for web (lossy with `quality`,
  lossless without ✔).
- Sharpen after resizing, preview at 100 % (`render_preview {max_side:0}`).
- Weight under platform/site limits; metadata copyright only.
- Respect each platform's safe areas (UI overlays such as the Instagram carousel counter in the top-right
  corner); keep key text and logos out of them.
- Background colours that belong in code (web) should not be baked into exported assets.

## Pitfalls
- Resize artboards with artboard commands, not Image/Canvas Size.
- JPEG warns because transparency/effects are flattened: keep the layered master.
- Batch errors: stop, fix the action, re-run; test the action on one file first.
- New layers placed while a group is selected may land outside it: check `doc_inspect`.
