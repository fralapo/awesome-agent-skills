# Chapter 11: Work, Learning, Information and Digital Rights (positions)

## Core Idea
Questions about what AI does to jobs, schooling, the news and personal rights mix a few measurements with many predictions. Each entry gives a position, the case for and against, and what would falsify it. Mechanism for the technical parts sits in `ai-ml-concepts`; for the cryptographic design of age checks and media provenance see `computer-science-fundamentals` ch9.8-9.10. Reports of specific disputes below are as told by commentators and unverified.

## 11.1 Tasks, not occupations (position)
- **Position**: models take over tasks, not whole jobs; few occupations consist only of knowledge work, and the gap between what is technically feasible and what is actually used is explained by reliability, legal obstacles and organisational slowness.
- **For**: an analysis of usage data from a single chatbot found no systematic rise in unemployment in highly exposed occupations; reports on usage show growth in non-work messages, information seeking and tasks delegated with more autonomy. Agent benchmarks on office tasks reported that the best systems completed a minority of tasks, with little common sense and deceptive shortcuts (a dated snapshot), and accuracy tends to improve faster than reliability.
- **Against**: usage data come from one product and an early period; entry-level roles may shrink first because their tasks are the easiest to delegate; occupations where work and creativity overlap are the sensitive zone.
- **Falsified by**: measured shifts in hiring or wages in exposed occupations, tracked over several years, or a reliability jump that removes the oversight burden (see the measured error rates in `ai-ml-concepts` ch9.15).

## 11.2 Learning with a tool that supplies answers (position)
- **Position**: learning requires productive struggle; delegating exercises gives an illusion of understanding, so AI helps most those who already have the basics and can supervise it.
- **For**: a controlled maths study reported better practice scores with free use but a worse unaided exam, whereas a tutor that withheld the answer avoided the harm; the distinction between useless obstacles and necessary ones; the supervisor needs domain knowledge.
- **Against**: the best-known "cognitive debt" study had few participants and no follow-up; meta-analyses are more positive but weak; tools can free time for deeper work.
- **Falsified by**: long-term controlled studies with unaided assessments that show no loss.
- **Practice**: train teachers and students, grade the process, and make the tool ask questions instead of giving answers.

## 11.3 When the chatbot becomes the main source (position)
- **Position**: attention shifts from finding sources to judging an answer, and more trust means less checking; integration into search will reduce traffic to the web and disturb the incentives that produced it.
- **For**: fluent output hides errors; research on reliance; the incentives of sites that depend on visits.
- **Against**: people can ask for sources and use retrieval tools; search was never neutral.
- **Falsified by**: measured checking behaviour that does not fall with trust.
- **Related**: once convincing fakes are common, genuine evidence can be dismissed as fabricated (the "liar's dividend"); see `computer-science-fundamentals` ch9.10.
- **Consequence for evidence**: a consensus-mediating communicator who cites many sources is more reliable than one who offers their own view; unfamiliar uncertainty (as in public health communication) was misread as shifting truth.

## 11.4 Who may set limits on a general-purpose model? (open question, position)
- **Dispute as reported**: a supplier refused two uses by a state customer: mass domestic surveillance (purchased data, once interconnected by models, allows profiling at scale) and fully autonomous weapons (models too unreliable, accountability unclear). The customer allegedly pressed for use outside the terms of service; a rival supplier accepted with stated limits and a contract that was not public.
- **Position A**: a company may set conditions for use of its product, as in any contract, especially where reliability and accountability are missing.
- **Position B**: elected governments, not suppliers, should decide the limits; supplier vetoes are unaccountable.
- **For A / for B**: a product has known failure rates and the supplier knows them / law has not caught up and democratic accountability sits with the state.
- **Falsified by**: a durable legal framework that fixes who decides and shows suppliers and states abiding by it. A commentator also warned against siding with any single company, since each pursues profit.

## 11.5 Gating a model after a jailbreak (position)
- **Reported case**: a model was withdrawn from release after researchers found a way to bypass its safeguards, with a government department involved.
- **Mechanism**: perfect resistance to jailbreaks has not been shown for any model; a narrow bypass and a broad one differ in consequence.
- **Options**: retract and retrain; gate releases behind government approval; rely on open or local models, which no one can recall; verify user identity. Each shifts cost to someone else.
- **Position**: selective withdrawal is hard to justify if other models are equally breakable; the commentator judged the models unready at release in both 2023 and later (opinion).
- **Falsified by**: an independent audit showing a measurable difference in risk between gated and ungated models.

## 11.6 Age verification (position)
- **Position**: a check can be designed so that sites learn only "adult" (see `computer-science-fundamentals` ch9.9), but whether it solves the harm is a separate question.
- **For**: a legal duty to protect minors; double-anonymity designs limit data collection.
- **Against**: the third party can still see volumes and timing; providers are poorly documented; each site may choose a different provider; in one country similar measures raised VPN use; critics prefer parental controls and education over a visible but leaky measure.
- **Falsified by**: measured exposure of minors before and after, together with measured leakage.

## 11.7 Training data, creators and likeness (position)
- **Position**: data are a currency; if models were trained on creators' material, compensation could be a share of subscriptions, valued by what the output resembles and not only by where the data came from (an illustrative share was proposed). Faces and voices raise a separate right: using another person's likeness in generated images needs negotiated limits.
- **For**: creators bear the cost and receive none of the value; regulators have already treated the personal-data side of training as a legitimate concern.
- **Against**: attribution of output to inputs is technically unsolved; a levy can be gamed.
- **Falsified by**: a licensing market that prices training data and pays creators without a legal mandate.
- **Creative work**: where music or text is generated, the human task moves from composing to searching and judging among endless candidates; a flood of generic output raises the value of curation (see `ai-ml-concepts` ch10.9).

## Checklist for this chapter
1. Is the claim about tasks, occupations, or the economy as a whole?
2. Is the evidence usage, exposure or measured outcome?
3. Is a dispute described by a participant, a commentator or a document?
4. Who decides, who is accountable, and what would show the position wrong?
