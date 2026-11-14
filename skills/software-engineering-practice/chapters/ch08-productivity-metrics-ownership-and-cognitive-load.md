# Chapter 08: Productivity Metrics, Ownership and Cognitive Load

## Core Idea
In this model developer productivity is not a single number: it is a set of **balanced indicators that inform the team's own experiments**, plus organisational choices (who runs the software, how much a team must hold in its head) that decide whether the indicators can improve. Metrics that escape to management as targets get abused.

## 8.1 DORA: the four delivery metrics
- **Thesis**: four metrics (deployment frequency, lead time for changes, change failure rate, time to restore service) give a generic, technology-independent signal of delivery performance; speed and stability move together.
- **Mechanism**: they come from survey-based research, and cluster analysis found speed and stability metrics bucket together reliably year after year (the former low / medium / high / elite bands). The research program is wider than the four: it identifies technical practices (CI, version control, test automation, architecture), cultural practices and management practices that explain how to improve them. The four metrics give **signal**, the rest of the research gives **action**. They suggest there is no trade-off between speed and quality.
- **Trade-off / critique (position)**: all four are indirect indicators; they do not tell what to fix (low deployment frequency could mean big stories, too much work in progress or a dependency). They contain no measure of value, of whether you build the right thing, or of how pleasant the place is to work.
- **Does not hold when**: used as targets. A low deployment frequency reported upward invites "work harder", overtime and output pushed out faster regardless of quality.

## 8.2 Metrics escape to management
- **Thesis (position)**: team-level use of delivery metrics is healthy; once they leave the team without an enlightened audience, they introduce dysfunction.
- **Mechanism**: almost all hard metrics measure output (throughput, deployment frequency), not outcome. Lean metrics in particular come from factory thinking: concepts such as a linear board with no going backwards, or rework as waste, do not fit agile development in which loops inside loops are normal. A short recovery time may be a sign of healthy experimentation rather than failure.
- **Counter-position**: the four are a set, balancing throughput against stability, and they are a useful picture precisely because they are indirect; value measures must be defined contextually per experiment.
- **Does not hold when**: the audience understands lean and agile; rare.

## 8.3 SPACE: a framework for choosing your own metrics
- **Thesis**: SPACE is a meta-framework of five dimensions to help you pick metrics; it does not supply the metrics.
- **Mechanism**:
  - **S**atisfaction and well-being (e.g. satisfaction with tools; surveyed, maybe quarterly).
  - **P**erformance (outcomes, quality, reliability).
  - **A**ctivity (counts: pull requests, commits, test runs; never lines of code).
  - **C**ommunication and collaboration (code-base searchability, coordination costs, pings to find who can help).
  - **E**fficiency and flow (time through the system, hand-offs, flow state, delays).
  Rules of thumb: there is no single metric that matters (anyone claiming otherwise is wrong); choose at least two to three metrics in **tension** with each other so they balance; take them from **different dimensions** (three counts of the same thing is not a framework); you need not cover all five.
- **Worked example (automated testing)**: satisfaction (are people content with the tooling, asked occasionally), performance (reliability, flaky tests, escaped defects), activity (tests run, reruns), collaboration (are suites maintained, do people ping each other), efficiency (run time, delays, whether tests are in the flow). Time-box to an hour or two: what data exists, are at least a few dimensions covered. Rotate metrics out as data improves.
- **Trade-off**: availability bias (measuring what you already have). Surveys cannot be frequent.
- **Does not hold when**: no one is willing to treat measures as experiments with a hypothesis.

## 8.4 Practical stance on measurement
Treat improvements as experiments: state a hypothesis (investing in automated tests improves lead time), choose measures, control variables, run, try to poke holes. Developer productivity in the useful sense is the individual and team experience of friction (three-hour release cycles, tools in the way, unreliable tests, waiting overnight for feedback) rather than output per person; put effort where the biggest delay is, as in performance tuning (measure, do not guess). Set a bold but concrete question ("why can't I release today's change today?") instead of a distant stretch target (position). Shortening feedback loops has revenue and quality benefits as well as developer morale; flaky tests and slow builds are productivity problems. Beware of treating the output of coding as the job (the job is understanding and deciding).

## 8.5 You build it, you run it
- **Thesis**: the product team builds, tests, deploys, operates and supports its own service, including first-line on-call.
- **Mechanism**: zero hand-offs, low knowledge-sync cost, no scheduling conflicts; change management is informed after deployment from an automated audit trail. Alerts go to the on-call engineer of the owning team first (not a separate operations team). They have the incentive, skill, time and permissions to fix the niggles that become latent faults and then major incidents. Reported example: 44 services owned by 29 teams, average time to acknowledge about 2 minutes and time to restore about 27 minutes, roughly twice as good as the earlier central operations team (single organisation). A cited survey: 59% of engineers on call, with strong correlation between job satisfaction and this model (survey, correlation).
- **Trade-off**: personal-life disruption is the top concern; it must be compensated (position: a flat on-call rate plus a flat call-out rate, paid for availability and not only for responding). Needs a "why" explained to engineers, and listening to concerns.
- **Does not hold when**: you cannot get it right at the start; you need not apply it everywhere. Legacy services may stay with operations and application support.

## 8.6 Accountability under you build it, you run it
- **Thesis**: accountability becomes clearer, not weaker, when product teams own it.
- **Mechanism**: product managers map operational requirements to customer outcomes, plan observability and availability targets; engineers help balance risk tolerance with effort (no one picks very high availability arbitrarily if they must do the work). Teams prioritise failure design alongside features, using circuit breakers and bulkheads against brittle dependencies. A RACI table helps: for legacy services operations stays accountable; for modern services operations is consulted, support informed, and the person funding the team (product head or IT head) is accountable, while the team is responsible for reliability. Operating cost moves from one line to many budgets, which is hard.
- **Does not hold when**: leadership will not shift budgets and accountabilities.

## 8.7 Cognitive load
- **Thesis**: team cognitive load is a cost with several drivers; the aim is to **manage** it, not minimise it to zero.
- **Mechanism**: research reported four clusters (about 25 drivers): team composition (skills, size, role clarity, working together), complexity of the work and clarity of goals and success measures, the environment (tools, workflow integration, physical noise), and dependencies/organisation (approvals, other teams). Some load is intrinsic to the problem; much is avoidable (managing dependencies on five teams, approvals from three people). Cost: symptoms show up as slower delivery, more incidents and lower DORA bands, burnout risk, lower motivation. Reorganisations and responsibility changes raise load; learning a new skill (including AI) temporarily raises it and can be a justified investment.
- **Organisation response**: split by value stream into small teams, abstract and decouple between them (information and coupling problem, ch05), offer platforms and "golden paths" whose purpose is to reduce the load of product teams, and reserve interaction modes with other teams that change over time. Trust between platform and product teams matters as much as tooling.
- **Trade-off**: some load is productive (hard problems motivate).
- **Does not hold when**: the diagnosis is only ever a black-box "too much load"; look for specific drivers.

## 8.8 AI and load
AI tools can raise load: another toolset, context switching, new pipelines, fatigue, feeling devalued, and individuals working alone with their own assistant. Gains are real but not a magic multiplier; coordinate the workflow and clarify what humans do.

## Cross-references
Chapter 01 and chapter 02 for the practices the metrics reflect; chapter 05 for coupling between teams; `software-architecture` for reliability and observability design.
Chapter 14 for the individual side of load: motivation, burnout causes and sustainable effort.
