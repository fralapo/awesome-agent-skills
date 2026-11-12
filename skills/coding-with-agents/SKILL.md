---
name: coding-with-agents
description: "Practical theory for building software with AI coding agents (automatic programming), written for designer-developers and product builders. Use whenever the user builds, reviews, tests or maintains code with an agent or chat model, decides how much to delegate or read, writes a spec or instructions file for an agent, asks how to verify AI-generated code (differential and random testing, invariants, observability, agentic QA), worries about software quality, complexity, dependencies, rewrites or technical debt, asks what skills or career moves matter in the AI era (juniors, seniors, learning methods, mentoring, fatigue), or needs to understand how LLMs behave (sampling and temperature, reasoning, token cost, model and vendor choice, local versus hosted, tool use, basic security of generated code such as authentication). Separates technical facts from positions and forecasts. Works with ux-ui-expert, workshop-facilitation and pricing-and-sales-negotiation."
allowed-tools:
  - Read
  - Grep
argument-hint: [situation, topic, or chapter number]
---

# Coding with Agents
**Chapters**: 6 | **Corpus**: ~60 practitioner notes on programming with coding agents, reviewing and testing AI code, software quality, learning and careers, and how LLMs work | **Generated**: 2026-11-12

## Role and Boundaries

This skill **decides how to work with a coding agent or chat model**: how much to delegate, how to specify and steer, how to verify what comes back, how to keep a codebase small and changeable, how to learn and position yourself, and which LLM mechanics matter in practice. It gives methods, checklists and decision rules; the user owns the product and the code.

| This skill decides | This skill hands off |
|---|---|
| Delegation level, spec and task shape, steering loop, instrumentation | What the product should look and feel like, flows, hierarchy, microcopy, AI-assisted UI and design-to-code handoff → `ux-ui-expert` |
| How to verify AI output: differential tests, invariants, fuzzing, agentic QA, review by another model | Running a workshop to agree the spec, priorities or acceptance → `workshop-facilitation` |
| Complexity, dependencies, rewrites, irreversible decisions, product focus | Pricing and selling AI-assisted work, one-time vs subscription as an offer → `pricing-and-sales-negotiation` |
| Learning method, career positioning, team and cost governance (as positions) | Visual direction and identity → `art-director`, `creative-director`, `graphic-designer`; operating a freelance practice → `freelance-designer-ops` |
| Sampling, tool use, tokens, model choice, local vs hosted, security checklist | Language- or framework-specific reviews, deep security audits, legal and licensing advice → specialist skills or professionals (not in this skill) |

**Stay in lane.** This skill does not write the user's product code for them as a substitute for the steps above, and it does not invent benchmarks. Models, prices and agent capabilities change every few months; every dated claim here is a snapshot to re-test.

## Facts vs Positions

The source material mixes verifiable engineering facts with opinions and forecasts. Keep them apart in your answers:
- **Fact**: can be checked (token and sampling mechanics, cache and memory costs, hashing and cookie practice, testing techniques).
- **Position**: written as "One position is..." or "In this model...". Examples: do not read generated code; no test-first development; agents are interchangeable; the gap between strong and average programmers narrows; productivity multipliers; job forecasts.
- When two positions conflict, the chapters give both and a **decision rule** (for example "delegate more when the task is isolated, specified, observable and testable; read the code when it is core, security-sensitive, performance-critical, or you are learning").

## How to Use This Skill

Diagnose before prescribing: ask what is being built, how critical it is, whether the user reads code, what exists to observe and test it, and which model and agent are in use.

| Task | Start with | Then |
|---|---|---|
| "Should I let the agent do this?" | ch01 | ch02 |
| Start a new project with an agent | ch02 (loop, spec) | ch04 (constraints, non-goals) |
| Agent keeps failing or says "done" falsely | ch02 section 4 (give it eyes) | ch03 |
| Review or trust AI-generated code | ch03 | ch06 section 7 (security) |
| Write tests / prompt for better tests | ch03 sections 3-4 | ch02 |
| Code getting messy, too many dependencies, rewrite or port | ch04 | ch03 (equivalence) |
| What to hand-code, how to learn, junior/senior, tiredness | ch05 | ch01, ch02 section 8 |
| Pick a model, temperature, estimate token cost, local vs hosted | ch06 | ch02 section 7 |
| Add AI features to a product | ch04 section 8 (invisible AI) | ch06, `ux-ui-expert` |
| Authentication or session code from an agent | ch06 section 7 | ch03 |
| Quick lookup | [cheatsheet.md](cheatsheet.md), [patterns.md](patterns.md), [glossary.md](glossary.md) | |

## The Core Principles (recurrence order)

1. **Steering, not prompting.** The work is design conversation, constraints and small corrections; interrupt early.
2. **Keep the concept for yourself.** What to build, what not to build and the trade-offs are human decisions; delegate implementation.
3. **Write the spec; leave no obscure points.** Agents rarely ask. Put stack preferences in an instructions file.
4. **Bound the task.** Isolated, with an end condition; research before implementation; parallelise only non-conflicting work.
5. **Give the agent eyes.** Observability, baselines and screenshots before the real change.
6. **Check ideas and states, not every line.** Differential tests, invariants, scale, a second model as reviewer. Read the code that is core or sensitive.
7. **Complexity is the enemy, not debt.** Refuse features, minimise dependencies, simplify the idea, stay rigorous in the details.
8. **Ship a good product before generalising.** A product is the sum of many decisions; AI should be invisible and remove friction.
9. **Keep your fluency.** Know one language by heart, write small things by hand, use AI as tutor, keep the struggle on fundamentals.
10. **Calibrate trust and re-test.** Capabilities, vendors and best practice move every few months; judge technology on your own measured work.

## Chapter Index

| # | Title | Key frameworks |
|---|---|---|
| [ch01](chapters/ch01-mental-model-and-when-ai-helps.md) | The Mental Model: When AI Helps and Hurts | concept vs implementation, delegation spectrum, decision rule, workflow by software type, three camps |
| [ch02](chapters/ch02-working-method-with-coding-agents.md) | Working Method with Coding Agents | iteration loop, spec first, task shaping, instrument-then-change, steering, harness, flow and fatigue, never-do list |
| [ch03](chapters/ch03-reviewing-and-verifying-ai-output.md) | Reviewing and Verifying AI Output | checking ideas over code, state coverage, differential and random testing, invariants, agentic QA, model as reviewer |
| [ch04](chapters/ch04-software-quality-and-complexity.md) | Software Quality and Complexity | debt vs systemic complexity, indirection, dependencies and vendoring, rewrites, irreversible decisions, product over platform, invisible AI |
| [ch05](chapters/ch05-learning-talent-and-career.md) | Learning, Talent, Careers and Teams | isolation then access, learning with AI, value concentration, juniors and seniors, cost governance, wellbeing |
| [ch06](chapters/ch06-how-llms-work-for-practitioners.md) | How LLMs Work for Practitioners | sampling, reasoning and context, tool-use loop, token economics, model choice, local inference, security checklist, trust calibration |

## Topic Index

- **Agent says "done" but it is not** → ch02, ch03
- **Authentication, sessions, hashing** → ch06
- **Code coverage, test strategy, random testing** → ch03
- **Complexity, simplicity, technical debt** → ch04
- **Cost of tokens, subscriptions** → ch05, ch06
- **Dependencies, vendoring** → ch04
- **Fatigue, flow, parallel agents** → ch02, ch05
- **Instructions file, spec file** → ch02
- **Juniors, seniors, hiring, learning to code** → ch05
- **Local vs hosted models** → ch06
- **Model and vendor choice** → ch02, ch06
- **Product, platform, invisible AI** → ch04
- **Rewrites and ports** → ch04, ch03
- **Sampling, temperature, loops** → ch06
- **Security of generated code** → ch06, ch03
- **Vibe coding vs supervised delegation** → ch01, ch02

## Related Skills

- `ux-ui-expert`: the interface, flows and AI-assisted UI decisions the agent does not make.
- `workshop-facilitation`: facilitating the sessions that produce a spec, priorities or acceptance criteria.
- `pricing-and-sales-negotiation`: selling and pricing digital products and AI-assisted work.
- `freelance-designer-ops`: operating a practice around the build work.
- `art-director`, `creative-director`, `graphic-designer`: the visual and conceptual layer built on top.

## Scope & Limits

Practical theory distilled from many hours of practitioner commentary, mostly from systems and product programming in compiled languages and from the first agent-heavy period. Findings about agents are **dated snapshots**; vendor names, model comparisons, prices and security figures change quickly and secondhand statistics are unverified. Opinions about jobs, markets and the future are labelled as positions, not facts. The skill gives no legal, licensing or compliance advice and no guarantee that generated code is correct or secure; treat it as a method for verifying, not a substitute for it.
