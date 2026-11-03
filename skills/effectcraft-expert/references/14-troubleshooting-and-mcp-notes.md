# Troubleshooting (appendix) and MCP behaviour notes

## From the appendix, translated
| AE problem | EffectCraft |
|---|---|
| Crash at startup → safe mode, reset preferences | `prefs.reset`; manage plug-ins with `effect.plugins.list` / `effect.manage` |
| Missing footage, fonts or effects | `footage.missing`, `file.findMissing`, `footage.relink`, `effect.warning`; relink one file and the others in the same folder follow |
| Slow renders (snail column) | no per-layer render-time column. Toggle effects or layers, lower `layer.quality`, use `view.res.half`, and pre-render heavy precomps (`render.preRender`) |
| Memory | `edit.purge`, `cache.diskStats`, `playback.cacheWhenIdle` |

## EffectCraft facts verified on 2026-11-03 (v0.21.0, headless)
- `app.capabilities`: 743 commands, 308 effects, export H264/HEVC/AV1/ProRes/WebM/GIF/image sequences/WAV/AIFF.
  - The engine describes itself as an alpha: about 91% of AE's feature breadth, about 45% "ready for real work".
  - It renders on the **CPU** unless started with `--gpu`.
- A new comp becomes the **active** comp. Most commands default to the active comp or the selection, so pass `layer` and `comp` explicitly.
- Layer references: an id (best), `"#n"` (index from the top) or a name. Ids are returned by the create commands.
- Times are seconds, in layer time by default (`timeBase:"comp"` to switch).
- **Large outputs:** `puppet.info`, `renderQueue.formats` and `roto.models` inside a `command_batch` overflowed the tool limit (85 k chars). `prop.get` on a tracked property dumps every key. Use `get_layer {flat:true, time}` to read values instead.
- `command_batch` stops on the first error unless `stop_on_error:false`. Unknown ids fail.
- `keys.wiggle` needs selected keyframes (`keys.select`). Otherwise it fails with "select keyframes first".
- Background jobs (roto propagate and freeze): `jobs.wait` returned at once. Poll `roto.status` / `track.status` until `running:false`.
- `file.newProject` resets the session. Do this at the end of throwaway tests, and **never** `file.save` over user files.
- `essential.exportTemplate` writes `.ectemplate`. `file.exportLottie` returns warnings for unsupported features.
- Test footage can be synthesised with ffmpeg (`color` + `overlay=x='…+t*…'`). Note: `drawbox` with `t` did not produce motion in our test.

## Absent or out of scope (checked with command_list)
Adobe Bridge, Adobe Media Encoder, Adobe Fonts, Creative Cloud Libraries, `.mogrt` export, Character Animator, Frame.io/Team Projects collaboration, the per-layer render-time column, and Substance/Adobe Stock integration.

The rough substitutes:
- the render queue instead of Media Encoder;
- `.ectemplate` instead of `.mogrt`;
- installed fonts via `text.fonts`;
- `file.exportTimeline` (Premiere project interchange, not tested).

> Availability notes in this file are a snapshot as of 2026-11-03. ArtCraft apps update almost daily: re-check the live command catalogue before treating anything as missing.
