# GEO Cheatsheet

## Content structure
- [ ] Direct-answer block (40-60 words) near the start of every page/section
- [ ] Headings phrased as questions for Q&A sections
- [ ] Every section self-contained (understandable in isolation, like a chunk)
- [ ] Explicit named entities instead of pronouns in key passages
- [ ] Consistent brand/product naming across the whole site
- [ ] Technical industry terminology where appropriate
- [ ] Fluent, readable prose
- [ ] No keyword stuffing
- [ ] Quarterly freshness review of content
- [ ] dateModified updated whenever content is substantially revised

## Structured data
- [ ] FAQPage schema on Q&A pages (optional: since May 2026 Google no longer shows FAQ rich results; the Q&A text is what counts)
- [ ] Article/BlogPosting schema with author (Person) and dateModified
- [ ] Consistent Organization schema across the whole site
- [ ] JSON-LD (not microdata) as the preferred format

## Citability
- [ ] Statistics/numerical data added where relevant
- [ ] Citations of authoritative sources in the text
- [ ] Expert quotations with clear attribution

## Authority signals
- [ ] Digital PR / mentions on independent third-party sources (Wikipedia/Wikidata, trade publications)
- [ ] Co-occurrence of brand + category keyword on authoritative external sites
- [ ] Coverage of the full topic cluster (not only the main keyword)

## Entity and local business (see [chapter 8](chapters/ch08-entity-geo-for-local-service-businesses.md))
- [ ] Full, unambiguous name used in titles, schema, profiles and directories (not the generic short form)
- [ ] Definition sentence under the homepage H1: entity + category + place + services
- [ ] Entity mini-description + links to the services in the footer of every page
- [ ] One strong page for each "service + city" query (explicit title/H1/first sentence), no duplicated doorway pages
- [ ] City sections only where there is a real office or presence
- [ ] Most specific `LocalBusiness` subtype (or Organization) on the homepage with a single `@id`, `alternateName`, `address`, `sameAs`; `Service` with `provider` → same `@id`; `BreadcrumbList`
- [ ] Identical NAP and description on the site, Google Business Profile, Bing Places, LinkedIn, directories (Clutch, Sortlist, DesignRush…)
- [ ] Textual case studies (client → problem → intervention → services → result) linked to and from the service pages
- [ ] Author/team pages with bio, skills, projects and external links
- [ ] Informational content supporting every money page
- [ ] Credits/mentions on client and partner sites; authentic reviews
- [ ] A niche vertical owned where the business has real credentials
- [ ] No "best X" ranking that puts its own author in first place

## Technical / llms.txt
- [ ] robots.txt does not block AI crawlers (GPTBot, PerplexityBot, ClaudeBot, Google-Extended)
- [ ] Critical content does not depend on client-side rendering
- [ ] Solid load speed and crawlability
- [ ] llms.txt present and in sync with the real content
- [ ] Up-to-date sitemap.xml

## Per-platform notes
- [ ] An active AI-visibility tool (Otterly/Peec/Profound/AthenaHQ)
- [ ] Separate monitoring per platform (ChatGPT, Perplexity and Google AIO cite different domains)
- [ ] Sentiment tracking, not only presence/frequency of the mention
