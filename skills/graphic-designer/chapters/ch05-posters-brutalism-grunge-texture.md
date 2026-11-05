# Chapter 05: Poster Languages: Brutalism, Grunge, Texture and Digital Effects

## Core Idea
Brutalist and grunge posters get their energy from loud type, abrasive image treatment, many small details and layered texture, held together by cohesion devices (a recurring accent colour, overlaps, one treatment applied to every image). Effects stay editable (smart objects, masks, duplicated groups), strength is kept moderate so words remain decipherable, and a single saturated accent in a muted composition gives the eye a focal point. Whether a brutalist or grunge language is the *right* one for the project is a direction decision for the art director.

## Framework: Five Ingredients of a Brutalist Poster
1. **Striking images**: bold, eye-catching, slightly weird or abstract.
2. **Bold typography**: big, heavy, extended display faces that cannot be ignored, paired with a second characterful display face for secondary words, and a neutral grotesque for small utility text (track lists, credits) to contrast with the loud type.
3. **Small graphic details**: little shapes, icons and tiny text blocks make a disproportionate difference.
4. **Cohesion**: overlap elements (a figure extending past its frame, two images partly overlapping), repeat a limited accent colour, apply the same treatment to all images.
5. **Texture**: stack scanned grunge textures, use a displacement map on the edges for an authentic printed feel, finish with a global noise layer in overlay at a subtle amount.

## Image Treatments
- **Threshold look**: a threshold adjustment layer reduces a photo to harsh black and white; add a little noise first so detail and richer grain survive. Convert to smart objects and apply the same treatment to every image.
- **Subject cut-outs**: automatic subject selection when speed matters; place a graphic behind the figure (for example a recoloured, thickened wireframe grid with a drop shadow for depth).
- **Differentiate layers**: apply a different filter (such as a graphic-pen effect) to the background image to separate it from the thresholded foreground while staying in a print-like language.
- **Repeated cut-out motifs** add depth; check they do not clutter.
- **Glow from gradient map**: gradient map plus noise and halftone on photographs makes colours look as if they glow; add noise carefully to avoid banding and excessive grain.

## Type Distortion
- Aim at the edge of legibility: letters still decipherable when cropped, overlapped or stacked.
- Split a phrase into word layers and scale them very large; crop, cramp and arrange around the subject for a dense typographic background.
- Vary the weight of individual words and nudge them up and down: irregular weight and baseline add controlled chaos.
- Avoid dead-centre placement; shift the composition toward an edge or the bottom.
- **Displacement**: convert type to a smart object and apply displacement with a texture map. Strength matters: very high values destroy the words; low values (about 15 to 50) distort edges and add grit but keep text readable. Try several maps (grid-like, splatter-like); one subtle accent can be enough.
- Mask effects deliberately: an unmasked texture spreads over everything underneath.
- Keep alternate versions (duplicate groups) before a radical change; try blend modes and filter-gallery effects playfully, since many fail and the occasional surprise gives character.
- Add one small low-emphasis element to anchor the composition without competing with the subject.

## Recipe: Luminous Line-Pattern Effect (digital-interface look)
1. Work on a smart object so filters stay editable.
2. Chain a large-cell pixelation (about 50 to 200 px cells), a median filter, then edge detection and an inversion: harsh blocks produce clean geometric edge lines following the subject contours. Swapping pixelation for a crystallize filter with large cells (about 130 to 220) gives a lightning-like network.
3. Remove the dark background by pulling the black slider of blend-if inward; hold Alt and drag to split the slider for a soft fall-off. Use the underlying-layer slider to reveal original-photo detail where the effect eats the subject.
4. Group the effect and style the group (inner glow, strong outer glow in cool blue, gradient overlay from yellow through white to blue).
5. Thicken thin lines with a maximum filter of 1 to 3 px (as a smart filter).
6. Portraits: desaturate, heavy median (about 50), small blur (15 to 20 px), posterize (4 to 20 levels) and threshold before edge detection; fewer levels give fewer lines.
7. Duplicate and merge the group, apply a long horizontal motion blur for glow behind the sharp lines.
8. Finish with noise, paper or photocopy textures in overlay or screen, a global colour grade, and small interface-like details (crosshairs, tiny labels) kept subordinate to the effect.
For click-level operation of these steps in the ArtCraft image editor, use `photocraft-expert`.

## Common Mistakes
- Displacement or noise set so high the words die.
- Different treatments on each image, so the set does not cohere.
- Too many accent colours; one is enough.
- Texture applied without masks and without keeping a clean version to return to.
- Cluttering with small motifs without checking the whole.
