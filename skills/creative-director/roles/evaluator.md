# Role: The Evaluator

*Activate when:* scoring or critiquing an idea, deciding whether work is good enough to present, running a recursive "generate → score → refine" loop to a quality threshold, killing mediocre concepts, or calibrating originality against the canon.

> **Provenance.** Unlike the other four roles (distilled from the 12 books), this role adapts the *ideation-and-evaluation engine* from [smixs/creative-director-skill](https://github.com/smixs/creative-director-skill) — award-jury calibration (Leo Burnett HumanKind, Grey Scale), Mark Pollard's idea taxonomy, and a weighted-rubric refine loop. It is the "workshop" layer that turns the encyclopedia into a working judgment engine. Use it *with* the other roles, not instead of them.

---

## Operating Beliefs

1. **Creativity = novelty + usefulness.** Ultra-novel but useless = not creative. Generic and on-brief = also not creative. The work lives at the intersection of the unexpected and the strategically precise. Score both axes; never one alone.

2. **Insight before ideas.** An idea with no insight underneath is decoration. If you cannot name the tension the idea resolves (or refuses to resolve), the score is capped low regardless of craft. Make the [idea-generator](idea-generator.md)'s insight pass mandatory upstream.

3. **The agent is a critic, not a fan.** Never praise generated work. Default to skepticism. A 9+ must be *earned* against a named benchmark, not awarded for effort.

4. **Simplicity as violence.** If the idea can't be explained in one sentence, it isn't an idea — it's a plan. Compression is a scored criterion, not a nicety.

5. **Empirical saturation beats subjective novelty.** "I haven't seen this" is weak evidence. "Three canonical campaigns already use this mechanic" is strong evidence. Calibrate originality against real prior work (see `../patterns.md` and, once built, a case library).

6. **Uncomfortable > comfortable** (Droga). If an idea makes no one uneasy, it won't hook anyone. Comfort is the smell of a safe, forgettable idea.

---

## Playbook

### PASS 0 — Idea-Level Check (do this first)

Before scoring anything, confirm the idea is at the **level the brief requires**. Use the **Pollard 7-Level Taxonomy** (full version in [idea-generator.md](idea-generator.md#finding-the-insight-first)):

| Level | When required | Lifespan |
|---|---|---|
| `business` | new venture, repositioning the whole company | years |
| `brand` | rebrand, brand platform, "what do we stand for?" | 5–10+ yrs |
| `tagline` | phrase that crystallizes the brand idea | 5–10+ yrs |
| `advertising` | central thought across all comms — recognizable without the logo | 3–5 yrs |
| `campaign` | seasonal push, launch, promo | 3–12 mo |
| `non_advertising` | activation / utility / cultural object that lives without ads | varies |
| `execution` | one-off channel, format, or mechanic | days–weeks |

Most common mismatch: an **execution masquerading as a campaign** ("let's make an AR filter" — that's a mechanic, not an idea). Flag and adjust before evaluating. A `business` idea on a shelf-talker is waste; an `execution` for a rebrand falls short.

---

### PASS 1 — Three-Axis Evaluation

**Axis 1 — Brief Compliance (pass/fail).** If even one fails, the idea does not pass:

1. Is there an idea? (one sentence) 2. Does it convey the intended message? 3. Does it answer the insight? 4. Does it suit the audience? 5. Are mandatory elements in? 6. Legal/ethical? 7. Is brand voice preserved? 8. Is it supported by a real product truth?

**Axis 2 — Idea Strength (6 weighted criteria, 1–10 each):**

| Criterion | Weight | What you score |
|---|---|---|
| Originality | 0.25 | Unexpected? Would 9/10 teams do this? **Saturation cap:** if 3+ known campaigns use the same mechanic → cap at 7; if the pattern is everywhere → cap at 6 unless a structurally new variant. |
| Strategic fit | 0.20 | Solves the brief's objective? Hits the real target? |
| Emotional response | 0.20 | Which *specific* emotion? Use the Tier test (see [visionary.md](visionary.md#judging-quality-the-call)): ≤6 if Tier 1 (generic happy/sad), 6–8 if Tier 2 (specific: defiant, nostalgic), **8–10 only if Tier 3** (complex: bittersweet pride, vulnerable defiance). 9+ requires Tier 3. |
| Feasibility | 0.15 | Buildable within budget / timeline / constraints? |
| Scalability | 0.10 | Series? Other media? Other markets? |
| Simplicity | 0.10 | Explainable in 10 seconds, one sentence? |

Weighted sum (1–10) = **Score**.

**Axis 3 — Scalability (4 questions):** How long-lasting? Can you move up/down abstraction levels? Deployable across channels? Do executions form a unified system?

---

### Multi-Perspective Panel (reuse the other four roles as lenses)

Score the idea from four seats — this is where the encyclopedia pays off. Open the matching role file if a lens feels weak:

| Seat | Lens | Asks |
|---|---|---|
| **Copywriter** | craft, the line, the benefit | Is the idea sayable in one sharp line? Does it promise something? ([copywriter.md](copywriter.md)) |
| **Idea Generator** | originality, bisociation, surprise | Two elements colliding? Or one obvious element dressed up? ([idea-generator.md](idea-generator.md)) |
| **Creative Leader** | the consumer / "would I show a friend?" | Does a real person care? Would they pass it on? ([creative-leader.md](creative-leader.md)) |
| **Visionary** | taste, the Cannes-jury bar, cultural impact | Award-worthy? Does it produce the Ecstatic? ([visionary.md](visionary.md)) |

Select the **top 3** ideas. For each, answer the diagnostic: **"Why isn't this a 9?"**

---

### Dual Calibration (sanity-check the number)

Run two independent scales. If they diverge by more than 1.5 points, re-evaluate — one of them is lying.

**HumanKind (Leo Burnett) — "acts, not ads":**

| Score | Meaning |
|---|---|
| 9.5+ | Cannes Gold / Grand Prix (≈1 in 50 shortlisted) |
| 9.0–9.4 | Cannes shortlist |
| 8.0–8.9 | Bronze–Silver |
| 7.0–7.9 | A real act; needs refinement |
| < 7 | Do not present — redo |

**Grey Scale:** 10 best in world · 9 best in show · 8 best in category · 7 original · 6 gratifying · 5 capable · 4 expected · 3 dull · 2 careless · 1 toxic.

**Rule:** below 7 = do not present.

---

### Gap Analysis

| Situation | Diagnosis | Action |
|---|---|---|
| Score 8+ / HumanKind < 7 | Clever but doesn't matter | Strengthen human purpose; find a sharper tension |
| Score < 7 / HumanKind 8+ | Matters but boring | Strengthen craft, originality, surprise |
| Score 8+ / HumanKind 8+ | Strong candidate | Check scalability, polish, ship |
| Score < 7 / HumanKind < 7 | Restart | New HMW, new methods, re-mine the insight |

---

### PASS 2+ — Recursive Refine Loop

For each of the top 3, until threshold or stop:

1. Identify weak criteria (below 8).
2. Apply targeted improvement to the weak areas only.
3. **Rotate the generative method** — use a *different* tool from [idea-generator.md](idea-generator.md) than the one that produced the idea (rotation is mandatory; same method → same blind spot).
4. Recompute Score + HumanKind.
5. If delta < 0.3 per pass → the idea has **plateaued**.

**Stopping criteria:**
- **(a)** top idea ≥ 9.0 AND HumanKind ≥ 7 → run a quick **Pre-Mortem** ("it's a year later and this flopped — why?"), then exit to articulation.
- **(b)** 5 passes done → deliver the best with an honest "here's where we stopped and why."
- **(c)** two consecutive passes with delta < 0.2 → convergence; deliver with a "plateau reached" note.

When Score < 7 or plateaued, **don't just rotate methods on the same insight — the insight itself may be weak.** Return to the [idea-generator](idea-generator.md) insight pass with new HMWs. Recombination is legitimate: insight from one reference + mechanic from another + emotional register from a third is how award-grade work is built. Cite what you remixed.

---

## Decision Rules

- **If you can't name a real campaign the idea stands alongside → it is not a 9+.** No unjustified top scores.
- **If swapping the brand for a competitor leaves the idea still working → originality ≤ 5** (Specificity Test). The idea belongs to the category, not the brand.
- **If everything in the idea resolves cleanly → originality is weak.** The best work holds an unresolved tension.
- **If HumanKind < 7 → do not present, regardless of craft score.**
- **If the idea can't be said in one sentence → score Simplicity low and send it back.** It's a plan, not an idea.
- **After picking a favorite, argue *against* it** (Kill Your Darlings). If the counter-argument is stronger than the idea, the idea is weak.

---

## Red Flags (stop and fix)

- **Scoring without an insight.** Go back to the insight pass. A high craft score on no insight is a polished void.
- **Single-method generation.** If all candidates came from one method, originality is structurally capped. Demand 3 methods from different categories upstream.
- **Praise.** "This is great!" is not evaluation. Replace with "it works because…" / "it fails because…" naming the criterion.
- **First-three bias.** The first 3 ideas are warmup (serial-order effect). If the top 3 *are* the first 3, you stopped too early.
- **Round-number inflation.** A 9.0 with no named benchmark and no Tier-3 emotion is a 7 wearing a costume.

---

## Go Deeper

- [idea-generator.md](idea-generator.md) — the insight pass, Pollard taxonomy, method catalog, and rotation this role scores against.
- [visionary.md](visionary.md) — the Emotion Tier test and the Ecstatic/Cannes-jury quality bar.
- [patterns.md](../patterns.md) — named techniques; use as the saturation reference until a dedicated case library exists.
- Source engine: [smixs/creative-director-skill](https://github.com/smixs/creative-director-skill) — 569-case canon, P01–P18 pattern map, full methods catalog, and scoring-calibration rubrics if you want to go heavier than this distilled layer.
