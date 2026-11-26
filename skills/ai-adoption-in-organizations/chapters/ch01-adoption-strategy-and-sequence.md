# Chapter 1: Adoption Strategy, Priorities and Sequence

## Core Idea
An organization does not adopt AI by buying a tool; it changes how people do recurring work. Most disappointing projects share a pattern: a large custom build started before the people, the processes and the data were ready. The practitioner consensus in this skill is that **people and process come first, software second**, and that the first visible win should be small, internal and cheap to reverse. Evidence labels used throughout: **Practitioner** (several independent practitioners teach it the same way, no controlled test), **Observational** (a pattern across many cases), **Position** (one practitioner's rule), **Contested** (practitioners disagree).

## 1.1 Why adoption projects fail
- **Principle**: Failure is rarely about the model. It comes from unrealistic expectations (replacing a whole department), fear of missing out instead of a strategy, ageing systems without interfaces, a team that was never prepared, rigid processes, and test periods that were too short.
- **How it works / sequence**: Before choosing a tool, write down which recurring task hurts, who owns it, how it is done today, and what "good" looks like.
- **Moves**: Ask the guiding question "if the owner were away for a month, would the work continue?" If not, the knowledge sits in one head and that is the first thing to extract.
- **Evidence**: Practitioner for the causes. **Contested** for the headline statistics ("most custom AI projects fail"): such figures circulate without a checkable source and differ by who quotes them. Use them as a mood, never as a number in a proposal.
- **Trade-off**: A cautious start looks slower in a quarter and is faster over a year.
- **Does not hold when**: The organization already has strong data infrastructure and engineers; then a custom build may be the right first step.

## 1.2 Training before building
- **Principle**: Trained people who know their own tasks usually return value sooner than a custom system built for people who do not yet know what to ask of it.
- **How it works / sequence**: Educate, then identify where time goes, then develop. Each stage must produce something usable before the next starts.
- **Moves**: Train a few "key users" per department first; let them find the repetitive tasks; build tools only for what survives that screening.
- **Evidence**: Position (stated forcefully by many adoption consultants, who also sell training). Treat the conflict of interest as a reason to measure, not to dismiss.
- **Trade-off**: Training raises demand for tools, which later costs money.
- **Does not hold when**: The task is already well-defined, high-volume and the same everywhere (for example routing one kind of email); then a narrow tool can come first.

## 1.3 Pick opportunities with an impact/complexity grid
- **Principle**: List candidate tasks, score each on business impact and implementation complexity, and start in the high-impact, low-complexity corner (quick wins). Keep one or two "big swings" as later bets.
- **How it works / sequence**: Task audit: group work into areas, break each area into atomic tasks, mark frequency, time, risk and data needed. Build a minimum version in a few weeks, test internally, then on a small number of customers or users.
- **Moves**: Prefer a **fixed workflow with model calls at named points** over a free-roaming agent where the path is known. Workflows are predictable, cheaper and testable; agents earn their place only where interpretation is needed (see `coding-with-agents` ch07).
- **Evidence**: Practitioner.
- **Trade-off**: Fixed workflows break on unusual inputs; agents handle them but are harder to bound.
- **Does not hold when**: Inputs are open-ended by nature (research, triage of unknown requests).

## 1.4 Keep people at both ends
- **Principle**: Put a person at the start (defining the task, the context, the criteria) and at the end (checking and owning the output), with the machine in the middle. The relationship with the end customer stays with people; automation mostly lives behind the scenes.
- **Moves**: Name an owner for every automated output. Require that numbers in any deliverable be traceable to a document.
- **Evidence**: Practitioner.
- **Trade-off**: Review time eats part of the saving.
- **Does not hold when**: The output is low-risk and reversible (an internal reminder).

## 1.5 A reasonable order of adoption
1. Policy and data rules (what may go into which service). 2. Training of key users and a first shared template. 3. A few skills or automations per team on repetitive tasks. 4. A shared knowledge layer ([ch03](ch03-company-knowledge-and-sensitive-data.md)). 5. Customer-facing assistants ([ch04](ch04-customer-and-sales-assistants-on-messaging-channels.md)), only after internal use is stable. 6. Measurement and review ([ch05](ch05-case-studies-and-measuring-return.md)).
- **Evidence**: Position; the order is a defensible default, not a law. Different priorities (a sales-heavy business may put a lead assistant earlier) are legitimate if the data rules come first.
- **Trade-off**: Customer-facing work is the most visible win and the most exposed to error.

## 1.6 Time pressure and the pace of change
- Capabilities, vendors and prices change every few months; "late adopters lose ground" is a **Position** used to sell urgency. A better test: what does waiting three months cost, and what does a mistake in the next three months cost?
- Reassess tool choices on a calendar (for example every quarter) and keep skills, data and context in formats you own so a swap is cheap.

## Common Mistakes
- Starting with agents because they sound advanced.
- Skipping departments that are not "technical", then wondering why adoption stalls.
- Expecting perfection on day one and abandoning at the first wrong answer.
- Using unverified failure statistics as proof.
- Building before the task is described in writing.

## Checklist
- [ ] Task written down with owner, frequency, time and "done" criterion
- [ ] Impact/complexity grid filled; first project is a quick win
- [ ] Workflow vs agent decided on purpose
- [ ] A person at both ends of every automated output
- [ ] Data rules agreed before any customer data is used
- [ ] Review date set to reassess tools

## Connects To
- ch02 (training), ch03 (knowledge and data), ch05 (return), ch07 (choosing tools).
- `coding-with-agents` for building and verifying the tools; `marketing-mba` for market and positioning questions; `pricing-and-sales-negotiation` for pricing an adoption engagement or selling it internally.
