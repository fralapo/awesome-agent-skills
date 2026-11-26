# Patterns

Recurring situation → move. Each entry: When / Move / Trade-offs. Chapter in brackets.

## Starting a new tool with an agent
**When**: empty folder, an idea.
**Move**: design chat with a strong model; MVP definition with constraints and references; minimal core; one feature at a time; build the debug/observability interface early. [ch02]
**Trade-offs**: hours of steering, not minutes; avoids a generic result.

## The agent says "done" and it is not
**When**: green claim, broken behaviour.
**Move**: stop; ask for observability (state dump, screenshot, benchmark); define the baseline; re-run against it. If it loops for about an hour, open the code yourself. [ch02, ch03]
**Trade-offs**: setup time; makes later iterations cheap.

## Reviewing a large AI diff
**When**: too much to read.
**Move**: write the critical decisions first; ask "how did you implement X?"; read the short answer; ask targeted questions; run randomised tests against a reference; have another model review. Read core and security parts anyway. [ch03]
**Trade-offs**: relies on good tests and your design sense.

## Porting or rewriting
**When**: move to another language or framework.
**Move**: first restructure the source to the intended design, then translate (or redesign during the port); write an equivalence test; do not accept "old tests pass". [ch04, ch03]
**Trade-offs**: more upfront work; avoids a wrong shape locked in.

## Dependency creep
**When**: the agent keeps adding packages.
**Move**: instructions file rule "avoid new dependencies"; implement small stable pieces; vendor small libraries; library only for hard domains. [ch04]
**Trade-offs**: more own code; far fewer updates and breakages.

## Code is growing but the product is not better
**When**: many features, complexity rising.
**Move**: list non-goals; refuse low-value features; stop and refactor when fragility shows; measure resource usage, not features. [ch04]
**Trade-offs**: slower feature count; healthier base.

## Performance-critical component
**When**: parser, store, engine.
**Move**: write design goals; get several candidate versions from different models; take the best ideas; iterate while reading; final hand pass (duplicated logic, state, missing cases); measure. [ch01, ch03]
**Trade-offs**: more reading; avoids "fast but poor".

## Tired and scattered after weeks of agents
**When**: many projects, constant waiting.
**Move**: one project at a time; alternate agent and hands-on phases; fill waits with a different flow activity; overnight runs only for well-defined goals. [ch02]
**Trade-offs**: lower apparent throughput; sustainable.

## Wanting to learn programming with AI
**When**: beginner or career changer.
**Move**: plain chat first; build toy programs by hand; AI as tutor and paper reader; reread hard material; one language by heart. [ch05]
**Trade-offs**: slower first months; real skill.

## Adding an AI feature to an app
**When**: product team wants "a chat".
**Move**: find a friction point; conventional retrieval or statistics first; LLM pass to re-rank, validate and normalise with explicit criteria; no chat unless the chat is the product. [ch04, ch06]
**Trade-offs**: less marketable, more useful.

## Generated login/auth code
**When**: agent wrote sessions and passwords.
**Move**: run the auth checklist (slow salted hash, identical errors, backoff, session ID rules, cookie flags, reset path, 2FA); add rules to the instructions file. [ch06]
**Trade-offs**: review time; avoids classic breaches.

## Agent gets worse late in a long run
**When**: the task succeeds early and fails late, or the context keeps growing.
**Move**: measure the quality knee on your task; keep the fixed prefix small; compact to a written summary below the knee, or hand a bounded sub-task to a sub-agent that returns a conclusion. [ch07]
**Trade-offs**: summaries lose detail; keep the original log for audit.

## Eval says 100%
**When**: every case passes after a prompt change.
**Move**: check whether the cases are too easy; add negative cases and the hardest real incidents; raise difficulty until some fail; keep a held-out set. [ch08]
**Trade-offs**: scores drop, which is the point.

## Agent is ready for real users
**When**: the demo works on a handful of cases.
**Move**: repeated runs with pass^k by category; traces with cost per completed task; shadow mode first; staged rollout with thresholds fixed in advance; kill switch and bounded retries. [ch08, ch07]
**Trade-offs**: a slower launch and fewer surprises.

## Session is expensive and getting worse
**When**: cost per task climbs, answers drift, the same constraints must be repeated.
**Move**: check the fixed prefix at session start; split work into one task per session; keep model and effort fixed; write a handoff file (goal, decisions and why, problems, files, open questions, next steps) and start fresh instead of letting automatic compaction choose; turn rarely used instructions into skills and switch off unused tool servers. [ch09, ch07]
**Trade-offs**: more discipline per task; the handoff file takes minutes and keeps what you chose to keep.

## Two agents on one change
**When**: a plan or a diff matters and one model wrote it.
**Move**: let a second model or tool review adversarially (specific objective, such as the plan); the first answers; repeat until no objections; read the critiques yourself; implement; security review; final cross-check. Split roles (plan, build, review), not difficulty. [ch09, ch03]
**Trade-offs**: two subscriptions or two runs; a different model family catches different errors.

## Unknown codebase, risky change
**When**: you are about to change code you do not fully know.
**Move**: in a separate working copy, run several read-only explorers; list known knowns, known unknowns, unknown knowns and unknown unknowns; check for committed secrets and duplicate deploy paths; interview the owner one question at a time; show design options with fake data; then implement. [ch09]
**Trade-offs**: an extra stage up front; hidden constraints surface before they cost a rewrite.

## Parallel work by several agents
**When**: backend and frontend, or independent modules, could proceed together.
**Move**: write the contract first (shapes, endpoints); give each agent its own working copy and file ownership; use sub-agents when they need not talk, teams only when they must share a task list; review before merge. [ch09, ch07]
**Trade-offs**: team token cost; sequential work does not benefit.

## Building an automation with a workflow tool
**When**: a recurring task (reply drafts, reports, lead handling) could run without you.
**Move**: write the trigger, steps and "done"; code for logic, dates and lookups, model for judgement; let an assistant draft the flow but review it as a skeleton; expose it to the assistant as one workflow per operation with a contract-style description; scope keys and actions narrowly; test plumbing, each step, edge cases, misuse and repeat runs; ship as drafts with an approval point. [ch10, ch07]
**Trade-offs**: slower than "it ran once"; avoids silent failures and unsafe effects.

## Test endpoint works, production does not
**When**: a flow passes in the editor but never fires from the real source.
**Move**: check it is saved, published or activated and flagged available to the protocol; use the production endpoint in production; confirm credentials and schedule; inspect run history. [ch10]
**Trade-offs**: five minutes; the most common cause.
