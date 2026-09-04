# Cheatsheet — UX/UI Research & Leadership Expert

## Sample Size Quick Reference
| Method | Sample Size |
|---|---|
| Usability testing (per design) | 5 minimum ("magic number five" = ~80-85% of issues); recruit 6-8 for buffer |
| Card sort — moderated | 10-15 |
| Card sort — unmoderated | 20-30+ |
| Any percentage-based claim | n ≥ ~30 (Central Limit Theorem rule of thumb) |

## Small-Sample Quantity Words (pair with raw number always)
| Fraction (of 8) | Word | Fraction (of 20) | Word |
|---|---|---|---|
| 0/8 | None | 0/20 | None |
| 1-3/8 | A few | 1-4/20 | A few |
| 4/8 | Half | 5-8/20 | Several |
| 5-6/8 | Some | 9-11/20 | About half |
| 7/8 | Most | 12-16/20 | Some |
| 8/8 | All | 17-19/20 | Many/Most |
| — | — | 20/20 | All |

## Strategic vs. Tactical Research Map
| | Strategic (= Foundational = Generative) | Tactical (= Evaluative) |
|---|---|---|
| Focus | Big-picture, long-term, exploratory | Implementation, specific design |
| Timing | Before concepts exist | After a prototype/idea exists |
| Sub-types | — | Formative (pre-launch) / Summative (post-launch) |
| Use with leadership | Say "strategic" | Say "tactical" |

## Usability Issue Triage
Ask all three — all "yes" = high priority:
- **Prevalence**: how many users affected?
- **Frequency**: how often does it occur?
- **Severity**: how bad is the impact if it happens?

## Belmont Report — 5 Principles
1. Respect for Persons — autonomy, informed consent, debrief
2. Beneficence — do no harm, maximize benefit
3. Justice — fair distribution of costs/benefits
4. Fidelity and Responsibility — build trust, own repercussions
5. Integrity — honesty and accuracy, never fabricate data

## Manipulation vs. Coercion vs. Persuasion vs. Influence
| | Direction | Timeframe | Ethical? |
|---|---|---|---|
| Manipulation | One-sided, selfish | Short-term | Bad |
| Coercion | Forced | Short-term | Worst (unethical) |
| Persuasion | One-directional | Short-term | Neutral ("something you do") |
| Influence | Mutual, cooperative | Long-term | Best ("something you earn") |

## Goleman's Six Leadership Styles
Good defaults: **Affiliative** (build harmony), **Visionary** (rally around a goal), **Coaching** (develop people), **Democratic** (build consensus).
Situational only: **Coercive/Commanding**, **Pace-Setting**.

## Between-Subjects vs. Within-Subjects
| | Between-Subjects | Within-Subjects |
|---|---|---|
| Each participant sees | 1 condition | All conditions |
| Main risk | Individual differences | Order effects |
| Fix | Random assignment | Counterbalancing (n! orderings; avoid Latin Square) |
| Sample size need | Larger | Smaller |
| Comparison data | No | Yes |

## Card Sort: Open vs. Closed
- **Open**: no predefined categories → use to *build* new IA.
- **Closed**: predefined categories → use to *validate* existing IA.

## Communication Styles (diagonal pairs clash most)
Direct ↔ Considerate | Spirited ↔ Systematic

## UX vs. UI vs. CX
| | Scope | Example fix belongs here if... |
|---|---|---|
| UX | Perceptions/responses from using or anticipating a product | The task flow or interaction is confusing/frustrating |
| UI | Visible layer: visual design, layout, branding | The look, color, or layout is the problem |
| CX | Full journey: compare → buy → support | The gap spans multiple touchpoints (e.g., sales to support handoff) |

## UX Iceberg (bottom-up priority, top-down visibility)
1. Strategy (users, objectives) — base, do first
2. Functional specs / content requirements
3. Interface design (structure, navigation, IA)
4. Visual design — visible tip, ~10% of the work

## 5 UCD Design Principles
1. Design for your target audience
2. Account for the organization's goals
3. Make it easy to learn and use
4. Make it satisfying and pleasant
5. Prioritize the human experience above all

## ROI of UX — Quick Formula
Payback period = fix cost ÷ recovered daily/monthly loss.
Fixing post-development costs ~100x fixing pre/during-development.
Metrics to attach a UX fix to: conversion rate, abandonment/drop-off rate, support-desk call volume, training time, error rate, development time saved.

## Top-3 UX-Relevant Project Failure Causes
1. Badly defined requirements
2. Poor communication among customers, developers, and users
3. Stakeholder politics

## Double Diamond — 4 Phases
| Phase | Direction | Focus |
|---|---|---|
| Discover | Go wide | Problem space: qual + quant data, competitive analysis |
| Define | Go narrow | Synthesize, prioritize, t-shirt size |
| Develop | Go wide | Sketch multiple solution directions |
| Deliver | Go narrow | Test, iterate, cross-functional review, ship |

## Research Project Cycle — 6 Steps
1. Surface knowledge gap
2. Define the question
3. Define the research plan
4. Recruit + guided script
5. Facilitate
6. Synthesize + present

## User Flow Notation
| Symbol | Meaning |
|---|---|
| Circle | Start / end |
| Solid line | Preferred path |
| Dotted line | Alternative path |
| Diamond | Decision point |

## 7+1 Beginner UI Mistakes
1. Unplanned user flow (missing edge cases)
2. Overusing effects (shadows/gradients)
3. Poor spacing
4. Inconsistent components
5. Weak icon system
6. Redundant elements
7. Missing interactive feedback
+ Overdesigned charts (legibility lost)

## Semantic Color Convention
| Color | Meaning |
|---|---|
| Blue | Trust |
| Red | Danger / urgency |
| Yellow | Warning |
| Green | Success |

## Minimum Component State Set
Default → Hover → Active/Pressed → Disabled (+ Loading when relevant)
Inputs also need: Focus, Error, sometimes Warning

## Typography Quick Rule
1 typeface is enough. ~6 font sizes max for landing pages/websites; narrower range (rarely >24px) for dense dashboards. Tighten letter-spacing ~-2 to -3% and line-height ~110-120% on large headlines.

## Spacing Rule
Use a base-unit system (4px or 8px multiples) for all spacing values — keeps every measurement evenly divisible and consistent.

## Psychology Mechanisms — Quick Reference
| Mechanism | Effect | Use with caution when... |
|---|---|---|
| Cognitive overload | Too much info at once stresses the brain | Any dense screen |
| Processing fluency | Less/simpler often reads as higher quality | Comparing two working layouts |
| Color psychology | Red=alert, blue/green=calm | Choosing alert vs. background colors |
| Classical conditioning | Sound/haptic cues trigger involuntary checking | Designing notification tones |
| Positive reinforcement | Immediate reward increases repeat behavior | Any "like"/action feedback |
| Intermittent reinforcement | Unpredictable reward = strongest engagement driver | Feed refreshes — highest compulsive-use risk |
| Hedonic adaptation | Static experiences lose appeal over time | Planning content/feature refresh cadence |
| Dopamine-driven design | Reward mechanisms funnel toward "feel good → use more" | Any engagement-optimization decision — check user wellbeing tradeoff |
