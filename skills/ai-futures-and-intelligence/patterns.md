# Patterns

Recurring situation -> move. Each entry: When / Move / Cost / Not when. Chapter in brackets.

## 1. A claim says a model is "intelligent" or "generalises"
**When**: a headline or paper uses the word without a definition.
**Move**: ask which definition (adaptation to novelty, specialised, task skill); ask how much was pre-loaded; run variants and extrapolation tests. [ch01, ch02, ch10]
**Cost**: slower verdict; may need your own tests.
**Not when**: the user only needs the task done.

## 2. A high exam or benchmark score is offered as proof
**When**: "it passes the bar / olympiad".
**Move**: ask whether the test can be passed by preparation; look for contamination and templated variants; separate memory-heavy from novelty-heavy tasks. [ch01, ch10]
**Cost**: needs access to test design.
**Not when**: the exam is the job.

## 3. "It reasons" because the steps look plausible
**When**: chain-of-thought text accompanies an answer.
**Move**: check for a verifier; test with altered steps and larger problems; separate fluency from soundness. [ch02]
**Cost**: building a checker.
**Not when**: a cheap verifier already exists (code with tests).

## 4. "Statistics cannot do X"
**When**: a sweeping limit claim.
**Move**: classify X as derived, learned or searched; look for a hybrid or verifier solving it; state the falsifier. [ch03]
**Cost**: requires specifying X precisely.
**Not when**: X is a pure recall task.

## 5. A hybrid or symbolic proposal
**When**: "add knowledge graphs / symbols / a planner".
**Move**: specify the interface: who writes, updates and checks the symbols; compare with a verifier-in-the-loop design. [ch03]
**Cost**: engineering and maintenance.
**Not when**: errors are tolerable and scale solves it cheaply.

## 6. "Does it understand?" stalemate
**When**: the debate loops on the word.
**Move**: split functional from experiential; state which reply to the Chinese room applies; propose an observable difference. [ch04]
**Cost**: some philosophical overhead.
**Not when**: only task performance matters.

## 7. "AI is creative / not creative"
**When**: outputs look novel.
**Move**: ask about stepping-stone archives, notion of interestingness, representation inside, human selector's contribution. [ch05]
**Cost**: inspecting internals or process.
**Not when**: the user wants variations, not discoveries.

## 8. A compute or hardware claim with no date
**When**: "the limit is X".
**Move**: date it; name the lead time; ask which constraint binds in the horizon; convert to gigawatts, chips and dollars. [ch06]
**Cost**: arithmetic and sourcing.
**Not when**: only a conceptual argument is needed.

## 9. Serving-cost or speed claims
**When**: "this model is cheap or slow because ...".
**Move**: apply the compute-time vs memory-time model; ask about batching, context length, active vs total parameters. [ch07]
**Cost**: needs hardware numbers.
**Not when**: the bottleneck is network or scheduling.

## 10. "AI will take the jobs / the share of the economy"
**When**: macro forecasts.
**Move**: separate size from share; list complements; ask the required reliability; look for aggregate forecasts and missing data. [ch06]
**Cost**: data gaps.
**Not when**: the claim is about one task, not the economy.

## 11. A timeline or intelligence-explosion claim
**When**: "AGI by year Z".
**Move**: name the assumed bottleneck, the missing capability, the analogy; list near-term observations that would change the number; mark as a dated position. [ch07, ch08]
**Cost**: refusing a single number.
**Not when**: the user only wants a range for planning, which can be labelled as a position.

## 12. A historical analogy is used as proof
**When**: "like the printing press / a weapon program / a plague".
**Move**: list required relations, where AI reverses them, what observation would break the analogy; use several that disagree. [ch09]
**Cost**: more cases to study.
**Not when**: the analogy is an illustration, not an argument.

## 13. Two sources disagree
**When**: conflicting numbers or theses.
**Move**: report the range; find the premise on which they differ (definition, measurement, bottleneck, horizon); do not average. [ch10]
**Cost**: longer answer.
**Not when**: both reports restate one claim.
