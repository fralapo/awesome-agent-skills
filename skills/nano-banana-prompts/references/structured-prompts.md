# Structured Prompts (JSON / YAML / XML)

Nano Banana Pro parses **structured formats reliably**. Non-Pro handles them partially — treat structured fields as hints it may ignore. Use structure when:

- The prompt has many orthogonal attributes (subject, wardrobe, lighting, background, etc.)
- You need to reuse the same schema across many generations (templating)
- You want to express conditional rules or nested grouping
- The task is multi-step (analyze → plan → render)

For simple prompts, free-form paragraphs still win.

## JSON Object Format

Best for: character/scene specs with many nested attributes. Seen in 2000s Mirror Selfie, Bathroom Selfie, fashion editorials.

```json
{
  "subject": {
    "description": "young woman taking mirror selfie",
    "age": "early 20s",
    "face": {
      "preserve_original": true,
      "makeup": "natural glam, glossy lips"
    },
    "hair": { "color": "platinum blonde", "style": "messy bun" },
    "expression": "confident, slightly playful"
  },
  "clothing": {
    "top": { "type": "crop tee", "color": "yellow", "graphic": "banana logo" },
    "bottom": { "type": "athletic shorts", "color": "white", "fit": "tight" }
  },
  "photography": {
    "camera_style": "early-2000s digital camera",
    "lighting": "harsh super-flash, blown-out highlights",
    "angle": "mirror selfie, tight composition",
    "texture": "subtle grain, crisp details"
  },
  "background": {
    "setting": "nostalgic 2000s bedroom",
    "elements": ["chunky wooden dresser", "CD player", "2000s pop posters"],
    "atmosphere": "authentic retro vibe"
  },
  "output": { "aspect_ratio": "9:16", "resolution": "high" }
}
```

**Tips:**
- Use `preserve_original: true` (boolean) for identity locks — Pro interprets this correctly
- Nest related attributes (`top` inside `clothing`, not flat keys)
- Keep array items short (2–6 elements max per array)
- Avoid deeply nested arrays-of-objects (Pro drops some entries)

## YAML Format (edit task schema)

Best for: image editing with explicit task type, preservation rules, and effects. Seen in torn-paper-reveal prompts.

```yaml
task: "edit-image: add widened torn-paper layered effect"

base_image:
  use_reference_image: true
  preserve_everything:
    - character identity
    - facial features and expression
    - hairstyle and anatomy
    - outfit design and colors
    - background, lighting, composition

rules:
  - Only modify the torn-paper interior areas.
  - Do not change pose, anatomy, proportions, clothing details.

effects:
  - effect: "torn-paper-reveal"
    placement: "across chest height"
    description:
      - Wide natural horizontal tear across the chest.
      - Torn interior uses the style in `interior_style`.

interior_style:
  mode: "line-art"
  style_settings:
    line-art:
      palette: "monochrome"
      line_quality: "clean, crisp"
      paper: "notebook paper with ruled lines"
```

**Tips:**
- Top-level `task:` string describes what — model prioritizes this
- `preserve_everything:` as an array is a strong identity anchor
- Named style settings (under `style_settings:`) let you swap modes without rewriting — change `mode: "line-art"` to `mode: "watercolor"` and re-run

## XML Tag Format (meta-prompt / multi-step)

Best for: director-style prompts that expand one image into a storyboard, spec generation, or any prompt with a clear role and output contract. Pro parses these with high fidelity.

```xml
<role>
You are an award-winning trailer director + cinematographer + storyboard artist.
</role>

<input>
User provides: one reference image.
</input>

<non-negotiable rules>
1) Analyze full composition first.
2) Do NOT guess real identities or real-world locations.
3) Strict continuity across all shots.
4) Realistic depth of field.
5) Do NOT introduce new characters not in the reference.
</non-negotiable rules>

<goal>
Expand the image into a 10-20 second cinematic clip with a clear 4-beat arc.
</goal>

<step 1 - scene breakdown>
Output: subjects list, environment + lighting, visual anchors.
</step 1 - scene breakdown>

<step 2 - theme & story>
Propose: theme (1 sentence), logline, 4-beat arc.
</step 2 - theme & story>

<step 3 - keyframes>
Output 9-12 keyframes labeled KF1..KFN.
Each must preserve continuity rules from above.
</step 3 - keyframes>

<final output format>
A) Scene Breakdown
B) Theme & Story
C) Keyframes list
D) ONE master contact-sheet image (3x3 or 4x3 grid)
</final output format>
```

**Tips:**
- Use numbered/named step tags — `<step 1 - scene breakdown>` beats `<step1>`
- `<non-negotiable rules>` is the strongest constraint tag observed
- `<final output format>` enforces delivery shape — Pro respects this
- Close every tag — unclosed tags get parsed as text

## Hybrid: Paragraph + Structured Block

Often the best shape. Free-form intent + structured constraints.

```
Create a professional headshot of the person in the uploaded image.

<identity>
Preserve face 100%. Same hairstyle, same skin tone, same eye color.
</identity>

{
  "outfit": { "suit_color": "navy", "shirt_color": "white", "tie": false },
  "lighting": "three-point, soft key, subtle rim",
  "lens": "85mm f/1.4",
  "background": "#2a2a2a studio backdrop, subtle vignette"
}

Ultra-realistic 8K, natural skin texture with visible pores. Catchlights in eyes.
```

## When Structure Backfires

- **Tiny prompts.** `{"subject": "a red apple"}` is worse than `A red apple on a white table, studio lighting, 1:1.`
- **Non-Pro Nano Banana + deep nesting.** Past 3 levels of JSON nesting, non-Pro drops fields silently.
- **Contradictions.** `"color": "red"` in JSON + "blue" in paragraph → unpredictable. Structure doesn't resolve conflicts; it amplifies them.
- **Made-up schemas.** Model has no prior for `"vibe_intensity": 0.7` — unknown keys are ignored. Stick to observable visual attributes.
