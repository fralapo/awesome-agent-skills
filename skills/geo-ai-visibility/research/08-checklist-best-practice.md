# Errori comuni, anti-pattern e checklist pratiche

## Errori comuni / anti-pattern GEO

1. **Ottimizzare solo citazioni linkate, ignorare le brand mention**
   Ciò che sposta l'ago in contesti commerciali è spesso la **menzione del brand per nome**, non il link. Focalizzarsi solo su schema/struttura pagina e ignorare il lavoro editoriale/PR che genera menzioni è un errore diffuso.

2. **Trattare le unlinked mention come irrilevanti**
   Ogni menzione esterna del brand va trattata come segnale di citazione, con o senza link.

3. **Nessuna validazione di terze parti**
   Gli LLM apprendono l'autorevolezza via **consenso cross-web**. Senza menzioni indipendenti su fonti terze, il modello non può "verificare" il brand → niente citazione, indipendentemente dalla qualità del sito proprio.

4. **Naming/entità incoerente**
   Se il nome del brand appare in forme diverse/scritture incoerenti nel sito e sui profili esterni, rischia di essere trattato come frase generica invece che entità distinta.

5. **Ignorare i segnali di co-occurrence**
   Nome brand + keyword di categoria nello stesso paragrafo su siti terzi autorevoli è un segnale importante che manca spesso nelle strategie.

6. **Assumere che ranking Google = visibilità AI**
   Errore diffuso: pensare che il posizionamento SEO tradizionale si traduca automaticamente in citazioni AI. Falso (vedi calo dal 76% al 38% di overlap con top-10 Google, file 07).

7. **Keyword stuffing** (residuo di pratiche SEO datate)
   Controproducente e misurabilmente dannoso nei motori generativi (vedi dati file 01/07).

8. **Bloccare involontariamente i crawler AI via robots.txt**
   Controllo tecnico basilare spesso saltato.

9. **Contenuto solo client-side rendered**
   I crawler AI spesso non eseguono JS in modo affidabile → contenuto invisibile.

## Checklist pratica riassuntiva (sintesi da più fonti: HubSpot, Ahrefs, Semrush-style guide, agenzie GEO)

### Fondamenta tecniche
- [ ] robots.txt non blocca crawler AI (GPTBot, PerplexityBot, ClaudeBot, Google-Extended, ecc.)
- [ ] Contenuto critico non dipende da client-side rendering
- [ ] Velocità di caricamento e crawlability solide (prerequisito SEO classico)
- [ ] llms.txt presente e sincronizzato con i contenuti reali (vedi file 05)
- [ ] Sitemap.xml aggiornata

### Structured data
- [ ] Schema **FAQPage** su pagine Q&A
- [ ] Schema **Article/BlogPosting** con autore (`Person`) e `dateModified`
- [ ] Schema **Organization** coerente su tutto il sito
- [ ] JSON-LD (non microdata) come formato preferito

### Struttura contenuto
- [ ] Blocco di risposta diretta (**40-60 parole**) vicino all'inizio di ogni pagina/sezione
- [ ] Heading in forma di domanda per sezioni Q&A
- [ ] Ogni sezione **self-contained** (comprensibile isolata, come chunk)
- [ ] Entità nominate esplicite invece di pronomi nei passaggi chiave
- [ ] Naming del brand/prodotto **coerente** in tutto il sito

### Qualità del contenuto (leve ad alto impatto misurato)
- [ ] Statistiche/dati numerici inseriti dove pertinente (+40% ceiling)
- [ ] Citazioni di fonti autorevoli nel testo
- [ ] Quotazioni di esperti con attribuzione chiara (+28% misurato)
- [ ] Terminologia tecnica di settore dove appropriato
- [ ] Fluency/leggibilità della prosa curata
- [ ] Nessun keyword stuffing

### Autorità esterna / off-site
- [ ] Digital PR / menzioni su fonti terze indipendenti (Wikipedia/Wikidata se pertinente, testate di settore)
- [ ] Co-occurrence brand + keyword categoria su siti esterni autorevoli
- [ ] Copertura del topic cluster completo (non solo keyword principale) per beneficiare del query fan-out di Google

### Manutenzione / freshness
- [ ] Revisione trimestrale di freshness dei contenuti
- [ ] `dateModified` aggiornato quando si aggiorna sostanzialmente un contenuto

### Misurazione
- [ ] Tool AI-visibility attivo (almeno uno tra Otterly/Peec/Profound/AthenaHQ — vedi file 06)
- [ ] Monitoraggio **per piattaforma separata** (ChatGPT ≠ Perplexity ≠ Google AIO — overlap solo 11%)
- [ ] Tracking sentiment e non solo presenza/frequenza della menzione

## Fonti
- https://www.seobrand.com/blog/10-mistakes-that-are-killing-your-ai-visibility/
- https://aisearch.similarweb.com/blog/geo-mistakes/
- https://www.cnabke.com/en/blogs/geo-mentions-linkless-ai-visibility.html
- https://www.entrepreneur.com/building-a-business/marketing/5-mistakes-that-are-quietly-destroying-your-ai-visibility
- https://cxl.com/blog/aeo-geo-seo-reality-check/
- https://genixly.io/blogs/common-geo-mistakes-to-avoid-ai-ecommerce
- https://trackmyvisibility.com/blogs/ai-seo/common-geo-mistakes-brands-make/
- https://blog.hubspot.com/marketing/generative-engine-optimization-best-practices
- https://directiveconsulting.com/blog/a-guide-to-generative-engine-optimization-geo-best-practices/
- https://www.pageoptimizer.pro/blog/generative-engine-optimization-geo-checklist
- https://www.erlin.ai/blog/generative-engine-optimization-checklist
