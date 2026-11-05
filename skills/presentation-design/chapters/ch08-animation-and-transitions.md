# Chapter 08: Animation & Transitions (Principles)

## Core Idea
Animations don't distract when used well: they direct attention, and to work they must be almost invisible. The problem is never animation itself but how and how much it is used: "fun" effects used to compensate weak graphics (a trashy animation ruins even good design, a delicate one improves design that is already good), durations that are too long, and forgotten sequencing. Animation is a choreography designed together with the layout, in the storyboard, not sprinkled on at the end "to add movement". A small toolkit covers almost everything: fade (the default that "never goes wrong"), fade-and-move, line drawing, and morph / magic move between duplicated slides. Timing is short (0.2–0.5 s for objects, 0.3 s preferred; 0.5–1 s for transitions; ~1 s for morph, 0.5–0.7 s for small moves; 0.1–0.2 s delays), content appears on click exactly when it is named, and one style is kept from first slide to last. Morph is "one transition that lets you build hundreds": design the final state, duplicate the slide, change position/size/color/opacity, apply the transition. Many recurring patterns (zoom, slider, horizontal scroll, reveal, masks, cards, progress indicators) are all variations of that one move. More slides do not mean a longer talk: duration is set by the speaker, not by the slide count.

## Frameworks Introduced
**Three functions of animation:** **functional** (focus attention: one bullet at a time, enlarge/color/move what is being discussed), **staging** (compose or decompose the scene with entrances/exits, e.g. a cover that builds while the topic is introduced), **expressive** (express the brand or topic, e.g. a checkered-flag transition for motor-racing slides; the hardest, born from research and inspiration from websites). Every animation must belong to one of the three.
When to use: deciding whether an animation should exist at all.

**Animation vs transition:** an *animation* acts on one object (entrance, emphasis, exit, motion path); a *transition* acts on the whole slide (the passage from slide 1 to slide 2). Transitions can be "built" with animations (brand shapes entering on one slide and exiting identically on the next).
When to use: choosing the right tool and where to apply it.

**Style · Timing · Sequence:** the three properties of every animation. Style = which effect (basic and combined); timing = duration depending on object size, path length and function; sequence = on click / with previous / after previous + delays.
When to use: specifying or reviewing animations in a deck.

**Three control levers (anti-distraction check):** style (a fade is hard to get wrong), time (when you name an element it must appear immediately, not after a second), entrance count (don't make the speaker click 10 times to populate one slide).
When to use: quick audit before delivery.

**Morph / magic move recipe:** build the end state → duplicate slide → change attributes of objects present in both slides → apply the transition to the arriving slide (PowerPoint: the second slide; Keynote: the first). Equivalents: Morph (PowerPoint), Magic Move (Keynote), Match & Move / "combined dynamics" (Canva); not available in Google Slides (simulate with duplicated slides + fade).
When to use: any movement between two layout states.

**Speaker in control:** content animations start on click; "service" animations (built transitions, populating a slide after the transition, bridge slides) run automatically.
When to use: setting start options.

## Rules & Numbers
**Style**
- Default: Fade. Base set: fade, fade-and-move (short distance), fade-and-scale, blur, line drawing, morph/magic move. Nothing else except special cases.
- The selection criterion is smoothness: effects without "smooth start / smooth end" (easing) look jerky. Fly-in only with both smooth start and end on; objects on the left enter from the left, on the right from the right; never cross paths.
- Wipe (left→right, or bottom→up for vertical lines) to "draw" a line; Split only for outline-only shapes or lines, never text; Spiral (one spoke) on outline circles to build a percentage ring; Stretch/expand only on lines (it deforms other objects); Zoom from the object's center (from slide center only for radial layouts); pixel/dissolve effects only on images in a "digital" theme.
- Avoid: blinds, checkerboard, dissolve "dots", sudden appear (except online), strips, shape, wedge, bounce, bounce-fade, boomerang, drops, somersault, credits, cube transitions, page-curl, fire, confetti. Context-only exceptions (a basketball, a quiz, a newspaper page).
- Animate short text by letter (one word) or by word (1–2 lines); never letter-by-letter on paragraphs. Word-by-word fade is far more elegant than a plain fade.
- For a "pro" soft move, combine Fade with an emphasis/path animation (grow or move) where easing can be set.
- Morph must always be completed with entrance animations or opacity changes, otherwise text disappears abruptly. Objects that should vanish during a morph get 100% transparency instead of being deleted.

**Timing (seconds)**
- Object appearing as it is named: ~0.3 s (perfect sync with voice). General animation range 0.2–0.5 s; fade default 0.5 s acceptable, 0.3 s preferred. 1 s for an object animation is "an eternity" and creates dead pauses.
- Line drawing 0.5 s (0.3 risks being too fast). Fade-and-move 0.3–0.5 s with a very short distance (≈3–10).
- Transitions 0.5–1 s, max 1.5 s for large objects or long paths. Exception: a plain fade between duplicated "state" slides (progressive focus, builds simulated in Google Slides) behaves like an object animation and can run at ~0.3 s.
- Morph: reduce the default 2 s to ~1 s; 0.5–0.7 s for small card/gallery moves; 1–1.5 s for large shapes covering the slide, big rotating/zooming shapes or large 3D-object moves, where faster looks frantic. Stay within the 1.5 s transition maximum.
- Delays for staggered entrances: 0.1–0.2 s between elements (0.1 can be imperceptible on text; use 0.2 there); cascades like 0.2/0.4/0.6/0.8 s. With "with/after previous" a slide populates in under 1 s.
- Long durations only for suspense or loops.
- Bridge slides: advance automatically after 0 s; a near-instant fade (~0.01 s) when an invisible regroup is needed.

**Sequence**
- On click for anything synced with speech ("I say lemon, lemon appears"). With previous + small delays for fluid staggered entrances. After previous rarely.
- One bullet at a time; active item 100% opacity, others ~30% (or covered by a background-colored rectangle at ~70% opacity). First show an overview with all points, then step through.
- Exit order communicates hierarchy: the biggest/most important element leaves first, then the smaller ones.
- Entrance animations of a slide start after the transition, not on an extra click.
- In PowerPoint delays count from the first element of the group.

**Consistency**
- All animations on a slide share one character (no bounce among soft moves); one animation style for the whole deck, not a new effect per slide.
- Present with the same software you designed in: effects get converted or dropped otherwise.
- Movement looks alive when several attributes change together (position, rotation, size, color, opacity) and objects move on different paths/speeds; everything on one axis looks static. Light rotations of ±10° between two morph slides add harmony; a slight offset between two objects' start/end makes them read as distinct.

**Loops**
- Slow, continuous, barely perceptible, never the focus: background glows, illustrations, waiting slides before an event.
- Path loop: path animation + auto-reverse + repeat until end of slide, easing off, duration 5–10 s (circular path ~10 s, path 8–15 s). Emphasis loop: rotation 45° (not 90°), ~10 s, auto-reverse; "teeter" ~2 s, no auto-reverse; grow ~5 s.
- Animate loops only on selected slides (e.g. glows present everywhere but moving only on big-statement slides); overlapping glow images must not overlap visibly or the trick shows.

**Corporate constraints**
- Many companies ban animations for fear of "PowerPoint disasters"; answer with a minimal allowed set in the template (fade on click for focus) rather than a total ban.
- Online presentations: avoid motion (lag makes fades stutter); use Appear / "all at once" to show one element per click.
- 3D models and heavy morphs: test on the presenter's computer.
- Google Slides only: duplicated slides + fast fade (~0.3 s) on all slides, covering rectangles with alpha for focus.

## Procedures
**Plan animation (before the software)**
1. Storyboard on paper/tablet: for each slide note entrance, action, exit. 2. Decide the function (functional/staging/expressive). 3. Build the final composition first, then derive previous states backwards. 4. Add multiple transition shapes at the end of the work, or the layout underneath becomes unmanageable.

**Morph / magic move**
1. Same objects in both slides (copy-paste, don't recreate). 2. Park incoming/outgoing objects off-slide (outside the canvas) on the previous/next slide. 3. Group elements that must move together; ungroup elements that must transform individually (morph does not match objects inside a group with ungrouped ones, it falls back to a fade). 4. If objects jump or "invent" paths, add an identical bridge slide where groups are rearranged, auto-advance 0 s. 5. Remove leftover entrance animations from objects that should stay still. 6. To animate the background, use a full-slide rectangle instead of the slide background. 7. Check layer order (selection pane) and remove default outlines from shapes.

**Recurring morph patterns**
- **Zoom:** image enlarged on slide 2; or a full-slide frame with a hole (subtract a smaller rectangle from a full-slide one) enlarged until only the image remains; product zoom + circle on a detail + connector to a callout.
- **Slider/carousel:** first item centered and highlighted, second smaller and transparent, third off-slide; duplicate and shift all by one position; progress bar (4 pt grey line + black segment ~1/3 long) advances. Morph ~1 s.
- **Gallery:** main image large, thumbnails darker (brightness −60) rotating into position; morph 0.7–1 s.
- **Horizontal scroll:** Push transition from the right on all slides; timeline strips use Push left→right with lines exiting the slide.
- **Reveal / mask:** rectangles in the background color cover text or images and move away on the next slide (text appears to rise "from a mask"); or bars covering an image slide out irregularly. Mind the layer order.
- **Masks:** shapes subtracted from full-slide rectangles (stars, region outlines, rounded windows) with the image underneath; enlarge the mask while shrinking the image for a parallax feel.
- **Cards and lists:** stacked rounded cards, previous one sliding back smaller and transparent; tilted cards entering and straightening; keywords scrolling up under a top/bottom white-to-transparent gradient, active word black, others grey.
- **Progress / chapter indicators:** pills or bars where the active one is white/opaque and the others transparent; chapter boxes that expand to full slide and collapse back.

**Data and text patterns**
- **Charts:** reveal one series/bar at a time following the voice; percentage rings built with Spiral on an outline circle; timeline lines drawn with Wipe in the stroke direction, the connecting vertical "with previous" +0.2 s, the next date group "after previous".
- **Rolling numbers:** all numbers already on the slide, stacked above/below in transparency; morph slides them up into place.
- **Counter change (01 → 02):** on the arriving slide put "2" and the old "1" at 0 opacity; on the departing slide paste "2" at the same position at 0 opacity, so one fades in as the other leaves.
- **Text exit with morph:** copy the text to the next slide, remove its animation, send it back and set text fill to 100% transparency, moving it slightly with the main object.
- **Moving photo background:** tall image filling the slide with the bottom overflowing; duplicate 2–8 times moving it up; morph.
- **Focus with an emphasis callout:** large sentence in grey with the key part duplicated in white on top; word-by-word fade 0.3 s with previous, then the emphasis on click by letter 0.3 s.

**Loop setup**
Select element → path (freehand/arc/circle) or emphasis (spin, teeter) → easing off, auto-reverse as above → with previous → repeat until end of slide → place entrance fades before the loop in the animation order.

## Common Mistakes
- Fun/trashy effects to "liven up" a weak slide → fix the design; use fade.
- Default durations (morph 2 s, 1 s fades) → 0.2–0.5 s objects (0.3 preferred), 0.5–1 s transitions, ~1 s morph.
- Everything moving at once → one or two moving objects; the eye must know where to look.
- Ten clicks to build one slide → group, with-previous + 0.1–0.2 s delays.
- Elements appearing after they are named → on click, ~0.3 s.
- Morph treated as decoration "because it's nice" → design the purpose first.
- Deleting an object between morph slides → set it to 100% transparency.
- Mixing bounce with soft moves, or a different effect per slide → one style deck-wide.
- Fly-in without easing, crossing paths → smooth start/end, enter from the near side.
- Presenting in another app than the one used to design → present in the original software.

## Mental Models
- **Animation must be invisible:** if the audience notices it, it is probably too much.
- **Number of slides is irrelevant:** five slides can look like three; splitting into states is easier than animating one slide.
- **The limit is the head, not the software:** solve the idea first, then build it with what you have.
- **Website hover → voice hover:** what lights up under the cursor on a site lights up on a slide when the voice names it.
- **Repeated elements make motion perceptible:** without shared objects between slides, movement is not perceived.
- **Opacity is the focus lever:** active 100%, inactive ~30%.

## Examples
- **Values list (5 points):** big "01/05" counter, arrow markers, active point 100% and others 30%; points scroll up in steps with magic move; the new number fades in at 0 opacity under the old one.
- **Product feature slides inspired by a console UI:** stacked rounded cards, glow PNGs at 50% transparency, top progress pill at 80% transparency; fades 0.5 s with previous, delays 0.2/0.4/0.6/0.8 s, product rising with a 1 s delay (a deliberate staging pause, not a stagger) and 0.65 s duration (a large object on a long path, so above the 0.2–0.5 s object default); card falls off-slide rotated 5°; morph 1 s via a regroup bridge slide.
- **Furniture product slider:** white frame with a hole, photos sliding beneath, 4 pt progress line, morph 1 s.
- **Motor-racing deck:** 15 squares as a checkered flag entering row by row left→right with fade-and-move 0.3 s, exiting identically on the next slide as a built transition.
- **Agency menu deck:** chapter tabs that open to full slide (morph 1 s → 0.7 s) to host content and close automatically ("after") to move to the next tab.
- **Pitch deck for a tech startup:** slow path loops (5–10 s, auto-reverse) on background glows only on big-statement slides.
- **Event-style three-point list:** three rounded rectangles entering in sequence with 0.5 s morph, built from the final slide backwards.
