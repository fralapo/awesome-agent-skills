# Chapter 40: AI-Assisted UI Workflow, Design-to-Code Handoff and Design QA

## Core Idea
AI design and code tools behave like a fast, literal junior: strong at execution, weak at hierarchy, restraint and judgment. Results depend on the brief, the order of work and the cleanliness of the design file. Treat the tool as an intern: give full context, work in small steps, state what not to do, and review everything against the same checks used on human work. Handoff and QA are the same discipline applied to the build: specific, contextual, linkable. Tool names change; the workflow below does not.

## Mindset
- Tools are still better at prototypes than at production-grade products built from nothing. Use them to explore and to build front ends from a clean design; keep humans on judgment, edge cases and payments.
- Durable value is problem solving, curiosity and execution, not tool mastery. Learn a tool when a problem needs it; get better at fundamentals before getting faster.
- Feeling behind is normal; many tools will not last. Experiment enough to stay fluent, without anxiety.

## Five Rules for Generating UI
1. **Give the destination**: long-term vision, target user, product premise, ideally a short PRD, as you would brief an intern.
2. **Go slow**: one screen at a time, in flow order (e.g. onboarding: home, phone number, personal info, email). Never one-shot a whole flow or landing page.
3. **State the prohibitions**: no new fonts, colours, styles, odd interactions, drop shadows or extra features. Telling the tool what not to do often helps more than saying what to do.
4. **Limit visual references**: one reference screenshot per screen plus what to create and what information it holds. Several similar references produce odd backgrounds, strange cropping and an obviously generated look. Reconciliation with rule 1: rich text context, minimal visual references.
5. **Revise against a checklist**: hierarchy (are the right things first, can users see what the product offers in seconds?), relevance (remove invented features and guesses), consistency (sizes, spacing, colours; generated output varies too much), polish (one obvious CTA, clean cropping, no stray backgrounds).
A stronger model noticeably improves polish. Once a few correct screens exist, reference them so later screens inherit their style.

## Common Failure Modes of Generated UI
Mis-prioritised hierarchy; bloated features; guessed content; inconsistent sizes, spacing and colours; placeholder icons and default backgrounds; the recognisable generic look that lowers trust (ch37).

## Anti-Generic Tweaks
Set a visual direction by hand first; make the tool reference existing screens for colour, type and spacing; replace placeholder icons and default shapes; change a few colours and images; add small human touches (a rotated icon, an unusual crop). The public website or store page is the trust-critical first impression, so check it more carefully than the product interior, which can be iterated.

## PRD-First Build Workflow (design to working app)
1. Draft a short, rough PRD with a chat AI that asks clarifying questions first. Keep it small; let it evolve.
2. Fix the MVP scope: user type, region, platform, payments, pickup or delivery model, tech stack.
3. Write the onboarding order and copy into the PRD.
4. Put the PRD (in a format the code tool can read, such as PDF), images and references in one project folder.
5. Ask the code tool to plan before building; create the base project and run it.
6. Connect the design tool to the code tool; pass the link to the selected frame, one screen at a time.
7. Correct with measurable instructions ("16 px margin on both sides of the button"), not adjectives.
8. Export images with explicit names into the asset catalogue and reference them by name.
9. After the first screens match the design, generate the rest from them.
10. Watch the context window: at about 80% use, start a new session and reference the previous one; quality degrades in long sessions.
If a screen looks wrong, fix the design file and have the code match it one to one; do not patch the code by eye.

## Design File Hygiene for Handoff
- **Auto layout** and well-structured frames: spacing and sizing are read from them. Unstructured frames and cropped images produced wrong spacing and wrong images in the first generated screens.
- Make sure the tool can access the file (permissions, link visibility); otherwise it sees only a shell.
- **Page structure** that shows the current state at a glance: Cover (product, year, item) -> Dev Ready -> Prototypes (if needed) -> Review -> work-in-progress pages per flow -> design system.
- Explore privately in the work-in-progress pages; move only items under discussion to Review; after approval clean up and move to Dev Ready, organised per flow, one board for the full happy path, with the states listed (card states, messages, base state, cancel).
- For a fast MVP, design the happy path and settle edge cases with the developer, but still define error states: contextual messages rather than one catch-all.
- Prototype what static frames cannot say: motion, maps, gestures, typing cadence of a chat reply. Hand over the numbers (duration, easing, speed).

## Animating with AI
Build frames from SVG elements with named layers so a prompt can target them ("animate the location indicator"). Prompt one effect at a time (fall in from the top, then fade in the dashed circles, then grow 10% and settle back), then adjust timing (double the duration). Asking for the full sequence in one prompt gets lost. A looped animation (a scan line across an ID card over about 5 seconds) can double as a loading state. Follow the restraint rules of ch37: no motion on critical moments.

## Design QA
Vague, scattered feedback with no reference to the design is the core problem. A good issue carries:
- title and description; type (bug, visual mismatch against the design, copy, other);
- priority (core flows such as a broken sign-in are urgent) and status (not started, in progress, blocked, done);
- the live implementation next to the design reference, side by side;
- the exact element, not a loose screenshot; for flows and behaviour, a short screen recording;
- context: device, window size, screenshot dimensions;
- a direct link so the developer lands on the issue.
Capture level by situation: element for spacing and sizing, area for layout regions, recording for flows. QA of your own product before launch uses the same four categories (bugs, visual inconsistencies versus design, copy, other). Polish expectations rise when the audience is designers.
Tests that cannot be delegated to a tool: payments and subscriptions, time-based triggers (nightly resets), sensors and anything needing a real device.

## Mistakes
- One huge prompt for a whole flow; several references with no written context.
- Unclean design files fed to a code tool.
- Adjective feedback ("make it cleaner") instead of numbers.
- Trusting generated hierarchy without review.
- Letting a long session run until quality degrades.
- QA by loose screenshots in a spreadsheet.

## Checklist
- [ ] Brief with vision, user, premise, prohibitions.
- [ ] One screen, one reference, one step at a time.
- [ ] Output checked for hierarchy, relevance, consistency, polish.
- [ ] File uses auto layout, named layers, a Dev Ready board per flow.
- [ ] Corrections stated in measurable terms.
- [ ] QA issues have side-by-side evidence, metadata and a link.
- [ ] Payments, time-based and sensor features tested on a real device.

## Connects To
ch17 (consistency), ch30 (prototyping), ch33 (component library), ch35 (contrast and craft), ch37 (generic look, motion restraint), ch38 (onboarding order and copy), ch41 (what to polish).
