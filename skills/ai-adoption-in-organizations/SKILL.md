---
name: ai-adoption-in-organizations
description: "Practical theory for introducing AI into companies, teams and small agencies: staff training and key users, shared company knowledge (a company brain) and where sensitive data may go (local versus public services), assistants for customers, leads and staff on messaging channels, case studies and how to measure return, priorities and order of adoption, and the main risks (answer reliability, contradictory source documents, prompt injection, over-broad access, unfiltered models, regulation and training duties). Includes how to compare tools and models on your own tasks without trusting hype or benchmarks. Use when the user plans, pitches, trains for, builds, buys or reviews an AI rollout, a company knowledge assistant, a customer or sales assistant, or asks what to adopt first and how to judge results. Labels practitioner consensus versus positions and flags unverified figures. Gives no legal, compliance or financial advice."
allowed-tools:
  - Read
  - Grep
argument-hint: [situation, topic, or chapter number]
---

# AI Adoption in Organizations
**Chapters**: 7 | **Corpus**: ~100 practitioner notes on training teams, company knowledge assistants, customer and sales automations, case studies, tool comparisons and AI risks | **Generated**: 2026-11-26

## Role and Boundaries

This skill **decides how an organization should introduce AI**: what to teach and to whom, what to build first, where the data may live, which assistants to put in front of customers and staff, how to judge a case study or a tool, and which risks to design against. It gives methods, checklists and decision rules; the organization owns its data, its choices and its legal duties.

| This skill decides | This skill hands off |
|---|---|
| Order of adoption, training design, key users, knowledge and data layout, human-in-the-loop points, pilot design and measurement, tool comparison method | Building, testing and verifying the agents, tools and automations themselves, context and token management, agent environment -> `coding-with-agents` |
| Which risks to design against and the conservative response to each | How models work (sampling, retrieval, embeddings, agents as concepts) -> `ai-ml-concepts`; system structure, storage, boundaries -> `software-architecture` |
| How to read vendor and consultant claims | Pricing an adoption service, proposals, negotiating with the client -> `pricing-and-sales-negotiation` |
| Customer-facing assistant design principles | Market, segmentation, offer, funnel and positioning -> `marketing-mba` |
| Training session shape | Facilitating the workshop itself -> `workshop-facilitation` |

**Stay in lane.** No legal, regulatory, tax, financial or medical advice: where a rule applies (data protection, AI regulation, platform terms, sector law), the skill says to check the current text and ask a professional. Models, prices and platform rules change every few months; every figure from a case is a self-reported snapshot to re-measure on your own work. No attack techniques are described.

## Facts vs Positions: how evidence is labelled

Concepts in the chapters have fields **Principle**, **How it works / sequence**, **Moves**, **Evidence**, **Trade-off** and **Does not hold when**. The **Evidence** line uses:
- **Practitioner**: taught the same way by several independent practitioners, no controlled test.
- **Observational**: a pattern seen across many cases; results are self-reported.
- **Position**: one practitioner's rule or forecast, written as such (for example "train before you build").
- **Contested**: practitioners disagree or the figure is unverified; the chapter gives the variants and a decision rule.
- **Fact**: arithmetic or documented mechanism (for example reliability compounding over steps).

Read **Does not hold when** before applying a rule.

## How to Use This Skill

Diagnose first: size and sector of the organization, who will use the AI, which data is involved, what exists today, who owns the process, and what a mistake would cost.

| Task | Start with | Then |
|---|---|---|
| "Where do we start with AI?" | ch01 | ch02, ch07 |
| Plan or sell a training programme | ch02 | ch01, ch05 |
| Set up shared company knowledge or a "brain" | ch03 | ch06 |
| Decide what may go to a public service, what stays local | ch03 section 3.6 | ch06 |
| Assistant for leads, customers, quotes, staff reports | ch04 | ch06, ch05 |
| Read a case study, estimate or prove return | ch05 | ch07 |
| Worry about wrong answers, conflicting documents, security | ch06 | ch03, `coding-with-agents` ch07-ch08 |
| Compare models or tools, decide cloud or open-weight | ch07 | ch05, `coding-with-agents` ch06 |
| Build the agent or automation | `coding-with-agents` ch09-ch10 | ch04 |
| Quick lookup | [cheatsheet.md](cheatsheet.md), [glossary.md](glossary.md) | |

## The Core Principles (recurrence order)

1. **People and process before software.** Train key users, then identify tasks, then build.
2. **Start small, internal and reversible.** A quick win beats a big swing as a first project.
3. **Fixed workflows with model calls at named points** beat free-roaming agents where the path is known.
4. **A person at both ends.** Define the task and own the result; the relationship with the end customer stays human.
5. **Data rules first.** Decide what may enter which service before anyone pastes anything.
6. **Cite or do not answer.** Numbers come from documents and queries, with source and date.
7. **Sources need owners.** Conflicting or stale documents are a design problem, not a model problem.
8. **Guardrails in code, not in prompts.** Deny by default, bind approvals to actions, cap spend.
9. **Measure before you believe.** Baseline, fixed period, full cost including review.
10. **Stay portable.** Own your context, skills and data; compare models on your own tasks and re-check on a calendar.

## Chapter Index

| # | Title | Key frameworks |
|---|---|---|
| [ch01](chapters/ch01-adoption-strategy-and-sequence.md) | Adoption Strategy, Priorities and Sequence | why projects fail, training before building, impact/complexity grid, workflow vs agent, human at both ends, order of adoption |
| [ch02](chapters/ch02-training-employees-and-key-users.md) | Training Employees and Key Users | four phases, second-brain template, three habits, skills per person, champions, funding and duties |
| [ch03](chapters/ch03-company-knowledge-and-sensitive-data.md) | Company Knowledge and Sensitive Data | layers, three technical patterns, linked files vs retrieval, permissions, sovereignty, local vs public, anonymisation |
| [ch04](chapters/ch04-customer-and-sales-assistants-on-messaging-channels.md) | Customer, Sales and Staff Assistants on Messaging Channels | lead reactivation, qualification scoring, staff reporting, quotes by email, layered sources with approval, platform rules |
| [ch05](chapters/ch05-case-studies-and-measuring-return.md) | Case Studies and Measuring Return | reading a case, case shapes, training vs custom, pilot measurement, numbers not to copy |
| [ch06](chapters/ch06-risks-reliability-security-and-unfiltered-models.md) | Risks | reliability compounding, contradictory sources, injection and access, cost loops, generated-app security, unfiltered models, regulation |
| [ch07](chapters/ch07-evaluating-tools-and-models-without-hype.md) | Evaluating Tools and Models Without Hype | same-prompt tests, benchmarks, model per task, cost per task, lock-in, prototype vs production, reading hype |

## Topic Index

- **Anonymisation, local vs public, free-tier data use** -> ch03
- **Benchmarks, model choice, cost per task** -> ch07
- **Case studies, ROI, baseline** -> ch05
- **Company brain, wiki, retrieval, text-to-query** -> ch03
- **Contradictory documents, source precedence** -> ch06
- **Customer assistant, lead reactivation, qualification** -> ch04
- **Key users, champions, workshops** -> ch02
- **Order of adoption, quick wins, workflow vs agent** -> ch01
- **Prompt injection, access, spend caps** -> ch06
- **Regulation, training duties, funding** -> ch02, ch06
- **Unfiltered models, security testing of your own apps** -> ch06
- **Vendor lock-in, portability** -> ch03, ch07

## Related Skills

- `coding-with-agents`: building, verifying and operating the agents and automations; context, memory, tools, evals.
- `ai-ml-concepts`: how the models, retrieval and agents work underneath.
- `software-architecture`: boundaries, storage and integration around the assistant.
- `pricing-and-sales-negotiation`: selling and pricing adoption work.
- `marketing-mba`: market, offer and funnel decisions the assistant serves.
- `workshop-facilitation`, `scientific-thinking`, `llm-wiki`: running sessions, judging evidence, building a wiki-style knowledge base.

## Scope & Limits

Practical theory distilled from practitioner commentary, mostly from small and mid-sized organizations and from automation consultancies; much of it comes from people who sell training or systems, and automatic captions were the main text source. Case figures (revenue, hours saved, response rates, savings) are **self-reported and often internally inconsistent**, so none are reproduced as facts; failure statistics quoted in the field are unverified. Product names, prices, platform policies and model rankings are omitted on purpose because they change quickly. Opinions about markets, regulation and the future are positions, not facts. The skill gives no legal, compliance, financial or clinical advice and does not guarantee that any assistant is correct or secure.
