# Audit Pattern: Scoring Content Against GEO Cheatsheet

Use this procedure when asked to "audit" a piece of content for AI
visibility — a local file, pasted text, or a URL.

## Procedure

1. **Obtain the content.** If given a local file path, Read it. If given
   a URL, WebFetch it. If given pasted text, use it directly.
2. **Score category by category**, using the six categories in
   `cheatsheet.md` (Struttura contenuto, Structured data, Citabilità,
   Segnali di autorità, Tecnico / llms.txt, Note per piattaforma). For
   each category, go item by item and mark: ✅ pass / ⚠️ partial / ❌ fail,
   with a one-line reason citing what's present or missing in the content.
3. **Prioritize fixes by measured impact.** When multiple ❌/⚠️ items
   compete for attention, rank fixes using the Princeton paper's technique
   impact table from `chapters/01-definizioni-storia.md` (e.g. adding
   quotations/statistics ranks above lower-impact structural tweaks,
   keyword stuffing is never recommended — it measured negative).
4. **Output format** — a markdown table, one row per checklist item:

   | Categoria | Item | Esito | Motivo |
   |---|---|---|---|
   | Struttura contenuto | Answer-first nelle prime righe | ❌ | Il pezzo apre con storia aziendale, risposta diretta arriva al paragrafo 4 |

   Followed by a short "Prioritized fixes" numbered list (3-7 items,
   highest-impact first, each one actionable sentence — no prose report,
   no restating the whole table).
5. **Stay grounded.** Don't invent findings not visible in the content;
   don't cite statistics not already documented in this skill's chapters.
