# Seedream 5.0 (ByteDance)

ByteDance's flagship text-to-image model — sibling of Seedance for video. Strong photorealism, native CJK text rendering, and rapid iteration via Doubao / Jimeng / Volcano Engine.

Cited as a first-class target by the YouMind ai-image-prompts-skill alongside Nano Banana Pro, GPT Image 2, Midjourney, FLUX, SDXL.

## Tier

- **Seedream 4.0 / 4.5** = Standard
- **Seedream 5.0** = Pro — top-tier photorealism, robust CJK + Latin typography, improved prompt adherence

## Syntax surface

- **Natural-language prose**, no flags, no weight syntax
- **Aspect ratio** via API param `image_size` or `aspect_ratio` (`1:1`, `9:16`, `16:9`, `4:3`, `3:4`, `2:3`, `3:2`)
- **Negative prompt** via `negative_prompt` API param
- **Reference image** via `reference_image` URL or upload (style + composition transfer)
- **Watermark** auto-applied on Doubao/Jimeng UIs unless API is used with watermark off
- **Seed** for reproducibility

## Best-in-class for

- Photorealistic Asian-faces portraits (large training-data home advantage)
- Dense Chinese typography (menus, posters, calligraphy, brand mockups)
- Mid-autumn / Lunar New Year / festival branding work
- E-commerce hero imagery for Douyin / Tmall / Taobao listings
- Lifestyle photography with East-Asian urban environments (Shanghai, Tokyo, Seoul)

## Weak points

- Western pop-culture priors weaker than Midjourney / GPT Image 2
- Long English headlines on Seedream 4.x — drift past ~12 words; better on 5.0
- Style-reference fidelity below Midjourney `--sref` (no equivalent flag exists)

## Anatomy template (prose form)

```
A <medium> of <subject> doing <action> in <environment>.
<wardrobe + props>. <lighting: key + rim + mood>. <camera: lens + angle>.
<style ref: era / film / movement>. <color palette>.
<aspect ratio sentence>.
<for typography: literal text in double quotes — Chinese or English>.
```

## Anti-patterns

- Mixing `--ar 16:9` MJ flags — parsed as text
- Mixing `(token:1.3)` SD weights — parsed as text
- Embedding very long English headlines on Seedream 4.x — switch to 5.0 or Ideogram

## Output target

Doubao (consumer chat), Jimeng (consumer image gen), Volcano Engine API (`text2image_v2`/`seedream-v5`), fal.ai (where available), Replicate (where available).

## See also

- `nano-banana.md` — sibling Pro-tier natural-language model
- `gpt-image-2.md` — when you need the strongest CJK + multi-panel consistency
- `../patterns.md`, `../templates.md`
