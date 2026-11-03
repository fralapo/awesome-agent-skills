# Selecting, aligning and transforming (Lessons 2 and 5)

Own-words summary of Classroom in a Book 2026, "Selecting Artwork" and "Transforming Artwork", mapped to VectorCraft commands.

## Selecting
| Need | Illustrator | VectorCraft |
|---|---|---|
| Whole object | Selection tool (V) | `select.set {ids}`, `select.add`, `select.toggle`; new objects are already selected |
| Anchors | Direct Selection (A) | `select.anchors`, `select.segments`, `select.anchorsMany` |
| All / none / inverse | Cmd+A, Shift+Cmd+A | `select.all`, `select.allOnArtboard`, `select.none`, `select.inverse` |
| Same attribute | Select > Same | `select.same.fillColor`, `.strokeColor`, `.strokeWeight`, `.fillAndStroke`, `.opacity`, `.appearance`, `.graphicStyle`, `.symbolInstance`, `.fontFamily`… |
| Magic Wand | Magic Wand | `select.magicWand` (+ `magicWand.options`) |
| Saved selection | Select > Save Selection | `select.save`, `select.recall`, `select.savedList` |
| Object behind another | Cmd-click repeatedly | `select.nextBelow` / `select.nextAbove`, or the id from `doc_inspect` |
| Special objects | Select > Object | `select.object.textObjects`, `.openPaths`, `.strayPoints`, `.clippingMasks`, `.brushStrokes` |
| Key object | click a selected object | `select.key` |

Headless golden rule: **work by id**. `doc_inspect {kind:"Path"}` or `document.find` return ids; almost every command takes `ids` and then ignores the current selection. Exception: commands with no params (e.g. `type.createOutlines`) act on the selection — call `select.set` first.

## Hide, lock, isolate, stack
- `object.hide`, `object.showAll`, `object.hide.otherLayers` / `.unselected`; `object.lock`, `object.unlockAll`, `object.lock.otherLayers`.
- `object.group` (Cmd+G), `object.ungroup`; isolation `object.isolate` / `object.exitIsolation` (double-click a group in Illustrator).
- Stacking: `object.arrange.bringToFront|bringForward|sendBackward|sendToBack`, `object.arrange.sendToCurrentLayer`.

## Align and distribute
- `object.align {horizontal, vertical, to:"selection"|"artboard"|"key", artboard, bounds:"preview"|"geometric"}`.
- `object.distribute` (centres/edges) and `object.distributeSpacing` (equal or fixed gap relative to the key object).
- With anchors selected, align moves the anchors (the book's "align anchor points"). To place objects along a path use `object.objectsOnPath.attach`.
- Tip: align logos and icons on **geometric bounds**; layouts with thick strokes on preview bounds.

## Transforming
| Need | VectorCraft |
|---|---|
| Move | `object.move {dx, dy, copy}`, `object.nudge` |
| Rotate / scale / reflect / shear | `object.rotate`, `object.scale`, `object.reflect`, `object.shear` (reference point, `copy`) |
| Free matrix | `object.transform {matrix:[a,b,c,d,e,f], strokes, corners, patterns}` |
| Repeat last transform | `object.transformAgain {copy:true}` (Cmd+D) — basis for radial and stepped series |
| Transform Each | `object.transformEach` (each object about its own centre, optional random) |
| Exact position/size | `object.setBounds`, `object.setProps` |
| Free distort | `object.distort`, effect `distort.freeDistort` |
| Reset bounding box | `object.resetBoundingBox` |
| Puppet Warp | `object.puppetWarp` + `object.puppetWarp.pins` |
| Dimension tool | `dimension.create` |

Options the book stresses: **Scale Strokes & Effects** (`strokes`) and **Scale Corners** (`corners`). Scaling a logo without `strokes:true` keeps stroke weights fixed and changes the proportions.

## Repeats
- Radial `object.repeat.radial {instances, radius}` (verified: 10 petals from one ellipse), grid `object.repeat.grid`, mirror `object.repeat.mirror`; `object.repeat.options`, `.release`, `.expand`.
- Repeats stay live: edit the source and every copy follows. Expand only at the end.

## Common mistakes
- Moving with values thought of in mm.
- Transforming the wrong selection: always pass `ids`.
- Forgetting `copy:true` when you meant to duplicate.
