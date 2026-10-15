# Category Templates

Fill-in templates for each Seedance 2.0 prompt category. Replace `{…}` placeholders.

---

## 1. Cinematic Film Style (Hollywood/Director Ref)

```
Style: {Director} Style, {genre} (e.g. Gritty Realism, Epic Scale), {film stock} (e.g. IMAX 70mm), {grading} (e.g. Desaturated).
Duration: 15s.

[00-05s] Shot 1 ({shot type, e.g. Extreme Wide Shot}): {scene establishing, scale cue}. {Hans Zimmer / Joe Hisaishi style score note}.
[05-10s] Shot 2 (Interior/Cockpit Cam): {character POV, panic/determination}. {Camera shake note}. Dialogue Cue: "{line}" (Subtitle: "{translation}").
[10-15s] Shot 3 (Climax / Slow Motion): {peak action}. {Lighting/debris detail}. Cut to {black / title card} on impact.
```

Proven refs: `Le Mans Style`, `Denis Villeneuve Style`, `Wong Kar-wai 90s Hong Kong Art Cinema`, `Christopher Nolan IMAX`.

---

## 2. Commercial / Brand Advertising

Simplest form (pure text brief):

```
Generate a promotional video for {brand}. Style: {brand aesthetic, e.g. MUJI minimal Japanese}. Duration: {N}s. Tone: {warm / aspirational / bold}.
```

Product-anchored form (image ref):

```
Based on @Image 1 script and @Image 2 product, generate advertising content for {product category}.
Voiceover: {natural female/male voice, language}. Keep {product} bottle/packaging proportional, integrated with natural lighting. Avoid heavy texture overlay and cutout effects. Pace: {brisk / contemplative}.
```

---

## 3. Social / Viral Meme Style

```
Style: {meme reference, e.g. Giant Orange Cat, absurdist scale}. Duration: 8–10s.
Scene: {ordinary setting} with {oversized/surreal element}.
Action: {subject} {unexpected action}. Camera: {static locked-off OR shaky handheld} for comedic effect.
Punchline beat at [T-1s]: {reveal / reaction}.
```

---

## 4. UGC / Surrealistic Documentary

```
Style: Handheld UGC / Phone camera aesthetic, {slight motion blur, natural lighting}. Duration: 10s.
[00-03s] Setup: {mundane shot, shaky cam}. {Subject} starts {normal activity}.
[03-07s] Break: {surreal element intrudes}. Subject reacts naturally.
[07-10s] Acceptance: {subject treats it as normal}, camera keeps rolling.
Audio: Natural room tone, no music, occasional off-camera voice.
```

---

## 5. Anime / Animation Style

```
Style: {anime tradition, e.g. 90s Shonen, Studio Ghibli, Motion Graphics, Van Gogh Post-Impressionism}. Duration: 10–15s.

[00-05s] Shot 1: {Character A} {action}. Motion lines, impact frames, speed blur. {Sound cue: "whoosh", "zing"}.
[05-10s] Shot 2: {Character B} counters. {Effect: ice/fire/lightning aura}. Camera: whip-pan to close-up.
[10-15s] Shot 3: Clash. {Character A vs B} collide mid-air. Screen splits, time freezes, then explosion.
```

Specific subtypes:
- **Mech battle**: `Otter Mecha vs Octopus. Scale contrast, parts flying, pilot close-up.`
- **Space-time folding**: `Nezha and Ao Bing ice-fire clash with Space-Time Folding effect.`
- **Comedy scene**: `Luffy coding on MacBook. Straw-hat costume + modern setting incongruity.`

---

## 6. Chinese Short-Drama (竖屏 Vertical)

```
Style: Chinese Mini-Drama Style (霸道总裁 CEO drama), Vertical Format, 9:16, high contrast colors, intense close-ups.
Duration: 15s.
画面比例：9:16

[00-05s] 特写: {female lead}, 雨夜, 眼含泪光 ({rainy night, tears}). Dialogue Cue: "{emotional line}".
[05-10s] 反打: {CEO male lead} 冷峻表情, 西装 ({stern CEO in suit}). Dialogue Cue: "{commanding line}".
[10-15s] 双人同框, 雨中对峙 ({two-shot, rainy standoff}). Slow pull back. 片尾标题: "{drama title}".

排除：画面模糊，低清，比例失调。
```

---

## 7. VFX / Experimental / Surrealism

```
Style: {Megalophobia / Surrealism / Liquid physics / Dimensional dissolve}, 8K Photorealistic, Unreal Engine 5 fluid rendering, visual illusion.
Duration: 15s.

[00-05s] Entry: Physical-seeming scene. {Subject} in {normal space}. Subtle uncanny tell.
[05-10s] Rupture: {Physical law breaks — liquid porcelain shatters into ink swallows, gravity reverses, scale inverts}.
[10-15s] Dissolve: {Scene melts into abstract vortex}. Camera plunges into {void / ink / light}.
```

---

## 8. Sound-Driven (Audio Reference)

```
{Scene description}. 背景BGM参考@视频3中的音效. 旁白参考@视频1的音色. {Action beat-synced to audio rhythm}.
```

English form:

```
{Scene description}. BGM references @audio1. Voiceover tone matches @video1. Action is beat-synced, with cuts landing on downbeats.
```

---

## 9. Character / Scene Consistency

Hard anchor pattern (most reliable):

```
使用@图片1的人物形象，生成{N}秒短片。
参考@图片1人物的: 面部特征, 发型, 服装, 身材比例 — 全程保持一致。
[00-04s] {Shot 1 with identity anchor repeated}.
[04-08s] {Shot 2 with identity anchor repeated}.
[08-12s] {Shot 3 with identity anchor repeated}.
```

English:

```
Using the character from @Image 1, generate a {N}-second clip.
Identity anchor: {facial features, hair, clothing, body proportions} — maintained across all shots.
Shot 1 ... {identity repeated}
Shot 2 ... {identity repeated}
```

### 9b. Reference Image Identity Lock (token + inherit / do-not-inherit)

Stronger, more explicit variant for any clip where a face, outfit, product, or UI layout must survive across shots (works for Seedance 2.0 and 2.5; 2.5 also accepts audio/video references under the same token scheme).

```
Token: @image1 = {role, e.g. "the woman", "the product", "the UI layout"}

INHERIT from @image1: {enumerate — identity, facial features, face shape, skin tone,
apparent age, hairstyle, hair color, height, build, body proportion, clothing
(each garment named), footwear, accessories, overall bearing}.

DO NOT INHERIT from @image1: {background, room, furniture, original pose,
camera angle/framing, original lighting, any text in the reference}.

Cross-shot clause: same face when turning, looking down, speaking, or with a
hand near the face — identity drifts hardest during head turns, occlusion,
and fast motion, so call those poses out explicitly.

Negative: no cloning, no duplicate subjects, no feature averaging, no
attribute swaps between characters.
```

Rules:
- One token per reference role (`@image1`, `@location1`, `@hands1` — never let one token double as two roles).
- Always pair an inherit list with a do-not-inherit list — without the second list, the reference's background/pose/lighting leak into the generated shot.
- For a sketch/illustration reference, add an explicit render instruction (`use only as a design blueprint, render as fully realistic live-action humans`) or the line-art survives into the video.
- Lock identity **once** in a fixed block, not inside every shot — repeating it per-shot is what triggers mutation between shots (see Quick Rules in SKILL.md).

---

## 10. Precise Camera Movement (Video Ref)

```
参考@图1的{主角形象}, 场景在@图2, 完全参考@视频1的所有运镜效果还有主角的面部表情.
Camera moves in order:
1. {Push-in to close-up}
2. {Hitchcock zoom on fear beat}
3. {360° orbit around subject}
4. {Exit through doorway, tracking}
5. {High-angle crane pull-back}
```

Camera-ref signature phrases:
- `完全参考@视频1的所有运镜效果` — copy all camera moves from video1
- `机械臂多角度跟随` — robotic arm multi-angle follow
- `希区柯克变焦` — Hitchcock zoom (dolly zoom)
- `鱼眼镜头` — fisheye lens

---

## 11. Video Extension / Continuity

```
Continue @视频1 seamlessly. Starting state: {exact pose, framing, lighting from last frame of @视频1}.
Next 10 seconds:
[00-04s] {logical next beat, maintain all visual continuity}.
[04-08s] {develop action}.
[08-10s] {land on new stable frame OR loop back to start frame for seamless loop}.
Maintain: {lighting direction, color grade, character identity, camera style}.
```

---

## 12. Video Edit (Character Replace / Add / Delete)

```
将@视频1中的{original subject}换成{new subject}, 场景保持不变, 参考@视频1的运镜和转场效果, 利用镜头匹配人物的动作.
```

English:

```
In @video1, replace {original subject} with {new subject}. Keep scene, camera moves, and transitions identical. Match new subject's motion to original keyframes.
```

Add/delete variants:

```
在@视频1中添加{new element} 在{specific location}. 其他保持不变.
删除@视频1中的{element}. 自然补全背景.
```

---

## 13. Music / Beat-Synced

```
Style: {dance/MV/montage}. Duration: {N}s. Beat-synced to @audio1 / {BPM note}.
Cut pattern: Every {0.5s / 1 beat / 2 beats}. 
Action lands on: downbeats.
Camera: {whip-pan on snare, push-in on drop}.
```

---

## 14. Emotion (Micro-Expression Focus)

```
Duration: 10s. Extreme close-up on {character}'s face throughout.
[00-03s] Baseline expression: {neutral / guarded}. Breathing {slow / shallow}.
[03-06s] Trigger: {subtle stimulus — a letter opens, a sound off-camera, memory flash}. Micro-expressions: {pupil dilate, jaw tense, lip quiver 0.3s}.
[06-10s] Release: {single tear / slow smile / eyes close}. Sound fades to silence.
Technical: shallow DOF, Rembrandt lighting, slow push-in 2–3mm over entire shot.
```

---

## 15. Hybrid Multi-Modal (Full Stack)

```
[Identity] @图片1 男人形象
[Scene] @图片2 电梯
[Camera] 完全参考@视频1的运镜
[Audio/BGM] @视频3的音效
[Action]
  [00-05s] 男人走进电梯, 希区柯克变焦
  [05-10s] 电梯门关闭, 360°环绕, 表情惊恐
  [10-15s] 门开, 跟随走出至@图片3场景, 环顾四周
[Tech] 16:9, 24fps, 电影级调色, 2.35:1可选
排除：模糊, 变形, 五官崩坏
```

This is the "power-user" form — combines all 4 modalities (image × 2, video × 2, text). Use sparingly; over-chaining references causes drift.

---

## 16. POV / Continuous Take (Bodycam, FPV, GoPro)

```
SCENE CONTEXT: {subject}, {mount — chest-mounted / helmet / handlebar}, {total duration}.
ACTIVE REFERENCES: @location1 = {place}, @hands1 = {forearms, tools, gear}.
LOCATION MAP: foreground/midground/background per segment, camera height = {POV chest-to-eye height}.
FIRST FRAME: non-empty opening frame — already mid-action (e.g. "already mid-cast, rod raised").
FORMAT MODE: {A: 0-Ns {location}, one continuous take, HARD CUT} {B: N-Ms {location}, one continuous take}. Camera cuts nowhere else.
OPTICS: FOV {X}° easing to {Y}° through {beat}. No drift within any segment.
Camera itself is never visible. {Left/right} hand holds {what}.
Audio: {diegetic sounds only, tied to the mount}.
```

Signature rules: declare the mount + height so shake is implied, not described; refuse an empty first frame; pin FOV in degrees per segment with a no-drift clause; ban cinematic treatment explicitly (`no slow-motion, no cinematic grading`) or bodycam footage turns into a movie trailer.

---

## 17. Retro Found Footage (Early-2000s DV / VHS Home Video)

```
{Duration}, {resolution}, early-2000s DV home-video format{, reference image if any}.
MAIN SUBJECT: {age, hair, full outfit}. Maintain the same face, hairstyle, clothing, body proportions.
SETTING: {specific lived-in neighborhood/room with clutter — potted plants, utility poles, laundry}. No tourist attractions, ads, recognizable brands.
CAMERA: autofocus hunting, exposure shifts, accidental zooms, drifting composition, occasional accidental face cropping. No stabilization, drone footage, gimbal movement, cinematic moves.
[Beat 1] {one small incident — not a plot}. "{short spoken line, <1 sentence}"
[Beat 2] {reaction / continuation}.
AUDIO: location sound only (footsteps, insects, ambient). No music.
Tail: hard cut to black.
```

The period feel comes entirely from the camera-defect list, not from "low quality" — piling on 4K/cinematic lighting kills the DV feel. Give one small event ~6s of screen time rather than cramming several; props must not vanish or duplicate between beats.

---

## 18. Pets & Animals as the Lead

```
Reference: {person, if any, locked via @image1}. Subject: exactly ONE {animal}, the same one throughout. No duplicate animal.
Format: {duration}, vertical 9:16, handheld front-camera selfie, indoor daylight, no grading, no beauty filter.
Camera: arm drift, imperfect framing, autofocus hunting, no cuts, no zoom, no third-person operator.
[00-Ns] {animal notices → reaches → steals/climbs → attacks the lens}, one escalating beat at a time.
Human reaction: {half-finished line, e.g. "You little—"}.
Audio: {on-set animal sounds + ambience only}. No background music, no subtitles.
Negative: exactly one person, exactly one animal, no duplicate reflection, no human-like walking/talking for the animal.
```

Keep the animal behaving like an animal (no talking, no human clothing/gait) — the joke/charm comes from real animal behavior, and the payoff lands on the lens, not on a punchline line.

---

## 19. Stop Motion / Stepped Cadence (Claymation, Paper-cut, Tabletop)

```
Cadence: True {12}fps, ANIMATED ON TWOS — {N} distinct hand-{painted/sculpted} poses per second, each held {2} frames then snapping to the next, never gliding.
Material: {hand-painted 2D / clay / paper-cut / moving oil painting}. NOT {excluded adjacent materials — clay, puppets, 3D}.
Negative (mandatory trio): NO smooth interpolation, NO motion blur, NO morphing.
Camera/surface: {locked top-down overhead OR locked stage}, no camera movement, no hands, no surrounding objects — only the subject changes.
[Segment 1] {transformation step}. [Segment 2] {next step}.
Craft imperfections: uneven handmade edges, tiny positional jitter between poses, occasional one-frame motion smear, constant painterly boil in outlines.
```

Separate environment motion from subject motion explicitly if background elements (smoke, water, haze) should drift smoothly while the subject steps on twos — otherwise everything smooths out together. Don't mix two craft materials in one prompt; don't combine stop-motion with a long moving-camera shot.

---

## 20. Game UI / Livestream HUD Overlay

```
Format: {duration}, {aspect ratio}, fixed full-screen game HUD throughout — genuinely gameplay, not a cinematic film.
Character lock: @image1 = face/identity only; outfit written out in text.
Screen layer spec (fixed positions, HUD only changes VALUES, never layout):
  top-left: {stamina/health bar} | top-center: {objective banner, 2-4 capitalized words}
  top-right: {date/score} | bottom-left: {minimap} | bottom-right: {button prompts / facecam}
Camera rig: third-person follow, {distance}m behind subject, FOV breathing {X}-{Y}°. (Or: one locked camera for desktop recordings.)
[00-Ns] {action beat} — HUD updates: {e.g. ammo 24/120 → 14/120}.
Cast: exactly {N} {enemy type}, no extra armed characters. Streamer/hero appears only in the facecam, never duplicated via reflection.
Audio: engine/footsteps/keyboard, ambience, voice language {X}, HUD text language {Y}.
Strict tail: no cuts, no transitions. If a close is needed: exactly one hard cut at {Ns}, no black screen, no end card.
```

Garbled text is the main failure mode — keep HUD banners to 2-4 capitalized words and numbers in a simple `N/M` pattern.

---

## 21. Fashion Lookbook / Portrait Film

```
Header: {aspect ratio}, {exact duration}, genre = {fashion campaign / Vogue editorial / cinematic portrait}, {cutting pace}.
Person & look lock: face, hair, makeup, jewelry, then every garment/shoe/bag named — identical in every scene.
Hero item lock: {material, color, hardware}, how it's carried (e.g. "hanging naturally on arm throughout all scenes").
Scene chain:
  Scene 1 · {N}s {shot size} — {place}. {one gesture}.
  Scene 2 · {N}s {shot size} — {place}. {one gesture}.
On-screen type (optional): one short line (≤2 words) under the scene it belongs to.
Closing hero beat: everything slows, camera orbits/pushes onto the hero item, last move tilts up to the face.
Visual direction: {lens, e.g. "Canon EOS R5 35mm f/1.4"}, {film tone}, grain. No plastic skin, robotic movement, stiff poses, watermarks.
```

One shot size + one place + one gesture per scene; packing three actions into a 3-second scene is the most common failure.

---

## 22. Food ASMR / Cooking

```
Opening: {duration}, look = {anime film / glossy commercial / handheld vlog}, exact dish = {dish}.
Style/light: macro close-ups, shallow DOF, steam, warm light{; for vlogs: camera device + its flaws}.
[If a person is in frame] Identity lock + outfit + room/street.
Timeline by step (one action + one texture change per segment, 2-3s each):
  [Step 1 — {name}] {raw state → first visible change}.
  [Step 2 — {name}] {...}.
Hero ending: finished dish alone, slow push-in or arc, steam rising.
Audio: {music style/tempo}, then cooking/eating sounds in the order they happen (knife, sizzle, bubbling, chewing).
Negative tail: no unrelated ingredients/dishes — {dish} only. No text, UI, logos. Food/hands/utensils stay consistent.
```

Let the subject bite → chew → swallow before speaking (talking with a full mouth breaks lip-sync and the chewing animation); give each cooking step its own timecode rather than packing several into one paragraph.

---

## 23. Horror & Suspense

```
Header: {runtime}, genre named explicitly, reference lock on whoever turns first.
[Shot 1, timecoded] Patient zero in an ordinary setting, already carrying ONE symptom. Face/outfit matching reference.
[Shot 2] {+1 visible change only — e.g. "dark veins emerging beneath the skin"}.
[Shot 3] {+1 more change — e.g. "eyes cloud milky white"}.
[Trigger shot] The attack itself, slow motion, with impact.
[Transmission] Bitten person runs the same escalation on a shorter clock.
[Crowd/barricade] Panic beat — door, luggage, hands clawing through glass.
[Closing shot] A sealed door still shuddering / a wide exterior. Nothing resolved.
```

One visible change per shot (never cram a whole transformation into one shot); the scare lands harder on someone else's reaction (a bystander stirring) than on gore volume; put the identity/consistency lock in Shot 1 — by the closing shots it's too late.

---

## 24. Process / Transformation Montage

```
Invariants block: {camera position/angle/focal length/perspective/composition} fixed. {Room dimensions/walls/layout} fixed — nothing moves that shouldn't.
Initial state: {concrete description}.
[Segment 1] {change, ordered spatially — e.g. "flooring spreads left to right"}.
[Segment 2] {next change, e.g. "walls and ceiling transform simultaneously"}.
[Segment 3] {furniture/details land}.
Final state + life-signs beat: {something still moves — water shimmers, a light turns on} — never end on a fully static freeze.
Sound: assembly clicks, ambience{, dialogue if any}.
```

If two reference images define different things (e.g. a floor plan vs. an exterior style photo), say explicitly which one controls what. Don't move the camera during the transformation — any camera motion competes with the change itself and the viewer loses the before/after anchor. Cap at ~6 steps per generation; split and stitch beyond that.

---

## 25. Storyboard Grid → Video (Two-Stage)

Stage 1 — image prompt (generate a single-page panel sheet first):

```
Single-page storyboard sheet, {aspect ratio}, {N} panels, style = {premium storyboard / infographic poster / rough pencil previs}.
Info card: TOTAL VIDEO TIME: {N}s · {M} SHOTS (recount in footer: {M} shots × {N/M}s = {N}s).
Panel list (one line each): {shot size} — {action already in motion, not a static picture}.
Tail: no timestamps baked into the art, no extra characters, no watermark.
```

Stage 2 — video prompt (feed the sheet back in as a reference):

```
Image1 = EXACT character reference (face/identity only). Image2 = EXACT storyboard design/layout reference.
Do not copy pose/layout from Image1 — storyboard (Image2) controls locations, actions, compositions, sequence.
Rules: follow panels 1→{M} in order. One shot per panel, ~{N/M}s each. No skipped/added steps. Character and set stay identical throughout.
Overall look: {lighting, camera movement}. Audio: {direction}. No subtitles, no watermark.
```

Work backwards from runtime at 1.5–3s per panel; every panel must show something already in motion (a static panel renders as a slideshow beat).
