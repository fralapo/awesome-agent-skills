# 14 — Compositing techniques (Lesson 14)

Summary in my own words; `ultra_key` and opacity blend modes verified.

## Concepts
- **Alpha channel**: besides RGB, a fourth channel describing opacity. Graphics and some codecs (ProRes 4444, PNG) carry it; it can be straight or premultiplied, and can be ignored or inverted via interpretation.
- **Plan for compositing when shooting**: even, flat light on the green/blue screen, subject well away from it to avoid spill, sharp focus, high bit-depth low-compression recording, no motion blur if possible.
- **Opacity**: rubber band or keyframes to fade layers; **blend modes** (multiply, screen, overlay, soft light, add…) combine tracks by luminance/color math.
- **Keying**: making pixels transparent by color (chroma key) or brightness (luma key). **Ultra Key**: pick the key color, then refine matte (transparency, highlight, shadow, tolerance, pedestal), matte cleanup (choke, soften, contrast) and spill suppression. Check the matte view (alpha) for holes and grey noise.
- **Garbage mattes / partial masks**: cut away rigging or edges of the screen with a mask before or after keying.
- **Track Matte Key**: uses another track (text, shape, video) as the matte by its alpha or luma; effects on the matte track affect the result.
- Object Mask (AI rotoscoping) is absent in FilmCraft: use bezier masks + tracking, or EffectCraft for heavy roto.

## FilmCraft
| Task | Command / effect |
|---|---|
| Opacity / keyframes | `effects.setParam {effect:"opacity", param:"opacity", value, time, keyframe}` |
| Blend mode | `effects.setParam {effect:"opacity", param:"blend", value:"Screen"}` (name or index; "Screen" = 8) |
| Alpha interpretation | `clip.interpretFootage`, effect `alpha_adjust {ignore, invert}` |
| Chroma key | `ultra_key {key_color:"#00b140", output, setting, transparency, tolerance, choke, soften, spill…}` |
| Other keys | `color_key`, `luma_key`, `logo_cutout`, `extract` |
| Track matte | `track_matte {matte:<track>, composite:"alpha"|"luma", reverse}` |
| Garbage mask | `masks.add {effect:"opacity", shape:"polygon", path}` + `masks.set {inverted}` |
| Edge help | `edge_feather`, `stroke`, `drop_shadow`, `choke` in ultra key |
| Export with alpha | preset "Apple ProRes 4444 with Alpha" or `exportMedia {alpha:true}` |

## Recipe: green screen
1. Background on V1, keyed clip on V2.
2. `effects.apply ultra_key` → `setParam key_color` (sample hex of the screen) → `setting` preset → adjust choke/soften small, spill up until the edges lose green.
3. Garbage mask on opacity for rigging; `render_frame` on hair/edges at 2–3 times.
4. Match the foreground to the background with `lumetri` (temperature, contrast), add a light `drop_shadow` or `gaussian_blur` on the background for depth.

> Availability notes in this file are a snapshot as of 2026-11-03. ArtCraft apps update almost daily: re-check the live command catalogue before treating anything as missing.
