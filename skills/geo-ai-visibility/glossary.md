# Glossary — GEO / AI Visibility

**AEO (Answer Engine Optimization)** — term used interchangeably with GEO by most sources in this material to describe optimizing content for AI-generated answers; one source (Niko) distinguishes it as the older, pre-LLM discipline of optimizing for featured snippets/People Also Ask (Ch1, Ch7).

**AI Overview / AI Mode** — Google's generative-answer surfaces layered on top of classic search; AI Mode has the highest measured zero-click rate (93%) and the lowest referral rate (1.6-2.5%) of all surfaces analyzed (Ch2, Ch5).

**Answer Engine** — a generative platform (ChatGPT, Perplexity, Google AI Overviews/AI Mode, Copilot, Gemini, Claude) that returns a single synthesized answer instead of a ranked list of links (Ch1).

**ARO (Agent-Readable Optimization)** — an emerging umbrella framework combining llms.txt, "companion files," and credential verification to make a site reliably readable by AI agents (Ch3).

**Atomic content** — writing every page section so it can stand alone and be understood without the rest of the page, since LLMs chunk content and the content owner cannot control where chunk boundaries fall (Ch7).

**BLUF (Bottom Line Up Front)** — starting every section with the direct answer before any backstory, because both humans and AI models weigh the beginning of a passage more heavily than the middle (Ch7).

**Capsule Content Technique** — formatting a section as a question-form H2 heading followed immediately by a direct, self-contained answer with no preamble (Ch7).

**Chunk / Chunking** — the unit generative engines actually retrieve and cite: a semantic segment of a page (not the whole page) converted into a vector embedding and stored for retrieval; content should be structured so each chunk is self-contained and citable on its own (Ch2, Ch3).

**Co-occurrence (signal)** — a brand name appearing in the same paragraph/context as category keywords on third-party authoritative sites, which signals to the model that the brand belongs to that category (Ch1, Ch3, Ch6).

**Cross-web consensus** — the pattern by which LLMs infer a brand's authority from independent third-party sources repeating the same claim; without such consensus, the model cannot "verify" a brand and won't recommend it, regardless of on-site content quality (Ch3, Ch6, Ch7).

**E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness)** — Google's classic SEO authority framework, now also treated as a guiding principle for GEO even though it is not a directly measurable ranking factor (Ch3).

**Entity-based content** — structuring content so it clearly identifies and explains the key entities (people, places, concepts, products) relevant to a topic, with consistent naming of the brand/entity across the site and external profiles (Ch3).

**GEO (Generative Engine Optimization)** — the practice of optimizing content and sites to increase the likelihood of being cited, mentioned, or summarized in the answers produced by generative engines, as opposed to ranking in a list of clickable links (Ch1).

**GEO-BENCH** — the 10,000-query benchmark (aggregated from 9 source datasets across 25 domains) built by the founding GEO paper (Princeton et al., arXiv:2311.09735) to test content-optimization techniques against a prototype generative search engine (Ch1).

**JSON-LD** — the structured-data markup format preferred over microdata for GEO because it is easier for crawlers to parse reliably (Ch3, Ch6).

**llms.txt** — a plain-markdown file placed at a site's root that provides a machine-readable summary of the site for AI agents, sparing them from crawling every page; an emerging bottom-up convention (not a W3C standard), adopted by 844,000+ sites as of 2026 (Ch3).

**LLMO (LLM Optimization)** — one of the terms used interchangeably with GEO/AEO in industry material to describe optimizing content for large language model outputs (Ch1, Ch7).

**Model Context Protocol (MCP)** — a complementary standard to llms.txt that lets AI agents take action on a site (e.g., check real-time inventory, place an order) rather than only read it (Ch3).

**PAWC (Position-Adjusted Word Count)** — one of the two metrics proposed in the founding GEO paper: a word count of cited content weighted with exponential decay by citation position within the answer, so citations near the top of the answer count more (Ch1).

**Query fan-out** — the mechanism by which a generative engine (notably Google AI Overviews/AI Mode) splits a single user query into multiple sub-queries and cites pages that recur across the sub-query results, which decouples AI citation from classic top-10 ranking (Ch1, Ch2).

**RAG (Retrieval-Augmented Generation)** — the shared architectural pattern behind all generative engines: query → retrieval → ranking/filtering of candidates → answer synthesis by the LLM → source citation (Ch2).

**Share of Voice** — a brand-visibility metric tracked by AI-visibility tools: how often a brand is cited/mentioned relative to competitors across a set of tracked prompts/topics (Ch4).

**Structured data / schema.org** — machine-readable markup (e.g., `FAQPage`, `Article`, `Organization`) added to a page; pages with correct structured data are cited 2.3x more often than those without (Ch3, Ch6).

**Subjective Impression (SI)** — the second metric proposed in the founding GEO paper: a composite 7-component score (relevance, citation influence, content uniqueness, positional prominence, perceived volume, click likelihood, source diversity) evaluated with GPT-3.5 (Ch1).

**Unlinked mention (brand mention)** — a mention of a brand by name in AI-generated or third-party content without an accompanying clickable link; treated as a citation signal in its own right and often more commercially important than linked citations (Ch1, Ch3, Ch6).

**WebMCP** — an emerging 2026 standard for exposing a site's functionality as MCP-style tools so AI agents can interact with it actively, part of the broader "agent-readable web" landscape alongside llms.txt (Ch3).

**Zero-click search** — a search result where the user gets their answer without clicking through to any website; the dominant outcome in 2026 (64.82% overall on Google, up to 93% with AI Mode), making citation/mention the new success metric instead of click-through (Ch2, Ch5).
