# 11 - Transparency and effects (lesson 12)

Snapshot of DesignCraft on 2026-11-03: the apps update daily, so re-check absent features with `list_commands {filter}` before using a workaround; the Adobe behaviour described here is the target.

Source: synthesis of *InDesign Classroom in a Book 2026*, lesson 12. ✔ = verified 2026-11-03.

## Concepts
- Opacity and blend modes (Multiply, Screen, Overlay…) change how an object combines with what is
  *below it in the stacking order*: rearranging objects changes the result.
- Levels: effects can target the whole object, or only its stroke, fill, or text.
- Effects: drop/inner shadow, outer/inner glow, bevel and emboss, satin, basic/directional/gradient
  feather. Copy an effect to another object (drag the fx icon) or store it in an object style.
- Text effects apply to the whole frame; to affect only some words, put them in their own frame.
- Shadows should sit tucked under the object; a shadow floating far away draws attention. A multiply
  shadow over white paper prints in black only.
- **Tint vs transparency**: if nothing below should show through (object on white), use a tint - it is
  simpler and prints predictably.
- Clear effects vs clear all transparency (also resets opacity and blending).
- Transparency is flattened for some outputs; check which pages contain it.

## DesignCraft
| Task | Command |
|---|---|
| Opacity + blend | `object.opacity {opacity:0.8, blend:"multiply", ids}` ✔ |
| Drop shadow | `object.dropShadow {on, distance, angle, size, opacity, color, mode}` ✔ |
| All effects in one step | `object.effects {effects:{dropShadow, innerShadow, outerGlow, innerGlow, bevel, satin, feather, directionalFeather, gradientFeather}, opacity, blend}` |
| Single effects | `object.innerShadow`, `object.outerGlow`, `object.innerGlow`, `object.bevel`, `object.satin`, `object.feather {width}`, `object.directionalFeather`, `object.gradientFeather` |
| Global light | `object.globalLight` |
| Isolate / knockout | `object.transparencyGroup {isolate, knockout}` |
| Blend space | `edit.transparencyBlendSpace` (CMYK for print) |
| Reuse | `style.object.create {fromSelection:true}` → `style.object.apply` |
| Copy look | `object.matchAttributes` (eyedropper) |
| Per-level (stroke/fill/text only) | not exposed as a separate parameter as of 2026-11-03 (re-check) - assume whole object |

## Export consequences ✔
- PDF/X-4 and interactive PDF: soft effects are exported as images (warning "objects with soft effects
  exported as images").
- PDF/X-1a: transparency flattened, regions rasterised at the `flatten` resolution (default 300 ppi).
  Prefer X-4 unless the printer asks for X-1a.
