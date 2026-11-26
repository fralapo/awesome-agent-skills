# Chapter 3: Company Knowledge ("Company Brain") and Sensitive Data

## Core Idea
Most organizations keep their real know-how in people's heads, inboxes, spreadsheets and old documents. A **company brain** is a deliberately built layer that makes that knowledge available to assistants, with permissions, sources and a clear home for the data. The real need of many managers is not a chatbot but **answers from their own data without invented content**: business intelligence with citations. Two questions decide the design: *where does the data live*, and *who may see what*.

## 3.1 Layers of a company brain
- **Principle**: Separate what the assistant needs to know into layers so each can be owned and updated alone.
- **How it works / sequence**: Context (who the company is, roles, tone), data (documents and tables), skills (procedures), intelligence (transcripts of meetings and calls, decisions), automations (scheduled or triggered jobs).
- **Moves**: Start with context and skills, which are cheap and human-readable. Add data connections later.
- **Evidence**: Practitioner.
- **Trade-off**: More layers mean more upkeep.
- **Does not hold when**: A single small team shares everything; one folder is enough.

## 3.2 Three technical patterns
- **Document retrieval with citation**: a maintained wiki of pages plus retrieval, so an answer can point to the page it came from.
- **Structured data through a translation layer**: tables exported from the enterprise system, described by an ontology (names and meanings of fields), queried by turning questions into database queries. Numbers come from the query, not from the model's memory.
- **Deterministic workflows with small model calls**: the fixed steps run as code; the model only classifies, extracts or drafts at named points.
- **Evidence**: Practitioner; this mix is a design position, not the only valid one.
- **Trade-off**: Each pattern needs different upkeep: pages go stale, ontologies drift, workflows need tests.
- **Does not hold when**: Questions are rare; a person with a search box may be cheaper.

## 3.3 Linked files versus retrieval only
- **Contested**: One camp says a brain made of linked, readable files (the assistant follows links) is more efficient than retrieval that only searches documents, because it keeps structure and context. Another camp says retrieval scales better and handles very large corpora. The decision rule: small, curated, human-maintained knowledge favours linked files; large or fast-changing corpora favour retrieval; many real systems combine both. Measure on your questions (see [ch07](ch07-evaluating-tools-and-models-without-hype.md)).

## 3.4 Permissions and ownership
- **Principle**: Departments get their own workspace; shared resources are visible across departments only with explicit approval from someone accountable.
- **Moves**: Decide, per source, who owns it, who reads it, how long it is valid. An answer should carry its source and date.
- **Evidence**: Practitioner.
- **Trade-off**: Tight permissions reduce the "ask anything" magic; loose permissions leak.
- **Position**: A single brain does not scale beyond a few dozen people; larger organizations need several, per department, with a shared top layer. This is a rule of thumb from practice, not a measured limit.

## 3.5 Sovereignty: model, vendor and data location
- **Principle**: Avoid dependence on one vendor. Keep context, skills and data in formats the organization owns, make the system work with more than one model, and let the company hold its own access keys.
- **Moves**: Choose storage in the jurisdiction your obligations require; where possible keep encryption keys under the company's control; document how to switch models.
- **Evidence**: Practitioner; the legal weight of location depends on your regulator, so ask a professional.
- **Trade-off**: Neutrality costs adapter work and may lose vendor-specific features.

## 3.6 Local versus public services
- **Principle**: The question is not "cloud or local" but "what is the worst case if this text leaves the building".
- **Moves**:
  - Public consumer chat services, especially free tiers, may use conversations for training and retain them: never paste customer, medical, legal or financial identifying data.
  - Business or enterprise plans and API access usually come with stronger contractual terms: still read them, and check data location.
  - For the most sensitive material, run a smaller model on company hardware, accepting lower capability and a hardware cost.
  - **Anonymise** before using a public service: replace names, identifiers and amounts with placeholders, and keep the mapping inside.
  - A sanitising step can replace detected personal data with variables before text reaches a model; keep the original under the same rules as any personal data.
- **Evidence**: Practitioner for the categories; plan terms change often, so verify them.
- **Does not hold when**: The data is already public (a demo built only from public sources is a safe way to show the idea to a prospect).

## 3.7 Transcripts and meetings
- Recordings and transcripts hold decisions nobody wrote down. Store them with consent, label speakers and dates, and keep them apart from client-confidential material of other clients.

## Common Mistakes
- Pasting identifying data into a free consumer tool "just once".
- One giant folder with no owners and no dates.
- Retrieval over documents nobody has curated; outdated pages are served as truth.
- Letting the model compute figures that a database query can return.
- Building around one vendor's proprietary storage.

## Checklist
- [ ] Data classes defined (public, internal, personal, restricted) with allowed services
- [ ] Each source has owner, date and permission
- [ ] Numbers come from queries or documents, not from model memory
- [ ] Answers cite page or table
- [ ] Model-agnostic; keys and data owned by the company
- [ ] Anonymisation step exists where public services are used

## Connects To
- ch06 (contradictory sources and security), ch02 (teaching the data rules).
- `software-architecture` for storage, interfaces and boundaries; `coding-with-agents` ch07 for context, memory and tool design; `llm-wiki` for building a wiki-style knowledge base; `ai-ml-concepts` for retrieval and embeddings.
