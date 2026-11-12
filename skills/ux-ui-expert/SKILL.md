---
name: ux-ui-expert
description: "UX research + UI design knowledge base. Research: study plans, roadmaps, sample sizes (usability 5, card sort, diary), small-sample reporting, experiment design, ethics, stakeholders, ROI of UX, Double Diamond. Design: UX/UI/CX scope, user flows, beginner UI mistakes, hierarchy, grids and spacing, component states, dark mode, design systems, the 9 typography laws, UX writing and microcopy, widows/orphans, color systems (60-30-10, color wheel, HSL, tokens, WCAG/EAA), and UX psychology (cognitive load, variable reward, goal gradient, peak-end, Von Restorff, choice overload). Practice and career: portfolios and case studies, the UX job search, winning research buy-in (minimum viable research), recruiting participants and top-task benchmarks, personas and mental-model workshops, feature prioritisation and website process, prototyping and design sprints, anticipatory design, transactional flows, atomic design. Product UX: premium feel and trust levers, onboarding, permission, paywall and cancellation flows, retention mechanics with ethics, AI-assisted UI and design-to-code handoff, design QA, shipping versus polishing and the results-driven UX audit. Use this skill whenever the user plans or runs user research, reviews or critiques a UI, screen, app, landing page or dashboard, picks fonts, colors or a palette, writes button/error/empty-state copy, maps a flow, builds a business case for UX, plans a portfolio or job search, scopes a website or feature list, recruits test participants, or asks why users behave a certain way in a product, even if they never say 'UX'."
allowed-tools:
  - Read
  - Grep
argument-hint: [task, topic, framework name, or chapter number]
---

# UX/UI Research & Design Expert
**Chapters**: 41 | **Supporting files**: cheatsheet, patterns, glossary

**Role boundary.** This skill is the UX/UI designer: screens, flows, interaction, usability evidence. Concept and insight → `creative-director`; visual direction and identity rules → `art-director`; print, poster, logo and layout craft → `graphic-designer`. Adapt their direction to interfaces and report back when it fails on screen (ch23, ch29 mood board handoff). Workshops, design sprints and group alignment exercises (agenda, timing, voting, facilitation) → `workshop-facilitation`.

## How to Use This Skill

1. **Match the task to a workflow** below and open only the chapters it names. Don't load them all.
2. **Use the Core Frameworks** for quick answers; read the chapter before going beyond them.
3. **Quick lookups**: [cheatsheet.md](cheatsheet.md) (tables: sample sizes, typography laws, 60-30-10, states, psychology), [patterns.md](patterns.md) (When / How / Trade-offs for 53 techniques), [glossary.md](glossary.md).
4. **Ground recommendations in evidence**: cite the rule or number (e.g. "line length 45-75 chars, ch21") and never blame the user.

---

## Task Workflows

**Review / critique a UI (screen, landing page, app, dashboard)**: go in this order and report findings as *issue → why it matters → fix*, sorted by severity.
1. Intent and flow: what is the user trying to do here? Are edge cases and the empty, error and loading states designed? (ch19, ch16)
2. Hierarchy: does the eye land on the primary action first? Is only one thing emphasised? (ch18, ch20 Von Restorff)
3. Spacing and grid: consistent 4/8px units, proximity groups the right things. (ch17, ch21 law 2)
4. Typography: the 9 laws, especially sizes, line height, line length and contrast. (ch21)
5. Color: 60-30-10 roles, an accent reserved for the CTA, semantic colors, never color alone. (ch22, ch18)
6. Components: consistency, icon system, all states (default/hover/active/disabled/focus/error). (ch17, ch18)
7. Copy: clear, concise, useful; widows/orphans in headings. (ch21)
8. Psychology: cognitive overload, choice overload, an ethical reward loop. (ch20)

**Plan user research**: frame the knowledge gap (ch15), then pick strategic vs. tactical (ch03), write the study plan with Who/Question/Why (ch05), choose the method and sample size (ch08; experiments ch09), check ethics (ch09), plan analysis and reporting (ch07), and measure impact against a baseline (ch10).

**Build a palette or color system**: one primary, HSL variants, 60-30-10 roles, semantic tokens, WCAG contrast check (ch22, ch21 law 9, ch18).

**Write or fix UI copy** (buttons, errors, empty states, onboarding): the 3 C's in order, front-load the context, end on the action (ch21).

**Make the case for UX to stakeholders**: the ROI model and cost-of-error multiplier (ch13), influence over persuasion with the Goleman sequence (ch11), and recommendation quality (ch06).

**Scope an ambiguous design brief**: UX/UI/CX layer (ch12), Double Diamond (ch14), start-with-intent (ch19), user flow (ch16).

**Build a portfolio or run a UX job search**: narrative first and mapped to job descriptions (ch24), 5-step search with criteria and one tracker (ch25), learning path and case-study contents (ch23).

**Get buy-in for research / run a small study**: interview the sceptic, mine existing data, one narrow test on the metric that matters (ch26), then recruit and run it (ch27).

**Recruit participants and run sessions or a before/after benchmark**: sources, screening, one-hour sessions, discussion guide, top-tasks benchmark (ch27).

**Define users and scope features or a website**: personas and mental-model workshop (ch28), profiles, goal scoring, value/difficulty, content-first site build (ch29).

**Validate before building**: prototype at the right fidelity, storyboard, design sprint (ch30).

**Design automation, predictions or recommendations**: suggest, do not silently decide; reversible and transparent (ch31).

**Redesign a transaction, kiosk or gesture**: frequency hierarchy, outcomes over codes, one gesture one meaning (ch32).

**Build a component library**: atomic design from page patterns (ch33).

**Audit or redesign an existing interface (app, kiosk, site)**: name the goal, one purpose per screen, merge duplicates, rank by frequency (ch34); check signals, contrast and context of use (ch35).

**Plan content for a site or app**: content model, audit, style guide, design for variance (ch36); survey method for customer language (ch27).

**Make an app feel premium or trustworthy**: eight premium traits, detail audit, ten trust levers, friction only where stakes are high (ch37).

**Design or fix onboarding, permission prompts, paywall or cancellation**: three failure points, pre-permission screens, progress, aha moment, paywall model by price, short honest cancel flow (ch38).

**Improve retention or add habit mechanics**: five tactics, loop model, diagnose the drop by cohort, ethics decision rules (ch39, with ch20).

**Use AI tools to generate UI, hand off to developers or run design QA**: intern briefing, one screen at a time, PRD-first build, file hygiene, QA issue fields (ch40).

**Decide what to polish versus ship, or run a UX audit tied to results**: ship/polish rules, closed-beta launch, five-step audit with five lenses and impact-effort grid (ch41, with ch34).

**Run a workshop or design sprint with stakeholders**: hand off the process design, exercises and timing to `workshop-facilitation` (ch01, ch07); keep the research questions and usability evidence here (ch05, ch08).

---

## Core Frameworks & Mental Models

### Research

**Strategic vs. tactical**: strategic research (= foundational = generative = exploratory = discovery) builds long-term knowledge of who the users are. Tactical (= evaluative) tests existing ideas: formative before launch, summative after. Use "strategic/tactical" with leadership and "generative/evaluative" with product teams, consistently.

**Study plan**: background/problem → objectives + explicit non-objectives → research questions + success metrics → timeline + DACI → methodology (methods, participants, sample, materials) → a procedure someone else could replicate. **Who / Question / Why** for every question filters out what analytics answers better.

**Sample sizes**: usability testing needs 5 participants per design (finds ~80-85% of issues; recruit 6-8). Card sort needs 10-15 moderated or 20-30+ unmoderated; open builds a new IA, closed validates one. Under n≈30, never report bare percentages: use quantity words + the raw number, and prioritise issues by prevalence × frequency × severity.

**Experiments and ethics**: between-subjects avoids order effects but needs more people (randomise). Within-subjects needs fewer but must be counterbalanced (n! orderings, not a Latin Square). Run the Belmont checklist (respect for persons, beneficence, justice, fidelity, integrity) before any study.

**Recommendations and influence**: recommendations are data-driven, feasible, prioritised, blame-free and concise. Influence (earned, mutual) beats persuasion (one-way). With a resistant stakeholder, open Affiliative, then switch to Democratic (Goleman).

**Impact and ROI**: decide what to measure → baseline → measure continuously → show before/after with the story. Payback = yearly loss from the problem ÷ cost of the fix; a fix after development costs ~100× more. For quoting UX/UI work, paid discovery phases and value-based fees see `pricing-and-sales-negotiation` ch01, ch05, ch07.

**Buy-in and minimum viable research** (ch26): treat "no" as a UX problem; interview the sceptic, tie the proposal to one live metric, mine existing data, run one narrow study on the biggest drop-off, lead with the insight and session video. Analytics shows what, people show why.

**Recruiting** (ch27): friends, family and street tests mislead; recruit in communities, reviews and your own users (including drop-offs); screen everyone; 1-hour sessions. Top-tasks benchmark: 10-12 tasks, 15-18 users, 80% success target, repeat after redesign.

**Scoping workshops** (ch29): 3-5 profiles, four-moment user stories, goal scoring (obtainability x desirability), value/difficulty matrix or MoSCoW, content-first site build.

**Anticipatory design** (ch31): offer, explain, allow reversal; ask first on high stakes.

### Design

**UX / UI / CX**: UI (the visible layer) ⊂ UX (perception from use or anticipated use) ⊂ CX (every touchpoint, including sales and support). **UX Iceberg**: visual design is the visible tip, with structure, scope and strategy underneath. Prioritise bottom-up.

**Double Diamond**: Discover (wide) → Define (narrow) → Develop (wide, sketch several directions before hi-fi) → Deliver (narrow, test and iterate). **Start with intent**: name the user's intent before layout, follow conventions unless breaking them helps the user, and use progressive disclosure.

**Beginner UI mistakes**: unplanned flow, piled-up effects, poor spacing, inconsistent components, weak icons, redundant elements, no interaction feedback, overdesigned charts. Removing usually beats adding.

**Fundamentals**: hierarchy comes from contrast in size, weight, position and color. One typeface is enough. Use 4/8px spacing. Build color from one primary's tints and shades plus semantic colors (blue trust, red danger, yellow warning, green success). Dark mode needs lighter surfaces instead of shadows. Every interactive element needs default/hover/active/disabled, and inputs also need focus and error.

**Typography laws** (ch21): hierarchy; proximity; line height that shrinks as size grows (body 1.4-1.5×, headings 1.1-1.2×); chunking; serial position (context first, CTA last); 1 font family, 2 at most; 45-75 characters per line; left-aligned body text; WCAG contrast 4.5:1 (3:1 for large text). **UX writing**: Clear → Concise → Useful, revised in that order. Fix widows and orphans with `text-wrap: balance/pretty`, `orphans/widows: 2` and a sparing `&nbsp;`.

**Color systems** (ch22): **60-30-10**: a neutral dominant, a supporting secondary, and an accent reserved for the primary CTA. It can be reapplied per section as a micro-palette. Analogous colors give harmony; a complementary color isolates the accent. Generate variants in HSL (fix the hue, vary saturation and lightness). Name tokens by role (`--color-accent`), not by hue. Never convey information through color alone; the European Accessibility Act makes this a legal duty for most businesses.

**UX psychology** (ch20): cognitive overload (too much information) differs from choice overload (too many options). Processing fluency makes simpler layouts read as higher quality. Variable reward is the strongest and riskiest engagement loop. Hedonic adaptation means static experiences fade. Goal gradient: show how close the finish line is. Peak-end: polish the peak and the ending. Labor illusion: visible effort raises trust for sensitive actions. Von Restorff: make only what matters stand out.

**Product UX** (ch37-ch41): premium feel = eight deliberate traits (anticipate, pace transitions, delight, know when not to animate, invisible consistency, intentional empty states, reward discovery, prescriptive errors); trust = ten levers, with friction added only on irreversible or sensitive actions. Onboarding fails by asking too much first, not setting expectations, or feeling generic; ask for permissions only after a pre-permission screen; keep cancellation as easy as sign-up. Retention rests on personalization, a fast aha moment, habit loops, community and switching costs, used only where the mechanic serves the user's goal. With AI tools: brief like an intern, one screen and one reference at a time, state prohibitions, review hierarchy and consistency. Polish only screens on conversion steps that have enough traffic; audit with a goal, five lenses (clarity, flow, hierarchy, consistency, density) and an impact-effort grid.

---

## Chapter Index

| # | Title | Key Frameworks |
|---|-------|----------------|
| [ch01](chapters/ch01-foundations.md) | Foundations: What UX Research Is | Scientific-method mapping, problem spotters vs. solvers |
| [ch02](chapters/ch02-stakeholders-team.md) | Stakeholders, Daily Life, Team Structure | Four core stakeholders, embedded/consulting/hybrid models |
| [ch03](chapters/ch03-types-of-research.md) | Types of Research & Business Acumen | Strategic vs. tactical map, concept testing, Campbell's Law |
| [ch04](chapters/ch04-research-roadmap.md) | The Research Roadmap | Roadmap scope rule, quarterly planning, buffer time |
| [ch05](chapters/ch05-study-plan.md) | Crafting the Study Plan | Study plan structure, Who/Question/Why, screener table |
| [ch06](chapters/ch06-stakeholders-in-session.md) | Live Sessions & Recommendations | Stakeholder-gone-wild scenarios, recommendation quality |
| [ch07](chapters/ch07-data-analysis.md) | Data Analysis: AI, Deliverables, Small Samples | Human-plus-AI sequence, small-sample reporting |
| [ch08](chapters/ch08-qualitative-methods.md) | Core Qualitative Methods | Magic number five, card sort, contextual inquiry, diary studies |
| [ch09](chapters/ch09-experimental-design-ethics.md) | Experimental Design & Ethics | Between/within-subjects, counterbalancing, Belmont Report |
| [ch10](chapters/ch10-measuring-impact.md) | Measuring & Tracking Impact | Four kinds of impact, 5 steps to measuring UX success |
| [ch11](chapters/ch11-leadership-influence.md) | Leadership, Influence, Communication | Goleman styles, influence vs. persuasion, communication styles |
| [ch12](chapters/ch12-ucd-ux-ui-cx.md) | User-Centred Design & UX/UI/CX | Scope model, UX Iceberg, 5 UCD principles |
| [ch13](chapters/ch13-roi-of-ux.md) | The ROI of User Experience | Cost-of-error multiplier, ROI model, failure causes |
| [ch14](chapters/ch14-double-diamond-process.md) | Applying the Double Diamond | Discover/Define/Develop/Deliver, t-shirt sizing |
| [ch15](chapters/ch15-researcher-project-cycle.md) | The Researcher's Project Cycle | Six-step cycle, bias replacement, qualitative impact |
| [ch16](chapters/ch16-user-flow-diagrams.md) | User Flow Diagrams | Notation, decision points, sub-flows |
| [ch17](chapters/ch17-beginner-ui-mistakes.md) | Common Beginner UI Mistakes & Fixes | 7+1 mistakes checklist |
| [ch18](chapters/ch18-visual-interaction-fundamentals.md) | Visual & Interaction Fundamentals | Affordances, hierarchy, grids, typography, color, dark mode, shadows, states, micro-interactions |
| [ch19](chapters/ch19-designing-around-user-intent.md) | Designing Around User Intent | Start-with-intent, conventions, progressive disclosure, design systems |
| [ch20](chapters/ch20-psychology-of-ux.md) | The Psychology Behind UI/UX | Cognitive/choice overload, fluency, conditioning, variable reward, goal gradient, peak-end, labor illusion, Von Restorff |
| [ch21](chapters/ch21-typography-laws-ux-writing.md) | Typography Laws, UX Writing, Micro-Typography | 9 typography laws, 3 C's, UX writer role, widows/orphans |
| [ch22](chapters/ch22-color-systems-60-30-10.md) | Color Systems | 60-30-10, color wheel, micro-palettes, HSL, design tokens, free tools, EAA |
| [ch23](chapters/ch23-learning-ux-portfolio-and-accessibility-checks.md) | Learning UX, Case Studies, First Accessibility Checks | informational interviews, self-initiated project, case-study contents, low-vision checks, working with other design roles |
| [ch24](chapters/ch24-ux-portfolio-and-case-study-narrative.md) | The UX Portfolio and Case-Study Narrative | narrative first, claim then proof, deck vs site, case-study skeleton |
| [ch25](chapters/ch25-ux-job-search-and-career-skills.md) | The UX Job Search and Career Skills | 5-step search, role landscape, neglected skills |
| [ch26](chapters/ch26-winning-research-buy-in-minimum-viable-research.md) | Winning Research Buy-In, Minimum Viable Research | MVR sequence, five benefits, what vs why, bookends |
| [ch27](chapters/ch27-recruiting-and-running-practical-research-sessions.md) | Recruiting and Running Practical Sessions | sources, guerrilla pitfalls, discussion guide, top-tasks benchmark |
| [ch28](chapters/ch28-personas-archetypes-and-mental-modeling.md) | Personas, Archetypes, Mental Modeling | research-based personas, first questions, mental-model workshop |
| [ch29](chapters/ch29-workshops-feature-prioritisation-and-website-process.md) | Workshops, Feature Prioritisation, Website Process | goal scoring, basket weaving, value/difficulty, MoSCoW, build order |
| [ch30](chapters/ch30-prototyping-early-and-design-sprints.md) | Prototyping Early and Design Sprints | fidelity by audience, storyboard, sprint intake and test day |
| [ch31](chapters/ch31-anticipatory-design-and-automation.md) | Anticipatory Design and Automation | 3 cautions, 5 principles, kill switch |
| [ch32](chapters/ch32-transactional-flows-and-gesture-design.md) | Transactional Flows and Gesture Design | frequency hierarchy, codes to outcomes, gesture rules |
| [ch33](chapters/ch33-atomic-design-component-library.md) | Atomic Design | atoms to pages, 6-step extraction |
| [ch34](chapters/ch34-interface-audit-and-redesign-method.md) | Interface Audit and Redesign Method | 3 redesign goals, audit order, merge duplicates, navigation fixes |
| [ch35](chapters/ch35-interface-craft-and-context-of-use.md) | Interface Craft and Context of Use | meaningful shadow/colour/shape, translucent contrast, status and range, low-attention controls |
| [ch36](chapters/ch36-content-modelling-and-ux-content-strategy.md) | Content Modelling and UX Content Strategy | content model, audit, design for variance, editors as users |
| [ch37](chapters/ch37-perceived-quality-premium-feel-and-trust.md) | Perceived Quality, Premium Feel and Trust | 8 premium traits, detail audit, perceived value, 10 trust levers |
| [ch38](chapters/ch38-onboarding-permissions-paywall-and-cancellation.md) | Onboarding, Permissions, Paywall and Cancellation | 3 failure points, pre-permission screens, paywall models, honest cancel flow |
| [ch39](chapters/ch39-retention-habit-mechanics-and-ethics.md) | Retention and Habit Mechanics, with Ethics | 5 tactics, loop model, cohort diagnosis, ethics rules |
| [ch40](chapters/ch40-ai-assisted-ui-workflow-and-design-to-code-handoff.md) | AI-Assisted UI, Design-to-Code Handoff, Design QA | 5 generation rules, PRD-first build, file structure, QA issue fields |
| [ch41](chapters/ch41-shipping-vs-polishing-and-results-driven-ux-audit.md) | Shipping vs Polishing, Results-Driven UX Audit | ship/polish rules, closed beta, 5-step audit, 5 lenses, impact-effort |

## Topic Index

- **Abandonment / drop-off rate** → ch13, ch38, ch41
- **AI-generated UI / prompts / design-to-code / MCP** → ch40
- **Attribution question ("where did you find us")** → ch38, ch41
- **Cancellation flow / paywall / freemium vs hard paywall** → ch38
- **Design QA / handoff / Dev Ready file structure** → ch40
- **Dark patterns / habit ethics / streaks / notifications** → ch39
- **Empty states / prescriptive errors** → ch37, ch38
- **Impact-effort grid / five audit lenses / UX audit** → ch41
- **Onboarding / permission prompts / aha moment** → ch38
- **Premium feel / perceived quality / invisible consistency** → ch37
- **Retention / habit loops / switching cost** → ch39
- **Ship vs polish / closed beta / validation** → ch41
- **Trust levers / friction at key moments** → ch37
- **Accessibility (contrast, EAA, color alone)** → ch21, ch22
- **Affordances & signifiers** → ch18
- **AI-assisted analysis** → ch07
- **Alignment (text)** → ch21
- **Anticipated use** → ch12
- **Anticipatory design / automation** → ch31
- **Archetype / persona** → ch28
- **Atomic design** → ch33
- **Auto-layout** → ch17
- **Basket weaving / feature prioritisation / MoSCoW / value-difficulty** → ch29
- **Belmont Report / ethics** → ch09
- **Between/within-subjects design** → ch09
- **Redesign audit / duplicate pages / navigation cleanup** → ch34
- **Business acumen** → ch03
- **Card sorting** → ch08
- **Case study / portfolio (relevance filter, cover letter)** → ch23, ch24
- **Charts (overdesigned)** → ch17
- **Choice overload** → ch20
- **Chunking (Miller's Law)** → ch21
- **Classical conditioning (notifications)** → ch20
- **Cognitive overload** → ch20
- **Content model / content strategy / content audit** → ch36
- **Color psychology** → ch20
- **Color theory / color wheel** → ch18, ch22
- **Communication styles** → ch11
- **Component consistency** → ch17
- **Concept testing** → ch03
- **Contrast ratio (WCAG)** → ch21
- **Conversion rate** → ch13
- **Cost-of-error multiplier** → ch13
- **Counterbalancing / Latin Square** → ch09
- **CX (customer experience)** → ch12
- **DACI** → ch05
- **Dark mode** → ch18
- **Decision point (user flow)** → ch16
- **Design sprint** → ch30
- **Design system** → ch19
- **Design tokens (semantic color)** → ch22
- **Desire path** → ch12
- **Diary studies** → ch08
- **Discussion guide (interview)** → ch27
- **Dopamine-driven engagement** → ch20
- **Double Diamond** → ch14
- **Empathy / empathy map** → ch07, ch11
- **Feedback & component states** → ch18
- **Font pairing** → ch21
- **Friends and family / guerrilla testing** → ch27
- **Gestalt proximity (spacing)** → ch21
- **Gestures** → ch32
- **Goal gradient effect** → ch20
- **Goal scoring / user stories** → ch29
- **Goleman leadership styles** → ch11
- **Hedonic adaptation** → ch20
- **HSL color variants** → ch22
- **Impact measurement** → ch10
- **Influence vs. persuasion** → ch11
- **Information architecture** → ch08, ch12
- **Job search / job descriptions / product designer role** → ch25
- **Labor illusion** → ch20
- **Leadership theories** → ch11
- **Line height / line length** → ch21
- **Magic number five (sample size)** → ch08
- **Mental modeling** → ch28
- **Micro-interactions** → ch18
- **Micro-palette (section-level color)** → ch22
- **Microcopy / UX writing (3 C's)** → ch21
- **Minimum viable research / research buy-in** → ch26
- **Non-breaking space / widows / orphans** → ch21
- **Participant recruiting** → ch27
- **Peak-end rule** → ch20
- **Processing fluency** → ch20
- **Progressive disclosure** → ch19
- **Prototype fidelity / storyboard** → ch30
- **Recommendations (writing)** → ch06
- **Reinforcement (positive / intermittent)** → ch20
- **Research project cycle** → ch15
- **Research roadmap** → ch04
- **ROI of UX (payback period)** → ch13
- **Sample size (small-N reporting)** → ch07, ch08
- **Screener design** → ch05
- **Serial position effect** → ch21
- **Shadows (depth, meaning)** → ch18, ch35
- **Shape per content type / button hierarchy** → ch35
- **Translucent surfaces / glass contrast** → ch35
- **Low-attention and physical interfaces (alarm, camera, intercom)** → ch35
- **60-30-10 rule** → ch22
- **Spacing system (4/8px)** → ch17, ch18
- **Stakeholder collaboration** → ch02, ch06
- **Study plan** → ch05
- **Survey (three zones, screener, categories)** → ch27
- **Team structure** → ch02
- **T-shirt sizing** → ch14
- **Top-tasks benchmark** → ch27
- **Types of research** → ch03
- **Typography laws** → ch18, ch21
- **UCD principles / UX Iceberg / scope model** → ch12
- **Usability testing** → ch08
- **User flow notation** → ch16
- **User intent** → ch19
- **UX writer (role)** → ch21
- **Visual hierarchy** → ch18
- **Von Restorff effect** → ch20
- **Website process / sitemap / landing page sequence** → ch29

## Related Skills

- `presentation-design`: the same visual fundamentals applied to slides (PowerPoint, Keynote, Canva, Google Slides).
- `creative-director`: concepts, copy and visual literacy beyond interface work.
- `depth-psychology`: motives and defences of people (this skill's ch20 covers behavioural psychology in products).
- `public-speaking-persuasion`: presenting research findings and pitching UX work.
- `freelance-designer-ops`: pipeline, client acquisition, content and organisation for the career chapters (ch24, ch25); growth and marketing of the product itself is outside this skill.
- `workshop-facilitation`: running workshops and design sprints (agenda, silent work, voting, remote).
- `pricing-and-sales-negotiation`: quoting UX/UI work and paid discovery.

## Scope & Limits

Thin coverage: resume/ATS formatting, interview answers and hiring-side scoring are not covered (ch25 gives search strategy and role definitions only); say so rather than inventing advice.

## Scope & Limits

Covers UX research practice and UI design fundamentals as listed above. Product growth, marketing, content and client acquisition are not covered here (see `freelance-designer-ops`). Not covered: advanced statistics (confidence intervals, significance testing), full WCAG audits beyond contrast and color, and tool tutorials (Figma etc.). Say so when a question goes beyond these chapters instead of inventing rules.
