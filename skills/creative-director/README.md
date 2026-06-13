# creative-director

A creative-director "operating system" skill, distilled from **12 books** on advertising, creative leadership, idea generation, and taste. Built with [book-to-skill](https://github.com/virgiliojr94/book-to-skill) + a custom multi-role synthesis.

## What it does

When invoked, it acts as a **router**: a small always-loaded `SKILL.md` sends the agent to **one of four role toolkits**, and only that role (plus, if needed, a specific book digest) is loaded into context. A typical task costs a few thousand tokens instead of the 1.28M-token source corpus.

### The four roles

| Role | Activates for | Source books |
|---|---|---|
| **Copywriter** | headlines, body copy, taglines, campaigns, briefs, positioning | Ogilvy on Advertising · Guts |
| **Idea Generator** | brainstorming, creative angles, wit, persuasion psychology | Creative Mischief · A Smile in the Mind · Predictably Irrational |
| **Creative Leader** | feedback, 1:1s, hiring, motivation, conflict, culture | Fired Up · The Making of a Manager · Tribal Leadership · Crucial Conversations |
| **Visionary** | taste, vision, judging quality, "the eye", creative practice | The Creative Act · The Eye · Steve Jobs |

## Structure

```
creative-director/
├── SKILL.md          # router: task → role, topic & book index
├── roles/            # 4 synthesized toolkits (one loads per task)
├── books/            # 12 per-book digests (deepest layer, on-demand)
├── glossary.md       # ~60 named frameworks/terms
├── patterns.md       # ~50 concrete techniques, grouped by use
└── cheatsheet.md     # decision rules + quick-reference tables
```

## Usage

```
/creative-director write a headline for a premium coffee brand
/creative-director how do I give hard feedback on a junior's concept
/creative-director help me develop my eye
/creative-director what does Ogilvy say about long copy
```

Read **one** role per task; the router suggests both when a task straddles two (e.g. a campaign = idea-generator + copywriter).

## Notes

- *Tested Advertising Methods* (Caples) was in the source folder but shipped as a scanned image-only PDF — no extractable text — so it is **not** included. OCR the file and fold it into the Copywriter role to add it.
- Source books are not redistributed; this skill contains only synthesized structure (frameworks, principles, techniques), never raw book text.
