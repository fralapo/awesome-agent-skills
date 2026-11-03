# 08 — Advanced editing techniques (Lesson 8)

Summary in my own words; trims verified (`timeline.trim` ripple, `timeline.roll`, `timeline.slip`).

## Concepts
- **Four-point edit**: source In/Out and sequence In/Out all set. If durations differ, choose: change speed to fit, or ignore one of the points (trim).
- **Speed/duration**: slowing a clip lengthens it unless duration is unlinked or a neighbour blocks it; reverse playback; ripple option to push following clips. **Rate Stretch** changes speed by dragging an edge: perfect to fill an exact gap.
- **Time interpolation**: frame sampling (crisp, can stutter), frame blending (soft), optical flow (synthesized in-between frames, best for slow motion, can warp).
- **Replace edit**: swap one clip instance in the sequence for another while keeping effects; **synchronized replace** keeps a matched frame. **Replace footage** swaps the source in the project, updating all instances.
- **Text-based editing**: transcribe, then remove or add content by selecting words; remove pauses and filler words.
- **Trimming**: regular (edge, leaves gap), ripple (edge, closes/opens gap), rolling (moves a cut, total unchanged), slip (changes content inside fixed boundaries), slide (moves the clip, neighbours adapt). Trim mode in the Program Monitor shows both sides of the cut; dynamic trimming trims while playing (J/K/L); keyboard trims move the selected edit by 1 or many frames.

## FilmCraft
| Task | Command |
|---|---|
| Speed / reverse | `clip.speedDuration {clips, speed:50, reverse, ripple:true, interpolation}` |
| Rate stretch | `timeline.rateStretch {clip, edge, delta}` |
| Interpolation | `clip.setTimeInterpolation {clips, mode:"opticalFlow"}` |
| Frame hold | `clip.frameHold`, `clip.frameHoldOptions`, `clip.insertFrameHoldSegment` |
| Replace in sequence | `clip.replaceFromBin {clips, item, keepSourceIn}`, `clip.replaceFromSource(MatchFrame)` |
| Replace footage | `media.replaceFootage {item, path}` |
| Transcript | `transcript.generate {items, model, language:"auto"}` (download `whisper-base` first, ~290 MB), `transcript.inspect`, `transcript.search` |
| Cut by text | `transcript.extract {from, to}`, `transcript.lift`, `transcript.removePauses {minSeconds}`, `transcript.removeFillers` |
| Trims | `timeline.trim {clip, edge, mode:"regular"|"ripple", deltaFrames}`, `timeline.roll {left, right, deltaFrames}`, `timeline.slip {clip, deltaFrames}`, `timeline.slide {clip, deltaFrames}` |
| Edit-point trims | `trim.selectEditPoint {clip, edge, kind}`, `trim.nudge {frames}`, `trim.ripplePrevious/rippleNext`, `trim.extendToPlayhead` |
| Dynamic trim | `trim.shuttle`, `trim.playAround`, `trim.monitor` |
| Scene detection | `clip.sceneEditDetection {clips, applyCuts, createSubclips, generateMarkers}` |

## Practice
- Cut on action and on breaths; roll edits fix "late" or "early" cuts without breaking sync.
- Use slip on B-roll to find the best moment without changing the edit's rhythm.
- For slow motion shoot high frame rate and interpret to the sequence rate; optical flow is the fallback.
- Ripple trims with sync lock off on music tracks desync everything after the edit.
