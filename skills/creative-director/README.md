# creative-director

A creative-director "operating system" skill, distilled from **16 books** on advertising, creative leadership, idea generation, taste, typography, visual literacy, and information design. Built with [book-to-skill](https://github.com/virgiliojr94/book-to-skill) + a custom multi-role synthesis.

## What it does

When invoked, it acts as a **router**: a small always-loaded `SKILL.md` sends the agent to **one of five role toolkits**, and only that role (plus, if needed, a specific book digest) is loaded into context. A typical task costs a few thousand tokens instead of the 1.28M-token source corpus.

### The five roles

| Role | Activates for | Source |
|---|---|---|
| **Copywriter** | headlines, body copy, taglines, campaigns, briefs, positioning | Ogilvy on Advertising · Guts |
| **Idea Generator** | brainstorming, creative angles, wit, persuasion psychology, insight mining | Creative Mischief · A Smile in the Mind · Predictably Irrational + insight layer¹ |
| **Creative Leader** | feedback, 1:1s, hiring, motivation, conflict, culture, maker→manager transition | Fired Up · The Making of a Manager · Tribal Leadership · Crucial Conversations · Herding Tigers |
| **Visionary** | taste, vision, judging quality, "the eye", typography, information/data-viz design, creative practice | The Creative Act · The Eye · Steve Jobs · A Primer of Visual Literacy · Envisioning Information · Stop Stealing Sheep |
| **Evaluator** | scoring an idea, refine-to-threshold loop, killing mediocrity, award-jury calibration | engine layer¹ |

¹ The Evaluator role and the insight/Pollard/emotion-tier layers are adapted from [smixs/creative-director-skill](https://github.com/smixs/creative-director-skill) (HumanKind/Grey calibration, Pollard idea taxonomy, weighted scoring loop) — not from the 16 books, and marked as such wherever they appear.

## Structure

```
creative-director/
├── SKILL.md          # router: task → role, topic & book index
├── roles/            # 5 synthesized toolkits (4 from books + 1 evaluation engine)
├── books/            # 16 per-book digests (deepest layer, on-demand)
├── references/       # ted-talks.md — 23 designer/creative TED talks distilled
├── glossary.md       # ~140 named frameworks/terms
├── patterns.md       # ~50 concrete techniques, grouped by use
└── cheatsheet.md     # decision rules + quick-reference tables
```

## Usage

```
/creative-director write a headline for a premium coffee brand
/creative-director how do I give hard feedback on a junior's concept
/creative-director help me develop my eye
/creative-director score this campaign idea and tell me if it's good enough to present
/creative-director find the insight before we brainstorm this brief
/creative-director what does Ogilvy say about long copy
```

Read **one** role per task; the router suggests both when a task straddles two (e.g. a campaign = idea-generator + copywriter).

## Notes

- *Tested Advertising Methods* (Caples) was in the source folder but shipped as a scanned image-only PDF — no extractable text — so it is **not** included. OCR the file and fold it into the Copywriter role to add it.
- Source books are not redistributed; this skill contains only synthesized structure (frameworks, principles, techniques), never raw book text.
- Two layers are **not** from the 16 books, and are attributed wherever they appear: the **Evaluator** role + insight/scoring layers (adapted from [smixs/creative-director-skill](https://github.com/smixs/creative-director-skill)), and `references/ted-talks.md` (23 public designer/creative TED talks, distilled and grouped by role).
