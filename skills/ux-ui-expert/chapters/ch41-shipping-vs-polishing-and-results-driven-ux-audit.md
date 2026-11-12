# Chapter 41: Shipping vs Polishing, and the Results-Driven UX Audit

## Core Idea
Design depth is a budget. With little traffic, most polish is invisible and unmeasured; the screens that drive key metrics deserve depth only once enough people reach them. Design time can also become a comfortable substitute for uncomfortable work (talking to users, distribution, asking for money). This chapter gives decision rules for when to ship, when to polish, and how to run an audit that ends in a prioritised list tied to a business goal. It extends the structural audit of ch34 and the discipline of ch30 (prototype early) and ch26 (minimum viable research).

## When to Ship and When to Polish
**Ship first** when:
- the product is new, traffic is near zero or the category is unproven for you;
- the screen is a rare edge case, a settings page or a micro-interaction;
- the change cannot be measured with the volume you have (three visitors a day yield no data).
**Go deep** when:
- a screen sits on a conversion step: onboarding drop-off points, paywall, store page, landing page, checkout;
- enough people reach it to measure a change (a rule of thumb: hundreds of visits per variant in the period you can wait);
- the audience judges craft (a product for designers has to look polished at launch).
Quality of the first impression is the exception: the public site or store page and the first run are worth polish early (ch37), because they set trust before any metric exists.

## Time-Boxed Solo Build
A realistic plan for a small app: about two weeks for design and build, then bug fixing, then submission.
1. Choose a category where demand is proven, and find a small twist (a trigger or mechanic competitors lack).
2. Keep scope small enough to design, build and ship alone.
3. Sticky-note the flow, write every onboarding step word for word, turn it into a PRD (ch40).
4. Design only the three to five key screens; use them as the style reference for the rest.
5. Skip architecture documents, a marketing site and detail work until something ships.
6. Decide the pricing model before building (ch38).
Anti-patterns: a costly agency-built first version with extra features and a free tier kept too long; six months of iteration without a second launch; a whole day redesigning a paywall before any traffic.

## Validate Before You Build
Signals, in order of cost: a pain you have felt for years (others likely share it); communities where target users gather (a survey of about 100 responses); competitors (their absence is a warning: too hard, or too small a problem); about 25 one-to-one conversations (ask for stories, "walk me through the last time", never lead); existing workarounds (spreadsheets, screenshots with manual tickets: people already pay in time). Surveys miss nuance by company size and role; follow them with interviews (ch27).
- Say versus do: unpaid consumers rarely join interviews, so recordings and analytics are often more truthful. When stated preference and behaviour conflict (a banner disliked in every test but better for sales in about twenty trials), follow the behaviour and keep tracking both.

## Launch with a Closed Beta
1. Build real connections with target users before asking for anything.
2. Invite 25-30 hand-picked users (a few influential ones) in exchange for feedback, ideally a call.
3. Announce that the beta is live; people not invited leave an email and see a "we are at capacity, we will reach out" screen. This measures interest.
4. Build the public site from a template; swap images, copy, colours and fonts.
5. QA pass (ch40) before the first invite.
6. Public launch after the feedback is absorbed. Prepare store screenshots from the real designs.
7. **Instrument from day one**: the attribution question in onboarding (ch38), funnel steps, paywall events. Most downloads arrive in the first weeks; without tracking, the source of those users is lost.

## The Five-Step UX Audit that Produces Results
An audit with no business goal produces random fixes ("digging a hole and filling it back up").
1. **Understand the current state**: pain points, where users drop off, where metrics fall, where they hesitate, biggest complaints, what motivates or deters purchase.
2. **Set the goal**: more sign-ups, conversions, time in app (only if aligned, ch39), shares. Each finding must support it.
3. **Run the audit** by walking the real product with notes. Use five lenses:
   - **Clarity**: is the offer or message clear?
   - **Flow**: logical, low friction (sign-up, checkout, free-to-paid)?
   - **Hierarchy**: is the most important information easiest to find?
   - **Consistency**: colours, fonts, weights, icons, spacing.
   - **Density**: limited options, no overload (a 300-item menu fails; ch20).
4. **Package findings**: issue -> evidence (screenshot, metric) -> why it matters to the goal -> proposed fix.
5. **Prioritise on an impact-effort 2x2**: do high-impact, low-effort first; schedule high-impact, high-effort; batch low-impact, low-effort; drop low-impact, high-effort.
Pair this with the structural audit order of ch34 (purpose, hierarchy, consistency, navigation, colour, layout, platform) and with ch37's detail audit.

## Time-Boxed Audit and Refresh
For a quick look at an app or a small refresh: set a fixed timer (about two hours for an audit, about sixty minutes for a refresh of one flow). Screenshot each flow; annotate inconsistencies, hierarchy problems, onboarding length, what could be consolidated, and open questions for the team. Reuse an existing component library and screens from past work; consult onboarding and pattern galleries for structure, not visuals; use free stock photography with an overlay or scrim for text legibility; show forms with realistic filled-in examples. Deliver direction, not final polish; the first screen sets the perceived polish of the whole flow. Check low-value space (decorative category tiles), fairness (one item per map pin so people can drill down) and relevance (why is a stranger's name shown here?).

## Stakeholders and Rejection
Rejection of a design is information. Detach, ask questions, find what the client is reaching for, and test each iteration against the original goal. If iterations drift, pause and push back with the goal; compromise by shipping the clear version and deferring fancy concepts. Before starting any "simple" request ask: how high is the priority, how will it evolve, what to avoid, does it differ per user, what does success look like. Align structure at low fidelity before visuals. A status or score display never relies on colour alone: add icons, labels and numbers, and avoid symbols that collide with existing meanings (stars vs ratings). Clarity first, playfulness later if the metric (quality) matters. Measure outcomes (onboarding completion, activation), not only aesthetics (ch06, ch13).

## Mistakes
- Polishing rare screens while the paywall or first run is untested.
- Auditing without a goal; listing findings without priority.
- Treating design activity as progress when the real blocker is user contact or distribution.
- Launching publicly with no beta feedback and no tracking.
- Reading a single success story as a playbook.

## Checklist
- [ ] Is this screen on a conversion step with enough traffic to learn from?
- [ ] Goal stated before the audit; five lenses applied.
- [ ] Findings prioritised on impact versus effort.
- [ ] Timer set for audits and refreshes.
- [ ] Beta list, capacity screen and attribution question ready before launch.
- [ ] Rejected designs checked against the original goal.

## Connects To
ch13 (ROI), ch26 (minimum viable research), ch27 (recruiting, surveys), ch30 (prototype early), ch34 (structural audit), ch37 (first impression), ch38 (paywall, attribution), ch40 (QA, PRD).
