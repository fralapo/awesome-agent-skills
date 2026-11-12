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
