# Chapter 12: Learning to Program: Mental Models That Make Code Predictable

## Core Idea
Beginners' errors cluster around a handful of wrong pictures of what a program is. In this model, a good introduction fixes the pictures (what a variable is, what a loop checks, what a function receives) before adding syntax, and it teaches a method: solve the general case on paper, then translate. Syntax can be looked up; concepts have to be reasoned. Examples use a typical scripting language; the ideas carry over.

## 12.1 Method: concepts reasoned, syntax searched
- **Thesis**: knowledge splits into things to look up (exact syntax, library names) and things to understand (decomposition, state, flow).
- **Mechanism**: work in order: state the general case on paper with a small example, split into sub-problems, write each as code, run it, then simulate loops by hand or in a visualiser that shows variables changing step by step. Search error messages and documentation (usually in English). Code is learned by writing it; watching others write it gives a feeling of understanding without the skill.
- **Trade-off**: slow at first, fast later; delegating this to a model removes the struggle that builds the skill (`coding-with-agents` ch05 section 9).
- **Does not hold when**: you need a one-off script and will not maintain it.

## 12.2 Variables, assignment, comparison and types
- **Thesis**: a variable is a named box whose content changes; "=" stores and "==" asks.
- **Mechanism**: assignment evaluates the right side and stores it on the left; swapping two values needs a temporary third box, otherwise the first value is overwritten (the general solution beats the case-specific one). Every value has a type, and input from a user arrives as text: convert it (casting) and validate it before use. Read an error trace from the bottom: the last line names the failure, the lines above show where it was reached. Indentation is part of the syntax in some languages.
- **Trade-off**: dynamic typing is quick to write and moves type errors to run time.
- **Does not hold when**: a statically typed language rejects the mistake before the program runs.

## 12.3 Conditions and booleans
- **Thesis**: a condition is an expression that yields true or false, and the natural-language shape of a sentence does not carry over.
- **Mechanism**: "a equals x or y" must be written as two comparisons joined by "or"; writing a == x or y is true whenever y is a non-empty value, whatever a is, because the second operand is tested on its own. Nested branches read better with descriptive names and early returns; hiding a program exit deep inside a branch makes flow hard to follow.
- **Trade-off**: more named intermediate conditions mean more lines and fewer misreadings.
- **Does not hold when**: the condition is a single obvious comparison.

## 12.4 Loops
- **Thesis**: a while loop repeats as long as a condition holds, so the body must be able to change that condition; a for loop is a "for each" that hides the index and stop test.
- **Mechanism**: teach the while loop first, because it exposes the counter, the test and the update that the for loop conceals. Ranges and slices include the start and exclude the end, and positions count from zero; the user counts from one, so the index is the position minus one (off-by-one errors live here). A comprehension is syntactic sugar for a loop that builds a list.
- **Trade-off**: explicit loops are verbose; comprehensions are compact and hide the steps.
- **Does not hold when**: the sequence is processed by a library function that already encodes the loop.

## 12.5 Choosing a data structure before writing code
- **Thesis**: the shape of the data decides the code; choose the container first.
- **Mechanism**: a *list* keeps order and allows duplicates and in-place change; a *dictionary* maps keys to values for direct lookup; a *set* keeps unique elements and answers membership faster than a list (ch3); a *tuple* is a fixed record. Moving data into a list makes behaviour updatable without editing the code (adding an item changes the data, not the logic). JSON is nested lists and dictionaries. A boolean flag can hold the state of a game or a loop.
- **Trade-off**: the right structure speeds the program and clarifies it; the wrong one forces convoluted code.
- **Does not hold when**: the data is tiny and the code runs once.

## 12.6 Memory: stack, heap and shared references
- **Thesis**: passing a list to a function passes the reference, not a copy, so caller and function change the same object.
- **Mechanism**: each call gets a frame on the stack holding its local names; objects live on the heap and names point to them (ch6, ch4). Rebinding a name inside a function does not affect the caller, but modifying a shared object does. Prefer returning new values to mutating arguments in place, and avoid global variables, because both create hidden coupling (`software-engineering-practice` ch05).
- **Trade-off**: sharing is cheap and surprising; copying is safe and costs time and memory.
- **Does not hold when**: the value is immutable (numbers, strings, tuples), so a change creates a new object.

## 12.7 Classes as templates
- **Thesis**: a class is a template for objects with guaranteed fields and methods that enforce rules.
- **Mechanism**: the constructor sets the fields; "self" is the object the method acts on; a method bundles data with the rule that changes it, which keeps invariants in one place (`software-engineering-practice` ch10). In several languages everything is an object, including numbers and functions.
- **Trade-off**: classes organise growth and add ceremony to small scripts.
- **Does not hold when**: a plain function and a dictionary do the job.

## 12.8 Talking to the outside: files, APIs and errors
- **Thesis**: code that depends on a network, a file or a user must expect that dependency to fail.
- **Mechanism**: an API call returns a status code (ch7.8); handle the unsuccessful ones, respect rate limits, send tokens in headers and never publish them, and wrap the risky call in a try/except that handles what you can recover from (`software-engineering-practice` ch12). Relative paths depend on where the program is launched; absolute paths do not travel. Packages are installed by a package manager and imported by name.
- **Trade-off**: defensive code is longer; undefended code fails far from the cause.
- **Does not hold when**: the input is fully under your control (a fixed local file you wrote).

## 12.9 Real data: common case first, then the anomalies
- **Thesis**: most of the work in a data project is cleaning, and the way to make progress is to parse the regular majority first.
- **Mechanism**: write the parser for the typical rows (in one worked case about 80% of the rows), then examine the rest, which are exceptions and errors; keep each parsing stage separate. Interpret cautiously: a rise in famous deaths per year in a Wikipedia-derived table may reflect Wikipedia's growth rather than reality (a selection effect, ch11).
- **Trade-off**: staged parsing is slower to write and easier to debug.
- **Does not hold when**: the data arrives in a rigid, validated schema.

## Common Mistakes
- Copying code without being able to simulate it by hand.
- Writing a == x or y, or counting from one in a zero-based list.
- Mutating a list passed as an argument and then being surprised.
- Treating user input as a number before converting it.

## Checklist
- [ ] General case solved on paper first?
- [ ] Types converted and validated at the boundary?
- [ ] Loop condition can change; boundaries checked?
- [ ] Data structure chosen before code?
- [ ] Failure of the outside world handled?

## Connects To
ch3 (structures), ch4 and ch6 (memory), ch7.8 and ch10 (web and APIs), ch11 (reasoning); `coding-with-agents` ch05 (learning with AI), `software-engineering-practice` ch12 (errors).
