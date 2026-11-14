# Chapter 12: Error Handling and Failing Fast

## Core Idea
In this model the default stance towards unexpected errors is to **fail early, visibly and specifically**, and to handle an error only at a place that can do something useful about it. Error handling is a design decision about who is told what, not a layer of defensive blocks. Examples use exception-based languages; other styles are noted where the idea differs.

## 12.1 Fail fast
- **Thesis**: letting a program stop at the first sign of a broken assumption yields simpler code and more robust systems than trying to anticipate and absorb every failure.
- **Mechanism**: take a function that builds an invoice from a payment: the customer may be missing, the fee lookup may fail, a metadata key may be absent. Wrapping each risky line in its own handler, plus a catch-all "just in case", buries the main logic in nesting. Worse, the function cannot recover anyway: without the fee or the customer record there is no invoice to produce. Printing and carrying on hides the failure from whoever called the function (a request handler, a job), which then proceeds as if it had succeeded.
- **Trade-off**: crashes are visible; that is the point, but it must be paired with monitoring and a sensible top-level handler.
- **Does not hold when**: failure has serious consequences or the system is real-time and cannot stop; handle explicitly there. In a distributed setting a failing dependency needs resilience patterns such as a circuit breaker (`software-architecture`).

## 12.2 Rules that make it work
1. **No bare catch-all** handlers inside the code. They swallow errors callers must know about and hide programmer mistakes (typos, missing names). The acceptable place is the **top level**: for example a server that must always answer, returning a generic server error while logging details.
2. **Context managers or equivalent** (scoped resources) for files, connections and locks, so cleanup happens when an error occurs.
3. **A package-level exception hierarchy**: one base error class for a library and specific subclasses, so users can catch everything from the library in one place and trust that what they catch is from it.
4. **Log errors**, but never secrets or personal data (passwords, keys, personal details).
5. **Check early**: validate inputs at the top of a function or at construction (see ch10.3) so failures point to the cause.

## 12.3 Custom exceptions
- **Thesis**: built-in error types (a generic value error) are cryptic to an end user; a domain-named exception is clearer and can carry data.
- **Mechanism**: subclass the base exception (or a fitting built-in), add fields (the limit that was exceeded, the current value, the offending weight), and handlers can read them rather than parsing a message. Initialise the parent class properly: setting the message directly is shorter and reads well but can leave the parent partly initialised and cause surprises (position: do it properly). Know the four clauses of the typical construct: the guarded block, the handler for a failure, the "no failure" branch and the "always run" branch.
- **Trade-off**: more types to maintain; keep the hierarchy small.
- **Does not hold when**: a built-in type is exactly right and nobody will handle it separately.

## 12.4 Specific failure beats accidental failure
A failing division on an empty collection reports a generic arithmetic error. Checking the precondition and raising a specific error ("the list is empty") costs one line and tells the next developer why. In this model this is the same fail-fast move: check early, say what is wrong, stop.

## 12.5 Raise or return nothing?
- **Thesis (position)**: in doubt, raise; do not return a null value that the caller must remember to test.
- **Mechanism**: a lookup **by identifier** expects the object to exist, so absence is a bug worth knowing about: raise a not-found error. A lookup by a key that may legitimately miss (an email address) can return "no value", but even then the stricter stance is to raise. A query returning **many** items returns an **empty list**, never null. Optional parameters (10.4) follow the same logic: use them only when absence has meaning.
- **Alternatives**: monadic or result types (common in some languages) make absence or failure explicit in the type; in languages where they are not standard they can confuse teammates (position).
- **Trade-off**: exceptions as control flow can hide the happy path; result types add ceremony.
- **Does not hold when**: absence is an ordinary outcome in the domain (a search that often finds nothing); then returning "no value" is the honest answer.

## 12.6 Check list
Does this function know how to recover? If not, do not catch. Is the error type specific enough to act on? Does the message say what was wrong and with which values (not secrets)? Is there exactly one place that turns errors into a response? Are resources released on failure?

## Cross-references
Chapter 10 (value objects and validation at construction), 04 (tests that depend on error paths), 07 (mindset for edge cases). `software-architecture` for resilience, retries and circuit breakers; `coding-with-agents` when generated code adds defensive handlers everywhere.
