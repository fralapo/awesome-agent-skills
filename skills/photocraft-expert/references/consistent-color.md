# Consistent colour across media and photo sets (Lesson 14)

Source: synthesis of *Photoshop Classroom in a Book 2026*, Lesson 14, mapped to PhotoCraft/LightCraft.
⧗ = not available in PhotoCraft/LightCraft as of 2026-11-03 (snapshot — re-check with `command_list {filter}`
on the live app; ArtCraft apps update daily). The Photoshop behaviour described stays the target.


## Concepts
- Gamut = colours a model or device can reproduce; every monitor and printer+ink+substrate has its own.
- RGB is additive (light), CMYK subtractive (inks; CMY alone gives a muddy brown, hence K). RGB gamut is
  usually larger: saturated blues/greens fall outside CMYK, some blues shift to purple.
- ICC profiles describe colour spaces and translate between document, monitor and printer; embed them.
- Working spaces: sRGB (web), Adobe RGB / P3 / ProPhoto (wide, use 16-bit). Keep the image in its space,
  convert a copy at export.
- Color Settings matter mainly for new or untagged files; embedded profiles win.
- Calibrate (bring the monitor to a standard, e.g. D65) and profile (measure the residual).
- Soft-proof = on-screen simulation; hard proof = real print under production conditions.
- Rendering intents: Relative Colorimetric (default choice), Perceptual (second to try).
- Gamut warning highlights out-of-gamut colours; separations = one plate per ink; PDF/X = print standard.

## PhotoCraft calls
| Task | Call |
|---|---|
| Inspect mode/profile | `doc_inspect` (`mode`, `depth`), `edit.profileInfo`, `edit.installedProfiles` |
| Color Settings | `edit.colorSettings` |
| Assign vs convert | `edit.assignProfile` (re-label, changes appearance) vs `edit.convertToProfile {profile:"srgb|display-p3|adobe-rgb-compat|coated-cmyk|…" or .icc path, intent:"relative", bpc:true}` ✔ |
| Soft-proof | `view.proofSetup {…}`, `view.proofColors` ✔ |
| Gamut warning | `view.gamutWarning` ✔ → returns `fraction` / `outOfGamut` pixel stats |
| Color samplers (actual vs proof) | `view.colorSamplers.add {x,y}` (returns rgb + cmyk), `view.colorSamplers.list`, `document.pixel` |
| Mode / bit depth | `image.mode.cmyk|rgb|lab|grayscale`, `image.mode.bits16` |
| Channels | `channel.list`, `channel.target`, `channel.split` |
| Print | `file.print {printer, paper, orientation, scaleToFit…}` |
| PDF for print | `doc_export {path:"x.pdf"}` ✔ = flattened raster PDF (no PDF/X presets ⧗) – for press PDF/X build the layout in DesignCraft and place the PhotoCraft TIFF/PSD |

Note: PhotoCraft's "coated-cmyk" is a synthetic profile (300 % TAC, medium GCR) ✔: for real jobs ask the
printer for their ICC and convert with its path.

## Print procedure
1. Ask the printer: format, profile, total ink limit, bleed (often 3 mm / 1/4 in), PDF standard.
2. Check resolution ≈300 ppi at final size (`image.imageSize {resolution:300}` without resample to read).
3. Soft-proof with the printer profile, Relative Colorimetric, simulate paper; compare with samplers on
   critical colours (brand colours, deep foliage).
4. Fix only important out-of-gamut colours (Hue/Sat or Selective Color while proofing). Expect less
   saturation on paper: it is an honest simulation.
5. Convert a **copy** to CMYK (permanent loss of RGB gamut), check each channel.
6. Export TIFF/PDF; for desktop printers keep RGB and let one side (app *or* driver) manage colour.

## Consistent colour across a photo set
1. Develop one hero image in LightCraft; WB from a neutral, exposure, tone, HSL.
2. `develop.copy {groups}` → `develop.paste {ids}` or select all + `develop.sync`; `develop.autoSync` for live
   edits; `develop.matchExposure` to equalise total exposure.
3. Check every photo (`render_preview`), adjust exposure/WB per frame, compare skin and brand colours.
4. Save the look as a preset (`preset.create`) for future shoots of the same client.
5. In PhotoCraft composites: same Color Lookup / gradient map / Curves stack on all pieces; copy adjustment
   layers between documents (`layer.copyToDocument`); verify neutrals with samplers (R≈G≈B).
6. `image.adjustments.matchColor {source, luminance, intensity, fade, neutralize}` to match one image to
   another (destructive: use on a copy layer).

## Pitfalls
- Assign Profile instead of Convert changes the look.
- Do not send CMYK to a desktop printer; avoid double colour management.
- Do not flatten for layout teams without asking: DesignCraft/InDesign can use layered files.
- Web exports without sRGB look dull or oversaturated in browsers.
