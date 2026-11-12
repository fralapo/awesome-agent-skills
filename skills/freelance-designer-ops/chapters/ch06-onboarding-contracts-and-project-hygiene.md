# Chapter 06: Onboarding, Contracts and Project Hygiene

## Core Idea
A project is won or lost in its first week and in its last mile. At the start, the "why" (business goals, users, current problems, what success looks like) is the most skipped step and the one most tied to results; "simple" asks often hide a lot of scope, so a fixed set of kickoff questions comes before any pixel. Around the work, three protections keep the freelancer solvent and sane: a short contract with objective limits, a deposit before work and payment before final files, and backups in more than two places. Inside the work, a predictable file structure and a precise QA/handoff format keep client, developer and designer looking at the same thing. None of this is glamour; all of it is why the next referral arrives.

Money terms in detail (amounts, splits, change orders) are in `pricing-and-sales-negotiation` ch03 and ch09; this chapter is the operational routine. Contract wording, tax and enforcement belong to a lawyer or accountant.

## Frameworks Introduced
**Four-phase project process**: (1) understand the why; (2) align on the core experience; (3) design; (4) deliver.
- *Why*: business goals, target users, problems, vision, what works and does not today.
- *Align*: map friction points to one shared end-to-end vision (for example browse, book, use, give feedback, cash out) and agree structure before polish.
- *Design*: collect inspiration from real products and the client's taste, then propose one direction.
- *Deliver*: prototypes for interactions that must be felt (maps, swipes, pinch, motion) plus organised screens/specs for developers.
When to use: any product, brand or web project of more than a few days. Measure the outcome (onboarding completion, users, enquiries) in the case study, not only the look.

**Pre-kickoff question set** for any "simple" request: How high is the priority? How will it evolve? What must we avoid? Does it differ per user type? What does success look like? Add the deck/page questions from ch01 (audience, occasion, deadline, count, assets, who edits later).
When to use: before quoting. Write the answers into the brief and send it back for confirmation.

**Contract minimum (four clauses)**: number of revision rounds included (two rounds is typical for a logo); an hourly rate for work after the agreed completion date or beyond the agreed scope; a deposit, stated as non-refundable once work starts; delivery of final and source files only after payment.
When to use: every job. This is orientation, not legal advice.

**Design file structure**: Cover (product, year, item) → Dev Ready → Prototypes (if any) → Review → work-in-progress pages, one per flow → design system (internal page or separate file).
Flow: explore privately in WIP → move only the pieces under discussion to Review for the weekly call → after approval, clean up and move to Dev Ready, split per flow, each flow as one board showing the full happy path with its states listed.
When to use: client product work in a design tool; keeps your messy playground away from the client.

**Design QA report format**: every issue carries title, description, type (bug, visual mismatch, copy, other), priority (for example high / medium / urgent), status (not started / in progress / blocked / done), a link to the design reference, the live capture next to it, and device/window size. Three capture levels: one DOM element (precise spacing, size), an area (layout region), a short screen recording (flows and behaviour, with network logs if debugging). A deep link per issue lets the developer land on it.
When to use: reviewing a build against your designs, or your own product before launch.

**Process one-pager (visual)**: a single page with five steps (for example research, concept creation, initial ideas, refinement, final result), each with a line on what the client can expect and what you need from them.
When to use: sent with the proposal or at onboarding; it raises client confidence and the chance of the next job.

## Rules & Practices

### Kickoff
- Align on structure (score + label + trend, page sections, flows) with low-fidelity concepts before visual polish, so the client reacts to direction and not to finish.
- Write the project goal in one or two sentences and keep it visible. A click goal, an awareness goal and a curiosity goal produce different imagery, CTA and style.
- Write a short design brief of goals (for example brand fit, low-friction onboarding, simple discovery, polish for trust, stay out of the way during use). Revisit it whenever iterations drift.
- Purpose also defines exclusions: a banking home screen shows balance and alerts at a glance and avoids heavy animation and decorative graphics.
- Ask who will see the work and where: a billboard has seconds, a brochure is read actively, a feed gets a thumb scroll.

### Money safety (practical)
- No deposit means working on spec with a stranger. Common deposits: 25%, 50% or the full fee; 50% is the most cited for design today (the pricing skill's payment-schedule section compares splits). Written as non-refundable once work starts.
- Never send final or source files before payment. A client who stopped replying and kept using the logo is the standard cautionary tale; without a contract the designer had no standing.
- Do not negotiate or deliver outside a platform that protects you unless you have a deposit and a contract.
- A vanishing client: send polite reminders, check their activity, then stop. Do not spend much time chasing.
- Charge for added time. A logo is "finished" when the client says so, but the contract decides what changes beyond the agreed deadline or budget cost.

### Scope and communication
- When a client pushes something you know will fail, be the professional: explain why, propose the alternative, politely and with reasons. Always explain why you do things (ch07 gives the full routine).
- Offer multiple solutions with the benefit of each to shorten the discussion.
- Say no confidently to overload or out-of-scope work ("I'm at capacity; we can fit it in the next cycle"). Say "I'm not sure, but I can find out" instead of bluffing.
- Email stays the official record (ch01). After a call, send a three-line summary of decisions.

### Files and backups
- Keep copies of all work in more than two places (for example two external drives plus cloud storage). One designer lost about 95% of past work from a single laptop; a loss like that also destroys the portfolio.
- Name files for the next person: project, item, version, date.

### Design file hygiene
- Keep exploration pages private. A client who can see every unfinished idea gets lost and derailed by endless discussion.
- Break WIP by flow (booking, payments, profile, onboarding, referral). One flow per page.
- Dev Ready holds only approved, cleaned work. One dumped page makes clients and developers hunt.
- For fast MVPs, design the happy paths and infer edge cases with the developer; still design contextual error states (for example a distinct message for password reset rather than one catch-all error), because missing error states block real users from signing up.
- Typical early-product tickets: team invites and remove-member flows, integrations page, paid-plan page for the payment provider, store screenshots made from the final screens.

### QA and handoff
The full AI-assisted handoff and design-QA method is in `ux-ui-expert` ch40; this is the freelancer's working version.
- Review the build against the design file: colours, font sizes, component sizes, positions, then copy, then behaviour (broken buttons, wrong destinations, scroll/resize breakage, half-open dropdowns).
- Core flows are urgent (a broken sign-in for the main integration), polish items are medium.
- Short screen recordings beat screenshots for behaviour. Side-by-side with the design reference removes ambiguity.
- A product aimed at designers will not retain them if the polish is low.

## Procedures
**Kickoff in one afternoon**
1. Send the pre-kickoff question set with the process one-pager.
2. Hold a 30-minute call; write the goal in one or two sentences and the three things to avoid.
3. Confirm scope, rounds, deposit, delivery date and who approves, in an email.
4. Deposit received → create the project in Notion (ch02) and the file with Cover, Review, WIP pages.
5. Back up the brief and assets to two locations.

**Weekly review rhythm (product work)**
1. Explore in WIP during the week.
2. Move the 2 to 4 pieces for discussion to Review the evening before.
3. Hold the call from the Review page only.
4. Record approvals in the email summary; move approved work to Dev Ready by flow.

**Pre-launch QA pass (your own product or a client's)**
1. Walk the product on a real device with a screen recorder.
2. Log each issue in the report format above, one per ticket, with category and priority.
3. Fix urgent core-flow issues first, then visual mismatches, then copy.

## Common Mistakes
- Starting without the "why" step.
- Working without a contract and then making free changes weeks later.
- Sending raw or final files before any payment.
- Delaying the portfolio site, and keeping a single copy of the work.
- Letting a strong-willed client dictate a design that does not help their business (ch07).
- One crammed Dev Ready page, or exploration visible to the client.
- Vague QA feedback with no reference, no device and no priority.
- Moving so fast that error states are forgotten.
- Over-polishing before alignment: colour and effects before structure.

## Mental Models
- A designer is a professional like a plumber: the client describes the leak; you decide the pipe.
- The contract does not signal distrust; it keeps the friendship possible.
- Backups are an investment in your own portfolio.
- Referrals come from projects that ended well, and "ended well" means clean handoff.
- Design with the customer's pain and the business goal in the same sentence.

## Examples
- A mobile product file for a fixed-fee engagement of about a few months: one Cover page, a Review page used in the weekly call, WIP pages per flow (booking, wallet, vetting, map, chat, profile, referral), then Dev Ready boards with the happy path and the states (card states, text messages, base state, cancel booking).
- A 0-to-1 mobile app delivered through the four-phase process reached 90% onboarding completion and 10,000 users in its first six months and supported a funding round; the case study led with those numbers.
- An illustrative QA ticket: "Button radius 8 instead of 12, onboarding step 3, iPhone 14, window 390 wide; reference link; capture side by side; priority medium; status not started."
