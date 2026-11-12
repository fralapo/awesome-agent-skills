# Chapter 8: Entity GEO for Local Service Businesses — the Agency A vs Agency B Case

## Core Idea
An LLM does not recommend the "best" company. It recommends the one that retrieval returns with enough evidence to cite it with confidence. For a local service business (agency, studio, consultancy), visibility in AI answers depends on three things, in this order: (1) the entity is **disambiguated** and can be reconstructed as *name → category → place → services → proof*; (2) there is a **page that answers literally** every "service + city" phrasing; (3) **independent third-party sources** confirm the same description. The case below shows an agency with a stronger portfolio left out of the answers and a competitor recommended almost every time, for entirely structural reasons.

> **Note on the source.** The case comes from a research session with an AI assistant (ChatGPT with web search, October 2026) on the public websites of two real agencies, anonymised here as Agency A and Agency B. The observations about the sites are those reported in that session and describe the sites as they were on that date. The traffic figures quoted for Agency B are **the company's own statements**, not verified with independent tools. Use the case as a reasoned example, not as measured data.

## The case: the starting question

A series of comparative queries ("brand identity agencies in [city]", "graphic design [city]", "ADV and media [city]", "web and digital strategy [city]") produced lists of agencies in which **Agency A** never appeared, while **Agency B** appeared almost every time, even when the city in the query changed.

- **Agency A** is a mid-size communication agency located in the metropolitan area of a large city. It offers six services (marketing strategy, brand identity, graphic design, licensing, ADV & media, web & digital) and has a licensing vertical, with a portfolio that includes well-known consumer and entertainment brands.
- **Agency B** is a communication and marketing agency with offices in two major cities.

Diagnosis: this is not a judgement of quality. In the sources retrieved first, other competitors were simply easier to find and corroborate. GEO means first of all **entering the right retrieval set**, and only then persuading.

## Why the excluded agency did not surface (Agency A)

The site already had a good base: a vertical page for each of the 6 services, FAQs, linked projects, and some titles already in the "service + city" format. The problems were elsewhere:

- **Entity ambiguity.** The agency's short name plus the city also returned other, unrelated organisations with the same name, one of them with a division carrying the same full name, plus other similar domains. The right site surfaced when starting from the domain, much less when the engine had to work out *by itself* which organisation of that name was the agency.
- **"Brand first" hero.** A creative H1 (a tagline about the brand) with no sentence saying who/where/what. The engine has to reconstruct it from elements scattered further down the page.
- **Weak external corroboration.** For the competitors, retrieval found directories, rankings, partner profiles and articles describing them. For Agency A it found almost only the agency's own site. An excellent primary source, but no second or third independent source.
- **Portfolio as a gallery.** Strong logos and images, little text. A retrieval engine does not "see" a carousel of logos; it sees (or fails to see) the relation *agency → did X for client Y with service Z*.
- **No informational content.** Six commercial landing pages, no library of articles demonstrating competence on the topics (topical authority).
- **Anonymous team.** Name + role, with no bio, skills or external links: no *person → skill → agency* network.
- **Under-used company profiles.** A LinkedIn page with the correct category and location but a thin description, not aligned with the current offer.

## Why the competitor surfaced everywhere (Agency B)

Agency B built its site as a **commercial knowledge graph**, openly oriented to SEO + GEO: its SEO page explicitly discusses customers asking an AI assistant for recommendations, and its marketing menu lists GEO/AI optimisation as a service.

| Lever | How Agency B uses it | Why it works in retrieval |
|---|---|---|
| **Query coverage** | An indexable surface for almost every commercial phrasing: communication agency, marketing agency, graphic design studio, web agency, SEO, brand strategy, each one paired with both of its cities | For "graphic design studio + city" there is literally a section with that title: the engine does not have to infer anything |
| **Cities written everywhere, with real offices** | A sub-section per city in the landing pages, physical offices declared in both cities, a description of the sectors of each local market | A direct match *company → physical office → city*; the geographic coverage is not a doorway page |
| **Long, all-encompassing pages** | The graphic design landing covers brand/visual identity, typography, palette, CGI, social visuals, brochures, print, brand book, the difference between a graphic design studio and a creative agency, FAQ | A single URL is associated with dozens of concepts without jumps between pages |
| **Retrieval-friendly FAQs** | Real comparison questions ("what is the difference between logo, brand identity and visual identity?") with discursive answers | Question-answer units ready to be extracted |
| **Entity reinforcement in the footer** | The same definition sentence (name + the list of advisory, strategy and communication services + "with offices in" its two cities) on every page | Whatever URL the crawler hits, it finds the full definition of the entity |
| **Money page + informational page** | A commercial *Brand Strategy* landing + a long guide ("Brand strategy: what it is, how to build it…") with a table of contents, an author and a reading time | Covers both purchase intent and informational intent; AI engines cite the second more easily |
| **Textual case studies** | A *previous situation → problems → intervention → results* structure with metrics | The engine infers competence from proof, not from a self-declaration |
| **People as proof** | Head of SEO, CDO, Head of Video, Head of Copy with professional descriptions and signed articles | A *service → person → role* network useful for E-E-A-T and entity building |
| **Freshness** | Articles published in the weeks before the analysis | Signals a live domain that keeps expanding its corpus |
| **"Best agencies" rankings** | Articles of the "top 10 agencies for SEO/branding in the country" type, with itself in 1st place | Intercepts "best agencies for X" queries — **but see the risks below** |

Summary of the comparison: Agency A won on portfolio, vertical specialisation (licensing) and brand. Agency B won on landing pages, informational content, city targeting, FAQs, textual case studies, entity reinforcement, team, freshness, keyword coverage and intentional GEO.

## Generalisable principles

1. **Retrieval before persuasion.** If the entity is not in the set of retrieved documents, quality does not count. The first question of a local GEO audit is: *for the query "service + city", which of my pages is retrieved?*
2. **Disambiguate the entity.** If the name is generic, use the full form everywhere (e.g. "Name Communication", not just "Name") in titles, schema, profiles and directories. The visual brand can stay short; the structured signals cannot.
3. **An explicit definition sentence.** Right below a creative H1, one sentence with *entity + category + place + services* ("X is a communication agency in [city] specialised in A, B, C"). It does not damage the tone of voice and resolves most of the ambiguity.
4. **One strong page for each "service + city"**, not two mediocre ones. Title, H1, meta and first sentence of the service page oriented to the primary query ("Brand Identity Agency [city]"), one main query per page, secondary clusters in the body.
5. **Entity reinforcement in the footer**: a consistent mini-description + links to all services on every page.
6. **Structured, bidirectional case studies**: client, sector, services, brief, intervention, deliverables, result. The case links to the services and the service page links to the cases. This creates the internal graph *agency → service → project → client*.
7. **Money page + informational library**: 20–30 excellent pieces per pillar beat 200 mediocre ones. "How X works" content is the most citable.
8. **Author pages**: bio, skills, projects, signed articles, links to LinkedIn, teaching and talks. Articles name their author.
9. **Consistent schema with a single `@id`**: on the homepage (or the "about" page; it is not needed on every page) the most specific `LocalBusiness` subtype if there is a physical office (e.g. `ProfessionalService`), otherwise `Organization`, with `name`, `legalName`, `alternateName`, `description`, `url`, `logo`, `address`, `telephone`, `email`, `vatID`, `foundingDate`, `sameAs` (LinkedIn, Instagram, Behance, Google Business Profile, directories). `Service` on every service page with `provider` pointing to the same `@id`; `BreadcrumbList`; `CreativeWork`/`Article` for the cases. Structured data must match the visible text. `Service` does not produce a rich result in Google: it only counts as a semantic signal. `FAQPage` no longer gives a rich result (see the checks below).
10. **Identical NAP and description everywhere**: the same name, address, phone and the same description sentence on the site, Google Business Profile, Bing Places (ChatGPT Search relies largely on Bing's index), LinkedIn, Clutch/Sortlist/DesignRush, Behance and trade associations. Do not mix registered office and operating office in directories. State the real geography (e.g. "[suburb], [city]"); never fake an address in the city.
11. **External corroboration as priority no. 1**: directory profiles, authentic reviews that describe the work done, and above all **credits on client and partner domains** ("creative agency: X"). A mention on a client's site is worth more than many generic directories.
12. **A vertical niche as a Trojan horse**: instead of chasing hyper-competitive queries ("communication agency [city]"), own a vertical where the business has real credentials (in the case: brand licensing, also in English with an `/en/` section and `hreflang` where the main site is in another language). The authority built there transfers to the entity and then to the other services.
13. **Important content in the DOM**: client names, services, descriptions and titles as text, not inside canvas, video or images; descriptive alt text on portfolio images; descriptive anchor text instead of "Learn more"; clean encoding (accents and apostrophes).

## Risks and anti-patterns

- **Doorway pages**: dozens of near-identical "agency X [city]" landings next to the existing service pages cause cannibalisation and can make the site worse. It is better to strengthen the existing URL or 301-redirect to a new slug.
- **City coverage without an office**: city sections work when they correspond to a real presence; otherwise they are doorways.
- **Self-ranking lists**: a "best agencies" article that puts its own author in first place **is not an independent source** and is now also risky. In Lily Ray's study (Apr–Jun 2026, 184 self-promotional listicles from 146 brands), when Google AI Overviews cited one of these lists, the authoring brand was left out of the recommendations in 69% of cases: the list ended up promoting competitors. Since January 2026, domain-level visibility drops have been observed for sites that publish many of them. Real third-party sources (publications, directories with reviews, awards) remain the strong signal.
- **Keyword stuffing in the GBP name or in titles** ("X Communication Agency [city] Brand Identity…"): the Google Business Profile guidelines forbid adding keywords, locations or slogans to the name, on pain of profile suspension; and keyword stuffing also measures negative in the Princeton paper ([chapter 1](ch01-definitions-and-history.md)).
- **Fake SEO FAQs**: what is needed is real questions with concrete answers of 40–100 words. The value is in the question-answer text, not in the markup: since May 2026 Google no longer shows FAQ rich results.
- **Self-declared data taken at face value**: traffic or authority growth published by an agency on its own site has to be verified with independent tools.

## Checks against sources (October 2026)

Claims from the analysis session, checked against primary sources or public studies:

| Claim | Outcome | What the source says |
|---|---|---|
| There is no special "GEO" markup for AI Overviews/AI Mode | ✅ Confirmed | Google: no additional requirements and no special optimisation; no "AI text" files or new markup are needed. What counts: crawlability, internal links, page experience, important content in text, structured data consistent with the visible text, an up-to-date Business Profile ("AI features and your website" doc, updated 10 Dec 2025) |
| Traffic from AI Overviews/AI Mode is in Search Console | ✅ Confirmed | Included in the Performance report, search type "Web", with no separate filter |
| `Organization` helps disambiguate the entity | ✅ Confirmed | Google: it helps to understand administrative details and to "disambiguate your organization". It goes on the homepage or the "about" page, not on every page. For a local business Google recommends the most specific `LocalBusiness` subtype |
| `FAQPage` schema on FAQs | ⚠️ Outdated | FAQ rich results were deprecated on 8 May 2026 and removed from the documentation on 15 Jun 2026. The markup no longer produces visual results in Google; FAQs remain useful as text |
| Duplicated "agency X city" pages are risky | ✅ Confirmed | Google spam policy (doorway abuse): it explicitly mentions pages "targeted at specific regions or cities that funnel users to one page" |
| GBP name without keywords | ✅ Confirmed | GBP guidelines: the name must be the real one; adding keywords, locations or slogans is forbidden |
| Directories and external citations count for LLMs | ✅ Confirmed, with nuance | BrightLocal (Sep 2026, 1.9M AI citations on local queries, ChatGPT + AI Mode + AI Overviews): business websites 42% of citations, Google Business Profile 28.6%, Yelp 9.5%, other directories <2% each; Google's engines weigh GBP heavily, ChatGPT weighs Yelp and Bing more. The business's own site remains the most cited source: external corroboration adds to it, it does not replace it |
| ChatGPT uses Bing for local searches | ✅ Confirmed (2024 study) | BrightLocal (Nov 2024): ChatGPT Search is "mostly powered by Bing's Index"; sources: business websites 58%, mentions 27%, directories 15%. Hence the importance of Bing Places |
| Self-ranking lists are useful | ❌ Disproved as a tactic | Lily Ray study 2026 (see Risks): citation without recommendation in 69% of cases, domain-level visibility drops |
| Agency B's growth numbers | ❓ Not verifiable | Declared by Agency B on its own site; no independent source |

Note for markets outside the US: the studies above are on US searches, where Yelp weighs heavily. Elsewhere the equivalent role is played by GBP, Bing Places and the sector directories actually used in the local market. The principle holds, not the list.

## GEO KPIs for a local business

Not only "position #1":

- **Branded search** (full name, name + city, name + vertical).
- **Non-branded impressions per cluster** in Search Console, with regex filters per service (`licens|licensee|licensor`, `brand|branding|identity`, `adv|advertising|media`…) and per place (the city name in each language the site uses, plus the suburb, e.g. `cityname|cityname-en|suburb`). Traffic from AI Overviews/AI Mode falls under the Web-type Search Console reports.
- **Number of authoritative domains that mention the entity** (mentions, even without a link).
- **Entity consistency**: identical name, address and description on the main sources.
- **AI citation testing**: a fixed set of "service + city" and "best agencies for X" prompts repeated periodically on ChatGPT, Gemini, Perplexity and Google AI Overviews/AI Mode (see the tools in [chapter 4](ch04-tooling-and-measurement.md)).

## Procedure: gap analysis against the competitor the AI recommends

1. List the "service + city" and "best X in city" queries the business wants to appear for.
2. For each one, ask 2–3 AI engines and note who is recommended and which URLs are cited.
3. For the most recurrent competitor: which page dominates the query, with which H1/section, FAQ, footer, schema.
4. For the business's own site: the equivalent page, what is missing (definition sentence, city section, FAQ, linked cases, schema, author), new content to create.
5. Assign priorities: 🔴 entity/schema/profiles/external corroboration, 🟠 landing pages and case studies, 🟢 the vertical where the competitor is weak and the business is strong. That is where it pays to beat the competitor instead of chasing it everywhere.

Useful format:

| Query | Competitor page | Own page | Gap | Priority |
|---|---|---|---|---|
| graphic design [city] | long landing + "Graphic Design Studio [city]" section + FAQ | service page | missing city section, comparison FAQs, textual cases | 🔴 |
| licensing [city] | weak | service page + 20+ licensing projects | opportunity: pillar + articles + English version | 🟢 |

## Action list for the excluded agency, in order

1. Disambiguate the entity: full name everywhere, a definition sentence under the homepage H1, the same NAP and description on every profile and directory.
2. Add third-party corroboration: directory profiles, authentic reviews, credits on client and partner sites.
3. Add schema with a shared `@id` (`LocalBusiness` subtype or `Organization`, `Service` per page, `BreadcrumbList`).
4. Rework the service pages: one strong page per "service + city", textual case studies linked both ways, author pages, informational content behind each money page.
5. Lead with the vertical niche where the credentials are real (licensing in the case).
6. Avoid doorway pages and self-ranking listicles.

## Key Takeaways
1. An LLM recommends whoever it can find and corroborate, not necessarily the best: a stronger portfolio does not make up for an entity that is ambiguous and rarely cited elsewhere.
2. Literal "service + city" coverage (headings, sections, titles) is why a competitor "always comes up", even when the city changes.
3. A definition sentence on the homepage, entity reinforcement in the footer and schema with a shared `@id` are the on-site interventions with the lowest cost and the highest impact.
4. Consistent third-party sources (directories, GBP with reviews, credits on client sites) are priority no. 1: the same description repeated by independent sources builds the entity.
5. A credible vertical niche is the most efficient lever for entering AI answers; doorway pages and self-ranking lists are shortcuts with low evidential value.

## Sources
- Analysis session with an AI assistant (October 2026) on the public websites of two agencies, anonymised.
- Google Search Central, "AI features and your website": https://developers.google.com/search/docs/appearance/ai-features
- Google Search Central, Organization structured data: https://developers.google.com/search/docs/appearance/structured-data/organization
- Google Search Central, documentation updates (FAQ rich result deprecation, 2026): https://developers.google.com/search/updates
- Google Search spam policies (doorway abuse): https://developers.google.com/search/docs/essentials/spam-policies
- Google Business Profile guidelines: https://support.google.com/business/answer/3038177
- BrightLocal, Local AI visibility study (Sep 2026): https://www.brightlocal.com/research/local-ai-visibility-study/
- BrightLocal, Uncovering ChatGPT Search sources (2024): https://www.brightlocal.com/research/uncovering-chatgpt-search-sources/
- Lily Ray's study on self-promotional listicles (summary by ALM Corp, 2026): https://almcorp.com/news/self-promotional-listicles-ai-overviews-help-competitors-lily-ray-study/
