# Basic photo corrections (Lesson 2)

Source: synthesis of *Photoshop Classroom in a Book 2026*, Lesson 2, mapped to PhotoCraft/LightCraft.

## Order of work (general → specific)
1. Tone (contrast, black/white points). Fix contrast before saturation: contrast changes saturation.
2. Colour: neutrals must be neutral (remove casts).
3. Remove distractions (wires, passers-by, dust).
4. Creative colour / grading.
5. Crop and composition for the target ratio and resolution.
6. Sharpening last, at final size.
Raw files: do steps 1–2 (and sharpening/noise) in LightCraft before PhotoCraft.

## Key concepts
- **Curves**: steeper = more contrast; an S-curve adds midtone contrast. Endpoints at the histogram edges;
  pushing past them clips to pure black/white. Few points = easier control.
- **White/gray/black point eyedroppers**: white on the brightest real white (clouds, a white sign),
  gray on something that must be neutral grey, black for shadow casts. Usually better than Auto.
- **Vibrance** boosts muted colours more and protects skin; can be pushed further than Saturation.
- **Resolution**: screen = pixel dimensions; print = pixel density. 240–360 ppi at final size counts as high
  resolution (≈300 typical). ppi = pixels ÷ inches (2100 px on 7 in = 300 ppi).
- File size changes only when the pixel count changes (resampling).
- Filters affect the selected layer only: to filter a multi-layer stack, convert the layers to one Smart
  Object instead of flattening; the filter becomes an editable Smart Filter.

## PhotoCraft recipe
```
layer.newAdjustmentLayer.curves {eyedropper:{point:"white", at:[x,y]}}      # true white
layer.setAdjustment {layer:<curves>, eyedropper:{point:"gray", at:[x,y]}}   # true neutral
layer.setAdjustment {layer:<curves>, points:[[0,0],[64,56],[192,204],[255,255]]}  # gentle S
layer.newAdjustmentLayer.vibrance {vibrance:15, saturation:10}
layer.new.layer {name:"Cleanup"} ; paint.remove {points:[…], size:45, sampleAllLayers:true}
image.crop {x,y,width,height, deleteCroppedPixels:false, targetWidth:3300, targetHeight:2550, resolution:300}
select.allLayers ; layer.smartObjects.convertToSmartObject
filter.sharpen.smartSharpen {amount:220, radius:1, reduceNoise:10}
```
Verified: curves/levels/hue-sat layers ✔, `paint.remove` ✔, `image.crop` ✔, SO + filter ✔.
`layer.newAdjustmentLayer.vibrance {vibrance, saturation}` and `filter.sharpen.smartSharpen {amount 1..500, radius, reduceNoise}` params checked in `command_list`.

## LightCraft equivalent (raw or a set of photos)
`develop.profile` → `develop.wbPick {x,y}` on a lit neutral → `develop.set {values:{"light.exposure":…,
"light.highlights":-20,"light.shadows":+40,"light.whites":…,"light.blacks":…}}` → `color.vibrance` +15 →
`develop.curve {channel:"master", points}` → `spot.add {mode:"heal"}` for dust → `crop` → detail sharpening
(`detail.sharpenAmount`, `detail.sharpenMasking`) → `export`.

## Removing distractions
- Photoshop's Remove tool with "Find Distractions" (wires, people) was not available in PhotoCraft as of
  2026-11-03 (re-check with `command_list {filter:"distract"}`); meanwhile stroke
  `paint.remove` over each object (`closeLoops:true` removes what a stroke encircles, `strokes:[…]` does
  several in one job, `newLayer:true` keeps the original intact).
- Traditional tools: `paint.spotHealing` (small spots), `paint.healingBrush`/`paint.cloneStamp` with
  `source`, `paint.patch`, `paint.contentAwareMove`; large areas: selection + `edit.contentAwareFill`.
- Brush a bit larger than the defect; check every result at 100 %; deal with the object's shadow too.
- Never remove people who are the subject; ask before removing anything identity-related.

## Creative colour
- Photo Filter warming (85) ≈30 % density, preserve luminosity: `layer.newAdjustmentLayer.photoFilter {filter:"warming85", density:30, preserveLuminosity:true}`.
- Look via LUT: `layer.newAdjustmentLayer.colorLookup {lut:"tealOrange"|"fadedFilm"|… or file}`.
- Creative B&W: `layer.newAdjustmentLayer.blackWhite` with per-colour sliders, optional tint; in LightCraft
  `develop.treatment {bw:true}` + `bw.*` sliders or `develop.autoBwMix`.

## Pitfalls
- Clipped areas (pure white/black blotches) = endpoints pushed too far.
- Over-saturation: stop before colours look unnatural; check skin.
- Crop tool remembers the last ratio; keep cropped pixels (`deleteCroppedPixels:false`) to recover later.
- Sharpen after resampling to final size; higher radius for coarse detail, lower for fine; for print,
  judge on a test print.
- Auto Tone/Contrast/Color in PhotoCraft are destructive image commands: apply to a duplicate layer.
