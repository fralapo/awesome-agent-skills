---
name: biomechanics-and-rehab-reasoning
description: "Mechanisms and reasoning for musculoskeletal rehab and lifting claims, educational only: clinical reasoning (pre-test probability, sensitivity, specificity, likelihood ratios, limits of special tests, reading studies), pain science (nociception, central sensitisation, nociplastic pain, biopsychosocial model, red and yellow flags), biomechanics basics (kinetics, torque, joints, spine, gait), load and capacity (Goldilocks, envelope of function, healing phases, tendons), regional functional anatomy, squat and deadlift mechanics, imaging and passive modalities, posture, feet and mobility myths. Use when the user asks why a rehab, posture, imaging, butt wink, depth or exercise-form claim does or does not hold, how to judge a test or a study, or how pain and load relate. Gives no diagnosis, treatment plan, dose or prescribed exercise; reports counter-arguments."
allowed-tools:
  - Read
  - Grep
argument-hint: [claim, mechanism, study, or chapter number]
---

# Biomechanics and Rehab Reasoning
**Chapters**: 10 | **Corpus**: ~68 theoretical transcripts on rehab reasoning, pain science, anatomy and lifting biomechanics | **Generated**: 2026-11-14

> Educational, not medical advice. This skill explains mechanisms and ways to evaluate claims. It does not diagnose, does not give an individual treatment plan, does not give a therapeutic dose and does not prescribe an exercise as therapy for any condition.

## Role and Boundaries

This skill **explains how musculoskeletal and lifting claims are reasoned about**: how to update a probability with a test, what pain science says about pain and tissue, how load and capacity relate, what a region's anatomy predicts, where lifting mechanics are disputed, and how to judge a rehab, posture or imaging claim. It gives mechanisms, positions with their counter-arguments, and a checklist.

| This skill decides | This skill hands off |
|---|---|
| How to read test accuracy, probability, studies and guidelines | Statistics, causal inference and cognitive bias in general -> `scientific-thinking` |
| How pain, beliefs and context interact; what flags mean | Any individual assessment, diagnosis or care -> a qualified clinician |
| Mechanisms of load, adaptation and healing; the contested positions | Training dose, programming, progression, periodisation, hypertrophy and strength science -> `exercise-science-and-programming` |
| Lifting mechanics (squat, deadlift, depth, spine) as reasoning, with the disagreements | Coaching a person's technique -> a qualified coach |
| How to judge posture, foot, imaging and "myth" claims | Psychology of behaviour change -> `behavior-and-decision-science` |

**Stay in lane.** Chapters hold practitioner theory, not benchmarks. Figures (prevalence, test accuracy, timelines) are dated, context-bound snapshots drawn from single studies or rules of thumb; many come from observational data. Where a point is unverified or unclear it is marked "unclear in source" or "general knowledge" (not from the distilled material). If a reader describes symptoms, the right reply is the mechanism plus advice to see a qualified clinician, and urgent care for red-flag situations (ch03).

## Facts vs Positions

- **Mechanism / fact**: how likelihood ratios change odds, what torque is, how the plantar fascia raises the arch, what the stages of disc herniation are.
- **Position**: written as "(position)" or "In this model": for example "pain is never meaningless", "movement quality predicts injury", "posture does not predict pain", "avoid ice in early inflammation", "retrain movements, not muscles". Each carries its counter-argument.
- Every concept in the chapters has fields **Thesis**, **Mechanism**, **Trade-off** or **Counter-argument**, and **Does not hold when**. Read the last one before applying: if the limit applies, drop the rule.

## How to Use This Skill

Clarify the claim first: what is asserted, in whom, based on what comparison. Then pick the chapter.

| Task | Start with | Then |
|---|---|---|
| "Does this test prove it?", likelihood ratio, sensitivity, base rate | [ch01](chapters/ch01-clinical-reasoning-and-evidence.md) | ch08, ch10 |
| Reading a study or a headline finding | [ch01](chapters/ch01-clinical-reasoning-and-evidence.md) | ch10 |
| Why does pain persist? Central sensitisation, nociplastic pain, nocebo | [ch02](chapters/ch02-pain-science.md) | ch03 |
| Biopsychosocial frame, red flags, yellow flags, what guidelines agree on | [ch03](chapters/ch03-biopsychosocial-flags-and-guidelines.md) | ch02, ch08 |
| Torque, levers, joints, spine, gait basics | [ch04](chapters/ch04-biomechanics-basics.md) | ch06, ch07 |
| Overload, "too much too soon", healing time, tendon pain, stretching | [ch05](chapters/ch05-load-capacity-and-healing.md) | ch10 |
| Why the shoulder dislocates, what the ACL restrains, windlass, disc herniation stages | [ch06](chapters/ch06-regional-functional-anatomy.md) | ch04, ch08 |
| Squat depth, butt wink, rounded back in the deadlift, neutral spine | [ch07](chapters/ch07-lifting-biomechanics.md) | ch09, ch04 |
| MRI findings, "bone on bone", ultrasound therapy | [ch08](chapters/ch08-imaging-and-passive-modalities.md) | ch01, ch03 |
| Posture, flat feet, anterior pelvic tilt, "does mechanics matter?" | [ch09](chapters/ch09-posture-mobility-and-when-mechanics-matter.md) | ch05, ch07 |
| A claim to evaluate, myths, checklist | [ch10](chapters/ch10-myths-and-claim-checklist.md) | ch01 |
| Quick lookup | [cheatsheet.md](cheatsheet.md), [patterns.md](patterns.md), [glossary.md](glossary.md) | |

## The Core Principles (recurrence order)

1. **Probability, not verdict.** A test revises a prior; it helps only if it can cross a decision threshold.
2. **Findings are not causes.** Structural and postural findings are common without pain; association is not direction.
3. **Pain is an output, not a damage meter.** It protects, learns, and is shaped by context, beliefs and stress.
4. **Words are exposure.** Structural labels and scans can raise threat; communication can lower it.
5. **Breadth is the point of the biopsychosocial frame.** Biology, mind and context each offer something to work on.
6. **Load versus capacity.** Too little, too much too soon, and a moving "just right".
7. **Tissues adapt.** The same adaptation explains why "faults" are often harmless and why graded exposure works.
8. **Specificity matters.** To tolerate a task the tissue is eventually exposed to something like it.
9. **Anatomy predicts failure sites.** Mobility costs stability; the ligament, lip or muscle that buys it back shows where problems occur.
10. **Mechanics explains load, rarely predicts pain.** Levers and moment arms show how load reaches tissue; static features seldom predict symptoms.
11. **Passive is not wrong, but ask for the active ingredient.** Context effects are real; dependency and opportunity cost are the issues.
12. **Always state the counter-argument.** If a claim cannot survive its best objection, hold it loosely.

## Chapter Index

1. [Clinical reasoning and evidence](chapters/ch01-clinical-reasoning-and-evidence.md)
2. [Pain science](chapters/ch02-pain-science.md)
3. [Biopsychosocial model, flags and guideline common ground](chapters/ch03-biopsychosocial-flags-and-guidelines.md)
4. [Biomechanics basics](chapters/ch04-biomechanics-basics.md)
5. [Load, capacity, healing and tendons](chapters/ch05-load-capacity-and-healing.md)
6. [Regional functional anatomy](chapters/ch06-regional-functional-anatomy.md)
7. [Lifting biomechanics](chapters/ch07-lifting-biomechanics.md)
8. [Imaging and passive modalities](chapters/ch08-imaging-and-passive-modalities.md)
9. [Posture, mobility and when mechanics matter](chapters/ch09-posture-mobility-and-when-mechanics-matter.md)
10. [Myths and a claim checklist](chapters/ch10-myths-and-claim-checklist.md)

## Topic Index

- **Base rate, pre-test probability** -> ch01
- **Biceps and supination** -> ch06
- **Bone density and loading** -> ch05
- **Butt wink** -> ch07
- **Central sensitisation, nociplastic pain** -> ch02
- **Disc herniation stages** -> ch06, ch08
- **Envelope of function, Goldilocks load** -> ch05
- **Flat feet, pronation, windlass** -> ch06, ch09
- **Gait cycle** -> ch04
- **Healing phases, ice and anti-inflammatories** -> ch05
- **Imaging, MRI findings, "bone on bone"** -> ch08
- **Knee ligaments** -> ch06
- **Likelihood ratio, sensitivity, specificity** -> ch01
- **Neutral zone, spinal flexion under load** -> ch07, ch04
- **Posture and pain, anterior pelvic tilt** -> ch09
- **Red and yellow flags, guidelines** -> ch03
- **Rotator cuff and abduction** -> ch06
- **Special tests, test clusters** -> ch01
- **Squat depth** -> ch07
- **Static vs dynamic stretching** -> ch05, ch09
- **Tendinopathy** -> ch05
- **Therapeutic ultrasound** -> ch08
- **Torque, moment arm** -> ch04, ch07

## Related Skills

- `exercise-science-and-programming`: dose, progression, programming and the science of adaptation; this skill stops where a number or a plan would begin.
- `scientific-thinking`: general reasoning about evidence, statistics and bias.
- `behavior-and-decision-science`: biases and habit change relevant to how people hold beliefs about their body.

## Scope & Limits

Practical theory on clinical reasoning, pain science, biomechanics, load and healing, regional anatomy, lifting mechanics, imaging, passive modalities and rehab myths. Not covered: diagnosis, treatment plans, therapeutic doses, medication, surgery decisions, nutrition or sport-specific coaching. This skill summarises practitioner commentary: some chapters report positions held by one camp (movement-based clinicians, pain-science clinicians, lifting-biomechanics researchers) and each is paired with its objection. Evidence figures are single-study or rule-of-thumb snapshots and may be superseded. The skill gives no medical, legal or safety guarantee; anyone with symptoms should see a qualified clinician.
