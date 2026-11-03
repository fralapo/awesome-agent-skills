---
name: effectcraft-expert
description: "Operational After Effects know-how for driving EffectCraft (the ArtCraft After Effects-class motion graphics compositor) over MCP (mcp__effectcraft__* tools: command_list, command_run, command_batch, add_keyframe, add_effect, set_property, render_frame, render_preview). Use whenever the work involves EffectCraft or any motion graphics request: animated text or titles, animated logos, kinetic typography, animated reels/stories/shorts/TikToks, animated slideshows or presentations, shape-layer animation, keyframes and easing, expressions, parenting/nulls, precomps, masks, track mattes, rotoscoping/Roto Brush, puppet pins, motion or camera tracking, stabilization, color grading/Lumetri, 3D layers/cameras/lights, motion graphics templates (Essential Graphics), Lottie, or rendering/exporting video for social (9:16, 1:1, 4:5, 16:9). Keywords - after effects, effectcraft, artcraft, motion graphics, compositing, keyframe, easy ease, expression, wiggle, precompose, track matte, mask, roto brush, puppet, motion tracking, warp stabilizer, 3d camera, lumetri, render queue, h.264, prores, lottie."
version: 1.0.0
source: "Workflow informed by Adobe After Effects Classroom in a Book 2026 Release (Adobe Press); EffectCraft mappings verified against the live command catalogue on 2026-11-03."
---

# EffectCraft expert (After Effects workflow over MCP)

This skill turns the standard After Effects workflow into concrete EffectCraft calls. It assumes EffectCraft is connected over MCP to Claude Code or any SKILL.md-compatible agent, so the `mcp__effectcraft__*` tools are available. Every mapping below is tied to a **verified** EffectCraft command id.

For *what* to cut and *why* (hooks, pacing, retention, caption style), pair it with the [`video-editor`](../video-editor/SKILL.md) skill; this one covers the *how* inside EffectCraft.

**Sources.** The workflow is informed by Adobe's *After Effects Classroom in a Book 2026 Release* (Adobe Press) and verified against EffectCraft's live command catalogue on 2026-11-03. This skill is written independently and reproduces no text from the book.

## 0. The app changes every day — re-check before saying "missing"

ArtCraft apps get updates almost daily. Every "absent" or "missing" item in this skill and in `references/` is a **snapshot as of 2026-11-03**, not a permanent limit.
- Before you tell the user that a feature is missing, or fall back to a workaround, search the live catalogue with a filter (`command_list` / `list_effects` / `effects.list`). If the command exists now, use it.
- The Adobe method described here is the **target**. Apply it in full as soon as the app supports it.
- If you find a command that this skill lists as absent, or a mapping that has changed, update this skill (or open an issue on the repository) so the snapshot stays accurate.

## 1. Core concepts
- **Project → compositions → layers → properties.** A composition has space (w×h) and time (fps, duration). Layers stack top to bottom. Every property has a **path**, for example:
  - `transform/position`, `transform/scale`, `transform/rotation`, `transform/opacity`, `transform/anchor`;
  - `effects/#1/blurriness`, `masks/<name>/feather`;
  - `text/sourceText`, `contents/trim/end`.
- **Keyframes** (`add_keyframe`) animate a property over time. **Interpolation** sets the temporal ease: linear, bezier, hold, easyEase, easyEaseIn, easyEaseOut. Never ship linear motion for graphics.
- **Expressions** (`set_property {expression}`) are JS code. Common ones: `wiggle(2,20)`, `time*90`, `loopOut()`, pick-whip references.
- **Anchor point** is the pivot for scale and rotation. **Parenting** (`layer.setParent`) passes position, rotation and scale (not opacity) from parent to child. **Nulls** are invisible controllers.
- **Precomp** (`layer.precompose`) nests layers into a sub-comp. Use it to group them, change render order, or apply one effect or animation to a whole group.
- **Adjustment layer** applies its effects to everything below it.
- **Track matte**: one layer is visible only through another layer's alpha or luma.
- **Motion blur** needs the layer switch **and** the comp switch.

## 2. Recommended flow (every job)
1. Check what is open with `doc_inspect`. Never `file.open`/`file.save` user files unless the user asks.
2. `command_run comp.new {name, width, height, frameRate, duration, background}`. The new comp becomes **active**.
3. Create layers with `layer.newSolid` / `layer.newText` / `layer.newShape` / `layer.newNull` / `file.import` + `layer.addItem`. Each returns `{layer:id}`, so keep those ids.
4. Arrange (`layer.arrange`), parent, and precompose.
5. Animate with `add_keyframe {layer, path, keys:[…], interpolation:"easyEase"}`. For behaviours use presets (`anim.applyBuiltinPreset`, `layer.applyTextPreset`) or expressions.
6. Add effects with `add_effect {layer, effect, values}`. It returns the parameter paths for later keys.
7. **Verify** with `render_frame {time}` at several times (start, each transition, end). Use `get_comp` for structure and `get_layer {flat:true, time}` for values.
8. Render with `renderQueue.add` → `renderQueue.render {wait:true}`, then ffprobe the file.
9. Deliver the rendered file where the user asked for it. At the end of throwaway tests, run `file.newProject` to clear the session.

## 3. Mapping: After Effects → EffectCraft
Legend: ✔ verified with a live call on 2026-11-03 · ○ command exists, not tested · ✘ absent as of 2026-11-03 (re-check, see §0).

| After Effects feature | EffectCraft (tool / command id / effect) | |
|---|---|---|
| New composition, comp settings | `comp.new {…}`, `comp.settings` | ✔ |
| Import, comp from footage | `file.import {paths, newComp?, addToComp?, importAs?}` | ✔ (PSD/AI as comp ○) |
| Solid, text, shape, null, adjustment | `layer.newSolid/newText/newShape/newNull/newAdjustment` | ✔ (adj ○) |
| Transform properties (P S R T A) | `set_property {layer, path:"transform/…", value}` | ✔ |
| Keyframes, Easy Ease | `add_keyframe {keys, interpolation}`; `keys.easyEase`, `keys.setEase`, `keys.velocity` | ✔ / ○ |
| Hold keys, roving, reverse | `interpolation:"hold"`, `keys.toggleHold`, `keys.timeReverse` | ○ |
| Expressions, pick whip | `set_property {expression}`, `prop.pickWhip` | ✔ / ○ |
| Wiggler, Smoother, Motion Sketch | `keys.wiggle` (needs selected keys), `keys.smooth`, `motion.sketch` | ○ |
| Parenting | `layer.setParent {layers, parent}` | ✔ |
| Pre-compose | `layer.precompose {layers, name, mode}` → `{comp, layer}` | ✔ |
| Effects + Effect Controls | `add_effect`, `effect.apply`, `set_property effects/#n/…` | ✔ (Glow, Gradient Ramp, Hue/Sat, Lumetri) |
| Animation presets (Bridge browse) | `anim.builtinPresets` + `anim.applyBuiltinPreset`; `anim.savePreset/applyPreset`; Bridge ✘ | ✔ |
| Text presets | `layer.applyTextPreset {preset: typewriter…}` | ✔ |
| Text animators and selectors | `layer.addTextAnimator {properties}`, `layer.addTextSelector`, paths `text/animators/<n>/…` | ✔ |
| Character/Paragraph formatting | `layer.setText {font, size, tracking, leading, justify, range}`; fonts `text.fonts` | ○ |
| Adobe Fonts | ✘ (installed fonts only) | ✘ |
| Shape operators (Wiggle, Offset, Pucker, Trim, Repeater) | `layer.addShapeItem {kind}` | ✔ (wiggle, trim) |
| Pen tool shape | `shape.newPath {vertices, closed, fill, stroke}` | ○ |
| Nulls follow points | `paths.nullsFollowPoints`, `paths.pointsFollowNulls` | ○ |
| Align and distribute, snapping | `layer.align`, `layer.distribute`; snapping UI-only | ○ |
| Layer styles | `layer.style.add {style}` | ○ |
| Masks (shape, pen, feather, modes) | `layer.addMask`, `mask.new`, `layer.mask.set/mode/invert`, `mask.featherPoint.*` | ✔ (ellipse + feather) |
| Track matte | `layer.setTrackMatte {layer, matte, kind}` | ✔ |
| Corner Pin | `add_effect "Corner Pin"` / `CC Power Pin` | ○ |
| Time remap, stretch, freeze | `layer.enableTimeRemap`, `layer.timeStretch`, `layer.freezeFrame` | ✔ / ○ |
| Sequence layers | `layer.sequence`, `layer.quickOffset` | ○ |
| Puppet pins and recording | `puppet.addPin/movePin/setPin/recordPin/follow` | ✔ (addPin) |
| Roto Brush, Refine Edge, Freeze | `roto.stroke` → `roto.propagate` → `roto.freeze`; matte refine effects | ✔ (classical model) |
| Point tracker → null | `track.motion` → `track.setPoint` → `track.analyze` → `track.setTarget` → `track.apply` | ✔ |
| Mask tracking, face tracking | `track.mask {method}` | ○ |
| Warp Stabilizer | `track.warpStabilizer` | ○ |
| 3D Camera Tracker | `track.camera`, `camera.createFromSolve`, `camera.setGroundPlane` | ○ |
| Content-Aware Fill, clone | `layer.newContentAwareFill`, `paint.stroke {kind:"clone"}` | ○ |
| Scene Edit Detection | `layer.sceneEditDetection` | ○ |
| Color: Lumetri, Hue/Sat Colorize, Auto Contrast… | `add_effect "Lumetri Color"`, `"Hue/Saturation"` (`colorize`), etc. | ✔ (applied, paths read) |
| Particles, Timewarp, Rolling Shutter Repair | `CC Particle World`, `Timewarp`, `Rolling Shutter Repair` effects | ○ |
| 3D layer switch | `layer.setSwitch {switch:"threeD"}` | ✔ |
| Camera, lights | `layer.newCamera`, `layer.newLight` | ✔ |
| 3D primitives / models (Advanced 3D) | `layer.new3dPrimitive` ✔, `layer.newModel` ○ | |
| Essential Graphics → template | `essential.addProperty/addMedia/addGroup`, `comp.responsiveTime`, `essential.exportTemplate` (.ectemplate) | ✔ |
| .mogrt, CC Libraries, Premiere template use | ✘ (`.ectemplate` only; `file.exportTimeline` ○) | ✘ |
| Render Queue + templates | `renderQueue.add/render/saveTemplate/applyTemplate` | ✔ (H.264) |
| Adobe Media Encoder | ✘ → use the render queue (GIF via `format:"gif"`) | ✘ |
| Lottie export | `file.exportLottie` | ✔ |
| Render-time (snail) column | ✘ | ✘ |
| Character Animator, Frame.io/Team Projects | ✘ | ✘ |

## 4. Recipes (condensed; details in references)
**Animated text (title or kinetic type)**: `layer.newText` → `layer.centerAnchor` → keys on scale 0→110→100 (easyEase) or `layer.applyTextPreset` (fadeUpCharacters, trackingIn, typewriter) → for per-character control `layer.addTextAnimator` and key `…/rangeSelector/offset` −100→100 → motion blur (layer and comp). Ref `02-animated-text.md`.

**Animated logo**: vector logo as a shape (`edit.pasteSvg`, `shape.newPath` or an import) → precomp it → write-on with `addShapeItem trim` (key `contents/trim/end` 0→100) or a mask reveal → scale/rotation settle with overshoot → `Glow`/`Drop Shadow` → optional 3D camera push (`10-3d-camera-lights.md`). Leave 0.5–1 s of hold at the end.

**Shape-layer animation**: `layer.newShape` → operators (`wiggle`, `offset`, `pucker`, `repeater`, `trim`) → keys on operator params → parent the shapes to a null for global moves. Ref `03-shapes-keyframes-parenting.md`.

**Slideshow / animated presentation**: one precomp per slide (title + image + bullets) → `layer.sequence {overlap:true, transition:"crossDissolve"}` or `anim.applyBuiltinPreset` in/out per slide → background preset (`softGradientDrift`, `bokehDrift`) → audio with `layer.addItem` → stagger the elements with `layer.quickOffset`. Ref `03-…` (lesson 5) and `01-…`.

**Masks and rotoscoping**: static shape → `layer.addMask` / `mask.new` + feather. Moving subject → `roto.stroke fg/bg` → `roto.propagate` (poll `roto.status`) → `roto.freeze` → new background below, or text between two copies. Refs `05-masks.md`, `07-roto-brush.md`.

**Puppet**: `puppet.addPin` at the joints/extremities (Starch on rigid parts) → `puppet.movePin` keys or `puppet.recordPin` → `puppet.follow` for secondary motion. Ref `06-puppet.md`.

**Color grading**: adjustment layer on top → `Lumetri Color` (correct first: temperature/exposure/contrast; then `creative/look`, vibrance, vignette) → per-shot fixes on the footage layers → `Hue/Saturation colorize` for duotones. Ref `08-color-and-mood.md`.

**Motion graphics template**: master comp → controls on a null (Color/Slider Control, pick whip) → `essential.addProperty` (text, font, colour), `essential.addMedia` (logo) → groups and comments → `comp.responsiveTime` for the intro/outro → `essential.exportTemplate`. Ref `09-motion-graphics-templates.md`.

**3D and camera**: `threeD` switch or `new3dPrimitive` → `layer.newCamera` (two-node 35–50 mm, key position with easyEase, optional DOF) → Spot with shadows + low Ambient → check the lighting in renders. Refs `10-…`, `11-3d-camera-tracker.md`.

**Tracking and stabilizing**: `track.motion` workflow onto a null, then parent the overlay. `track.warpStabilizer` for shake. Ref `12-stabilize-track-advanced.md`.

**Render and export for social**: 9:16 1080×1920, 1:1 1080×1080, 4:5 1080×1350, 16:9 1920×1080; 30 fps; H.264 10–20 Mbps; ProRes 4444/WebM for alpha. Build one master and nest it in per-format comps. Respect safe areas on 9:16. Ref `13-render-export-social.md`.

## 5. Common mistakes
- Acting on the wrong comp. Creating or opening a comp changes the active one, so pass `comp`/`layer` ids explicitly.
- Motion blur switched on for the layers only (it needs the comp switch too).
- Parenting after animating: the child jumps. Parent first, or use `compensate`.
- Scaling or rotating text around a baseline anchor: run `layer.centerAnchor` first.
- Linear keys everywhere. Use easyEase, and an overshoot for "pop".
- Text in the platform UI zones of 9:16.
- Wanting Lottie but using 3D, Puppet or most effects (dropped on export; read the warnings).
- Huge tool outputs: avoid `puppet.info`, `renderQueue.formats` and `roto.models` inside batches, and `prop.get` on tracked properties. Use `get_layer {flat:true, time}`.
- `keys.wiggle` without selected keys fails. Prefer the `wiggle()` expression.
- Reading background jobs too early: poll `roto.status`/`track.status` (`jobs.wait` may return immediately).

## 6. Pre-delivery checks
1. `get_comp`: size, fps and duration match the brief; no stray solo/guide/disabled layers.
2. `render_frame` at **at least 4 times**: 0 s, mid-animation of each element, the last transition, the final frame (and frame 0 = last frame for loops).
3. Text is legible and inside the safe areas, and the brand colours are correct.
4. Render with `renderQueue.render {wait:true}` → `renderQueue.list` shows Done → ffprobe codec, size, frames and audio.
5. Deliver to the location the user specified and tell them the path. Clean the session with `file.newProject` after tests.

## 7. References
- `references/01-workflow-effects-presets.md` (L1–2), `02-animated-text.md` (L3), `03-shapes-keyframes-parenting.md` (L4–5), `04-layers-mattes-time.md` (L6), `05-masks.md` (L7), `06-puppet.md` (L8), `07-roto-brush.md` (L9), `08-color-and-mood.md` (L10), `09-motion-graphics-templates.md` (L11), `10-3d-camera-lights.md` (L12), `11-3d-camera-tracker.md` (L13), `12-stabilize-track-advanced.md` (L14), `13-render-export-social.md` (L15), `14-troubleshooting-and-mcp-notes.md` (appendix + verified MCP behaviour).
- "L" numbers refer to the lesson order of the Adobe book the workflow follows.
- Found something out of date? Update this skill or open an issue.
