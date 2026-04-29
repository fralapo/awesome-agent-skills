# GPT Image 1 / DALL·E 3 (OpenAI)

OpenAI's previous-generation image model — natural-language-first, strong photography priors, weaker at long text and CJK than its successor GPT Image 2.

## Tier

Standard. Use for single-subject generations, short prompts, simple edits. For long text in image, multi-panel consistency, or CJK, prefer GPT Image 2 (`gpt-image-2.md`).

## Syntax surface

- **Natural language only**, no flags, no weight syntax
- **Prompt rewriting on the model side** — the model reformulates short prompts into longer ones internally; this can drift from intent. Counter with explicit detail: lens, lighting, composition, framing
- **Mask-based edits** via Images Edit API — supply a transparent PNG mask + prompt describing the change to the masked region only
- **Reference images** referenced as "the provided image" in API; not addressable inline as multiple images in one prompt
- **Aspect ratios** via API `size` param: `1024x1024`, `1024x1792` (9:16-ish), `1792x1024` (16:9-ish). DALL·E 3 limited to these three sizes; GPT Image 1 adds intermediate ratios

## What works well

- Studio product photography, single hero subject
- Cartoon / illustration with strong style prior (DALL·E 3 era loves Pixar/3D-render aesthetic by default)
- Short Latin-script labels (< 10 words)
- Simple compositions with one or two subjects

## What fails

- Long text in image — letters distort past ~10 words
- CJK / Arabic / Cyrillic — breaks
- Multi-panel consistency — character drifts across generations
- Dense bento/infographic layouts — modules collapse, copy garbles

## Identity preservation

Weaker than Nano Banana / GPT Image 2. For face-preserving edits, use the Images Edit API with a mask covering only the area to change, and write the preservation clause in the prompt:

```
Preserve the subject's face, hair, and skin tone exactly. Only modify the {region} to {change}.
```

## Anti-patterns

- Overly polished default look — counter with `"natural skin texture, no airbrushing, no beauty filter"`
- Letting prompt rewriting hijack intent — be explicit about what NOT to add
- Asking for text > 10 words — splits / misspells

## Output target

OpenAI Images API (`dall-e-3`, `gpt-image-1`), ChatGPT image generation, third-party wrappers. For programmatic use specify `quality: "hd"` and `style: "natural"` (vs `"vivid"`) when the brief is photographic, not stylized.

## See also

- `gpt-image-2.md` — newer, far stronger at text + consistency
- `../patterns.md`, `../templates.md`, `../identity-preservation.md`
