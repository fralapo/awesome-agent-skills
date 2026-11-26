---
name: coding-with-agents
description: "Practical theory for building software with AI coding agents, for designer-developers and product builders. Use whenever the user builds, reviews, tests or maintains code with an agent or chat model, decides how much to delegate or read, writes a spec or instructions file, asks how to verify AI-generated code (differential testing, invariants, agentic QA), worries about quality, complexity or technical debt, asks what skills or career moves matter in the AI era, or needs LLM mechanics (sampling, token cost, caching, model choice, local versus hosted, tool use, context and harness design, evals, unattended-agent safety, security of generated code). Also covers long sessions and token use, agent environment setup (instructions, skills, memory, hooks), combining several agents, and building and testing automations with workflow tools and tool protocols. Separates facts from positions. Works with ai-adoption-in-organizations, ux-ui-expert and workshop-facilitation."
allowed-tools:
  - Read
  - Grep
argument-hint: [situation, topic, or chapter number]
---

# Coding with Agents
**Chapters**: 10 | **Corpus**: ~60 practitioner notes on programming with coding agents, reviewing and testing AI code, software quality, learning and careers, and how LLMs work, plus ~60 notes on session and token practice, agent environment, multi-agent setups and building agents with workflow tools | **Generated**: 2026-11-12, extended 2026-11-26

## Role and Boundaries

This skill **decides how to work with a coding agent or chat model**: how much to delegate, how to specify and steer, how to verify what comes back, how to keep a codebase small and changeable, how to learn and position yourself, and which LLM mechanics matter in practice. It gives methods, checklists and decision rules; the user owns the product and the code.

| This skill decides | This skill hands off |
|---|---|
| Delegation level, spec and task shape, steering loop, instrumentation | What the product should look and feel like, flows, hierarchy, microcopy, AI-assisted UI and design-to-code handoff → `ux-ui-expert` |
| How to verify AI output: differential tests, invariants, fuzzing, agentic QA, review by another model | Running a workshop to agree the spec, priorities or acceptance → `workshop-facilitation` |
| Complexity, dependencies, rewrites, irreversible decisions, product focus | Pricing and selling AI-assisted work, one-time vs subscription as an offer → `pricing-and-sales-negotiation` |
| Session hygiene, token trimming, agent environment (instructions, skills, hooks, memory), builder-versus-reviewer setups | Rolling AI out in a company: training, company knowledge, customer assistants, return on investment, tool comparison for the business → `ai-adoption-in-organizations` |
| Building and testing agents and automations with workflow tools and tool protocols | Market, offer and funnel logic behind a customer assistant → `marketing-mba` |
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
| Get better answers from a chat model; run agents unattended safely | ch06 sections 10-11 | ai-ml-concepts ch15 |
| Add AI features to a product | ch04 section 8 (invisible AI) | ch06, `ux-ui-expert` |
| Authentication or session code from an agent | ch06 section 7 | ch03 |
| Context budget, tool design, memory, sub-agents, guardrails in the harness | ch07 | ch02, ch06 section 4 |
| Measure an agent, trace failures, release it safely, retrieval quality, fine-tune or prompt | ch08 | ch07, ai-ml-concepts ch15 |
| Session getting expensive or slow, trimming the fixed prefix, handoff files, model and effort settings | ch09 sections 1-4 | ch06 section 4, ch07 section 1 |
| Set up the agent's environment: instructions file, skills, memory, hooks, permissions | ch09 section 6 | ch02, ch07 section 6 |
| Use two agents or tools together, blind-spot pass, sub-agents vs teams | ch09 section 7 | ch03, ch07 section 5 |
| Build an agent or automation in a workflow tool, connect it through a protocol server | ch10 sections 1-3 | ch07 sections 3-4 |
| Test a built agent or workflow (endpoints, edge cases, misuse, scale) | ch10 section 8 | ch08, ch03 |
| Roll AI out in an organization (training, company knowledge, customer assistants) | `ai-adoption-in-organizations` | ch10 |
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
| [ch07](chapters/ch07-context-engineering-and-agent-harness-design.md) | Context Engineering and Agent Harness Design | context as a budget, load/retrieve/externalise/compact/isolate, tool design, protocol-style tools, sub-agent contracts, memory write gates, workflow vs agent, guardrails in code |
| [ch08](chapters/ch08-evals-observability-and-production-agents.md) | Evals, Observability and Production Agents | outcome-first evals, calibrated judges, pass@k vs pass^k, regression gates, traces, failure taxonomy, autonomy ladder, agent security, retrieval quality, fine-tuning vs prompting |
| [ch09](chapters/ch09-sessions-tokens-environment-and-multi-agent-practice.md) | Sessions, Tokens, Agent Environment and Combining Agents | what a session pays for, one task per session, handoff files, trimming the fixed prefix, prompting habits, environment components and hooks, builder vs reviewer, blind-spot pass, sub-agents vs teams |
| [ch10](chapters/ch10-building-and-testing-agents-with-workflow-tools-and-protocols.md) | Building and Testing Agents with Workflow Tools and Protocols | workflow anatomy, build by hand vs assistant vs hybrid, protocol servers as a bridge, retrieval for builders, teams in a workflow tool, voice and chat agents, deterministic core, a ten-point test plan |

## Topic Index

- **Agent says "done" but it is not** → ch02, ch03
- **Agent environment: instructions file, hooks, skills, memory, permissions** → ch09 section 6, ch02
- **Authentication, sessions, hashing** → ch06
- **Builder vs reviewer, second model, blind-spot pass, agent teams** → ch09 section 7, ch03
- **Testing a workflow or automation** → ch10 section 8, ch08
- **Token trimming, handoff file, compaction vs rewind, model and effort changes** → ch09 sections 2-4
- **Workflow tools, protocol servers, no-code agents, retrieval for builders** → ch10, ch07 section 4
- **Code coverage, test strategy, random testing** → ch03
- **Complexity, simplicity, technical debt** → ch04
- **Context budget, compaction, memory, sub-agents** → ch07
- **Cost of tokens, subscriptions, prompt caching, Jevons effect, kill switch** → ch05, ch06 (sections 4, 11)
- **Habits for chat models (dossier, questions, red team, two models)** → ch06 section 10
- **Backups, isolation and approval points for unattended agents** → ch06 section 11
- **Deskilling, desirable difficulty, signal inflation** → ch05 section 9
- **Dependencies, vendoring** → ch04
- **Evals, judges, traces, failure taxonomy, staged rollout** → ch08
- **Fatigue, flow, parallel agents** → ch02, ch05
- **Instructions file, spec file** → ch02
- **Juniors, seniors, hiring, learning to code** → ch05
- **Local vs hosted models** → ch06
- **Model and vendor choice** → ch02, ch06
- **Product, platform, invisible AI** → ch04
- **Retrieval quality, RAG, fine-tuning vs prompting** → ch08
- **Rewrites and ports** → ch04, ch03
- **Sampling, temperature, loops** → ch06
- **Security of generated code** → ch06, ch03
- **Tool design, protocol-style tool interfaces** → ch07
- **Vibe coding vs supervised delegation** → ch01, ch02

## Related Skills

- `ux-ui-expert`: the interface, flows and AI-assisted UI decisions the agent does not make.
- `ai-adoption-in-organizations`: the organizational side: training, company knowledge, customer assistants, return and tool comparison.
- `workshop-facilitation`: facilitating the sessions that produce a spec, priorities or acceptance criteria.
- `pricing-and-sales-negotiation`: selling and pricing digital products and AI-assisted work.
- `freelance-designer-ops`: operating a practice around the build work.
- `art-director`, `creative-director`, `graphic-designer`: the visual and conceptual layer built on top.

## Scope & Limits

Practical theory distilled from many hours of practitioner commentary, mostly from systems and product programming in compiled languages and from the first agent-heavy period. Findings about agents are **dated snapshots**; vendor names, model comparisons, prices and security figures change quickly and secondhand statistics are unverified. Opinions about jobs, markets and the future are labelled as positions, not facts. The skill gives no legal, licensing or compliance advice and no guarantee that generated code is correct or secure; treat it as a method for verifying, not a substitute for it.
