# Chapter 35: Interface Craft and Design for the Context of Use

## Core Idea
Details carry meaning: a shadow says "tappable", a colour says "danger", a shape says "album". And the conditions of use decide how loud and simple a control must be: a half-awake user, a courier at a door, a person recording video with one hand. This chapter adds craft rules and context-of-use rules to ch18 (fundamentals) and ch34 (structure).

## Visual Signals Must Mean Something
- **Shadow = interactive**: use it to say an element is tappable; not on logos or non-clickable items. A shadowed card implies the whole card is tappable; if only one item inside is, remove the shadow or add carousel affordances and pagination.
- **Primary colour = the one primary action**. Destructive actions get a red treatment but as a secondary option; a red primary draws attention to the wrong choice. Reserve red for errors and danger, not passive information or brand accents. Colour an action by its role, not habit: "continue" should not be more alarming than the rest of the screen.
- **A tappable action looks tappable** (outline or fill); a non-action must not look like a button (a "no thanks" styled like a payment method fails).
- **Never pair two equal-weight buttons**: one primary, one secondary.
- **Encode content type in shape**: square for albums, circle for artists, a distinct form for podcasts; separate bands (charts, new releases, events) with distinct treatments; give curated sections the brand's own visual assets. Uniform tiles flatten hierarchy.
- **Slightly rounded shapes** read as softer. Use concentric corner radii that match the device. Card padding must keep text off image corners.
- **Dashboard content uses visible tabs** rather than accordions.
- **Back controls** sit top-left or bottom-left, never centred or right (confirm/forward goes right, ch32).
- **Avatars, badges, icons**: small avatars next to chat names speed recognition; badges follow the username so long names do not push text; user badges use the brand's visual identity; give first, second and third place different marks.

## Translucent Surfaces and Contrast
A striking visual language still has to pass legibility checks. Test text and icons against WCAG AA at minimum (AAA is better) in the design tool; translucent surfaces fail easily, so add blur, a tint or a gradient scrim (ch18 overlays). Keep icon tone consistent across varying backgrounds. A reflection or highlight should respond to a real light source or be dropped: a gimmick that moves randomly misleads. Floating tab bars with progressive blur keep contrast over scrolling content.

## Labels and Language
- Put the text inside the action control; an icon-only stop control is unclear. Do not move a label off its control to fit an icon: long translations break it.
- Use unambiguous verbs. "Snooze" and "Dismiss" are near-synonyms to a tired user; "Stop" is clearer. A "Chat" button label is worse than a send arrow.
- Settings that behave like toggles must look like toggles, not clickable rows.
- Two close icons (two X's) that do different things confuse; separate them.

## Status, Data and Progress
- **Decode raw data into status**: show a tick and a colour code (ok, caution, act) and a reference range beside the value (a resting range, a recommended sleep time). Raw numbers without interpretation are noise.
- **Show time remaining or progress as a bar**, not only a number; show the next active item and when it fires at the top of a list.
- **Give frequent tasks their own place**; move rarely used content lower. Group many repeating items into folders by context (work, medication, sport).
- **Warnings**: short copy, a warm colour that signals caution rather than neutral information, and a dismissible state.
- **Passive displays need state feedback**: call pending, answered, live view, what to do after unlocking.

## Designing for the Context of Use
- **Low attention (alarm, one-handed use)**: make the whole screen the target (tap anywhere to snooze, press and hold to stop) with visual and haptic feedback; make the main element (the time) dominant and the date secondary; escalate visibly with repetition (the screen reddens with each snooze); add an icon that says what the screen is; test which variant is primary rather than assuming. Authentication friction (eyes open, face unlock) is a deliberate option.
- **Ergonomics and reach**: most-used controls are larger, more prominent and within thumb or hand reach; primary content and actions sit where eye and hand are both comfortable. In a consumption-first app, move "create" away from the centre and put search within thumb reach. Small buttons placed close together with no margin for error fail when the user is groggy.
- **Camera and capture screens**: keep frequent modes visible and rare ones behind one labelled control; a "more options" arrow opens exactly what it promises in the direction it suggests; gesture direction matches the effect (drag up to zoom in, not sideways); show recording state with a persistent cue (a coloured frame), not only a small icon; place the flash toggle near the shutter in video; keep shooting settings in the camera screen; show the preview in the photo's real orientation; rotate labels with the device; hide technical specs from consumer views; remove duplicate feedback (a control that animates twice).
- **Physical and public objects (intercom, speaker, kiosk)**: ask who really uses it (the courier, not only the resident) and which questions the interaction repeats ("who is it?", "why are you calling?"); answer them before they are asked (camera, message option). Write the feature list before sketching the form. Use a stable order for long lists (alphabetical when lists change constantly), surface people expecting something, use a physical control where tactile feedback matters, avoid a many-key digital pad.
- **Minimal aesthetics can hurt usability**: a clean surface with no visible controls leaves users unsure how to operate it. Keep affordances visible; a material (fabric) can hide mechanical detail while keeping the form clean. Balance functionality, aesthetics and emotion; set functional goals first, explore bold forms, then check feasibility. Modular bases allow personalisation and upgrades.
- **Poor usability is not excused** by "it is cheap" or "it is a kiosk". Design for the actual user (age, familiarity with the device).

## Mistakes
- Equal-weight buttons, tiny targets close together, labels that require reading when groggy.
- Shadows on non-interactive elements; red used for brand accents.
- Translucent material without a contrast check.
- Zoom or action controls that clash with a platform gesture.
- Optimising only aesthetics or only function.

## Checklist
- [ ] Shadow, colour and shape each carry one meaning.
- [ ] One primary, one secondary per decision; destructive is secondary.
- [ ] Contrast checked on translucent and image backgrounds.
- [ ] Labels inside controls; survive longer translations.
- [ ] Data has status and range; progress is visible.
- [ ] Controls tested for the user's actual state of attention and reach.

## Connects To
ch17, ch18 (states, shadows, overlays), ch20 (peak-end, colour psychology), ch21 (contrast, 3 C's), ch22 (colour alone), ch32 (gestures, kiosk), ch34.
