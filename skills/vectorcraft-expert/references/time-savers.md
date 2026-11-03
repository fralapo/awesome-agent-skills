# Time-saving techniques: symbols, libraries, global edit, mockups (Lesson 14)

Own-words summary of Classroom in a Book 2026, "Exploring Time-Saving Techniques".

## Symbols
- Why (book): edit once and every instance updates, smaller files, faster placement.
- Create: `symbol.new {ids, name, registration: 4, type:"static"|"dynamic", nineSlice}`. The selection is replaced by an instance.
- Place more instances: `symbol.place`; spray many: `symbol.spray`, then `symbol.adjust` (size, spin, stain…).
- Edit the master: `symbol.edit` … `symbol.exitEditing` (isolation mode), or `symbol.update` from edited art.
- **Dynamic symbols**: instances can change some appearance (colours) without breaking the link — `symbol.instance.setAppearance`, reset `symbol.instance.reset`.
- `symbol.replace` (swap the master used by selected instances), `symbol.breakLink` (instance becomes plain art), `select.same.symbolInstance`, `symbol.selectInstances`, `symbol.unused`, libraries `symbol.libraries` / `addFromLibrary` / `saveLibrary`.
- Use for: repeated icons in infographics, trees/people in illustrations, logo lockups used many times in one file.

## Libraries
- Illustrator's Creative Cloud Libraries sync colours, type styles and graphics across apps and devices. VectorCraft has **local** libraries only: `library.create`, `library.add`, `library.use`, `library.list` / `get`, groups `library.createGroup`, share by file with `library.export` / `library.import`. Cloud sync and the linked "Edit Original" round trip with other apps are not available as of 2026-11-03 (snapshot — re-check with `command_list {filter:"library"}`); target behaviour: assets dragged from a library stay linked and update everywhere when the library item changes, or can be embedded to stop updating.
- Practical substitute for a brand kit: one `.vectorcraft` library per brand or project (colours as global swatches, logo variants, paragraph/character styles), exported with `library.export` and kept next to that project's source files.

## Global editing
- Change every copy of a repeated element that is **not** a symbol: select one, `select.globalEdit {appearance, size, artboards:"all"}` → returns all matching ids; edit; call `select.globalEdit` again to stop. Options: `select.globalEditOptions`.
- Great for files built by copy-paste across many artboards (social carousels).

## Mockups — not available as of 2026-11-03 (snapshot — re-check with `command_list {filter:"mockup"}`)
- Target behaviour: Illustrator's Mockup bends vector art onto a product photo (mugs, bags, shirts) following its shape, and the art stays editable and repositionable on the photo.
- Workaround until then: `file.place` the photo, put the art above, distort with `object.envelope.makeWithMesh` / `object.envelope.makeWithWarp` or the perspective grid (`perspective.*`), set a blend mode such as Multiply with `transparency.set`, and clip with `object.clippingMask.make`. For realistic product shots a raster editor with smart objects works better (e.g. ArtCraft PhotoCraft `doc_replace_smart_object`, if available).

## Other speed-ups in VectorCraft
- `command_batch` runs many commands in one call (and one undo group with `edit.undoGroup.begin/end`).
- `object.transformAgain`, `object.repeat.*`, `object.blend.make` for series.
- Variables and data sets (data merge for name badges, price tags): `variable.define`, `variable.makeTextDynamic`, `dataset.import`, `dataset.next`.
- Cleanup add-ons: `addon.cleanup.check` / `fix`, `addon.arrange.grid`, `addon.color.applyNearestSwatch`.
