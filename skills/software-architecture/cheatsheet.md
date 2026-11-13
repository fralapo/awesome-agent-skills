# Software Architecture: Cheatsheet

Figures are rules of thumb or values stated in the material; re-test. "Position" = judgment, not fact. Chapter references in brackets.

## Where to Start
| Situation | First move |
|---|---|
| Vague brief | Scope features, state assumptions, estimate users/requests/data, find read:write [ch01] |
| Reads dwarf writes | Replicas, caches, precompute, eventual reads; one write path per key range [ch01, ch06] |
| Writes dominate | Batch, append to a log, log-structured storage [ch04] |
| Money or permissions | Strong consistency, quorum or leader reads, no stale cache [ch02] |
| Feature is "nice to have" | Approximate, delay or drop first under load [ch03] |

## Replication and Consistency
| Choice | Gain | Cost | Use when |
|---|---|---|---|
| Async replica | Light primary, read scale | Lag, loss on crash | Staleness tolerable |
| Sync replica | No acknowledged loss | Latency, stall if replica down | Loss is unacceptable |
| Single leader + followers | No conflicts | Write ceiling | Default |
| Two writers | Write availability | Split brain, conflicts | Mergeable operations only |
| Quorum (N=3, 2) | Correct under one failure | A second failure still errs; Q=N brittle | Leaderless stores |
| Strong read | Fresh | Hits the leader | Right after a write that matters |
| Eventual read | Cheap, balanced | Stale or resurrected data | Feeds, counts, profiles |
| Timestamp token | "At least as fresh as my write" | Client carries it | Permission checks |
| Write via nearest replica to primary | Read-your-writes | One extra hop | Social writes |
| Order + background repair | No distributed transaction | Short dangling state | Edge + inverse edge |
| Saga | Long workflows | Visible intermediate states, compensation | Orders, metered usage |

## Availability Targets (order of magnitude)
| Organisation | Typical target | Note |
|---|---|---|
| Small / early | Two to three nines | Scheduled downtime OK |
| Mid-sized | About an hour of downtime a year | Remove single points, monitor |
| Mature platform | Five to six nines | Redundancy, practised failure |
| Safety-critical | Near zero downtime | Special engineering |

## Overload Levers
| Cause | Lever |
|---|---|
| Known event | Pre-scale |
| Uncertain event | Autoscale (accept spend) |
| Viral | Rate limit + shed + cache |
| Midnight bulk send | Chunk over minutes |
| Hot publisher | Batch + jitter |
| Non-critical numbers | Approximate |
| Server lost | Capacity headroom, bounded queue, temporary/permanent errors |
| Cache cold | Constant work / warm before use / overflow pool |
| Deploy | Gradual batches |

## Storage Choice
| Need | Pick | Because |
|---|---|---|
| Files read by many | Object storage + CDN | Immutable, replicated |
| Relations, ACID, many consumers | Relational | Constraints, joins |
| Flexible schema, key access, huge reads | Document / key-value | One read, scale-out |
| Heavy writes | Log-structured store | Sequential appends |
| Ad-hoc analytics | Not a key-value store | Joins and scans |
| Nearby search | Cell code + sorted index (or DB geo extension) | Range query |
| Semantic retrieval | Vector index (+ re-rank) | Nearest neighbours |

## Shard / Cache Layout
| Pattern | Do |
|---|---|
| Request needs one key | Shard the cache |
| Request needs hundreds of keys | Replicate the cache |
| Lookups by one entity | Shard key = that entity |
| Hot key | Split by type; then bypass the cache |
| Node added/removed | Consistent hashing, replicas on next nodes |
| Unknown ownership | Coordination service (strong) or gossip (fast) |

## Realtime Transport
| Need | Use |
|---|---|
| Bidirectional low latency | WebSocket |
| Server to client only, occasional | Server-sent events or refresh |
| Tolerates loss, high rate | UDP-style stream |
| Simple, not real-time | Long polling |
| Heavy transformation | Queue + workers + 202 accepted |

## RAG Triage (symptom -> fix, cheapest first)
| Symptom | Fix |
|---|---|
| Wrong chunks, broken tables | Custom parse/chunk, repeat headers [ch10] |
| Right doc missed | Retrieve more candidates |
| Similar but wrong (numbers, negation) | Cross-encoder re-rank |
| Compound question | Decompose, retrieve in parallel |
| Live structured data | Tool / agentic retrieval |
| Linked records matter | Graph retrieval |
| Hallucinated answer | Judge grounding, evaluate, cap |
| Long chat | Memory, not full history |

## Call, RAG or Agent?
| Need | Choose |
|---|---|
| General knowledge | Plain call |
| Private / fresh information | RAG |
| Act, or pick sources over steps | Agent (loop + tools + limits) |
| Fixed steps | Plain code |

## Estimation Formulas
Events/day = users x actions. Rate = events/day / 86,400. Storage/day = events x size x copies (formats x resolutions x replicas). Burst credit = provisioned rate x seconds of bucket (200 x 300 = 60,000). Fan-out = members of the largest group x messages.
