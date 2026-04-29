# Identity Preservation

The #1 failure mode across image models: **face drift** — outputs that resemble the reference but aren't the same person. This file covers how to lock identity on each model family, common breakage patterns, and fixes.

## Per-model identity surface (cheat sheet)

| Model family | How identity is anchored |
|---|---|
| Nano Banana / Nano Banana Pro | Natural-language anchor phrases below + uploaded reference image |
| GPT Image 2 | Natural-language anchor + uploaded reference + cross-image consistency clause |
| GPT Image 1 / DALL·E 3 | Mask-based edit via Images Edit API; weaker preservation |
| Midjourney v6 / v7 | `--cref <url> --cw 100` flag; weight 0–100 |
| Stable Diffusion (SDXL/SD3.5) | IP-Adapter / InstantID / PhotoMaker / PuLID at workflow level |
| FLUX | PuLID-FLUX / FLUX-IP-Adapter at workflow level (community) |
| Imagen 3/4 | `referenceImages` payload with `referenceType: SUBJECT` |
| Ideogram 3 | `style_reference_images` (style only — weaker for identity) |
| Recraft v3 | Trained brand `style_id` (style/brand only — not face) |

The phrases below apply to natural-language models (Nano Banana, GPT Image 2, FLUX, Imagen). For flag-based models, append the model's reference flag instead.

## Anchor Strength Ranking

Ranked by observed fidelity in working prompts:

| Rank | Phrase | Notes |
|---|---|---|
| 🥇 | `The face must be 100% identical to the uploaded image. Do not change the face.` | Strongest. Use for any realistic-person edit. |
| 🥈 | `Keep the facial features of the person in the uploaded image exactly consistent.` | Reliable second. |
| 🥉 | `Same face 100% from the reference image. Preserve facial features, expression, hairstyle.` | Good for aesthetic restyles. |
| 4 | `The person from the attached image (uploaded image facial details).` | Works for Pro; weaker on non-Pro. |
| 5 | `Using the attached reference, same face.` | Weak — only for stylistic remixes. |

**Double-anchor rule:** repeat the anchor at both the top AND near the end of long (>200-word) prompts. Model attention decays in the middle.

## Minimum Edit Preservation Clause

Any edit that should retain the person must include:

```
Preserve entirely unchanged:
- face, facial features, expression
- hairstyle, hair color, texture
- skin tone, pores, natural blemishes
- body proportions, pose, posture

Only modify: {NAMED_REGION}.
```

Omitting `skin tone` causes drift toward lighter/airbrushed skin. Omitting `pose` causes body re-rendering.

## Failure Modes and Fixes

| Failure | Cause | Fix |
|---|---|---|
| Face resembles subject but isn't them | Weak anchor + style pressure | Use top-rank anchor; add `do not stylize the face` |
| Skin becomes airbrushed / too smooth | No texture clause | Add `render natural skin texture with visible pores, not an airbrushed look` |
| Ethnicity drift | No explicit descriptor + strong style ref | Describe skin tone, hair texture, facial structure explicitly alongside the ref |
| Eyes change color or shape | No eye clause | Add `preserve eye color and shape from reference` |
| Hair restyled unexpectedly | Style prompt overrides | Add `keep the same hairstyle, hair length, and color from reference` |
| Age drift (too young / too old) | Style era pressure | Add `keep apparent age consistent with reference` |
| Expression changes | No expression lock | Add `preserve the original expression` OR explicitly set new one |
| Face rendered as cartoon in realistic scene | Medium conflict | Either style whole scene consistent, or add `the face remains photorealistic while the environment is {style}` |

## Multi-Person Preservation

Past 2 named subjects, Nano Banana drifts. Counter with:

```
The people in the uploaded image are named A, B, C (left to right).
Preserve the face of each person exactly as in the reference.
Person A: {distinguishing features to lock identity}
Person B: {distinguishing features}
Person C: {distinguishing features}
```

Describing distinguishing features (glasses, beard, scar, hairstyle) adds a secondary identity signal the model falls back to when face embedding drifts.

## Celebrity Integration

When adding celebrities around a reference subject:

```
Center: the person from the attached image (uploaded image facial details — preserve 100%).
Around them: [NAMED_CELEB_1], [NAMED_CELEB_2], [NAMED_CELEB_3] all recognizable.
```

Gemini has strong celebrity priors — name recognition beats description for public figures. For non-public or private reference subject, always prioritize their identity anchor first.

## Mixed-Style Face Preservation

When body/scene is stylized (chibi / plush / origami) but face is realistic:

```
Transform the person into a {STYLE} character, BUT keep the face photorealistic
and 100% matching the reference. The stylization applies only to body, outfit, and environment.
```

This "face island" pattern works for chibi bodies with real heads, plush toys with 3D-rendered faces, etc. (See Case 66 Stick People Effect pattern.)

## Aging Sequences

```
Generate a {N}-panel grid showing the person from the uploaded image at ages
[LIST: 20, 30, 40, 50, 60, 70].
Preserve core facial structure across all panels — same bone structure, eye shape,
and mouth shape. Only age-appropriate changes: skin texture, hair color (graying progression),
wrinkles, weight distribution. Keep lighting and background consistent across panels.
```

## What NOT to Do

- ❌ Describe the face in abstract terms ("beautiful", "elegant") — replaces identity with an archetype
- ❌ Combine multiple face references without explicit roles — model averages them
- ❌ Use strong era/style anchors without face-preservation clause — style wins
- ❌ Leave skin tone unspecified when requesting a different lighting setup — warm/cool lights shift it
- ❌ Describe new hair/makeup without saying what to preserve — everything gets restyled
