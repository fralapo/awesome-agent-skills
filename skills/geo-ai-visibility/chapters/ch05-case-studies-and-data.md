# Chapter 5: Case Studies and Data

## Core Idea
Aggregate numbers on search behaviour (zero-click rates, the distribution of referral traffic, the concentration of citations on a small number of domains) show why GEO has become relevant: the click is becoming the exception rather than the rule, and AI citations concentrate heavily on a few domains that are already authoritative. There is still measurable room to grow for sites that structure their content well.

## Zero-click and volumes

- **Google zero-click rate**: up from **50% in 2019** to **64.82% in 2026**. On **mobile** the rate rises to **77%**.
- **Out of 1,000 Google searches in the US**: only **360 lead to a click on the open web**; **640 end without any click**.
- **When an AI Overview appears**: zero-click is **80-83%** (data for the first 4 months of 2026; the general average is ~68% when an AIO is present). With Google **AI Mode** the rate rises to **93%**, the highest of all measured surfaces.
- **Referral traffic from AI**: **AI Mode** generates a referral for only **1.6-2.5%** of queries, against a **17-19%** referral rate for traditional Google search, so volume is low. But **AI-referred visitors convert ~4.4×** better than traditional organic traffic: less volume, much higher value per visit.
- **Distribution of referral traffic across AI platforms**: **ChatGPT dominates**, with estimates between **~63% and ~92%** of trackable AI referral (the figure varies with the measurement methodology), followed by Gemini, Perplexity, Claude and Copilot.

## Citation concentration

- **Concentration of cited domains**: an aggregated study of **680M+ citations** (6 large studies, Aug 2024–Apr 2026) shows that the **top 1% of domains (~12 sites)** — Wikipedia, Reddit, Forbes, Healthline, Investopedia, NYT, large .gov/.edu domains — captures **47%** of all AI citations.
- **Overlap between engines**: very low. Only **11%** of domains are cited by both ChatGPT and Perplexity.
- **Citation patterns in Google AI Overviews**: **38%** of citations now come from pages in the **Google top 10**, sharply down from **76%** in mid-2025, an effect of query fan-out (see [chapter 2](ch02-how-generative-engines-work.md)). **55%** of citations come from the first **30%** of the source page's content. Pages of **more than 2,500 words** are cited **1.6×** more often than pages under 800 words. Pages with **schema markup** are cited **2.3×** more often, and pages with **at least one source cited in the body** are cited **2.1×** more often than pages with none.
- **Measured impact of content techniques** (Princeton paper, [arXiv:2311.09735](https://arxiv.org/abs/2311.09735); full detail in [chapter 1](ch01-definitions-and-history.md)): Quotation Addition +41% PAWC in the paper (the best single technique), +22% PAWC validated on real Perplexity; Statistics Addition +33% PAWC in the paper, +37% Subjective Impression on real Perplexity; Keyword Stuffing -8% PAWC in the paper, -10% on real Perplexity (counterproductive on a real engine too, not only in the lab). The redistributive effect holds: **+115%** lift for sources in position 5 (low ranking) against **-30%** for sources already in position 1, with the "Cite Sources" technique.

## Named cases

The material behind this chapter does not contain "before/after" case studies of single companies with a detailed method and result (those come from practitioner reports, see [chapter 7](ch07-cross-source-consensus.md), and from the local-agency case in [chapter 8](ch08-entity-geo-for-local-service-businesses.md)). What is named here is market adoption and signals of the sector's economic maturity:

- **llms.txt adoption** (a proxy for the maturity of the GEO market): more than **844,000 sites** had implemented llms.txt by 2026, including well-known names such as **Stripe, Cloudflare, Vercel and Anthropic**. Google added an llms.txt check to **Chrome Lighthouse** (Apr 2026), a sign that the practice is becoming institutional. See [chapter 3](ch03-optimization-factors.md) for the convention itself.
- **Funding in the AI-visibility tool sector** (a proxy for economic maturity): **Profound** raised a **$96M Series C** at a **$1B** valuation (Feb 2026), for total funding of **$155M**. **Peec AI** raised an **€18M Series A** (Nov 2025) after reaching **€650K ARR within 4 months** of launch (mid-2025). See [chapter 4](ch04-tooling-and-measurement.md) for the tools.

## Caveat on source reliability

Most figures in this chapter come from blogs and reports published by commercial GEO agencies and tool vendors (2026). They are useful for sector patterns but are not peer reviewed. The Princeton paper (arXiv:2311.09735) is the only source here with a published experimental methodology and reproducible numbers. Treat everything else as sector-level evidence to verify and update over time, because the field changes quickly.

## Key Takeaways
1. Zero-click is now the norm, not the exception: 64.82% on Google overall, up to 93% with AI Mode. The click is no longer the default success metric.
2. AI traffic is low volume but high value: a 1.6-2.5% referral rate with AI Mode against conversions ~4.4× higher than traditional organic traffic.
3. AI citations are heavily concentrated: the top 1% of domains (~12 sites) captures 47% of all citations in a sample of 680M+.
4. The link between classic Google ranking and AI Overview citation is weakening: only 38% of citations now come from Google top-10 pages, against 76% in mid-2025.
5. The maturity signals of the GEO market are concrete and recent: more than 844,000 sites with llms.txt and nine-figure funding rounds for AI-visibility tools (Profound at a $1B valuation).

## Sources
- Aggarwal et al., "GEO: Generative Engine Optimization", arXiv:2311.09735 (KDD 2024): https://arxiv.org/abs/2311.09735
- Chrome for Developers, Lighthouse llms.txt audit: https://developer.chrome.com/docs/lighthouse/agentic-browsing/llms-txt
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
