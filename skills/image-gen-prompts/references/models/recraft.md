# Recraft v3

Design-system focused image model. Distinguishing feature: **native vector (SVG) output** alongside raster, plus persistent brand styles you can train and reuse.

## Tier

Pro for design-system work. Standard for casual generation.

## Syntax surface

- **Natural-language prose**, similar to FLUX/Imagen
- **`style` param** picks a base style: `realistic_image`, `digital_illustration`, `vector_illustration`, `icon`, plus user-trained brand styles
- **Vector output**: when `style` family is `vector_illustration`, response includes SVG path data
- **Brand style ID**: train a custom style on 5+ reference images, get a style ID, reference it in subsequent generations
- **Aspect ratio** via `image_size` API param: `square_hd`, `portrait_hd`, `landscape_hd`, plus explicit dimensions
- **Reference images** via `controls.image_url` (style transfer) or `controls.colors` (palette lock)
- **Negative prompt** via `negative_prompt` API param

## Best-in-class for

- **Vector output** — only major image gen with native SVG path generation
- **Brand consistency** — trained style IDs reproducibly hit a designed look
- **Icons & UI illustrations** — clean, on-brief, scaleable
- **Editorial illustration** — flat, geometric, illustrative styles
- **Color palette lock** via `controls.colors`

## Weak points

- Photorealism — usable but below Imagen / GPT Image 2 / FLUX Krea
- Cinematic photography priors — limited
- Long text in image — Ideogram and GPT Image 2 still stronger
- Complex narrative scenes — drift past 3 subjects

## Anatomy template (vector illustration)

```
A flat geometric illustration of <subject>.
Color palette: <named tones or hex list>.
Composition: <centered / asymmetric / grid-based>.
Style: editorial, clean line work, <weight cue>.
Small details: <list>. No text in image.
```

For posters or marketing assets, layer Ideogram quotes on top in a downstream tool, or specify text inline if Recraft v3 is rendering raster.

## Anti-patterns

- Asking for photorealistic skin in `vector_illustration` style — wrong tool
- Forgetting to specify the style family — defaults to `realistic_image` which underuses Recraft's strengths
- Embedding `(token:1.3)` SD weights — parsed as text

## Output target

Recraft web app + API. For brand-style work train a style on a few reference images first; the resulting `style_id` is the strongest consistency anchor across many gens.

## See also

- `ideogram.md` — when typography quality matters more than vector output
- `flux.md` — when you need photoreal output instead of design illustration
