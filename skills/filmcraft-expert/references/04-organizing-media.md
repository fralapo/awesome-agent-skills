# 04 — Organizing media (Lesson 4)

Summary in my own words; FilmCraft mapping verified.

## Concepts
- The **Project panel** is the asset database: columns of metadata, list/icon/freeform views, search field that also finds items inside closed bins.
- **Bins** group clips by type, scene, day or purpose; you can nest bins, drag clips in and create a bin from a selection. Organization is non-destructive: renaming or deleting a clip in the project never touches the file.
- **Labels** (colors) and **metadata** (scene, shot, description, log notes) make search and selection faster.
- **Reviewing footage**: play with space, shuttle with J/K/L, step with arrows, jump with timecode; lower playback resolution for heavy media; safe margins overlay.
- **Modifying clips**: fix audio channel mapping (e.g. two mono mics recorded as a stereo pair), **merge clips** to marry a camera clip with separately recorded audio, **interpret footage** to override frame rate, pixel aspect, alpha or color space.
- Premiere's Media Intelligence (AI visual search) has no FilmCraft equivalent.

## FilmCraft
| Task | Command |
|---|---|
| Bins | `file.newBin {name,parent}`, `file.newBinFromSelection`, `project.moveToBin`, `project.renameBin` |
| Search bins | `file.newSearchBin {column,operator,text}`, `project.editSearchBin` |
| Find | `edit.find {scope:"project", column, operator, text}`, `edit.findNext` |
| List items | `project.items {bin, recursive}`, `project_inspect` |
| Columns / view / sort | `project.columns.set`, `project.view.set`, `project.sort` |
| Labels | `edit.label {label, items}` or `edit.label.<color>` |
| Rename | `clip.rename {item, name}` |
| Metadata | `metadata.get`, `metadata.set {item, field, value}` |
| Playback / navigation | `source.open`, `source.setPlayhead`, `playhead.set {timecode}`, `playhead.step` |
| Audio channels | `clip.audioChannels {items, format, channels}` |
| Merge with external audio | `clip.mergeClips {items, method:"audio"|"timecode"|"in"}` |
| Interpret footage | `clip.interpretFootage {items, colorSpace, pixelAspect}` |
| Frame-rate / timecode | `clip.modifyTimecode`, `clip.speedDuration` (sequence level) |
| Poster frame | `clip.setPosterFrame` |
| Freeform board | `project.freeform.*` (layout, stack, arrangements) |

## Good practice
- Name bins by purpose (01_Footage, 02_Audio, 03_Graphics, 04_Sequences, 99_Exports) so sorting is stable.
- Log notes in metadata while reviewing; later `edit.find` on `Log Note` finds the good takes.
- Fix channel mapping and interpretation in the project *before* editing: every instance in sequences inherits it.
