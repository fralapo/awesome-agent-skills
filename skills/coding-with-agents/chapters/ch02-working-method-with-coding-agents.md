# Chapter 02: Working Method with Coding Agents

## Core Idea
Prompts are not the point; **steering is**. A non-trivial tool built with an agent takes hours of design conversation, constraint setting and small corrections, not one clever prompt. The method below is: design first, spec, bounded task, instrumented feedback, early interruption, independent review.

## 1. The Iteration Loop
1. **Design conversation before any agent.** In a plain chat with a strong model, explore alternatives, algorithms and feasibility, and test hard requirements. Cost: minutes. It prevents building the wrong thing.
2. **Define an MVP with explicit constraints.** Language, "no dependencies", allowed libraries, reference look, what is out of scope. Load references (papers, docs, API specs) into a local folder the agent can consult.
3. **Build a minimal core first.** Then add features one at a time. Describe the future shape of the data model up front (for example "grouping will be a tree") so the representation is not rewritten later.
4. **Steer each feature**: UX, performance, naming. Give concrete, observable feedback ("I see flicker; maybe the refresh rate is too high"), not abstract complaints.
5. **Give the agent ways to test itself** (section 4).
6. **Review** (ch03), then repeat.

The only time that counts is your interactive time; the agent's unattended run is not the cost.

## 2. Specification Before Code
- Write a spec or outline; a two-line prompt iterated by approximation is acceptable only if you lack design skill.
- Optionally refine the spec in a web chat: ask it to find unclear points, fragilities and non-orthogonal commands. Keep final design authority; its proposals may not match your taste.
- Include **design intuitions phrased non-bindingly** ("I suspect X works well here, but pick what you judge best") so the model is guided, not boxed in.
- **Leave no obscure points**: agents rarely ask. A few minutes of writing the critical decisions up front (what is shared, what is split, what must never happen) prevents the architectural errors that are costly to find later.
- Put **stack preferences and constraints in an agent instructions file** (which framework, which cache, "prefer fewer lines of code", "avoid new dependencies"). Do not blame a tool for its defaults when three lines would change them.
- Comment the **fundamental tensions** and the reasons for past fixes in the code; the agent reads them and keeps the invariants.

**Spec and code travel together.** One position: prose gives fast human understanding, code holds the fine interactions prose cannot express, and regenerating from a spec alone reintroduces already-fixed bugs. Agents also work in reverse: ask one to study a codebase and write the spec so it could be rebuilt, which is a good onboarding document.

## 3. Task Shaping
- **Bounded, isolated, not open-ended.** One concern per task, with a stated end condition.
- **Parallelise only non-conflicting tasks.** Avoid merge problems; meanwhile plan, test or start an unrelated task.
- **Separate research from implementation.** First understand the target (reference pipeline, data transforms, peculiarities), extract a spec and check it is exact. If the pipeline is complex, ask for a small self-contained reference version (hundreds of lines, in a high-level language). Only then implement. Never say "now look at my other implementations" before the understanding step is finished.
- **Reuse your own earlier work as a culture.** Point the agent at previous, optimised implementations in a folder and ask it to transfer their tricks to the new case. Generic frameworks are convenient but rarely the fastest; cheap agent time makes specialised code per case affordable.
- **Use different models for different phases**: a reliable one for most of the task, a more exploratory one for the hard parts. Get several candidate versions from different models, take the best ideas, then iterate while reading.
- **Dependency removal recipe that worked**: state the goal, convert only the needed part, write a thorough equivalence test between old and new, replace the calls, fix the build file, compile, run the project's tests.

## 4. The Decisive Trick: Give the Agent Eyes
An agent that cannot observe real state declares "done, everything works", sprays print statements, or papers over the problem. Instrument first, then change:
1. Ask the agent to **add observability** before the real task: a debug interface (a local socket with state dumps, breakpoints), dumps of internal state, a screenshot mode.
2. Build a **baseline or benchmark** that measures progress objectively.
3. Let it iterate against that. Its strengths are tenacity and speed: it can retry endlessly if it can see outcomes.
4. On a failure case, have the tool dump the failing input, analyse why it failed, and test whether an alternative would have succeeded.

Front-end variant: browser screenshots plus a simplified layout representation (box tree, computed styles), because the model cannot otherwise see the result. Design tools for agent use from the start: documented local API, simple commands, measuring primitives. Tests alone are not enough on complicated systems; add direct inspection.

## 5. Steering in Practice
- **Interrupt early** when you see the agent going wrong. Correcting before the mistake is like a mentor with a junior; doing it a couple of times a day changes output quality.
- **Ask the agent to announce each significant step.** It costs tokens, but you can follow, catch wrong directions and stay engaged.
- **Prefer tools that stay conversational while working** (you can ask mid-task) over long silent runs; silence removes your chance to steer.
- **If an agent loops for about an hour on a bug, open the code yourself.** The cause is often simple (a shift without clearing bits, a wrongly initialised field).
- **Restate in your own words** what the agent said it did; mismatches expose design errors.
- Start with a **clean, compact, well-commented core**. If you are far better than the model at the core, write it yourself; agents extend good structure and amplify bad structure.
- Give your own code as **style examples**; from-scratch output tends toward average, baroque code.

## 6. What the Harness Does (technical)
- Tool use is a model capability: given a manifest of tools (name, arguments, description, return shape), the model emits calls and the harness runs them and returns results in a loop. The loop is short script; a minimal one is already a basic agent. Clear tool descriptions matter more than the protocol.
- Edit tools: replacing "old text with new text" fails when the old text repeats; raw line numbers drift after earlier edits and duplicate lines. A stronger design keeps **state in the harness** (which line ranges the model last saw), invalidates or re-maps ranges that moved, and forces a re-read or says "what was 42-45 is now 47". Cheaper variants use short per-line hashes (single-token words cost fewer tokens than random tags) or a whole-file checksum. Different models prefer different tool formats from their training; test per model.
- See ch06 for token economics and security of tool servers.

## 7. Tool and Vendor Choice
- One position: agents are interchangeable because the interface is natural language and intelligence sits in the model (rough personal estimate: most of the leap came from model strength, a smaller part from orchestration). Keep more than one subscription, switch to whichever is best this month, and try low-cost open models in your pipeline to learn what top models add.
- Claims that one agent beats another on very hard tasks are **point-in-time personal results**. Re-test both at maximum reasoning effort on the same hard task; convenience (fast replies) can create a false sense of safety because the faster tool may make subtler mistakes.
- Respect each vendor's terms about which harness a subscription may be used in.

## 8. Pace, Flow and Fatigue
- Agent work fragments attention, removes flow and invites over-production ("flying with nowhere to go"). Symptoms: chronic tiredness, anxiety about overnight runs, many half-projects.
- Counter-measures: **one project at a time**; alternate phases where the model works from your idea with phases where you work directly in the code; tell the model what to do, read the source, change what you dislike, then show the model how you did it; use overnight runs only for well-defined goals (optimisation, bug hunting); fill model wait time with a different flow activity; keep fast compile/run cycles.
- Do not run 12-14 hour sessions. For paid work do not spend ten times the time for the pleasure of craft; keep craft for side projects.
- Running many parallel sessions removes dead time but trades away flow and raises stress; leave room to breathe.

## What Never to Do
- Click "accept, accept, accept" while claiming not to vibe code.
- Brute-force prompt until something works; inelegant patches accumulate until the code is incomprehensible.
- Give an open-ended task, or an unsupervised long task with serious consequences.
- Give agents access to production. Run permission-skipping modes only on a dedicated machine.
- Make humans the permanent cleanup crew for agent-written code as a team workflow; it recreates the bottleneck and the worst kind of work.
- Hide a failed approach: try variants cheaply, discard after minutes, A/B test.

## Checklist
- [ ] Design chat done before the agent started?
- [ ] Spec with constraints, no obscure points, instructions file updated?
- [ ] Task bounded; research separated from implementation?
- [ ] Observability and a baseline exist before the real change?
- [ ] I can interrupt: am I watching steps?
- [ ] One project at a time?

## Connects To
- ch01 (delegation spectrum), ch03 (verification), ch04 (keeping the codebase small).
- `workshop-facilitation` for turning a vague wish into an agreed spec with stakeholders; `ux-ui-expert` for the UX details to specify.
