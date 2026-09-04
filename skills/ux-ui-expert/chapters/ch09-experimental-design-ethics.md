# Chapter 9: Experimental Design and Research Ethics

## Core Idea
Choosing between between-subjects and within-subjects design is a tradeoff between sample size and order effects, solvable with counterbalancing — but no methodological rigor matters if the research violates basic ethical principles, which the field's own history (the Stanford Prison Experiment, the Milgram obedience study) shows can go catastrophically wrong.

## Frameworks Introduced
- **Between-Subjects vs. Within-Subjects Design**: Between-subjects (independent groups) — each participant sees only ONE condition/prototype. Pros: no order/fatigue effects, shorter sessions, simpler setup. Cons: needs a larger sample for statistical power, more exposure to individual differences (mitigate via random assignment). Within-subjects (repeated measures) — each participant sees ALL conditions. Pros: smaller sample needed, reduces individual-difference noise, yields direct comparison data. Cons: order effects (fatigue, practice/learning bias) — mitigate via counterbalancing.
  - When to use: within-subjects when you need comparison data and can control order effects; between-subjects when sessions must stay short or conditions can't be meaningfully compared side-by-side.
- **Counterbalancing / Pseudorandomization**: systematically varying the order conditions are shown to cancel out order effects. For n designs, compute n-factorial (n!) to find the total possible orderings (2 designs → 2 orders; 3 designs → 6 orders; 4 designs → 24 orders), then randomly assign participants to those orderings (e.g., a spreadsheet `=RANDBETWEEN(1, n!)` formula). Avoid the **Latin Square design** as a shortcut — it still embeds systematic order bias (A always precedes B, B always precedes C).
  - When to use: any within-subjects study with 2+ conditions; practically, cap prototypes at 3 to keep the combinatorics manageable.
- **The Belmont Report's Five Principles**: (1) Respect for Persons — protect autonomy, ensure informed consent, debrief if deception was used; (2) Beneficence — do no harm, maximize benefit, minimize risk; (3) Justice — fair, non-exploitative distribution of research costs/benefits; (4) Fidelity and Responsibility — establish trust, take responsibility for repercussions; (5) Integrity — honesty and accuracy in all research activities, never fabricate data to look good.
  - When to use: as a checklist before fielding any study, especially with vulnerable or high-stakes participant groups.

## Key Concepts
- **Order effects**: bias introduced by the sequence conditions are shown in (fatigue, practice/learning effects).
- **Institutional Review Board (IRB)**: academic/biomedical body that vets research ethics — most UX researchers work without one, which raises the stakes of self-policing ethics.
- **Belmont Report (1974)**: created in response to the Tuskegee syphilis experiment; foundational ethics document behind modern research-conduct standards (later folded into the APA's ethical code).

## Mental Models
- Analogy for between-subjects: two people separated by a river, never interacting — each experiences only their own condition. Within-subjects: one person with "powers within" — they experience everything.
- Neither design is "better" — always frame the choice as a pros/cons tradeoff tied to your specific goals (comparison data vs. shorter sessions vs. sample size constraints).

## Anti-patterns
- **Using a Latin Square and assuming it's unbiased**: it removes randomness but not the underlying systematic order pattern — true counterbalancing/pseudorandom assignment is needed instead.
- **Skipping informed consent or debriefing "because it's just UX research"**: the Stanford Prison Experiment and Milgram studies show how quickly researcher authority can override participant welfare — non-academic research is not exempt from ethical obligation.
- **Fabricating or cherry-picking data to look good** (Integrity violation): a documented failure mode where someone quietly skews results to look good — it ultimately harms the users the data is supposed to represent.

## Key Takeaways
1. Choose between-subjects for simplicity/shorter sessions, within-subjects for comparison data and smaller samples — mitigate each design's main con (individual differences vs. order effects) with random assignment or counterbalancing respectively.
2. Compute n! to know how many orderings exist, then randomly assign — avoid the Latin Square's hidden systematic bias.
3. Apply the Belmont Report's five principles (Respect for Persons, Beneficence, Justice, Fidelity/Responsibility, Integrity) to every study, even without a formal IRB.
4. Treat ethics as core curriculum, not an afterthought — the field's own history shows the cost of skipping it.

## Connects To
- **Ch8**: usability tests comparing multiple prototypes are exactly where this between/within-subjects choice comes up.
- **Ch10**: baseline/benchmark studies (next chapter) rely on consistent, ethical, well-controlled methodology to be trustworthy over time.
