# 10 - Importing and modifying graphics, links, clipping, libraries (lesson 11)

Snapshot of DesignCraft on 2026-11-03: the apps update daily, so re-check absent features with `list_commands {filter}` before using a workaround; the Adobe behaviour described here is the target.

Source: synthesis of *InDesign Classroom in a Book 2026*, lesson 11. ✔ = verified 2026-11-03.

## Concepts
- **Vector** (AI, EPS, PDF, SVG: scale freely) vs **raster** (PSD, TIFF, JPEG, PNG: resolution-bound).
- **Links**: placed files are linked, not copied. Status: OK, modified (update), missing (relink or relink
  to folder). Update all instances at once; relink swaps the picture keeping the frame.
- **Effective resolution** = original ppi ÷ scale. Print target ≥ 300 ppi effective; screen ~72-150.
- Fitting: fill proportionally (crop to fill), fit proportionally (show all), fit frame to content,
  centre; **auto-fit** keeps the fit when the frame is resized.
- Backgrounds removed: vector clipping paths (hard edge, from Photoshop paths or detected edges) vs
  alpha transparency (soft edge). Native PSD/AI placement respects layers and transparency.
- Subject-aware text wrap (AI) wraps around the detected subject.
- Type filled with an image: create outlines, place into them.
- **Libraries** hold reusable items (logos, boilerplate, author photos).
- Generative AI (expand, text to image) appears in the 2026 edition.

## DesignCraft
| Task | Command |
|---|---|
| Place image | `place_image {path|base64, frame | x,y,width}`; `file.place {path, frame}` ✔ (also PDF pages: `pdfPage`, `pdfCrop`; IDML/designcraft page as group: `layoutPage`) |
| Place cursor | `place.load`, `place.drop` |
| Fit | `object.fit {mode:"fillProportionally"|"fitProportionally"|"fitContentToFrame"|"centerContent"|"fitFrameToContent"}` ✔ |
| Auto-fit | `object.fittingOptions {…}`, clear with `object.clearFittingOptions` |
| Links | `links.list` → status ok/modified/missing/embedded, `pixels`, per-use `ppi`; `links.update`, `links.relink {asset, path}`, `links.relinkFolder`, `links.embed`, `links.copyTo` |
| Clipping | `object.clippingPath {type:"alpha"|"edges", threshold, tolerance}` ✔ |
| Wrap | `object.textWrap` (see 03) ✔ |
| Text filled with image | `type.createOutlines {ids}` → compound path frame → `file.place {frame}` |
| Vector art from VectorCraft/Figma | `edit.pasteSvg {svg, at}` (paths editable, text outlined) |
| Libraries | `library.new {path}`, `library.add`, `library.place`, `library.list`; `conveyor.collect|place` |
| Anchored (inline) image | `anchored.insert {ids, story, pos, position:"inline"|"aboveLine"|"custom"}` |
| Alt text | `object.altText {text, ids}` ✔ (EPUB warns about images without it ✔) |
| Display quality | n/a headless |
| Subject-Aware wrap, generative fill/expand | **Not available as of 2026-11-03 (re-check `list_commands`)** - prepare the image in PhotoCraft (cut-out with alpha), then clipping path + contour wrap |

## Checks
- `preflight.run {minPpi:300}` flags `lowResolution` per item ✔ (e.g. "effective 86 ppi").
- Images are read from paths the engine can see; keep assets inside the server's allowed root (e.g. `~/Craft/<job>/Links/` in a default install; check the server instructions or the error message).
