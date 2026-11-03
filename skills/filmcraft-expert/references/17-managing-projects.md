# 17 — Managing projects (Lesson 17)

Summary in my own words; Project Manager dry run verified.

## Concepts
- **File menu housekeeping**: save, save as, save a copy, auto-save and recovery, close projects.
- **Offline clips**: disconnect clips from their files (e.g. after editing low-res copies without a proxy workflow) and relink them to full-resolution media.
- **Project Manager**: **collect** copies the project and all used media to one place; **consolidate & transcode** creates new media in a single codec and can **trim** to just the used portions plus **handles** (30-frame handles add 30 frames at each end, 60 total per clip). Dynamically linked assets (e.g. After Effects comps) are not collected; keep such projects inside the project folder.
- **Remove unused** deletes project items not used in any sequence (files stay on disk). **Consolidate duplicates** merges duplicate items.
- **Link Media / Locate** finds moved or renamed files by name, extension, duration, timecode.
- **Importing projects**: import a whole project or chosen sequences into the current one, or browse another project and copy/paste.
- **Ingest and proxies**: copy/transcode/create proxies on import; toggle proxies for smooth editing, export always from full resolution.
- **Collaboration**: Team Projects/Productions/Frame.io in Premiere (not in FilmCraft); here share via interchange files, project copies and review exports with burned timecode.
- **Storage**: delete render previews and media cache when the project is finished.

## FilmCraft
| Task | Command |
|---|---|
| Save / copy / auto-save | `file.save`, `file.saveAs`, `file.saveCopy`, `file.autoSaveNow`, `file.listAutoSaves`, `file.recover` |
| Close | `file.closeProject {force}` |
| Offline / relink | `media.makeOffline`, `media.findMissing`, `media.relink {item, path}`, `media.autoRelink {from, to}`, `media.search {folder}` |
| Project Manager | `file.projectManager {destination, mode:"collect"|"consolidate", sequences, excludeUnused:true, handles:30, preset:"prores_lt"|"prores_hq"|"h264", includeProxies, projectName, dryRun:true}` |
| Clean | `edit.removeUnused`, `edit.consolidateDuplicates`, `sequence.simplify` |
| Import project parts | `file.import {paths:[project]}`, `file.exportSelectionProject {path, items}` |
| Proxies | `media.createProxies {items, preset}`, `media.attachProxies`, `media.toggleProxies {enabled}` |
| Templates | `file.saveAsTemplate`, `file.newProjectFromTemplate` |
| Notes | `project.setNotes {text}` |
| Storage | `sequence.deleteRenderFiles`, `mediaCache.clean {all}` |

## Archive checklist (end of job)
1. `sequence.simplify` a copy of the final sequence (remove disabled clips, empty tracks).
2. `file.projectManager {mode:"consolidate", handles:30, dryRun:true}` → check `files`/`resultBytes` → run for real into the archive folder.
3. Export master + WAV stems + XML/AAF + captions (SRT) next to the archived project.
4. Deliver the final files to the agreed shared location, with versioned names, and note what was delivered and where.
5. `mediaCache.clean`, `sequence.deleteRenderFiles` on the working copy.

> Availability notes in this file are a snapshot as of 2026-11-03. ArtCraft apps update almost daily: re-check the live command catalogue before treating anything as missing.
