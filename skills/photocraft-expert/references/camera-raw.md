# Camera Raw → LightCraft (Lesson 12)

Source: synthesis of *Photoshop Classroom in a Book 2026*, Lesson 12, mapped to LightCraft (primary) and
PhotoCraft's Camera Raw Filter.

⧗ = not available in PhotoCraft/LightCraft as of 2026-11-03 (snapshot — re-check with `command_list {filter}`
on the live app; ArtCraft apps update daily). The Photoshop behaviour described stays the target.

LightCraft command ids here come from its command catalogue and were **not live-tested**; confirm with
`command_list {filter}` / `list_controls` before relying on them.

## Concepts
- Raw = digital negative: single-channel sensor data, not yet RGB. The camera/preview JPEG is only an
  embedded rendering; the developer reinterprets the data from scratch (much more latitude than JPEG).
- Non-destructive: the raw stays read-only, edits live in a sidecar (.xmp) or inside DNG. Move sidecars with
  the raw. DNG is the open archival format.
- Raw profile (Adobe Color/Landscape/Portrait/Vivid/Monochrome/Adaptive, camera matching, creative) is the
  first interpretation, not an ICC profile.
- WB = Temperature (blue↔yellow, kelvin) + Tint (green↔magenta). Sample a lit neutral, not clouds or
  shadow areas.
- Light: Exposure, Contrast, Highlights/Shadows (detail near the ends), Whites/Blacks (end points).
- Effects: Texture and Clarity (local contrast at different scales), Dehaze. Vibrance gentler than
  Saturation.
- Histogram clipping overlays: red = blown highlights, blue = blocked shadows; specular highlights may clip.
- Panel order top → bottom is a sensible workflow. Sync settings to a set, then check each photo.

## LightCraft mapping (develop ids from `list_controls`)
| ACR | LightCraft |
|---|---|
| Profile | `develop.profile {id, amount}` (`profiles.list`) |
| WB preset / eyedropper | `develop.wb {mode:"cloudy"|…|"custom", temp, tint}`, `develop.wbPick {x,y}` (normalised 0..1) |
| Auto | `develop.auto` |
| Light sliders | `develop.set {values:{"light.exposure":0.5,"light.contrast":0,"light.highlights":-20,"light.shadows":70,"light.whites":20,"light.blacks":-10}}` |
| Parametric/point curve | `curve.highlights|lights|darks|shadows`, `develop.curve {channel, points}` |
| Vibrance, saturation | `color.vibrance`, `color.saturation` |
| Color Mixer (HSL) / Point Color | `mixer.<band>.hue|sat|lum` (red…magenta), `pointColor.pick` |
| Color Grading | `grading.shadows|midtones|highlights|global.hue|sat|lum`, `grading.blending`, `grading.balance` |
| Texture / Clarity / Dehaze | `effects.texture`, `effects.clarity`, `effects.dehaze` |
| Vignette, grain | `vignette.*`, `grain.*` |
| Sharpening (Amount, Radius, Detail, Masking) | `detail.sharpenAmount|Radius|Detail|Masking` |
| Noise reduction / Denoise | `detail.nr*`, `enhance.denoise` + `denoise.*` (AI model) |
| Lens corrections / CA / defringe | `optics.*` |
| Upright / transform | `geometry.upright`, `geometry.vertical|horizontal|rotate|scale`, `crop.angle` |
| Crop | `crop {…}` / `crop.set`, `crop.aspect`, `crop.autoStraighten` |
| Calibration | `calibration.*` |
| B&W | `develop.treatment {bw:true}`, `bw.*`, `develop.autoBwMix` |
| Masks (brush, linear, radial, subject, sky, background, object, people-like, colour/luminance range) | `mask.add {kind, …}`, `mask.addComponent {op}`, `mask.brushStroke`, `mask.adjust`, `mask.invert`, `mask.rename` |
| Remove / heal spots | `spot.add {mode:"remove|heal|clone|fill", points, size}`, `spot.findDust`, `spot.findBlemishes` |
| Red eye | `redeye.add` |
| Before/after | `beforeAfter.*`, `render_preview` |
| Sync / copy-paste | `develop.copy {groups}`, `develop.paste`, `develop.sync`, `develop.autoSync`, `develop.matchExposure` |
| Snapshots/versions | `version.create`, `version.restore`, `history.*` |
| HDR / panorama merge | `merge.hdr`, `merge.panorama`, `merge.hdrPanorama`; HDR editing `develop.hdr` |
| Save Images (JPEG 800 px sRGB) | `app.export {format:"jpeg", longEdge:800, quality:85, colorSpace:"srgb", metadata:"copyright"}` (`export` tool) |
| Open as Object (raw SO in PS) | ⧗ direct; export 16-bit TIFF/PSD and `doc_place` it; or use PhotoCraft `filter.cameraRaw` on an SO |

PhotoCraft `filter.cameraRaw` ✔ (on an SO it is a Smart Filter): temperature/tint (relative −100..100),
exposure, contrast, highlights, shadows, whites, blacks, texture, clarity, dehaze, vibrance, saturation,
parametric and point curves, HSL arrays, colour grading, calibration.

## Recipes
**Landscape/architecture set**: Landscape profile → WB eyedropper on a white sign → Auto, then exposure
+0.5, highlights −20, shadows +70, whites +20, blacks −10 → vibrance +20, clarity +20 → sharpen judged at
100 % (exaggerate to see, then back off: e.g. 100 → 70, radius 0.9, detail 25, masking ~60) → copy/sync to
the other frames → check each → export.

**Portrait**: Portrait profile → WB on lit white clothing → Auto then exposure back to 0, contrast −20,
clarity small (+8) → remove spots (non-generative) at 100 % → brush masks: irises saturation +70, red eye
corners −50 saturation, eye brighten +0.5 exposure → skin mask (subject/skin kind) texture −30 → compare
before/after.

## Pitfalls
- The look changes on open because the camera preview is replaced: normal.
- Clarity until halos appear, then reduce; on portraits use only through masks.
- Mixed light needs local WB corrections.
- After syncing, review each image; AI features slow syncing.
- Ethics: do not remove moles, jewellery or identity marks without the subject's consent.
- Do not import into the user's LightCraft library without permission (agent rule for this skill).
- Professional workflow: unique date-based names, master in PSD/TIFF, convert (not assign) profiles,
  multiple automatic backups.
