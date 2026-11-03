# 13 - Interactive PDF, forms, review: DesignCraft → PdfCraft (lesson 14)

Snapshot of DesignCraft on 2026-11-03: the apps update daily, so re-check absent features with `list_commands {filter}` before using a workaround; the Adobe behaviour described here is the target.

Source: synthesis of *InDesign Classroom in a Book 2026*, lesson 14 "InDesign and Acrobat".
✔ = verified 2026-11-03 (DesignCraft export opened in PdfCraft).

## Concepts from the lesson
- Interactive PDF = links (URL, email, page in the document), navigation buttons (next/previous page,
  go to page), an automatic table of contents whose entries are links, form fields (e.g. a notes field
  per section, each with a unique name and a tooltip description), popups (click a trigger → a hidden
  button-image shows, others hide), video with a poster image, page transitions.
- Every interactive item is tested in Acrobat (Reader too, since most users have it): hover = hand
  cursor, click goes to the right place. Video needs a poster that *looks* playable (Acrobat shows no
  controls by default) and the user must trust the document.
- Editing after export: change hyperlink source/destination, move pages and update the TOC, re-export.
- Review: PDF comments can be brought back to InDesign; Open PDF converts a PDF/AI file into editable
  objects.

## What to do where
| Need | DesignCraft (author) | PdfCraft (post-process) |
|---|---|---|
| URL / email / page link | `hyperlink.create {url|email|page, ids}` ✔ | `link_add`, `link_edit`, `links_from_urls` (auto-link plain URLs), `link_list` ✔ |
| Next/prev/go-to-page button | `button.set {ids, action:"nextPage"|"page", page}` ✔ - exported as a link annotation, not a push button ✔ | real push buttons: `form_add_field` (button) + `form_set_actions {menu:"NextPage"}` |
| Popup (Show/Hide) | **Not available as of 2026-11-03 (re-check `list_commands`)** (`button.set` has only page/url actions); `states.create` makes multi-state objects for EPUB/desktop | `form_set_actions {trigger:"mouse_up", show:[…], hide:[…]}` on button fields; initial visibility via `form_set_props` |
| Text field / checkbox / list / signature | `form.set {ids, kind:"textField"|"checkBox"|"comboBox"|"listBox"|"signature", name, required, options}` ✔ | `form_add_field`, `form_add_field_table`, `form_set_props` (tooltip, format), `form_tab_order`, `form_detect_fields` |
| Calculations, validation, scripts | - | `form_set_props {calculate}`, `form_set_script`, `form_calculation_order`, `js_set_document_script` |
| Submit / reset / print actions | - | `form_set_actions {submit|reset|menu:"Print"}` |
| TOC with links + bookmarks | `toc.generate {styles:["H1","H2"], createBookmarks:true}`, `toc.update` | `bookmark_from_structure`, `bookmark_from_text_styles`, `bookmark_*` |
| Bookmarks | `bookmark.add {name, page}` ✔ | `bookmark_list` ✔, `bookmark_add/move/rename` |
| Page transitions | `page.transition {all:true, kind:"dissolve"}` ✔ | `page_transition_set` |
| Video/audio | `file.place` (mp4) + `media.options {poster, controls, playOnPageLoad}`; export with `media:true` | - |
| Initial view, full screen | `file.exportPdf {fullScreen, pageLayout, view, bookmarksPanel}` ✔ | `doc_initial_view` |
| Accessibility (tags, alt text, reading order) | `file.exportPdf {tagged:true}` ✔ + `object.altText` ✔, `object.exportOptions {artifact}` | `accessibility_check`, `accessibility_fix`, `accessibility_autotag_*`, `accessibility_set_alt`, `accessibility_report` |
| Review comments | `note.*`, `changes.*` inside the layout; no import of PDF comments as of 2026-11-03 (re-check) | `comment_add` (note, highlight, replace, stamp…), `comment_list`, `comment_reply`, `comment_set_status`, `comments_summarize` |
| Compare versions | - | `doc_compare`, `doc_compare_report` |
| Edit text in a final PDF | re-export from DesignCraft (preferred) | `text_edit` for small fixes only |
| Open PDF as editable objects | **Not available as of 2026-11-03 (re-check `list_commands`)**: `file.place {pdfPage}` places it as a graphic; vector art via `edit.pasteSvg` | - |
| Security / signing / PDF/A | - | `doc_protect`, `sign_document`, `pdfa_convert`, `pdfa_verify` |

## Recommended flow
1. Build in DesignCraft: styles for headings → `toc.generate {createBookmarks:true}`; links; nav buttons;
   form fields with unique names; alt text on images.
2. `file.exportPdf {path, tagged:true, bookmarksPanel:true, pageLayout:"single", media:true}` ✔
   (no bleed, no marks, RGB intent).
3. PdfCraft: `doc_open` → `link_list` ✔, `form_fields` ✔, `bookmark_list` ✔ to verify every item → add
   what DesignCraft lacks (show/hide popups, calculations, tooltips, tab order) → `accessibility_check` →
   `doc_save` under a new name.
4. Hand off: Acrobat Reader compatible; tell the client that video needs "trust this document".
5. After layout changes, re-export from DesignCraft and **re-apply** the PdfCraft step (keep the PdfCraft
   actions as a script/batch in the job notes), rather than patching the PDF repeatedly.
