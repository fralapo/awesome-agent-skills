# Chapter 18: Colour Craft: Value, Harmony Schemes, Palette Building and Output Checks

## Core Idea
Colour in graphic work is controlled on three sliders (hue, saturation, value), built into roles rather than picked by taste, and checked on every output it will live in. The direction-level questions (meaning, five layers, competitive position, accent budget) belong to `art-director` ch11; screen palettes with 60-30-10, HSL ramps, tokens and WCAG numbers belong to `ux-ui-expert` ch22 and ch18. This chapter is the print and graphics craft between them: how to construct a palette, test it, and avoid the typical colour errors.

## Three Properties and Value Contrast
- Control **hue, saturation and value** together. Moving only the hue is a beginner move.
- Low saturation with mid-tone value reads sophisticated or calm; high saturation with strong contrast reads energetic and active. Bright + low saturation = soft; dim + high saturation = hard. Weak contrast and weak saturation = calm (a safe-hands insurance feel); strong = active.
- **Readability comes from value difference, not hue opposition.** Pale yellow on white fails; dark navy on soft cream works. Opposite hues of similar value vibrate and blur.
- **Grayscale test.** Convert to grey. If elements merge, hierarchy is missing. Fix lightness and darkness first, then reintroduce colour. Headlines, calls to action and focal points must stand out without colour.
- Shrink to 50 or 25 percent to check legibility. If text fails, darken the text or lighten the ground; raising the size alone often does not fix it. Pastel text on beige fails on a phone.

## Hue, Tint, Tone, Shade
Tint = hue + white. Tone = hue + grey. Shade = hue + black. Build the supporting colours of a palette from one base by moving along these three, which keeps them related.

## Harmony Schemes and What They Do
| Scheme | Construction | Effect and use |
|---|---|---|
| Monochromatic | one hue plus tints, tones, shades | soft, relaxed, low tension; not for urgent messages |
| Analogous | base plus one neighbour either side (five colours: two either side) | unified, calm (spa, wellness); muted greens and blues |
| Complementary | direct opposite | impact and tension; to soften, use a hue and a tint plus their complements (four colours) |
| Triadic | three hues evenly spaced | attention-grabbing, good for charts and infographics; keep text legible against the strong contrasts |
| Split complementary | a hue plus the two neighbours of its opposite | hard to balance; needs tint experiments |
Think in relationships, not formulas. A vibrant red beside a vibrant green clashes; lighten the red towards soft pink and make the green less saturated and slightly darker. When a complementary pair is too intense, tone down saturation or brightness (muted burnt yellow with a softer purple).

## Palette Roles
- **Recipe**: one dominant colour sets the tone, a softer or neutral-leaning supporting colour balances it, one or two contrasting accents are used sparingly (terracotta dominant, soft peach secondary, deep olive accent). Neutrals stop every colour from fighting for attention.
- **Role model for graphics and interfaces**: action taker (calls to action, emphasis), communicator (headings, key text), support (balances layouts, leads between sections), neutral (breathing room), anchor (the stabilising thread: icons, borders, dividers), feedback (success, warning, error). Example set: vibrant orange = action, deep navy = communicator, muted teal = support, soft off-white = neutral, mid-grey = anchor.
- **Palette map**: platforms across the top (digital, print, social, motion), roles down the side; check each colour in every cell and adjust per output. Typical findings: orange prints dull in CMYK, so adjust the red component for print; teal blends into small mobile backgrounds, so raise its contrast; a grey anchor goes muddy on animated backgrounds, so keep it on static flat areas; navy holds everywhere.
- **Apply with pacing**: navy headline, orange action, teal for the feature section, grey frames on cards, off-white as negative space. The eye hits orange, glides to teal, rests in neutral, ends on the final orange: tension, release, repeat. Not colour blasted everywhere.
- Where this differs from 60-30-10 (`ux-ui-expert` ch22): the proportion rule governs how much of each colour; the role map governs what each colour does per output. Use both: roles first, then proportion. Spreading brand colours through small graphics (a flag-colour motif, a pulled accent in the type) unifies a layout.

## Building a Palette: Procedures
**A. Feeling first.** (1) Write words for how the viewer should feel. (2) Write words for the design's personality. (3) Map keywords to one to three colours. (4) Start from a base colour and explore harmony schemes. (5) Assign main colour against action and focal colours. (6) Check with the audience, then with a contrast tool, a black-and-white preview, a colour-blindness simulation, a phone and a print proof.

**B. Colour analogy.** Name the target emotions, research the colours typically associated with them, pick a base, add supporting pastels for backgrounds, add a small accent for the action or key information. Mental-health site: soft comforting blue base, pastel lavender and pink backgrounds, light mint green action accent. The audience flips the answer: for young teenagers raise the saturation away from pastels and use a bold orange base.

**C. Analyse an existing or competitor palette** (rebrand or entry to a niche). Ask what is outdated or misaligned and whether to align with the niche or stand out. Sustainable fashion default is natural greens and earthy browns; in an oversaturated niche choose differentiation (sunset orange base, deep ocean blue complement, black or white accent) that still fits the message. Following the niche by default, without a decision, is the usual weak result.

**D. Single feeling-word.** Pick one word (nostalgia, energy, elegance), choose two or three colours that match it (one dominant, one or two supports, an accent), apply them to real elements, then re-check against the word; if off, adjust warmth or coolness and saturation.

**E. Sensory analogy.** For a subject such as jazz, note what colours come to mind while listening, write a colour language (cool blue = smooth melodies, red and orange = improvised solos), build around a base with complementary accents, test shades and tones, and document the associations for reuse.

## Perception Effects You Can Use
- **Advance and recede**: warm hues advance, cool hues recede; combine with size for depth. Extended cool hues suggest cold; warm hues in packaging suggest warmth.
- **Visual weight**: a small dark element can outweigh a large light one.
- **Relativity**: the same colour looks warmer, lighter, darker or more saturated depending on its surround. Control the surround to control perception (a desaturated orange looks livelier on a cool surround than on a vibrant one).
- **Edge vibration**: saturated complementary colours side by side shimmer. Use sparingly for urgency, to break monotony or to intensify a headline without more size or weight; never for body text.
- **Single accent in a monochrome layout** (one red stamp on grey and off-white) draws the eye without size or centring.
- **Colour grouping** acts as proximity (a coloured region in a grid replaces boxes and labels).
- **Heritage and restraint**: deep desaturated forest green with gold; low saturation reads as controlled. Deep desaturated blues with low brightness feel cold and withdrawn; a small red adds tension against a melancholy environment.
- **Status convention**: green approved, yellow potential issue, red problem or discard, grey unavailable.
- Brand colour is the strongest memory-recall tool; consistent use across decades turns it into a trigger.

## Colour Craft Fixes
- **Cheap primaries**: swap pure red, yellow and blue for deeper relatives (forest green, burgundy, deep navy); add a metallic hint, a subtle gradient or a soft texture for richer feel.
- **Shadows**: not default black; about 30 percent black (around #4D4D4D to #777), multiply mode, 30 to 50 percent opacity. Flat design over drop shadows in most cases.
- **Textures**: overlay or soft light, never normal mode; set opacity so the texture supports rather than dominates (also ch10 on semi-transparent overlays).
- **Gradient grounds**: flatten and surface-blur to remove banding or grain before adding type; a vibrant gradient plus an off-white band gives distinction and room for the action.
- **Print**: working in RGB for screen preview is fine, but convert and proof for CMYK; saturated oranges, greens and blues shift. Check colour mode before export (ch01, ch12).
- **Pull accent from the focal point**: take the type and action accent from the hero image (a model's red and black) so the layout reads as one piece.
- **Logo colour**: one or two colours aids recognition and reproduction; more only when planned and defensible. Design black and white first to avoid colour bias.

## Evidence Notes
Colour tests quoted in this area are small, informal samples: yellow and orange most often chosen as the happiest group (about two thirds of respondents), a red action beating green by about 21 percent in one click test, a high-contrast orange and black thumbnail lifting click-through by about 35 percent in one alternating test. Use them as tendencies aimed at the majority of a defined audience, never as proof or as client-facing statistics. Association tables (orange = energy, blue = trust, purple = luxury, brown = rugged, black = high-end) are hypotheses: the same red reads premium on a watch, fast on a racing team and entertainment on a streaming brand depending on type, imagery and industry. Cultural meaning varies (white at weddings or at funerals, red as love or anger).

## Warning Signs
- A dominant colour overpowering the focal content (a saturated background drowning the product and the action).
- Poor balance across a family of products (one bold variant beside subdued ones).
- Temperature mismatched to the brief: red and orange for a meditation brand, only cool colours for a toy.
- Colour effects (random full-background gradients, glowing yellow text) overpowering the message; colour is rarely the star.
- Too many or inconsistent colours, especially in type.
- No colour hierarchy, or credit given to colour for work done by contrast and placement.
- Status or meaning carried by colour alone.
- Print conversion ignored.

## Checklist
- [ ] Hue, saturation and value all set on purpose
- [ ] Grayscale and 25 percent tests pass
- [ ] Every colour has a role; neutrals present
- [ ] Palette map checked for digital, print, social and motion
- [ ] Harmony scheme chosen for the effect wanted, tinted down if too intense
- [ ] Shadows and textures set to soft values
- [ ] CMYK proof or conversion done for print
- [ ] Direction-level colour decisions (layers, competitor position) come from the art director
