# Chapter 8: Entity GEO per Business Locali di Servizi — Caso Magnet vs Bliss

## Core Idea
Un LLM non consiglia l'azienda "migliore": consiglia quella che il retrieval gli restituisce con abbastanza evidenza da poterla citare con sicurezza. Per un business di servizi locale (agenzia, studio, consulenza) la visibilità nelle risposte AI dipende da tre cose, in quest'ordine: (1) l'entità è **disambiguata** e ricostruibile come *nome → categoria → luogo → servizi → prove*; (2) esiste una **pagina che risponde letteralmente** a ogni formulazione "servizio + città"; (3) **fonti terze indipendenti** confermano la stessa descrizione. Il caso sotto mostra un'agenzia con portfolio più forte esclusa dalle risposte e una concorrente consigliata quasi sempre, per ragioni interamente strutturali.

> **Nota sulla fonte.** Il caso è ricavato da una sessione di ricerca con un assistente AI (ChatGPT con web search, ottobre 2026) su due siti pubblici: magnetmilano.it e blissagency.it. Le osservazioni sui siti sono quelle riportate in quella sessione; i dati di traffico citati per Bliss sono **dichiarazioni dell'azienda stessa**, non verificate con tool indipendenti. Va usato come esempio ragionato, non come dato misurato.

## Il caso: la domanda di partenza

Una serie di query comparative ("agenzie di brand identity a Milano", "graphic design Milano", "ADV e media Milano", "web e digital strategy Milano") ha prodotto liste di agenzie in cui **Magnet Communication** (Assago/Milano: marketing strategy, brand identity, graphic design, licensing, ADV & media, web & digital; clienti come Ferrero, Vespa, FIAT 500, San Siro Stadium, Lupin III) non compariva mai, mentre **Bliss Agency** (Roma e Milano) compariva quasi sempre, anche cambiando città.

Diagnosi: non è un giudizio di qualità. *"Nelle fonti recuperate inizialmente, altri concorrenti erano più facili da trovare e corroborare."* GEO significa prima di tutto **entrare nel retrieval corretto**, solo dopo convincere.

## Perché l'agenzia esclusa non emergeva (Magnet)

Il sito aveva già basi buone: pagine verticali per ognuno dei 6 servizi, FAQ, progetti collegati, alcuni title già nel formato "servizio + Milano". I problemi erano altrove:

- **Ambiguità dell'entità.** "Magnet" + Milano restituiva anche altre realtà omonime (un magazine/consulting milanese, una casa di produzione con una divisione chiamata anch'essa "Magnet Communication", altri domini simili). Il sito giusto emergeva partendo dal dominio, molto meno quando il motore doveva capire *da solo* quale Magnet fosse l'agenzia.
- **Hero "brand first".** H1 creativo ("Dove il brand diventa forza d'attrazione") senza una frase che dica chi/dove/cosa: il motore deve ricostruirlo da elementi sparsi più in basso.
- **Corroborazione esterna debole.** Per i concorrenti il retrieval trovava directory, classifiche, profili partner e articoli che li descrivevano; per Magnet quasi solo magnetmilano.it. Fonte primaria ottima, ma nessuna seconda o terza fonte indipendente.
- **Portfolio come gallery.** Loghi e immagini forti, poco testo: un retrieval engine non "vede" un carosello di loghi, vede (o non vede) la relazione *agenzia → ha fatto X per cliente Y con servizio Z*.
- **Assenza di contenuti informativi.** Sei landing commerciali, nessuna libreria di articoli che dimostri competenza sui temi (topical authority).
- **Team anonimo.** Nome + ruolo, senza bio, competenze, link esterni: nessuna rete *persona → competenza → agenzia*.
- **Profili aziendali sottoutilizzati.** LinkedIn con categoria e sede corrette ma descrizione povera e non allineata all'offerta attuale.

## Perché la concorrente emergeva ovunque (Bliss)

Bliss ha costruito il sito come **knowledge graph commerciale**, dichiaratamente orientato a SEO + GEO (la loro pagina SEO parla esplicitamente di "il cliente chiede a ChatGPT" e il menu marketing include "GEO & AIO").

| Leva | Come la usa Bliss | Perché funziona nel retrieval |
|---|---|---|
| **Query coverage** | Una superficie indicizzabile per quasi ogni formulazione commerciale: agenzia di comunicazione, di marketing, studio grafico, web agency, SEO, brand strategy — ognuna "Roma e Milano" | Per "studio grafico Milano" esiste letteralmente una sezione intitolata *Studio Grafico Milano*: il motore non deve inferire nulla |
| **Città scritte ovunque, con sedi reali** | Sottosezioni Roma/Milano nelle landing, sedi fisiche dichiarate in entrambe le città, descrizione dei settori del mercato locale | Corrispondenza diretta *azienda → sede fisica → città*; il presidio geografico non è una doorway page |
| **Pagine lunghe e onnicomprensive** | La landing graphic design copre brand/visual identity, tipografia, palette, CGI, social visual, brochure, stampa, brand book, differenza studio grafico vs agenzia creativa, FAQ | Una sola URL si associa a decine di concetti senza salti tra pagine |
| **FAQ retrieval-friendly** | Domande reali di confronto ("differenza tra logo, brand identity e visual identity?") con risposte discorsive | Unità domanda-risposta già pronte da estrarre |
| **Entity reinforcement nel footer** | La stessa frase-definizione ("Bliss è una società di Brand Advisory, Brand Strategy… con sede a Roma e Milano") su ogni pagina | Qualunque URL il crawler colpisca, trova la definizione dell'entità completa |
| **Money page + pagina informativa** | Landing commerciale *Brand Strategy* + guida lunga "Brand Strategy: cos'è, come si costruisce…" con indice, autore e tempo di lettura | Copre sia l'intento d'acquisto sia quello informativo; gli AI citano più facilmente il secondo |
| **Case study testuali** | Struttura *situazione precedente → problemi → intervento → risultati* con metriche | Il motore deduce la competenza da una prova, non da un'autodichiarazione |
| **Persone come prova** | Head of SEO, CDO, Head of Video, Head of Copy con descrizioni professionali, articoli firmati | Rete *servizio → persona → ruolo* utile per E-E-A-T ed entity building |
| **Freschezza** | Articoli pubblicati nelle settimane precedenti all'analisi | Segnala un dominio vivo che espande il proprio corpus |
| **Classifiche "best agencies"** | Articoli "Le 10 migliori agenzie SEO/Branding in Italia" con sé stessa al 1° posto | Intercetta query "migliori agenzie X" — **ma vedi rischi sotto** |

Sintesi del confronto: Magnet vinceva su portfolio, specializzazione verticale (licensing) e brand; Bliss vinceva su landing, contenuti informativi, targeting città, FAQ, case study testuali, entity reinforcement, team, freschezza, keyword coverage e GEO intenzionale.

## Principi generalizzabili

1. **Retrieval prima della persuasione.** Se l'entità non è nel set di documenti recuperati, la qualità non conta. La prima domanda di un audit GEO locale è: *per la query "servizio + città", quale pagina mia viene recuperata?*
2. **Disambigua l'entità.** Se il nome è generico, usa ovunque la forma completa (es. "Magnet Communication", non "Magnet") in title, schema, profili e directory. Il brand visivo può restare corto; i segnali strutturati no.
3. **Frase-definizione esplicita.** Subito sotto un H1 creativo, una frase *entità + categoria + luogo + servizi* ("X è un'agenzia di comunicazione di Milano specializzata in A, B, C"). Non rovina il tone of voice e risolve gran parte dell'ambiguità.
4. **Una pagina forte per ogni "servizio + città"**, non due mediocri. Title, H1, meta e prima frase della pagina servizio orientati alla query primaria ("Agenzia Brand Identity Milano"), una query principale per pagina, cluster secondari nel corpo.
5. **Entity reinforcement nel footer**: mini-descrizione coerente + link a tutti i servizi su ogni pagina.
6. **Case study strutturati e bidirezionali**: cliente, settore, servizi, brief, intervento, deliverable, risultato; il case linka i servizi e la pagina servizio linka i case. Questo crea il grafo interno *agenzia → servizio → progetto → cliente*.
7. **Money page + libreria informativa**: 20–30 contenuti eccellenti per pillar battono 200 mediocri. I contenuti "come funziona X" sono quelli più citabili.
8. **Pagine autore**: bio, competenze, progetti, articoli firmati, link a LinkedIn/docenze/talk. Gli articoli indicano l'autore.
9. **Schema coerente con un unico `@id`**: in homepage (o nella pagina "chi siamo"; non serve su ogni pagina) il sottotipo più specifico di `LocalBusiness` se c'è una sede fisica (es. `ProfessionalService`), altrimenti `Organization`, con `name`, `legalName`, `alternateName`, `description`, `url`, `logo`, `address`, `telephone`, `email`, `vatID`, `foundingDate`, `sameAs` (LinkedIn, Instagram, Behance, Google Business Profile, directory). `Service` su ogni pagina servizio con `provider` che punta allo stesso `@id`; `BreadcrumbList`; `CreativeWork`/`Article` per i case. I dati strutturati devono corrispondere al testo visibile. `Service` non produce rich result in Google: vale solo come segnale semantico. `FAQPage` non dà più rich result (vedi verifiche sotto).
10. **NAP e descrizione identici ovunque**: stesso nome, indirizzo, telefono e stessa frase-descrizione su sito, Google Business Profile, Bing Places (ChatGPT Search si appoggia in gran parte all'indice Bing), LinkedIn, Clutch/Sortlist/DesignRush, Behance, associazioni di categoria. Non mescolare sede legale e operativa nelle directory. Indicare la geografia reale (es. "Assago, Milano"), mai fingere un indirizzo in città.
11. **Corroborazione esterna come priorità n.1**: profili directory, recensioni autentiche che descrivono il lavoro svolto, e soprattutto **credit sui domini dei clienti/partner** ("creative agency: X"). Una menzione sul sito di un cliente vale più di molte directory generiche.
12. **Nicchia verticale come cavallo di Troia**: invece di inseguire query ipercompetitive ("agenzia comunicazione Milano"), presidia una verticale dove si hanno credenziali reali (nel caso: brand licensing, anche in inglese con `/en/` e `hreflang`). L'autorità costruita lì si trasferisce all'entità e poi agli altri servizi.
13. **Contenuto importante nel DOM**: nomi clienti, servizi, descrizioni e titoli in testo, non dentro canvas, video o immagini; alt descrittivi sulle immagini portfolio; anchor text descrittivi al posto di "Scopri di più"; encoding pulito (accenti e apostrofi).

## Rischi e anti-pattern

- **Doorway page**: decine di landing quasi identiche "agenzia X Milano" accanto alle pagine servizio esistenti producono cannibalizzazione e possono peggiorare il sito. Meglio rafforzare l'URL esistente o fare redirect 301 verso uno slug nuovo.
- **Presidio di città senza sede**: le sezioni per città funzionano quando corrispondono a una presenza reale; altrimenti sono doorway.
- **Classifiche autoreferenziali**: un articolo "migliori agenzie" che mette sé stessi al primo posto **non è una fonte indipendente** e oggi è anche rischioso. Nello studio di Lily Ray (apr–giu 2026, 184 listicle autopromozionali di 146 brand), quando Google AI Overviews citava una di queste liste, il brand autore restava fuori dalle raccomandazioni nel 69% dei casi: la lista finiva per promuovere i concorrenti. Dal gennaio 2026 sono stati osservati cali di visibilità a livello di dominio per i siti che ne pubblicano molte. Le fonti terze vere (testate, directory con recensioni, award) restano il segnale forte.
- **Keyword stuffing nel nome GBP o nei title** ("X Agenzia Comunicazione Milano Brand Identity…"): le linee guida di Google Business Profile vietano di aggiungere keyword, località o slogan al nome, pena sospensione del profilo; e il keyword stuffing misura negativo anche nel paper Princeton (chapter 01).
- **FAQ SEO finte**: servono domande reali con risposte concrete di 40–100 parole. Il valore è nel testo domanda-risposta, non nel markup: da maggio 2026 Google non mostra più i rich result FAQ.
- **Dati autodichiarati presi per buoni**: crescite di traffico o authority pubblicate da un'agenzia sul proprio sito vanno verificate con tool indipendenti.

## Verifiche con fonti (ottobre 2026)

Affermazioni della sessione di analisi controllate su fonti primarie o studi pubblici:

| Affermazione | Esito | Cosa dice la fonte |
|---|---|---|
| Non esiste un markup "GEO" speciale per AI Overviews/AI Mode | ✅ Confermata | Google: nessun requisito aggiuntivo né ottimizzazione speciale; non servono file "AI text" o markup nuovi. Contano crawlability, internal link, page experience, contenuto importante in testo, dati strutturati coerenti col testo visibile, Business Profile aggiornato (doc "AI features and your website", agg. 10 dic 2025) |
| Il traffico da AI Overviews/AI Mode è in Search Console | ✅ Confermata | Incluso nel report Performance, tipo di ricerca "Web", senza filtro separato |
| `Organization` aiuta a disambiguare l'entità | ✅ Confermata | Google: aiuta a capire i dettagli amministrativi e a "disambiguate your organization". Va in homepage o nella pagina "chi siamo", non su ogni pagina. Per un business locale Google raccomanda il sottotipo più specifico di `LocalBusiness` |
| Schema `FAQPage` sulle FAQ | ⚠️ Superata | Rich result FAQ deprecati l'8 mag 2026 e rimossi dalla documentazione il 15 giu 2026. Il markup non dà più risultati visivi in Google; le FAQ restano utili come testo |
| Pagine "agenzia X città" duplicate sono rischiose | ✅ Confermata | Spam policy Google (doorway abuse): cita esplicitamente pagine "targeted at specific regions or cities that funnel users to one page" |
| Nome GBP senza keyword | ✅ Confermata | Linee guida GBP: il nome deve essere quello reale; vietato aggiungere keyword, località, slogan |
| Directory e citazioni esterne contano per gli LLM | ✅ Confermata, con sfumatura | BrightLocal (set 2026, 1,9M citazioni AI su query locali, ChatGPT + AI Mode + AI Overviews): siti dei business 42% delle citazioni, Google Business Profile 28,6%, Yelp 9,5%, altre directory <2% ciascuna; i motori Google pesano molto GBP, ChatGPT più Yelp e Bing. Il sito proprio resta la fonte più citata: la corroborazione esterna si aggiunge, non sostituisce |
| ChatGPT usa Bing per le ricerche locali | ✅ Confermata (studio 2024) | BrightLocal (nov 2024): ChatGPT Search "mostly powered by Bing's Index"; fonti: siti business 58%, menzioni 27%, directory 15%. Da qui l'importanza di Bing Places |
| Classifiche autoreferenziali utili | ❌ Smentita come tattica | Studio Lily Ray 2026 (vedi Rischi): citazione senza raccomandazione nel 69% dei casi, cali di visibilità di dominio |
| I numeri di crescita di Bliss | ❓ Non verificabili | Dichiarati da Bliss sul proprio sito; nessuna fonte indipendente |

Nota per il mercato italiano: gli studi sopra sono su ricerche USA, dove Yelp pesa molto. In Italia il ruolo equivalente lo hanno GBP, Bing Places e le directory di settore realmente usate nel proprio mercato; vale il principio, non la lista.

## KPI GEO per un business locale

Non solo "posizione #1":

- **Branded search** (nome completo, nome + città, nome + verticale).
- **Impression non-branded per cluster** in Search Console, con filtri regex per servizio (`licens|licensee|licensor`, `brand|branding|identity`, `adv|advertising|media`…) e per luogo (`milano|milan|assago`). Il traffico da AI Overviews/AI Mode rientra nei report Search Console di tipo Web.
- **Numero di domini autorevoli che citano l'entità** (mention, anche senza link).
- **Entity consistency**: nome, indirizzo e descrizione identici sulle fonti principali.
- **AI citation testing**: set fisso di prompt "servizio + città" e "migliori agenzie X" ripetuto periodicamente su ChatGPT, Gemini, Perplexity, Google AI Overviews/AI Mode (vedi tool in chapter 04).

## Procedura: gap analysis contro il concorrente che l'AI consiglia

1. Elenca le query "servizio + città" e "migliori X a città" per cui vuoi comparire.
2. Per ognuna, chiedi a 2–3 motori AI e annota chi viene consigliato e quali URL vengono citati.
3. Per il concorrente più ricorrente: quale pagina domina la query, con quale H1/sezione, FAQ, footer, schema.
4. Per il proprio sito: pagina equivalente, cosa manca (frase-definizione, sezione città, FAQ, case collegati, schema, autore), contenuto nuovo da creare.
5. Assegna priorità: 🔴 entità/schema/profili/corroborazione esterna, 🟠 landing e case study, 🟢 verticale dove il concorrente è debole e tu sei forte. È lì che conviene batterlo invece di inseguirlo ovunque.

Formato utile:

| Query | Pagina concorrente | Pagina propria | Gap | Priorità |
|---|---|---|---|---|
| graphic design Milano | landing lunga + sezione "Studio Grafico Milano" + FAQ | pagina servizio | manca sezione città, FAQ di confronto, case testuali | 🔴 |
| licensing Milano | debole | pagina servizio + 21 progetti licensing | opportunità: pillar + articoli + versione EN | 🟢 |

## Key Takeaways
1. Un LLM consiglia chi trova e può corroborare, non necessariamente il migliore: un portfolio più forte non compensa un'entità ambigua e poco citata altrove.
2. La copertura letterale "servizio + città" (heading, sezioni, title) è il motivo per cui un concorrente "esce sempre", anche cambiando città.
3. Frase-definizione in homepage, entity reinforcement nel footer e schema con `@id` condiviso sono gli interventi on-site a costo più basso e impatto più alto.
4. Le fonti terze coerenti (directory, GBP con recensioni, credit sui siti dei clienti) sono la priorità n.1: la stessa descrizione ripetuta da fonti indipendenti costruisce l'entità.
5. Una nicchia verticale credibile è la leva più efficiente per entrare nelle risposte AI; doorway page e classifiche autoreferenziali sono scorciatoie a basso valore probatorio.

## Fonti
- Sessione di analisi con assistente AI (ottobre 2026) su https://www.magnetmilano.it/ e https://blissagency.it/, fornita da Jacopo come caso di ricerca.
- Google Search Central, "AI features and your website": https://developers.google.com/search/docs/appearance/ai-features
- Google Search Central, Organization structured data: https://developers.google.com/search/docs/appearance/structured-data/organization
- Google Search Central, aggiornamenti documentazione (deprecazione FAQ rich result, 2026): https://developers.google.com/search/updates
- Google Search spam policies (doorway abuse): https://developers.google.com/search/docs/essentials/spam-policies
- Linee guida Google Business Profile: https://support.google.com/business/answer/3038177
- BrightLocal, Local AI visibility study (set 2026): https://www.brightlocal.com/research/local-ai-visibility-study/
- BrightLocal, Uncovering ChatGPT Search sources (2024): https://www.brightlocal.com/research/uncovering-chatgpt-search-sources/
- Studio Lily Ray sui listicle autopromozionali (sintesi ALM Corp, 2026): https://almcorp.com/news/self-promotional-listicles-ai-overviews-help-competitors-lily-ray-study/
