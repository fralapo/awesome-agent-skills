# Rotoscoping with the Roto Brush (lesson 9)

## Concepts
- Rotoscoping means separating a foreground subject from its background over time. The Roto Brush does it from strokes:
  - foreground strokes mark the subject;
  - background strokes remove regions.
- The **segmentation boundary** is the edge between foreground and background. It is propagated frame by frame within the **span**, starting from the frames you stroked.
- **Refine Edge** handles hair and fur with partial transparency. Use it only after the base boundary is good over the whole clip.
- **Freeze** caches the result so it does not recompute, and locks it.

## EffectCraft commands (verified on synthetic footage)
- Models: `roto.models`.
  - The built-in `classical` model (graph cut + optical flow) is always available.
  - MobileSAM-type models can be installed with `roto.model.download`/`install`/`select`.
- Stroke: `roto.stroke {layer, kind: fg|bg|refine|refineErase, points:[[x,y]…] (layer px), frame?, radius?}`. It creates the Roto Brush effect and a span.
- Then:
  - `roto.propagate {layer}`, which runs in the background;
  - `roto.status`, to check progress;
  - `roto.span`, to change the span;
  - `roto.freeze` / `roto.unfreeze`, to lock or release the result.
- Object matte (alternative, model-based tracking): `objectMatte.apply` / `objectMatte.propagate` / `objectMatte.freeze`.
- Refine the matte with the effects `Refine Soft Matte`, `Refine Hard Matte`, `Matte Choker` and `Simple Choker`.

## Workflow
1. Open the footage layer and go to a frame where the subject is clear.
2. Make one generous foreground stroke inside the subject, then background strokes where it bleeds.
3. Propagate. Inspect frames across the span with `render_frame {time, transparent:true}`.
4. Where the boundary drifts, add corrective strokes on that frame and propagate again.
5. Refine edges, freeze, then put a new background under the layer or the text behind the subject.

## Text behind the subject (the book's final shot)
Duplicate the rotoscoped layer above the text, so the stack is subject → text → original footage. Then animate the text.

## Gotchas
- `jobs.wait` returned immediately in headless mode. Poll `roto.status` until `running:false` before rendering.
- Strokes are in **layer pixels**, not comp pixels, when the layer is scaled.
