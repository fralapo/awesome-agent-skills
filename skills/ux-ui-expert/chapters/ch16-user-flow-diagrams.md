# Chapter 16: User Flow Diagrams

## Core Idea
A user flow diagram maps every step a user can take to complete a task, letting designers predict the full path in advance, spot potential problems before they're built, and communicate that path clearly to non-designer stakeholders.

## Frameworks Introduced
- **User Flow Notation**: a small, standard symbol set.
  - **Circle** — start and end points of a flow.
  - **Solid/regular line** — the preferred action, usually moving the user forward.
  - **Dotted line** — an alternative action, such as going back or branching off.
  - **Rectangle/step** — a discrete step or screen in the process.
  - **Diamond** — a decision point where the path branches based on a condition.
  - When to use: whenever mapping any multi-step task (onboarding, checkout, login) to visualize every possible path, not just the happy path.
  - How: start with a circle, connect steps and decisions in sequence, branch alternate/edge-case paths (e.g., "forgot password") into their own linked sub-flows rather than cramming them into the main flow.

## Key Concepts
- **Preferred path vs. alternative path**: the main flow (solid lines) represents the expected/most common route; dotted lines and branching diamonds capture edge cases (errors, back-navigation, recovery flows) that must still be designed for.
- **Decision point**: any moment in a flow where the system or user's input determines which of two or more paths is taken next (e.g., "does the email/password match?").
- **Sub-flow**: a separate, linked flow diagram (e.g., registration, password recovery) that a decision point in the main flow can route into, keeping the main diagram legible instead of overloaded.

## Mental Models
- Treat a user flow as a debugging tool for the design itself: walking every branch on paper before building surfaces missing states (e.g., "what happens if the password doesn't match twice?") much more cheaply than discovering them after implementation.
- Design user flows for a non-designer audience by default — stakeholders, executives, and cross-functional partners are common viewers of this deliverable, so clarity of notation matters as much as completeness.

## Anti-patterns
- **Only diagramming the happy path**: omitting error states, back-navigation, and recovery flows (e.g., forgotten password) leaves exactly the edge cases most likely to cause user drop-off undesigned.
- **Overloading a single diagram with every sub-flow**: cramming registration, recovery, and the main flow into one diagram makes it unreadable — branch complex alternate paths into their own linked flows instead.
- **Inconsistent or undocumented notation**: mixing up solid/dotted line meaning or improvising symbols defeats the purpose of a shared, quickly-readable visual language for cross-functional review.

## Key Takeaways
1. Use the standard notation (circle = start/end, solid line = preferred path, dotted line = alternative path, diamond = decision) consistently so any stakeholder can read the diagram without training.
2. Map decision points explicitly (e.g., "does input match expected value?") and route both outcomes somewhere — never leave a branch as a dead end.
3. Split complex alternate journeys (e.g., password recovery) into their own linked sub-flow diagrams rather than overcrowding the main flow.
4. Use flow diagrams as an upfront problem-finding tool, not just a post-hoc documentation artifact.

## Connects To
- **Ch14**: user flows are a concrete artifact typically produced during the Develop phase of the Double Diamond, once a solution direction is being explored.
- **Ch12**: flow mapping operates at the interface-design/information-architecture layer of the UX Iceberg — structural work beneath visual design.
