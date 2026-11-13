# Chapter 10: LLM Systems and Retrieval-Augmented Generation

## Core Idea
A language model is a probabilistic component whose context you control. In this model retrieval-augmented generation (RAG) is **ordinary data engineering around that component**: parse, chunk, embed, store, retrieve, optionally re-rank or rewrite, and generate - improved only when real traces show where it fails. Treat model output as unverified until grounded and evaluated.

## 10.1 What the model is, in system terms
- **Thesis**: a language model is a neural network trained to predict the next token of an input sequence; everything else is engineering around it.
- **Mechanism**: text is split into tokens (pieces that carry a concept, such as stems and suffixes), each token becomes a vector in a high-dimensional space where related meanings sit close together, and relations (capital-of) appear as consistent directions. The model is stateless between calls and tends to be helpful: with no relevant context it either guesses or gives a useless answer. This is background knowledge, not something application engineers must implement.
- **Trade-off**: probabilistic output, so hallucination is part of the architecture; you reduce its rate, you do not remove it.
- **Does not hold when**: the task is deterministic (use code).

## 10.2 RAG definition and purpose
- **Thesis**: when the answer depends on private or fresh data the model never saw, retrieve the relevant data and add it to the prompt.
- **Mechanism**: retrieve context for the query from your own store, **augment** the query with it, **generate**. Example: "where is order 123?" -> fetch the order record -> the model turns the record into a readable answer.
- **Trade-off**: extra latency and tokens for every call.
- **Does not hold when**: the question is answerable from general knowledge, or the real need is to **act** (that is a tool call, ch11).

## 10.3 Vector search in one paragraph
- **Thesis**: store each chunk as a vector so "similar meaning" becomes "close in space".
- **Mechanism**: embed the query into a query vector; the vector database returns the nearest chunks by cosine similarity. To be fast it clusters or builds graph structures (hierarchical navigable small world graphs; inverted-file indexes; other libraries exist), searching only the closest clusters, so results are approximate: a nearby relevant chunk can be missed. Any database can store documents; the vector kind adds nearest-neighbour search.
- **Trade-off**: approximate recall for speed; embeddings smooth away fine distinctions (for example nearby numbers or negations).
- **Does not hold when**: queries are exact lookups or filters (use normal indexes), or the data is small enough for brute force.

## 10.4 Ingestion: parse, chunk, embed, store
- **Thesis**: retrieval quality is decided mostly at ingestion, and the best ingestion is custom to the documents.
- **Mechanism**: embedding a whole large file in one vector loses detail; split it. Fixed-size (words or sentences) chunks are described as almost useless; semantic chunking works better but is slow, so in practice teams write a **custom parser and chunker** after studying 20-30 real documents with a subject-matter expert: header and footer as their own chunks with higher weight, one chunk per image or table, paragraphs as text chunks. Large tables are split into row groups and **each chunk repeats the column headers and a description** of the columns, and may carry a short summary. Images need a multimodal encoder, or captions, or an image-to-text step. Add metadata to chunks. Each chunk becomes one vector.
- **Trade-off**: effort and domain involvement; ingestion cost grows with volume (parallel ingestion speeds it up and costs more).
- **Does not hold when**: the data is dynamic structured data (a live database) - chunking static copies makes them stale.

## 10.5 Retrieval problems and the fixes in order
- **Thesis**: fix retrieval only after traces show retrieval is the root cause, and start with the cheapest fix.
- **Mechanism**: (1) parsing and chunking (is the document broken wrongly?); (2) retrieve more candidates; (3) re-rank; (4) rewrite the query. If the request pipeline works, change nothing.
- **Trade-off**: each step costs latency and money.
- **Does not hold when**: the pipeline is untested - first collect traces.

## 10.6 Re-ranking with a cross-encoder
- **Thesis**: retrieve many cheaply, then score a few precisely.
- **Mechanism**: retrieve the top 20 chunks instead of 5; pass each (query, chunk) pair through a cross-encoder that compares tokens of both texts directly through an attention operation and returns a score; keep the top 5. Because vectors smooth numbers ("$550" and "$2,500" and "$500-1000" look alike) and negations ("excluding Intel"), the pairwise check separates relevant from merely similar. Local models do this without paying for model tokens.
- **Trade-off**: slower and more compute than plain vector search; not 100% safe.
- **Does not hold when**: simple semantic matches are already accurate.

## 10.7 Query rewriting and decomposition
- **Thesis**: one retrieval cannot serve a compound question.
- **Mechanism**: a small model splits a multi-part query ("suggest birthday gifts; how many flowers in one delivery?", or "compare tax rules for two years") into sub-queries, retrieves for each in parallel, generates for each, and combines the pieces by simple concatenation or with a small model asked to synthesise. The small model first decides whether to split at all. A summariser can shorten very long queries but is rarely used.
- **Trade-off**: more hops, more tokens, longer wait, usually worth it for comparisons. Latency is managed by parallelism, cost is not.
- **Does not hold when**: queries are single-topic.

## 10.8 Static architecture choices
- **Thesis**: whether to include a re-ranker or a rewriter is a design-time decision.
- **Mechanism**: the system cannot know at run time whether the retrieved order is good without running the fuzzy step itself; so the steps are in or out of the pipeline. Only agents (ch11) choose steps dynamically.
- **Trade-off**: fixed cost on every query.
- **Does not hold when**: you can route cheap vs hard queries with a classifier.

## 10.9 RAG over databases, graphs and agents
- **Thesis**: choose the retrieval form by data shape.
- **Mechanism**: for live structured data, expose each source as a tool, or let a model write the query given the schema, run it, and answer from the result - this is the first step toward **agentic RAG**, where an agent picks sources in a loop. Ask first whether an API call would do. **Graph RAG** follows links from a retrieved document to linked ones (related cases, pages, outage causes); someone has to build the graph. Static documents suit chunking; dynamic ones make the chunks stale.
- **Trade-off**: dynamic queries can go wrong; graphs need maintenance.
- **Does not hold when**: a fixed path is known; then make the path concrete.

## 10.10 RAG vs tools
- **Thesis**: RAG supplies **information**; tools (and the protocol that exposes them) supply **capabilities**.
- **Mechanism**: if the need is to read context, retrieve; if the need is to change the world (book, send), call a tool. A read-only tool can fetch the latest data (last ten minutes of telemetry) without any embedding.
- **Trade-off**: a design may need both.
- **Does not hold when**: the distinction blurs (a search tool is both).

## 10.11 Model size and cost
- **Thesis (position)**: RAG generation often works with smaller models, while agents need larger ones.
- **Mechanism**: reading provided chunks and answering is a narrower task than choosing tools in a loop; models of a few billion to tens of billions of parameters can suffice for RAG, though results vary.
- **Trade-off**: smaller models need tighter prompts.
- **Does not hold when**: questions require deep reasoning over context.

## 10.12 Scale and product choices
- **Thesis**: scale rarely reaches billions of vectors; split data by use case when it does.
- **Mechanism**: a billion embeddings is the territory of the largest companies. For tens of thousands of chunks a vector extension of a relational database is enough; hosted vector services, managed file-search products and object-store vectors exist, with dedicated vector stores for larger scale. Hybrid lexical-plus-semantic search is a common approach at scale. Claims that a technique makes RAG obsolete should be treated as marketing until proven in practice.
- **Trade-off**: managed services trade control for speed.
- **Does not hold when**: your data is legally or contractually restricted (vendor promises not to train on enterprise data are the stated protection).

## 10.13 Grounding, evaluation and history
- **Thesis**: you cannot guarantee correctness; you can measure and reduce error.
- **Mechanism**: (a) use another model as a judge to check that retrieved documents are relevant to the query and that the answer uses them (grounding); a practitioner reported 5-10% of results flagged; (b) sit with a domain expert to write the system prompt; (c) avoid piling ad-hoc "never do X" rules into prompts, which moves problems around; automated prompt optimisation is described as not yet practical; (d) conversations grow: store long-term and short-term memory with a saver rather than resending all turns, which raises tokens and latency.
- **Trade-off**: evaluation has its own cost and can be wrong.
- **Does not hold when**: stakes are low and errors cheap.
