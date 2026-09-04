# Patterns — UX/UI Research & Leadership Expert

## Research Roadmap Planning
**When to use**: quarterly (or longer) planning across 2+ concurrent research projects.
**How**: gather stakeholder priorities → sequence highest-priority project first (kickoff → desk research → recruit → draft plan → feedback → pilot → sessions → analysis → readout → ideation if foundational) → stagger lower-priority project's studies so no two studies run the same week → always insert buffer time for recruiting delays.
**Trade-offs**: roadmaps beyond one quarter have low confidence of being followed exactly — treat as directional, not contractual; revisit as priorities shift.

## Study Plan Template
**When to use**: every study, as the alignment and record-keeping artifact.
**How**: Background/Problem → Objectives + Non-Objectives → Research Questions + success metrics → Timeline + DACI → Methodology (methods, participants, sample size, materials) → Procedure/Discussion Guide.
**Trade-offs**: first draft should take minutes if the kickoff meeting was thorough; over-investing in a "perfect" first draft wastes time better spent getting stakeholder feedback.

## Who / Question / Why Framework
**When to use**: drafting research questions for any study.
**How**: 3-column table — Who (target audience/segment) | Question (the research question) | Why (what you'll do with the answer). Use it to filter out questions analytics can answer better than qualitative research (e.g., click-through rates).
**Trade-offs**: adds a planning step, but prevents wasted interview time on unanswerable or purposeless questions.

## Method/Sample Organization Table
**When to use**: study plans with multiple methods or participant segments.
**How**: columns for Method | What You're Trying to Learn | Participant Segment; add sub-rows per segment if a method needs different questions for different groups.
**Trade-offs**: extra table maintenance, but prevents muddled methodology sections.

## Screener Table (Track / Question / Why)
**When to use**: designing recruiting screeners.
**How**: columns for Track (which answer routes to which next question or exclusion) | Question | Why (purpose: hard screen-out vs. quota/profiling). Distinguish true exclusion criteria from quota-balancing criteria.
**Trade-offs**: more upfront design time, but produces a screener stakeholders can audit and trust.

## Handling a Stakeholder Going Wild (Live Session)
**When to use**: any observed remote/in-person session with stakeholders watching.
**How**: mic/camera slip → message privately, use it to introduce them to the participant. Chat-flooding with questions → acknowledge ("got it," "I'll cover it," "circle back later") without ignoring. Unmuting to ask directly → let them finish, neutrally reframe if leading, then privately ask them to relay future questions through you.
**Trade-offs**: requires real-time diplomatic judgment; over-correcting (calling someone out on-call) damages the relationship more than the interruption did.

## Counterbalancing / Pseudorandomization
**When to use**: within-subjects designs with 2+ conditions.
**How**: compute n! for the number of possible orderings, list them, randomly assign participants to an ordering (e.g., `=RANDBETWEEN(1, n!)` in a spreadsheet). Cap conditions at ~3 to keep combinatorics manageable.
**Trade-offs**: avoid the Latin Square shortcut — it removes randomness but keeps a systematic order bias (A always before B).

## Human-Plus-AI Analysis
**When to use**: qualitative synthesis sessions, especially time-constrained ones.
**How**: duplicate raw data (never edit the original) → hand-analyze/affinity-diagram first → duplicate that result → run AI clustering (by keyword, then optionally by sentiment) on top → compare AI themes to your own for a different perspective.
**Trade-offs**: AI-only clustering/summarization is unreliable (misattributes quotes between participants) — always verify against source data before sharing with stakeholders.

## Small-Sample Reporting
**When to use**: any qualitative study readout, typically n<30.
**How**: never report bare percentages; use quantity words (none/a few/some/most/all) paired with the raw number (e.g., "most participants (7 of 8)..."). For usability issues, triage with Prevalence × Frequency × Severity rather than raw counts.
**Trade-offs**: less precise-sounding than a percentage, but avoids misleading stakeholders about statistical confidence you don't have.

## Card Sort Procedure (5 Steps)
**When to use**: designing or validating information architecture.
**How**: (1) prepare labeled + blank cards; (2) instruct participants to think aloud while sorting, probe on hesitation; (3) review formed groups, ask if any should merge/split; (4) have participants label each group; (5) photograph/screenshot the result. Open card sort for new IA, closed for validating existing IA. Moderated: 10-15 participants; unmoderated: 20-30+.
**Trade-offs**: moderated sorts cost more time per participant but need fewer people and yield richer rationale; unmoderated scales cheaply but loses the "why."

## Communication Style Matching
**When to use**: navigating friction with a colleague or stakeholder.
**How**: identify their style on the Direct/Spirited/Considerate/Systematic grid (assertiveness × expressiveness); expect the most friction with your diagonal opposite; adapt tone/pacing to their style rather than defaulting to your own.
**Trade-offs**: requires ongoing social calibration rather than a one-size-fits-all communication approach.

## Gaining Influence (Affiliative → Democratic Sequence)
**When to use**: proposing a change to a skeptical or resistant stakeholder.
**How**: start Affiliative — ask non-judgmental questions to understand their current view and rationale ("how do you decide to do this today?"); once understood, shift Democratic — offer suggestions and invite their input ("I think X, what do you think?").
**Trade-offs**: slower than simply asserting a recommendation, but builds durable influence instead of one-off persuasion.

## Scoping a UX / UI / CX Problem
**When to use**: a cross-functional disagreement about whose job a problem is, or which layer of work will fix it.
**How**: classify the reported problem — is it about the interaction/flow/behavior (UX), the visual/interface layer (UI), or a broader journey spanning multiple touchpoints including sales/support (CX)? Match the fix to the layer: don't visually polish (UI) a task-flow problem (UX); don't redesign a flow when the real gap is a broken handoff to customer service (CX).
**Trade-offs**: adds a classification step before jumping to solutions, but prevents fixing the wrong layer and re-surfacing the same complaint later.

## Bottom-Up Prioritization via the UX Iceberg
**When to use**: a stakeholder wants to jump straight to visual design/UI before strategy or IA is defined.
**How**: name the iceberg layer being skipped (strategy → functional specs/content → interface/IA → visual design) and insist on resolving it before moving up. Visual design is only ~10% of the work and depends on everything beneath it being settled.
**Trade-offs**: slows down visible progress early, but prevents costly visual rework once the underlying structure changes.

## Building a UX ROI Business Case
**When to use**: justifying a UX research/design investment to stakeholders who think in dollars, not usability heuristics.
**How**: (1) estimate current loss — daily/annual lost conversions or revenue from the known UX problem; (2) estimate fix cost — research/design + implementation; (3) divide fix cost by recovered loss per period to get payback period; (4) present everything after payback as net gain, and map the improvement to a stakeholder-legible metric (conversion, drop-off, support volume, training time, error rate, dev time).
**Trade-offs**: requires reasonably confident loss estimates up front; a rough estimate is still more persuasive than no number at all, but a wrong estimate can undermine credibility — state assumptions explicitly.

## Scoping an Ambiguous Design Prompt (Double Diamond)
**When to use**: a broad, vague redesign prompt with too many possible sub-problems to start on directly.
**How**: Discover — audit current design, gather qual (user research/surveys) and quant (usage metrics) data, run competitive analysis. Define — synthesize findings with cross-functional partners, prioritize, t-shirt size. Develop — sketch multiple rough directions before high-fidelity tools. Deliver — run multiple testing/iteration rounds, review with cross-functional partners, ship.
**Trade-offs**: adds structured overhead to a prompt that might tempt a quick solution; pays off by preventing wasted effort on the wrong sub-problem.

## Running a Research Project (6-Step Cycle)
**When to use**: any research engagement, from a quick usability check to a multi-week study.
**How**: surface the knowledge gap in cross-functional conversation → define the specific question, known/unknown, timeline, segments → write the research plan (goals, timeline, participants, questions) → recruit and write a guided script with probes → facilitate sessions (record, invite stakeholders to observe) → synthesize findings into a share-out and present, ending in a next-steps/solutioning discussion.
**Trade-offs**: skipping the "define the question" step to save time usually costs more later in a study that answers the wrong thing.

## Mapping a User Flow
**When to use**: designing or reviewing any multi-step task (onboarding, checkout, login) before or during implementation.
**How**: start with a circle (entry point); connect steps in sequence with solid lines for the preferred path; add diamonds at every decision point and route both outcomes somewhere (never a dead end); use dotted lines for alternative actions (back, retry); branch complex alternate journeys (e.g., password recovery) into their own linked sub-flow rather than overloading the main diagram.
**Trade-offs**: takes upfront diagramming time, but is far cheaper than discovering a missing error state after the feature ships.

## Beginner UI Self-Review Pass
**When to use**: before considering any UI screen or flow "done," especially with less design experience.
**How**: walk the 7+1 checklist in order — (1) is the full flow sketched, including edge cases? (2) are effects (shadows/gradients) minimal and single-color-family? (3) is spacing grid/auto-layout driven with generous whitespace? (4) do repeated components share one style/variable/component definition? (5) are icons consistent in style, labeled where non-obvious? (6) is every element functional, or is it clutter? (7) does every action produce visible feedback? (+8) if there's a chart, is it legible before it's pretty?
**Trade-offs**: adds a review pass, but catches the specific issues that most reliably signal inexperience to a trained eye.

## Building Visual Hierarchy
**When to use**: any screen where multiple pieces of information compete for attention.
**How**: pick the single most important element and make it larger, bolder, more colorful, and positioned higher than everything else; push secondary information (metadata, timestamps) smaller and lower; use an image near the top as a fast color/scan anchor when available.
**Trade-offs**: over-applying contrast to too many elements flattens the hierarchy back out — reserve strong contrast for the one or two things that matter most per screen.

## Building a Color System from One Primary
**When to use**: starting color decisions for a new design or design system.
**How**: pick one primary/brand color; derive a light tint for backgrounds and a dark shade for text from it; layer in semantic colors with fixed meaning (blue=trust, red=danger, yellow=warning, green=success) only where that meaning is needed (alerts, states, chips).
**Trade-offs**: simpler and more consistent than picking colors ad hoc per screen, but requires discipline not to introduce off-system colors later for one-off decorative purposes.

## Start-with-Intent Scoping
**When to use**: beginning any new design task, before opening a design tool.
**How**: name the specific user intent(s) the design must serve; design the minimal UI that serves the primary intent; only add UI for a second intent once it's confirmed as real and distinct — don't let icon/layout exploration substitute for this step.
**Trade-offs**: feels slower than jumping straight into visuals, but prevents building polished UI that doesn't map to any real user goal.

## Auditing a Design for Cognitive Overload
**When to use**: a screen feels overwhelming or users report confusion despite the feature working correctly.
**How**: count how much information/how many choices are shown simultaneously; cut or progressively disclose anything not needed for the user's immediate intent; check whether color/visual noise (not just text volume) is contributing to the load.
**Trade-offs**: trims content that stakeholders may want visible "just in case" — requires being able to justify removals by user intent, not just aesthetic preference.

## Designing an Ethical Reinforcement Loop
**When to use**: adding any reward, notification, or refresh mechanic intended to drive repeat engagement.
**How**: identify whether the reward is consistent (predictable) or variable (intermittent); variable rewards drive stronger engagement but carry higher compulsive-use risk — weigh that tradeoff explicitly rather than defaulting to variable reward for growth metrics alone; pair engagement mechanics with user-control features (easy opt-out, visible frequency settings) to offset the risk.
**Trade-offs**: a more ethical, predictable reward system will likely produce lower raw engagement numbers than an unpredictable one — a deliberate tradeoff between growth and user wellbeing.
