# GEO vs SEO: differenze chiave

## Modello mentale di base

- **SEO**: ottimizzi per **rankare** in una lista di link cliccabili → l'utente clicca → traffico sul sito.
- **GEO**: ottimizzi per essere **selezionato come fonte/passaggio** dentro una risposta sintetizzata unica → spesso zero click, il valore è la citazione/menzione stessa (brand exposure), non il traffico diretto.

Frase chiave da più fonti: *"Gli LLM non rankano pagine — selezionano passaggi, riusano evidenze, e citano ciò che li aiuta a rispondere con sicurezza."*

## Differenze strutturali

| Dimensione | SEO tradizionale | GEO |
|---|---|---|
| Output per l'utente | Lista di 10 link (SERP) | Risposta sintetica unica, multi-fonte |
| Unità di ottimizzazione | Pagina intera (title, meta, backlink) | **Chunk/passaggio semantico** dentro la pagina |
| Segnali principali | Keyword, backlink, metadata, PageRank | Fact density, structured data, entity relationships, citabilità |
| Query tipiche | Keyword brevi, navigazionali | **Conversazionali**, multi-turno, informazionali/comparative |
| Metrica di successo | Ranking position, CTR, traffico | Frequenza citazione/menzione, share of voice, sentiment nella risposta |
| Click-through | Centrale | Spesso assente (zero-click) — la "vittoria" è essere menzionati anche senza click |
| Backlink | Segnale di autorità primario | Secondario; contano di più **entity co-occurrence** e menzioni non linkate (unlinked mentions) |
| Ranking multiplo | 1 pagina = 1 posizione | 1 risposta può citare 3-10 fonti diverse contemporaneamente (nessuna "posizione 1" esclusiva) |
| Ciclo di feedback | Google Search Console, rank tracker | Tool AI-visibility (Profound, Peec, Otterly...) — nuova categoria, no standard consolidato |

## Cosa resta uguale (fondamenta condivise)

- Autorevolezza, chiarezza, struttura e allineamento con l'intento utente contano in entrambi.
- Ma il modo in cui questi segnali vengono "letti" cambia: SEO li legge via backlink/CTR, i motori generativi li leggono via **entity recognition** e coerenza semantica.
- Una base SEO tecnica solida (velocità, crawlability, heading puliti, no blocchi robots.txt su crawler AI) resta prerequisito per GEO — GEO si costruisce *sopra* SEO, non lo sostituisce.

## Perché "ranking bene su Google" non garantisce visibilità AI

- Google AI Overviews sintetizza (in parte) dalle pagine già indicizzate/rankate da Google classico, MA con il meccanismo di **query fan-out** (la query originale viene spezzata in più sotto-query, e vengono citate le pagine che compaiono più spesso nei risultati delle sotto-query) solo il **38% delle citazioni AI Overview** proviene oggi da pagine nel top-10 Google (dato 2026, in forte calo dal 76% di metà 2025).
- ChatGPT Search e Perplexity hanno pipeline di retrieval **indipendenti** da Google: solo l'**11% dei domini** è citato sia da ChatGPT sia da Perplexity (su 680M+ citazioni analizzate) → serve ottimizzare per ogni motore separatamente, non basta un solo canale.

## Query fan-out (Google) — concetto chiave 2026

- La query utente non viene trattata come singola ricerca: Google la scompone in **sotto-query correlate**, esegue ricerche multiple, e sintetizza. Le pagine che appaiono ricorrentemente in più sotto-query hanno più probabilità di essere citate nell'AI Overview.
- Implicazione pratica: bisogna coprire un **topic cluster ampio** (tutte le sotto-domande collegate al tema), non solo la keyword principale.

## Brand mention vs citazione linkata

- Nel contesto commerciale reale, ciò che conta di più spesso è la **menzione del brand** (l'AI raccomanda l'azienda per nome), non necessariamente un link cliccabile.
- Le menzioni **senza link** vanno comunque trattate come segnale di citazione: contribuiscono comunque alla visibilità del brand nelle risposte AI.
- Segnale di **co-occurrence**: il nome del brand che appare nello stesso paragrafo/contesto delle keyword di categoria su siti terzi autorevoli è ciò che "dice" al modello che il brand appartiene a quella categoria.

## Fonti
- https://writesonic.com/blog/geo-vs-seo
- https://www.contentful.com/blog/generative-engine-optimization-seo/
- https://gofishdigital.com/blog/seo-vs-geo/
- https://www.within.co/blog/generative-engine-optimization/
- https://ahrefs.com/blog/ai-overview-citations-top-10/
- https://ahrefs.com/blog/search-rankings-ai-citations/
- https://discoveredlabs.com/blog/ai-citation-patterns-how-chatgpt-claude-and-perplexity-choose-sources
