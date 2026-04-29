# Conversation Workflows

Three high-level workflows for using this skill in a conversational agent. Adapted from `YouMind-OpenLab/ai-image-prompts-skill` (a sibling skill that searches a 12,000+ prompt corpus).

## Workflow 1 — Direct Generation

User describes the image they want → produce a prompt directly using the universal anatomy + per-model file.

### Steps

1. Ask clarifying questions if the request is too vague (see "Clarifying Questions" below).
2. Identify category → pick a template from `templates.md`.
3. If a model is named, read `models/<name>.md` and apply its syntax surface.
4. Compose the prompt and output it in a single fenced block.

### Clarifying Questions (ask before generating if any are missing)

- **Type of image** — avatar, product photo, poster, infographic, etc.
- **Topic / subject** — what is being depicted
- **Audience / mood** — who will see it, what feeling it should evoke
- **Model** — Nano Banana Pro, GPT Image 2, Midjourney, FLUX, SDXL, Imagen, Ideogram, Recraft, Seedream
- **Aspect ratio / format** — square, vertical, landscape; print sizes for posters

| Vague request | Questions to ask |
|---|---|
| "Help me make an infographic" | What type? (data comparison / process flow / timeline / statistics). What topic / data? |
| "I need a portrait" | What style? (realistic / artistic / anime / vintage). Who or what? Mood? |
| "Generate a product photo" | What product? Background? (white / lifestyle / studio). Purpose? |
| "Make me a poster" | Event / topic? Style? (modern / vintage / minimalist). Size / orientation? |
| "Illustrate my content" | Style? (realistic / illustration / cartoon / abstract). Mood? (professional / playful / dramatic) |

## Workflow 2 — Content Illustration (Article / Video / Podcast → Image)

User pastes article text, video script, or podcast notes and asks for cover art / illustrations.

### Steps

1. **Detect Content Illustration mode** — signals: pasted article, "image for my article / video / podcast", "illustration for", "create visual for".
2. **Analyze the content**:
   - Core theme / topic
   - Key concepts and visual metaphors
   - Emotional tone (professional / casual / inspiring / urgent / playful)
   - Target audience
3. **Match to category** — social-post hero, blog cover, podcast cover, YT thumbnail, infographic, poster.
4. **Pick a template** from `templates.md` that fits the inferred style.
5. **Move to Workflow 3 (Remix)** to personalize the template with extracted content elements.

## Workflow 3 — Remix / Personalization (after a template is chosen)

When a user selects an existing template (or one is auto-selected from Content Illustration), do not output it verbatim. Personalize it.

### Step 3.1 — Collect Personalization Info

Ask only the questions that affect the image. Skip irrelevant ones (e.g. don't ask gender for a landscape).

| Scenario | Questions |
|---|---|
| Template shows a person | Gender? (male / female / neutral). Age range? (young / middle-aged / senior). Ethnicity if user named one? |
| Template has specific setting | Indoor / outdoor / abstract? Time of day? |
| Template has specific mood | Professional / casual / dramatic? |
| Content mentions specific items | Any specific elements to highlight? Brand colors? |
| Professional context | Profession / identity? (entrepreneur / creator / student / etc.) |

### Step 3.2 — Remix the Template

Keep the **structure**, replace the **content**:

1. **Keep**: lighting, composition, artistic style, lens, format, mood adjectives
2. **Replace**: subject matter with the content's key concepts
3. **Adjust**: based on personalization answers (gender, age, setting)
4. **Add**: 1–2 visual metaphors extracted from the content

### Step 3.3 — Output Format

```markdown
### Customized Prompt

**Based on template**: [original template title]

**Content highlights**:
- [key theme]
- [important visual elements]
- [mood / tone]

**Customized prompt** (English — use this for generation):

```
[Remixed prompt — paragraph or model-specific format]
```

**Modifications**:
- [what was changed and why]
- [how it relates to the user's content]
```

### Remix Examples

**Example 1 — article about startup failure**
- Template: "Professional woman in modern office, confident pose, soft lighting"
- User info: male founder, 30s
- Remixed: "Professional man in his 30s in a modern office, contemplative expression, soft dramatic lighting, startup environment with whiteboard in the background"

**Example 2 — podcast about AI future**
- Template: "Futuristic cityscape, neon lights, cyberpunk style"
- User content: AI and human collaboration
- Remixed: "Futuristic cityscape with holographic AI assistants walking alongside humans, warm neon lights suggesting harmony, cyberpunk style with optimistic undertones"

## When to Recommend Existing Prompts vs Compose New

If the user wants **inspiration** or **proven prompts**, point them to `external-corpora.md` for searchable libraries (12,000+ curated prompts on YouMind, ~3,000 GPT Image 2 prompts on EvoLink, ~600 Nano Banana cases on Awesome lists, etc.).

If the user wants a **prompt for a specific scene**, compose using the universal anatomy (`SKILL.md`) + per-model file + `templates.md`.

Both paths are valid; ask which the user prefers when ambiguous.

## Conversational Conventions

These conventions help when this skill runs inside a chat agent:

- **One image-generation prompt per response** unless the user explicitly asks for variations.
- **Always state the target model** in a one-line preamble (`For GPT Image 2:` / `For Midjourney v7:`) before the fenced prompt block.
- **Truncate verbose previews** to ~100 chars when listing many template options; offer a "show full" expansion.
- **Cite the source** when you draw from `examples.md` or `external-corpora.md` (attribution lines like `Source: @author via repo-name`).
