# Chapter 6: Runtimes, Compilers and Operating Systems

## Core Idea
Between your code and the transistors sit layers that lie on purpose: the compiler rewrites what you wrote, the runtime frees memory for you, the operating system gives every program a private machine. In this model each lie buys safety or convenience at a known cost, and most debugging and performance work is finding which layer is answering and what it assumes.

## 6.1 From source to execution: compiled, interpreted, typed
- **Thesis**: a programming language is an abstraction that hides the machine layer by layer; how it is executed decides when errors and costs appear.
- **Mechanism**: a compiler converts the whole program to machine code in advance, producing an executable that needs no extra dependencies; an interpreter executes the program line by line at run time. Statically typed languages require declared types, checked early; dynamically typed ones work types out at run time. Many languages sit in between (compile to an intermediate form, then run it on a virtual machine; translate hot code at run time).
- **Trade-off**: ahead-of-time compilation gives speed and early errors; interpretation gives flexibility and faster feedback.
- **Does not hold when**: the language is implemented by a hybrid, in which case the simple split is only a first approximation (general knowledge).

## 6.2 Manual memory management and the three classic mistakes
- **Thesis**: asking for memory and giving it back by hand is easy to describe and hard to do right at scale.
- **Mechanism**: a program asks the system for a block (allocate) and returns it when done (free), because it cannot know in advance how much it will need (the size of a photo, of a web page, of a shopping basket). Mistakes: forgetting to free is a leak (memory grows until the program or machine fails); using a block after freeing it gives random behaviour, since the memory may belong to someone else by then; freeing the same block twice can free a block now used by another part of the program, which then fails. Humans are poor at tracking this in large programs.
- **Trade-off**: manual control gives predictable timing and no collector overhead.
- **Does not hold when**: the program is small, short-lived or exits soon, or an ownership system in the language checks lifetimes for you.

## 6.3 Reference counting
- **Thesis**: attach a counter to each block recording how many holders it has; free it when the counter reaches zero.
- **Mechanism**: allocation sets the count to one; sharing increments it; releasing decrements it. It is mostly automatic, and it frees memory promptly.
- **Trade-off**: every block carries a counter; updates are error-prone to write by hand and can cost a lot when references are passed around constantly; and cycles defeat it: two objects that point to each other keep each other's count above zero even when nothing else can reach them. The result is a leak that looks like correct code.
- **Does not hold when**: data is acyclic or cycles are broken explicitly (weak references).

## 6.4 Tracing garbage collection: mark and sweep
- **Thesis**: decide what is garbage by asking what can still be reached from the program's roots; everything else can go. Reachability is more accurate than counting.
- **Mechanism**: roots are the references the running program holds (for example variables). Mark phase: start at the roots, follow every reference, and mark each object reached (this is a graph traversal). Sweep phase: look at all objects in memory; free those not marked. An object not pointed at directly by a variable survives if another live object points to it. Real collectors are the same idea plus optimisations: the mark is one bit stored with other object data, and to avoid clearing every mark after each cycle the meaning of the bit flips each time.
- **Trade-off**: the collector costs time and memory, and the marking work has to be scheduled (general knowledge: pauses or concurrent collection, a large design space). A program can still "leak" in a collected language: one forgotten reference (a long-lived list, a cache, a listener) keeps millions of objects reachable. Tooling exists to find the root that holds them.
- **Does not hold when**: you need hard real-time guarantees without pauses, or you must control exactly when memory is returned to the system.

## 6.5 Stack and heap
- **Thesis**: function calls and long-lived objects use different memory areas with different rules.
- **Mechanism**: the call stack holds the frames of the function calls in progress and is short-term and limited (deep recursion overflows it); the heap holds objects that outlive a call and can grow and shrink; passing an object by reference means several variables point to one heap object, with no copy of the data.
- **Trade-off**: shared references save memory and copying but create aliasing (a change through one name is visible through another).
- **Does not hold when**: the language copies on assignment (value semantics).

## 6.6 What compilers do: the division example
- **Thesis**: a compiler is not a literal translator; it replaces expensive operations by cheaper equivalent ones whenever it can prove equivalence.
- **Mechanism**: on current hardware an addition or logical operation takes about one cycle (a third of a nanosecond at a few gigahertz); an integer multiplication takes about five cycles; an integer division takes roughly 30 to 100 (figures as stated, a dated snapshot, varying with the processor). When the divisor is a constant known at compile time, the compiler replaces the division by a multiplication by an approximation of the reciprocal followed by a cheap shift. By analogy: a 20 per cent tip is double the bill and drop the last digit. Dividing by 3 in decimal terms: multiply by 334 and drop the last three digits (14 times 334 is 4676, giving 4, equal to 14 divided by 3 rounded down); the multiplier is rounded up slightly so that rounding comes out right over the whole input range. In binary the same idea uses a fraction with a power-of-two denominator: one third is about 11/32, so multiply by 11 and drop five bits (14 times 11 is 154, which shifted right five places is 4). Dividing by powers of two is just a shift.
- **Trade-off**: it works only when the divisor is known ahead of time; the multiplier and shift must be chosen with enough precision for the range of the input (a bounded word size). The trick makes the machine code unrecognisable, which matters when you read disassembly.
- **Does not hold when**: both numbers come from the user at run time; the processor must then divide. Other things a compiler does: unrolling loops (doing several elements per loop trip to cut loop tests) and choosing instructions such as decrement-and-branch.

## 6.7 What an operating system does, in boot order
- **Thesis**: an operating system is the program that builds processes, files and isolation out of a bare CPU and a disk.
- **Mechanism**: (1) Firmware wakes just enough hardware to find a disk and hands over to a bootloader, which loads the kernel into memory. (2) Privilege levels: the kernel runs at the most privileged level, user programs at the least; user code must ask for anything beyond its own memory, so a buggy program crashes itself, not the machine. (3) Virtual memory (see ch4): each process has its own page table; a missing page raises a fault, the kernel loads it and resumes. (4) File systems: a disk is numbered blocks; the file system presents files and folders. A file is described by an index node that holds size, permissions, timestamps and pointers to data blocks, but not the name; names live in directories, which map names to index-node numbers, so several names can point at one file. Journaling writes intentions first, so a power loss mid-write usually leaves a consistent disk. (5) Device drivers translate generic kernel requests for each piece of hardware; they run in kernel mode, so a faulty driver can crash the whole system. (6) Interrupts: instead of polling, hardware signals the CPU, which jumps to a handler; this is how keyboards, networks and timers get attention. (7) The first user process is the ancestor of all others; the kernel keeps a process table and assigns each process an id. (8) System calls are the real API of the machine: the process loads arguments into registers and executes a special instruction; the CPU switches to kernel level; there are on the order of four hundred on one popular kernel (as stated); a library call such as printing ends in a write system call. Creating processes uses fork (copy) and exec (replace with a new program). (9) The scheduler decides which of hundreds of runnable processes gets a core, aiming at fair shares; the policy named for one popular kernel is based on virtual deadlines (dated). (10) Threads share memory and files but have their own stack and program counter; sharing creates races (ch5). (11) Inter-process communication: pipes (a byte stream from one process to another, so two programs that know nothing of each other compose), sockets, message queues; shared memory is possible through page mapping. (12) Shutdown: processes get a polite termination signal, then after a timeout a forced kill; the file system flushes its journal and unmounts; drivers release hardware; memory is synced; the CPU halts.
- **Trade-off**: every boundary crossing (system call, context switch, page fault) costs time; isolation costs performance.
- **Does not hold when**: the system is a small embedded device without kernel/user separation.

## 6.8 Concurrency models above the kernel
- **Thesis**: doing several things at once means either true parallelism (several cores) or interleaving on one; they differ in what can go wrong.
- **Mechanism**: a processor core can expose several hardware threads. Some languages offer parallel threads; others are single-threaded and use an event loop or coroutines that pause and resume work. Languages also add safety nets (lightweight tasks, ownership checks that refuse to compile unsafe sharing).
- **Trade-off**: an event loop avoids data races but one slow task blocks everything; threads use all cores but need locks.
- **Does not hold when**: the workload is I/O bound and a single thread is enough.

## 6.9 Virtual machines in the cloud
- **Thesis**: software can simulate hardware, so a large machine is split into many small ones.
- **Mechanism**: a virtual machine is a program that presents a complete (virtual) computer; this is the basis of rented servers.
- **Trade-off**: isolation and flexibility against some overhead and a layer that can hide the real cost.
- **Does not hold when**: you need access to specific hardware features directly.

See also: `software-architecture` ch12 (kernel cost, huge pages, lock stalls in production) and ch13, ch16; `coding-with-agents` for how agents write and review such code.
