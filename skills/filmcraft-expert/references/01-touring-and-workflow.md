# 01 — Touring the editor and the overall workflow (Getting Started + Lesson 1)

Source: summary in my own words of *Premiere Classroom in a Book 2026*, Getting Started and Lesson 1, mapped to FilmCraft.

## Concepts
- **Nonlinear editing**: you can place, move, replace and re-order any clip at any time; nothing forces a fixed order of operations.
- **Standard pipeline**: get media onto fast storage → organize → assemble a sequence → refine edits → audio → effects/compositing → color → titles/captions → export → archive.
- **Companion apps**: Premiere relies on After Effects (motion), Audition (audio), Photoshop/Illustrator (stills), Media Encoder (background exports). In the ArtCraft suite the equivalents are **EffectCraft**, **SoundCraft**, **PhotoCraft/VectorCraft** and FilmCraft's own **export queue**. There is no Dynamic Link: hand off by rendering files (ProRes/PNG/WAV) and re-importing.
- **Panels**: Project (assets), Source Monitor (raw clip), Program Monitor (sequence output), Timeline, Effect Controls, Properties/Essential panels, meters. Workspaces are saved panel layouts.
- **Performance**: fast drives for media and cache, enough RAM, GPU rendering; lower playback resolution when the machine struggles.

## FilmCraft equivalents
| Task | Command / tool |
|---|---|
| State of the project | `project_inspect`, `doc_inspect`, `state.inspect` |
| See a frame of the Program output | `render_frame {seconds}` / `render_preview` |
| Discover features | `command_list {filter:"..."}`, `effects.list {kind}` |
| Preferences | `prefs.get`, `prefs.set`, `prefs.schema` |
| Keyboard shortcuts | `shortcuts.list/get/set/presets/export` |
| Workspace / panel layout | UI only: `ui_elements`, `ui_click`, `ui_screenshot` in bridge mode |
| Performance and renderer | `perf.stats`, `file.projectSettings.general {renderer:"gpu"}` |
| Demo material for tests | `file.openDemoProject`, `file.importDemoFootage {scene}` |

## "First video" quick path (headless)
1. `file.newProject {name}` → `media_import {paths}` (or demo footage).
2. `file.newSequence {name, width, height, fps}` or `timeline.place {..., matchSequence:true}` on an empty sequence.
3. `timeline.place {items:[...], track:"V1", seconds:0}` to lay clips back to back.
4. A title: `graphics.newText`. A transition: `sequence.applyVideoTransition`.
5. `render_frame` at a few points, then `file.exportMedia {path, preset, wait:true}`.

## Good practice
- Learn the shortcut layer: in FilmCraft every menu item, shortcut and gesture maps to a command id, so the shortcut table (`shortcuts.list`) doubles as a feature index.
- Keep the headless backend in mind: dialogs never open; everything takes explicit parameters.
