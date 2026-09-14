# GEO: definizioni e storia

## Cos'è GEO

**Generative Engine Optimization (GEO)** = pratica di ottimizzare contenuti/siti per aumentare la probabilità di essere citati, menzionati o riassunti dalle risposte di motori generativi (ChatGPT, Perplexity, Google AI Overviews/AI Mode, Copilot, Gemini, Claude). Analogo del SEO ma per risposte sintetizzate invece di liste di link.

Termini correlati usati in modo intercambiabile nel settore: **AEO** (Answer Engine Optimization), **AI Search Optimization**, **AI Visibility**, **LLM Optimization (LLMO)**.

## Il paper fondativo: "GEO: Generative Engine Optimization"

- **Autori**: Pranjal Aggarwal, Vishvak Murahari, Tanmay Rajpurohit, Ashwin Kalyan, Karthik Narasimhan, Ameet Deshpande.
- **Affiliazioni**: Princeton University, Allen Institute for AI, Georgia Tech, IIT Delhi.
- **Pubblicato**: arXiv 16 nov 2023 (arXiv:2311.09735), poi ACM SIGKDD 2024 (KDD '24).
- Primo paper accademico a formalizzare GEO come "black-box optimization framework" per content creator, con benchmark dedicato.

### GEO-BENCH (il benchmark)

- **10.000 query totali** (8k train / 1k validation / 1k test).
- Query aggregate da **9 dataset sorgente**: MS MARCO, ORCAS-I, Natural Questions, AllSouls, LIMA, Davinci-Debate, Perplexity.ai Discover, ELI5, query generate da GPT-4.
- **25 domini/categorie** diverse (Arts, Health, Games, Law & Government, Debate, History, People & Society, Science, Explanation, Opinion, ecc.).
- Distribuzione query: **80% informazionali, 10% transazionali, 10% navigazionali**.
- Backend di ricerca: **Google Search** (top-5 risultati per query) usato per costruire il motore generativo prototipo su cui testare gli interventi.
- Validazione reale anche su **Perplexity.ai** come motore generativo deployato.

### Le due metriche proposte

1. **Position-Adjusted Word Count (PAWC)**
   Conteggio parole normalizzato che pesa il contributo di ciascuna fonte citata nella risposta, con **decadimento esponenziale in base alla posizione della citazione** (le citazioni più in alto/più vicine all'inizio della risposta pesano di più — analogia con il CTR posizionale nella SERP classica).
   Formula: `Σ(s∈Sci) |s|·e^(-pos(s)/|S|) / Σ(s∈Sr) |s|`

2. **Subjective Impression (SI)**
   Metrica composita a 7 componenti valutata con GPT-3.5 (metodologia simile a G-Eval): rilevanza rispetto alla query, influenza della citazione, unicità del contenuto, prominenza posizionale soggettiva, volume percepito del contenuto, probabilità di click, diversità del materiale citato.

### Le 9 tecniche testate e il loro impatto misurato

| Tecnica | Δ PAWC | Δ Subjective Impression | Note |
|---|---|---|---|
| **Quotation Addition** (aggiungere citazioni/quote di esperti) | **+41%** (top performer) | +28% | Migliore tecnica assoluta |
| **Statistics Addition** (aggiungere dati/statistiche) | +33% | +22% | Forte anche su Perplexity reale (+37% SI) |
| **Cite Sources** (citare fonti autorevoli nel testo) | +30% | +15% | Effetto molto più forte su siti a basso ranking (vedi sotto) |
| **Fluency Optimization** (migliorare scorrevolezza/leggibilità della prosa) | +28% | +13% | |
| **Technical Terms** (uso di terminologia tecnica di settore) | +18% | +10% | |
| **Easy-to-Understand** (semplificare linguaggio) | +13% | +5% | |
| **Authoritative** (tono autorevole/assertivo) | +12% | +17% | Migliore per Debate/History/Science |
| **Unique Words** (vocabolario/parole rare, distintive) | +6% | minima | Effetto debole |
| **Keyword Stuffing** | **-8%** (fino a -10% su Perplexity reale) | — | **Controproducente**: contraddice la SEO classica |

- Validazione su Perplexity.ai reale: Quotation Addition +22% PAWC; Statistics Addition +37% SI; Keyword Stuffing -10% (conferma controproducenza).
- Le strategie combinate battono le singole: **Fluency + Statistics Addition** = combinazione ottimale nei test.

### Effetto redistributivo (finding chiave)

- Il lift da GEO è **molto più forte per fonti già a basso ranking**: "Cite Sources" dà **+115% per fonti in posizione 5** contro **-30% per fonti già in posizione 1**.
- Implicazione: GEO tende a "democratizzare" la visibilità — i siti che partono svantaggiati nella SERP tradizionale hanno il margine di crescita più alto nelle risposte generative, i siti già dominanti hanno meno da guadagnare (o perdono relativamente).

### Efficacia per dominio (differenziata)

- **Authoritative**: migliore per Debate, History, Science.
- **Quotation Addition**: ottimale per People & Society, Explanation, History.
- **Statistics Addition**: più efficace per Law & Government, Debate, Opinion.
- **Cite Sources**: più forte su query fattuali/dichiarative.
- Conclusione: **non esiste una tecnica universale** — l'ottimizzazione va adattata al dominio/tipo di query.

### Limiti dichiarati dagli autori

- Le tecniche richiedono adattamento continuo man mano che i motori generativi evolvono (i modelli sottostanti cambiano).
- I dataset di query possono "invecchiare" e richiedere aggiornamento del benchmark.
- Lo studio **non valuta l'impatto sul ranking SEO tradizionale** (è ortogonale).
- Il tagging delle query per dominio è soggetto a interpretazione soggettiva (nonostante verifica manuale).

## Cronologia essenziale del settore GEO

- **Nov 2023**: pubblicazione paper GEO (Princeton/Georgia Tech/Allen AI/IIT Delhi) — nascita del termine accademico.
- **2024**: paper presentato a KDD 2024 (ACM SIGKDD).
- **2024–2025**: esplosione di tool commerciali AI-visibility (Profound, Peec AI, Otterly.AI, AthenaHQ, Goodie...) e di contenuti "how-to" da agenzie SEO (Ahrefs, Semrush, HubSpot, Search Engine Land).
- **2025–2026**: consolidamento del mercato — round di finanziamento importanti (Profound $96M Series C @ $1B valuation, feb 2026; Peec AI €18M Series A, nov 2025); nascita di standard emergenti come **llms.txt** (adozione riportata >844.000 siti, incl. Stripe, Cloudflare, Vercel, Anthropic); Google integra un check llms.txt in **Chrome Lighthouse** (apr 2026).
- 2026: crescita ulteriore del "query fan-out" in Google AI Overviews/AI Mode, cambiando il modo in cui le citazioni si formano (vedi file 03).

## Fonti
- https://arxiv.org/abs/2311.09735 (paper originale)
- https://arxiv.org/html/2311.09735v3 (versione HTML leggibile — usata per estrarre tabelle/numeri)
- https://dl.acm.org/doi/10.1145/3637528.3671900 (KDD 2024)
- https://searchengineland.com/generative-engine-optimization-framework-introduced-research-paper-435855
- https://blckalpaca.at/en/knowledge-base/seo-geo/geo-generative-engine-optimization/the-princeton-geo-study-methodology-results-and-critique
