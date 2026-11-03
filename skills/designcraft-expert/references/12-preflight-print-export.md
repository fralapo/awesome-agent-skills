# 12 - Preflight, separations, PDF for print, printing, package, web/social export (lesson 13)

Snapshot of DesignCraft on 2026-11-03: the apps update daily, so re-check absent features with `list_commands {filter}` before using a workaround; the Adobe behaviour described here is the target.

Source: synthesis of *InDesign Classroom in a Book 2026*, lesson 13. ✔ = verified 2026-11-03.

## Concepts
- **Preflight** (basic profile) checks: fonts available, links missing or modified, overset text,
  unresolved caption variables, broken URL links. Printers may supply their own profile.
- **Separations preview** shows each ink; **ink limit** view marks areas above the total (default 300%).
  Avoid multi-ink colour on small type. **Ink Manager** aliases duplicate spot inks or sends spots to
  process.
- Preview the pages without guides before output.
- PDF proof (high quality print preset) for clients; **press-ready PDF** with bleed and marks, saved as
  a reusable preset; PDF/X standards for printers; flatten if required.
- **Package**: copies the document, links and fonts into one folder (+ IDML, + PDF, + instructions);
  links in the copy point to the packaged Links folder. Adobe Fonts are not packaged.
- The two standard handoffs: press-ready PDF with bleed, or a package.
- Digital: export selected graphics as PNG (clean edges, type) or JPEG (photos), 72 ppi for screen;
  whole pages for email/social/web banners, often from alternate layouts per platform.

## DesignCraft
| Task | Command |
|---|---|
| Preflight | `preflight.run {minPpi:300}` ✔ → `{errors, warnings, issues:[{severity, kind:"overset"|"lowResolution"|…, item, page}]}` |
| Separations | `ink.separations {page, dpi, inkLimit:300, standard}` ✔ → inks, `maxTotal`, `overLimit.regions` |
| Inks | `ink.list` ✔, `ink.options` (alias, all to process) |
| Overprint black | `document.preferences {overprintBlack:true}` |
| Press PDF | `file.exportPdf {path, standard:"x4", bleed:true, marks:{crop:true, bleed:true, pageInfo:true}}` ✔ (PDF 1.6, PDF/X-4, TrimBox inset by bleed + offset) |
| Flattened press PDF | `file.exportPdf {standard:"x1a", bleed:true, marks:true, flatten:"high"}` ✔ (PDF/X-1a:2003, CMYK + spot only) |
| Proof PDF | `file.exportPdf {path, compressImages:true}` |
| Page ranges / spreads | `pages:"1-3,5"`, `spreads:true` |
| PDF presets | **Not available as of 2026-11-03 (re-check `list_commands`)**: keep the option object in your project notes (or in this skill) and pass it every time |
| Print | `file.printers`, `file.print {printer, dryRun:true, …PDF settings}`, `file.printBooklet` |
| Package | `file.package {dir, idml:true, pdf:{standard:"x4", bleed:true, marks:true}, instructions}` |
| PNG/JPEG page | `export_png {page, path, scale}` ✔ - scale = px per pt (1 for a px document, 300/72≈4.17 for 300 ppi) |
| Social sizes | separate documents (`intent:"web", units:"pixels"`): 1080×1080, 1080×1350 ✔, 1080×1920; or `layout.createAlternate {name, width, height}` + `liquid.pageRule` |
| Other formats | `file.exportEpub`, `file.exportHtml`, `file.exportPptx`, `file.exportIdml` ✔, `file.exportText` |

## Verify the PDF
- `pdfinfo -box file.pdf` shows TrimBox/BleedBox ✔; or PdfCraft `doc_open` → `print_readiness` (image ppi as
  drawn, boxes, bleed, output intent, unembedded fonts) and `render_preview`.
- Export result `warnings` (rasterised effects, flattening) must be read and judged, not ignored ✔.

## Printer handoff checklist
1. Preflight 0 errors; low-res warnings resolved or accepted by the client.
2. Bleed on every edge with edge-to-edge art (`render_page {bleed:true}`).
3. Inks: only the expected spots (`ink.list`), total ink under the printer limit.
4. PDF/X-4 (or X-1a on request) + crop marks; name `client_job_v01_print.pdf`.
5. Optional package with IDML; deliver to wherever the project keeps its final files.
