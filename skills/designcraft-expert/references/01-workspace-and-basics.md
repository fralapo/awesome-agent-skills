# 01 - Workspace and first layout (lessons 1-2)

Snapshot of DesignCraft on 2026-11-03: the apps update daily, so re-check absent features with `list_commands {filter}` before using a workaround; the Adobe behaviour described here is the target.

Source: synthesis of *InDesign Classroom in a Book 2026*, lessons 1 "Introducing the Workspace" and
2 "Getting to Know InDesign", translated to DesignCraft. ✔ = run on a scratch document 2026-11-03.

## What the lessons teach (in short)
- InDesign work happens in frames: the Type tool makes text frames, the Selection tool moves/threads
  them, the Direct Selection tool reaches the content (image inside a frame, path points).
- Screen modes (Normal, Preview, Bleed, Slug, Presentation) only change what you see; Preview hides
  guides and non-printing items.
- A first layout: open template → add text → apply styles → place graphics → object styles → preflight.
- Best practices stated as the backbone of the whole book: don't stack objects to fake a layout,
  thread text instead of separate boxes, format everything with styles, preflight early and often,
  automate repetitive tasks.

## DesignCraft equivalents
| Concept | DesignCraft |
|---|---|
| Tools (Selection, Direct Selection, Type, Frame…) | Not needed headless: commands act on ids (`ids` param) or on the selection (`selection.set {ids}` ✔). `tool.select`/`tool.list` exist for the desktop app. |
| Container vs content | `select.container`, `select.content`; `object.fit` moves the content. |
| Preview mode | `render_page` renders printing items only ✔; `render_page {bleed:true}` = Bleed mode ✔. |
| Navigation / zoom | Irrelevant; address pages by index (`page` 0-based in render/export, 1-based in PDF ranges). |
| Undo / History | `edit.undo`, `edit.redo`, `document.history`. |
| Sample/template | `new_document {sample:true}` opens a 4-page magazine sample with styles, parent page and folios: good reference for how a working document is built. |
| QR code (Object menu) | `object.qrCode {type:"url", content, rect}`. |
| Text to Image (generative) | **Not available as of 2026-11-03 (re-check `list_commands`)**. Generate images elsewhere (PhotoCraft / external) and `place_image`. |
| Preflight indicator | `preflight.run` ✔ (no live indicator: call it yourself after each big step). |

## Agent habits
- Start every session with `inspect_document`: it returns pages with bounds and column rectangles,
  items with ids, stories with overset, styles, swatches, layers.
- Prefer `batch` with `$N.id` references: one round-trip, ids flow from step to step ✔.
- Check visually with `render_page {scale:0.5}` (cheap) and zoom with `export_png {scale:3}` + crop
  when detail matters (e.g. folios, small type) ✔.
- Unknown parameter names: pass a bogus attribute to `type.char`/`type.para`; the error lists all
  valid attributes ✔.
