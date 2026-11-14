# Chapter 10: Function and Module-Level Design

## Core Idea
Most day-to-day design happens below the architecture line: how many arguments a function takes, where a rule lives, what a value is allowed to be, how data travels through a workflow. In this model the question behind every choice here is the same one as in chapter 05: **if I change this, what else must change?** Locality of change is the metric; patterns, principles and "clean code" rules are only means to it. Examples use a Python-like language, but the reasoning is language-independent (typing and immutability tools differ by language: general knowledge).

## 10.1 Too many parameters: introduce the concept that is missing
- **Thesis**: keyword arguments make a long call readable but do not fix the design; when the same group of values travels through many functions, a concept is missing.
- **Mechanism**: each function in the chain needs a slightly different copy of the same parameter group, so adding one option means editing every signature. Group the values into an immutable **parameter object** (for example a search query). Once the concept exists, it can own behaviour: validation when it is created (so every holder knows it is valid), derived values such as a cache key, and normalisation. Adding a field then touches the object and only the code that cares about the new field. Branching on the object's contents can use pattern matching where the language has it (taste, not a requirement) (position).
- **Trade-off**: a new class to name and maintain.
- **Does not hold when**: passing the whole object to a low-level helper that needs one field. That is **stamp coupling** (10.7): the helper now knows the object, can start to use other fields by accident and cannot be reused elsewhere. Use the parameter object for high-level orchestration that really works with the whole concept; pass plain values to small helpers. Sometimes the right fix is not a new object but splitting the function so each does less.

## 10.2 Growing conditionals and flags: policies
- **Thesis**: a function that accumulates boolean flags and `if` branches for every new rule becomes hard to extend, test and reuse; one rule per unit fixes this.
- **Mechanism**: model each rule as a **policy** (one rule, one responsibility), then compose them. In an object style that is a protocol with one method plus a composite that applies a list. In a function style each policy takes the context and returns the (possibly updated) context, so a pipeline is a fold over a list. Pushing it further, a registry maps names to functions and an enabled-list read from configuration builds the pipeline: **switching a rule on or off becomes configuration, a feature flag without conditionals scattered in logic**; order is explicit and configurable.
- **Trade-off**: more code for the same behaviour (one worked comparison roughly doubled the line count) and more up-front thinking; rules become explicit, individually testable and reusable.
- **Does not hold when**: a throwaway script or a rule set that will stay small. In this model "policy" (combine rules) is distinct from "strategy" (choose one algorithm), though they share structure (position). Where the flag is really a toggle for unfinished work, see ch02.

## 10.3 Primitive obsession and invalid states
- **Thesis**: representing domain concepts as bare primitives forces every function to re-validate and invites unit mistakes; make invalid states unrepresentable.
- **Mechanism**: a price as a float or a discount as a number: is 0.2 twenty percent or 0.2 percent? Cents or units? Already rounded? Every function validates defensively and one eventually forgets. A **value object** is immutable, compared by value and enforces its own invariants: validate once at construction, trust the value everywhere else. The signature now states the concept, and extra behaviour (a domain extraction on an email address, a constructor from a 0-100 scale) lives with the data. Implementation choices: a frozen record with a post-construction check, or a subclass of the primitive; a validation library is possible but adds weight, and for pure domain concepts a plain frozen record is simpler (position).
- **Trade-off**: more types; conversions at the edges.
- **Does not hold when**: a primitive carries no rule or meaning. An **enumeration** answers "which option"; a value object answers "is it valid and how does it behave"; they complement each other. Money precision: floating point is inadequate for currency in production; use integer minor units or a decimal type (general knowledge).

## 10.4 Brittle functions: types, branches and defaults
- **Thesis (position)**: do not use runtime type checks as logic; let annotations document and a static checker verify.
- **Mechanism**: four styles exist: no hints and no checks; assertions before every call; checks inside the function; annotations. Assertions clutter, force every caller to pay, and break on legitimate subtypes; annotations act at development time. Do not annotate too narrowly: if a function works on any collection of numbers, say so. How precise to be depends on audience (internal helper versus widely used package). **Branching on argument type inside one function** is brittle: split into separate, well-named functions, use type-based dispatch, or a dictionary of functions (strategy), with a preference here for separate named functions. Enforce value constraints (non-empty list, positive number) with specific errors (ch12).
- **Optional parameters**: use `None` only when there is logic tied to its absence (a precision argument where none means "do not round"); otherwise prefer a sensible default or a required argument. Fewer optional values means fewer checks.
- **Does not hold when**: the language is statically typed (many of these checks are then compile-time) or the input crosses a trust boundary (validate there, see ch12).

## 10.5 Data that spreads: phases, orchestration and Demeter
- **Thesis**: a long function becomes fragile not because it is long but because one piece of data (a reference returned by one step) is threaded through every later step.
- **Mechanism**: **structural coupling** (every step knows the data) plus **temporal coupling** (order matters: reserve, then save, then invoice, then notify). A harmless feature request (add the reference to the confirmation message) then breaks analytics and invoicing. Remedies: split into clear phases; keep the workflow as **orchestration** and move rules to the domain objects that own the data (a traveller object answers "do you need a visa for this country?"); collect the spread data into the record that owns it (the booking), so consumers depend on the record and not on a local variable; stop reaching through objects (chains such as itinerary, destination, country) by giving the owner a property or method (**Law of Demeter**), so internal structure can change. Ordering that must exist stays explicit.
- **Abstraction placement**: inject collaborators (good) and make them depend on a small interface, but put the abstraction **at the edge** between workflow and infrastructure (external APIs, databases, event systems, logging); inside the domain, direct coupling between its own objects is less harmful (position).
- **Connascence** (a 1990s concept): two pieces are connected if changing one forces changing the other; use "how far does a change propagate?" as a design metric.
- **Does not hold when**: a short script whose single owner holds all of it in mind.

## 10.6 Cohesion beats smallness
- **Thesis**: clean-code rules applied as a checklist (small classes, short methods, abstract everything, add patterns) produce **over-decomposition**: tidy on the surface, still hard to change the behaviour. The goal is cohesion, not smallness.
- **Mechanism**: a worked example had a container and a protocol with a single implementation where injection bought nothing, while the real service stayed a long method with its settings buried. Cohesive reorganisation: remove abstractions that do not solve a problem; group settings that change together into one immutable **configuration object** with defaults; make the pipeline visible and controllable from the top (load, summarise, export as separate steps called in one place, so data is loaded once and exported many times); put behaviour with the data it describes (a summary renders itself); use separate export functions instead of a target switch; name honestly (a function that summarises should not be called "run"); extract the validity check. A new output format then becomes one more function.
- **Trade-off**: an explicit pipeline in the entry point exposes more steps to the reader.
- **Does not hold when**: you genuinely need to swap implementations; then an abstraction is right. Place it where variation actually occurs. Value objects (10.3) are a good example of clean-code principles applied in the right place.

## 10.7 A repair menu for code-level coupling (see 5.9)
| Smell | Cheap fix | Cost of that fix |
|---|---|---|
| Function reads module-level constants (global coupling) | Pass them in | Many arguments (data coupling) |
| Many arguments | Group into a client or config object | Every layer that uses it must receive it |
| Code modifies another object's internals (content coupling) | Add an explicitly named method on the owner (for example an unchecked variant whose name warns) | An unsafe path now exists; language may not enforce it |
| Whole object passed for a few fields (stamp coupling) | Pass fields, or a tiny interface listing what is used | Long argument lists, or interface proliferation |
| Function belongs to the data it reads | Make it a method | Owner grows; may not be its job |
There is no free option; each fix trades one coupling for a less harmful one. In this model a design assistant can write the code for these options but judging the trade-off remains the engineer's work (position; any claimed share of "code generation versus the rest of the work" is an unverified opinion). See `coding-with-agents`.

## Cross-references
Chapter 05 (taxonomy of coupling), 11 (duplication, patterns, composition), 12 (errors), 06 (when to design). `software-architecture` for boundaries at service level.
