# Chapter 31: Anticipatory Design and Automation

## Core Idea
Anticipate needs by offering information and choices, not by silently deciding for the user. Anticipatory design predicts and offers; automated design acts on the user's behalf. Full automation causes deskilling, failure risks, lost innovation and lost fulfilment. This complements ch20 (choice overload) and ch19 (progressive disclosure).

## Three Cautions
1. **Accuracy**: what happens when the prediction or automation fails, and can the user correct course?
2. **Innovation**: where do people check in and give feedback? Full automation removes the people who would find improvements.
3. **Human experience**: flow and fulfilment often come from effort. Pilots hand-fly only a few minutes per flight and deskilling has contributed to accidents (reported, single source).

## Principles
1. **Do not invade**: suggest better options; decide for the user only when the decision is simple and the context well understood.
2. **Never remove full control**: make actions reversible; offer a kill switch ("never do this for me again").
3. **Be transparent**: say when a decision was made on the user's behalf; let users pause, change or reverse it.
4. **Curate with context**: use history and plans to filter options, not just rank long lists; more human, less algorithmic; quality over quantity.
5. **Build trust before reaching into personal data** (calendar, money, mail): say why each data request is made and show how it is used in the next step.
Rule: decide case by case whether the system acts or asks. Mark high-stakes decisions ask-first. Test by segment: some users welcome predictions and some hate them, so offer a hide or turn-off option.

## Procedure
1. List the decisions in the flow; for each, ask: made out of necessity or novelty?
2. Allocate functions deliberately between system and person (human-factors technique). Automate the tedious parts; keep the meaningful ones.
3. Answer the question directly where the user asks it (for example a voter-registration module at the top of search results).
4. Reduce choice to fight decision fatigue, without hiding the way back.
5. Define failure behaviour: how the user takes over.
6. Validate before building; if research says no, ship a small MVP.

## Related Restraint
Do not hyper-personalise every visitor until it feels intrusive; prioritise clarity and fast task completion for the majority. Small human imperfections and inconsistency are acceptable if they do not block tasks. One figure for daily decision counts is widely cited but unsourced; do not rely on it.

## Emerging Positions on Human-Centred AI
Drawn from talks summarised in short descriptions only; treat as positions, not frameworks.
- **Comprehensible, predictable, controllable**: one design position for systems that can fail with serious consequences. Pair it with independent oversight at three moments: planning, continuous monitoring, and retrospective analysis after failures. Clarifying who is responsible for a failure is argued to improve design thinking.
- **Test across user groups**: AI systems have been shown to fail or mischaracterise some faces, notably dark-skinned ones. Include varied users in testing and treat an accuracy gap between groups as a defect, not an edge case.
- **Do not do the user's thinking where thinking is the goal**: in learning products, concern is that generative tools may do the thinking for the user. Prefer designs that enhance learning over designs that replace it.

## Mistakes
- Silently booking or adding items from incomplete data; calendar entries appearing with no explanation.
- Recommendation modules users read as sales pitches.
- Automating everything because it is possible; solving a problem no one has.

## Checklist
- [ ] Each automated action is visible, reversible and explained.
- [ ] A permanent opt-out exists.
- [ ] High-stakes decisions ask first.
- [ ] Data requests carry a reason and a visible payoff.
- [ ] Failure path lets the user take over.

## Connects To
ch19, ch20, ch09 (ethics), ch18 (feedback).
