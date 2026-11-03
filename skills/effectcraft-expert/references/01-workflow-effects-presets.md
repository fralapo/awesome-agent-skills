# Workflow, effects and presets (lessons 1–2)

Our own summary of *After Effects Classroom in a Book 2026*, lessons 1–2, mapped to EffectCraft over MCP.

## The standard cycle
1. Import and organize the footage.
2. Create a composition. It is a container with space (size) and time (duration and fps).
3. Stack the layers. Top to bottom in the list is front to back on screen.
4. Transform and animate properties with keyframes.
5. Add effects.
6. Preview at several times.
7. Render and export.

| Step | EffectCraft |
|---|---|
| Import files | `command_run file.import {paths:[…], addToComp?, newComp?}`. For layered PSD/AI files, add `importAs: composition` or `compositionLayerSizes` (not tested). |
| Comp from footage | `file.import {…, newComp:true}` (verified) or `file.newCompFromSelection` |
| New comp | `comp.new {name,width,height,frameRate,duration,background,renderer?}` |
| Comp settings | `comp.settings` |
| Footage to layer | `layer.addItem {item, time?, position?, in?, out?}` |
| Fit to frame | `layer.transform {op:"fit"|"fitWidth"|"fitHeight"|"center"}` |
| Missing footage | `footage.missing`, `file.findMissing`, `footage.relink` |
| Workspaces and panels | UI only (`window.workspace`). Irrelevant when headless. |

## Transform properties
- Paths: `transform/anchor`, `position`, `scale`, `rotation`, `opacity`. 3D layers add `orientation`, `rotationX` and `rotationY`.
- In AE the reveal shortcuts are A, P, S, R and T (U shows animated properties). In EffectCraft, read them with `get_layer {layer, flat:true}`.
- `set_property` without `time` sets a static value. With `time` it adds a key and turns the stopwatch on.
- Scale is in percent. You can pass `[x,y]`, and it is stored as vec3.

## Effects
- An effect lasts the whole layer duration and can be switched off with `effect.toggle`.
- `add_effect {layer, effect:"Drop Shadow", values:{…}}` returns the parameter paths (`effects/#1/…`). Use those with `set_property` and `add_keyframe`.
- To affect many layers at once, use one of these:
  - an **adjustment layer** (`layer.newAdjustment`), which affects everything below it;
  - a **precomp**, with the effect on the precomp layer.
- Other commands: `effect.copy`/`effect.paste`, `effect.remove`/`effect.removeAll`, `effect.reorder`.

## Animation presets
- Built-in text presets: `layer.applyTextPreset {layer, preset}`. The values are typewriter, fadeUpCharacters, bounceInWords, trackingIn, scramble, blurIn, jitter and dropInLines.
- General presets: list them with `anim.builtinPresets`, apply them with `anim.applyBuiltinPreset {preset, layers}` (verified). There are three categories:
  - Transitions: fadeIn/Out, wipes, clockReveal, cardFlip…
  - Backgrounds: softGradientDrift, bokehDrift, grainyWash…
  - Behaviors: floatUpDown, pulse, shake, orbit, heartbeat…
- Your own presets: save with `anim.savePreset {path:.ecpreset}`, apply with `anim.applyPreset`.
- There is no Adobe Bridge. `anim.browsePresets` only works in the UI.

## Precomposing (nesting)
- Use it to group layers, change the render order, or animate a group as one object.
- `layer.precompose {layers:[…], name, mode:"move"}` returns `{comp, layer}` (verified).
  - `move` moves the attributes and effects inside the new comp.
  - `leave` keeps them on the layer. It works for a single layer only.
- To edit the inner comp, run `comp.open {comp}`. Calls without `comp` act on the **active** comp.

## Transparency
Lower `transform/opacity`. For a fade, key it from 0 to 100, or use the `fadeIn` preset.

## Common mistakes
- The effect lands on the wrong layer. Check `get_comp` first.
- You forget that a newly created or opened comp becomes the active one.
- You put an effect on a precomp when you meant one inner element, or the other way round.

> Availability notes in this file are a snapshot as of 2026-11-03. ArtCraft apps update almost daily: re-check the live command catalogue before treating anything as missing.
