# Fattori di ottimizzazione concreti

## Ranking dei fattori (da studio aggregato 54 esperimenti/paper/case study, 23 fattori)

Fonte: digitalapplied.com — sintesi di 54 esperimenti/patent/case study su ChatGPT, Gemini, Perplexity, con scoring per fattore. Prendere come riferimento più solido rispetto ai singoli blog.

### I 4 fattori a impatto più alto
1. **Statistiche/dati numerici nel contenuto** — fino a **+40% visibilità** (ceiling, non media; realistico +20-30%).
2. **Citare fonti autorevoli** — impatto simile (~stesso ordine di grandezza dello stat addition).
3. **Quotazioni/citazioni di esperti con attribuzione** — **+28%**.
4. **Structured data (JSON-LD/schema.org)** — pagine con schema corretto **citate 2.3× più spesso**; con schema + risposta fattuale chiara nei primi 200 parole → lift misurabile rapido (**+28-34% coverage in 14-21 giorni**).

### Altri fattori confermati
- **Content length**: pagine >2.500 parole citate **1.6×** più spesso di pagine <800 parole.
- **Presenza di almeno una citazione a fonte nominata nel body**: **2.1×** più citate rispetto a pagine senza.
- **Posizione del fatto nella pagina**: 55% delle citazioni AI Overview vengono dal primo 30% della pagina (vedi file 03).
- **Freshness / dateModified**: pagine con timestamp di aggiornamento recente ricevono priorità su query time-sensitive.
- **E-E-A-T** (Experience, Expertise, Authoritativeness, Trustworthiness): framework Google esteso oggi anche a GEO — non è un fattore diretto ma un principio guida che correla con autorevolezza percepita dal modello.

## Structured data / schema.org

- **FAQPage** e **Article** schema tra i più raccomandati per GEO.
- Schema markup correla con **2.3× citazioni** (vedi sopra).
- JSON-LD preferito a microdata (più facile da parsare in modo affidabile).
- Da includere: `Organization`, `Person` (autore), `FAQPage`, `HowTo`, `Article`/`BlogPosting`, `Product`/`Review` dove pertinente.

## Formato Q&A / answer-first

- Pattern raccomandato: **blocchi di risposta di 40-60 parole** vicino all'inizio di ogni pagina/sezione, sotto un heading **a forma di domanda**.
- Ogni sezione deve essere **self-contained** (comprensibile isolata, senza dover leggere il resto della pagina) — coerente col fatto che gli LLM recuperano a livello di **chunk**, non di pagina intera (vedi file 03).
- Usare **entità nominate esplicite** (nome prodotto/categoria) invece di pronomi — aiuta il modello a mantenere chiarezza referenziale nel chunk isolato.

## Content chunking / struttura semantica

- Ogni sezione = **un solo concetto** (semantic chunking).
- Sei aree su cui lavorare sistematicamente: **struttura del contenuto, formattazione della risposta, qualità delle citazioni, schema markup, riconoscimento delle entità, autorità topicale**.
- Evitare **client-side rendering** per contenuto importante — i crawler AI spesso non eseguono JS in modo affidabile.

## Entity-based content

- Content chunk devono identificare ed spiegare chiaramente le **entità chiave** (persone, luoghi, concetti, prodotti) rilevanti per il settore.
- **Naming coerente del brand/entità** in tutto il sito e sui profili esterni (social, directory, Wikipedia/Wikidata se applicabile) — naming incoerente rischia che l'AI tratti il brand come frase generica invece che entità distinta.

## Autorevolezza e "consenso di terze parti"

- Gli LLM apprendono l'autorevolezza di un brand tramite **consenso cross-web**: se fonti terze indipendenti non menzionano il brand, il modello non può "verificarne" l'esistenza/credibilità e non lo raccomanda, anche con contenuto proprio eccellente.
- **Digital PR / menzioni su siti terzi autorevoli** diventa quindi leva GEO cruciale, non solo contenuto on-site.
- **Co-occurrence signal**: nome brand + keyword di categoria nello stesso paragrafo su siti esterni autorevoli = segnale forte di appartenenza a quella categoria.

## Brand mention (anche senza link)

- Le **unlinked mentions** vanno trattate come segnale di citazione a tutti gli effetti — contribuiscono alla visibilità anche senza backlink cliccabile.
- Errore comune: ottimizzare solo per citazioni linkate/tracciabili e ignorare le menzioni testuali pure.

## Robots.txt e crawler AI

- Molti siti **bloccano involontariamente i crawler AI** (GPTBot, PerplexityBot, ClaudeBot, Google-Extended, ecc.) via robots.txt — primo controllo tecnico da fare in un audit GEO.

## Anti-fattore: keyword stuffing

- Confermato **controproducente** sia nel paper Princeton (-8% PAWC, -10% su Perplexity reale) sia nella pratica: le tecniche SEO classiche basate su densità di keyword **non si trasferiscono** ai motori generativi.

## Fonti
- https://www.digitalapplied.com/blog/ai-search-citation-ranking-factors-2026-data-study
- https://www.omnibound.ai/blog/generative-engine-optimization-statistics
- https://www.rankio.studio/learn/llm-ranking-factors
- https://thedigitalbloom.com/learn/llm-ranking-factors-2026/
- https://blog.hubspot.com/marketing/generative-engine-optimization-best-practices
- https://directiveconsulting.com/blog/a-guide-to-generative-engine-optimization-geo-best-practices/
- https://www.lumar.io/blog/best-practice/content-chunking-ai-extractability-geo-aeo-explainer/
- https://searchengineland.com/guide/content-chunking-seo
- https://www.frase.io/blog/what-is-answer-engine-optimization-the-complete-guide-to-getting-cited-by-ai
- https://www.cnabke.com/en/blogs/geo-mentions-linkless-ai-visibility.html
