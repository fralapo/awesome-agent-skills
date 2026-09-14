# Citazioni dirette e tecniche actionable (materiale grezzo da video)

Estratti parola per parola dai transcript in `Downloads/geo/`, per riuso diretto in cheatsheet/patterns futuri.

## Definizioni memorabili

> "SEO optimises for a ranked list of links. GEO optimises for a synthesised answer." — Kaliber (Rob)

> "SEO is like saying put me on the stage and GEO is like saying make me the script the speaker reads from." — Vendasta

> "SEO gets you found. AEO makes you the answer. GEO gets you recommended." — Niko, AI Ranking

> "SEO gets you ranked while GEO gets you quoted." — Hostinger Academy

> "The biggest threat to you and your business right now isn't AI replacing you. It's AI ignoring you." — Silicon Valley Girl (Marina Mogilko)

> "influence matters more than authorship now." — Vendasta

> "82% of what AI cites is earned media. Earned media means other people talking about you not you talking about yourself." — Silicon Valley Girl

> "whether you call it GEO, LLMO, or AEO… it all boils down to just doing good SEO." — Ryan Law (Ahrefs), citato in Surfer Academy

> "People are going to hate me, but it's build a better business." — esperto SEO anonimo, Ahrefs "Top SEO Experts" video

> "if you want to dramatically increase your AI visibility, getting your brand mentioned on YouTube is one of the highest impact moves you can make." — Ahrefs, "Learn 80% of AEO"

## Tecniche actionable — struttura del contenuto

- **BLUF (Bottom Line Up Front)**: "start every section with the answer, not the backstory. Both humans and AI weigh the beginning and end of a passage more heavily than the middle." (Ahrefs)
- **Atomic content**: "every section on your page should be able to stand on its own... AI chunks your content into pieces when it processes it, and you can't control where the chunks fall." (Ahrefs)
- **Entity-rich writing**: sostituire "This tool helps with SEO" con "Ahrefs Keywords Explorer helps you find keywords with low difficulty and high traffic potential." (Ahrefs)
- **Simple & declarative**: "Write one idea per sentence in clear subject-verb-object structure. A good litmus test is that if a sentence takes two reads to understand, it's too complex." (Ahrefs)
- **Capsule Content Technique** (Niko): H2 formulato come domanda diretta, risposta immediata sotto senza preamboli. Esempio cattivo: "In today's digital landscape, businesses are increasingly looking for ways to improve yada yada yada." Esempio buono: "Technical SEO is the process of optimizing your website infrastructure so that search engines can crawl, index, and rank your pages effectively."
- **Answer-first rewrite (Kaliber)**: "if a page is answering 'What is GEO?', the first sentence should clearly define GEO. Not open with five lines of context."
- Checklist Hostinger: scrivere in Q&A chiaro; ogni paragrafo standalone e completo; includere esempi specifici e dati; linguaggio autorevole ma accessibile; aggiungere contesto facilmente estraibile.

## Tecniche actionable — tecnico/crawling

- Controllare `dominio.com/robots.txt` per **GPTBot** (OpenAI), **OAI-SearchBot**, **ClaudeBot**, **Google-Extended**, **Bingbot** — non disallow accidentale.
- **Attenzione a Cloudflare**: feature "Block AI Bots via robots.txt" attiva **di default** su molti piani → blocca involontariamente i crawler AI.
- Contenuto chiave deve stare in **HTML puro / testo statico pre-renderizzato**, non dietro interazione JS: "AI systems primarily read your raw HTML. If your key information only appears after a JavaScript interaction, AI might miss it entirely." (Surfer)
- **ChatGPT Search usa l'indice di Bing** → serve sitemap su Bing Webmaster Tools, non solo Google Search Console.
- Alt text descrittivo per immagini, trascrizioni complete per video/podcast.
- Diagnosi rapida: "take your URL, paste it into whatever chatbot you're using, and ask it how visible you are in AI search, and what's stopping you from showing up." (Silicon Valley Girl) — tecnica: mandare l'URL a Claude/ChatGPT e chiedere un audit di leggibilità.

## Tecniche actionable — schema/structured data

- **Organization schema**: nome, logo, social profile → aiuta l'entity resolution nel knowledge graph.
- **Article schema**: data di pubblicazione, autore, headline → segnali di rilevanza/credibilità.
- **Service schema specifico per pagina** (per business locali multi-servizio), diverso da pagina a pagina.
- Presenza su **Wikidata** anche senza pagina Wikipedia piena — campo "instance of" deve descrivere correttamente cosa sei (case reale: cambiare da "vlogger/YouTuber" a "podcast host, entrepreneur, angel investor" ha sbloccato citazioni Gemini corrette).
- Coerenza NAP (Name/Address/Phone) e descrizioni **identiche parola per parola** su tutte le piattaforme (Apple Podcasts, Spotify, directory locali ecc.) — "when the sources disagree, the models play safe and name someone else. When all three say the same sentence, it repeats your sentence back."

## Tecniche actionable — autorità/off-site

- **Consensus**: un claim solo sul proprio sito è debole; lo stesso claim ripetuto su sito + terze parti + recensioni + comparison page diventa affidabile. "Your authority has to be distributed. Not just sitting on your own domain." (Kaliber)
- **3 tier di menzioni esterne** (Ahrefs): Tier 1 editoriale terzo (review site, listicle su blog autorevoli — più difficile, più prezioso); Tier 2 UGC (Reddit — "one of the most frequently cited sources by ChatGPT", Quora, forum nicchia); Tier 3 proprietà proprie (YouTube, podcast, LinkedIn).
- **YouTube come leva prioritaria**: dominio più citato nelle AI Overviews Google; correlazione 0.737 con visibilità ChatGPT (la più forte misurata). Strategia: creare "search hits" evergreen (non viral hit) — keyword nel titolo + prime righe descrizione + capitoli + dire la keyword a voce nel video.
- **Comparison page "identity-based"**: non solo "A vs B" generico ma targettizzato per persona (es. "QuickBooks alternative for graphic designers") — sfrutta il fatto che i modelli spesso "sanno" chi è l'utente nella sessione.
- Per nuovi player senza budget: listicle a 3 vie (piggyback sul confronto tra due big), o comprare/sponsorizzare gli stessi link dove sponsorizzano i competitor (individuabili con filtro "sponsored link" nei tool backlink).
- Fonte insight non ovvi: caricare **trascrizioni di sales call/conversazioni reali** su un LLM e chiedere analisi tipo market research (paure, obiezioni, cosa conta per il cliente) — sostituisce/integra la keyword research classica, perché i prompt sono ~5x più lunghi delle keyword e contengono più contesto reale.

## Tecniche actionable — audit e misurazione

- **20-Minute GEO Audit** (Kaliber): aprire ChatGPT, Claude, Perplexity, Google AI Overview → lanciare le top 5 query informazionali/di categoria (mai query col nome del brand) → verificare: appari? come sei descritto? quali competitor citati al posto tuo? confrontare col ranking SEO classico per capire se il problema è di copertura o di struttura/autorità.
- **AI filter per keyword research** (Ahrefs): per ogni keyword chiedersi "un AI Overview può soddisfare completamente questa query da solo?" — se sì, ripensare l'obiettivo da "click" a "menzione dentro la risposta".
- **3 metriche da tracciare in assenza di Search Console-level data**: AI referral traffic (sottostimato — non tutte le piattaforme passano referral pulito); AI bot activity sul sito (i bot "di citazione" che rileggono pagine specifiche segnalano probabile uso come fonte); self-reported attribution ("come ci hai trovato?" in sign-up/checkout).
- Tool nominati esplicitamente nei video: **Surfer AI Tracker**, **Ahrefs Brand Radar**, **Ahrefs Web Analytics** (con integrazione Cloudflare per bot tracking), **Peec AI** (peecai.com — multi-engine: Google, AI Overview, ChatGPT, Perplexity; mostra le keyword interne cercate dal modello).
