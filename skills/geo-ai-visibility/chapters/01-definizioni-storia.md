# Chapter 1: GEO — Definizioni e Storia

## Core Idea
**Generative Engine Optimization (GEO)** è la pratica di ottimizzare contenuti e siti per aumentare la probabilità di essere citati, menzionati o riassunti dalle risposte dei motori generativi (ChatGPT, Perplexity, Google AI Overviews/AI Mode, Copilot, Gemini, Claude) — l'equivalente del SEO ma per risposte sintetizzate invece che per liste di link cliccabili.

## Cos'è il GEO

- **GEO (Generative Engine Optimization)**: ottimizzare per essere selezionati come fonte/passaggio dentro una risposta sintetizzata unica generata da un LLM, non per rankare in una lista di 10 link. (fonte: research/01-definizioni-storia.md)
- **Termini correlati/intercambiabili nel settore**: **AEO** (Answer Engine Optimization), **AI Search Optimization**, **AI Visibility**, **LLM Optimization (LLMO)** — per i confini esatti tra questi termini vedi glossary.md. (fonte: research/01-definizioni-storia.md)
- **Frase chiave del settore**: *"Gli LLM non rankano pagine — selezionano passaggi, riusano evidenze, e citano ciò che li aiuta a rispondere con sicurezza."* (fonte: research/02-seo-vs-geo.md)

## Il paper fondativo

- **"GEO: Generative Engine Optimization"** — autori Pranjal Aggarwal, Vishvak Murahari, Tanmay Rajpurohit, Ashwin Kalyan, Karthik Narasimhan, Ameet Deshpande; affiliazioni Princeton University, Allen Institute for AI, Georgia Tech, IIT Delhi. Pubblicato su arXiv il 16 novembre 2023 (arXiv:2311.09735), poi presentato a ACM SIGKDD 2024 (KDD '24). Primo paper accademico a formalizzare GEO come "black-box optimization framework" per content creator, con benchmark dedicato. (fonte: research/01-definizioni-storia.md)

### GEO-BENCH (il benchmark)

- **10.000 query totali** (8k train / 1k validation / 1k test), aggregate da **9 dataset sorgente**: MS MARCO, ORCAS-I, Natural Questions, AllSouls, LIMA, Davinci-Debate, Perplexity.ai Discover, ELI5, e query generate da GPT-4. (fonte: research/01-definizioni-storia.md)
- **25 domini/categorie** diverse (Arts, Health, Games, Law & Government, Debate, History, People & Society, Science, Explanation, Opinion, ecc.). Distribuzione query: **80% informazionali, 10% transazionali, 10% navigazionali**. (fonte: research/01-definizioni-storia.md)
- **Backend di ricerca**: Google Search (top-5 risultati per query) usato per costruire il motore generativo prototipo su cui testare gli interventi, con validazione reale anche su Perplexity.ai come motore generativo deployato. (fonte: research/01-definizioni-storia.md)

### Le due metriche proposte

- **Position-Adjusted Word Count (PAWC)**: conteggio parole normalizzato che pesa il contributo di ciascuna fonte citata nella risposta, con decadimento esponenziale in base alla posizione della citazione (le citazioni più vicine all'inizio della risposta pesano di più — analogia con il CTR posizionale nella SERP classica). Formula: `Σ(s∈Sci) |s|·e^(-pos(s)/|S|) / Σ(s∈Sr) |s|`. (fonte: research/01-definizioni-storia.md)
- **Subjective Impression (SI)**: metrica composita a 7 componenti valutata con GPT-3.5 (metodologia simile a G-Eval) — rilevanza rispetto alla query, influenza della citazione, unicità del contenuto, prominenza posizionale soggettiva, volume percepito del contenuto, probabilità di click, diversità del materiale citato. (fonte: research/01-definizioni-storia.md)

### Le 9 tecniche testate e il loro impatto misurato

| Tecnica | Δ PAWC | Δ Subjective Impression | Note |
|---|---|---|---|
| **Quotation Addition** (citazioni/quote di esperti) | +41% (top performer) | +28% | Migliore tecnica assoluta |
| **Statistics Addition** (dati/statistiche) | +33% | +22% | Forte anche su Perplexity reale (+37% SI) |
| **Cite Sources** (citare fonti autorevoli nel testo) | +30% | +15% | Effetto molto più forte su siti a basso ranking |
| **Fluency Optimization** (scorrevolezza/leggibilità) | +28% | +13% | |
| **Technical Terms** (terminologia tecnica di settore) | +18% | +10% | |
| **Easy-to-Understand** (semplificare linguaggio) | +13% | +5% | |
| **Authoritative** (tono autorevole/assertivo) | +12% | +17% | Migliore per Debate/History/Science |
| **Unique Words** (vocabolario raro/distintivo) | +6% | minima | Effetto debole |
| **Keyword Stuffing** | -8% (fino a -10% su Perplexity reale) | — | Controproducente: contraddice la SEO classica |

(fonte: research/01-definizioni-storia.md)

- **Validazione su Perplexity.ai reale**: Quotation Addition +22% PAWC; Statistics Addition +37% SI; Keyword Stuffing -10% (conferma la controproducenza). (fonte: research/01-definizioni-storia.md)
- **Combinazione ottimale**: le strategie combinate battono le singole — Fluency Optimization + Statistics Addition è la combinazione migliore nei test. (fonte: research/01-definizioni-storia.md)

### Effetto redistributivo (finding chiave)

- **Effetto redistributivo**: il lift da GEO è molto più forte per fonti già a basso ranking — "Cite Sources" dà **+115% per fonti in posizione 5** contro **-30% per fonti già in posizione 1**. Implicazione: GEO tende a "democratizzare" la visibilità — i siti svantaggiati nella SERP tradizionale hanno margine di crescita più alto nelle risposte generative, mentre i siti già dominanti hanno meno da guadagnare (o perdono relativamente). (fonte: research/01-definizioni-storia.md)

### Efficacia per dominio (differenziata)

- **Authoritative**: migliore per Debate, History, Science. **Quotation Addition**: ottimale per People & Society, Explanation, History. **Statistics Addition**: più efficace per Law & Government, Debate, Opinion. **Cite Sources**: più forte su query fattuali/dichiarative. Non esiste una tecnica universale — l'ottimizzazione va adattata al dominio/tipo di query. (fonte: research/01-definizioni-storia.md)

### Limiti dichiarati dagli autori

- **Limiti dichiarati**: le tecniche richiedono adattamento continuo man mano che i motori generativi evolvono; i dataset di query possono invecchiare e richiedere aggiornamento del benchmark; lo studio non valuta l'impatto sul ranking SEO tradizionale (è ortogonale); il tagging delle query per dominio è soggetto a interpretazione soggettiva (nonostante verifica manuale). (fonte: research/01-definizioni-storia.md)

## Cronologia essenziale del settore

- **Nov 2023**: pubblicazione del paper GEO (Princeton/Georgia Tech/Allen AI/IIT Delhi) — nascita del termine accademico.
- **2024**: paper presentato a KDD 2024 (ACM SIGKDD).
- **2024–2025**: esplosione di tool commerciali AI-visibility (Profound, Peec AI, Otterly.AI, AthenaHQ, Goodie...) e di contenuti "how-to" da agenzie SEO (Ahrefs, Semrush, HubSpot, Search Engine Land).
- **2025–2026**: consolidamento del mercato — round di finanziamento importanti (Profound $96M Series C @ $1B valuation, feb 2026; Peec AI €18M Series A, nov 2025); nascita di standard emergenti come **llms.txt** (adozione riportata su oltre 844.000 siti, incl. Stripe, Cloudflare, Vercel, Anthropic); Google integra un check llms.txt in **Chrome Lighthouse** (apr 2026).
- **2026**: crescita ulteriore del "query fan-out" in Google AI Overviews/AI Mode, che cambia il modo in cui si formano le citazioni (vedi Chapter 2).

(fonte: research/01-definizioni-storia.md)

## GEO vs SEO tradizionale

| Dimensione | SEO tradizionale | GEO |
|---|---|---|
| Output per l'utente | Lista di 10 link (SERP) | Risposta sintetica unica, multi-fonte |
| Unità di ottimizzazione | Pagina intera (title, meta, backlink) | **Chunk/passaggio semantico** dentro la pagina |
| Segnali principali | Keyword, backlink, metadata, PageRank | Fact density, structured data, entity relationships, citabilità |
| Query tipiche | Keyword brevi, navigazionali | **Conversazionali**, multi-turno, informazionali/comparative |
| Metrica di successo | Ranking position, CTR, traffico | Frequenza citazione/menzione, share of voice, sentiment nella risposta |
| Click-through | Centrale | Spesso assente (zero-click) — la "vittoria" è essere menzionati anche senza click |
| Backlink | Segnale di autorità primario | Secondario; contano di più entity co-occurrence e menzioni non linkate (unlinked mentions) |
| Ranking multiplo | 1 pagina = 1 posizione | 1 risposta può citare 3-10 fonti diverse contemporaneamente (nessuna "posizione 1" esclusiva) |
| Ciclo di feedback | Google Search Console, rank tracker | Tool AI-visibility (Profound, Peec, Otterly...) — nuova categoria, no standard consolidato |

(fonte: research/02-seo-vs-geo.md)

- **Cosa resta uguale**: autorevolezza, chiarezza, struttura e allineamento con l'intento utente contano in entrambi — ma il modo in cui questi segnali vengono "letti" cambia: il SEO li legge via backlink/CTR, i motori generativi via entity recognition e coerenza semantica. Una base SEO tecnica solida (velocità, crawlability, heading puliti, nessun blocco robots.txt sui crawler AI) resta prerequisito per il GEO: il GEO si costruisce *sopra* il SEO, non lo sostituisce. (fonte: research/02-seo-vs-geo.md)
- **Perché "ranking bene su Google" non garantisce visibilità AI**: con il meccanismo di query fan-out (la query originale viene spezzata in più sotto-query, e vengono citate le pagine che compaiono più spesso nei risultati delle sotto-query) solo il **38%** delle citazioni AI Overview proviene oggi da pagine nel top-10 Google (dato 2026, in forte calo dal 76% di metà 2025). ChatGPT Search e Perplexity hanno pipeline di retrieval indipendenti da Google: solo l'**11% dei domini** è citato sia da ChatGPT sia da Perplexity (su 680M+ citazioni analizzate) — serve ottimizzare per ogni motore separatamente, non basta un solo canale. (fonte: research/02-seo-vs-geo.md)
- **Brand mention vs citazione linkata**: nel contesto commerciale ciò che conta di più spesso è la menzione del brand (l'AI raccomanda l'azienda per nome), non necessariamente un link cliccabile — le menzioni senza link contribuiscono comunque alla visibilità del brand nelle risposte AI. Il segnale di co-occurrence (il nome del brand che appare nello stesso paragrafo/contesto delle keyword di categoria su siti terzi autorevoli) è ciò che "dice" al modello che il brand appartiene a quella categoria. (fonte: research/02-seo-vs-geo.md)

## Key Takeaways
1. Il GEO ottimizza per essere citati/menzionati dentro una risposta sintetizzata, non per rankare in una SERP — l'unità di ottimizzazione è il chunk semantico, non la pagina intera.
2. Il paper fondativo (arXiv:2311.09735) dimostra che aggiungere citazioni di esperti e statistiche (Quotation/Statistics Addition) è la leva più efficace, mentre il keyword stuffing è controproducente in GEO.
3. Il lift da GEO è redistributivo: i siti in posizione bassa nella SERP tradizionale hanno il margine di crescita più alto nelle risposte generative.
4. Nessuna tecnica GEO è universale — l'efficacia varia per dominio/tipo di query, quindi l'ottimizzazione va adattata caso per caso.
5. Il ranking Google classico non garantisce citazione AI: con il query fan-out solo il 38% delle citazioni AI Overview arriva dal top-10 Google, e ChatGPT/Perplexity hanno pipeline indipendenti (solo 11% di overlap di domini citati tra i due).

## Fonti
- https://arxiv.org/abs/2311.09735 (paper originale)
- https://arxiv.org/html/2311.09735v3 (versione HTML leggibile — usata per estrarre tabelle/numeri)
- https://dl.acm.org/doi/10.1145/3637528.3671900 (KDD 2024)
- https://searchengineland.com/generative-engine-optimization-framework-introduced-research-paper-435855
- https://blckalpaca.at/en/knowledge-base/seo-geo/geo-generative-engine-optimization/the-princeton-geo-study-methodology-results-and-critique
- https://writesonic.com/blog/geo-vs-seo
- https://www.contentful.com/blog/generative-engine-optimization-seo/
- https://gofishdigital.com/blog/seo-vs-geo/
- https://www.within.co/blog/generative-engine-optimization/
- https://ahrefs.com/blog/ai-overview-citations-top-10/
- https://ahrefs.com/blog/search-rankings-ai-citations/
- https://discoveredlabs.com/blog/ai-citation-patterns-how-chatgpt-claude-and-perplexity-choose-sources
