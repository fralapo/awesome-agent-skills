# 15 — Creating graphics, titles and captions (Lesson 15)

Summary in my own words; text, alignment, captions verified (title + caption rendered).

## Typography essentials for video
- **Font**: readability first; sans-serif for small or fast text on screens; at most two families per project.
- **Color/contrast**: light text on dark or vice versa; add stroke, shadow or a background box over busy images.
- **Kerning** = space between two specific letters; **tracking** = spacing over a whole word/line; **leading** = space between lines.
- **Alignment**: left for reading blocks, centered for short titles; lower thirds are usually left-aligned on the left third.
- **Safe margins**: keep titles inside the title-safe zone (and inside platform UI safe zones for social).
- Give text time on screen: roughly a line read twice in the duration.

## Concepts
- **Point text** grows as you type; **paragraph text** wraps inside a box you size. Graphics can hold several text and shape layers, be aligned and distributed, use responsive pinning (layers that follow others), styles, and be saved as templates.
- **Rolls and crawls** for credits/tickers.
- **Motion Graphics templates**: reusable graphics with exposed controls (text, colors, positions).
- **Captions**: a caption track (subtitle, CEA-608/708, Teletext) with segments; import SRT/VTT, create from a transcript, style globally, export as sidecar or burn in; captions can be upgraded to graphics for custom design.

## FilmCraft
| Task | Command |
|---|---|
| Text | `graphics.newText {text, position:[x,y], box:[w,h]?, size, font, fontStyle, seconds, track, time}` |
| Style | `graphics.set {clip, layer, props:{font, font_style, size, align, tracking, leading, fill_color, stroke, stroke_width, shadow, background…}}` |
| Per-character | `graphics.setCharStyle {start, end, style}` |
| Point ↔ paragraph | `graphics.setTextType {type}` |
| Shapes / image | `graphics.newRectangle`, `newEllipse`, `newPolygon`, `newShape {points}`, `newFromFile {path}` |
| Align / distribute | `graphics.alignFrame.<left|hcenter|right|top|vcenter|bottom>`, `graphics.align {to:"frame"}`, `graphics.distribute` |
| Inspect | `graphics.list {clip}` (quad = real bounds in frame pixels) |
| Responsive | `graphics.pin`, `graphics.setResponsiveTime {introFrames, outroFrames}` |
| Roll / crawl | `graphics.setRoll {mode:"roll", startOffScreen, endOffScreen}` |
| Templates | `graphics.template.list/apply {template, values}/export/install` (`.fcgt` only) |
| Fonts | `fonts.list`, `graphics.fonts.used`, `file.replaceFonts` |
| Captions | `captions.newTrack {format:"Subtitle", language}`, `captions.add {text, seconds, durationSeconds}`, `captions.setText/setTimes/split/merge`, `captions.setStyle {font, size, color, background, anchor, margin}`, `captions.import {path}`, `captions.export {path, format:"srt"}` |
| From speech | `transcript.generate` → `transcript.createCaptions {maxChars, lines, minSeconds, maxSeconds}` |
| Caption → graphic | `graphics.upgradeCaption` |
| Burn-in | `file.exportMedia {burnCaptions:true}` |

**Verified gotcha**: `position` is the first-baseline anchor of point text, and the default alignment is left, so `position:[540,500]` in a 1080-wide frame starts the text at the center instead of centering it. Fix: `graphics.set {props:{align:"center"}}` + `graphics.alignFrame.hcenter`. In a test, a centered title at y≈900 also collided with bottom captions: keep titles and captions in separate zones.

## Social caption style (good default)
Bold sans 60–80 px on 1080×1920, white with black stroke or a semi-transparent box, 1–2 lines, max ~32 characters per line, placed around 65–75% of frame height (above platform UI), segments 1–3 s.
