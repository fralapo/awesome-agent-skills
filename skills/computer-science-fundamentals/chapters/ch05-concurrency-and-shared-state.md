# Chapter 5: Concurrency and Shared State

## Core Idea
When two activities can touch the same thing at the same time, correctness depends on timing, and tests rarely cover the bad timings. In this model the cure is to make the dangerous step indivisible, to take shared resources in a fixed order, and to prefer operations whose repetition does no harm. The hardware gives one tiny primitive; everything else is a discipline built on it.

## 5.1 Race conditions: check-then-act and read-modify-write
- **Thesis**: a race is a result that depends on the interleaving of steps from different activities; the classic form is "check a condition, then act on it" with a gap in between.
- **Mechanism**: a withdrawal routine that checks "balance is at least the amount", then pays out, then subtracts, can be run by two machines at once on a joint account: both pass the check, both pay out. Even the subtraction can go wrong: both read the same balance, both subtract, both write, so one update is lost (money apparently created or destroyed). The same shape appears in everyday life (two people each buying milk after seeing none; copying a rota while the manager changes it, so a person ends up with two shifts or none): a multi-step read of changing data gives an inconsistent snapshot.
- **Trade-off**: closing every gap costs waiting; in some cases the right answer is a design that does not need the check (see 5.5).
- **Does not hold when**: only one activity ever touches the data (single thread, or a data structure owned by one worker with messages sent to it).

## 5.2 The atomic exchange: the one hardware primitive that builds a lock
- **Thesis**: a lock cannot be built from plain reads and writes ("if not locked then lock" is itself a race), so the hardware offers an indivisible read-and-replace.
- **Mechanism**: an exchange instruction writes a new value into a memory cell and returns the old value in one step that no other core can split. A mutex is a cell holding 0 (free) or 1 (held). To lock, exchange in a 1: if the old value was 0 you now own it; if it was 1 someone else does and nothing changed, so try again. To unlock, write 0. The protected region between lock and unlock runs one activity at a time. This works across threads, processes and cores on one machine; across several computers it needs a distributed protocol, which is a different problem.
- **Trade-off**: spinning on the exchange burns a full core while waiting and hammers the memory system; operating systems therefore spin briefly, then put the waiter to sleep and wake it on unlock (a cost: a system call and a context switch). Spinning can still be right when waits are tiny and latency matters more than power.
- **Does not hold when**: the waits are long (then sleeping is better) or contention is heavy (see 5.6).

## 5.3 Memory ordering: the lock must also be a barrier
- **Thesis**: a compiler or CPU may reorder independent-looking instructions, so a lock must also stop loads and stores from moving across it.
- **Mechanism**: lock and unlock operations carry ordering guarantees (acquire and release semantics): reads inside the region must not be hoisted above the acquisition, writes must not sink below the release. Both the compiler and the processor must be told. Some processor families keep a strong order by default and forgive mistakes; others reorder aggressively and expose them.
- **Trade-off**: stronger ordering costs performance; weaker ordering is faster and harder to get right.
- **Does not hold when**: you use a language runtime or library lock; it already includes the correct barriers. Hand-written lock-free code is where this bites.

## 5.4 Deadlock, livelock and lock ordering
- **Thesis**: waiting on each other forever (deadlock) or reacting to each other forever without progress (livelock) are design faults, not bad luck; they are prevented by discipline.
- **Mechanism**: with a lock per account, a transfer needs both locks. If one transfer takes A then B while another takes B then A, each holds one and waits for the other. Fixed order solves it: always take locks in increasing order of a key (the account number), whatever the direction of the transfer. Other deadlock shapes: roundabout or crossroads where each party waits for the one on its right; the dining philosophers, each holding one utensil and waiting for the second; a car-park gridlock. Livelock: two parties who both back off by the same amount and retry in step, forever; even doubling the delay does not help if clocks are synchronised, and a deterministic "random" number can repeat. Fixes: break symmetry (one party picks up the other utensil first, or add real randomness drawn from the environment), set timeouts and roll back (databases do), or impose a global order.
- **Trade-off**: ordering rules constrain code structure; timeouts and retries add complexity and can mask bugs.
- **Does not hold when**: only one lock is ever held at a time, which is the simplest safe design.

## 5.5 Idempotence and splitting the action
- **Thesis**: making an operation safe to repeat removes a whole class of races without any lock.
- **Mechanism**: a single toggle button that both starts and stops a machine races with the machine's own automatic stop: pressing it at the wrong instant restarts it. Separate "start" and "stop" buttons make stop idempotent: stopping twice equals stopping once. The same idea underlies retry-safe network requests (see `software-architecture` ch20 for idempotency keys).
- **Trade-off**: not every action can be made idempotent (a payout is not); then it needs a lock, a transaction or a reservation.
- **Does not hold when**: the operation is inherently additive (counters, money movement).

## 5.6 When one lock is too coarse
- **Thesis**: a mutex serialises everyone who wants the same thing, so throughput stops growing with the number of cores.
- **Mechanism**: finer-grained locks (one per account instead of one per bank), reader-writer locks, partitioning data so each worker owns a slice, and other hardware primitives (atomic add, compare-and-swap) that update a single value without a lock. In this model a communal bathroom (many readers at once) is the analogy for relaxing exclusion when use is read-only.
- **Trade-off**: each refinement trades simplicity for scalability and adds ordering and deadlock risk.
- **Does not hold when**: the lock is rarely contended; the simple mutex is then fast enough and the refinement is cost without benefit.

See also: ch06 (operating-system view of threads and scheduling), `software-architecture` ch14 (locks, deadlocks and optimistic versus pessimistic control in databases).
