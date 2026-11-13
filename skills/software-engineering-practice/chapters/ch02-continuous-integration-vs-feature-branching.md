# Chapter 02: Continuous Integration vs Feature Branching

## Core Idea
Continuous integration (CI) is about **integrating changes with everybody else's, at least once per day**. It is not a server product. In this model, long-lived branches delay the moment you learn whether changes work together, and the cost of that delay grows with the size of the divergence. The material presents this as a reasoned position backed by survey data, and also as an emotionally contentious one.

## 2.1 What integration means
- **Thesis**: integration is a technical activity that precedes delivery; delivery has business meaning, integration is its prerequisite.
- **Mechanism**: integrating means bringing different copies of the code together so the combined result can be evaluated. Running a CI server on a feature branch is not CI; neither is pulling trunk into your branch while nobody else is merging. The definition used: if you are not merging your work with the shared line at least daily, you are not practising continuous integration.
- **Trade-off**: "continuous" is discrete in practice (committed at moments of readiness); the aim is to keep the gap between moments small.
- **Does not hold when**: people use the word loosely; agree on the definition before arguing.

## 2.2 CI and CD are one practice, not two
- **Thesis (position)**: you cannot do continuous delivery without continuous integration; "CI/CD" names one idea twice.
- **Mechanism**: CI is the technical prerequisite, outward-facing delivery is the business language. A single shared view of the code ("only one interesting version of the software, the current one") underlies both.
- **Trade-off**: the distinction still matters for communication with non-technical people.
- **Does not hold when**: a team defers integration to run time and accepts the risk.

## 2.3 The cone of change
- **Thesis**: any two developers working on shared code diverge over time; the cone of possible clashes widens with the time between merges.
- **Mechanism**: if anything is shared, the two are coupled to some degree, and you can only learn whether my change affects yours when both are together. CI limits the time horizon and so limits the fan-out. The worst case of a short horizon is losing minutes or at most a day of work; the worst case of a long one is losing everything. Reported cases: a team that could not compile the whole system for 18 months after splitting into repository copies (about 250 people's work lost); a printer-firmware team that spent roughly five times as much effort managing branches as writing new code before it adopted continuous delivery; a company with monthly integration days that took days.
- **Trade-off**: you must adapt how you work (small steps, dark launching, branch by abstraction, feature toggles).
- **Does not hold when**: nothing is shared between workers (no integration needed).

## 2.4 "I pull from trunk into my branch"
- **Thesis**: pulling trunk into a feature branch is useful but is not integration.
- **Mechanism**: as long as nobody commits, nobody sees anyone else's changes; once someone commits, the visibility starts. Each developer then sees a different reality (A sees C's changes but not B's, and so on). Until your own changes meet the others' you cannot know they work. In a team where everybody uses feature branches, everyone works "in the dark" until the first finished feature is committed. The recommended plan is to minimise the dark period.
- **Trade-off**: pulling still beats not pulling.
- **Does not hold when**: you are the only committer.

## 2.5 Predicting conflicts instead of integrating
- **Thesis**: planning work so branches do not clash is guesswork about the future.
- **Mechanism**: it requires knowing what everyone else will do, scales only to small code bases and is wrong sometimes. The alternative that deals in facts is to integrate more often in smaller steps.
- **Trade-off**: you lose some autonomy; you gain evidence.
- **Does not hold when**: the design cleanly separates the work (low coupling), which reduces but never removes the need.

## 2.6 Information-divergence argument
- **Thesis**: copies of information modified independently diverge; reconciliation effort grows with divergence.
- **Mechanism**: until copies are brought together the "truth" of the combined state is unknown; integration establishes one snapshot. This is independent of tools and applies to code, configuration and documents.
- **Trade-off**: none for the argument itself; its practical force depends on how much is shared.

## 2.7 Why it is contentious (positions)
- It challenges the self-image of the lone developer working uninterrupted; version control is a communication tool and CI means communicating more.
- A reported pattern in talks: roughly half the audience thinks daily trunk integration is impossible, the other half thinks it is obvious.
- Survey data cited in the material says CI correlates with better outcomes than feature branching; the correlation is not a controlled experiment. Feature branching can work and "even do a good job"; the claim is it is not the best job and its failure mode is severe.

## 2.8 Making CI work
Small steps; keep trunk always releasable; feature toggles and branch by abstraction for unfinished work; fast reliable commit-stage tests (ch01, ch04); revert or fix immediately when the build breaks. For tightly coupled code CI is the defensive tool (ch05).

## Cross-references
`software-architecture` for module boundaries and deployment independence; chapter 05 for coupling as the reason integration matters.
