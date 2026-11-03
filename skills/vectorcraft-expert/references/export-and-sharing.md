# Packaging, PDF, export and sharing (Lesson 16)

Own-words summary of Classroom in a Book 2026, "Sharing Projects".

## Packaging
- `file.package {folder, name, copyLinks, linksFolder, relink, copyFonts, report}`: copies the saved document, its linked files (Links/) and fonts (Fonts/, only licence-permitted) plus a report. Without `folder` it returns a zip as base64. Check `missingLinks` and `skippedFonts` in the reply.

## PDF
- `document.exportPdf {path, preset, standard, range, bleed, marks, output, advanced, compression, security}` (also via the `export` tool with `options`).
  - Default preset keeps VectorCraft editing data (`preserveEditing`), like Illustrator's default PDF that reopens without loss: fine for review, not for print.
  - Print: `standard:"pdfX4"` (keeps transparency and layers, ICC-tagged) or `pdfX1a` (flattened, CMYK only); `bleed:{useDocument:true}`; `marks:{trim:true}`; `advanced:{outlineText:true}` when fonts are uncertain. Verified on a CMYK test: PDF/X-4 with document bleed, trim marks, outlined text written correctly; the reply warned about an RGB raster (drop shadow) being converted to CMYK.
  - Read every `warnings` entry: they flag RGB in CMYK files, flattening, missing fonts.
  - Archive: `pdfA2b`. Presets: `pdf.preset.list` / `save`.

## Export for screens and assets
- Quick single files: `export {path, format, artboard|range, scale, selection, outlineText}`. Verified: SVG with `outlineText:true`, PNG at `scale:2`.
- Many artboards / sizes at once: `document.exportForScreens {folder, artboards|range, formats:[{format:"png", scale:"2x"}, {format:"svg"}, {format:"jpg", quality:80}], includeBleed, name, folders}`.
  - `preset:"mobile"` (PNG 1x/2x/3x) or `"density"` (Android ldpi…xxxhdpi).
- Asset export (logo, icons as separate files): `assets.add` (Collect for Export) → `assets.list` → `assets.export` or `exportForScreens {assets:[ids]}`. Assets stay linked to the art: re-export after edits.
- Only the selection: `export {selection:true}` or `document.exportSelection`.
- Formats available: vectorcraft, svg/svgz, pdf, ai, eps, dxf, emf, wmf, png, png8, jpg, webp, gif, tiff, bmp, tga, psd, txt. **Not available as of 2026-11-03 (re-check with `document.formats`): OBJ, USDA, USDZ, GLTF** (3D formats Illustrator exports from 3D art).
- Web specifics: SVG options `minify`, `decimals`, `responsive`, `styling`, `embedFonts`; legacy `document.exportForWeb`; CSS `css.generate`.

## Choosing the format
| Use | Format |
|---|---|
| Website logo/icon | SVG (text outlined) + PNG 1x/2x fallback |
| Social post | PNG (or JPG 80–90 for photos), exact pixel size, RGB |
| Print shop | PDF/X-4 (or X-1a if requested), CMYK, bleed, marks, fonts embedded or outlined |
| Client editable source | .vectorcraft + .ai/.pdf with preserveEditing |
| Cutting plotter / CAD | DXF or SVG with outlined text and expanded strokes |

## Collaboration — not available as of 2026-11-03 (snapshot, re-check with `command_list {filter:"share"}` / `"invite"` / `"review"`)
- Target behaviour in Illustrator: **Invite to Edit** saves a cloud document and lets invited people edit it, one editor at a time (asynchronous); **Share for Review** creates a link where reviewers comment in the browser without Illustrator, access can be limited to invited people, and "Update Content" pushes the latest version to the same link.
- Substitute until then: deliver PNG/PDF through whatever shared folder or channel the project uses and collect feedback there; for annotated review, comment on the exported PDF (e.g. with ArtCraft's PdfCraft, if available).
