# Chapter 7: Cross-Source Consensus

## Core Idea
A survey of nine practitioner sources (SEO agencies, tool vendors and one first-person case study) shows broad consensus on what matters for GEO: SEO as the foundation, external mentions as the strongest lever, answer-first structure, and YouTube as a high-impact channel. There are also some real differences of emphasis and terminology, and one important caveat: many of the numbers that practitioners repeat as "confirmed by several sources" come from a single piece of primary research (Ahrefs) that is quoted and re-quoted across the sector, not from multiple independent studies.

## Cross-source consensus

- **Traditional SEO remains the foundation; it is not replaced.** The idea recurs in almost identical form in seven of the nine sources. The single most repeated figure is **"76% of AI Overview citations come from pages already in the Google top 10"**. This is an Ahrefs figure that other practitioners repeat word for word: **these are not independent confirmations, it is the same research circulating in the sector**. (The share has since fallen to 38%, see [chapter 5](ch05-case-studies-and-data.md).)
- **The goal shifts from "click/ranking" to "being mentioned or cited in the answer"**, even without a click and sometimes without a visible link. All nine sources say this in different words: visibility is the metric; influence matters more than authorship; traffic becomes exposure-driven; SEO gets a site found, GEO gets it recommended.
- **Off-site mentions (not the brand's own site) are the single most decisive factor for AI visibility.** Ahrefs quantifies it: in a study of **75,000 brands**, branded web mentions show the strongest correlation with visibility in AI Overviews, stronger than backlinks, Domain Rating or referring domains. An independent practitioner-reported figure points the same way: **82% of what AI cites is "earned media"** (third-party articles, listicles, Reddit threads), not self-published content. Practitioners also describe this as "consensus": a claim present only on the brand's own site is weak; the same claim repeated on the site, on third parties, in reviews and on comparison pages becomes reliable for the AI. In one panel of five SEO practitioners, three named external mentions as the priority lever. The convergence here is more solid than elsewhere because it combines an Ahrefs figure with an independent one.
- **"Answer-first" content structure** (BLUF, capsule content, a direct answer straight after the heading): explicit in five of the nine sources. It is the most repeated tactical pattern.
- **YouTube as a high-impact channel specifically for AI visibility**, not only a generic marketing channel: present in five of the nine sources (in one of them indirectly, through the same logic applied to text versions of podcast episodes). The strong quantitative figure, a **0.737 correlation between YouTube mentions and visibility on ChatGPT**, the strongest correlation measured in that study, is an Ahrefs figure. Other practitioners repeat the same point only qualitatively ("YouTube mentions are the factor most strongly correlated with AI visibility") without the 0.737 figure: **same primary source and same claim, but the exact number appears in one place only.** The recurring rationale has two parts: GPT-4 was trained on more than 1 million hours of transcribed YouTube audio, and YouTube is the most cited domain in Google's AI Overviews.
- **Structured data is still relevant but is not "the secret key".** It enables; it is not sufficient on its own. Google's own position, which practitioners quote, is that there is no secret AI tag, only the same standard schema used for Rich Results. Practitioners agree that schema (including a per-page service schema and a Wikidata entry) plays a supporting role, not a decisive one.
- **Measurement needs a different approach from classic SEO.** There is no clean CTR or position. The agency and tool-vendor sources propose variants of the same scheme: manual multi-platform audit + a dedicated tracking tool + self-reported attribution.
- **Fresh, updated content weighs more than in classic SEO.** The quantitative figure (content cited by AI is **25.7%** fresher, or **26%** fresher in a second study, the same order of magnitude) comes from **two distinct Ahrefs studies by the same research team**, so both trace to the same research area rather than to fully independent sources. Other practitioners confirm it qualitatively (without numbers of their own) and treat content updates as a practical priority.

**Caveat on "consensus" numbers:** many of the quantitative figures that appear to be confirmed by several practitioner sources derive from the same primary Ahrefs research (76% top-10, 0.737 YouTube correlation, 25.7%/26% freshness, data on 75,000 brands, 174,000 pages, 17 million citations analysed), quoted and re-quoted by different practitioners. Attribute them as "Ahrefs data"; do not present them as the independent consensus of several studies.

## Disagreements

- **"GEO is just good SEO" vs "GEO requires new, distinct tactics".** Some practitioners play down the novelty: it all comes down to doing good SEO, and most skills transfer directly. Others stress clear paradigm changes (explaining RAG, fixing identity on Wikidata, a full site rewrite) as interventions distinct from classic SEO. A middle position gives an explicit estimate: **~70% classic SEO, ~30% GEO-specific tactics**. The balanced reading: SEO is a necessary but not sufficient prerequisite, and the GEO-specific tactics (consensus, entity schema, atomic content, identity fixing) are an additional layer with its own return.
- **GEO/AEO/LLMO terminology is not standardised.** A minority view (one source in nine) separates AEO (featured snippets and People Also Ask, an older, pre-LLM concept) sharply from GEO (optimisation for generative chatbots). Most practitioners use AEO and GEO as interchangeable synonyms, and treat "GEO, AEO or LLMO" as variants of the same concept.
- **Weight of content length.** An Ahrefs analysis of **174,000 pages cited in AI Overviews** reports a clear result: the word count↔citation correlation is **≈ zero**, and more than half of the cited pages have fewer than 1,000 words. No source contradicts this explicitly, but several still insist on "comprehensive topical coverage". This is not a real contradiction: the distinction is between **per-page depth** (short and atomic is fine) and **per-topic/site breadth** (wide, spread over several pages, recommended by everyone).
- **Role of the blog and classic content marketing.** One source addresses the objection "blogs are useless now" directly and rejects it, redefining the blog's purpose from traffic driver to topical-authority builder. No source openly denies the value of the blog, but some put more emphasis on PR and earned media than on managing owned content. It is a difference of emphasis between a "content-first" approach and a "PR/earned-media-first" approach.
- **Descriptive models of how AI generates answers.** No two sources use the same scheme, but the schemes are compatible: three mechanisms (live web search under the hood / dedicated AI Overview optimisation / pre-trained knowledge with no search); a 4-step pipeline (intent decomposition → retrieval → rank/filter → compose, with optional citation); a 2-layer model (training knowledge + retrieval/RAG); and query fan-out (one prompt split into dozens of parallel sub-queries). These are complementary descriptions at different levels of detail, not in conflict. They combine into one multi-level technical model: training time vs inference time, with query fan-out as a detail of the retrieval step (see [chapter 2](ch02-how-generative-engines-work.md)).

## Techniques practitioners repeat

### Content structure
- **BLUF (Bottom Line Up Front)**: start every section with the answer, not the backstory. Both humans and AI weigh the beginning and end of a passage more heavily than the middle.
- **Atomic content**: every section of a page should be able to stand on its own. AI splits content into chunks when it processes it, and the author cannot control where the chunk boundaries fall.
- **Answer-first rewrite**: if a page answers "What is GEO?", the first sentence should define GEO clearly, not open with five lines of context.
- **Capsule Content Technique**: an H2 phrased as a direct question, with the answer immediately below and no preamble. A weak opening talks about "today's digital landscape"; a good one reads like "Technical SEO is the process of optimising a website's infrastructure so that search engines can crawl, index and rank its pages effectively."
- **Entity-rich writing**: replace "This tool helps with SEO" with a sentence that names the product and what it does (e.g. "Ahrefs Keywords Explorer helps you find keywords with low difficulty and high traffic potential").
- **Simple and declarative**: one idea per sentence, in a clear subject-verb-object structure. If a sentence takes two reads to understand, it is too complex.
- A recurring writing checklist: clear Q&A form; every paragraph standalone and complete; specific examples and data; authoritative but accessible language; context that is easy to extract.

### Technical and crawling
- Check `domain.com/robots.txt` for **GPTBot** (OpenAI), **OAI-SearchBot**, **ClaudeBot**, **Google-Extended** and **Bingbot**: no accidental disallow.
- **Watch Cloudflare**: the "Block AI Bots via robots.txt" feature is on **by default** on many plans and blocks AI crawlers unintentionally.
- Key content must be in **plain HTML / pre-rendered static text**, not behind a JavaScript interaction. AI systems mainly read raw HTML; information that appears only after a JavaScript interaction may be missed entirely.
- **ChatGPT Search uses Bing's index**, so the sitemap has to be submitted in Bing Webmaster Tools, not only in Google Search Console.
- Descriptive alt text for images; full text versions of video and podcast content.

### Schema and structured data
- **Organization schema**: name, logo, social profiles. It helps entity resolution in the knowledge graph.
- **Article schema**: publication date, author, headline. These are relevance and credibility signals.
- **A specific Service schema per page** for multi-service local businesses, different on each page.
- **Wikidata presence** even without a full Wikipedia page. The "instance of" field must describe correctly what the entity is: in one reported case, replacing an outdated occupation with the current ones unlocked correct citations in Gemini.
- **Cross-platform consistency of descriptions**: NAP (Name/Address/Phone) and descriptions **identical word for word** on every platform (podcast directories, Wikidata, local directories, etc.). When the sources disagree, the models play safe and name someone else; when they all carry the same sentence, the model repeats that sentence back.

### Authority and off-site
- **Consensus / distributed authority**: a claim only on the brand's own site is weak; the same claim on the site, third parties, reviews and comparison pages becomes reliable. Authority has to be distributed, not sit only on the brand's own domain.
- **Three tiers of external mentions**: Tier 1, third-party editorial (review sites, listicles on authoritative blogs; the hardest and most valuable); Tier 2, user-generated content (Reddit, one of the sources ChatGPT cites most often, plus Quora and niche forums); Tier 3, owned properties (YouTube, podcast, LinkedIn).
- **YouTube as a priority lever**: the most cited domain in Google's AI Overviews, with a 0.737 correlation with ChatGPT visibility (Ahrefs). The strategy is to create evergreen "search hits" rather than viral hits: keyword in the title, in the first lines of the description, in the chapters, and spoken aloud in the video itself.
- **"Identity-based" comparison pages**: not only a generic "A vs B" but a page targeted at a persona (e.g. "QuickBooks alternative for graphic designers"). This uses the fact that models often know who the user is within the session.
- For new players without budget: a three-way listicle (piggybacking on the comparison between two large competitors), or buying/sponsoring the same links competitors sponsor (found with the "sponsored link" filter in backlink tools). See the risks of self-ranking listicles in [chapter 8](ch08-entity-geo-for-local-service-businesses.md).
- A source of non-obvious insight: upload **records of real sales calls and customer conversations** to an LLM and ask for a market-research style analysis (fears, objections, what matters to the customer). This complements classic keyword research, because prompts are about 5× longer than keywords and carry more real context.

### Audit and measurement
- **Quick AI-visibility diagnosis**: paste the site URL into a chatbot and ask how visible the site is in AI search and what is stopping it from showing up (in practice, a readability audit by the model).
- **20-Minute GEO Audit**: open ChatGPT, Claude, Perplexity and Google AI Overview → run the top 5 informational/category queries (never queries containing the brand name) → check whether the brand appears, how it is described and which competitors are cited in its place, then compare with the classic SEO ranking to see whether the problem is coverage or structure/authority.
- **AI filter for keyword research**: for each keyword ask "can an AI Overview fully satisfy this query on its own?" If yes, change the goal from "click" to "mention inside the answer".
- **Three metrics to track in the absence of Search Console-level data**: AI referral traffic (underestimated, since not every platform passes a clean referrer); AI bot activity on the site (citation bots re-reading specific pages suggest those pages are being used as sources); self-reported attribution ("how did you find us?" at sign-up or checkout).
- Tools practitioners name: **Surfer AI Tracker**, **Ahrefs Brand Radar**, **Ahrefs Web Analytics** (with a Cloudflare integration for bot tracking), **Peec AI** (multi-engine: Google, AI Overview, ChatGPT, Perplexity; it shows the internal queries the model searched). See [chapter 4](ch04-tooling-and-measurement.md).

## Frequently repeated figures and their origin

| Figure | Value | Origin |
|---|---|---|
| AI Overview citations from pages already in the Google top 10 | 76% | Ahrefs (repeated by other practitioners) |
| Position-1 CTR reduction caused by AI Overviews | -58% | Ahrefs (study of 300k keywords) |
| Queries that trigger an AI Overview | ~21% of all queries, ~58% of questions | Ahrefs |
| Share of AI Overview-triggering keywords with informational intent | 99.9% | Ahrefs |
| Freshness of cited content vs classic SERP | +25.7% / +26% (two different Ahrefs studies, same order of magnitude; the second analysed 17 million AI citations) | Ahrefs |
| Cited pages under 1,000 words | more than 50% (of 174k pages analysed) | Ahrefs |
| ChatGPT top cited pages updated in 2025 / in the last 30 days | 89.7% / 76% | Ahrefs |
| Pages cited by ChatGPT that are in list format | 43.8% | Ahrefs |
| Correlation of branded web mentions with AI Overview visibility | stronger than backlinks/DR/referring domains (study of 75k brands) | Ahrefs |
| Correlation of YouTube mentions with ChatGPT visibility | 0.737 (strongest measured) | Ahrefs |
| Sites unintentionally blocking GPTBot | 5.9% of 140M sites | Ahrefs |
| Improvement in AI-answer inclusion with structured E-E-A-T content | +37% (Perplexity, an otherwise unspecified 2024 study) | Tool-vendor source |
| Average sources cited per AI Overview query | ~5 | Tool-vendor source |
| Queries with 8 or fewer cited sources | 90% | Tool-vendor source |
| Google zero-click search rate | 60% (older figure) / >80% (more recent 2026 figure) / ~93% with AI Mode | Practitioner sources |
| Marketers who want to optimise for AI search vs those who do | 92% vs 40% | Practitioner source |
| Conversion rate of ChatGPT traffic vs Google organic | 15.9% vs 1.76% | One practitioner's own newsletter data (self-reported) |
| Share of what AI cites that is earned media | 82% | Practitioner source |
| AI search traffic vs share of sign-ups generated (Ahrefs internal case) | 0.5% of traffic → 12.1% of sign-ups (23× conversion) | Ahrefs |
| Growth of AI traffic in one year | 9.7× | Ahrefs |

Many of these figures derive from the same primary source (Ahrefs research). They are not multiple independent confirmations.

## Key Takeaways
1. The most widely shared pattern across the nine sources is the shift of the goal from "click/ranking" to "being mentioned in the answer", stated in different words in every source analysed.
2. Many numbers that look "confirmed by several sources" (76% of citations from the Google top 10, 0.737 YouTube-ChatGPT correlation, 25.7%/26% freshness) trace to the same primary Ahrefs research. Attribute them as Ahrefs data, not as independent consensus.
3. The most solid convergence, because it combines Ahrefs research (75,000 brands) with an independent practitioner figure (82% earned media), is that off-site brand mentions count for more than any traditional SEO signal measured.
4. GEO/AEO/LLMO terminology is not standardised: most practitioners treat the terms as synonyms, but at least one source separates them sharply.
5. The most actionable and most repeated tactics are answer-first structure (BLUF/capsule content) and word-for-word consistency of brand descriptions across all external platforms.

## Sources
- Ahrefs, AI Overview citations and the Google top 10: https://ahrefs.com/blog/ai-overview-citations-top-10/
- Ahrefs, search rankings and AI citations: https://ahrefs.com/blog/search-rankings-ai-citations/
- The remaining points summarise practitioner observation across nine industry sources (agencies, tool vendors, one first-person case). Figures marked "practitioner source" come without a cited methodology in the material surveyed and should be treated as indicative.
