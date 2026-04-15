---
name: seedance-prompts
description: Write production-grade prompts for ByteDance Seedance 2.0 video generation. Use when the user wants to generate videos with Seedance 2.0, needs prompt templates for cinematic/anime/commercial/UGC/short-drama/VFX styles, asks about multi-modal references (@图片/@视频/@audio), shot-by-shot timecoded storyboards, camera move vocabulary, character/scene consistency, or video extension/continuity. Triggers on keywords: seedance, seedance 2.0, 即梦, bytedance video, text-to-video prompt.
version: 1.0.0
source: local-git-analysis
analyzed_repos:
  - github.com/ZeroLu/awesome-seedance
  - github.com/YouMind-OpenLab/awesome-seedance-2-prompts
  - github.com/weshopai/awesome-Seedance-2.0-prompt
analyzed_prompts: ~195
---

# Seedance 2.0 Prompt Engineering

Seedance 2.0 is ByteDance's quad-modal video model: **image + video + audio + text** input. Output: up to 1080p, 4–15s, auto dubbing/scoring. Prompts are high-density storyboards, not one-line descriptions.

## When to Use This Skill

- User asks to write / improve a Seedance 2.0 prompt
- User wants to port a shot idea into Seedance structure
- User mentions multi-shot storyboards, camera moves (Hitchcock zoom, FPV, bullet time), character consistency across shots, video-to-video edits, or audio-driven generation
- User requests a specific style: cinematic, anime, commercial, UGC, short-drama (竖屏), VFX

## Core Prompt Anatomy

Every strong Seedance 2.0 prompt combines 5 blocks. Order is flexible but all blocks matter.

```
[Style]      → genre, film ref, director ref, render engine, resolution, color grade
[Duration]   → total seconds (4–15s); Seedance caps at 15s
[Scene]      → setting, time of day, weather, atmosphere
[Shot List]  → timecoded blocks ([00-05s], [05-10s], [10-15s]) with shot type,
                camera move, subject action, micro-details, dialogue cue
[Tech/Neg]   → aspect ratio, fps, lens, lighting; negatives (optional 排除: block)
```

### Minimum viable template

```
Style: {genre/director ref}, {resolution}, {color grade}.
Duration: {N}s.

[00-Ts] Shot 1 ({shot type}): {camera move}. {subject} {action}.
  Details: {micro-detail}. Dialogue Cue: "{line}"
[T-2Ts] Shot 2 ...
[2T-Ns] Shot 3 ...

Tech: {aspect ratio}, {fps}, {lens}, {lighting}.
```

## Multi-Modal Reference Syntax

Seedance accepts explicit reference tags inline. Use sparingly — one ref per asset.

| Tag | Meaning | Example |
|-----|---------|---------|
| `@图片1` / `@Image 1` | Reference image 1 (identity, style, composition) | `参考@图片1的男人形象` |
| `@视频1` / `@Video 1` | Reference video (camera move, action, transition) | `完全参考@视频1的所有运镜效果` |
| `@audio1` | Audio drives rhythm/BGM | `BGM参考@视频3中的音效` |

Reference chaining in a single prompt is supported — e.g. identity from image, camera from video, music from audio: `参考@图1的男人形象，他在@图2的电梯中，参考@视频1的运镜`.

## Three Generation Modes

| Mode | When | Key idiom |
|------|------|-----------|
| **Text-to-Video** | No input asset | Full storyboard + style block |
| **Image-to-Video** | Product / character / scene provided | `@图片1` anchors identity; describe motion only |
| **Video-to-Video** | Remix / extend / edit | `@视频1` anchors motion or style; describe delta (`将...换成...`) |

## Category Catalog

Detailed templates and examples for each category live in `references/`.

- `references/patterns.md` — structural patterns + idioms mined from 195+ prompts
- `references/templates.md` — fill-in templates per category (cinematic, anime, commercial, UGC, short-drama, VFX, sound, consistency, camera, extension)
- `references/camera-vocab.md` — camera moves, lens, lighting, grading vocabulary
- `references/examples.md` — curated working prompts with source attribution

## Quick Rules

1. **Always timecode shots.** `[00-05s]` blocks → Seedance's temporal alignment is shot-based, not descriptive.
2. **Three shots is the sweet spot** for 15s. Five max. More → drift.
3. **One action per second.** Don't pack; over-dense shots desynchronize.
4. **Director/film refs work.** `Denis Villeneuve style`, `Wong Kar-wai 90s Hong Kong`, `Hans Zimmer score` → strong tonal anchors.
5. **Dialogue cues inline** with lip-sync intent: `Dialogue Cue: "line" (200-400ms pauses)`.
6. **Aspect ratio matters.** `9:16` for vertical short-drama / TikTok, `2.35:1` for cinematic, `16:9` default.
7. **Negative prompts use 排除:** (Chinese-native pattern) — `排除：模糊，低清，噪点，水印，文字，扭曲变形，五官崩坏`.
8. **Character consistency** → repeat identity anchor in each shot (`同一人物`, `maintain consistent face/clothing/hair`).
9. **For extension/continuity** → end shot N with exact state, start shot N+1 from that state (pose, lighting, framing).
10. **Audio drives rhythm** — if using `@audio`, beat-align actions (`beat-synced`, `与音乐节拍完全吻合`).

## Anti-Patterns

- One-line descriptions → Seedance under-performs vs shot-list format
- Mixing Chinese and English mid-sentence without commas → parser trips
- More than 2 reference tags per shot → identity conflict
- Abstract emotion-only prompts (no visual action) → static output
- Over-specifying > 8 micro-details per shot → model drops some

## Workflow

1. Ask user: style, duration, assets on hand (images/videos/audio)
2. Pick closest template from `references/templates.md`
3. Fill 3-shot storyboard with timecodes
4. Add style header + tech footer + (optional) negative block
5. If references exist, insert `@图片N` / `@视频N` tags
6. Output prompt in a single fenced block — user pastes into Seedance
