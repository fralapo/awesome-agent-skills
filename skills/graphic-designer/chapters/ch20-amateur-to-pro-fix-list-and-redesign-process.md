# Chapter 20: Amateur to Pro: The Fix List, Systems and the Redesign Process

## Core Idea
Amateur work is rarely a failure of talent. It is the absence of decisions made before opening the software, of a system behind the layout, and of testing in the conditions the piece will live in. Professionals sketch the structure first, constrain the number of decisions, reuse a system and check the result at several sizes. This chapter turns that into a pre-design checklist, a diagnosis table for before/after fixes, a small set of numeric systems and a redesign procedure. Ch07 gives the critique language and ch10 the refinement pass; here the focus is the repeatable fix. Direction-level judging (five levels, perception tests) is `art-director` ch10; brief expansion and approval is `art-director` ch12; interface audits are `ux-ui-expert` ch34.

## Procedure 1: Decide Before You Execute
1. **Sketch structure in under a minute**: focal point, supporting message, secondary details. The software then builds a decision instead of looking for one.
2. **Purpose and success**: write what the piece must do (sign-ups, sales, recall) and what it must avoid (a banking app: excessive animation, irrelevant graphics, overloaded screens). Design backwards from the result; a plainer look that converts better is a win. Part of the job is persuading the client why a choice helps them.
3. **Four pre-design checks**:
   - *Canvas*: size and orientation (a square composition forced onto a wide banner fails); for brands plan how the design adapts across canvas shapes.
   - *Context*: where and how it is seen, at what speed and distance (a roadside billboard needs minimal text; a favicon; cosmetic packaging among competitors). Visualise the real environment so the piece is not lost there.
   - *Dynamism*: the more it must grab attention fast, the more dynamic (movement, italics, diagonals; younger, action-oriented audiences); the more information it must convey, the more static.
   - *Contextual relevance*: season, industry, audience, brand values show in colour, type and imagery (summer palette for a June event, earthy tones for organic).
4. **Constraints**: platform dimensions, dark and light mode, paper stock, viewing distance, cheap printing, ink spread, rich against non-rich black, hairlines that vanish, colour shift. Ask: where will it live, how small or large, what breaks first?
5. **Visual language from keywords**: reduce the objective to one sentence ("high-end, clean, delicate") and derive palette, shape, type, imagery and texture from its words; every later choice must trace back to it. Colour (ch18), shape (ch19) and type (ch03) follow.
6. **Emotion to elements**: pull the emotions from the brief (excitement, FOMO), list four categories (colour, typography, imagery, layout) and write how each expresses the emotion (vibrant reds; futuristic bold sans; a countdown, a crowded virtual world). Concept generation (reverse thinking, metaphor, psychology techniques) belongs to the creative director; research and moodboard to the art director.
7. **References**: absorb the feel of the niche and adjacent media (album covers, fashion), note what catches the eye, never copy.
8. **Build around how a person reads**: first impression, information flow, action. Top = headline or hero, middle = essentials, bottom = action; use a grid, then break it once on purpose (ch15).

## Diagnosis Table: Common Amateur Tells and Fixes
| Tell | Fix |
|---|---|
| Clutter, scattered dates and URLs | remove irrelevant imagery and dots; group key information in one corner and the focal subject in the opposite corner; put the offer in a circle |
| No typographic hierarchy, slogan "slapped" at the bottom | differentiate lines by size, weight and colour; put the slogan close under the logotype in a thinner weight; break a uniform four-line block into three with one larger, bolder, coloured key line |
| Too many fonts (four or more) | two, three at most, or one family with role weights |
| Informal script beside a serious uppercase line, or serious type on playful art | match type tone to brand and illustration (ch03, ch10) |
| Title vertical or clashing with the ground | set horizontally; use white or a lighter neutral from the palette |
| Call to action in the colour of its surroundings | contrasting colour and shape (ch16); keep it from dominating |
| Related items far apart | proximity (ch14); frame or icon to reinforce |
| Cramped micro space: tight leading, buttons touching | open the leading, widen padding (ch14) |
| A lone word as a title line | rebreak the lines |
| Unbalanced halves | symmetrical groups of similar size, or a large group against a small one with aligned edges (ch16) |
| Content hugging the edge, unaligned | safe margins and one clear axis |
| Hairline logo details | thicker, more widely spaced strokes; test at card scale |
| Pure primaries, black drop shadows, textures in normal mode | ch18 fixes |
| Placeholder text, template typos left in | proofread; use real copy, not lorem ipsum (also for font tests) |
| Unnecessary drop shadow | flat design |
| Everything centred and correct but lifeless | offset the hero, shift one alignment, re-order the type: alignment, tension, space between text and image, and flow are the roughly 20 percent of choices that give most of the impact |
| Brand colours only in one corner | spread them through small graphics (a flag-colour motif, an accent pulled into the type) |

## Systems That Remove Guesswork
- **Decision budget.** Cut a 12-choice poster to about 4 decisions: what it is (title), what to look at (one hero), when and where (dates), and everything else in one proximity-grouped footer strip, with sponsors monotone in one line. Then the **10-second test**: a fresh viewer must state the one idea; if they list extras or get stuck, cut again.
- **Relief zones.** A deliberately low-density area (a warm grey block, soft type, empty space) so the next loud moment hits harder; calm by design, not leftover space. Vary density across a piece; making about 70 percent of a composition less dominant often reads as more professional.
- **Spatial echo.** Reuse one spacing value in unrelated places: a 60 px top and left margin echoed on a quote block; 40 px at the bottom of a front cover and 40 px at the top of the back; 80 px for the next item (double). Invisible rhythm, no rules needed.
- **Type ramp by ratio.** Choose a ratio and climb: body 11 pt x 1.618 = 18 (subhead), x 1.618 = 29 (headline), x 1.618 = 47 (hero). A tighter ratio (x 1.414) gives 11 / 16 / 23. Choose the ratio from the layout: a poster takes the larger ratio, a dense brochure the smaller. This is the same idea as ch03 (headline divided by a fixed factor), run upward from the body. Print body 10 to 12 pt (avoid below 9 pt unless test-printed; 7 pt is possible on a business card only if proofed), web 15 to 25 px; leading 120 to 145 percent of the size; 45 to 90 characters per line (multi-column is the exception); primary heading 180 to 200 percent of body, secondary 130 to 150 percent.
- **One variable family with roles.** Primary wider and heavier, secondary regular width and medium weight, tertiary narrower for small sizes; weight steps of 100 to 200 units (body 400, subhead 600, headline 800). Mispairing fonts is the fastest way to look amateur; test with real headlines and body copy.
- **Scale test: design once, test four times.** Check at about 1920, 768, 280 and 64 px (or the equivalent print sizes): tight tracking collapses, thin fonts vanish, margins look exaggerated or cramped.
- **Platform fluency.** Vertical hierarchy, quick entry points and a strong anchor in the first third for an image feed; more breathing room for a professional network; learn stacked against horizontal, fast against slow, compact against expansive. Clients who pay more want a system that works everywhere.
- **Build the framework once.** Grid logic, margins, rhythm and micro and macro spacing rules take the first hour; each piece in a series is then a variation, and the framework becomes a personal signature. Speed comes from the system, not from rushing.
- **Time-box and step away**: leave the file for 1 to 2 hours, return and re-check the path; save a copy before experimenting with blend modes (the final often chooses simplicity).

## Trends
Use them only on short-lived pieces (a month-long promotion, a year), never in long-term brand assets or logos. Three steps: check relevance to goals and audience, tailor to the client (brand colours, real members or local icons instead of stock, related icons), and make sure the piece still serves its purpose. Two trends can be blended (bold minimalism plus natural textures). The trend is never the most important aspect; the brief is.

## Procedure 2: Redesign an Existing Piece
1. **Diagnose in three parts**: what is wrong, why it is wrong, how to fix it. Common faults: clutter, poor information display, no hierarchy, no focal point, no sense of the genre.
2. **Keep the copy and the facts**; strip back to a blank canvas when the structure is the problem. Remove random graphics and decoration; the message ("new, innovative") must be expressed by imagery, type, colour and layout together.
3. **Choose one distinctive focal element** true to the subculture (a rave: vivid lime on purple or jet black, an inflated 3D letter from the name) and build the palette from the audience's world.
4. **Rebuild the hierarchy**: three levels (ch16), contrast of type styles, white or black label rectangles for minor information, a thin accent bar structuring the information zone.
5. **Check the flow**: diagonal lines in the artwork lead to the action; the focal shape may bleed slightly over a rectangle for interest.
6. **Check consistency**: the same 3:2 image ratio, a repeated shape, icons echoing the artwork (round icons among circles or square icons for contrast, chosen consciously), accent colour pulled from the art.
7. **Iterate**: key word placement and left-side spacing need several tries; never settle on the first layout.
8. **Compare** before and after at thumbnail and real size; ask someone from the target audience whether it excites them.
Before-and-after set pieces: sale poster (group information, circle the discount, muted red), save-the-date (one serif, two rules around the main line, simpler date layout), corporate card (name largest and boldest, title smaller, contact smallest and thinnest, content away from the edge), landing page (two or three fonts, balanced halves), logo (thick plus thin sans in the logotype, thicker symbol lines).

## Skill Ladder (self-assessment)
| Area | Amateur | Pro | Master |
|---|---|---|---|
| White space | fills it | lets it breathe, using proximity, flow, hierarchy | uses objects and shapes to lead the viewer through it |
| Personality | technically fine, cold | builds emotion through colour, type, shape | iconic through originality or humour |
| Consistency | mixed gradients, faces, casings, layouts | repeats shape, face, palette | breaks the pattern where it highlights the key information |
| Simplification | clutter (often client-driven) | removes the unnecessary | knows how far to simplify, and can do busy when the brief calls for it |

## Delivery Habits
- Pre-delivery: spell-check everything, print and test in hand on different paper, mock up in context (on a shelf beside competitors), get a trusted second opinion.
- Work non-destructively: layer masks instead of erasing, duplicate the original before edits, smart objects so scaling does not degrade, dodge and burn on a separate 50 percent grey layer in overlay or soft light, versioned saves, a higher undo count, lowering shape opacity to see what a pathfinder cut will do. For print PDFs avoid outlining all fonts when editability matters (use a flattener preset and embed fonts instead); outline for logos and for files going to a printer without the font.
- Organise by phase: board for typography, imagery and moodboard (hex swatches); a font shortlist separating heading from body candidates, tested as pairs; three variations; export per platform size and format.
- Responsive and technical: design for the most constrained screen first, test on several devices, SVG for logos and icons, compress images.
- Mobile-first applies beyond websites: flyers, brochures and logos must translate to phone, tablet and desktop.
- Hand file structure and a logo kit to the next person (ch01, ch19).

## Common Mistakes
- Moving things around hoping a layout appears.
- Twelve competing micro-choices on one poster.
- Random scale; type selected "by spinning a wheel".
- Testing only at full size or only on the desktop monitor.
- Rebuilding every layout from scratch instead of varying a system.
- Chasing applause rather than the defined result.
- Delivering a good-looking piece nobody can explain or maintain.

## Checklist
- [ ] Structure sketched; success and exclusions written
- [ ] Canvas, context, dynamism and relevance answered
- [ ] Decisions budgeted; 10-second test passed with a fresh viewer
- [ ] Type ramp and weights from a stated ratio; real copy used
- [ ] Spacing values reused; a relief zone exists
- [ ] Tested at four scales and in context
- [ ] Redesign: problem, reason, fix written; before and after compared
- [ ] Non-destructive file; proofread; delivery kit ready
