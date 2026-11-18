---
name: computer-science-fundamentals
description: "Computer-science fundamentals as reasoning tools: Turing and counter machines, undecidability, incompleteness, busy beaver, P vs NP, Big-O; binary search, quicksort, Dijkstra, A*, Monte Carlo tree search, annealing and other algorithms; arrays vs linked lists, B-trees, Bloom filters, Huffman and Reed-Solomon codes; CPU caches, DRAM, page tables, TLB; mutexes, races, deadlock; garbage collection, compiler division trick, OS concepts; TCP slow start and AIMD, Ethernet line coding, DNS; RSA, square-and-multiply, AES, hashes; protocol flaws, double ratchet, blockchain, sessions vs tokens; REST, GraphQL, design patterns; ports and HTTP, password and passkey threat models, beginner programming mental models. Use when the user asks how a machine, algorithm, protocol or cipher works, why code is slow, what cannot be computed, or which structure or algorithm fits a workload. Separates facts from positions and says when each rule stops applying."
allowed-tools:
  - Read
  - Grep
argument-hint: [concept, problem, or chapter number]
---

# Computer Science Fundamentals
**Chapters**: 12 | **Corpus**: ~37 theoretical transcripts | **Generated**: 2026-11-14

## Role and Boundaries

This skill **explains the mechanism behind computing and tells you when a rule stops applying**: what a model of computation can and cannot do, what an algorithm costs on real hardware, how memory, processes and networks work, how cryptographic tools and protocols fit and fail. It gives mechanisms, trade-offs and exit conditions; the user owns the choice of design.

| This skill decides | This skill hands off |
|---|---|
| Limits of computation, complexity class, which algorithm or structure fits an access pattern | Distributed system design, consistency, caching and TLS in production, incidents → `software-architecture` |
| Why a program is slow at CPU, cache, page, lock or kernel level | Neural networks, optimisation as learning, transformers, diffusion → `ai-ml-concepts` |
| How a protocol, cipher or key exchange works and where it breaks | Writing, reviewing and testing code with agents → `coding-with-agents` |
| What a pattern or paradigm buys and costs | Tests, refactoring, review practice → `software-engineering-practice`; interface and flows → `ux-ui-expert` |

**Stay in lane.** Numbers in the chapters are dated snapshots (cycle counts, cache sizes, key sizes, protocol flavours change); re-check before relying on them. Items that could not be confirmed are marked "(unverified)"; background knowledge is marked "general knowledge". This is theory for reasoning, not security advice: do not implement cryptography from the toy examples.

## Facts vs Positions

- **Mechanism / fact**: how a cache set is chosen, how AIMD behaves, why RSA decrypts, what a mark phase does.
- **Position**: written "(position)" or "In this model...": for example "nothing computes more than a Turing machine", "most believe P is not NP", "the book of patterns is criticised", "tokens vs sessions storage choices".
- Every concept in the chapters has four fields: **Thesis**, **Mechanism**, **Trade-off**, **Does not hold when**. Read the last one before recommending.

## How to Use This Skill

Diagnose before prescribing: ask the size of the input, the access pattern, what dominates the cost, the hardware and language, the threat model (for security), and what has been measured.

| Task | Start with | Then |
|---|---|---|
| "Can this be computed / decided at all?", halting, NP-hard | [ch01](chapters/ch01-models-of-computation-and-limits.md) | ch11 |
| Pick a search, sort, path or planning algorithm | [ch02](chapters/ch02-algorithms-search-sort-and-paths.md) | ch03, ch04 |
| Array vs list, tree, hash, Bloom filter, compression, error correction | [ch03](chapters/ch03-data-structures-and-compact-representation.md) | ch04 |
| Slow loops, cache misses, page faults, TLB, why layout matters | [ch04](chapters/ch04-cpu-caches-and-memory.md) | ch03, ch06 |
| Race, lock, deadlock, livelock, retry storms | [ch05](chapters/ch05-concurrency-and-shared-state.md) | ch06 |
| Memory leaks, garbage collection, compiler tricks, OS internals | [ch06](chapters/ch06-runtimes-compilers-and-operating-systems.md) | ch04, ch05 |
| TCP speed, congestion, Ethernet signalling, DNS, addresses, ports, the path of a web request | [ch07](chapters/ch07-networks-and-transport.md) | ch09 |
| RSA, AES, hashes, signatures, fast exponentiation, side channels | [ch08](chapters/ch08-cryptographic-building-blocks.md) | ch09 |
| Protocol attacks, secure messaging, ledgers, sessions vs tokens, passwords and passkeys, age-check schemes, media authenticity | [ch09](chapters/ch09-protocols-trust-and-secure-messaging.md) | ch08 |
| REST, GraphQL, design patterns, paradigms | [ch10](chapters/ch10-interfaces-patterns-and-application-layer.md) | ch11 |
| Teach or learn programming basics (variables, loops, lists, references, classes, APIs) | [ch12](chapters/ch12-learning-to-program-mental-models.md) | ch03, ch06 |
| "How should I think about this?" | [ch11](chapters/ch11-reasoning-in-computer-science.md) | the matching chapter |
| Quick lookup | [cheatsheet.md](cheatsheet.md), [patterns.md](patterns.md), [glossary.md](glossary.md) | |

## The Core Principles (recurrence order)

1. **Place the problem on the ladder**: undecidable, intractable, polynomial, linear; settle for heuristics knowingly.
2. **Find the dominant operation** and its machine cost; memory access usually beats arithmetic.
3. **Measure**: the same code behaves differently across processors, compilers and workloads.
4. **Layout follows access**: contiguous, sequential data wins on cached machines; random pointers do not.
5. **Amortise**: sort once, precompute, specialise at compile time, reuse connections and translations.
6. **Every cache costs staleness and policy**; add one deliberately.
7. **Make the dangerous step indivisible, order the locks, make repeats harmless.**
8. **Abstractions lie usefully**: descend a layer when behaviour surprises.
9. **Easy to verify, hard to find** is the engine of cryptography and a design resource.
10. **Secure parts do not make a secure protocol**: bind identities and runs, assume combinations.
11. **Probe, then back off hard**: growth by small steps and cuts by half is how shared resources stay stable.
12. **Explore early, exploit later**, and keep some exploration.

## Chapter Index

1. [Models of computation and their limits](chapters/ch01-models-of-computation-and-limits.md)
2. [Algorithms for searching, sorting, paths and decisions](chapters/ch02-algorithms-search-sort-and-paths.md)
3. [Data structures, representation and compact coding](chapters/ch03-data-structures-and-compact-representation.md)
4. [CPU, caches and memory](chapters/ch04-cpu-caches-and-memory.md)
5. [Concurrency and shared state](chapters/ch05-concurrency-and-shared-state.md)
6. [Runtimes, compilers and operating systems](chapters/ch06-runtimes-compilers-and-operating-systems.md)
7. [Networks, transport and naming](chapters/ch07-networks-and-transport.md)
8. [Cryptographic building blocks](chapters/ch08-cryptographic-building-blocks.md)
9. [Protocols, trust and secure messaging](chapters/ch09-protocols-trust-and-secure-messaging.md)
10. [Interfaces, design patterns and programming paradigms](chapters/ch10-interfaces-patterns-and-application-layer.md)
11. [How to reason in computer science](chapters/ch11-reasoning-in-computer-science.md)
12. [Learning to program: mental models that make code predictable](chapters/ch12-learning-to-program-mental-models.md)

## Topic Index

- **A*, heuristics, admissible estimate** → ch02
- **IPv4, address translation, ports, TCP vs UDP, HTTP request path** → ch07 (7.8)
- **Credential stuffing, offline cracking, passkeys** → ch09 (9.8)
- **Age verification, double anonymity, attribute tokens** → ch09 (9.9)
- **Content provenance, watermarks, deepfake detectors** → ch09 (9.10)
- **Off-by-one, loops, lists vs dictionaries vs sets, shared references, input casting** → ch12
- **AES, S-box, rounds, finite field** → ch08
- **Array vs linked list, locality** → ch03, ch04
- **AIMD, slow start, congestion window** → ch07
- **Base case, call stack, recursion** → ch02, ch06
- **Binary search, sorted-once-searched-often** → ch02
- **Bloom filter, cuckoo hashing, B-tree, radix tree, rope** → ch03
- **Busy beaver, Ackermann growth** → ch01
- **Cache lines, sets, ways, prefetch, inclusive caches** → ch04
- **Counter machine, Turing machine** → ch01
- **DNS records and resolution** → ch07
- **Deadlock, livelock, lock ordering, dining philosophers** → ch05
- **Design patterns (singleton, prototype, builder, factory, facade, proxy, iterator, observer, mediator, state)** → ch10
- **Dijkstra, shortest path, routing** → ch02, ch07
- **Division by a constant (compiler trick)** → ch06
- **Double ratchet, forward secrecy** → ch09
- **Ethernet encoding (Manchester, 8b/10b, scrambling)** → ch07
- **Garbage collection (reference counting, mark and sweep)** → ch06
- **Incompleteness theorems, diagonalisation** → ch01
- **GraphQL, REST, status codes, statelessness** → ch10
- **Huffman code, entropy, efficiency** → ch03
- **Man in the middle, nonce protocol flaw** → ch09
- **Mutex, atomic exchange, memory ordering** → ch05
- **Monte Carlo tree search, UCT** → ch02
- **NP-complete, P vs NP** → ch01
- **Operating system boot, syscalls, scheduler, inodes, pipes** → ch06
- **Page table, TLB, huge pages** → ch04
- **Proof of work, blockchain** → ch09
- **Reed-Solomon, Hamming, parity** → ch03
- **RSA, signatures, hashes** → ch08
- **Sessions vs tokens** → ch09
- **Square and multiply, side channels** → ch08
- **System on a chip, native vs translated** → ch04
