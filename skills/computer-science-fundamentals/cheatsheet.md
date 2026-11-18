# Computer Science Fundamentals: Cheatsheet

Figures are rules of thumb and dated snapshots; re-test. "Position" = judgment, not fact. Chapter references in brackets.

## Where to Start
| Situation | First move |
|---|---|
| Is it computable? | Check halting-style reductions; undecidable means restrict the input [ch1] |
| Exact answer exponential | Heuristic, approximation, annealing, time limit [ch1, ch2] |
| Many lookups on static data | Sort once, binary search or hash [ch2] |
| Program slow, CPU idle | Look at cache misses, page faults, system calls, lock waits [ch4, ch5, ch6] |
| Shared data, intermittent bug | Find the check-then-act gap; make it indivisible [ch5] |
| Memory grows | Leak by missing free, cycle in reference counts, or one forgotten root [ch6] |
| Transfer slow on a fresh connection | Slow start; reuse connections [ch7] |
| Secure a protocol | Bind identities and runs; use a vetted protocol [ch9] |

## Complexity and Algorithms
| Item | Cost / rule | Use when | Not when |
|---|---|---|---|
| Linear scan | n | one lookup, unsorted | many lookups |
| Binary search | log2 n (about 23 steps for ten million) | sorted, random access, many lookups | unsorted, list structure |
| Quicksort | recursion on smaller side; base case empty list | general sorting (average n log n, general knowledge) | bad pivot, tight memory |
| Dijkstra | cheapest unfinished node first | non-negative costs | negative edges, huge graph |
| A* | order by cost so far + estimate | estimate never overestimates | no estimate |
| Monte Carlo tree search | select, expand, simulate, back up | no model, limited time | small known model |
| Annealing | accept worse moves, cool down | rugged landscape | single smooth peak |
| Dynamic programming | store sub-results | overlapping sub-problems | none overlap |

## Complexity Classes
| Class | Meaning | Example |
|---|---|---|
| P | solvable in polynomial time | sorting |
| NP | checkable in polynomial time | satisfiability, travelling salesman (14! = about 87 billion routes for 15 cities) |
| NP-complete | any one solved solves all | satisfiability |
| Undecidable | no algorithm | halting |
| Busy beaver | grows faster than any computable function | machines of n cards: (4(n+1))^(2n) |

## Memory and CPU
| Level | Rough figure as stated | Note |
|---|---|---|
| Add / logic | about 1 cycle | a third of a nanosecond at a few GHz |
| Integer multiply | about 5 cycles | |
| Integer divide | about 30 to 100 cycles | compilers avoid it for constants |
| L1 cache | a few cycles, tens of KB | lines of 64 or 128 bytes |
| L2 / L3 | about 1 MB / 10 to 15 MB | L3 shared |
| Page | 4 KB (2 MB huge) | four or five table levels |
| DRAM refresh | tens of milliseconds | leaks charge, row hammer |

## Concurrency
| Choice | Gain | Cost | Use when |
|---|---|---|---|
| Spinning mutex (atomic exchange) | lowest latency | burns a core | very short waits |
| Sleeping mutex | frees the core | system call, switch | longer waits |
| Fixed lock order | no deadlock | design constraint | several locks |
| Idempotent action | safe repeats | not always possible | stop, set, upsert |
| Random backoff | breaks symmetry | non-reproducible | retry loops |

## Network
| Item | Rule |
|---|---|
| Slow start | window doubles each round (initial window typically about 10 segments) until first loss or ssthresh |
| AIMD | +1 per round, halve on loss |
| Loss signals | three duplicate acks (mild), timeout (severe) |
| Line coding overhead | Manchester 100 per cent; 8b/10b 25 per cent; 64b/66b about 3 per cent |
| DNS chain | cache, resolver, root, top-level domain, authoritative |
| Record types | A, CNAME, MX, TXT, NS, SOA |

## Crypto
| Tool | Gives | Note |
|---|---|---|
| RSA | encryption, signatures | modulus 2048 bits, exponent 65537, padding needed |
| Square and multiply | fast exponent | about bit-length squarings; timing leaks key bits |
| AES | symmetric block cipher | 128-bit block; 10, 12 or 14 rounds |
| Hash (256-bit) | digest, tamper detection | not reversible |
| Double ratchet | forward secrecy and self-healing | keys per message |
| Proof of work | agreement without authority | hard to find, easy to verify |
| Session vs token | state on server vs client | revocation vs scaling |

## Web, Passwords and Learning to Code (ch7.8, ch9.8-9.10, ch12)
| Item | Rule |
|---|---|
| 32-bit address | 2^32 hosts (about 4.3 billion): hence address translation and the 128-bit scheme |
| Status codes | 200 ok, 403 forbidden, 404 missing, 500 server fault; HTTP itself has no memory (cookie) |
| Password space | 10^8 for eight digits; 62^8 (about 2.2 x 10^14) for eight alphanumerics; reuse beats length |
| Credential stuffing | Leaked pair replayed elsewhere: unique password per site plus second factor |
| Passkey | Device keeps private key, site stores public key; bound to site, so no look-alike phishing |
| Age-check token | Signed "over threshold", issuer does not see site; metadata still leaks |
| Media authenticity | Signature proves signer, not truth; watermarks removable; detectors fail on unseen generators |
| Beginner errors | a == x or y; off-by-one from one-based counting; mutating a shared list; input is text |

## Patterns (one line each)
Singleton one instance; prototype clone; builder step-by-step; factory chooses type; facade simple front; proxy intercepts; iterator pulls; observer pushes; mediator hubs; state object per state [ch10].
