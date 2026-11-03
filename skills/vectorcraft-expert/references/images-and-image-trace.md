# Placed images, masks and Image Trace (Lesson 15, Image Trace from Lesson 3)

Own-words summary of Classroom in a Book 2026, "Placing and Working with Images" and "Using Image Trace".

## Placing
- `file.place {path, link:true|false, rect:[x,y,w,h] | at:[x,y], template, replace, page, crop}` → ids (verified: a PNG fitted into a 150×150 rect, embedded with `link:false`).
- Linked vs embedded (book): a **linked** file stays outside, keeps the document light, but must travel with it; an **embedded** file lives inside the document, cannot break, makes it heavier. Pasted images are always embedded.
- Inspect before placing: `file.place.info` (size, ppi, colour mode). Many files: `file.place.queue`.
- Photoshop files keep layers when placed as PSD (check `file.place.info` warnings).
- Effective resolution: for print aim at ≥ 300 ppi at final size; never upscale a small photo for a poster.

## Transforming and cropping
- Scale/rotate like any object (`object.scale`, `object.setBounds`).
- Crop: `object.cropImage` (destructive, removes hidden pixels → smaller file); quick mask: `object.maskImage`.

## Masks
- Clipping mask with a shape or text on top: `object.clippingMask.make {ids}`; colour of the mask shape does not matter (paint is removed). Edit: `editContents` / `editMask`; release.
- Text as mask: photo inside a big headline — outline or keep live text; both work.
- **Opacity mask** (soft fades): put a gradient-filled shape (white = visible, black = hidden) above the art, then `transparency.makeOpacityMask`; options `transparency.setOpacityMask` (clip, invert), `releaseOpacityMask`, `disable` / `enable`, `unlinkOpacityMask` to move image and mask separately, `editOpacityMask`.

## Links
- `links.list`, `links.info`, `links.check`, `links.update` / `updateChanged`, `links.relink {ids, path, preserve:"bounds"}` (swap a photo keeping its frame), `links.embed` / `unembed`, `links.findFiles`, `links.placementOptions`, `links.goTo`.
- Before delivery: `links.check` — no missing links; then `file.package` gathers them.

## Image Trace
- `imageTrace.make {id, preset, params}` or `imageTrace.makeAndExpand` (verified: colour mode, 6-colour limited palette → 22 paths, 928 anchors).
  - `params.mode`: blackAndWhite | grayscale | color | logo (flat logos: snaps edges, lines and circles; up to 10 colours via `logoColors`).
  - `palette`: limited (`colors` N) | fullTone | automatic | documentLibrary (trace with the document's swatches — keeps brand colours).
  - `paths` / `corners` / `noise` sliders (fidelity vs simplicity), `ignoreWhite`, `method: abutting|overlapping`, `strokes` for line art, `shapes` to snap circles/rectangles, `gradients`.
  - Presets: `imageTrace.presets`; views: `imageTrace.setView`; `imageTrace.release` / `expand`.
- After expanding: ungroup, delete background pieces (`select.same.fillColor` + delete), `object.path.simplify`, merge same-colour neighbours with `pathfinder` merge.
- Book advice: start from the cleanest, highest-contrast image; trace sketches in black and white, then colour with Live Paint.

## Common mistakes
- Shipping a linked file without its images (use `file.package`).
- Tracing a low-res JPEG and accepting thousands of anchors: raise noise, lower paths, simplify.
- Low effective ppi in print files.
