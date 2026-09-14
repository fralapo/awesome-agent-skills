# Come funzionano tecnicamente i motori generativi (RAG)

## Meccanismo generale RAG (Retrieval-Augmented Generation)

Pipeline tipica: **query → retrieval (ricerca su indice/web) → ranking/filtering candidati → sintesi risposta con LLM → citazione fonti**.

RAG permette al modello di recuperare informazioni dal web *prima* di generare la risposta, accedendo a info fresche e citando fonti in tempo reale invece di affidarsi solo alla conoscenza di training.

### Pipeline di citazione (generalizzata, es. Perplexity)

1. Query utente → retrieval di **5-10 fonti candidate** con hybrid search (keyword + semantic/vector).
2. Le candidate passano attraverso una **pipeline di filtro a più stadi** (report: 6 stadi) prima di sopravvivere come citazioni finali (3-4 sopravvissute).
3. I test che ogni fonte deve superare: **rilevanza rispetto alla domanda, freshness, chiarezza dell'entità, evidenza estraibile (extractable evidence), autorevolezza della fonte, attribuzione pulita (clean attribution)**.
4. Punto chiave: **il gap tra retrieval e citazione è dove falliscono la maggior parte delle content strategy** — essere recuperati non basta, bisogna sopravvivere al filtro.

## Differenze per piattaforma

### ChatGPT (Search)
- Favorisce **fonti di consenso**: Wikipedia (~7.8% delle citazioni), e cita siti concorrenti più spesso di Google (+11.1 punti percentuali rispetto a Google).
- Attinge sia a knowledge pre-trained sia a retrieval live via Bing/partnership.

### Perplexity
- Esegue **retrieval in tempo reale ad ogni query** (approccio più "search-native").
- Fortemente influenzato da **community discussion**: **Reddit ~46.7%** delle top citation di Perplexity.
- Hybrid search (keyword + vettoriale) con pipeline di filtro multi-stadio (vedi sopra).

### Google AI Overviews / AI Mode
- Sintetizza soprattutto da pagine **già presenti nell'indice/ranking di Google classico** — ma nel 2026 solo **38%** delle citazioni viene dal top-10 (in calo dal 76% di metà 2025) per via del **query fan-out**.
- **Query fan-out**: la query viene scomposta in sotto-query multiple; le pagine che compaiono ricorrentemente nei risultati delle sotto-query hanno più probabilità di citazione.
- AI Mode ha **zero-click rate del 93%** (il più alto tra le piattaforme).

### Copilot (Microsoft)
- Basato su Bing index + GPT; meno dati pubblici specifici sul suo pipeline di citazione rispetto a ChatGPT/Perplexity/Google.

### Claude / Gemini
- Meno documentazione pubblica granulare sul loro retrieval-per-citazione rispetto a ChatGPT/Perplexity; generalmente seguono lo stesso pattern RAG (retrieval + filtro + sintesi).

## Overlap tra piattaforme (dato chiave)

- Analisi di **680 milioni di citazioni**: solo **11%** dei domini è citato **sia** da ChatGPT **sia** da Perplexity.
- Implicazione: le strategie GEO **non sono trasferibili 1:1 tra motori** — bisogna testare/misurare per singola piattaforma (da qui il valore dei tool di AI-visibility multi-piattaforma, vedi file 05).

## Concentrazione della citazione (potere ai grandi domini)

- Studio aggregato (6 tra i maggiori citation-tracking study, ago 2024–apr 2026, 680M+ citazioni): il **top 1% dei domini citati (~12 siti)** — Wikipedia, Reddit, Forbes, Healthline, Investopedia, NYT, domini .gov/.edu grandi — cattura il **47%** di tutte le citazioni.
- Fattori di posizione dentro la pagina sorgente: **55%** delle citazioni AI Overview provengono dal **top 30%** del contenuto della pagina, **24%** dalla sezione centrale (30-60%), solo **21%** dal fondo pagina → mettere le risposte/fatti chiave in alto.

## Retrieval a livello di "chunk", non di pagina

- Gli LLM segmentano il contenuto in **chunk semantici**, li convertono in **embedding vettoriali**, li archiviano in un vector database, e recuperano i chunk più rilevanti per rispondere.
- Ogni chunk dovrebbe essere **autosufficiente** (comprensibile/citabile senza dover leggere il resto della pagina) — vedi file 04 per dettagli pratici su come scrivere per chunk.

## Fonti
- https://discoveredlabs.com/blog/ai-citation-patterns-how-chatgpt-claude-and-perplexity-choose-sources
- https://discoveredlabs.com/blog/chatgpt-claude-perplexity-and-google-ai-overviews-how-each-platform-cites-sources-differently
- https://authoritytech.io/blog/how-perplexity-selects-sources-algorithm-2026
- https://www.usegrowthos.com/blog/google-ai-overviews-vs-chatgpt-vs-perplexity
- https://ahrefs.com/blog/ai-overview-citations-top-10/
- https://ahrefs.com/blog/search-rankings-ai-citations/
- https://www.deltavdigital.com/resources/reports/ai-citation-study/
- https://everything-pr.com/ai-platform-citation-source-index-2026
- https://www.lumar.io/blog/best-practice/content-chunking-ai-extractability-geo-aeo-explainer/
