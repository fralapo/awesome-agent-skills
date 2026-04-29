# GPT Image 2 (OpenAI, codename "duct-tape")

OpenAI's next-gen image model — significant leap over GPT Image 1 / DALL·E 3 in text rendering, cross-image consistency, commercial-grade illustration, and multilingual (CJK + Latin) typography. **GPT Image 1.5** is sometimes referenced as an intermediate tier between GPT Image 1 and 2; treat its prompt grammar as the same natural-language surface, with text/consistency capabilities sitting between the two.

Source repos: `ZeroLu/awesome-gpt-image`, `YouMind-OpenLab/awesome-gpt-image-2`, `EvoLinkAI/awesome-gpt-image-2-prompts`. ~5500 prompts analyzed.

## What it's best at

- **Pixel-perfect text rendering** — Chinese, English, Japanese, Korean, mixed-script in one image, no warped glyphs or typos
- **Cross-image consistency** — same character / style / IP stays identical across a series, down to wardrobe
- **Commercial-grade illustration** — output ready to ship without manual polish
- **True art-style induction** — evokes the *feel* of a style, not just surface approximation
- **Multi-panel storyboards & product series** — multi-panel comics, character expression sheets, exploded-view product diagrams
- **Multi-language design** — social cards, banners, posters with accurate multilingual typography in one shot
- **Dense Chinese typography** — restaurant menus, textbooks, almanacs, propaganda posters all achievable

## Syntax surface

- **No documented `--flag` syntax.** One `--ar 9:16` mention surfaced but is not the canonical input form. Prefer prose: "9:16 vertical", "16:9 landscape", "1:1 square".
- **JSON-structured prompts parse reliably.** Heavy nested objects with `type`, `subject`, `style`, `background`, `header`, `layout`, `callout_labels` work for exploded-view posters and infographics.
- **Raycast `{argument name="x" default="y"}` placeholders** widely used and respected when paired with Raycast Snippets.
- **Natural-language ref images**: "Based on this character", "Using this portrait", "Upload a source image", "the same character from panel 1".
- **Inpainting / mask editing** via the OpenAI Images Edit API surface — prompt text describes the change to the masked region.

## Strengths called out repeatedly

- "Information density should be high but not crowded" — the model respects this; structure beats sprawl
- "Restrained / minimal / negative space" produces premium results for product/poster work
- "Extract style DNA, combine information visualization, avoid templated assets" — directives the model follows
- 35mm film, 90s point-and-shoot, RAW iPhone, 2003 digicam aesthetics rendered authentically

## Identity & consistency phrases

| Phrasing | Use |
|---|---|
| `absolutely consistent in appearance` | Cross-panel character lock |
| `must remain highly consistent across all panels` | Multi-panel grid |
| `the same character from panel 1, identical wardrobe and hair` | Series continuation |
| `Based on this portrait, preserve facial features, expression, hairstyle` | Identity anchor with attached image |
| `face and posture must look like a real pedestrian, not overly polished` | Anti-AI-glamour clause |

## Aspect ratios seen in source

- `1:1` square — social posts, e-commerce main image
- `9:16` vertical — mobile/portrait, smartphone-shot aesthetic, posters
- `16:9` landscape — TV/interview scenes, bento infographics
- `4:5` — LinkedIn-style portraits
- `6:7` — medium-format film aesthetic
- `3:4` — vertical poster format
- 360 equirectangular panorama — the model resolves this prompt verbatim

## Categories with strong examples in source

- **Photography & photorealism** — RAW iPhone, 35mm film, golden hour, 90s point-and-shoot, 2003 digicam, Apple Park crowd shots, candid life slices, harsh on-camera flash
- **Game & entertainment** — Hitman / Black Myth: Wukong / GTA / Zelda / League of Legends in-game footage, gacha UIs
- **UI/UX & social media** — livestreams, e-commerce screens, Douyin grid, historical figures on modern platforms
- **Video / animation / collage** — storyboards, manga panels, multi-shot continuity
- **Typography & poster design** — propaganda posters, character posters, product launches, calligraphy, Chinese newspaper layouts
- **Infographics & education** — knowledge cards, fitness guides, gaokao exams, travel guides, exploded-view product diagrams
- **Character & consistency** — 16-panel expression grids, reference sheets, IP character series
- **Image editing & style transfer** — photo enhancement, colorization, comic translation, before/after restoration
- **E-commerce main image** — luxury perfume on marble, miniature diorama skincare, sustainable T-shirt with plantable tag, premium grain powder ad board, earbuds infographic, gaming motherboard studio shot, pastel-blue Crocs fashion ad, 9-panel product TVC storyboard
- **Livestream UI mockup** — Douyin / TikTok / Twitch screenshots with chat ribbons, gift overlays, viewer counts, brand-character livestream PK
- **Gacha-game UI screen** — full mobile game screen with HUD, banner art, summon button, item cards, chat
- **Character reference card** — official character sheets with stats, 16-pose dance/expression grids, anime/Persona-style hybrid layouts
- **Style-to-UI design system** — pass a reference image, model produces a UI mockup matching its style/color grade
- **JSON-recreate-from-image** — model analyzes a reference photo, produces a JSON spec, then renders from the JSON

## JSON template that works (exploded-view poster pattern)

```json
{
  "type": "exploded view product diagram poster",
  "subject": "VR headset",
  "style": "clean high-tech 3D render, studio lighting, glowing accents",
  "background": "{argument name=\"background color\" default=\"soft purple and blue gradient\"}",
  "header": {
    "logo": "∞ {argument name=\"product name\" default=\"Meta Quest 3\"}",
    "subtitle": "{argument name=\"main catchphrase\" default=\"new reality, new structure\"}"
  },
  "layout": {
    "centerpiece": "vertically stacked exploded view of a VR headset showing 9 distinct layers ...",
    "callout_labels": {
      "count": 8,
      "left_side": ["Snapdragon® XR2 Gen 2 — real-time experience", "...", "..."],
      "right_side": ["Pancake lenses — wide FOV, slim profile", "...", "..."]
    },
    "footer": {
      "headline": "Experience evolves from structure",
      "body": "Every component is an answer to the question: how do we make immersion lighter?"
    }
  }
}
```

## Anti-AI-glamour clause (important)

For candid/lifestyle photos, GPT Image 2 defaults to "polished AI aesthetics" unless explicitly vetoed:

```
Realistic skin texture, natural flyaway hairs, slight asymmetry, no glamour retouching,
no beauty filter, no overly polished AI aesthetic. Phone-camera perspective, not studio perfection.
```

## Multilingual / CJK rules

- Place exact target-language copy in the prompt — do not paraphrase
- Specify "must include exact Chinese labels at original positions"
- For overlays: "large emotionally expressive handwritten brush-pen style", "slightly irregular and emotional"
- For dense Chinese: "dense Chinese typography, all text clear and readable with realistic fonts"

## Anti-patterns

- Vague font directives ("elegant", "modern") → garbled glyphs. Use concrete: `serif`, `sans-serif`, `monospace`, named font family
- Asking for "perfectly polished AI rendering" when the brief is candid — fights the natural-skin clause
- Forcing JSON on tiny prompts — `{"subject":"red apple"}` is worse than a sentence
- Mixing Midjourney `--flags` — parsed as literal text

## Output target

Paste into ChatGPT (image generation), the OpenAI Images API (`gpt-image-2` model), or any wrapper that exposes the model. For inpainting, supply the mask via the `image_edit` API surface; the prompt describes only the change to the masked region.
