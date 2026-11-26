# Chapter 7: Evaluating and Comparing Tools and Models Without Hype

## Core Idea
Tool and model rankings change faster than any training plan. The durable skill is not knowing today's best model but running a **fair, cheap comparison on your own tasks** and keeping the freedom to switch. Treat public benchmarks, launch videos and personal rankings as hypotheses.

## 7.1 Same prompt, several models, your task
- **Principle**: Give the identical task and context to each candidate, then judge the output against criteria written beforehand.
- **How it works / sequence**: Choose 5-10 real tasks (a proposal, a spreadsheet analysis, a landing page, a workflow definition, a research question). Write the pass criteria. Run each candidate once or more, record time, cost, number of corrections needed and the result. Blind the judge to the model name where possible, and add a second judge from outside the team.
- **Evidence**: Practitioner.
- **Trade-off**: A handful of tasks is anecdote; repeat and report spread. Aesthetic judgements are subjective; separate them from correctness.
- **Does not hold when**: Candidates differ in access (region, plan), so the comparison is not available to your users anyway.

## 7.2 Benchmarks
- **Position**: Public benchmark scores are weak predictors of fit for a specific job and are sometimes gamed or measured under conditions you will not have. Use them to shortlist, not to decide.
- Look for: the task type, whether tools were allowed, the number of runs, and whether the figure is from the vendor.

## 7.3 Pick a model per task
- **Principle**: Match power, output type and price to the task. Many routine tasks are served by a mid-range model; harder reasoning or large code changes may justify a stronger one; cheaper open-weight models can be good enough for bulk work at a fraction of the price.
- **Moves**: Keep a short table: task class, chosen model, why, cost per completed task, review date. Let a strong model plan and a cheaper model execute where that holds up in your tests (see `coding-with-agents` ch06 and ch09).
- **Evidence**: Practitioner; shares of tasks suited to each tier are claims to re-measure.
- **Trade-off**: More models, more upkeep.

## 7.4 Cost per completed task
- Compare total cost to finish the task including retries and reviewing, not price per token. A cheaper model that needs more corrections or runs longer may cost more.
- Slower is not free: elapsed time is part of cost.

## 7.5 Lock-in and portability
- Keep prompts, skills, data and context in files you own. Prefer interfaces that several vendors support. A managed retrieval service is convenient but may hide chunking, ranking and thresholds you cannot tune, and keep documents on the vendor's servers.
- **Evidence**: Practitioner.
- **Trade-off**: Portability has an adapter cost.

## 7.6 "Free" and availability
- Free tiers are paid for with data or with limits that change. Features may not exist in your region or plan. Check both before building on a demo.

## 7.7 Prototype or production?
- Visual app builders, chat-based generators and agent builders are often excellent for prototypes and weak for production: limited triggers, single-vendor models, thin integration and little control over security or backends. **Decision rule**: use them to learn and demonstrate; move to code or a workflow engine with tests when users, money or sensitive data are involved.

## 7.8 Agentic browsers and assistants
- Evaluate on a fixed list of web tasks with success, speed and number of interventions. Set a rule to stop before personal data or payment steps. A single failed test is not a verdict.

## 7.9 Reading the hype
- Questions that cut through: What exactly was tested? By whom? On how many runs? What was the baseline? What does the author sell? When was it measured? Ranking lists that reshuffle every few months show how perishable the conclusion is.
- Maintain a **watch list with a review date**, not a love for one tool.

## Common Mistakes
- Choosing from a benchmark chart.
- One-shot tests judged by taste.
- Comparing price per token, not cost per finished task.
- Building on a free tier or a prototype tool for production.
- Locking context and skills into one vendor's format.

## Checklist
- [ ] 5-10 own tasks with written criteria
- [ ] Blind or second judge
- [ ] Cost per completed task recorded
- [ ] Data terms, region and plan checked
- [ ] Portability: where do prompts, skills and data live
- [ ] Review date set

## Connects To
- ch05 (measuring), ch06 (risks), `coding-with-agents` ch06 (model choice), ch08 (evals), ch10 (building and testing agents), `scientific-thinking`, `software-architecture` for adapter and boundary design.
