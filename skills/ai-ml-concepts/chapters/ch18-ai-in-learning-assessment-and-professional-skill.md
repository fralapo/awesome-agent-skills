# Chapter 18: AI in Learning, Assessment and Professional Skill

## Core Idea
A model that does a task for you changes what you practise, what you can check and how skill is built over years. The mechanisms below concern people learning or working with AI assistance: deskilling, the need for prior knowledge to verify output, the role of effort in learning, and how schools, employers and hiring processes can measure competence when output is cheap. Most of the empirical evidence is early, observational or task-level, so the chapter marks what is measured and what is a reasoned position. Psychological side effects of technology use belong to `behavior-and-decision-science` (ch12); this chapter stays with learning, assessment and professional formation.

## 18.1 Delegation and deskilling
- **Thesis**: a skill that is no longer practised weakens. If a tool performs a step every time, the person may stop being able to perform it, and may not notice the loss until the tool is unavailable or wrong.
- **Mechanism**: skill is maintained by retrieval and repeated attempts. When a step is always delegated, the practice that maintains it stops. The loss is gradual, which is why it is hard to see from inside.
- **Evidence**: largely observational and early (contested in size). Some controlled studies of writing and problem-solving show reduced independent performance after heavy use; the effect size and its persistence are not settled.
- **Trade-off**: delegating routine steps frees time for harder work. The question is which steps are learning goals and which are overhead.
- **Does not hold when**: the skill is low-reuse and not part of the job or the learning goal, such as converting a file format you will never handle again.

## 18.2 To verify an answer you need prior knowledge
- **Thesis**: you can check an AI answer only in areas you already understand. Experts gain more from assistance than novices, because novices cannot tell a plausible error from a correct statement.
- **Mechanism**: a wrong answer that sounds fluent is accepted when the reader lacks the knowledge to spot it. Verification therefore depends on the reader's prior model of the domain. The same tool amplifies whatever knowledge is present.
- **Practice for learners**: build the foundations first, use the assistant to explain and to point to sources you then read yourself, and check claims against those sources. Ask for the reasoning and the assumptions, then test them.
- **Trade-off**: studying foundations first takes longer than asking for the answer.
- **Does not hold when**: verification is cheap and external. Compilers, test suites, unit conversions and running a program give a verdict that does not depend on the reader's expertise; use them.

## 18.3 Productive friction
- **Thesis**: effort is the mechanism by which a method is learned. Removing friction helps tasks that will not be reused; keeping friction helps tasks whose point is to learn.
- **Mechanism**: the struggle to find a structure, choose words or debug a fault builds the schemas that make the next task easier. Removing that struggle saves time now and may leave the next task harder.
- **Practice**: classify tasks as (a) throughput tasks, where the output is the goal, and (b) learning tasks, where the process is the goal. Automate (a) freely; protect (b) with guided effort, and where needed have an experienced teacher or reviewer judge the process.
- **Trade-off**: deliberately slow work is unpopular and can be seen as inefficiency by employers and students alike.
- **Does not hold when**: the learner already has the skill and the task is no longer a learning goal.

## 18.4 Redesign assessment; do not only ban tools
- **Thesis (position)**: when a task can be completed by a prompt, the assessment should change to measure what the prompt cannot supply, rather than relying on a ban that is hard to enforce.
- **Mechanism**: an unobserved take-home product can no longer show whether the student produced it. Assessments that remain informative include oral defence of the work, closed-book or handwritten work in a supervised setting, a critique of an AI-produced answer that the student must correct, and process evidence such as drafts, version history and notes. Oral checks scale poorly, but they are direct evidence of understanding.
- **Evidence**: practitioner judgment; the reliability of handwritten closed-book tests as a measure is generally accepted for recall and reasoning, but its validity for all skills is contested.
- **Trade-off**: oral and supervised assessments cost staff time and can disadvantage some students; process evidence can be fabricated.
- **Does not hold when**: the assessment is not meant to measure individual competence (a team project graded on its output), or the course is explicitly about working with the tool. Then assess how well the tool was used and checked.

## 18.5 Writing is thinking (position)
- **Thesis (position)**: the act of choosing words and structure clarifies what you think. A fluent rewrite by a model may read better while leaving the author less clear about the claims and less identified with the text.
- **Mechanism**: drafting forces decisions about claims, order and evidence. A model can supply fluent alternatives that the author has not chosen, so the decisions are made elsewhere.
- **Practice**: use the model to critique, question or find weak points in a draft you wrote; rewrite the final version yourself where ownership matters.
- **Trade-off**: writing alone takes longer and can be slower than the quality gained justifies for routine messages.
- **Does not hold when**: the text is a standard form or a message where the content is fixed and the author's voice is not important.

## 18.6 Task exposure is not job loss
- **Thesis**: studies that measure how much of a job's tasks a model could perform describe exposure, not automation; occupations are bundles of tasks, and exposure can change work without removing the job.
- **Mechanism**: task-level exposure is measured by matching task descriptions to what models do. Whether the exposure becomes replacement depends on cost, regulation, quality requirements, accountability and how the work is reorganised. Evidence about entry-level work is recent, mixed and sensitive to the sample.
- **The entry-level question (open)**: if junior tasks are the ones most automated, how do people learn the judgement that senior roles require? Possible answers include structured apprenticeships, review assignments, deliberate practice on real problems and deliberate hiring of people for their learning potential. None is established.
- **Trade-off**: the statistics show what could happen; the decision is still made by organisations and individuals.
- **Does not hold when**: the job is defined by a physical or legal requirement that a model cannot meet.

## 18.7 When output is cheap, judgement is the bottleneck
- **Thesis**: producing code, text or designs is becoming cheap; deciding whether they are right, safe and worth keeping is not. Specification, modelling and verification gain weight.
- **Mechanism**: reviewing requires knowing what good looks like, which comes from having produced and debugged similar work. A reviewer who has never written the kind of code under review may approve errors they cannot recognise. Reputation attaches to what a person signs, so authorship and responsibility remain human.
- **Practice**: keep some work hands-on at the level you review; state the acceptance criteria before generating; treat generated output as a draft that a named person must own. Software-specific gates for generated code are in `software-engineering-practice` ch09.
- **Trade-off**: hands-on time competes with delivery; judgement is hard to measure in short cycles.
- **Does not hold when**: the output is mechanically checkable end to end, such as a conversion with a full test suite; then the verdict comes from the checker.

## 18.8 Evaluating people when the evaluator is a model
- **Thesis (position)**: a model should not replace the reading of a person's work when a judgement about that person is at stake.
- **Mechanism**: AI-assisted applications and AI-assisted screening both raise the volume of candidates, which pushes screening toward cheap signals. When candidates use models to pass the screen and employers use models to filter, the process measures who uses tools well at the screen rather than the skill the job needs. Closed-book tests measure recall under time pressure, which is one component of skill. Asking a model to grade work it has not properly read produces a verdict with no accountable reader.
- **Practice**: use work samples that the candidate or student performs live or explains afterwards; read the work yourself; use models to organise notes or to draft questions, not to decide.
- **Trade-off**: work samples and live explanations cost time per candidate; at high volume, a short structured task is the practical compromise.
- **Does not hold when**: the evaluation is a first, explicitly low-stakes filter with a clear appeal route; then say so and do not treat its output as a final judgement.

## 18.9 Creative work: the sparring partner (contested)
- **Thesis**: generative models can recombine existing material quickly, which makes them useful for generating options. Whether they produce genuinely new directions is contested.
- **Mechanism**: a model trained on common material tends to return common combinations. Generating many options and selecting the best is a useful method for people too, and the model can speed the first stage. The worry worth taking seriously is that creative output may look easy to reproduce, which is a question about the value of taste and selection, not only about the tool.
- **Practice**: ask for many options; reject the first obvious ones; use the model for critique and counter-arguments; keep the choice of what to pursue with the person.
- **Trade-off**: volume is cheap; selection is the scarce act and needs criteria stated beforehand.
- **Does not hold when**: the goal is to reproduce a known style or format; then recombination is the task.

## Stay in lane
This chapter gives mechanisms and assessment design. It does not replace professional advice on education policy, employment law or the rules for a particular examination body. Measured effects are early and depend on the population studied; the chapter labels them as such.

## Cross-references
- ch10 for failure modes of models (hallucination, sycophancy, detector weakness) that make verification necessary.
- ch15 (15.20) for reliability compounding over long agent runs.
- `software-engineering-practice` ch09 for generated code, gates and review debt.
- `behavior-and-decision-science` ch12 for attention, effort and reliance from the individual side.
- `coding-with-agents` for working practice with coding agents.
