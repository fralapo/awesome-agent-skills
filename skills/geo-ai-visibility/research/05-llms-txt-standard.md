# llms.txt e standard emergenti per siti "AI-readable"

## Cos'è llms.txt

- File **markdown semplice** posto nella root del dominio: `https://example.com/llms.txt`.
- Fornisce un **riassunto machine-readable strutturato** del sito: chi sei, cosa fai, quali sono le fonti di verità definitive — risparmiando all'agente AI la navigazione ed elaborazione di ogni singola pagina.
- Convenzione **emergente**, non uno standard W3C ufficiale (proposta originariamente da Jeremy Howard/Answer.AI, standard "bottom-up" adottato per consenso di community).

## Adozione (dati 2026)

- **>844.000 siti** hanno implementato llms.txt, inclusi **Stripe, Cloudflare, Vercel, Anthropic** e centinaia di aziende mid-market.
- **Aprile 2026**: Google integra un **check llms.txt direttamente in Chrome Lighthouse** — stesso framework che ha normalizzato HTTPS, mobile-first, Core Web Vitals → segnale forte che lo standard sta diventando mainstream/auditabile.
- Vantaggi di adozione: costo zero di hosting, deploy in pochi minuti, valore immediato per qualsiasi sistema AI che lo incontri.

## Cosa NON fa

- llms.txt permette solo **lettura** (agente legge il sito). Non abilita **azione** (es. verificare inventario in tempo reale, fare un ordine).
- Per l'azione servono standard diversi/complementari: **Model Context Protocol (MCP)** è indicato come la direzione per far "agire" gli agenti AI, non solo leggere.

## Altri standard/proposte nel panorama "agent-readable web" (2026)

Da un confronto comparativo (Platinum.ai): llms.txt vs **WebMCP** vs **SDF** vs **CAP**.
- **llms.txt**: riassunto statico, letto passivamente.
- **WebMCP**: esposizione di funzionalità del sito come tool MCP-style, per interazione attiva dell'agente.
- **SDF / CAP**: standard più recenti/di nicchia per structured discovery e capability advertisement (verificare dettagli aggiornati al momento di scrivere lo skill — nomi meno consolidati, in evoluzione).
- Framework più ampio citato: **ARO (Agent-Readable Optimization)** — combina llms.txt, "companion files" e verifica delle credenziali per costruire un web leggibile dagli agenti in modo affidabile (fonte: paper Zenodo).

## Buone pratiche pratiche per llms.txt (da guide pratiche)

- Struttura tipica: H1 col nome del sito/azienda, breve blockquote di descrizione, sezioni con link Markdown alle pagine/risorse più importanti (docs, pricing, API reference, blog).
- Mantenerlo **sincronizzato** con i contenuti reali (non un artefatto statico dimenticato).
- Complementare (non sostitutivo) a: sitemap.xml, robots.txt, schema.org markup — sono livelli diversi dello stesso obiettivo (rendere il sito leggibile a un consumatore non-umano).

## Fonti
- https://www.yotpo.com/blog/what-is-llms-txt/
- https://developer.chrome.com/docs/lighthouse/agentic-browsing/llms-txt
- https://www.platinum.ai/what-is-llms-txt
- https://www.platinum.ai/ai-agent-web-standards
- https://promptowl.ai/resources/how-ai-agents-should-read-your-site-llms-txt/
- https://zenodo.org/records/18817486
