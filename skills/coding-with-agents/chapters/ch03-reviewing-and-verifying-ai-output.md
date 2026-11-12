# Chapter 03: Reviewing and Verifying AI Output

## Core Idea
With strong models, **local errors** (a single function) are rarer than **architectural errors** (the wrong split, the wrong shared state, the wrong data model). Reading everything does not scale: generation is faster than reading, and reviewing is harder than writing because you must rebuild the author's mental state. So shift effort from *reading code* to *checking ideas, behaviour and states*. Where code is core or security-sensitive, read it anyway (ch01 decision rule).

Facts vs positions: the techniques below (differential testing, fuzzing, sanitizers, invariants) are established practice. "Do not read generated code", "no TDD" and "few unit tests" are **positions** held by experienced practitioners; weigh them against team context.

## 1. Checking Ideas Instead of Reading Code
1. **Before a big implementation**, spend a few minutes writing the critical design constraints (example: "split the weights 50/50 across devices, do not duplicate them").
2. **After**, ask the model how it implemented specific parts. Read a short page of explanation and ask targeted follow-ups.
3. **QA** manually and with the model, in varied conditions and scale.
4. If you fear a design flaw, **discuss it with the model** instead of patching style. Stylistic edits after reading give only an illusion of impact.
5. Use freed time for validating ideas, inventing, and deciding what the software should do.
6. Second reviewer: have a **model from another vendor** review, and ask for targeted tests where unconvinced.

## 2. What "Tests Pass" Does and Does Not Prove
- Passing the old suite does **not** prove a rewrite is equivalent. Suites have holes; that is why QA teams exist.
- **Line coverage is a weak signal.** 100% line coverage means every line ran, not every state; it does not mean zero bugs. It is still useful in an agent workflow: every uncovered line is a consequence of the change, so the report becomes a to-do list.
- The true target is **state coverage**, especially fragile and boundary states.
- Unit tests alone are insufficient; add integration tests that exercise the system like a user.

## 3. Test Techniques That Find Real Bugs
**Position (deliberate alternative to mainstream):** write tests *after* the implementation, because writing the code shows where it is fragile; test through the public/high-level API so tests survive refactors; avoid tests of internal functions (they break at every interface change). Exception: standalone data-structure libraries, stressed through their exported API. Test code is disposable accessory code; do not be stingy writing it.

### 3.1 Random differential testing
Run the same operations on the real implementation and on a trivially correct (slow) one inside the test, then compare. Examples: a hash table in the test as reference for a custom store; a linear scan as reference for an approximate nearest-neighbour index (assert recall stays above a threshold).
- Use scale: millions of items, heavy destructive operations (delete 95% then check structural quality), save and reload, replication.
- Read back without storing in a helper structure when you can derive the expected value from the key.

### 3.2 Invariant checks
Assert properties that must always hold: every link is reciprocal, minimum connectivity per node, output within range, checksum matches, sorted order preserved.

### 3.3 Shape the random generator
Uniform random bytes exercise few states. Bias towards fragile cases:
- compressor: compressible strings of varied length;
- parser: partly valid, partly corrupted input; bit and byte flips; crossover of two valid documents;
- codec: realistic images with transformations, compared with a tolerance metric, not exact bytes;
- boundaries known from the implementation: if a limit is 256, test 255, 256, 257.

### 3.4 Reproducibility
Print the RNG seed at the start of every randomised test so a failure can be replayed (threaded tests may remain non-deterministic). On assertion failure dump as much state as possible.

### 3.5 Runtime checkers and speed
Run under address/memory sanitizers or a leak detector; keep the suite fast enough to run constantly. Good tests make code **malleable**: you change the design with confidence instead of treating it as a crystal vase. This matters more with agents, because tests are rails that let them reject their own breakage.

### 3.6 Targeted tests still have a place
Expression engines (each operator, division by zero), auth rules, and anything with a small finite input space.

## 4. Prompt the Agent for Good Tests
Agents rarely produce these test styles by default. One sentence changes output a lot:
- "Stress boundary conditions of each limit (N-1, N, N+1)."
- "Add a randomised test against a simple reference implementation inside the test; print the seed."
- "Add invariant checks after every mutation."
- "Do not over-emphasise testability in the design" (over-stating one property can degrade performance-critical structure).
- For numerical or model code: build tooling that **compares intermediate outputs (tensors, stages) with a reference implementation**. Neural pipelines tolerate small errors, so "looks fine" is not a test (for example a wrong scheduler in a few-step image model still produces plausible images).

## 5. Agentic QA (emerging practice)
A markdown test-plan file tells an agent to act as a QA engineer or user:
1. Invent use cases and write stress programs.
2. Scale gradually (10, 100k, 1M, 10M, 50M entries).
3. Add replication, save and reload, broken connections.
4. A **second agent verifies each reported bug is real** before a human is notified.
5. Run after significant changes or continuously; both agent and system vary per run, so new states are explored.

It complements, not replaces, the deterministic suite. Agents can also build test infrastructure that was too costly before (for example a terminal emulator inside the harness to assert on screen content).

## 6. Using the Model as Reviewer
- Use models as **bug finders** on delicate code, security code and your own diffs (memory corruption, double free, buffer overflow, wrong initialisation). A model caught a wrongly initialised field that would have broken filtering.
- **Backtest** to calibrate trust: does it find known bugs in earlier commits?
- A model finding a bug that an expert review missed is real added value, even if its patch is imperfect.
- For code you did not read, check for the failure modes of section 7.

## 7. Failure Modes to Look For in Generated Code
- Unrequested **dependencies**; ask to avoid them (ch04).
- **Verbosity and layering**; duplicated logic (for example two string-skipping routines), unnecessary state, missing cases.
- A candidate that allocates where it claimed not to, or does not truly skip work: check claims against measurements.
- **Plausible but wrong** numerical or semantic results.
- Silent "fixes" that make a test pass (special-casing, loosened assertion).
- Rewrites in a stricter language that become more verbose and layered; being stuck in a poor structure needs another rewrite.
- Auth, session and input-handling code: use the checklist in ch06.

## 8. Agent-Friendly Codebase Practices (reported by one team)
Descriptive greppable file names and namespaces (the file system is the agent's navigation interface); many small files; strong typing and generated typed API clients (remove degrees of freedom); cheap, fast checks (lint, type-check, tests) run constantly; fully automated, ephemeral parallel dev environments; end-to-end tests of user-level behaviour. Principle: **solid constraints matter more than prompts**; with firm limits the agent bounces until the only way out is correct. The file-count advice is only partly endorsed.

## Common Mistakes
- "Looks good to me" on complex code (rubber stamp).
- Fixed-data tests that exercise few states; trivial insert/remove tests that test nothing.
- Treating 100% line coverage as safety.
- Trusting a long unattended loop; trusting the faster tool because it feels safer.
- Accepting tiny risks without knowing them. Acceptable only when impact is negligible and understood (for example a rare hash collision skipping one display line).

## Checklist
- [ ] Critical design constraints written before implementation?
- [ ] Do I understand how the risky parts were implemented (explanation, not full reading)?
- [ ] Differential or invariant tests with a printed seed?
- [ ] Boundaries (N-1, N, N+1) and scale covered?
- [ ] A different model reviewed it?
- [ ] For numeric code: compared with a reference?

## Connects To
- ch02 (observability and baselines), ch04 (rewrites need equivalence, not just green tests), ch06 (security checklist).
- `ux-ui-expert` for usability testing of what the code does; `workshop-facilitation` for running a bug-bash or acceptance session.
