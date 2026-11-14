# Patterns

Recurring situation -> move. Each entry: When / Move / Cost / Not when. Chapter in brackets.

## 1. Question may be undecidable or intractable
**When**: "check that any program does X" or an exact optimum over exponentially many cases.
**Move**: restrict the input class, accept approximation or a timeout, report "unknown" explicitly. [ch1, ch11]
**Cost**: completeness or optimality.
**Not when**: instances are small.

## 2. Many lookups over data that rarely changes
**When**: the same collection is searched repeatedly.
**Move**: sort once and use binary search, or build a hash set; never use a generic membership test on an unsorted list in a loop. [ch2]
**Cost**: sorting time, memory.
**Not when**: one lookup, or data changes constantly.

## 3. Scanning a collection is slow although the code looks linear
**When**: a list of nodes is traversed repeatedly.
**Move**: use contiguous storage (an array), sequential access, small elements; measure on the target machine. [ch3, ch4]
**Cost**: costlier insertion in the middle.
**Not when**: the working set fits in the first cache level.

## 4. Cheapest route with a known goal direction
**When**: shortest path on a map or grid.
**Move**: use A* with a never-overestimating estimate instead of flood-fill Dijkstra. [ch2]
**Cost**: two values per node; estimate quality.
**Not when**: no estimate exists.

## 5. Decision without a model, little time
**When**: a robot or agent must act under uncertainty.
**Move**: sample simulated futures and grow a tree (Monte Carlo tree search), plan briefly, act, replan. [ch2]
**Cost**: biased early estimates; rare events missed.
**Not when**: the model is small and exact.

## 6. Shortlist membership cheaply
**When**: most queries are for absent items and the store is slow.
**Move**: put a Bloom filter in front; consult the store only on "maybe". [ch3]
**Cost**: false positives.
**Not when**: a false positive is unacceptable with no second check.

## 7. Check-then-act on shared data
**When**: two actors withdraw, reserve or update after reading.
**Move**: hold a lock around check and act (atomic exchange based), or restructure to a single atomic operation. [ch5]
**Cost**: waiting.
**Not when**: single owner.

## 8. Two locks needed
**When**: a transfer touches two accounts.
**Move**: always acquire in increasing key order. [ch5]
**Cost**: ordering discipline.
**Not when**: only one lock is ever held.

## 9. Two identical parties keep colliding
**When**: both back off by the same time and retry.
**Move**: randomise with real entropy or impose an order (one picks up the other utensil first). [ch5, ch11]
**Cost**: reproducibility.
**Not when**: a protocol dictates the order.

## 10. Memory grows in a language with collection
**When**: usage climbs although nothing seems allocated.
**Move**: find the root that still references the data (cache, listener, list); in reference-counted systems look for cycles. [ch6]
**Cost**: investigation time.
**Not when**: the growth is the live data.

## 11. A division by a constant in a hot loop
**When**: dividing by a known number.
**Move**: let the compiler convert to multiply and shift; do not hand-roll unless proven necessary. [ch6]
**Cost**: unreadable machine code.
**Not when**: the divisor is a run-time value.

## 12. Fresh connections are slow
**When**: many short transfers.
**Move**: reuse connections and keep windows open instead of paying slow start each time. [ch7]
**Cost**: held state.
**Not when**: transfers are rare.

## 13. Fast exponentiation with a secret exponent
**When**: private-key operations.
**Move**: square and multiply with reduction at every step, in a constant-time form. [ch8]
**Cost**: speed.
**Not when**: the exponent is public.

## 14. Protocol seems right
**When**: design or review of an authentication exchange.
**Move**: include both identities and the role in every message, test the role-swap and relay cases, prefer a vetted protocol. [ch9]
**Cost**: bytes, analysis effort.
**Not when**: closed trusted setting.

## 15. Messaging with offline parties
**When**: asynchronous end-to-end encryption.
**Move**: initial key agreement through pre-published keys, a one-way key chain per message and periodic fresh Diffie-Hellman values, delete each key after use. [ch9]
**Cost**: state, stored skipped keys.
**Not when**: endpoint compromise is the threat.

## 16. Login state on a scaled-out service
**When**: choosing sessions or tokens.
**Move**: sessions if revocation matters and a shared store is fine; signed tokens if lookups are the bottleneck, with short lifetimes. [ch9]
**Cost**: revocation difficulty (tokens) or store lookups (sessions).
**Not when**: single server.

## 17. Too many options or round trips in an API
**When**: constructors or endpoints with too many parameters, or too many round trips.
**Move**: builder or options object; graph-style query; keep resource-shaped REST where it fits. [ch10]
**Cost**: server complexity.
**Not when**: few fixed shapes.

## 18. Conditional logic keyed on state
**When**: a long switch on a status.
**Move**: one object per state with the same interface, or an explicit state machine. [ch10]
**Cost**: more classes.
**Not when**: two states.

## 19. Unsure which of two designs is faster
**When**: array vs list, loop style, library choice.
**Move**: write a small benchmark on the real machine and data; check the compiler did not remove the work. [ch11]
**Cost**: time.
**Not when**: the gap is orders of magnitude.
