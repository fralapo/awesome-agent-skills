# Coding with Agents: Cheatsheet

Figures are rules of thumb or reported results; re-test on your work. "Position" = judgment, not fact.

## Delegate or Read?
| Task is... | Do |
|---|---|
| Isolated, specified, observable, testable | Delegate; judge by behaviour and tests |
| Core, security-sensitive, performance-critical, or you are learning | Read the code; hand-polish the core |
| Open-ended ("make it faster") | Do not delegate; add design hints or split |
| Long, unattended, high consequence | Do not delegate without supervision |
| Poorly known library | Provide docs or write by hand |

## Loop
Design chat → MVP + constraints + references → minimal core → one feature at a time → observability + baseline → steer, interrupt early → verify (other model) → repeat.

## Spec Contents
Goal · constraints (language, no dependencies, libs) · non-goals · design intuitions (non-binding) · critical decisions (what is shared/split) · future data-model shape · how to test · "announce each significant step" · instructions file with stack preferences.

## Give the Agent Eyes
Debug socket / state dump · baseline benchmark · screenshots + simplified layout tree (UI) · reference-implementation comparison (numeric) · failing-input dump.

## Test Menu
Differential vs trivial reference · invariants · boundaries N-1/N/N+1 · smart generator (compressible, corrupted, flips, crossover) · scale (millions; delete 95%) · printed RNG seed · sanitizers/leak checker · fast suite · agentic QA with second-agent bug check · line coverage = to-do list, not proof.

## Quality Moves
Refuse 10-20%-value / 80%-effort features · few lines, few dependencies · vendor small libs, library for hard domains (crypto, graphics) · group nodes to cut indirection · rewrite = restructure first, no 1:1 port · stop and refactor when fragile · flag irreversible choices (language, framework, schema, API).

## Never
Accept-accept-accept · brute-force prompting · production access · agent cleanup crew · "tests pass = equivalent" · platform before product · more projects because you can.

## LLM Settings
Code/facts: temperature 0 (greedy) · creative on RL-heavy models: raise it · loops: fix model, not penalties · N samples → ask for a new answer, not "pick best" · keep a progress document for long runs · tool descriptions clear, arguments separated.

## Cost (positions)
Flat subscriptions beat per-token API for routine work (quoted range 150-300 USD/month per developer) · two vendors as hedge · review usage after a few months · single-token identifiers · result per token.

## Chat Habits (ch06 s10)
Dossier of context · ask it to ask questions · ask its assumptions · push past first answer · simplest solution · red-team the plan · two different models (agreement is a hint) · fresh chat when long · verify numbers and sources.

## Unattended Agents (ch06 s11)
Spending cap + alert + kill switch · backups on more than one storage, restore tested · separate host and dedicated account · keys never in prompts, rotated · no production write access · human gate on customer-facing or irreversible steps · stable prompt prefix, same model per conversation.

## Auth Checklist
Length 8+ (10-12 better), no composition rules · Argon2 (bcrypt ok), per-user CSPRNG salt, 100 ms-1 s · same error for unknown user/wrong password · exponential backoff then CAPTCHA/email · session 128+ bits, server-side, invalidated on logout/reset, timeouts · HttpOnly + Secure + SameSite lax · reset email = separate path · 2FA · idempotent payments.

## Learning
Write by hand to keep skill (tutor that withholds answers beats free answer-giving in one study) · cheap signals (CV, letter) are inflated; costly ones count.
6-12 months for a jump · one language by heart · plain chat first · hand-write toy programs (interpreter, database, game) · reread hard material many times · publish and join better peers · skill returns in about a week after a break.

## Context and Harness (ch07)
Measure the fixed prefix (tool definitions included) · find the quality knee, compact below it · load few stable rules, retrieve by key or meaning, externalise big output, compact lossy, isolate with sub-agents that return conclusions · fewer, sharper tools; errors say how to recover · bounded output, visible failures, no hidden prompts · guardrails in code, deny by default · memory: distil, scope, date, gate writes · cost per completed task.

## Evals and Production (ch08)
Start from the failure that matters; test the not-do · deterministic checks first; judges calibrated on labelled cases · several runs per case: pass@k for retries, pass^k for experience · per-step reliability compounds along the path · trace every run; cluster failures by cause · protect verifiers from the agent's write scope · shadow mode, then staged rollout, thresholds fixed in advance · bounded retries, idempotent actions, kill switch.

## Sessions, Tokens, Environment (ch09)
Measure the fixed prefix at session start · one task per session · fix model and effort at the start · handoff file (goal, decisions and why, problems, files, open questions, next steps) instead of automatic compaction · instructions file = short index, rare procedures = skills · disable unused tool servers; CLI over protocol for local repeated work · pre-extract text from bulky documents in code · reasons instead of bare bans; goal and "done" criterion; interview first; sketch before build · hooks for what must always happen; secrets in env files; read downloaded skills before use · parallel sessions in separate working copies.

## Combining Agents and Tools (ch09)
Builder is not the judge · plan -> adversarial review by a second tool -> reply -> repeat -> human reads -> implement -> security review -> cross-check · blind-spot pass: read-only parallel explorers, four categories of unknowns, interview one question at a time · split by role, not by difficulty · sub-agents for bulk, teams only for truly parallel work, contract first · no merge without review.

## Building and Testing Agents with Workflow Tools (ch10)
Trigger -> steps -> output; code for logic and dates, model for judgement · generated workflow = skeleton · tool description = contract; one workflow per operation; publish/activate it · narrow scopes, expiring keys in env files · same embedding model both sides; sources and dates on chunks · availability and totals from tools, not words · test: plumbing (test vs production endpoint), each step, end to end, edge cases, misuse, repeat run, polling limits, scale gradually, human approval, logs and cost per task, kill switch.

## Hand-offs
Roll-out in a company (training, company knowledge, customer assistants, return) → `ai-adoption-in-organizations` · UI/UX decisions → `ux-ui-expert` · spec workshops → `workshop-facilitation` · pricing → `pricing-and-sales-negotiation` · visuals → `art-director` / `graphic-designer`.
