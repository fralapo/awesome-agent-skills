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

## Human-Centred AI: Control, Oversight and Fairness
The first two points are design and governance positions argued by analogy with other safety-critical fields, not empirical findings; the learning and distribution points rest on reported studies and are marked as such.
- **Control and automation are not a trade-off on one slider.** The stance: raise automation while keeping the human in control, so the person initiates and understands what happens. Systems with serious failure consequences should be comprehensible, predictable and controllable, as a lift is: you press a floor and you know what will happen. Good engineering often removes the need to call something 'AI' at all, because a cleaned-up system becomes plain and dependable.
- **Independent oversight at three moments.** (1) Planning review before launching something consequential at scale, like a building permit scaled to the stakes (basic research should not be gated). (2) Continuous monitoring: costly, but evidence from other regulated fields says it works. (3) Retrospective investigation after a failure by someone independent who can see the data. This needs **logging designed in** (a flight-recorder idea) and a tiering by consequence: discretionary (recommenders), consequential (credit, hiring, parole) and life-critical. Its advocates add that software decisions are more inspectable than unrecorded human discretion, and that companies often want clear rules and may find insurers pushing the same way. A critique of the principles lists (awareness, redress, accountability, explanation, data provenance, auditability, testing) is that 'should' is untestable until someone says who, how and when. Design consequence: build explanation, an appeal route, an audit trail and test cases into the product before launch.
- **Test across user groups and treat a gap as a defect.** Measure accuracy and task success per group, not only on average. Reports of recognition systems failing on some faces illustrate the risk, but the evidence behind that example is not covered here; ch23 holds the evidence on adaptive interfaces. Keep the ethical question upstream too: start from the kind of society and user outcome you want, not from what the technology can do.
- **Do not do the user's thinking where thinking is the goal (reported survey and experiments).** In a large survey of secondary-school students (self-report), about half said they relied on AI too much and over 40% had tried to limit use and failed; motivation to study some subjects fell. Designs that hold up: the learner plans and does the thinking while AI scaffolds or quizzes; tasks are rebuilt so a chatbot cannot simply answer (students invent problems the tools cannot solve and then defend them aloud); metacognition is taught (what a human mind does better than the tool). Human presence still matters: identical written feedback was rated more useful when believed to come from the teacher, because it signals care; in one comparison an AI tutor and a human tutor produced similar retention, but learners enjoyed and engaged more with the human; good tutors manage motivation and withdraw support step by step. Measure learning, not completion.
- **Distribution and data.** One reported study found less experienced workers gained more from a text assistant than experts (a flattening effect), but it is unreplicated and the long-run effect on inequality is open. Ask who designed it, who owns it, what happens to the data, who benefits and who loses.

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
