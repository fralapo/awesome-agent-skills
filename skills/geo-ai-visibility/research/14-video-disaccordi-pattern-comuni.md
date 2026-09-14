# Consenso e disaccordi cross-video (9 video, sintesi comparativa)

## Consenso forte (detto in ≥5/9 video, indipendentemente) → alta priorità per lo skill

1. **La SEO tradizionale resta la fondamenta, non viene sostituita.** Ripetuto quasi identico in Kaliber, Surfer Academy, Ahrefs (entrambi i video), Niko, Hostinger, Vendasta. Dato più citato in assoluto: **"76% delle citazioni in AI Overviews provengono da pagine già in top 10 Google"** (Ahrefs, ripreso testualmente sia da Ahrefs stesso sia da Niko).
2. **Il vecchio obiettivo "click/ranking" è sostituito da "essere menzionati/citati/inclusi nella risposta"**, anche senza click e a volte senza link visibile. Presente in tutti i 9 video sotto formulazioni diverse (Kaliber: "visibility is the metric"; Vendasta: "influence matters more than authorship"; Hostinger: "exposure-driven traffic"; Niko: "GEO gets you recommended").
3. **Le menzioni off-site/esterne (non il proprio sito) sono il fattore singolo più determinante.** Ahrefs lo quantifica (branded web mentions > backlink/DR in uno studio su 75k brand), Silicon Valley Girl lo conferma con "82% earned media", Kaliber con "consensus/authority must be distributed", Ahrefs Top-SEO-Experts-video con 3 esperti su 5 che puntano a menzioni esterne come leva #1.
4. **Struttura del contenuto "answer-first"** (BLUF / capsule content / risposta diretta subito dopo l'H2): presente esplicitamente in Kaliber, Ahrefs, Niko, Hostinger, Surfer.
5. **YouTube come canale ad alto impatto specifico per AI visibility** (non solo canale marketing generico): presente in Vendasta, Niko, Ahrefs (2 video), Silicon Valley Girl (via podcast/transcript). Motivazione ricorrente identica: addestramento LLM su trascrizioni YouTube + YouTube dominio più citato in AI Overviews.
6. **Structured data/schema resta rilevante ma non è "la chiave segreta"** — è abilitante, non sufficiente da solo. Surfer cita Google: "no secret AI tag". Concordano Vendasta, Niko (service schema), Silicon Valley Girl (Wikidata).
7. **Necessità di misurare in modo diverso dalla SEO classica** (niente CTR/posizione pulita) — tutti i video con taglio "agenzia/tool" (Kaliber, Surfer, Ahrefs, Silicon Valley Girl) propongono varianti dello stesso schema: audit manuale multi-piattaforma + tool di tracking + self-reported attribution.
8. **Contenuto fresco/aggiornato pesa più che nella SEO classica.** Dato quantitativo ripetuto in 2 fonti Ahrefs indipendenti (25.7% più fresco / 26% più fresco, studi diversi — Ryan Law citato in entrambi) e confermato qualitativamente da Kaliber e Silicon Valley Girl (aggiornamento contenuti come priorità).

## Disaccordi o enfasi divergenti tra fonti

- **"GEO è solo buona SEO" vs "GEO richiede tattiche nuove e distinte".**
  Surfer Academy e Hostinger tendono a minimizzare la novità ("boils down to just doing good SEO", "most skills translate directly"). Kaliber e Silicon Valley Girl enfatizzano invece cambi di paradigma netti (RAG, identity fixing su Wikidata, rewrite completo del sito) presentati come interventi distinti dalla SEO classica. Niko sta nel mezzo: stima esplicita **70% SEO classica / 30% tattiche GEO specifiche**.
  → Per lo skill: posizione equilibrata, SEO = prerequisito necessario ma non sufficiente; le tattiche GEO-specifiche (consensus, schema entity, atomic content, identity fixing) sono un livello aggiuntivo con ROI proprio.

- **Definizione di AEO vs GEO non è univoca.**
  Niko distingue nettamente AEO (= featured snippet / People Also Ask, tecnicamente più vecchio, pre-LLM) da GEO (= ottimizzazione per chatbot generativi). Ahrefs e Silicon Valley Girl invece usano **AEO e GEO come sinonimi intercambiabili** ("GEO stands for generative engine optimization. Some people call it AEO. It's basically the same" — Silicon Valley Girl). Surfer usa "GEO, AEO, o LLMO" come varianti dello stesso concetto via citazione di Ryan Law.
  → Per lo skill: segnalare esplicitamente che la terminologia nel settore NON è standardizzata; dare la propria definizione operativa chiara e nominare le varianti come sinonimi de facto, salvo la distinzione minoritaria di Niko.

- **Peso della lunghezza del contenuto.**
  Ahrefs ("Learn 80% of AEO") dà un dato quantitativo netto: **correlazione word count↔citazione ≈ zero**, oltre metà delle pagine citate sotto 1.000 parole. Nessun altro video contraddice esplicitamente, ma Surfer/Niko insistono comunque su "comprehensive topical coverage" e "coprire l'intero spettro di domande" — non è una vera contraddizione (copertura del topic a livello di sito ≠ lunghezza della singola pagina) ma nello skill va chiarita la distinzione tra **profondità per-pagina** (breve, atomica, ok) e **ampiezza per-topic/sito** (ampia, tramite più pagine, consigliata da tutti).

- **Ruolo del blog/content marketing classico.**
  Niko affronta esplicitamente l'obiezione "i blog sono inutili ora" e la respinge, ma ridefinendone lo scopo (da traffic driver a topical-authority builder). Nessun altro video nega esplicitamente il valore del blog, ma alcuni (Silicon Valley Girl, Exposure Ninja) mettono più enfasi su PR/earned media che su content management del proprio sito. Non contraddizione netta, ma differenza di enfasi tra "content-first" (Niko, Surfer, Ahrefs) e "PR/earned-media-first" (Silicon Valley Girl, uno dei 5 esperti Ahrefs).

- **Framework dei "meccanismi" con cui l'AI genera risposte — nessuno replica lo stesso schema, ma sono compatibili.**
  Exposure Ninja: 3 meccanismi (web search live / ottimizzazione AI-Overview dedicata / conoscenza pre-addestrata senza search). Vendasta: 4-step pipeline (intent decomposition → retrieval → rank/filter → compose, con citazione opzionale). Kaliber: modello a 2 layer (training knowledge + retrieval/RAG). Ahrefs: query fan-out (un prompt → decine di sotto-query parallele). Sono descrizioni complementari a diversi livelli di dettaglio, non in conflitto — utile combinarle nello skill come un unico modello tecnico a più livelli (training-time vs inference-time; query fan-out come dettaglio del passo "retrieval").

## Dati quantitativi più riutilizzabili (cross-check fonte)

| Dato | Valore | Fonte |
|---|---|---|
| Citazioni AI Overview da pagine già in top-10 Google | 76% | Ahrefs (ripreso da Niko) |
| Riduzione CTR posizione-1 per AI Overviews | -58% | Ahrefs / Kaliber (studio su 300k keyword) |
| Query che triggerano AI Overview | ~21% di tutte, ~58% delle domande | Ahrefs |
| Keyword che triggerano AI Overview di intento informazionale | 99.9% | Ahrefs |
| Freshness contenuto citato vs SERP classica | +25.7% / +26% (due studi Ahrefs diversi, stesso ordine di grandezza) | Ahrefs |
| Pagine citate <1.000 parole | oltre 50% (su 174k pagine analizzate) | Ahrefs |
| ChatGPT top pagine citate aggiornate nel 2025 / ultimi 30gg | 89.7% / 76% | Ahrefs |
| Pagine citate da ChatGPT in formato lista | 43.8% | Ahrefs |
| Correlazione branded web mentions ↔ visibilità AI Overviews | più forte di backlink/DR/referring domains (studio su 75k brand) | Ahrefs |
| Correlazione menzioni YouTube ↔ visibilità ChatGPT | 0.737 (più forte misurata) | Ahrefs |
| Siti che bloccano involontariamente GPTBot | 5.9% di 140M siti | Ahrefs |
| Miglioramento inclusione risposte AI con contenuto E-E-A-T strutturato | +37% (Perplexity, studio 2024 non meglio specificato) | Surfer Academy |
| Fonti citate in media per query AI Overview | ~5 | Surfer Academy |
| Query con 8 o meno fonti citate | 90% | Surfer Academy |
| Zero-click search rate Google | 60% (Hostinger) / >80% (Niko, dato 2026 più recente) / ~93% con AI Mode (Niko) | Hostinger, Niko |
| % marketer che vogliono ottimizzare per AI search vs chi lo fa davvero | 92% vs 40% | Silicon Valley Girl |
| Conversion rate traffico ChatGPT vs Google organico | 15.9% vs 1.76% | Silicon Valley Girl (dato interno newsletter) |
| % di ciò che l'AI cita che è earned media | 82% | Silicon Valley Girl |
| AI search traffic vs % sign-up generati (Ahrefs, caso interno) | 0.5% del traffico → 12.1% dei sign-up (23x conversion) | Ahrefs |
| Crescita traffico AI in un anno | 9.7x | Ahrefs |

Nota: molti dati derivano dalla stessa fonte primaria (ricerca Ahrefs) citata/riportata da video diversi — non sono conferme indipendenti multiple, ma la stessa ricerca che circola nel settore. Da segnalare nello skill come "dato Ahrefs" con attribuzione unica, non come consenso di più studi distinti.
