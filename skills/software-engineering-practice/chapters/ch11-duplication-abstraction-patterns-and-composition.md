# Chapter 11: Duplication, Abstraction, Patterns and Composition

## Core Idea
Abstraction has a cost; it pays only where it matches what really varies or changes together. In this model the reliable order is: **write the code, notice duplicated knowledge or tangled responsibilities, then abstract**; patterns are a consequence of analysis, not a starting point. Examples are Python-like but the reasoning is language-independent.

## 11.1 DRY means "do not duplicate knowledge"
- **Thesis**: DRY is about knowledge (rules, data, business logic), not about the shape of loops and branches.
- **Mechanism**: a worked case merged two similar normalisation functions into one generic function steered by flags (strip, lower-case, required symbol, minimum length, prefix removal). Duplication shrank, but behaviour became impossible to read and every new requirement meant another flag. The better refactor ignored duplication and looked at responsibilities: separate **filtering** (is it valid?) from **normalising** (what shape?), one function per concern. Validity rules and normalisation rules each ended up in one place; two similar list comprehensions remained and were cheap and readable. A sign that you are going wrong: you need a growing set of flags to remove the duplication.
- **Trade-off**: a little duplication in return for readable code and visible local structure.
- **Does not hold when**: the duplicated thing is a rule (a validation, a pricing formula, a path-handling routine): there, remove it, even when it is hidden. A related case had the same "file or directory?" handling in two commands in a different order and spread across two files; the fix was one generic helper that accepts either and raises a specific error.

## 11.2 Wrong abstraction is worse than duplication
- **Thesis (position)**: prefer duplication to the wrong abstraction.
- **Mechanism**: a generic "calculate any area" function with a list of dimensions and two switches removed repetition but lied about its name (it fails for shapes outside its two special cases), was harder to read and harder to call than the specific functions. Better reuse built on meaning: a cylinder's volume reuses the circle's area. Duplication can also **protect a boundary**: a persistence schema and an API schema look alike, but sharing one object leaks database concerns into the API and couples their evolution.
- **Rule**: abstract when pieces have the same meaning and will change for the same reason, not because they look similar. A base class whose methods return untyped "objects" for two unrelated record types is a sign of shared look but not shared meaning.
- **Practical tips**: before writing, ask whether a library or an existing helper already does it; keep a clearly named central home for helpers (by theme, not one giant utility dump); refactor routinely (one practitioner spends roughly a tenth of the time; a personal figure) or schedule debt-focused periods (position). Duplication also signals an under-developed concept: grouping loose variables into an employee record removed it.
- **Does not hold when**: the duplicated copies must stay in lockstep (a rule); then the duplication is a defect waiting.

## 11.3 Patterns appear; they are not selected
- **Thesis**: choosing a pattern first leads to structure that outweighs the problem; analyse coupling and responsibilities first.
- **Mechanism**: a text summariser used a strategy hierarchy and a factory to build a prompt string selected by a style name. With very little variation, plain functions in a dictionary keyed by style did the job in far less code, and the main function became easy to read. The real volatility was elsewhere: provider-specific details (response format, token counting, context limit) inside a function that should not know them. A small interface for "a language-model client" (generate, count tokens, context limit), injected, put the variation behind one boundary and made tests trivial. That is the adapter pattern, and it was **reached by analysis, not chosen**. Test ease is a good check that the abstraction is in the right place.
- **Trade-off**: you may re-derive a known pattern; that is fine.
- **Does not hold when**: you already know many variants are coming; then the structure is justified earlier. Cross-reference ch06 (YAGNI).

## 11.4 The facade as a real boundary
- **Thesis**: a wrapper around somebody else's SDK helps only if it protects your application from that design.
- **Mechanism**: first step: gather the repetitive calls (create customer, create intent, confirm) into one service and callers get simpler. Common mistake: the method still returns the provider's object and raises the provider's errors, so callers still know it. A real boundary decides **which operations, which data, which errors and which vocabulary cross**: your own result type, your own error kinds, domain-level operations (pay, refund) rather than provider-level ones. Same for weather responses, engine vectors in a game, persistence-model objects in business logic, and model-provider response objects: do not let another system's objects shape your architecture. A fake behind the same interface makes tests simple.
- **Three failure modes**: a pass-through wrapper whose methods mirror the provider's; a **god facade** covering payments, invoices, subscriptions and coupons (split by cohesion); **hiding behaviour callers must know** (asynchronous completion, a required extra authentication step).
- **Facade versus adapter**: a facade simplifies access to a complex subsystem; an adapter converts one interface to another so implementations can be swapped. Different goals, both wrap.
- **Does not hold when**: you will never change the provider and use one call in one place; a facade is overhead. Service-level boundaries and anti-corruption layers: `software-architecture`.

## 11.5 Inheritance versus composition
- **Thesis**: inheritance is the strongest coupling in object-oriented code; prefer "has a" over "is a" unless the subtype truly is the parent.
- **Mechanism**: an employee example (hourly, salaried, freelancer, each with an optional commission) shows the progression. A base class removes duplicated personal data; but to separate commission from pay by inheritance you need a subclass per combination, so duplication returns and classes multiply with each dimension. Composition separates concerns: a person, a **contract** (hourly or salaried, an interface) and an optional **commission** (an interface); an employee combines any contract with or without a commission, with no combinatorial explosion, and each part extends independently.
- **Six common mistakes taken for good object orientation**: (1) inheriting to get an implementation (a report that "is" a database service and a logger): compose instead; (2) **turning values into types** (a subclass per tax rate): model variations as immutable data plus factory functions, keeping types for different behaviour or constraints; (3) modelling independent features as a hierarchy (retry plus validation): options object or composition, but note that options then couple behaviour to flags, and pulling validation out entirely can be better; (4) a base class that forces one shape on everything (stamp coupling, "not implemented" methods): split into small capability interfaces and ask each function for exactly what it uses; (5) a subtype that cannot honour the parent's guarantees (a read-only queue that fails on write): separate reader and writer contracts so the type checker rejects misuse; (6) abstracting before understanding the similarity (see 11.2).
- **Abstract interfaces versus concrete inheritance**: depending on an interface reduces coupling; subclassing a concrete class increases it. One practitioner uses inheritance almost only for abstract interfaces with one level (position); most classic patterns need one level.
- **Trade-off**: composition needs more wiring and some delegation.
- **Does not hold when**: the subtype really is the parent in every guaranteed way and the relationship is stable.

## 11.6 What good object orientation looks like
Objects protect invariants, combine state with meaningful behaviour and expose clear boundaries. Use composition when things vary independently, interfaces to describe capabilities, and **plain functions when there is no meaningful state or identity**. Classes are not the default answer.

## 11.7 The design principles in practice (SOLID, translated)
- **Thesis (position)**: these principles come from object-oriented design and are not commandments, but they teach thinking in responsibilities, dependencies and isolation, which also applies to functions.
- **Mechanism**: a messy "generate report" method read a file, filtered dates, computed several metrics and wrote output. Step by step: extract each metric behind a one-method interface and inject a list (single responsibility; open for extension: add a metric without touching the generator); extract the reader and the writer behind interfaces so CSV can become another format without editing the generator (dependency inversion); filter as its own step. The place where objects are created and connected is one entry point (the **composition root**), a good sign because the swap point is obvious and tests can supply fakes. Substitution means an implementation keeps the meaning of the contract (a metric function uses the data it is given and returns its own result); interface segregation means small interfaces matching what a client needs.
- **A function-based version** of the same design (a metric is a callable, config is a frozen record, reading, filtering and writing are functions) was shorter, equally modular and testable and in this practitioner's Python the preferred form; keep a record type where it groups data.
- **Single responsibility** raises cohesion but introduces a new coupling (the payment processor needs the order): say so.
- **Does not hold when**: the program is tiny; applying all five is ceremony.

## 11.8 Dependency injection
- **Thesis**: separate where an object is created from where it is used.
- **Mechanism**: an email sender that picks a service by a type argument grows another branch for every provider, and its construction needs the union of every provider's constructor arguments. Passing in an object that implements a small interface removes the switch; the sender no longer changes for a new provider; wiring happens at the top. Tests no longer need patching, and a failure points either at the sender body or at the service, not both. The default value of an injected dependency is still a dependency: consider no default, or a harmless fake (position).
- **Trade-off**: wiring code; one more indirection to read.
- **Does not hold when**: the dependency is stable and cheap (a pure helper); inject what varies or what is awkward to test. Injection in the domain interior has diminishing value; apply at the infrastructure edge (10.5).

## Cross-references
Chapter 05 (coupling kinds), 10 (function-level repairs), 06 (design versus architecture), 03 (test-driven design pressure). `software-architecture` for dependency inversion at architecture scale (hexagonal and layered styles).
