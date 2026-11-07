# Chapter 33: Atomic Design for a Reusable Component Library

## Core Idea
Build a component library in layers so a change propagates and several designers stay consistent. The process is not linear: you do not start by designing atoms. This gives a concrete procedure for the design-system sizing advice in ch19.

## Five Levels
| Level | Content | Examples |
|---|---|---|
| Atoms | Colours, type styles, labels, inputs, buttons | Primary button, input field |
| Molecules | Groups of atoms with one function | Contact form, team-member card, course card |
| Organisms | Page sections | Course listing, site footer, related posts |
| Templates | Page structures with placeholder content | Home, blog post, product, login, contact |
| Pages | Templates with real content | The shipped page |

Style guides stop at atoms and leave a gap to full pages; molecules and organisms bridge it.

## Procedure
1. Design two or three full pages; explore 10 to 20 variants of key pages before abstracting.
2. Look for recurring patterns across them.
3. Extract and standardise those patterns.
4. Build each component from smaller components.
5. Replace the instances in the pages with the component.
6. Share the library; editing a component updates every instance.

## Principles
- Pattern first, abstraction second: picking button styles before any page exists produces guesses.
- One source per component: edit the shared component, never each instance by hand.
- Match weight to team (ch19): a small team keeps atoms and a few molecules; add organisms and templates as the product multiplies.
- Pair with semantic tokens (ch22) so atoms read roles, not hex values.
- Define the states for every atom (ch18).

## Mistakes
- Starting with atoms in a vacuum.
- Hand-editing instances so copies drift.
- Heavy governance for a tiny team.

## Checklist
- [ ] 10-20 variants explored before extraction.
- [ ] Each organism built from molecules built from atoms.
- [ ] Pages use instances, not copies.
- [ ] Library shared with an owner.

## Connects To
ch17, ch18, ch19, ch22.
