# Audit Pattern: Scoring Content Against the GEO Cheatsheet

Use this procedure when asked to "audit" a piece of content for AI
visibility — a local file, pasted text, or a URL.

## Procedure

1. **Obtain the content.** If given a local file path, Read it. If given
   a URL, WebFetch it. If given pasted text, use it directly.
2. **Score category by category**, using the seven categories in
   [cheatsheet.md](cheatsheet.md) (Content structure, Structured data,
   Citability, Authority signals, Entity and local business,
   Technical / llms.txt, Per-platform notes). Score "Entity and local
   business" only when the subject is a business site (agency, studio,
   local services). For each category, go item by item and mark:
   ✅ pass / ⚠️ partial / ❌ fail, with a one-line reason citing what is
   present or missing in the content.
3. **Prioritize fixes by measured impact.** When multiple ❌/⚠️ items
   compete for attention, rank fixes using the Princeton paper's technique
   impact table from
   [chapters/ch01-definitions-and-history.md](chapters/ch01-definitions-and-history.md)
   (e.g. adding quotations/statistics ranks above lower-impact structural
   tweaks; keyword stuffing is never recommended — it measured negative).
4. **Output format** — a markdown table, one row per checklist item:

   | Category | Item | Outcome | Reason |
   |---|---|---|---|
   | Content structure | Answer-first in the opening lines | ❌ | The piece opens with company history; the direct answer arrives in paragraph 4 |

   Followed by a short "Prioritized fixes" numbered list (3-7 items,
   highest-impact first, each one actionable sentence — no prose report,
   no restating the whole table).
5. **Stay grounded.** Don't invent findings not visible in the content;
   don't cite statistics not already documented in this skill's chapters.

## Variant: "why does the AI recommend my competitor?"

When the question is why an AI assistant recommends another business
instead of the user's, run the competitor gap analysis in
[chapters/ch08-entity-geo-for-local-service-businesses.md](chapters/ch08-entity-geo-for-local-service-businesses.md)
instead of a single-page audit: list the "service + city" queries, find
which competitor page wins each one, compare it with the user's
equivalent page, and output the Query / Competitor page / Own page /
Gap / Priority table, with the vertical niche where the user is
strongest marked 🟢 as the opportunity.
