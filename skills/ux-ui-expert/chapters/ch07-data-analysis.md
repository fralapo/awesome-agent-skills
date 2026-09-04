# Chapter 7: Data Analysis — AI, Deliverables, and Small Samples

## Core Idea
AI clustering tools are useful accelerants but unreliable on their own — human analysis first, then AI as a second-perspective layer, produces the best synthesis — and reporting small qualitative sample sizes correctly (words and raw numbers, never bare percentages) is essential to not mislead stakeholders.

## Frameworks Introduced
- **Human-Plus-AI Analysis Sequence**: (1) duplicate raw data (never touch the original), (2) do a hand-drawn affinity diagram/theme analysis first, (3) duplicate that result and run AI clustering (by keyword, then optionally further cluster by sentiment) on top of it, (4) compare AI output against your own themes for a different perspective. AI-only summarization is often unreliable (mixing up which participant said what) — always verify AI output, never take it at face value.
  - When to use: any qualitative synthesis session, especially when short on time but wanting a "different lens" on the data.
- **Small Sample Reporting Rule**: never report percentages for samples under ~30 (Central Limit Theorem rule of thumb) — use raw numbers and/or quantity words instead (none/a few/some/most/all), always including the raw number alongside the word since perceived meaning of "a few" varies by reader.
  - When to use: any qualitative study readout (typically 5-20 participants).
- **Prevalence / Severity / Frequency Triage**: three questions to prioritize a usability issue — Prevalence (how many users affected), Frequency (how often it occurs), Severity (impact if it occurs). All three "yes" = high-priority issue.
  - When to use: prioritizing findings across multiple observed issues, tying back to business/user implications rather than raw counts.

## Key Concepts
- **Affinity diagram**: grouping raw qualitative data points (quotes, observations) into emergent themes.
- **Central Limit Theorem (practitioner rule of thumb)**: statistical power for percentage-based claims generally needs n≥30.
- **Empathy Map**: a "user says/thinks/does/feels" deliverable often considered redundant with a user journey map, which draws on the same underlying research data but is typically more actionable and better visualized.

## Mental Models
- Treat AI analysis output the same way you'd treat a junior researcher's first pass: useful, fast, but requiring your verification before it goes to stakeholders.
- When reporting small samples, deliberately steer stakeholders away from numbers and toward the qualitative story — that's the actual value of small-N research.
- If a deliverable duplicates information already captured elsewhere (empathy map vs. journey map), cut it — don't create artifacts for their own sake.

## Anti-patterns
- **Reporting raw percentages on N<30**: e.g., "33% of users struggled" from 2-of-6 participants is statistically misleading.
- **Trusting AI summarization uncritically**: AI clustering/summarization tools can repeatedly misattribute quotes between participants when used unsupervised.
- **Making empathy maps because a template exists**: often duplicates journey-map data without adding decision-useful insight.
- **Skipping the "always copy before editing" habit**: risks corrupting or losing raw participant data during analysis.

## Key Takeaways
1. Do human analysis first, then layer AI clustering on top for a second perspective — never AI-only.
2. Always duplicate raw data before analyzing; never edit the original.
3. Never report bare percentages under n≈30; use quantity words + raw numbers together.
4. Prioritize findings using Prevalence × Frequency × Severity, not gut feel.
5. Consider skipping empathy maps when a user journey map already covers the same ground more usefully.

## Connects To
- **Ch5**: sample sizes set here interact with the study plan's participant/methodology section.
- **Ch8**: usability testing's n=5 rule extends the same small-sample logic to a specific method.
