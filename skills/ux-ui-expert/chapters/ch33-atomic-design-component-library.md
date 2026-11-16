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

## Design Tokens in Three Layers
Tokens are named values for everything repeated in the styles: colour, type, spacing, radius. Layer them so one edit lands in exactly the right place.
| Layer | Says | Example |
|---|---|---|
| Raw (primitive) | what the value is | `lime-500` |
| Semantic | what the value is for | `color-accent` -> `lime-500` |
| Component | where it is used | `button-bg` -> `color-accent` |
- Components read only the component layer; the component layer reads semantic; semantic reads raw. Never skip a layer.
- Change one point on purpose: re-point `color-accent` to move every accent; re-point `button-bg` to restyle buttons alone; edit `lime-500` only when the palette itself changes.
- Light and dark themes are a second set of semantic values; components stay untouched (ch22, ch18 dark mode).
- Adding an icon or a radius to every button is one edit in the button component, not a search through pages.

## Variant x Size x State Matrix
Define a component's whole space once, inside the component, instead of improvising per page.
- Example: a button with 3 variants (primary, secondary, text-only) x 3 sizes x 5 states (default, hover, focus, disabled, loading) = 45 combinations. Build them as properties of one component; pages pick a combination and never restyle it.
- Write the matrix before building; cross out combinations that will never exist (a loading text-only button may not be needed).
- Every added option multiplies the matrix. A component with 15 options for cases that do not exist is over-engineering: add an option when a real screen needs it.

## Real Content in the Concept
Layouts that survive placeholder text often break on real data: a 40-character product name, a missing image, a 6-line description, an empty list.
- Build the concept with content close to final (real names, lengths, images, numbers) and add the awkward cases: shortest, longest, empty, error.
- Templates may hold placeholders; pages must be checked with real content before the pattern is declared done (ch36 design for variance).
- Lorem ipsum hides hierarchy problems, because the text has no meaning to rank.

## Document and Review Components in Isolation
- Show each component alone with every variant and state in a component workbench or a library page (a documentation tool such as Storybook is the usual choice, version-dependent / verify). Test states there, not by hunting through pages.
- Per component record: purpose, when not to use it, the matrix, content limits (max characters), accessibility notes.
- The isolated view is also the QA and handoff surface (ch40): developers and designers argue about one rendered thing.

## Do Not Rebuild the Accessible Base
Keyboard navigation, focus management and screen-reader roles for menus, dialogs, tabs, selects and tooltips are hard to get right.
- Start from a headless (unstyled, behaviour-only) accessible component library (for example Radix) and apply your tokens on top. You own the look; the library owns the behaviour.
- Contrast of at least 4.5:1 for body text and never colour alone for status (ch18, ch22) stay your job, since a headless base has no colours.
- Check the library's maintenance and framework support before adopting it (version-dependent / verify).

## Start Small on an Existing Site
1. List the colours, fonts, radii and spacings already in use; turn each into a named token.
2. Find the most repeated components (button, card, input) and move each into its own file.
3. Replace the instances with the component.
Keep the library small: simple and tied to real needs beats a system for imagined cases.

## Mistakes
- Starting with atoms in a vacuum.
- Components that read raw values directly, so a palette change is a hunt.
- Skipping the variant matrix and styling one-off button versions per page.
- Concepts made with lorem ipsum.
- Rebuilding focus handling and keyboard behaviour from scratch.
- Hand-editing instances so copies drift.
- Heavy governance for a tiny team.

## Checklist
- [ ] 10-20 variants explored before extraction.
- [ ] Each organism built from molecules built from atoms.
- [ ] Pages use instances, not copies.
- [ ] Library shared with an owner.
- [ ] Tokens in three layers; components read only component tokens.
- [ ] Variant x size x state matrix written and built once per component.
- [ ] Concept checked with real, shortest, longest and empty content.
- [ ] Components documented and tested in isolation.
- [ ] Accessible behaviour comes from a headless base, not from scratch.

## Connects To
ch17, ch18, ch19, ch22, ch36, ch40, ch42.
