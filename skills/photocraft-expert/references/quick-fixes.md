# Quick fixes (Lesson 5)

Source: synthesis of *Photoshop Classroom in a Book 2026*, Lesson 5, mapped to PhotoCraft/LightCraft.
⧗ = not available in PhotoCraft/LightCraft as of 2026-11-03 (snapshot — re-check with `command_list {filter}`
on the live app; ArtCraft apps update daily). The Photoshop behaviour described stays the target.


## Fixes and their PhotoCraft calls
| Fix | Photoshop | PhotoCraft / LightCraft |
|---|---|---|
| Red eye | Red Eye tool, pupil ≈23 %, darken ≈62 % | `paint.redEye {points:[[x,y],…], pupilSize:23, darken:62}`; LC `redeye.add` |
| Face reshaping | Face-Aware Liquify sliders (eyes, mouth, jaw) | ⧗ sliders. Use `filter.liquify {strokes:[{tool:"forwardWarp"|"bloat"|"pucker", size, pressure, points}]}` on an SO ✔ – subtle only |
| Motion blur behind a car | mask the subject, Path Blur on an SO background | `layer.new.layerViaCopy` + mask the subject (`select.object` → `layer.layerMask.revealSelection`); on the background SO `filter.blurGallery.pathBlur` (or `filter.blur.motionBlur`) |
| Spinning wheels | Spin Blur per wheel | `filter.blurGallery.spinBlur` on a masked wheel layer converted to SO |
| Miniature / focus effects | Tilt-Shift, Iris, Field | `filter.blurGallery.tiltShift {blur, centerY, angle, focus, transition}`, `.irisBlur`, `.fieldBlur` |
| Panorama | Photomerge, Perspective/Auto, blend, vignette removal, geometric correction, content-aware fill | `file.automate.photomerge {useOpenDocuments:true, layout, blend, vignetteRemoval, geometricCorrection, contentAwareFill}`; LC `merge.panorama` |
| Brighten / neutralise | Levels white-point eyedropper on a near-white cloud | `layer.newAdjustmentLayer.levels {eyedropper:{point:"white", at:[x,y]}}` |
| Straighten + fill corners | Crop Straighten + Generative Expand | `image.crop {angle, contentAware:true}` ✔ (content-aware, not generative) |
| Lens distortion, CA, vignetting | Filter > Lens Correction (auto profile from metadata) | `filter.lensCorrection {profile:"auto", correctDistortion, correctCA, correctVignette, autoScale, edge}`; LC `optics.*` sliders, `geometry.upright` |
| Extended depth of field | load files as layers, Auto-Blend Layers > Stack | open each shot, combine into one doc (`layer.copyToDocument`), `edit.autoAlignLayers {projection:"reposition"}` if hand-held, then `edit.autoBlendLayers {method:"stack", seamlessTones:true}` |
| Perspective of an object | Perspective Warp: Layout quads, then Warp | `edit.perspectiveWarp {planes:[{src:[4 corners], dst:[4 corners]}], straighten:"auto"}` (on an SO it becomes a smart filter) |
| Duplicate/extend an element | Content-Aware Move (Extend) | `paint.contentAwareMove` |
| Sky replacement | Edit > Sky Replacement | ⧗ → `select.sky` + new sky placed as SO with the sky selection as mask, then match colour with clipped adjustments |

## Good practice
- Apply filters as Smart Filters (`filter.convertForSmartFilters` / convert to SO first) so they stay editable
  (`layer.smartFilter.setParams`).
- Converting a masked layer to SO hides the mask inside: convert first, then mask.
- After any big effect re-check the whole frame (e.g. the driver vanished behind the blur mask).
- Panoramas: 15–40 % overlap, constant focal length and exposure, level horizon; try another layout if odd.
- If the white eyedropper does nothing, the sampled pixel was already pure white.
- Lens profiles work only with correct camera/lens metadata.
- Focus stacking is best on a tripod; align hand-held frames first.
- Perspective Warp quads must wrap the subject like a container.
- When generative AI is not allowed, use the content-aware tools; as of 2026-11-03 they were also the only option in PhotoCraft (re-check).
