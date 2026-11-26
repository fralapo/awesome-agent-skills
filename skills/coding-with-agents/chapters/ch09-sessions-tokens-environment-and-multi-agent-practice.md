# Chapter 09: Sessions, Tokens, Agent Environment and Combining Agents

## Core Idea
Ch06 and ch07 explain why cost and quality follow context length; this chapter is the **daily practice** that follows: how to measure what a session carries, how to keep it small, how to configure the agent's environment (persistent instructions, skills, memory, rules, hooks), and how to combine several agents or tools so that the one that builds is not the one that judges. Most of it is cheap to try and easy to measure on your own work.

Facts vs positions: that the whole history is re-read every turn, that switching model or effort mid-session breaks a cached prefix, and that tool and skill definitions occupy context before you type are mechanics (ch06 section 4, ch07). Specific thresholds, "percent saved" claims and preferred line counts are **positions or contested**: practitioners report very different values, so this chapter gives none as a rule. Measure on your task.

## 1. What a Session Pays For
- Each turn re-reads the conversation. A long session therefore costs far more than the same work split into focused ones.
- **Fixed prefix** before your first word: system prompt, the persistent instructions file, descriptions of installed skills, definitions of every connected tool server. Idle tool servers cost context even when unused.
- Variable load: files read, tool output, your messages, the agent's reasoning and replies.
- **Quality, not only cost**: past a certain fill level (position; reports range from roughly half the window upward) answers degrade and earlier constraints are lost. Find your own knee (ch07 section 1).

## 2. Measure Before Trimming
- Use the agent's context meter and usage view to see how full a fresh session already is; a high number at the start means the fixed prefix is the problem.
- Put a persistent status line (model, context percentage) in the terminal so the number is always visible.
- Record a baseline for one repeated task, change one thing, record again. Tools claiming very large savings often drop information: test that the answers did not get worse.

## 3. Session Hygiene
- **One task, one session.** Clear or start fresh when the task changes. A new conversation is cheap; a polluted one is expensive and confused.
- **Decide model and effort at the start** and keep them. Changing mid-session forces a re-read of the whole history at full price.
- **Match effort to the job**: low for tidying, medium for a document, high for a refactor or architecture. Lower effort reduces reasoning, not the length of the reply; ask for a concise output style separately.
- **Avoid automatic compaction when you can.** The tool decides what to keep, and it may drop a constraint stated once. Prefer rewinding to an earlier point, or writing a **handoff file** and starting fresh.
- **Handoff file contents**: the goal, decisions made and why, problems met and how they were solved, files touched, open questions, next steps. Paste or reference it in the new session. This is the externalise/compact move of ch07 done by hand, with you controlling what survives.
- **Parallel sessions**: use separate working copies of the repository (version-control worktrees) so edits never collide; give each session a bounded task.

## 4. Trimming the Fixed Prefix
- **Instructions file as an index.** Keep it short; point to documents read on demand. Reported targets differ widely (tens of lines to a few hundred), so treat any number as a **Contested** guideline and test whether the agent still follows the rules that matter. A per-folder instructions file keeps local rules out of the global one.
- **Skills load on demand.** A skill's short description sits in context; its body loads only when triggered. A project-level prompt, by contrast, is sent every turn. Move rarely used procedures into skills, shorten descriptions, archive unused skills.
- **Disable tool servers you are not using**, and prefer a command-line tool with filtered output to a protocol server for local, repeated technical work (ch07 section 4). Protocol servers can add thousands of tokens of definitions before first use; the figure depends on the server.
- **Pre-process bulky input in code.** Extract text from long PDFs with a script and give the agent the text; keep direct reading for charts and images. Convert anything repeatable and judgement-free into a script and call it.
- **Code-map tools** that index a codebase help on large repositories but may cost more than they save on small ones (**Contested**; test).
- **Sub-agents save context only for bulk work** (many files, many sources). For a small task the brief and report cost more than the work.

## 5. Prompting Habits for Strong Models
- Describe the **goal, the audience, and what "done" looks like**; with a strong model, a goal beats a step list.
- Give the **reason** instead of a bare prohibition: not "never invent figures" but "every figure must come from a document because this goes to a client". Position: bare bans can derail a capable model.
- **Have it interview you** before it works, and dictate instead of typing when the context is long.
- **Show before building**: a text sketch, then a mockup, then code; cheaper to change.
- **Search for existing solutions first** (forums, repositories) before asking the agent to invent one.
- **Ask for proof**: a rubric and an end-to-end run by the model itself, then your own check (ch03).
- **Refresh old prompts and skills** written for weaker models; remove obsolete prohibitions and over-detailed steps.
- A classic six-part prompt (role, objective starting with a verb, specifications, context, examples, closing constraints repeated because start and end carry weight) still works as a checklist; figures claimed for the gain of each part are unverified.

## 6. Configuring the Agent's Environment
Think of five components of a persistent assistant (a position that works as a checklist):
- **Identity**: tone and working style in a file the agent reads at start.
- **Instructions and rules**: the index file plus rules for stack, conventions and non-goals (ch02).
- **Memory**: facts and history outside the window, with the write path controlled (ch07 section 6). Keep a file stating how fast each kind of fact goes stale.
- **Skills and connectors**: procedures and tool access; test each connector the moment it is added with one concrete question, and restart after adding if the client requires.
- **Hooks and permissions**: instructions are advisory; **hooks run deterministically** before or after actions (block a command, scan a downloaded skill, format on save). Permission modes that skip confirmations speed work and widen the blast radius: pair them with isolation (ch06 section 11).
- Also: an overview file describing the stack and what each file does, so the instructions file stays short; a private version-controlled repository as backup; secrets in environment files, never pasted into a chat.
- **Vet downloaded skills and plugins.** They are instructions your agent will follow; a malicious one can steer it. Read them or have a scanning hook check them before install.
- **Maturity ladder (position)**: assistant in chat -> colleague working on files -> director orchestrating several instances -> a self-feeding system. Climb one step at a time, and stop where the cost of supervision exceeds the gain.

## 7. Combining Agents and Tools
- **The builder is not the judge.** Use a second model or tool for review: it catches different errors (ch03 section on a model as reviewer). A common flow: strongest model drafts the plan; a second tool runs an **adversarial review** of it; the first answers; repeat until no objections; a person reads the critiques; a capable model implements; a security review and a final cross-check follow.
- **Blind-spot pass before touching code**: in a separate working copy, let several read-only agents explore the codebase in parallel and report hidden constraints, sorted as known knowns, known unknowns, unknown knowns and unknown unknowns. Typical finds: a committed secret, files missing from the ignore list, two deploy paths to the same target. Then interview the person on the known unknowns, one question at a time; show several design directions with fake data before implementation.
- **Do not split a feature by difficulty across models** ("80% with the cheap one, the hard 20% with the strong one"): coherence is lost. Split by role: plan, implement, review.
- **Strong planner, cheaper executor** is a common setup; confirm on your tasks that the cheaper model follows the plan.
- **Sub-agents vs agent teams.** Sub-agents work in parallel without talking to each other and cost less. Teams that message each other and share a task list cost more tokens, and pay off only for truly parallel work (position: a handful at most). Define the **contract first** (for example the API shape between backend and frontend) so parallel work fits together. Never merge a team's output without review.
- **When to switch tools**: a bug the first agent circles on, a full context, a usage limit, or a need for an independent opinion.
- **Cost of two subscriptions or two tools** is often smaller than the cost of one unreviewed mistake; decide on measured value, not preference.

## Common Mistakes
- Never checking how full the session is at the start.
- Switching model or effort mid-session, then wondering why cost jumped.
- Leaving every tool server and skill enabled "just in case".
- Trusting automatic compaction with a constraint stated once.
- A single huge instructions file loaded every turn.
- Installing skills or plugins without reading them.
- Using the same model to build and to approve.
- Spawning agents for a task smaller than the brief.

## Checklist
- [ ] Fixed prefix measured at session start
- [ ] One task per session; model and effort fixed
- [ ] Handoff file template ready
- [ ] Instructions file is an index; rarely used procedures are skills
- [ ] Unused tool servers off; CLI preferred for local repeated work
- [ ] Bulky input pre-processed in code where text is enough
- [ ] Hooks for what must always happen; secrets in environment files
- [ ] Downloaded skills read before use
- [ ] Builder and reviewer are different models or tools
- [ ] Parallel work in separate working copies with a contract defined first

## Connects To
- ch02 (loop, instructions file), ch03 (checking), ch06 sections 4 and 11 (cost, unattended safety), ch07 (context as a budget, memory, sub-agents), ch10 (building agents).
- `software-engineering-practice` for version control and review habits.
