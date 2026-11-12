# Chapter 01: The Mental Model — When AI Helps and When It Hurts

## Core Idea
A coding agent is a fast, tireless, broadly knowledgeable executor with no taste, no product sense and weak self-awareness about what it does not know. In this model the human supplies **ideas, constraints and judgment**; the agent supplies **implementation bandwidth**. Results depend far more on how much of the design the human keeps than on which tool is used. AI is a **multiplier of the culture it is used in**: care and tests produce more quality, carelessness produces more mess, faster.

Separate in every sentence what is a **technical fact** (can be checked) from what is a **position** (a judgment or forecast). This skill marks positions as "One position is...".

## 1. Two Moments in Programming
| Moment | What it is | Who does it now |
|---|---|---|
| Concept | What to build, what NOT to build, how the parts relate, which trade-offs | Human (the agent can survey options but does not choose with taste) |
| Implementation | Turning the concept into code, wiring, ports, boilerplate, repetitive fixes | Increasingly delegated |

One position is that the concept moment gains value as implementation gets cheap: choosing what is worth building, UX details, menu behaviour, remembered state and architecture are not decided autonomously by models. A designer-developer already works in the concept moment, so the leverage is large.

## 2. The Delegation Spectrum
Positions in use, from least to most delegation. Pick per task, not per career.

| Mode | How it works | Fits |
|---|---|---|
| 0. No AI | Everything by hand | Learning, tiny craft programs |
| 1. Chat as consultant | Ask in a plain chat, read the answer like an email from a colleague, paste by hand | Delicate code, unfamiliar maths or algorithms, learning |
| 2. Agent on bounded tasks | Spec file, isolated task, review the result | Most product work today |
| 3. Hands-off | Agent designs, codes and writes its own tests; human judges the final behaviour | Prototypes, throwaway tools, non-programmers |

**Decision rule.** Delegate more when the task is **isolated, well specified, observable and testable**. Read the code (stay at mode 1-2) when it is **core, security-sensitive, performance-critical, or when you are learning**.

**Contradiction in the field.** One position: reading all generated code makes you the bottleneck, so control ideas and behaviour and open code only when something is wrong. Another position: read and understand every line you or the model writes. The rule above reconciles them; see ch03 for what to check instead of reading.

## 3. Where AI Helps (technical, repeatable)
- **Breadth of knowledge**: the algorithm, data structure or mathematical tool you only half remember; the concept behind an unfamiliar platform.
- **Bug finding** on delicate low-level code, even when you do not trust its patches. Finding the bug is the valuable part; write the fix yourself if unsure. Calibrate with a **backtest**: take the commit before a known fix and see whether the model finds the bug.
- **Mechanical work**: porting a module, removing a dependency, wiring, build files, test scaffolding.
- **Tooling that was too expensive to write**: debug interfaces, test harnesses, comparison tools, exporters.
- **Exploration of a design space**: "which approaches exist, how could they combine for my context" while you make the combination decision.
- **Tutoring**: a tireless tutor that is sometimes wrong, good on fundamentals.
- **Text domains with fast feedback**: backend, scripts, systems code. Agents are weaker on UI and visual work because a screenshot or embedding loses information (see ch02 for mitigation).

## 4. Where AI Hurts
- **Open-ended tasks** ("make it faster", "make me an awesome X"): you get one of all possible results, none of your choices.
- **Long unattended runs** on high-consequence work: errors compound multiplicatively (full system administration, production changes).
- **Code size and complexity**: agent output tends to be verbose and over-layered (a pattern of 10,000 lines where 1,000 would do), adds dependencies unprompted, and reproduces average code when starting from nothing.
- **Poorly known libraries**: if the model barely knows a new or unusual library, you must teach it first and it may be slower than writing by hand.
- **Skill erosion**: delegating every snippet erodes fluency; passive delegation hurts comprehension and debugging (ch05).
- **Attention**: many parallel sessions fragment focus and cause fatigue (ch02).
- **Agents rarely stop to ask** when a requirement is unclear; they guess.

## 5. Match the Workflow to the Software
| Kind of software | Workflow |
|---|---|
| Idea matters more than implementation (typical business app, landing, internal tool) | Strong product design and clear intent already beat typical results; delegate more |
| Foundational or performance-critical (database, parser, engine, kernel code) | Treat as a white box: put technical detail in the prompt, get several candidate versions, read and hand-polish the core. Pure "judge only the effects" coding fails; vague "make it faster" produces nothing clever |
| Numerical / ML code | Compare against a reference implementation (ch03); plausible output proves nothing |
| UI and visuals | Give the agent a way to see (screenshots, simplified layout dump); specify UX details yourself |

## 6. Three Camps and One Habit
Programmers split into those who deny AI, those who collaborate with it, and those who hand everything to agents. Do not spend effort converting others. **Re-evaluate your own position every 3-6 months**: capability moved sharply with each model generation, and advice written for older agents (for example "always mediate through chat because agents compound errors") may no longer hold. Test claims on your own work; published productivity figures and personal multipliers differ widely.

## Common Mistakes
- Judging the technique from one bad answer. A bad answer usually means a bad question or too little context; ask again from another angle.
- Assuming a demo on an easy case (a small front end) generalises to complex, changing requirements.
- Treating lines of code, or percentage of code written by AI, as a productivity measure. Fewer lines is usually better.
- Choosing a stack for the pleasure of writing it once nobody reads the code; optimise instead for speed, easy deployment, succinctness and how well the model knows the stack.
- Elaborate personal rituals (dozens of hand-tuned skills) that give an illusion of expertise; the learning curve is short and the real skill is **calibrating trust**.

## Checklist
- [ ] Which delegation mode fits this task, and why?
- [ ] Is the task isolated, specified, observable, testable? If not, do I read the code?
- [ ] Am I keeping the concept moment (what, what not, trade-offs) for myself?
- [ ] Do I know what "done" looks like in observable behaviour?
- [ ] When did I last re-test my assumptions about what agents can do?

## Connects To
- ch02 (how to run the loop), ch03 (what to verify instead of reading), ch05 (skills and careers).
- `ux-ui-expert` for the product and interaction decisions the agent will not make; `workshop-facilitation` to settle design intent with a team before the agent starts.
