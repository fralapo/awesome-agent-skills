# Chapter 6: Checklist and Best Practices

## Core Idea
The GEO best practices that emerge from industry guides (HubSpot, Ahrefs, specialised agencies) fall into a few coherent categories: technical foundations, structured data, content structure, editorial quality, off-site authority, maintenance and measurement. Each one corrects a specific, recurring anti-pattern.

## Consolidated checklist

### Technical foundations
- **robots.txt must not block AI crawlers** (GPTBot, PerplexityBot, ClaudeBot, Google-Extended, etc.).
- **Critical content must not depend on client-side rendering.**
- **Solid load speed and crawlability.** This is a classic SEO prerequisite that still holds for GEO.
- **llms.txt present and in sync** with the site's real content (see [chapter 3](ch03-optimization-factors.md)).
- **Up-to-date sitemap.xml.**

### Structured data
- **FAQPage schema** on Q&A pages (Google retired FAQ rich results in May 2026; the value is now in the Q&A text, see [chapter 8](ch08-entity-geo-for-local-service-businesses.md)).
- **Article/BlogPosting schema** with an author (`Person`) and `dateModified`.
- **Consistent Organization schema** across the whole site.
- **JSON-LD** (not microdata) as the preferred format.

### Content structure
- **A direct-answer block (40-60 words)** near the start of every page or section.
- **Headings phrased as questions** for Q&A sections.
- **Every section self-contained**, understandable in isolation, like a chunk.
- **Explicit named entities** instead of pronouns in key passages.
- **Consistent brand/product naming** across the whole site.

### Content quality (levers with high measured impact)
- **Statistics and numerical data** added where relevant. This lever has a measured impact of up to +40% (ceiling).
- **Citations of authoritative sources** in the text.
- **Expert quotations with clear attribution.** Measured impact: +28%.
- **Technical industry terminology** where appropriate.
- **Fluent, readable prose.**
- **No keyword stuffing.**

### External / off-site authority
- **Digital PR and mentions on independent third-party sources** (Wikipedia/Wikidata where relevant, trade publications).
- **Co-occurrence of brand + category keyword** on authoritative external sites.
- **Coverage of the full topic cluster** (not only the main keyword), to benefit from Google's query fan-out.

### Maintenance / freshness
- **Quarterly freshness review** of content.
- **`dateModified` updated** whenever a piece of content is substantially revised.

### Measurement
- **An active AI-visibility tool** (at least one of Otterly, Peec, Profound, AthenaHQ; see [chapter 4](ch04-tooling-and-measurement.md)).
- **Separate monitoring per platform.** ChatGPT ≠ Perplexity ≠ Google AIO; the measured overlap is only 11%.
- **Sentiment tracking**, not only the presence or frequency of the mention.

## Anti-patterns

1. **Optimising only for linked citations and ignoring brand mentions.** In commercial contexts what moves the needle is often the mention of the brand by name, not the link. Focusing only on schema and page structure while ignoring the editorial and PR work that generates mentions is a common mistake.
2. **Treating unlinked mentions as irrelevant.** Every external mention of the brand should be treated as a citation signal, with or without a link.
3. **No third-party validation.** LLMs learn authority through cross-web consensus. Without independent mentions on third-party sources the model cannot "verify" the brand, so there is no citation, whatever the quality of the brand's own site.
4. **Inconsistent naming/entity.** If the brand name appears in different forms or spellings on the site and on external profiles, it risks being treated as a generic phrase rather than a distinct entity.
5. **Ignoring co-occurrence signals.** Brand name + category keyword in the same paragraph on authoritative third-party sites is an important signal that strategies often miss.
6. **Assuming Google ranking = AI visibility.** A common mistake is to think that traditional SEO positioning translates automatically into AI citations. The drop from 76% to 38% in overlap with the Google top 10 disproves it (see [chapter 5](ch05-case-studies-and-data.md)).
7. **Keyword stuffing**, a leftover from dated SEO practice. It is measurably counterproductive in generative engines.
8. **Unintentionally blocking AI crawlers through robots.txt.** A basic technical check that is often skipped.
9. **Client-side-only rendered content.** AI crawlers often do not execute JavaScript reliably, so the content becomes invisible.

## Key Takeaways
1. The GEO checklist groups into seven areas: technical foundations, structured data, content structure, editorial quality, off-site authority, maintenance/freshness, measurement.
2. The content levers with the highest measured impact remain statistics/data (+40% ceiling) and attributed expert quotations (+28%).
3. Nine anti-patterns recur in industry guides, including the mistaken assumption that traditional Google ranking automatically guarantees AI visibility.
4. Measurement has to be done per platform: the overlap between domains cited by ChatGPT and Perplexity is only 11%, so a single tool or a single channel is not enough.

## Sources
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
