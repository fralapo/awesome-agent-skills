# Chapter 2: Come Funzionano Tecnicamente i Motori Generativi (RAG)

## Core Idea
Ogni motore generativo (ChatGPT, Perplexity, Google AI Overviews/AI Mode, Copilot, Gemini) segue lo stesso pattern architetturale di base — Retrieval-Augmented Generation (RAG): query → retrieval → ranking/filtering dei candidati → sintesi della risposta con l'LLM → citazione delle fonti — ma ogni piattaforma implementa retrieval, ranking e selezione delle citazioni in modo sufficientemente diverso da rendere le strategie di ottimizzazione non trasferibili 1:1 da un motore all'altro.

## Il meccanismo generale RAG

- **Pipeline tipica**: query utente → retrieval (ricerca su indice/web) → ranking/filtering dei candidati → sintesi risposta con LLM → citazione fonti. RAG permette al modello di recuperare informazioni dal web prima di generare la risposta, accedendo a info fresche e citando fonti in tempo reale invece di affidarsi solo alla conoscenza di training. (fonte: research/03-motori-generativi-tecnico.md)
- **Pipeline di citazione generalizzata (es. Perplexity)**: (1) la query utente genera un retrieval di **5-10 fonti candidate** con hybrid search (keyword + semantic/vector); (2) le candidate passano attraverso una pipeline di filtro a più stadi (report: **6 stadi**) prima di sopravvivere come citazioni finali (**3-4 sopravvissute**); (3) ogni fonte deve superare test di rilevanza rispetto alla domanda, freshness, chiarezza dell'entità, evidenza estraibile (extractable evidence), autorevolezza della fonte, attribuzione pulita (clean attribution). Il gap tra retrieval e citazione è dove falliscono la maggior parte delle content strategy — essere recuperati non basta, bisogna sopravvivere al filtro. (fonte: research/03-motori-generativi-tecnico.md)
- **Retrieval a livello di chunk, non di pagina**: gli LLM segmentano il contenuto in chunk semantici, li convertono in embedding vettoriali, li archiviano in un vector database, e recuperano i chunk più rilevanti per rispondere. Ogni chunk dovrebbe essere autosufficiente (comprensibile/citabile senza dover leggere il resto della pagina). (fonte: research/03-motori-generativi-tecnico.md)

## Motore per motore

### ChatGPT (Search)
- **Favorisce fonti di consenso**: Wikipedia (~**7,8%** delle citazioni), e cita siti concorrenti più spesso di Google (**+11,1 punti percentuali** rispetto a Google). (fonte: research/03-motori-generativi-tecnico.md)
- **Retrieval ibrido**: attinge sia a knowledge pre-trained sia a retrieval live via Bing/partnership. (fonte: research/03-motori-generativi-tecnico.md)

### Perplexity
- **Retrieval in tempo reale ad ogni query** — l'approccio più "search-native" tra le piattaforme analizzate. (fonte: research/03-motori-generativi-tecnico.md)
- **Fortemente influenzato dalla community discussion**: Reddit copre circa il **46,7%** delle top citation di Perplexity. (fonte: research/03-motori-generativi-tecnico.md)
- **Hybrid search** (keyword + vettoriale) con la pipeline di filtro multi-stadio descritta sopra (6 stadi, 5-10 candidate → 3-4 citazioni finali). (fonte: research/03-motori-generativi-tecnico.md)

### Google AI Overviews / AI Mode
- **Sintetizza soprattutto da pagine già presenti nell'indice/ranking di Google classico** — ma nel 2026 solo il **38%** delle citazioni viene dal top-10 (in calo dal 76% di metà 2025) a causa del query fan-out. (fonte: research/03-motori-generativi-tecnico.md)
- **Query fan-out**: la query viene scomposta in sotto-query multiple; le pagine che compaiono ricorrentemente nei risultati delle sotto-query hanno più probabilità di citazione. (fonte: research/03-motori-generativi-tecnico.md)
- **AI Mode ha uno zero-click rate del 93%** — il più alto tra le piattaforme analizzate. (fonte: research/03-motori-generativi-tecnico.md)

### Copilot (Microsoft)
- **Basato su Bing index + GPT**; meno dati pubblici specifici sul suo pipeline di citazione rispetto a ChatGPT/Perplexity/Google. (fonte: research/03-motori-generativi-tecnico.md)

### Claude / Gemini
- **Meno documentazione pubblica granulare** sul loro retrieval-per-citazione rispetto a ChatGPT/Perplexity/Google; generalmente seguono lo stesso pattern RAG (retrieval + filtro + sintesi). (fonte: research/03-motori-generativi-tecnico.md)

## Divergenza tra piattaforme

- **Overlap tra piattaforme**: un'analisi di **680 milioni di citazioni** mostra che solo l'**11%** dei domini è citato sia da ChatGPT sia da Perplexity. Implicazione: le strategie GEO non sono trasferibili 1:1 tra motori — bisogna testare/misurare per singola piattaforma, da qui il valore dei tool di AI-visibility multi-piattaforma. Nessuna ottimizzazione su un solo canale è sufficiente. (fonte: research/03-motori-generativi-tecnico.md)
- **Concentrazione della citazione**: uno studio aggregato (6 tra i maggiori citation-tracking study, ago 2024–apr 2026, 680M+ citazioni) mostra che il **top 1% dei domini citati (~12 siti)** — Wikipedia, Reddit, Forbes, Healthline, Investopedia, NYT, domini .gov/.edu grandi — cattura il **47%** di tutte le citazioni. (fonte: research/03-motori-generativi-tecnico.md)
- **Posizione del contenuto nella pagina sorgente conta**: il **55%** delle citazioni AI Overview proviene dal top 30% del contenuto della pagina, il **24%** dalla sezione centrale (30-60%), solo il **21%** dal fondo pagina — mettere le risposte/fatti chiave in alto. (fonte: research/03-motori-generativi-tecnico.md)

## Key Takeaways
1. Tutti i motori generativi condividono lo stesso scheletro RAG (retrieval → filtro/ranking → sintesi → citazione), ma da 5-10 fonti candidate recuperate sopravvivono solo 3-4 citazioni finali dopo il filtro a più stadi (fonte: research/03-motori-generativi-tecnico.md).
2. L'unità recuperata e citata è il chunk semantico autosufficiente, non la pagina intera — coerente con quanto visto in Chapter 1 sulla differenza strutturale GEO vs SEO.
3. Ogni piattaforma pesa fonti diverse: ChatGPT favorisce fonti di consenso (Wikipedia ~7,8%) e concorrenti (+11,1pp vs Google); Perplexity è fortemente Reddit-influenced (~46,7%); Google AI Overviews dipende sempre meno dal top-10 classico (38% nel 2026, giù dal 76%) per via del query fan-out; AI Mode ha il più alto zero-click rate (93%).
4. Solo l'11% dei domini è citato sia da ChatGPT sia da Perplexity su 680M+ citazioni analizzate: nessuna strategia single-platform è sufficiente, serve misurare e ottimizzare per ciascun motore.
5. Il potere di citazione resta concentrato: il top 1% dei domini (~12 siti) cattura il 47% di tutte le citazioni, e dentro la pagina sorgente il 55% delle citazioni proviene dal primo 30% del contenuto.

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
