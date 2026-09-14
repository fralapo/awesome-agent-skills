# Chapter 6: Checklist e Best Practice

## Core Idea
Le best practice GEO che emergono dalle guide del settore (HubSpot, Ahrefs, agenzie specializzate) si raggruppano in poche categorie coerenti — fondamenta tecniche, structured data, struttura del contenuto, qualità editoriale, autorità off-site, manutenzione, misurazione — e ognuna corregge un anti-pattern specifico e ricorrente.

## Checklist consolidata

### Fondamenta tecniche
- **robots.txt non deve bloccare i crawler AI** (GPTBot, PerplexityBot, ClaudeBot, Google-Extended, ecc.). (fonte: research/08-checklist-best-practice.md)
- **Il contenuto critico non deve dipendere dal client-side rendering.** (fonte: research/08-checklist-best-practice.md)
- **Velocità di caricamento e crawlability solide** — prerequisito SEO classico che resta valido per il GEO. (fonte: research/08-checklist-best-practice.md)
- **llms.txt presente e sincronizzato** con i contenuti reali del sito (vedi chapter su llms.txt/standard). (fonte: research/08-checklist-best-practice.md)
- **Sitemap.xml aggiornata.** (fonte: research/08-checklist-best-practice.md)

### Structured data
- **Schema FAQPage** su pagine Q&A. (fonte: research/08-checklist-best-practice.md)
- **Schema Article/BlogPosting** con autore (`Person`) e `dateModified`. (fonte: research/08-checklist-best-practice.md)
- **Schema Organization coerente** su tutto il sito. (fonte: research/08-checklist-best-practice.md)
- **JSON-LD** (non microdata) come formato preferito. (fonte: research/08-checklist-best-practice.md)

### Struttura contenuto
- **Blocco di risposta diretta (40-60 parole)** vicino all'inizio di ogni pagina/sezione. (fonte: research/08-checklist-best-practice.md)
- **Heading in forma di domanda** per le sezioni Q&A. (fonte: research/08-checklist-best-practice.md)
- **Ogni sezione self-contained**, comprensibile anche isolata, come un chunk. (fonte: research/08-checklist-best-practice.md)
- **Entità nominate esplicite** invece di pronomi nei passaggi chiave. (fonte: research/08-checklist-best-practice.md)
- **Naming del brand/prodotto coerente** in tutto il sito. (fonte: research/08-checklist-best-practice.md)

### Qualità del contenuto (leve ad alto impatto misurato)
- **Statistiche/dati numerici** inseriti dove pertinente — leva con impatto misurato fino a +40% (ceiling). (fonte: research/08-checklist-best-practice.md)
- **Citazioni di fonti autorevoli** nel testo. (fonte: research/08-checklist-best-practice.md)
- **Quotazioni di esperti con attribuzione chiara** — impatto misurato +28%. (fonte: research/08-checklist-best-practice.md)
- **Terminologia tecnica di settore** dove appropriato. (fonte: research/08-checklist-best-practice.md)
- **Fluency/leggibilità della prosa** curata. (fonte: research/08-checklist-best-practice.md)
- **Nessun keyword stuffing.** (fonte: research/08-checklist-best-practice.md)

### Autorità esterna / off-site
- **Digital PR / menzioni su fonti terze indipendenti** (Wikipedia/Wikidata se pertinente, testate di settore). (fonte: research/08-checklist-best-practice.md)
- **Co-occurrence brand + keyword di categoria** su siti esterni autorevoli. (fonte: research/08-checklist-best-practice.md)
- **Copertura del topic cluster completo** (non solo la keyword principale) per beneficiare del query fan-out di Google. (fonte: research/08-checklist-best-practice.md)

### Manutenzione / freshness
- **Revisione trimestrale di freshness** dei contenuti. (fonte: research/08-checklist-best-practice.md)
- **`dateModified` aggiornato** quando si aggiorna sostanzialmente un contenuto. (fonte: research/08-checklist-best-practice.md)

### Misurazione
- **Tool AI-visibility attivo** (almeno uno tra Otterly/Peec/Profound/AthenaHQ). (fonte: research/08-checklist-best-practice.md)
- **Monitoraggio per piattaforma separata** — ChatGPT ≠ Perplexity ≠ Google AIO, overlap misurato solo all'11%. (fonte: research/08-checklist-best-practice.md)
- **Tracking di sentiment**, non solo presenza/frequenza della menzione. (fonte: research/08-checklist-best-practice.md)

## Anti-pattern

1. **Ottimizzare solo citazioni linkate, ignorando le brand mention** — ciò che sposta l'ago in contesti commerciali è spesso la menzione del brand per nome, non il link; concentrarsi solo su schema/struttura e ignorare il lavoro editoriale/PR che genera menzioni è un errore diffuso. (fonte: research/08-checklist-best-practice.md)
2. **Trattare le unlinked mention come irrilevanti** — ogni menzione esterna del brand va trattata come segnale di citazione, con o senza link. (fonte: research/08-checklist-best-practice.md)
3. **Nessuna validazione di terze parti** — gli LLM apprendono l'autorevolezza via consenso cross-web; senza menzioni indipendenti su fonti terze il modello non può "verificare" il brand, quindi niente citazione indipendentemente dalla qualità del sito proprio. (fonte: research/08-checklist-best-practice.md)
4. **Naming/entità incoerente** — se il nome del brand appare in forme diverse/scritture incoerenti nel sito e sui profili esterni, rischia di essere trattato come frase generica invece che come entità distinta. (fonte: research/08-checklist-best-practice.md)
5. **Ignorare i segnali di co-occurrence** — nome brand + keyword di categoria nello stesso paragrafo su siti terzi autorevoli è un segnale importante che manca spesso nelle strategie. (fonte: research/08-checklist-best-practice.md)
6. **Assumere che ranking Google = visibilità AI** — errore diffuso: pensare che il posizionamento SEO tradizionale si traduca automaticamente in citazioni AI, smentito dal calo dal 76% al 38% di overlap con il top-10 Google (vedi chapter 05). (fonte: research/08-checklist-best-practice.md)
7. **Keyword stuffing**, residuo di pratiche SEO datate — misurabilmente controproducente nei motori generativi. (fonte: research/08-checklist-best-practice.md)
8. **Bloccare involontariamente i crawler AI via robots.txt** — controllo tecnico basilare spesso saltato. (fonte: research/08-checklist-best-practice.md)
9. **Contenuto solo client-side rendered** — i crawler AI spesso non eseguono JS in modo affidabile, quindi il contenuto diventa invisibile. (fonte: research/08-checklist-best-practice.md)

## Key Takeaways
1. La checklist GEO si raggruppa in sei aree: fondamenta tecniche, structured data, struttura contenuto, qualità editoriale, autorità off-site, manutenzione/freshness, misurazione. (fonte: research/08-checklist-best-practice.md)
2. Le leve di contenuto con impatto misurato più alto restano statistiche/dati (ceiling +40%) e quotazioni di esperti con attribuzione (+28%). (fonte: research/08-checklist-best-practice.md)
3. Nove anti-pattern ricorrono nelle guide di settore, e il più citato è l'assunzione errata che il ranking Google tradizionale garantisca automaticamente visibilità AI. (fonte: research/08-checklist-best-practice.md)
4. La misurazione va fatta per piattaforma separata: l'overlap tra domini citati da ChatGPT e Perplexity è solo dell'11%, quindi un solo tool o un solo canale non basta. (fonte: research/08-checklist-best-practice.md)

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
