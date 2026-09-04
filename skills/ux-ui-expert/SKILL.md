---
name: ux-ui-expert
description: "UX/UI research and design knowledge base covering study plans, research roadmaps, the researcher's project cycle, usability-testing/card-sort/diary-study sample sizes, small-sample reporting, experimental design, research ethics (Belmont Report), stakeholder leadership/influence, the UX/UI/CX distinction with user-centred design principles, the ROI of UX, the Double Diamond design process, user flow diagrams, common beginner UI mistakes, visual/interaction design fundamentals (hierarchy, grids, typography, color, states), designing around user intent, and the psychology behind UI/UX (cognitive load, conditioning, reinforcement, hedonic adaptation). Use when planning UX research or design work, choosing methods or sample sizes, writing recommendations, leading/influencing stakeholders, scoping UX vs. UI vs. CX work, building a business case for UX investment, mapping a user flow, reviewing a UI for common mistakes, applying visual design fundamentals, or reasoning about why a design choice affects user behavior/engagement."
allowed-tools:
  - Read
  - Grep
argument-hint: [topic, framework name, or chapter number]
---

# UX/UI Research & Leadership Expert

## How to Use This Skill

- **Without arguments** — load core frameworks below for reference
- **With a topic** — ask about `study plan`, `sample size`, `ethics`, or another indexed topic; I find and read the relevant chapter
- **With a chapter** — ask for `ch05`; I load that specific chapter file
- **Browse** — ask "what chapters do you have?" to see the full index

When you ask about a topic not covered in Core Frameworks below, I will read the relevant chapter file before answering.

---

## Core Frameworks & Mental Models

**Strategic vs. Tactical Research Map**: Strategic research (= foundational = generative = exploratory = discovery, all the same thing) is big-picture, long-term, and builds the knowledge base of who users are. Tactical research (= evaluative) tests existing ideas/prototypes, splitting into formative (pre-launch, improve) and summative (post-launch, measure at scale). Use "strategic/tactical" language with leadership, "generative/evaluative" with product teams — pick one set per audience and stick with it.

**Study Plan Structure**: Background/Problem (why now) → Objectives + Non-Objectives (explicitly scope out what you won't study) → Research Questions + success metrics → Timeline + DACI (who's doing what, when) → Methodology (methods, participants, sample size, materials) → Procedure/Discussion Guide (a "recipe" someone else could replicate). First drafts should take minutes after a good kickoff meeting — treat drafts as drafts, get stakeholder feedback before running.

**Who / Question / Why Framework**: structure every research question with 3 columns — Who you're learning from, the Question itself, and Why (what you'll do with the answer). Filters out questions analytics can answer better than qualitative interviews (e.g., "how many people click X" is not a qualitative-research question).

**The Magic Number Five**: 5 participants in a usability test uncover ~80-85% of usability issues (Nielsen/Virzi/Lewis). Recruit 6-8 for no-show buffer. Holds per design being tested, regardless of how many demographic segments you sample from, unless you have a strong hypothesis that segments differ enough to need separate localized studies.

**Card Sorting**: Open card sort (no predefined categories) builds new information architecture; Closed card sort (predefined categories) validates existing IA. Moderated sorts need 10-15 participants; unmoderated need 20-30+.

**Small-Sample Reporting Rule**: never report bare percentages under n≈30 (Central Limit Theorem rule of thumb). Use quantity words (none/a few/some/most/all) paired with the raw number. Prioritize usability issues by Prevalence × Frequency × Severity, not raw counts.

**Between-Subjects vs. Within-Subjects**: Between-subjects (each participant sees one condition) avoids order effects but needs a bigger sample — fix individual-difference risk with random assignment. Within-subjects (each participant sees all conditions) needs a smaller sample and yields comparison data, but risks order effects — fix with counterbalancing (compute n! possible orderings, randomly assign; avoid the Latin Square shortcut, which still embeds systematic bias).

**Belmont Report's Five Ethics Principles**: Respect for Persons (autonomy, informed consent, debrief), Beneficence (do no harm, maximize benefit), Justice (fair distribution of costs/benefits), Fidelity and Responsibility (build trust, own the repercussions), Integrity (honesty and accuracy — never fabricate data). Apply this checklist before fielding any study, especially without a formal IRB.

**Manipulation vs. Coercion vs. Persuasion vs. Influence**: Manipulation is one-sided control for short-term selfish gain; Coercion is force/threats (unethical); Persuasion is "something you do" — short-term, one-directional convincing; Influence is "something you earn" — long-term, mutual, cooperative, win-win. Build influence, not persuasion, with resistant stakeholders.

**Goleman's Six Leadership Styles**: Affiliative, Visionary, Coaching, Democratic are good defaults; Coercive/Commanding and Pace-Setting are situational only. Start Affiliative (non-judgmental questions to understand) then shift Democratic (offer suggestions, invite input) when proposing change to a resistant stakeholder — apply the same curious, research-like posture to teammates that you use with participants.

**Recommendation Quality Bar**: good recommendations are data-driven, feasible, appropriately prioritized (impact/severity/prevalence/frequency), never blame the user, and are concise (context lives separately from the one-line recommendation). Avoid single-solution framing, non-data-driven suggestions, and reflexive "more research is needed."

**5 Steps to Measuring UX Success**: decide what to measure (tied to real objectives) → plan the study → conduct a baseline/benchmark study → continuously measure against that baseline → visualize before/after and tell the story (pair numbers with qualitative narrative).

**UX / UI / CX Scope Model**: UX = perceptions and responses from using (or anticipating) a product; UI = the visible interface layer (visual design, layout, branding); CX = the full customer journey across every touchpoint, including sales and support. UI is a subset of UX; CX is the superset. A fix at one layer doesn't resolve a problem at another.

**The UX Iceberg**: visual design is the visible ~10% tip. Beneath it: interface design (structure, navigation, information architecture) → functional specs/content requirements → strategy (users, objectives) at the base. Priorities are set bottom-up even though the deliverable is built top-down in visibility.

**ROI Calculation Model**: (current daily/annual loss from a UX problem) ÷ (research + implementation fix cost) = payback period. Fixing an error post-development costs ~100x fixing it before/during development. Three of the most common project-failure causes — badly defined requirements, poor cross-team communication, stakeholder politics — are directly addressed by UX practice (stakeholder interviews, research, usability testing).

**Double Diamond Process**: Discover (go wide — explore user/business problems, qual + quant data, competitive analysis) → Define (go narrow — synthesize, prioritize, t-shirt size) → Develop (go wide — sketch multiple solution directions before high-fidelity tools) → Deliver (go narrow — multiple testing/iteration rounds, cross-functional review, ship). The wide/narrow rhythm repeats twice: once for the problem, once for the solution.

**Six-Step Research Project Cycle**: surface knowledge gap → define the question (what's known/unknown, timeline, segments) → define the research plan → recruit + write guided script → facilitate (run sessions, stakeholders observe) → synthesize and present. Research exists to replace the psychological ownership/bias of whoever built a feature with objective evidence.

**User Flow Notation**: circle = start/end, solid line = preferred path, dotted line = alternative path, diamond = decision point. Map every branch, not just the happy path, to catch missing states before implementation.

**Beginner UI Mistakes Checklist**: unplanned flow (missing edge cases), overusing effects (stacked shadows/gradients — default to removing), poor spacing (fix with grids/auto-layout), inconsistent components (fix with shared styles/variables/components), weak icon systems (consistent library, labels for non-obvious icons), redundant elements (cut visual clutter with no function), missing interactive feedback (every action needs a visible response), overdesigned charts (legibility over aesthetics).

**Visual Hierarchy & Fundamentals**: hierarchy comes from contrast (size/position/color) — most important content bigger, bolder, higher. One typeface is enough. Use a base-unit (4/8px) spacing system. Build color from one primary's tints/shades, then layer semantic color (blue=trust, red=danger, yellow=warning, green=success). Dark mode needs its own treatment (softened borders, lighter surfaces instead of shadows). Every interactive element needs default/hover/active/disabled states at minimum.

**Start-with-Intent Design**: identify the user's specific intent before choosing layout or visuals; expand functionality only when a new real intent is identified, not for aesthetic reasons. Default to established layout conventions unless deviating deliberately serves the user better. Use progressive disclosure (e.g., "load more" over infinite scroll) to keep users in control.

**Psychology of Engagement**: cognitive overload (too much info at once) is reduced by limiting what's shown and structuring how it's presented. Color carries learned meaning (red=alert, blue/green=calm) — use deliberately, not just aesthetically. Notification sounds work via classical conditioning (Pavlov) to trigger involuntary checking. Positive intermittent (unpredictable) reinforcement is the strongest engagement driver — and the mechanism requiring the most ethical scrutiny, since it's structurally identical to what drives compulsive use. Hedonic adaptation means any static experience loses its appeal over time — expect and plan for refreshes.

---

## Chapter Index

| # | Title | Key Frameworks |
|---|-------|----------------|
| [ch01](chapters/ch01-foundations.md) | Foundations — What UX Research Is | Scientific-method mapping, problem spotters vs. solvers |
| [ch02](chapters/ch02-stakeholders-team.md) | Stakeholders, Daily Life, Team Structure | Four core stakeholders, embedded/consulting/hybrid models |
| [ch03](chapters/ch03-types-of-research.md) | Types of Research & Business Acumen | Strategic vs. tactical map, concept testing, Campbell's Law |
| [ch04](chapters/ch04-research-roadmap.md) | The Research Roadmap | Roadmap scope rule, quarterly planning walkthrough, buffer time |
| [ch05](chapters/ch05-study-plan.md) | Crafting the Study Plan | Study plan structure, Who/Question/Why, screener table |
| [ch06](chapters/ch06-stakeholders-in-session.md) | Managing Live Sessions & Recommendations | Stakeholder-gone-wild scenarios, good/poor recommendation criteria |
| [ch07](chapters/ch07-data-analysis.md) | Data Analysis — AI, Deliverables, Small Samples | Human-plus-AI sequence, small-sample reporting, empathy map critique |
| [ch08](chapters/ch08-qualitative-methods.md) | Core Qualitative Methods | Magic number five, card sort procedure, contextual inquiry, diary studies |
| [ch09](chapters/ch09-experimental-design-ethics.md) | Experimental Design & Ethics | Between/within-subjects, counterbalancing, Belmont Report |
| [ch10](chapters/ch10-measuring-impact.md) | Measuring & Tracking Impact | Four kinds of impact, 5 steps to measuring UX success |
| [ch11](chapters/ch11-leadership-influence.md) | Leadership, Influence, Communication | Leadership theories, Goleman styles, influence vs. persuasion, communication styles |
| [ch12](chapters/ch12-ucd-ux-ui-cx.md) | User-Centred Design & the UX/UI/CX Distinction | UX/UI/CX scope model, UX Iceberg, 5 UCD design principles |
| [ch13](chapters/ch13-roi-of-ux.md) | The ROI of User Experience | Cost-of-error multiplier, ROI calculation model, top-12 failure causes |
| [ch14](chapters/ch14-double-diamond-process.md) | Applying the Double Diamond Design Process | Discover/Define/Develop/Deliver, t-shirt sizing |
| [ch15](chapters/ch15-researcher-project-cycle.md) | The UX Researcher's Project Cycle & Evaluation | Six-step research cycle, bias-replacement rationale, qualitative impact evaluation |
| [ch16](chapters/ch16-user-flow-diagrams.md) | User Flow Diagrams | User flow notation, decision points, sub-flows |
| [ch17](chapters/ch17-beginner-ui-mistakes.md) | Common Beginner UI Mistakes & Fixes | 7+1 mistakes checklist (flow, effects, spacing, consistency, icons, redundancy, feedback, charts) |
| [ch18](chapters/ch18-visual-interaction-fundamentals.md) | Visual & Interaction Design Fundamentals | Affordances/signifiers, visual hierarchy, grids/spacing, typography, color theory, dark mode, shadows, states, micro-interactions |
| [ch19](chapters/ch19-designing-around-user-intent.md) | Designing Around User Intent, Content & Systems | Start-with-intent process, layout conventions, progressive disclosure, design systems |
| [ch20](chapters/ch20-psychology-of-ux.md) | The Psychology Behind UI/UX Design | Cognitive overload, processing fluency, color psychology, conditioning, variable reward, hedonic adaptation |

## Topic Index

- **Abandonment/drop-off rate** → ch13
- **Affordances & signifiers** → ch18
- **Anticipated use** → ch12
- **Auto-layout** → ch17
- **Belmont Report** → ch09
- **Between/within-subjects design** → ch09
- **Business acumen** → ch03
- **Card sorting** → ch08
- **Classical conditioning (notifications)** → ch20
- **Cognitive overload** → ch20
- **Color psychology** → ch20
- **Color theory** → ch18
- **Communication styles** → ch11
- **Component consistency** → ch17
- **Concept testing** → ch03
- **Conversion rate** → ch13
- **Cost-of-error multiplier** → ch13
- **Counterbalancing** → ch09
- **Decision point (user flow)** → ch16
- **CX (customer experience)** → ch12
- **Dark mode (design)** → ch18
- **Dopamine-driven engagement** → ch20
- **Data analysis (AI-assisted)** → ch07
- **DACI** → ch05
- **Design system** → ch19
- **Desire path (design diagnostic)** → ch12
- **Diary studies** → ch08
- **Double Diamond (applied)** → ch14
- **Empathy / empathy map** → ch07, ch11
- **Ethics** → ch09
- **Feedback & states (UI)** → ch18
- **Goleman leadership styles** → ch11
- **Hedonic adaptation** → ch20
- **Impact measurement** → ch10
- **Influence vs. persuasion** → ch11
- **Information architecture** → ch12
- **Latin Square design** → ch09
- **Leadership theories** → ch11
- **Magic number five (sample size)** → ch08
- **Micro-interactions** → ch18
- **Persuasive design** → ch20
- **Positive/intermittent reinforcement** → ch20
- **Processing fluency** → ch20
- **Progressive disclosure** → ch19
- **Recommendations (writing)** → ch06
- **Research roadmap** → ch04
- **Research project cycle (6 steps)** → ch15
- **ROI of UX (payback period)** → ch13
- **Sample size (small-N reporting)** → ch07, ch08
- **Screener design** → ch05
- **Shadows (depth)** → ch18
- **Stakeholder collaboration** → ch02, ch06
- **Study plan** → ch05
- **Team structure (embedded/consulting)** → ch02
- **T-shirt sizing** → ch14
- **Types of research (strategic/tactical)** → ch03
- **Typography** → ch18
- **UCD design principles** → ch12
- **Usability testing** → ch08
- **User flow notation** → ch16
- **User intent (start-with-intent process)** → ch19
- **UX Iceberg** → ch12
- **UX/UI/CX scope model** → ch12
- **Visual hierarchy** → ch18

## Supporting Files

- [glossary.md](glossary.md) — all key terms with definitions
- [patterns.md](patterns.md) — all techniques and frameworks with when-to-use/how/trade-offs
- [cheatsheet.md](cheatsheet.md) — quick-reference tables and decision guides

---

## Scope & Limits

This skill covers UX/UI product research and design practice: research planning, methods, sample sizes, ethics, impact tracking, stakeholder leadership, the UX/UI/CX distinction, the ROI of UX, the Double Diamond design process, user flow diagrams, visual/interaction design fundamentals, and the psychology behind engagement-driving design decisions. For statistics/quant methods beyond what's covered here (confidence intervals, significance testing) or for hands-on tool tutorials (Figma, specific design software), check related skills or ask the agent directly.
