# Chapter 2: How Generative Engines Work Technically (RAG)

## Core Idea
Every generative engine (ChatGPT, Perplexity, Google AI Overviews/AI Mode, Copilot, Gemini) follows the same basic architectural pattern — Retrieval-Augmented Generation (RAG): query → retrieval → ranking/filtering of candidates → synthesis of the answer by the LLM → citation of sources. Each platform, however, implements retrieval, ranking and citation selection differently enough that optimization strategies do not transfer 1:1 from one engine to another.

## The general RAG mechanism

- **Typical pipeline**: user query → retrieval (search over an index or the web) → ranking/filtering of candidates → answer synthesis by the LLM → source citation. RAG lets the model retrieve information from the web before generating the answer, so it can access fresh information and cite sources in real time instead of relying only on its training knowledge.
- **Generalized citation pipeline (e.g. Perplexity)**: (1) the user query triggers a retrieval of **5-10 candidate sources** through hybrid search (keyword + semantic/vector); (2) the candidates go through a multi-stage filtering pipeline (reported as **6 stages**) before surviving as final citations (**3-4 survivors**); (3) each source has to pass tests on relevance to the question, freshness, entity clarity, extractable evidence, source authority, and clean attribution. The gap between retrieval and citation is where most content strategies fail — being retrieved is not enough; the source has to survive the filter.
- **Retrieval at chunk level, not page level**: LLMs split content into semantic chunks, convert them into vector embeddings, store them in a vector database, and retrieve the most relevant chunks to answer. Each chunk should be self-sufficient (understandable and citable without reading the rest of the page). For the practical side of writing for chunks, see `ch03-optimization-factors.md`.

## Engine by engine

### ChatGPT (Search)
- **Favors consensus sources**: Wikipedia (~**7.8%** of citations), and it cites competitor sites more often than Google does (**+11.1 percentage points** compared with Google).
- **Hybrid retrieval**: it draws on both pre-trained knowledge and live retrieval via Bing/partnerships.

### Perplexity
- **Real-time retrieval on every query** — the most "search-native" approach among the platforms analyzed.
- **Strongly influenced by community discussion**: Reddit accounts for about **46.7%** of Perplexity's top citations.
- **Hybrid search** (keyword + vector) with the multi-stage filtering pipeline described above (6 stages, 5-10 candidates → 3-4 final citations).

### Google AI Overviews / AI Mode
- **Synthesizes mainly from pages already present in the classic Google index/ranking** — but in 2026 only **38%** of citations come from the top 10 (down from 76% in mid-2025) because of query fan-out.
- **Query fan-out**: the query is broken down into multiple sub-queries; pages that appear repeatedly in the sub-query results are more likely to be cited.
- **AI Mode has a 93% zero-click rate** — the highest among the platforms analyzed.

### Copilot (Microsoft)
- **Based on the Bing index + GPT**; there is less specific public data on its citation pipeline than for ChatGPT/Perplexity/Google.

### Claude / Gemini
- **Less granular public documentation** on their retrieval-for-citation than for ChatGPT/Perplexity/Google; they generally follow the same RAG pattern (retrieval + filtering + synthesis).

## Divergence between platforms

- **Overlap between platforms**: an analysis of **680 million citations** shows that only **11%** of domains are cited by both ChatGPT and Perplexity. Implication: GEO strategies do not transfer 1:1 between engines — testing and measurement have to be done per platform, which is where multi-platform AI-visibility tools get their value (see `ch04-tooling-and-measurement.md`). No single-channel optimization is sufficient.
- **Citation concentration**: an aggregated study (6 of the largest citation-tracking studies, Aug 2024–Apr 2026, 680M+ citations) shows that the **top 1% of cited domains (~12 sites)** — Wikipedia, Reddit, Forbes, Healthline, Investopedia, NYT, large .gov/.edu domains — captures **47%** of all citations.
- **The position of the content in the source page matters**: **55%** of AI Overview citations come from the top 30% of the page content, **24%** from the middle section (30-60%), and only **21%** from the bottom of the page — put the key answers and facts near the top.

## Key Takeaways
1. All generative engines share the same RAG skeleton (retrieval → filtering/ranking → synthesis → citation), but out of 5-10 candidate sources retrieved only 3-4 final citations survive the multi-stage filter.
2. The unit that is retrieved and cited is the self-sufficient semantic chunk, not the whole page — consistent with the structural GEO vs SEO difference covered in `ch01-definitions-and-history.md`.
3. Each platform weights different sources: ChatGPT favors consensus sources (Wikipedia ~7.8%) and competitors (+11.1pp vs Google); Perplexity is strongly Reddit-influenced (~46.7%); Google AI Overviews depends less and less on the classic top 10 (38% in 2026, down from 76%) because of query fan-out; AI Mode has the highest zero-click rate (93%).
4. Only 11% of domains are cited by both ChatGPT and Perplexity across 680M+ citations analyzed: no single-platform strategy is sufficient; each engine has to be measured and optimized for.
5. Citation power stays concentrated: the top 1% of domains (~12 sites) captures 47% of all citations, and inside the source page 55% of citations come from the first 30% of the content.

## Sources
- https://discoveredlabs.com/blog/ai-citation-patterns-how-chatgpt-claude-and-perplexity-choose-sources
- https://discoveredlabs.com/blog/chatgpt-claude-perplexity-and-google-ai-overviews-how-each-platform-cites-sources-differently
- https://authoritytech.io/blog/how-perplexity-selects-sources-algorithm-2026
- https://www.usegrowthos.com/blog/google-ai-overviews-vs-chatgpt-vs-perplexity
- https://ahrefs.com/blog/ai-overview-citations-top-10/
- https://ahrefs.com/blog/search-rankings-ai-citations/
- https://www.deltavdigital.com/resources/reports/ai-citation-study/
- https://everything-pr.com/ai-platform-citation-source-index-2026
- https://www.lumar.io/blog/best-practice/content-chunking-ai-extractability-geo-aeo-explainer/
