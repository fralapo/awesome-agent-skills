# Chapter 4: Customer, Sales and Staff Assistants on Messaging Channels

## Core Idea
Mainstream messaging apps are where many customers, guests and staff already are, which is why assistants for lead follow-up, support and daily reporting are built there first. The pattern that works in practice is **small, specialised agents; fixed steps for what must always happen; model calls where interpretation is needed; structured storage and a dashboard; and a person for anything with responsibility**. The platforms impose rules (approved message templates, limits on human intervention in automated chats, costs per conversation) that shape the design as much as the model does.

## 4.1 Reactivating dormant leads
- **Principle**: An old contact list plus history (purchases, interests) can be re-engaged with personalised, offer-linked messages, classified by reply (interested, not interested, wants something else).
- **How it works / sequence**: Input table (contact, name, history, interests) and a knowledge base; a first message sent through the platform's business interface with an approved template and variables; classify each reply; collect the missing facts (budget, who is travelling, dates); book a call or hand over to a person.
- **Moves**: Define two global intents that work at every step: "I want a person" and "I want an appointment". Keep a pipeline with statuses so a person can pause the agent and take over.
- **Evidence**: Observational. Reported results come from the sellers of these systems and from screenshots; treat any specific revenue figure as an unverified claim (**Contested**).
- **Trade-off**: Messages initiated by the company cost money and consent rules apply.
- **Does not hold when**: There is no consent to contact the list, or the list is stale beyond use.

## 4.2 Qualifying leads
- **Principle**: Ask a few weighted questions (budget, urgency, similar services), combine them into a score, and act on a threshold: qualified leads get a calendar slot, others a polite alternative.
- **Moves**: Write the weights and threshold down and review them against outcomes. A deliberate short delay before replying and grouping several incoming messages before answering makes the conversation feel natural and avoids answering half a thought.
- **Evidence**: Practitioner for the structure; the weights are a **Position** and must be fitted to your business.
- **Trade-off**: Scoring can reject good leads whose first answers were vague.

## 4.3 Making conversations natural without deceiving
- Handling voice notes, several messages in a row, slight variation in wording and timing all improve the experience. Claims that "most people cannot tell" are unmeasured. **Position**: tell people they are talking to an assistant where your rules or local rules require it, and offer a human route; do not build the system on concealment.

## 4.4 Daily reporting from staff
- **Principle**: Instead of a form, the assistant asks at a set time what was done. People answer by text, voice or photo; the assistant extracts structured fields (date, duration, site, team, equipment), asks for corrections, and stores them.
- **How it works / sequence**: Wait a short moment to group messages; extract one field per small step; check that every person, site and vehicle exists in the registry before saving; send a correctable summary; store in a table; build a dashboard with filters; send a weekly summary by email.
- **Moves**: Plan follow-ups for people who do not reply (a reminder, a second reminder), and keep the sequence editable.
- **Evidence**: Practitioner for the design; time-saving figures are claims.
- **Trade-off**: Staff may feel watched; agree purpose and retention with them first.

## 4.5 Email quotes and routine requests
- **Principle**: Classify incoming mail (quote, information, support, order); filter spam and duplicates before the agent sees it; look up the customer's identifiers from several sources; draft the reply.
- **Moves**: A **draft approved by a person** is the default for anything that commits the company. Run OCR on image signatures and attachments where needed.
- **Evidence**: Practitioner.

## 4.6 Answers that carry responsibility (a medical-style example)
- **Principle**: Where an answer can harm (health, legal, financial), use layered sources and mandatory human approval.
- **How it works / sequence**: Level one: answers already validated by an expert. Level two: an internal library of documents the expert has approved. Level three: a live search of an authoritative database. Score and rerank sources; exclude outdated documents; send low-confidence cases to the expert; learn only from corrections the expert explicitly confirms.
- **Evidence**: Practitioner for the layering. Savings estimates are **Contested** (the client of one such project called theirs a gamble).
- **Does not hold when**: The domain has regulation of its own (clinical, legal): then get professional and regulatory advice before building. This skill gives none.

## 4.7 Platform rules and costs
- Business messaging platforms typically require approved templates for company-initiated messages, may charge per conversation, and may bar manual replies in chats of a number run by an automated agent unless a compliant inbox tool is used. **Details change often: read the current platform policy before designing.** Phone and voice agents add their own issues: dates, times and spelled-out email addresses are misheard, so confirm them back.
- Test voice and chat flows in text before spending voice minutes.

## 4.8 Cold outreach
- Automated outreach by email or professional networks can work but is limited by sender reputation (correct DNS records, gradual warm-up), by platform limits on connections and messages, and by law and platform terms. Check consent and local rules; the first message and the offer matter more than volume.

## Common Mistakes
- No human takeover route.
- Contacting a list without consent or template approval.
- No validation against the registry before saving staff data.
- Letting the model answer from memory where a validated source exists.
- Judging a pilot on a handful of friendly test chats.
- Spending voice minutes on testing that text could do.

## Checklist
- [ ] Consent, templates and platform rules checked
- [ ] Global intents: person, appointment
- [ ] Status pipeline and takeover control
- [ ] Extraction validated against the registry
- [ ] Drafts approved by a person where the company commits
- [ ] Sources layered and dated for high-stakes answers
- [ ] Dashboard and weekly summary exist

## Connects To
- ch05 (return and case studies), ch06 (reliability and security).
- `coding-with-agents` ch07-ch10 for building and testing these agents; `marketing-mba` for offer, segmentation and funnel logic; `pricing-and-sales-negotiation` for the commercial conversation the assistant hands to a person.
