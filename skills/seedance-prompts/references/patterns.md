# Structural Patterns

Mined from 195+ working Seedance 2.0 prompts across three awesome-lists.

## The 5-Block Structure

Every high-quality prompt contains these blocks, often bracket-tagged:

```
[Style]        → Cinematic genre, director/film ref, render engine, 4K/8K, grading
[Duration]     → 10s or 15s (Seedance cap)
[Scene]        → Location + time + weather + atmosphere
[Shot N]       → Timecode block (see Shot Block Pattern below)
[Technical]    → Lens, fps, aspect ratio, lighting, color
```

Some authors use headers (`[Style]`), others inline prose. Both work. Brackets improve parseability in complex prompts.

## Shot Block Pattern

The strongest recurring structural unit:

```
[T1-T2] Shot N (Shot Type):
  Camera Position: {angle, height, distance}
  Camera Move: {push-in, dolly, orbit, handheld, FPV, bullet time}
  Action: {subject does what}
  Details: {micro-expressions, textures, physics, lighting interaction}
  Dialogue Cue: "{line}" ({emotion/pacing note})
  Sound: {ambient + FX + beat note}
```

Shortened inline form:

```
[00:00-00:05] Extreme Wide Shot (The Scale). A colossal sandstorm ... Hans Zimmer style tension.
```

## Timecode Idioms

Three equivalent formats appear across the corpus. Pick one, stay consistent.

| Format | Example | Feel |
|--------|---------|------|
| Bracketed | `[00-05s]` `[05-10s]` | Fast, cinematic |
| Colon | `[00:00-00:05]` | Precise, pro-storyboard |
| Chinese | `0-4秒画面：` `4-8秒画面：` | Native CN prompts |

Sub-second beats are valid: `0.3 seconds` micro-action mid-shot → `gently biting her lower lip, her cheeks and earlobes instantly bloom with cherry blossom pink`.

## Style Anchoring Idioms

High-leverage anchors that measurably shift output quality:

- **Director refs**: `Denis Villeneuve Style`, `Wong Kar-wai Film Style`, `Christopher Nolan IMAX`
- **Film refs**: `Le Mans Style`, `Blade Runner 2049`, `In the Mood for Love`
- **Render engine**: `Unreal Engine 5 fluid rendering`, `Octane render`
- **Film stock**: `IMAX 70mm Film`, `retro film grain`, `high ISO grain`
- **Camera gear**: `Sony A7S3`, `Arri Alexa`, `2.35:1 wide-screen`
- **Grading**: `desaturated`, `ambiguous yellow-green tint`, `silver-blue tonal`
- **Score composer**: `Hans Zimmer style tension`, `Joe Hisaishi piano swell`

## Character Consistency Idioms

Chain-of-identity tokens that hold a subject stable across shots:

- `characters maintain consistent faces, clothing, and hairstyles throughout without deformation, drift, or artifacts`
- `同一人物` (same character) — CN shortform
- `Character identity is maintained throughout`
- For referenced input: `参考@图片1的男人形象` (reference man-identity from image 1)
- Pair with physical anchors: specific clothing, hair, accessory — `dark blue linen outfit`, `wooden hairpin`, `loose school uniform collar`

Reinforce in **each shot** if drift observed.

## Multi-Modal Reference Syntax

```
@图片1 / @Image 1   → identity, composition, style anchor
@视频1 / @Video 1   → camera move, action rhythm, transition style
@视频3 / @audio1    → BGM, SFX, rhythm reference
```

Chained example (from repo3 Consistency #3):

```
使用参考图片人物的形象生成一段古装穿越剧的预告短片
```

Complex chain (from repo3 Camera #1):

```
参考@图1的男人形象，他在@图2的电梯中，完全参考@视频1的所有运镜效果还有主角的面部表情
```

Rule: **one conceptual role per reference** — don't mix identity and camera in the same `@tag`.

## Dialogue + Lip-Sync Pattern

When Seedance needs to speak, spell out emotion and timing:

```
Dialogue Cue: He gives a subtle nod and mouths "Let's go."
```

```
Lip synchronization is natural and precise, emotional micro-tremors and breathing
are synchronized, dialogue is low-energy whispering with a shy tone, natural short
pauses between 200-400 milliseconds.
```

Key phrases that work:
- `mouths "..."` (silent mouthing)
- `whispers "..."`
- `stutters in response, "..."`
- `(Subtitle: ...)` for on-screen text

## Sound Design Pattern

Sound blocks follow structure: **ambient → FX → dialogue tone → score**.

```
Overall Sound Effects: Distant summer cicada chirping faintly, the soft scratching
sound of the pen touching the paper, the almost inaudible low-frequency pulse of
their heartbeats, finally fading into a very light, airy piano.
```

For audio-driven (`@audio1`): `beat-synced`, `与音乐节拍完全吻合` (perfectly matched to beat).

## Negative Prompt Idiom (CN)

Native Chinese negative block. Use at prompt tail:

```
排除：模糊，低清，噪点，水印，文字，logo，扭曲，变形，五官崩坏，动作僵硬，画面抖动，比例失调
```

English equivalent is rarer but valid:

```
No text, watermarks, or subtitles. No facial deformation, drift, or artifacts.
```

## Aspect Ratio + Orientation

| Aspect | Use case | Cue phrase |
|--------|----------|------------|
| `16:9` | Default cinematic | (implicit) |
| `2.35:1` | Ultra-wide cinematic, 24fps | `cinematic 2.35:1` |
| `9:16` | Short-drama, TikTok, IG Reels | `画面比例为9:16` / `Vertical Format` |
| `1:1` | Social, ads | `square format` |

## Recurring Action Verbs

Verbs that Seedance handles cleanly (high-signal):

- Motion: `accelerates`, `launches into the air`, `spins frantically`, `plunges`
- Camera: `push-in`, `pull-back`, `orbits`, `tracks`, `whip-pans`, `tilts`, `racks focus`
- Subject: `mouths`, `whispers`, `freezes`, `gazes`, `turns slowly`, `collapses`
- Environment: `lashes` (rain), `swallows` (storm), `bleeds and dissolves`

## Dense Multi-Clause Rhythm

Top-tier prompts stack comma-separated clauses per line:

```
A pure girl in a summer school uniform is focused on writing notes with her head
down, long black hair and stray hairs by her ears are gently lifted by a slight
breeze, long eyelashes cast subtle shadows, skin is naturally pink and tender, a
slight unintentional upturn of the corner of her mouth in concentration, light
and even breathing.
```

Pattern: `subject + gerund-action, body-part + micro-motion, sensory detail, emotional tell, breath/heartbeat note`.

## Sub-Genre Markers

Quick-look labels recurring across the corpus:

| Sub-genre | Marker phrases |
|-----------|---------------|
| Hollywood racing | `Le Mans Style`, `Cinematic Night, Rain, High Stakes Sport` |
| Denis Villeneuve SF | `IMAX 70mm, Gritty Realism, Epic Scale, Desaturated` |
| HK 90s art cinema | `90s Hong Kong Art Cinema, retro film grain, yellow-green tint, frame stepping` |
| Japanese romance | `pure love ambiguous short film, warm golden sunlight, shallow DOF, cherry blossom` |
| Chinese short-drama | `竖屏 (vertical), 霸道总裁 (CEO-style), 9:16, rainy night emotional` |
| Anime battle | `Figure 1 vs Figure 2, motion lines, speed blur, impact frames` |
| Modern rural ASMR | `Sony A7S3, Extreme Macro, natural transparent lighting, healing ASMR` |
| Haute couture fantasy | `Unreal Engine 5 fluid rendering, 8K, visual illusion, liquid porcelain` |
