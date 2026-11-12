# Chapter 3: Concrete Optimization Factors

## Core Idea
A small set of content techniques (statistics, expert quotes, authoritative sources, structured data) explains most of the visibility lift in generative engines, with measured impacts that repeat between the academic study (Princeton, see `ch01-definitions-and-history.md`) and an aggregated market study (digitalapplied.com). On top of this comes a new class of signals — unlinked brand mentions, cross-web consensus, and "agent-readable" conventions such as llms.txt — that have no direct equivalent in classic SEO.

## Citable content techniques

The ranking of factors below comes from the digitalapplied.com study, a synthesis of 54 experiments, patents, papers and case studies on ChatGPT, Gemini and Perplexity that scores 23 factors. Treat it as a more solid reference than individual blog posts.

- **Statistics/numerical data**: the highest-impact factor in that aggregated study of 54 experiments/papers/case studies on 23 factors (ChatGPT, Gemini, Perplexity) — up to **+40% visibility** as a theoretical ceiling, with a realistic estimated impact of **+20-30%** (not a measured average).
- **Citing authoritative sources in the body**: an impact of the same order of magnitude as statistics addition; pages with at least one citation of a named source in the body are cited **2.1×** more often than pages without one.
- **Expert quotes with attribution**: **+28%** measured impact in the aggregated study.
- **Q&A / answer-first format**: answer blocks of **40-60 words** near the start of each page/section, under a heading phrased as a question; every section must be self-contained (understandable in isolation), consistent with the fact that LLMs retrieve at chunk level and not at whole-page level (see `ch02-how-generative-engines-work.md`). Use explicit named entities (product/category name) instead of pronouns, to keep referential clarity when the chunk is read in isolation.
- **Entity-based content**: chunks must clearly identify and explain the key entities (people, places, concepts, products) relevant to the sector, with consistent naming of the brand/entity across the whole site and on external profiles (social, directories, Wikipedia/Wikidata where applicable) — inconsistent naming risks the AI treating the brand as a generic phrase instead of a distinct entity.
- **Semantic chunking**: each section must cover a single concept. The six areas to work on systematically are content structure, answer formatting, citation quality, schema markup, entity recognition, and topical authority. Avoid client-side rendering for important content, because AI crawlers often do not execute JS reliably.
- **Content length**: pages over 2,500 words are cited **1.6×** more often than pages under 800 words.
- **Position of the fact in the page**: 55% of AI Overview citations come from the first 30% of the page content (see `ch02-how-generative-engines-work.md`) — put the key answers and facts near the top.
- **Freshness / dateModified**: pages with a recent update timestamp get priority on time-sensitive queries.
- **Anti-factor — keyword stuffing**: confirmed as counterproductive both in the Princeton paper (-8% PAWC, -10% on real Perplexity, see `ch01-definitions-and-history.md`) and in practice — classic SEO techniques based on keyword density do not transfer to generative engines.

## Authority and brand mentions

- **E-E-A-T** (Experience, Expertise, Authoritativeness, Trustworthiness): the Google framework, now extended to GEO as well — it is not a direct factor but a guiding principle that correlates with the authority the model perceives.
- **Cross-web consensus**: LLMs learn a brand's authority through cross-web consensus — if independent third-party sources do not mention the brand, the model cannot "verify" its existence or credibility and does not recommend it, even when the brand's own content is excellent. Digital PR and mentions on authoritative third-party sites therefore become a crucial GEO lever, not just on-site content.
- **Co-occurrence signal**: the brand name together with category keywords in the same paragraph on authoritative external sites is a strong signal to the model that the brand belongs to that category.
- **Brand mentions without a link**: unlinked mentions should be treated as a citation signal in their own right — they contribute to visibility even without a clickable backlink. A common mistake is to optimize only for linked/trackable citations and ignore pure text mentions.
- **Robots.txt and AI crawlers**: many sites unintentionally block AI crawlers (GPTBot, PerplexityBot, ClaudeBot, Google-Extended, etc.) through robots.txt — this is the first technical check to run in a GEO audit.

## Structured data / schema.org

- **Measured impact**: pages with correct structured data (JSON-LD/schema.org) are cited **2.3×** more often; combining correct schema with a clear factual answer in the first 200 words gives a quick measurable lift — **+28-34% coverage in 14-21 days**.
- **Preferred format**: JSON-LD is preferred over microdata because it is easier to parse reliably.
- **Recommended schema types**: `FAQPage` and `Article` are among the most recommended for GEO. Also include `Organization`, `Person` (author), `HowTo`, `Article`/`BlogPosting`, and `Product`/`Review` where relevant.

## llms.txt and emerging standards

- **What it is**: a plain markdown file placed at the root of the domain (`https://example.com/llms.txt`) that provides a structured, machine-readable summary of the site — who you are, what you do, which sources of truth are definitive — sparing the AI agent from navigating and processing every single page. It is an emerging convention, not an official W3C standard: originally proposed by Jeremy Howard/Answer.AI and adopted "bottom-up" by community consensus.
- **Adoption (2026 data)**: more than **844,000 sites** have implemented llms.txt, including **Stripe, Cloudflare, Vercel, Anthropic** and hundreds of mid-market companies. The adoption advantages cited are zero hosting cost, deployment in a few minutes, and immediate value for any AI system that encounters it.
- **Chrome Lighthouse**: in April 2026 Google added an llms.txt check directly to Chrome Lighthouse — the same framework that normalized HTTPS, mobile-first and Core Web Vitals — a signal that the standard is becoming mainstream and auditable.
- **Typical structure**: an H1 with the site/company name, a short blockquote description, and sections with Markdown links to the most important pages/resources (docs, pricing, API reference, blog). It has to be kept in sync with the real content, not left as a forgotten static artifact. It complements — and does not replace — sitemap.xml, robots.txt and schema.org markup: these are different layers of the same goal, making the site readable to a non-human consumer.
- **Real limits — it is a convention, not a citation guarantee**: llms.txt is a static summary that is read passively. It only enables **reading** (the agent reads the site); it does not enable **action** (checking inventory in real time, placing an order) — that requires complementary standards such as the **Model Context Protocol (MCP)**, which is indicated as the direction for letting AI agents "act", not just read. In the wider 2026 landscape of "agent-readable web" standards, a comparison published by Platinum.ai sets llms.txt against **WebMCP** (exposing the site's functionality as MCP-style tools, for active interaction by the agent) and **SDF** and **CAP** (more recent/niche standards for structured discovery and capability advertisement, with less established names that are still evolving — verify the current details before relying on them). A broader framework called **ARO (Agent-Readable Optimization)**, described in a paper published on Zenodo, combines llms.txt, "companion files" and credential verification to build a web that agents can read reliably.

## Key Takeaways
1. The four highest-impact factors according to an aggregated study of 54 experiments/papers/case studies (23 factors in total) are statistics/numerical data (up to +40% ceiling, realistic +20-30%), citing authoritative sources (same order of magnitude), attributed expert quotes (+28%), and correct structured data (cited 2.3× more often).
2. Pages over 2,500 words are cited 1.6× more often than those under 800 words, and pages with at least one citation of a named source in the body are cited 2.1× more often than pages without one.
3. Keyword stuffing remains as counterproductive in GEO as in the Princeton paper covered in `ch01-definitions-and-history.md` (-8% PAWC, -10% on real Perplexity) — classic keyword-density SEO techniques do not transfer.
4. The authority the model perceives depends on cross-web consensus: without mentions on independent third-party sources, even a brand with excellent content of its own is neither "verified" nor recommended — unlinked mentions count as a citation signal in their own right.
5. llms.txt has passed 844,000 adopting sites (including Stripe, Cloudflare, Vercel, Anthropic) and was added to Chrome Lighthouse in April 2026, but it remains a read-only convention — it does not guarantee citation and does not enable actions, which require complementary standards such as MCP.

## Sources
- https://www.digitalapplied.com/blog/ai-search-citation-ranking-factors-2026-data-study
- https://www.omnibound.ai/blog/generative-engine-optimization-statistics
- https://www.rankio.studio/learn/llm-ranking-factors
- https://thedigitalbloom.com/learn/llm-ranking-factors-2026/
- https://blog.hubspot.com/marketing/generative-engine-optimization-best-practices
- https://directiveconsulting.com/blog/a-guide-to-generative-engine-optimization-geo-best-practices/
- https://www.lumar.io/blog/best-practice/content-chunking-ai-extractability-geo-aeo-explainer/
- https://searchengineland.com/guide/content-chunking-seo
- https://www.frase.io/blog/what-is-answer-engine-optimization-the-complete-guide-to-getting-cited-by-ai
- https://www.cnabke.com/en/blogs/geo-mentions-linkless-ai-visibility.html
- https://www.yotpo.com/blog/what-is-llms-txt/
- https://developer.chrome.com/docs/lighthouse/agentic-browsing/llms-txt
- https://www.platinum.ai/what-is-llms-txt
- https://www.platinum.ai/ai-agent-web-standards
- https://promptowl.ai/resources/how-ai-agents-should-read-your-site-llms-txt/
- https://zenodo.org/records/18817486
