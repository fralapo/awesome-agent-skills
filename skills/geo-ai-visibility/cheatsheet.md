# GEO Cheatsheet

## Struttura contenuto
- [ ] Blocco di risposta diretta (40-60 parole) vicino all'inizio di ogni pagina/sezione
- [ ] Heading in forma di domanda per sezioni Q&A
- [ ] Ogni sezione self-contained (comprensibile isolata, come chunk)
- [ ] Entità nominate esplicite invece di pronomi nei passaggi chiave
- [ ] Naming del brand/prodotto coerente in tutto il sito
- [ ] Terminologia tecnica di settore dove appropriato
- [ ] Fluency/leggibilità della prosa curata
- [ ] Nessun keyword stuffing
- [ ] Revisione trimestrale di freshness dei contenuti
- [ ] dateModified aggiornato quando si aggiorna sostanzialmente un contenuto

## Structured data
- [ ] Schema FAQPage su pagine Q&A (facoltativo: da maggio 2026 Google non mostra più i rich result FAQ; conta il testo Q&A)
- [ ] Schema Article/BlogPosting con autore (Person) e dateModified
- [ ] Schema Organization coerente su tutto il sito
- [ ] JSON-LD (non microdata) come formato preferito

## Citabilità
- [ ] Statistiche/dati numerici inseriti dove pertinente
- [ ] Citazioni di fonti autorevoli nel testo
- [ ] Quotazioni di esperti con attribuzione chiara

## Segnali di autorità
- [ ] Digital PR / menzioni su fonti terze indipendenti (Wikipedia/Wikidata, testate di settore)
- [ ] Co-occurrence brand + keyword categoria su siti esterni autorevoli
- [ ] Copertura del topic cluster completo (non solo keyword principale)

## Entità e business locale (vedi chapter 08)
- [ ] Nome completo e non ambiguo usato in title, schema, profili e directory (non la forma corta generica)
- [ ] Frase-definizione sotto l'H1 della homepage: entità + categoria + luogo + servizi
- [ ] Mini-descrizione dell'entità + link ai servizi nel footer di ogni pagina
- [ ] Una pagina forte per ogni query "servizio + città" (title/H1/prima frase espliciti), nessuna doorway duplicata
- [ ] Sezioni per città solo dove c'è una sede o presenza reale
- [ ] Sottotipo `LocalBusiness` più specifico (o Organization) in homepage con `@id` unico, `alternateName`, `address`, `sameAs`; `Service` con `provider` → stesso `@id`; `BreadcrumbList`
- [ ] NAP e descrizione identici su sito, Google Business Profile, Bing Places, LinkedIn, directory (Clutch, Sortlist, DesignRush…)
- [ ] Case study testuali (cliente → problema → intervento → servizi → risultato) linkati da e verso le pagine servizio
- [ ] Pagine autore/team con bio, competenze, progetti e link esterni
- [ ] Contenuti informativi a supporto di ogni money page
- [ ] Credit/menzioni sui siti di clienti e partner; recensioni autentiche
- [ ] Verticale di nicchia presidiata dove si hanno credenziali reali
- [ ] Nessuna classifica "migliori X" che mette sé stessi al primo posto

## Tecnico / llms.txt
- [ ] robots.txt non blocca crawler AI (GPTBot, PerplexityBot, ClaudeBot, Google-Extended)
- [ ] Contenuto critico non dipende da client-side rendering
- [ ] Velocità di caricamento e crawlability solide
- [ ] llms.txt presente e sincronizzato con i contenuti reali
- [ ] Sitemap.xml aggiornata

## Note per piattaforma
- [ ] Tool AI-visibility attivo (Otterly/Peec/Profound/AthenaHQ)
- [ ] Monitoraggio per piattaforma separata (ChatGPT, Perplexity, Google AIO hanno domini diversi)
- [ ] Tracking sentiment e non solo presenza/frequenza della menzione
