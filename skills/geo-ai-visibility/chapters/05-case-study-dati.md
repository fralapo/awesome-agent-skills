# Chapter 5: Case Study e Dati

## Core Idea
I numeri aggregati sul comportamento di ricerca (zero-click, distribuzione del traffico referral, concentrazione delle citazioni su un piccolo numero di domini) mostrano perché il GEO è diventato rilevante: il click sta diventando l'eccezione, non la regola, e le citazioni AI si concentrano fortemente su pochi domini già autorevoli — con margini di crescita comunque misurabili per chi si struttura bene.

## Zero-click e volumi

- **Tasso zero-click Google**: passato dal **50% nel 2019** al **64.82% nel 2026**. Su **mobile** il tasso sale a **77%**. (fonte: research/07-case-study-dati.md)
- **Su 1.000 ricerche Google US**: solo **360 portano a un click sul web aperto**, **640 finiscono senza alcun click**. (fonte: research/07-case-study-dati.md)
- **Quando appare un AI Overview**: zero-click **80-83%** (dato sui primi 4 mesi 2026, media generale ~68% quando l'AIO è presente). Con **AI Mode** (Google) il tasso sale a **93%**, il più alto tra tutte le superfici misurate. (fonte: research/07-case-study-dati.md)
- **Traffico referral da AI**: **AI Mode** genera referral solo per il **1.6-2.5%** delle query, contro il **17-19%** del referral rate della ricerca Google tradizionale — volume basso. Ma i visitatori **AI-referred convertono ~4.4×** rispetto al traffico organico tradizionale: meno volume, valore per visita molto più alto. (fonte: research/07-case-study-dati.md)
- **Distribuzione del traffico referral tra piattaforme AI**: **ChatGPT domina**, con stime tra **~63% e ~92%** del referral AI tracciabile (varia per metodologia di misurazione), seguito da Gemini, Perplexity, Claude, Copilot. (fonte: research/07-case-study-dati.md)

## Concentrazione delle citazioni

- **Concentrazione dei domini citati**: uno studio aggregato su 680M+ citazioni (6 grandi studi, ago 2024–apr 2026) mostra che il top 1% dei domini (~12 siti) — Wikipedia, Reddit, Forbes, Healthline, Investopedia, NYT, grandi domini .gov/.edu — cattura il **47%** di tutte le citazioni AI. (fonte: research/07-case-study-dati.md)
- **Overlap tra motori**: bassissimo — solo l'**11%** dei domini è citato sia da ChatGPT sia da Perplexity. (fonte: research/07-case-study-dati.md)
- **Pattern di citazione in Google AI Overviews**: il **38%** delle citazioni proviene oggi da pagine nel **top-10 Google** — in netto calo dal **76%** di metà 2025, effetto del "query fan-out" (vedi chapter 03). Il **55%** delle citazioni proviene dal primo **30%** del contenuto della pagina sorgente. Le pagine **>2.500 parole** sono citate **1.6×** più spesso di quelle sotto le 800 parole. Le pagine con **schema markup** sono citate **2.3×** più spesso, e quelle con **almeno una fonte citata nel body** sono **2.1×** più citate rispetto a chi non ne ha. (fonte: research/07-case-study-dati.md)
- **Impatto misurato delle tecniche di contenuto** (paper Princeton, dettaglio completo in chapter 01): Quotation Addition +41% PAWC nel paper, +22% PAWC validato su Perplexity reale; Statistics Addition +33% PAWC nel paper, +37% Subjective Impression su Perplexity reale; Keyword Stuffing -8% PAWC nel paper, -10% su Perplexity reale (controproducenza confermata anche su motore reale, non solo in laboratorio). L'effetto redistributivo resta: **+115%** di lift per fonti in posizione 5 (basso ranking) contro **-30%** per fonti già in posizione 1, con la tecnica "Cite Sources". (fonte: research/07-case-study-dati.md)

## Casi studio nominati

Il materiale raccolto in questa fonte non contiene case study "prima/dopo" di singole aziende con metodo e risultato dettagliati (quelli emergono invece dai digest video, vedi chapter 07). Ciò che è nominato qui sono adozione di mercato e segnali di maturità economica del settore:

- **Adozione llms.txt** (proxy di maturità del mercato GEO): oltre **844.000 siti** con llms.txt implementato entro il 2026, inclusi nomi noti come **Stripe, Cloudflare, Vercel, Anthropic**. Google ha integrato un check llms.txt in **Chrome Lighthouse** (apr 2026), segnale di istituzionalizzazione della pratica. (fonte: research/07-case-study-dati.md)
- **Finanziamenti nel settore tool AI-visibility** (proxy di maturità economica): **Profound** ha raccolto **$96M in Series C** con valutazione **$1B** (feb 2026), per un funding totale di **$155M**. **Peec AI** ha raccolto **€18M in Series A** (nov 2025), dopo aver raggiunto **€650K ARR in 4 mesi** dal lancio (metà 2025). (fonte: research/07-case-study-dati.md)

## Key Takeaways
1. Lo zero-click è ormai la norma, non l'eccezione: 64.82% su Google in generale, fino al 93% con AI Mode — il click non è più la metrica di successo di default. (fonte: research/07-case-study-dati.md)
2. Il traffico da AI è a basso volume ma alto valore: 1.6-2.5% di referral rate con AI Mode contro conversioni ~4.4× superiori al traffico organico tradizionale. (fonte: research/07-case-study-dati.md)
3. Le citazioni AI sono fortemente concentrate: il top 1% dei domini (~12 siti) cattura il 47% di tutte le citazioni analizzate su un campione di 680M+. (fonte: research/07-case-study-dati.md)
4. Il legame tra ranking Google classico e citazione AI Overview si sta indebolendo: solo il 38% delle citazioni viene oggi da pagine top-10 Google, contro il 76% di metà 2025. (fonte: research/07-case-study-dati.md)
5. I segnali di maturità del mercato GEO sono concreti e recenti: oltre 844.000 siti con llms.txt e round di finanziamento a 9 cifre per i tool di AI-visibility (Profound $1B di valutazione). (fonte: research/07-case-study-dati.md)

## Fonti
- https://www.similarweb.com/blog/marketing/geo/zero-click-marketing/
- https://www.digitalapplied.com/blog/zero-click-search-statistics-2026-complete-data
- https://www.omnibound.ai/blog/zero-click-search-statistics
- https://www.omnibound.ai/blog/ai-seo-statistics
- https://arrow-ai.us/blog/ai-search-geo-statistics-2026/
- https://www.instantpress.co/aeo-statistics
- https://ahrefs.com/blog/ai-overview-citations-top-10/
- https://ahrefs.com/blog/search-rankings-ai-citations/
- https://www.deltavdigital.com/resources/reports/ai-citation-study/
- https://everything-pr.com/ai-platform-citation-source-index-2026
- https://www.tryprofound.com/blog/best-ai-visibility-tools-for-marketing-agencies
