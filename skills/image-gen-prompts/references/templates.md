# Universal Prompt Templates

Fill-in templates per category. `[ALL_CAPS]` = replace. Each template is tested-shape — seen across multiple working prompts on Nano Banana, Nano Banana Pro, and/or GPT Image 2 community repos.

**Model notes per template** are inline (`Best on:` line). For Midjourney, append the appropriate `--ar`, `--v 7`, `--stylize` flags from `models/midjourney.md`. For SDXL/SD3, split into positive + negative prompts. For FLUX/Imagen, use the prose form as-is and pass aspect ratio as an API param.

---

## 1. Professional Headshot (Business / LinkedIn)

```
Keep the facial features of the person in the uploaded image exactly consistent.
Dress them in a [COLOR] business suit with a [SHIRT_COLOR] shirt.
Background: clean solid [BG_COLOR] studio backdrop with subtle vignette gradient.
Photography: Sony A7III with 85mm f/1.4 lens, flattering portrait compression.
Lighting: classic three-point setup. Key light creates soft defining shadows on face.
Subtle rim light separates shoulders and hair from background. Catchlights in eyes.
Details: natural skin texture with visible pores (not airbrushed). Fabric shows subtle wool texture.
Ultra-realistic 8K professional headshot.
```

## 2. Film-Era Portrait (1990s / 2000s / Kodak Portra)

```
Keep the facial features of the person in the uploaded image exactly consistent.
Style: cinematic emotional portrait shot on [FILM_STOCK e.g. Kodak Portra 400].
Setting: [LOCATION e.g. urban coffee shop window at golden hour].
Lighting: warm nostalgic light hitting side of face, [EXTRA e.g. direct front flash on 35mm].
Atmosphere: subtle film grain, soft focus, dreamy storytelling vibe.
Action: [POSE e.g. looking slightly away, holding coffee cup, relaxed candid expression].
Bokeh background of [BACKGROUND_DETAIL]. High quality, shallow depth of field.
```

## 3. Celebrity / Group Selfie Integration

```
An ultra realistic group selfie. Center: the person from the attached image (uploaded image facial details),
wearing [OUTFIT], holding an iPhone for the selfie.
Around them: [CELEB_1] as [ROLE], [CELEB_2] as [ROLE], [CELEB_3] as [ROLE], ...
All hugging, smiling, posing casually like close friends. Fun joyful mood.
Bright daylight, cinematic quality, natural look, high detail.
```

## 4. Action Figure / Collectible Box

```
Create a collectible action figure of the person in the uploaded image, packaged in a
premium toy box. The figure is posed [POSE], wearing [OUTFIT], with accessories:
[ACCESSORY_1], [ACCESSORY_2], [ACCESSORY_3].
Box design: cardboard blister pack, clear plastic window, brand name "[BRAND]" in bold
serif at top, tagline "[TAGLINE]" below. Side panels show character art and accessory callouts.
Studio product photography, soft shadows, 1080x1080.
```

## 5. Product Photography (Flatlay / Editorial)

```
A high-end editorial photo of [PRODUCT] placed flat on [SURFACE], captured from a
direct top-down view. The surface is gently disturbed to suggest recent motion.
Front of the product is fully visible and properly oriented upright.
Around the product, place [PROPS] that enhance the scene.
Natural sunlight from upper left casts warm realistic shadows.
3D realism, luxury product photography, shallow depth of field, 1:1 format.
```

## 6. Cinematic Product Poster

```
Design a hyperrealistic cinematic poster showcasing [PRODUCT] as the centerpiece,
placed on a sleek [PEDESTAL_MATERIAL] at the edge of [ENVIRONMENT].
Surrounding elements: [ATMOSPHERIC_ELEMENTS e.g. bioluminescent plants, reeds, mist].
Background: [BACKGROUND_SCENE] with [LIGHTING_EFFECT e.g. aurora, lightning].
Moody atmospheric lighting: cool [COLOR] contrasted by warm [COLOR] highlights on the device.
Low angle to emphasize grandeur. Shallow depth of field sharpens [PRODUCT].
Lens flares, polished textures, cinematic vignette.
Brand name "[BRAND]" and tagline "[TAGLINE]" rendered in [FONT] at [POSITION].
```

## 7. 3D Isometric Diorama (Geographic / Thematic)

```
Create a high-detail 3D isometric diorama of [SUBJECT e.g. the United States],
where each [UNIT e.g. state] is represented as its own miniature platform.
Inside each unit, place a stylized small-scale 3D model of that unit's most iconic landmark.
Visual style: cute polished 3D diorama — soft pastel colors, clean materials, smooth rounded forms,
gentle shadows, subtle reflections. Each landmark: miniature, charming, simplified but clearly recognizable.
Arrange in accurate geographical layout. Consistent lighting and orthographic perspective across all units.
Include [UNIT] labels and landmark labels in clean modern sans-serif, floating above each model.
1080x1080.
```

## 8. Bento Grid Infographic (Pro only)

```
Create a premium liquid glass Bento grid infographic with [N] modules, 16:9 landscape.
Hero card: 28-30%. Info modules: 70-72%. Asymmetric bento grid.

Color palette derived from [SUBJECT]: hero color = [DOMINANT_COLOR] at full saturation.
Icons and borders: muted hero (30-40% saturation, never black).
Cards: Apple liquid glass (85-90% transparent), whisper-thin borders, subtle drop shadow.
Background: [CHOICE — ethereal product essence / macro blurred texture / pattern 10-15% opacity / blurred context].

M1 — Hero: [PRODUCT] displayed as [real photo / 3D glass / stylized] + product name label
M2 — [SECTION TITLE]: [CONTENT] + hero-color icons
M3 — [SECTION TITLE]: [CONTENT] + icons
M4 — Key Metrics: [5 EXACT DATA POINTS], format: [icon] [label] [bold value] [unit]
M5 — [SECTION]: [CONTENT]
M6 — [SECTION]: [CONTENT]
M7 — [SECTION]: [CONTENT]
M8 — Did You Know: 3 facts + icons

Typography: sans-serif, tiered weights. Output: 1 image, 16:9 landscape, ultra-premium.
```

## 9. Magazine Quote Card

```
A wide quote card featuring [FAMOUS_PERSON], [BG_COLOR] background,
[FONT] serif font for the quote: "{argument name="quote" default="[DEFAULT_QUOTE]"}"
and smaller text: "—{argument name="author" default="[DEFAULT_AUTHOR]"}".
Large subtle quotation mark before the text.
Portrait on the left, text on the right.
Text occupies two-thirds, portrait one-third. Slight gradient transition on portrait edge.
```

## 10. Comic Book / Storyboard Panel Grid

```
Create a [N]-panel [STYLE e.g. vintage comic book] storyboard of [SUBJECT],
arranged in a [GRID] grid. Continuity rules:
- Same subject across all panels (preserve face, wardrobe, hair).
- Same environment, same lighting, same color grade.
- Only action / expression / framing / camera angle change.

Panels:
1. [WIDE ESTABLISHING] — [action]
2. [MEDIUM] — [action]
3. [CLOSE-UP] — [emotional beat]
[...]

Each panel labeled with shot type in safe margin. Consistent ink weight and halftone.
```

## 11. Chibi / Plush / Origami Transform

```
Transform [SUBJECT] into a [STYLE — chibi 3D / plush toy / origami folded paper / pixel art / LEGO minifigure].

For chibi: Q-style 3D proportions (big head, small body), preserve [OUTFIT] colors.
For plush: fluffy fabric texture, visible stitching, button eyes.
For origami: realistic colored paper, visible creases, geometric folds capturing distinctive features.
For pixel art: 32x32 or 64x64 grid, limited palette, crisp pixels.
For LEGO: minifigure proportions, ABS plastic sheen, printed face and torso graphics.

Placed on [CLEAN_SURFACE] with soft shadows. Minimalist product photography. 1080x1080.
```

## 12. Non-Destructive Background Swap

```
Perform non-destructive background editing on the attached photo.

Preserve entirely unchanged: foreground subject(s), posture, facial features, expression,
clothing, hairstyle, all fine details — zero alterations.

Only modify the background area: replace with [NEW_ENVIRONMENT].
Match the original photo's: lighting direction, color temperature, perspective, depth of field.

The edit should feel natural — as if the subject was always there.
```

## 13. Split-View Render (Realistic | Wireframe)

```
Create a high-quality realistic 3D render of exactly one [OBJECT].
Object floats freely in mid-air, gently tilted and rotated in 3D space. 1080x1080. Dark minimalist background.

Left Half — Full Realism:
Accurate materials, colors, textures, reflections, proportions. Completely opaque, no transparency.

Right Half — Hard Cut Wireframe Interior:
Crisp vertical boundary from top to bottom edge. No diagonal, no curve, no gradient.
Wireframe: 80% white lines, 20% accent color sampled from the realistic half.
Thin, precise, engineering-style lines. Geometry must exactly match the object.

[STRICT_SINGLE_OBJECT_RULE — see patterns.md]

Soft neutral global illumination, no hard shadows.
```

## 14. Meta-Prompt Keyframe Director (Pro only)

Use `<tag>` structure — Pro parses reliably.

```
<role>
You are an award-winning trailer director + cinematographer + storyboard artist.
Turn ONE reference image into a cohesive cinematic short sequence, output AI-video-ready keyframes.
</role>

<non-negotiable rules>
1. Analyze full composition — identify all subjects, spatial relationships, interactions.
2. Do NOT guess real identities or real-world locations.
3. Strict continuity across ALL shots: same subjects, same wardrobe, same environment, same lighting.
4. Realistic depth of field: deeper in wides, shallower in close-ups.
5. Do NOT introduce new characters/objects not in the reference.
</non-negotiable rules>

<output>
A) Scene Breakdown
B) Theme & Story (logline + 4-beat arc)
C) Cinematic Approach (shot progression, camera moves, lens, grade)
D) Keyframes (9–12 frames with shot type + duration)
E) ONE Master Contact Sheet Image (3x3 or 4x3 grid, all keyframes labeled in safe margins)
</output>
```

## 15. Floating Country / Island Diorama

```
Create an ultra-HD hyper-realistic digital poster of a floating miniature [SHAPE e.g. country]
shaped like [TARGET], resting on white clouds in the sky.
Blend iconic landmarks, natural landscapes ([LIST]), and cultural elements unique to [TARGET].
Carve "[TARGET]" into the terrain using large white 3D letters.
Artistic details: [NATIVE_BIRDS], cinematic lighting, vivid colors, aerial perspective, sun reflections.
Ultra-quality, 4K+ resolution, 1080x1080 format.
```

## 16. Exploded-View Product Poster (GPT Image 2 / Nano Banana Pro)

Best on: GPT Image 2 (parses JSON nesting flawlessly), Nano Banana Pro.

```json
{
  "type": "exploded view product diagram poster",
  "subject": "[PRODUCT_NAME]",
  "style": "clean high-tech 3D render, studio lighting, glowing accents",
  "background": "[BG_COLOR_OR_GRADIENT]",
  "header": {
    "logo": "∞ [BRAND_NAME]",
    "subtitle": "[CATCHPHRASE]"
  },
  "layout": {
    "centerpiece": "vertically stacked exploded view of [PRODUCT] showing [N] distinct layers: [LAYER_1], [LAYER_2], ...",
    "callout_labels": {
      "count": [N_CALLOUTS],
      "left_side": ["[CALLOUT_1_TITLE] — [DESCRIPTION]", "..."],
      "right_side": ["[CALLOUT_4_TITLE] — [DESCRIPTION]", "..."]
    },
    "footer": {
      "headline": "[FOOTER_HEADLINE]",
      "body": "[FOOTER_BODY_COPY]"
    }
  },
  "aspect_ratio": "9:16"
}
```

## 17. RAW iPhone Candid Lifestyle (GPT Image 2)

Best on: GPT Image 2 (RAW iPhone aesthetic is a strong prior). Works on Nano Banana Pro with anti-glamour clause.

```
Create a completely RAW quality, unprocessed, unedited image with full iPhone camera quality.
[ENVIRONMENT, e.g. "A subway station in [CITY], a momentary blur"]. [SUBJECTS_AND_ACTION].

Realistic skin texture, natural flyaway hairs, slight asymmetry, no glamour retouching,
no beauty filter, no overly polished AI aesthetic. Faces and postures must look like real
pedestrians, not styled models. Phone-camera perspective, not studio perfection.

[Aspect ratio, e.g. 9:16 vertical].
```

## 18. Multi-Panel Character Expression Sheet

Best on: GPT Image 2, Nano Banana Pro. Fragile on Midjourney v6, SDXL.

```
A [N]-panel character expression sheet for [CHARACTER_NAME], arranged in a [GRID_LAYOUT e.g. 4x4 grid].
The character is the same person across all panels — identical face, hairstyle, wardrobe color and silhouette,
age, and skin tone. Only facial expression and head angle change between panels.
Same lighting style, same color grade, same plain background across the series.

Panels:
1. Neutral / resting expression
2. Happy / smiling
3. Surprised / wide-eyed
4. Sad / tearful
5. Angry / brow furrowed
6. Skeptical / one eyebrow raised
7. Laughing
8. Calm / introspective
[...]

Each panel labeled with the expression name in clean small caps below the portrait.
Style: [ART_STYLE — anime / illustration / 3D render / photograph]. [Aspect ratio].
```

## 19. E-commerce Hero / Main Product Image

Best on: Nano Banana Pro, GPT Image 2, FLUX Krea, Imagen 4.

```
A clean e-commerce main product image of [PRODUCT].
The product is centered in the frame on a [BG_COLOR_OR_GRADIENT] background, with [SHADOW_STYLE — soft shadow / floating / surface contact].
Lighting: bright even softbox lighting from above and 45° front, no harsh shadows on the product,
gentle highlight on top edge, very subtle reflection beneath.
Camera: 100mm f/8 macro, sharp focus on the front face of the product, ample padding around all edges.
Realistic materials and accurate brand colors. Crisp surface detail.
Format: 1:1 square, 1080x1080, optimized for product listing thumbnail.
```

## 20. YouTube Thumbnail (16:9)

Best on: Ideogram 3 (best text), GPT Image 2, Nano Banana Pro, Midjourney v7.

```
A high-contrast YouTube thumbnail, 16:9 landscape.
Subject: [SUBJECT_DESCRIPTION], expression [EXPRESSION e.g. wide-eyed surprise], placed off-center [LEFT/RIGHT].
Background: [SCENE_DESCRIPTION] with strong color saturation and a dramatic light gradient.
Large bold sans-serif headline reading "[HEADLINE_TEXT — keep under 6 words]" in [COLOR] with thick black stroke,
positioned [POSITION e.g. upper-left, occupying 1/3 of frame].
Small accent badge or arrow near the subject. Crisp kerning, exact spelling.
Saturated color palette, high contrast, immediate visual hook.
```

## 21. Game-Style In-Engine Screenshot

Best on: GPT Image 2 (strong game-engine priors), Midjourney v7.

```
A photorealistic in-engine screenshot from [GAME_TITLE_OR_GENRE_e.g. "a stealth-action title in the style of Hitman"].
Scene: [SCENE_DESCRIPTION].
HUD elements: [HUD_DETAILS_OR_NONE]. Lighting: [GAME_LIGHTING_STYLE e.g. moody volumetric, neon-lit].
Engine look: [UNREAL 5 / DECIMA / RE ENGINE / etc.] with high-resolution textures, motion blur,
post-process color grading.
[Aspect ratio, e.g. 16:9].
```

## 22. Knowledge Card / Educational Infographic (Pro)

Best on: GPT Image 2 (dense Chinese typography), Nano Banana Pro.

```
A clean educational knowledge card on the topic "[TOPIC]", [LANGUAGE] copy.
Layout: [GRID_DESCRIPTION e.g. "title at top, three labeled illustration columns, footer with key takeaway"].

Title: "[TITLE_TEXT]" in bold serif, large, centered.
Three columns, each with:
  - Stylized minimalist illustration of [CONCEPT_N]
  - Subtitle "[CONCEPT_N_TITLE]"
  - 2-3 sentence body copy "[DESCRIPTION]"
Footer: takeaway "[KEY_TAKEAWAY]" in italic.

Color palette: [HEX_LIST]. Typography hierarchy clear; information density high but not crowded.
[Aspect ratio, e.g. 4:5 portrait].
```
