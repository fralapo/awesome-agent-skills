# Chapter 12: Operating System and the Cost of the Kernel

## Core Idea
Architecture rarely fails on the diagram; it fails on a hidden cost underneath an abstraction that was assumed to be free. In this model the operating system is the most common source of such costs: a memory read may be a table walk, a system call is a mode switch, a "tiny" critical section may stall behind a page fault. Know the order of magnitude of each hop before choosing processes versus threads, memory-mapped files, large shared buffers or chatty syscalls.

## 12.1 Latency orders of magnitude as an intuition tool
- **Thesis**: relative differences of orders of magnitude matter more than exact values; some numbers move with technology, others (distance between regions) are fixed by physics.
- **Mechanism**: register access and a clock cycle are sub-nanosecond; L1/L2 cache are single-digit nanoseconds; L3 and main memory sit in tens to hundreds of nanoseconds (main memory is hundreds of times slower than a register). A simple system call costs several hundred nanoseconds for the trap alone; a thread context switch costs at least a few microseconds, far more if the new thread's data is cold. A reverse proxy handling one request is tens of microseconds; an SSD page read is about a hundred microseconds and an SSD page write about ten times slower; an in-zone cloud round trip is a few hundred microseconds; a typical cache operation measured from the client is about a millisecond; a spinning-disk seek is several milliseconds; a cross-continent round trip is tens of milliseconds and an intercontinental one a few hundred; a TLS handshake is a few hundred milliseconds because it needs several round trips; a deliberately slow password hash is a few hundred milliseconds by design; copying 1 GB inside a region takes seconds.
- **Trade-off**: figures are dated snapshots; the habit (group costs by power of ten, notice which neighbour is 1000x apart) is what lasts.
- **Does not hold when**: you need a decision on real hardware; measure it.

## 12.2 Switching into kernel mode is a bounded but real cost
- **Thesis**: user code cannot touch kernel structures; every transition is a save-and-restore, so a cheap-looking call repeated a hundred thousand times is not cheap.
- **Mechanism**: the kernel is mapped into the top part of every process's address space but is invisible in user mode. A system call, a page fault or an interrupt flips the same process into kernel mode: registers are saved to the process control block, the instruction pointer is pointed at kernel code, kernel structures (memory-area list, page tables) are read and possibly updated, and the state is restored on return. It is the same process, not a separate kernel thread.
- **Trade-off**: one switch is microseconds; the sum is what hurts, hidden in loops (many tiny reads, per-row calls, per-request allocation).
- **Does not hold when**: calls are rare or already batched. Reduce the count (buffering, batching, bulk APIs), do not micro-tune a single call.

## 12.3 Virtual memory and multi-level page tables
- **Thesis**: a flat translation table from virtual to physical addresses is the fastest possible design (one addition and one read) but is impossibly large, so translation is organised as a sparse tree.
- **Mechanism**: with a 48-bit address a flat byte-level table is far beyond any memory, so memory is mapped in 4 KB pages (a 12-bit offset inside the page); a flat page-level table for one process would still be about half a terabyte. The bet is that processes are sparse: the remaining 36 bits are split into four 9-bit levels, each table has 512 eight-byte entries (exactly 4 KB), and a level is allocated only when something under it is first touched. Each entry has bits such as present, writable and no-execute. The CPU itself walks this tree; the kernel only fills it in. Writing one byte to a fresh process can allocate several table pages before the data page: the overhead is paid once per region, then amortised.
- **Trade-off**: lookup becomes several dependent memory reads (a page walk); memory overhead grows with scattered use.
- **Does not hold when**: a process truly touches all its memory (the saving disappears) or a design bypasses the general-purpose kernel entirely (unikernel-style systems drop virtual memory, at the price of generality).

## 12.4 The translation cache (TLB) and locality
- **Thesis**: a page walk is too slow to repeat, so the CPU caches recent page translations in a small, scarce cache; access locality decides whether it works.
- **Mechanism**: a hit makes translation free; a miss costs a page walk. Sequential and stack-like access reuses the same few pages; random heap access and a huge, scattered code base evict entries and cause misses. Entries belong to one address space: a switch between **processes** invalidates the cache (the kernel changes the root pointer of the page tables), while a switch between **threads of the same process** keeps it. Kernel pages are marked global and survive the flush.
- **Trade-off**: threads share translations and are cheaper to switch; processes isolate faults and memory.
- **Does not hold when**: the working set is tiny, or the platform tags entries per address space so a flush is not needed.

## 12.5 Page faults: lazy allocation, copy-on-write, swap, mapped files, permissions
- **Thesis**: by design everything starts "not present"; the CPU asks the kernel to fix it on first use. A page fault is a mechanism, not always an error.
- **Mechanism**: the main causes are: first access to a page (memory is allocated lazily); stack growth (the stack region is extended and a new page faulted in); copy-on-write after a fork (parent and child share pages read-only; the first write copies the page, so the worst case after a fork is writing to every shared page, and a child that only reads, for example a snapshot writer, pays almost nothing); swap-in of a page the kernel evicted; first touch of a memory-mapped file page; and a permission violation (executing from a no-execute page, which blocks injected-code attacks and otherwise ends in a crash).
- **Trade-off**: lazy allocation saves memory and start-up time but moves cost to the first touch, in kernel mode, often under a lock.
- **Does not hold when**: you can pre-fault and pin memory (huge allocations at start-up, pre-warmed buffers) and latency at first touch is unacceptable.

## 12.6 Process-per-connection versus threads: the hidden multiplier
- **Thesis**: a large memory region shared by many processes is not populated once; every process fills its own translation tables.
- **Mechanism**: a database that forks a process per connection and shares a big buffer pool means each process faults in its own page-table entries for the buffer region. With a thousand connections that is thousands of tables and a flood of misses and kernel entries, repeated for each process. Threads of one process share one table. Standard-size pages make it worse: a 4 KB page against an 8 KB database page means two faults to reach one database page; huge pages (2 MB) cut the number of entries by two orders of magnitude and the fault count with it.
- **Trade-off**: processes give isolation and crash containment; threads give cheaper switches and shared translations; huge pages need reservation and tuning.
- **Does not hold when**: the buffer is small, the connection count is low, or a connection pool in front caps the number of processes.

## 12.7 A critical section can be stretched by the scheduler (spin lock plus preemption)
- **Thesis**: a lock meant to be held for nanoseconds becomes a convoy if its holder is descheduled or stuck in a kernel path while others spin.
- **Mechanism**: short locks on shared memory are often spin locks with back-off (waiting costs CPU but avoids being descheduled). If the holder takes a page fault inside the critical section and the kernel is allowed to preempt kernel code, the holder can be moved off the CPU while holding the lock; every waiter keeps spinning for something that is not running. One real regression showed roughly a halving of throughput on a kernel release that changed the default from "do not preempt kernel code" to "lazily preempt it"; the workaround was configuration (huge pages, fewer faults), the structural fix is threads, and a kernel feature lets a critical section ask not to be preempted briefly.
- **Trade-off**: preemptible kernels improve fairness and latency for the rest of the machine at the cost of lock-holder stalls.
- **Does not hold when**: critical sections never fault or sleep, or locks are sleeping mutexes (waiters sleep instead of burning CPU).

## 12.8 Upgrading the platform is a change to your system
- **Thesis**: a kernel, runtime or default change can alter the performance of unchanged application code.
- **Mechanism**: the regression above was found by running the same database version against successive kernels and bisecting the commits until one change was isolated. Treat OS upgrades as deployments: benchmark critical paths before and after, read release notes for scheduler, memory and I/O defaults.
- **Trade-off**: benchmarking costs time; skipping it moves the discovery to production.
- **Does not hold when**: the workload is not sensitive to scheduling or memory (stateless, I/O-bound services with generous headroom).
