# Chapter 3: Fattori di Ottimizzazione Concreti

## Core Idea
Un set ristretto di tecniche di contenuto (statistiche, citazioni di esperti, fonti autorevoli, structured data) spiega la maggior parte del lift di visibilità nei motori generativi, con impatti misurati e ripetibili tra studio accademico (Princeton, Chapter 1) e studio aggregato di mercato (digitalapplied.com); a questo si aggiunge una nuova classe di segnali — brand mention non linkate, consenso cross-web, e convenzioni "agent-readable" come llms.txt — che non hanno equivalente diretto nel SEO classico.

## Tecniche di contenuto citabile

- **Statistiche/dati numerici**: fattore a impatto più alto in uno studio aggregato di 54 esperimenti/paper/case study su 23 fattori (ChatGPT, Gemini, Perplexity) — fino a **+40% visibilità** come ceiling teorico, con un impatto realistico stimato di **+20-30%** (non una media misurata). (fonte: research/04-fattori-ottimizzazione.md)
- **Citare fonti autorevoli nel body**: impatto dello stesso ordine di grandezza della statistics addition; le pagine con almeno una citazione a fonte nominata nel body sono citate **2,1×** più spesso rispetto a pagine senza. (fonte: research/04-fattori-ottimizzazione.md)
- **Quotazioni/citazioni di esperti con attribuzione**: **+28%** di impatto misurato nello studio aggregato. (fonte: research/04-fattori-ottimizzazione.md)
- **Formato Q&A / answer-first**: blocchi di risposta di **40-60 parole** vicino all'inizio di ogni pagina/sezione, sotto un heading a forma di domanda; ogni sezione deve essere self-contained, coerente col fatto che gli LLM recuperano a livello di chunk e non di pagina intera. Usare entità nominate esplicite (nome prodotto/categoria) invece di pronomi, per mantenere chiarezza referenziale nel chunk isolato. (fonte: research/04-fattori-ottimizzazione.md)
- **Entity-based content**: i chunk devono identificare e spiegare chiaramente le entità chiave (persone, luoghi, concetti, prodotti) rilevanti per il settore, con naming coerente del brand/entità in tutto il sito e sui profili esterni (social, directory, Wikipedia/Wikidata) — un naming incoerente rischia che l'AI tratti il brand come frase generica invece che entità distinta. (fonte: research/04-fattori-ottimizzazione.md)
- **Semantic chunking**: ogni sezione deve trattare un solo concetto. Le sei aree su cui lavorare sistematicamente sono struttura del contenuto, formattazione della risposta, qualità delle citazioni, schema markup, riconoscimento delle entità, autorità topicale. Evitare client-side rendering per contenuto importante, perché i crawler AI spesso non eseguono JS in modo affidabile. (fonte: research/04-fattori-ottimizzazione.md)
- **Content length**: pagine oltre 2.500 parole sono citate **1,6×** più spesso di pagine sotto 800 parole. (fonte: research/04-fattori-ottimizzazione.md)
- **Posizione del fatto nella pagina**: il 55% delle citazioni AI Overview proviene dal primo 30% del contenuto della pagina (fonte: research/03-motori-generativi-tecnico.md, ripreso in research/04-fattori-ottimizzazione.md) — mettere le risposte/fatti chiave in alto.
- **Freshness / dateModified**: le pagine con timestamp di aggiornamento recente ricevono priorità su query time-sensitive. (fonte: research/04-fattori-ottimizzazione.md)
- **Anti-fattore — keyword stuffing**: confermato controproducente sia nel paper Princeton (-8% PAWC, -10% su Perplexity reale, vedi Chapter 1) sia nella pratica — le tecniche SEO classiche basate su densità di keyword non si trasferiscono ai motori generativi. (fonte: research/04-fattori-ottimizzazione.md)

## Autorevolezza e brand mentions

- **E-E-A-T** (Experience, Expertise, Authoritativeness, Trustworthiness): framework Google esteso oggi anche al GEO — non è un fattore diretto ma un principio guida che correla con l'autorevolezza percepita dal modello. (fonte: research/04-fattori-ottimizzazione.md)
- **Consenso cross-web**: gli LLM apprendono l'autorevolezza di un brand tramite consenso cross-web — se fonti terze indipendenti non menzionano il brand, il modello non può "verificarne" l'esistenza/credibilità e non lo raccomanda, anche con contenuto proprio eccellente. La digital PR / menzioni su siti terzi autorevoli diventa quindi una leva GEO cruciale, non solo il contenuto on-site. (fonte: research/04-fattori-ottimizzazione.md)
- **Co-occurrence signal**: il nome del brand insieme a keyword di categoria nello stesso paragrafo su siti esterni autorevoli è un segnale forte di appartenenza a quella categoria per il modello. (fonte: research/04-fattori-ottimizzazione.md)
- **Brand mention senza link**: le unlinked mentions vanno trattate come segnale di citazione a tutti gli effetti — contribuiscono alla visibilità anche senza backlink cliccabile. Un errore comune è ottimizzare solo per citazioni linkate/tracciabili e ignorare le menzioni testuali pure. (fonte: research/04-fattori-ottimizzazione.md)
- **Robots.txt e crawler AI**: molti siti bloccano involontariamente i crawler AI (GPTBot, PerplexityBot, ClaudeBot, Google-Extended, ecc.) via robots.txt — è il primo controllo tecnico da fare in un audit GEO. (fonte: research/04-fattori-ottimizzazione.md)

## Structured data / schema.org

- **Impatto misurato**: le pagine con structured data (JSON-LD/schema.org) corretto sono citate **2,3×** più spesso; combinando schema corretto con una risposta fattuale chiara nei primi 200 parole si ottiene un lift misurabile rapido — **+28-34% di coverage in 14-21 giorni**. (fonte: research/04-fattori-ottimizzazione.md)
- **Formato preferito**: JSON-LD è preferito a microdata perché più facile da parsare in modo affidabile. (fonte: research/04-fattori-ottimizzazione.md)
- **Schema types raccomandati**: `FAQPage` e `Article` sono tra i più raccomandati per il GEO. Da includere anche `Organization`, `Person` (autore), `HowTo`, `Article`/`BlogPosting`, `Product`/`Review` dove pertinente. (fonte: research/04-fattori-ottimizzazione.md)

## llms.txt e standard emergenti

- **Cos'è**: un file markdown semplice posto nella root del dominio (`https://example.com/llms.txt`) che fornisce un riassunto machine-readable strutturato del sito — chi sei, cosa fai, quali sono le fonti di verità definitive — risparmiando all'agente AI la navigazione ed elaborazione di ogni singola pagina. È una convenzione emergente, non uno standard W3C ufficiale: proposta originariamente da Jeremy Howard/Answer.AI e adottata per consenso di community, "bottom-up". (fonte: research/05-llms-txt-standard.md)
- **Adozione (dati 2026)**: oltre **844.000 siti** hanno implementato llms.txt, inclusi **Stripe, Cloudflare, Vercel, Anthropic** e centinaia di aziende mid-market. I vantaggi di adozione citati sono costo zero di hosting, deploy in pochi minuti e valore immediato per qualsiasi sistema AI che lo incontri. (fonte: research/05-llms-txt-standard.md)
- **Chrome Lighthouse**: ad aprile 2026 Google integra un check llms.txt direttamente in Chrome Lighthouse — lo stesso framework che ha normalizzato HTTPS, mobile-first e Core Web Vitals — segnale che lo standard sta diventando mainstream/auditabile. (fonte: research/05-llms-txt-standard.md)
- **Struttura tipica**: H1 col nome del sito/azienda, breve blockquote di descrizione, sezioni con link Markdown alle pagine/risorse più importanti (docs, pricing, API reference, blog). Va mantenuto sincronizzato con i contenuti reali, non lasciato come artefatto statico dimenticato. È complementare — non sostitutivo — a sitemap.xml, robots.txt e schema.org markup: sono livelli diversi dello stesso obiettivo, rendere il sito leggibile a un consumatore non-umano. (fonte: research/05-llms-txt-standard.md)
- **Limiti reali — è una convenzione, non una garanzia di citazione**: llms.txt permette solo la **lettura** (l'agente legge il sito), non abilita l'**azione** (verificare inventario in tempo reale, fare un ordine) — per quello servono standard complementari come il **Model Context Protocol (MCP)**, indicato come la direzione per far "agire" gli agenti AI, non solo leggere. Nel panorama più ampio degli standard "agent-readable web" 2026 compaiono anche **WebMCP** (esposizione delle funzionalità del sito come tool MCP-style, per interazione attiva), **SDF** e **CAP** (standard più recenti/di nicchia per structured discovery e capability advertisement, con nomi meno consolidati e ancora in evoluzione), e un framework più ampio chiamato **ARO (Agent-Readable Optimization)** che combina llms.txt, "companion files" e verifica delle credenziali per costruire un web leggibile dagli agenti in modo affidabile. (fonte: research/05-llms-txt-standard.md)

## Key Takeaways
1. I quattro fattori a impatto più alto secondo uno studio aggregato di 54 esperimenti/paper/case study (23 fattori totali) sono statistiche/dati numerici (fino a +40% ceiling, realistico +20-30%), citazione di fonti autorevoli (stesso ordine di grandezza), quotazioni di esperti attribuite (+28%) e structured data corretto (citazioni 2,3× più frequenti) (fonte: research/04-fattori-ottimizzazione.md).
2. Le pagine oltre 2.500 parole sono citate 1,6× più spesso di quelle sotto 800 parole, e le pagine con almeno una citazione a fonte nominata nel body sono citate 2,1× più spesso rispetto a pagine senza (fonte: research/04-fattori-ottimizzazione.md).
3. Il keyword stuffing resta controproducente in GEO tanto quanto nel paper Princeton del Chapter 1 (-8% PAWC, -10% su Perplexity reale) — le tecniche SEO classiche di densità keyword non si trasferiscono (fonte: research/04-fattori-ottimizzazione.md).
4. L'autorevolezza percepita dal modello dipende dal consenso cross-web: senza menzioni su fonti terze indipendenti, anche un brand con contenuto proprio eccellente non viene "verificato" né raccomandato — le unlinked mentions contano come segnale di citazione a tutti gli effetti (fonte: research/04-fattori-ottimizzazione.md).
5. llms.txt ha superato gli 844.000 siti adottanti (inclusi Stripe, Cloudflare, Vercel, Anthropic) ed è stato integrato in Chrome Lighthouse ad aprile 2026, ma resta una convenzione di sola lettura — non garantisce la citazione e non abilita azioni, per cui servono standard complementari come MCP (fonte: research/05-llms-txt-standard.md).

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
- https://www.yotpo.com/blog/what-is-llms-txt/
- https://developer.chrome.com/docs/lighthouse/agentic-browsing/llms-txt
- https://www.platinum.ai/what-is-llms-txt
- https://www.platinum.ai/ai-agent-web-standards
- https://promptowl.ai/resources/how-ai-agents-should-read-your-site-llms-txt/
- https://zenodo.org/records/18817486
