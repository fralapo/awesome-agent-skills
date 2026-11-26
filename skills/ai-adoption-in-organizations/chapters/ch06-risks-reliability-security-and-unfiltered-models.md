# Chapter 6: Risks: Reliability, Contradictory Sources, Security and Unfiltered Models

## Core Idea
Organizations meet the same risks again and again: answers that sound right and are wrong, source documents that disagree with each other, agents with too much access, cost loops, and the temptation to use powerful models without safety filters. Most of these are managed by **design in code and process**, not by instructions in a prompt. This chapter states the risks and a conservative response to each, without legal or compliance advice.

## 6.1 Reliability of answers
- **Principle**: A fluent answer is not a checked answer. Reliability falls with each added step, tool or function.
- **How it works / sequence**: If every step is right 90% of the time, five steps in a row are right about 59% of the time (arithmetic, assuming independence). Therefore shorten the path, make steps deterministic where possible, and check the end state.
- **Moves**: Require sources for numbers and claims; run the output against a rubric or test; show confidence to the reader; sample outputs for review on a schedule. For evaluation methods see `coding-with-agents` ch08.
- **Evidence**: Fact for the arithmetic; Practitioner for the moves.
- **Trade-off**: More checks mean slower answers.

## 6.2 Contradictory rules in your own documents
- **Principle**: An assistant that reads two documents with conflicting rules (an old price list and a new one, a policy and an exception) will pick one, often the wrong one, and sound sure.
- **How it works / sequence**: Give every source an owner, a date, a status (current, superseded) and a precedence rule (newer wins, specific beats general, a named authority wins). Surface conflicts to a person rather than letting the model reconcile them silently.
- **Moves**: Before launching a knowledge assistant, run a "contradiction sweep": ask it questions known to touch overlapping documents and read the answers. Archive superseded files out of the search area instead of deleting history.
- **Evidence**: Practitioner.
- **Does not hold when**: The corpus is small and fully curated.

## 6.3 Prompt injection and over-broad access
- **Principle**: Text from emails, web pages and documents is data, but a model may follow instructions hidden in it. The dangerous combination is private data, untrusted content and a way to send things out, all in one run.
- **Moves**: Deny access by default; give each agent only the files, accounts and actions the task needs; require approval for sending, deleting or paying; keep keys out of prompts and out of repositories; set spending caps and disable automatic top-ups; use dedicated accounts and, for always-on agents, dedicated machines or servers rather than a personal laptop. A screening step in front of the agent (checks for jailbreak patterns, personal data, secrets, links) lowers risk but **does not stop all injection**; the share it catches is unverified, so never rely on it alone.
- **Evidence**: Practitioner; see `coding-with-agents` ch07 section 8 and ch08.
- **Trade-off**: Approvals add friction; broad approvals breed fatigue, so bind approvals to specific actions.

## 6.4 Cost loops and accidents
- An agent that retries forever, or is left running with a pay-per-use key, can run up a bill in hours. Use step limits, budget alerts and a kill switch. Back up what an agent may modify, and test restoring.
- Connecting a personal subscription to a third-party agent tool may break the provider's terms and lead to account suspension (**Position**, reported by practitioners): read the terms and prefer an API key with a cap for such uses.

## 6.5 Security of generated applications
- Apps built quickly with an agent have repeatedly shown exposed data and missing checks in independent reviews (unverified email addresses, unprotected endpoints, unchecked uploads, no payload limits, no abuse protection). **Position**: an agent that says "done" is not an audit.
- **Moves**: Have a second model or tool review the plan and the code; run the platform's security review; then check the stack-specific rules (access policies on the database, secrets, rate limits). Keep repositories private. For an application with many users or sensitive data, hire a security professional. See `coding-with-agents` ch03 and ch06.

## 6.6 Unfiltered ("uncensored") models
- **Principle**: A model with its refusals removed refuses less; it is not smarter and may be less capable.
- **Why people use them**: commercial assistants often refuse legitimate security testing of one's own application, leaving small organizations without cheap testing.
- **Moves and limits**: Use only on systems you own or with **written permission** from the owner. The workflow is: scoped scan of one domain, a report in plain text, fix with your usual assistant, repeat. Run it through a hosted provider, a rented machine you shut down, or locally, and cap spending. Do not use such models to produce operational harm; this skill does not describe attack techniques.
- **Evidence**: Position (an argument about a gap in the market); the legal and contractual side is for a professional.
- **Trade-off**: Frontier models refuse more often than older ones; scanners and test frameworks may find more with fewer false alarms than a raw model.

## 6.7 Regulation and training duties
- Several regions require organizations to train staff who use AI and to keep documentation, with penalties tied to size or turnover. **Verify the current official text; this skill does not interpret it.** A practical response is to map where AI is used, keep a training record, and write simple standard procedures.

## 6.8 Debate, forecasts and hype
- Claims about existential risk, regulation proposals and market winners are **Positions or forecasts**. Keep them out of the business case; plan for vendor change instead.

## Common Mistakes
- Trusting a screening node as a complete defence.
- Letting an agent hold keys, files and a send button at once.
- Treating "done" from the agent as a security review.
- Conflicting documents in the same search area.
- Using a personal account for always-on automation.

## Checklist
- [ ] Sources have owner, date, status, precedence
- [ ] Deny-by-default access; approvals bound to actions
- [ ] Spend cap, step limit, kill switch, tested backups
- [ ] Independent review of generated apps; expert for high stakes
- [ ] Written permission for any penetration testing
- [ ] Training record and AI-use map kept

## Connects To
- ch03 (data), ch04 (customer-facing risk), `coding-with-agents` ch06-ch10, `software-engineering-practice`, `ai-ml-concepts` ch15 (agents), `scientific-thinking` (judging claims).
