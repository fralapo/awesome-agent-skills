# Chapter 04: Software Quality — Complexity, Simplicity, Dependencies and Product

## Core Idea
Cheap code does not make complexity free. Code rarely dies of technical debt; it dies of **compounding design errors and unnecessary complexity**. The most productive engineers get leverage from **design sacrifice**: deciding not to build features that add 10-20% of value for ~80% of the effort. Agents make building cheap, so the discipline of *not* building matters more.

## 1. Debt vs Systemic Complexity
| | Technical debt | Systemic complexity |
|---|---|---|
| What | A conscious, local simplification | An unrecognised design error patched by more complexity |
| Example | A linear loop where a log-time search exists, justified by "never more than 10,000 items" | A wrong abstraction fixed by layers, then documented as "the user must configure it this way" |
| Repair | Rewrite that part later | Rebuild the foundation |
| Analogy | A wooden stair, cheap furniture | A wrong floor plan |

Rules:
- Do not label every simple solution "debt"; be more suspicious of people who complicate than of people who simplify.
- Design errors compound (each is patched by a worse patch), so design quality dominates even when an LLM writes the code. What changes is that someone must be able to **recognise design flaws in generated output**.
- Distinguish deliberate design sacrifice (consciously not handling something, documented) from error.
- Simplify the *idea* and stay rigorous in the *implementation*; the two are orthogonal. A plain `goto` or global state is fine when it is the simplest correct solution.

## 2. Reducing Complexity (technical)
- Complexity grows roughly **quadratically with tangled dependencies** and much closer to n log n with **opaque, narrow interfaces**; in practice between. Isolate risky modules behind small interfaces.
- Decompose into fundamental pieces, then layer functions as abstractions; abstract a fiddly computation (wrap-around indexing) once, and extensions become trivial.
- Avoid undefined or implementation-dependent behaviour; prefer portable, simple formulations.
- Measure resource usage, not features shipped. One position: make efficiency count in promotion; fewer features and more refactoring beat speed.
- Ask the agent for **minimal lines and few dependencies**; give an existing compact codebase as the style reference. Fewer lines is usually better; do not measure AI by code produced.
- Know what **not** to build. State the non-goals in the spec.

## 3. Indirection (technical)
Each reference or pointer costs memory and time: 8 bytes on 64-bit plus padding, and each hop risks a cache miss. A linked list of 4-byte integers can cost 8-24 bytes per element.
- Group elements into nodes holding N elements (16 or 32) to move indirection from per-element to per-group; too-large nodes over-allocate and slow small inserts.
- Sparse arrays: a directory of fixed-size slices (for example 4096 elements) allocated on demand; promote to a sparse upper level only above a size threshold so a pathological index cannot blow up memory.
- Tagged pointers: low bits freed by alignment store small integers or short strings inline, avoiding a heap object.
- Pick the representation by size and switch (promote) only when needed.
- Space and time reductions often coincide (fewer hops, fewer cache misses); complexity is sometimes worth paying for 20-30%.
- Agents tend to be conservative: give them the structural idea they will not find alone (specialised tables, grouped buckets, tag-based lookup) and let them implement it.

## 4. Dependencies
Large transitive trees mean frequent, mostly useless updates, breakage chains, attack surface and abused semantic versioning.
- Ask the agent to **implement rather than import** for small, stable problems (terminal size has needed the same few lines for decades; a small event loop can be hundreds of lines).
- **Vendor** a small, well-written library (copy it into the project) and check occasionally for fixed bugs.
- Use real libraries for genuinely hard domains: cryptographic protocols, complex graphics, codecs you cannot test exhaustively.
- Models add dependencies unless told not to; put "avoid unnecessary dependencies" in the instructions file.
- Resist review cultures that reward adding libraries; reward code that needs no change for years.
- Self-contained deliverables (own small decoders, built-in minimal server, quick builds) become affordable when agent bandwidth is abundant.

## 5. Rewrites
- Mature code embeds years of small lessons. A rewrite loses them and reintroduces bugs; comment bug fixes and security lessons so models keep the invariants.
- **Do not regenerate what a mature library already solves** (image decoders, parsers).
- Agents cut a rewrite from years to days, so the old "never rewrite" rule is revisable. One position: attachment to code drops when a model wrote it, which lowers sunk-cost resistance and improves team dynamics. Attach to the **design idea**, not the implementation.
- **Design space is not continuous**: good and bad designs of a large project are often separated by valleys, so small refactors cannot always morph one into the other.
- **Do not port 1:1 and plan to "refactor later" in the target idiom.** A literal port keeps the wrong shape (for example lots of escape-hatch blocks in a safe language). Either restructure deeply in the source first and then translate, or redesign during the port (harder for the agent, more iterations, higher failure risk).
- "Old tests pass" is not equivalence (ch03). Invest time up front to find the right design, then grow it organically.

## 6. Irreversible vs Reversible Decisions
Irreversible or expensive to reverse: language, framework, base architecture, production database schemas, public APIs. Either raise reversibility (abstraction at the boundary, migration path) or think ahead before choosing. When fragility grows, **stop feature work and refactor** even against schedule pressure; agent-assisted refactoring takes weeks instead of months. Quality gates from the start in domains where drift accumulates (numerical inference), otherwise kernels get rewritten.

## 7. Technology Choice
Choose on your own judgement, not fashion. When code is rarely read by humans, optimise for deployment simplicity, speed, succinctness and how well the model knows the stack. A simple stack (minimal backend, server-rendered HTML, JavaScript only where it matters) gives low latency and good accessibility for crawlers and AI agents. If a language or stack is semantically heavy or rare in training data, expect a handicap and consider switching. Prefer native over heavy cross-platform stacks when resource use and responsiveness matter (one position: abstraction stacks often create the memory and latency problems).

## 8. Product Quality Over Generalisation
- Ship a concrete product that is good for its users before generalising; generalise later or never. Users do not care about the implementation language.
- A platform needs a new space, a personal following or strong organisational backing; building one often postpones the question "who will actually use this?"
- Show something that impresses rather than something that "can do anything".
- **A product is the sum of countless design decisions**: UI, interaction, algorithms, trade-offs, supported formats. A prototype is not a product (months of curated iteration). Cloning a demo is cheap; cloning domain depth, trust, reliability and years of support is not.
- Differentiators: long domain experience, a personal vision, integration of AI into the interaction (precise selection and in-place direction of edits) rather than a generic chat, a fair pricing model (for example one-time purchase with updates included for one to three years and discounted upgrades). Pricing structure: `pricing-and-sales-negotiation`.
- **Invisible AI**: improve an existing feature (search, ranking, cleaning, prediction) so users feel it simply works; do not bolt a "talk to your data" chat onto an app. Pattern: conventional retrieval or statistics first, then an LLM pass to re-rank, validate and normalise candidates against explicit criteria in the prompt (consistency checks, data-error detection, unit and state conversions, intent matching). Direct controls and predictive suggestions beat natural-language entry for repetitive actions.
- Large-company product failures come from non-technical product ownership, siloed teams, legal risk aversion and committee design; good products often come from a few people who hold both technical depth and design sense. Avoid thousand-button feature piles; disclose rarer functions progressively; use context and timeouts, not fixed menus.
- A crowded market is not a reason to stop if incumbents are poor. Positions on markets are opinions.

## Common Mistakes
- "Cheap code, so more features." Complexity compounds regardless of who typed it.
- Calling a design error "debt" and layering a patch over it.
- Reaching for more infrastructure instead of fixing quality.
- Complicating specs to look sophisticated; fearing "too simple".
- Literal port plus "clean up later".
- Building a platform before one good product.

## Checklist
- [ ] Non-goals written? Which feature am I refusing and why?
- [ ] Can I name each dependency's reason? Could the agent write or vendor it?
- [ ] Is this debt (local, repayable) or a design error (spreading)?
- [ ] Which decisions here are irreversible?
- [ ] Is a rewrite port 1:1 or redesigned, and how is equivalence shown?
- [ ] Does the product feel better to its user, or only more general?

## Connects To
- ch02 (spec and constraints), ch03 (equivalence testing), ch06 (invisible AI integration).
- `ux-ui-expert` (progressive disclosure, hierarchy, usability); `pricing-and-sales-negotiation` (one-time vs subscription as an offer decision); `workshop-facilitation` (prioritising what not to build).
