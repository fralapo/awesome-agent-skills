---
name: exercise-science-and-programming
description: "Exercise science and resistance-training programming for lifters and coaches: reasoning about evidence (average versus individual effects, study limits), mechanisms of hypertrophy and strength, weekly volume and landmarks (MEV, MAV, MRV), frequency, proximity to failure (RIR, RPE) and the contested effective-reps model, rep ranges, exercise selection and specificity, range of motion, rest and tempo, progression (linear, double, autoregulated, e1RM), periodization and deloads, fatigue, sleep and the overtraining debate, barbell mechanics and when form matters, novice versus advanced, strength versus size, cardio interference, and a checklist to judge training advice. Use when the user designs or critiques a lifting programme, asks how many sets, how often, how close to failure, whether to deload, why progress stalled, or whether a training claim is reliable. Separates consensus from contested positions; educational only, no supplement, drug or medical advice."
allowed-tools:
  - Read
  - Grep
argument-hint: [training question, programme, or chapter number]
---

# Exercise Science and Programming
**Chapters**: 12 | **Corpus**: ~80 theoretical transcripts | **Generated**: 2026-11-14

> Educational, not medical or coaching advice. This skill explains evidence and mechanisms of resistance training and ways to evaluate claims. It does not diagnose, prescribe an individual programme, or give medical, supplement or drug advice.

## Role and Boundaries

This skill **reasons about resistance training**: what evidence says and does not say, how to set volume, frequency and effort, how to progress and when to back off, how to read a stall, how to think about technique, and how to evaluate a claim. It gives mechanisms, defaults, trade-offs and checklists; the lifter or coach owns context and the final choice. Every chapter opens with an "educational, not medical or coaching advice" notice.

| This skill decides | This skill hands off |
|---|---|
| Programming variables (sets, reps, effort, frequency, rest, progression), periodization and deload logic, interpretation of training studies | Injury mechanisms, pain, rehabilitation, load tolerance of tissues, back pain -> `biomechanics-and-rehab-reasoning` |
| Whether a training claim is well supported, contested or speculative | Statistics, study design and scientific method in general -> `scientific-thinking` |
| Fatigue, sleep and overtraining as a *training* question | Diagnosis, medication, cardiovascular risk, eating disorders, performance-enhancing drugs, supplement protocols -> a qualified clinician (this skill gives none) |
| Habits, expectation setting, behaviour change in training | Motivation and persuasion -> `behavior-and-decision-science` |

**Stay in lane.** Figures are dated, context-bound snapshots from trials with limits (short, mostly untrained participants); many numbers are rules of thumb. Where a claim is unclear in source, the text says "unclear in source"; where it is not from these chapters, it says "general knowledge".

## Facts vs Positions

- **Consensus** is marked as such (for example: progressive overload; 10 or more hard sets per muscle weekly beat fewer; hard sets near failure; a wide rep range builds muscle).
- **Contested** items are written "(position)" or presented as Position A / B with evidence and counter-argument: the volume ceiling, going to failure, effective reps, periodization for size, scheduled versus reactive deloads, high versus low bar, the novice/advanced categories, posture and injury, the exact value of any single number.
- Every concept has **Thesis**, **Mechanism**, **Trade-off**, **Does not hold when**. Read the last one before recommending.

## How to Use This Skill

Diagnose before prescribing: goal (size, strength, both, health), training history, current weekly volume and frequency, how hard sets are, logs, sleep and stress, injuries, time available. Ask for the numbers, not the label.

| Task | Start with | Then |
|---|---|---|
| "Is this study / claim / influencer right?" | [ch12](chapters/ch12-evaluating-a-training-claim.md) | ch01 |
| Average result versus what works for me | [ch01](chapters/ch01-reasoning-about-training-evidence.md) | ch12 |
| Why does muscle or strength grow? | [ch02](chapters/ch02-mechanisms-of-hypertrophy-and-strength.md) | ch05 |
| How many sets per week? Landmarks, autoregulating volume | [ch03](chapters/ch03-volume.md) | ch04, ch09 |
| How often to train a muscle, split choice | [ch04](chapters/ch04-frequency.md) | ch03 |
| Reps, load, failure, RIR / RPE, effective reps | [ch05](chapters/ch05-intensity-proximity-to-failure-and-effective-reps.md) | ch07 |
| Exercise choice, variations, range of motion, mind-muscle | [ch06](chapters/ch06-exercise-selection-specificity-and-range-of-motion.md) | ch10 |
| No equipment or calisthenics: patterns, levers, adjusting difficulty | [ch06](chapters/ch06-exercise-selection-specificity-and-range-of-motion.md) (6.7) | ch07 (7.8), ch05 (5.5) |
| Rest times, tempo, adding weight, linear progression, e1RM, stalls | [ch07](chapters/ch07-rest-tempo-and-progression.md) | ch08, ch11 |
| Periodization, blocks, taper, when and how to deload | [ch08](chapters/ch08-periodization-and-deloads.md) | ch09 |
| Fatigue, sleep, overtraining, "CNS fatigue", monitoring load, weight versus fat and appetite (concepts) | [ch09](chapters/ch09-fatigue-recovery-sleep-and-overtraining.md) | ch08 |
| Deadlift / squat / bench mechanics, bar path, is "form" a myth | [ch10](chapters/ch10-mechanics-of-the-big-lifts-and-when-form-matters.md) | `biomechanics-and-rehab-reasoning` |
| Beginner versus advanced, strength versus size, cardio and lifting | [ch11](chapters/ch11-novices-advanced-trainees-strength-vs-size-and-cardio.md) | ch07, ch08 |
| Quick lookup | [cheatsheet.md](cheatsheet.md), [patterns.md](patterns.md), [glossary.md](glossary.md) | |

## The Core Principles (recurrence order)

1. **Average is not you.** Use the group result as a default, then test on yourself ([ch01](chapters/ch01-reasoning-about-training-evidence.md)).
2. **Hard sets near failure, enough of them.** Effort and volume work together; neither alone ([ch03](chapters/ch03-volume.md), [ch05](chapters/ch05-intensity-proximity-to-failure-and-effective-reps.md)).
3. **Progressive overload, logged.** What you cannot measure you cannot progress ([ch07](chapters/ch07-rest-tempo-and-progression.md)).
4. **Frequency is a tool for distributing volume and fatigue** ([ch04](chapters/ch04-frequency.md)).
5. **Wide ranges, narrow edges.** Many loads, rests and tempos work; the extremes (very light, very short rests, very slow) do not ([ch05](chapters/ch05-intensity-proximity-to-failure-and-effective-reps.md), [ch07](chapters/ch07-rest-tempo-and-progression.md)).
6. **Specificity is a spectrum; strength skills need specific practice** ([ch06](chapters/ch06-exercise-selection-specificity-and-range-of-motion.md)).
7. **Adaptation happens in recovery.** Read fatigue early, deload on signal or schedule ([ch08](chapters/ch08-periodization-and-deloads.md), [ch09](chapters/ch09-fatigue-recovery-sleep-and-overtraining.md)).
8. **Structure helps most when there is a date.** Periodization is clearest for peaking, murkier for size ([ch08](chapters/ch08-periodization-and-deloads.md)).
9. **Labels describe waiting time, not biology.** Let observed response set increments ([ch11](chapters/ch11-novices-advanced-trainees-strength-vs-size-and-cardio.md)).
10. **Technique is a skill; fear is not a method.** Efficiency and protection are different claims ([ch10](chapters/ch10-mechanics-of-the-big-lifts-and-when-form-matters.md)).
11. **Precise numbers on proxies deserve suspicion.** Use ranges and tests ([ch12](chapters/ch12-evaluating-a-training-claim.md)).
12. **Stay in scope.** No supplement, drug or medical protocols; refer out.

## Chapter Index

1. [Reasoning about training evidence](chapters/ch01-reasoning-about-training-evidence.md)
2. [Mechanisms of hypertrophy and strength](chapters/ch02-mechanisms-of-hypertrophy-and-strength.md)
3. [Volume](chapters/ch03-volume.md)
4. [Frequency](chapters/ch04-frequency.md)
5. [Intensity, proximity to failure and effective reps](chapters/ch05-intensity-proximity-to-failure-and-effective-reps.md)
6. [Exercise selection, specificity and range of motion](chapters/ch06-exercise-selection-specificity-and-range-of-motion.md)
7. [Rest, tempo and progression](chapters/ch07-rest-tempo-and-progression.md)
8. [Periodization and deloads](chapters/ch08-periodization-and-deloads.md)
9. [Fatigue, recovery, sleep and overtraining](chapters/ch09-fatigue-recovery-sleep-and-overtraining.md)
10. [Mechanics of the big lifts and when form matters](chapters/ch10-mechanics-of-the-big-lifts-and-when-form-matters.md)
11. [Novices, advanced trainees, strength vs size and cardio](chapters/ch11-novices-advanced-trainees-strength-vs-size-and-cardio.md)
12. [Evaluating a training claim](chapters/ch12-evaluating-a-training-claim.md)

## Topic Index

- **Autoregulation, RIR, RPE** -> ch05, ch07
- **Barbell mechanics, form** -> ch10
- **Bodyweight and calisthenics: movement patterns, leverage, variant ladders** -> ch06 (6.7), ch07 (7.8)
- **Body weight versus body fat, satiety, energy balance (concepts only)** -> ch09 (9.8)
- **Buffer from failure in skill and impact work** -> ch05 (5.5)
- **Cardio interference** -> ch11
- **CNS fatigue, overtraining** -> ch09
- **Deloads** -> ch08, ch09
- **Evaluating claims, study limits** -> ch01, ch12
- **Exercise selection, range of motion** -> ch06
- **Frequency, splits** -> ch04
- **Hypertrophy and strength mechanisms** -> ch02
- **Load and rep range, effective reps** -> ch05
- **Novice versus advanced** -> ch11
- **Periodization, tapering** -> ch08
- **Progression, e1RM, stalls** -> ch07, ch11
- **Rest intervals, tempo** -> ch07
- **Volume, MEV, MAV, MRV** -> ch03
- **Strength versus size** -> ch02, ch11

## Related Skills

- `biomechanics-and-rehab-reasoning`: injury mechanisms, pain, load tolerance of tissues and rehab reasoning; this skill stops where an individual injury or treatment begins.
- `scientific-thinking`: general reasoning about evidence, statistics and bias.
- `behavior-and-decision-science`: habits, motivation and behaviour change in training.

## Scope & Limits

Practical theory on resistance-training programming: volume, frequency, effort, rep ranges, exercise selection, rest, progression, periodization, fatigue, novice versus advanced, strength versus size and cardio interference. Not covered: diagnosis, injury treatment, medication, diet, calorie, macro and supplement protocols (only concepts about body weight and appetite appear in ch09), performance-enhancing drugs or sport-specific coaching. This skill summarises practitioner commentary: some chapters report positions held by one coaching camp and each is paired with its objection. Evidence figures are single-study or rule-of-thumb snapshots and may be superseded. The skill gives no medical or safety guarantee; anyone with symptoms should see a qualified clinician.
