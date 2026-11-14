# Software Architecture: Cheatsheet

Figures are rules of thumb or values stated at the time; re-test. "Position" = judgment, not fact. Chapter references in brackets.

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

## Protocol and Connection Choices [ch13, ch16]
| Situation | Choice | Watch out |
|---|---|---|
| Many small requests, one host | HTTP/2 end to end | Every proxy must speak it; avoid blind server push |
| Lossy or mobile network | HTTP/3 (UDP-based, connection ids) | UDP must pass firewalls |
| Need path/header routing | Layer-7 balancer | Must preserve the protocol version |
| Keep protocol end to end, minimal logic | Layer-4 balancer | No content routing |
| Secure channel | TLS 1.3 (one round trip, forward secrecy) | Termination points see plaintext |
| Short-lived connections | Reuse (keep-alive, pool, multiplex) | Slow start and handshakes on each new one |
| Latency rises, CPU idle | Count connections, ports, descriptors | Ephemeral port range is only about 28,000 |
| Server must accept many connections | Several listeners (address reuse) or request-level dispatch | Binding to all interfaces exposes admin ports |

## Timeout Map for a Reverse Proxy [ch16]
| Hop | Timer | Typical rule |
|---|---|---|
| Client to proxy | idle, send/ack, whole-request read, keep-alive | Bound the whole request (slow-send defence); longer only on upload routes |
| Proxy to backend | connect | Short (backend is near) |
| Proxy to backend | response | Measured maximum plus margin, per endpoint |
| Chain | caller > callee | Inner timeouts shrink; no work for abandoned requests |

## Cache Failure Modes [ch06 6.12]
| Mode | Cause | Fix |
|---|---|---|
| Stampede | One hot key expires, many recompute | Per-key lock, stale copy, refresher, early probabilistic refresh |
| Penetration | Keys that do not exist | Placeholder with short time-to-live, Bloom filter |
| Avalanche | Many keys expire together, or cold/failed cache | Jittered expiry, redundant cluster, pre-warm, circuit breaker |

## Database Operations Checklist [ch14]
| Question | Why |
|---|---|
| Oldest open transaction? | Pins dead row versions, causes bloat |
| Which lock mode does this migration take, and who is it queued behind? | A queued strong lock blocks all later queries |
| Index used? (read the plan on production-size data) | Low selectivity, function on column, wrong column order, OR |
| Log flushed at commit? Checkpoint spikes? | Durability versus occasional latency |
| Connections per process vs limit | Process-per-connection costs memory and page tables |
| Update order consistent across code paths? | Prevents deadlocks |

## Incident Questions [ch15]
Smallest change that removes the health signal? Does recovery depend on the failed system? Which automatic action is catastrophic when correlated (withdraw, eject, scale, retry, restart)? Which shared choke point lacks a capacity alarm? Can everything restart together? Did the alert fire on the cause?

## CRUD or Task-Driven? [ch17] (position)
| Signal | Lean |
|---|---|
| Users maintain reference data, no rules | CRUD |
| Users perform a capability with order, validation, outcomes | Task-driven commands, named facts |
| External system owns the behavior, you map data | CRUD |
| Downstream needs to know why (cancelled vs not used) | Capture intent at the action |
| Collection is huge and the rule is a count | Enforce the rule, not the relationship (17.3) |

## Decoupling Spectrum [ch18 18.6]
| Step | Gain | Cost |
|---|---|---|
| Direct call | Call stack, order | Shared availability |
| Interface | Seam | Indirection (worse with one implementation) |
| Queue | Time decoupling, spikes | Retries, duplicates, dead letters, lost stack, "accepted" not "done" |
| Events | Fan-out, extensibility | Invisible behavior, contracts to version |

## Four Meanings of "Event" [ch19 19.1]
| Use | Boundary |
|---|---|
| Event sourcing | Internal, state storage |
| Event-carried state transfer | Data distribution; stale copy |
| Notification (domain/integration) | Fact; integration event is the contract |
| Workflow step | Between participants; commands have one handler |

## Stale Read After a Write [ch19 19.9]
| Try first | Then |
|---|---|
| Read from the primary; send the user elsewhere; add the new id locally | Wait out the lag; update projection in the command |
| Return log position or version at write; read compares | Push update or poll |
| Read enforces a rule on another boundary's copy | Move the decision to the data owner |

## Calling an External System Safely [ch20, ch14 14.10]
| Layer | Note |
|---|---|
| Provider idempotency key | Same key on retry; offer one in your own API |
| Lookup by reference id | Race remains unless provider enforces uniqueness |
| Lock per granular business key | Lowers throughput; a timeout is not a failure |
| Pending state plus outbox, separate handler | Better state; can still double charge |
| Reconciliation or compensation | Last line; goal is effectively once |

## Multi-Tenant Isolation Menu [ch18 18.9]
| Resource | Shared | Pooled | Dedicated |
|---|---|---|---|
| Data | Tenant id column | Schema or database per group | Database per tenant |
| Compute | Same instances | Instances per tier | Instances per tenant |
| Cheaper levers first | Per-tenant rate limit, per-tenant connection pool | | |

## Time, Order and "Exactly One" [ch21]
| Need | Use | Watch out |
|---|---|---|
| Elapsed time | Monotonic clock | Time-of-day clock jumps on sync |
| Order concurrent writes, keep both | Version vectors (siblings) | Size grows with replicas |
| Order concurrent writes, pick one | (counter, node id) logical timestamp | One write lost; order known only afterwards |
| One lock holder or leader | Majority decision plus fencing token checked by the resource | Pauses make a holder wrong without knowing it |
| Strong single-object consistency | Linearizable store via consensus log | Cost on every write; not the same as serializable |
| Real-time order across machines | Bounded clock error plus commit wait | Needs specialised time infrastructure |
| Atomic commit over partitions | Two-phase commit with replicated participants | Blocks if coordinator dies unreplicated |

## Approximate Structures [ch24]
| Question | Structure | Error shape |
|---|---|---|
| Is X in the set? | Bloom filter | No false negatives; some false positives; no delete |
| How many distinct items? | Trailing-bit estimator (HyperLogLog-style) | A few percent either way |
| How often was X seen? | Logarithmic probabilistic counter | Precise at small counts, coarse at large |
| Which key to evict? | Sample, keep worst in a small pool | Sometimes not the exact worst |
| Scan flushes my cache | Young/old lists, insert at the old head | Slower warm-up of new hot pages |

## Eviction Policy Choice [ch24 24.6]
| Access pattern | Policy |
|---|---|
| Recency predicts reuse | LRU (approximate by sampling) |
| A few keys stay popular through quiet spells | LFU with decay |
| Uniform access | Random (no bookkeeping) |
| Keys carry a time to live | Evict nearest expiry; apply only to keys with expiry to protect permanent keys |
| Memory fits the data | No eviction |

## Picking a Database [ch04 4.15]
| Need | Lean towards |
|---|---|
| Transactions across rows, correctness over speed | Relational (B-tree) |
| Data read and written as one nested unit | Document store |
| Huge write rate, tunable consistency, loss of a rare write acceptable | Leaderless wide-column (log-structured merge) |
| Mergeable counters and sets with leaderless writes | Conflict-free data types |
| Hot small data, no ranges | In-memory key-value |
| Full-text search | Inverted index |

## Log Durability and Exactly-Once [ch07 7.17-7.18]
| Setting | Effect |
|---|---|
| Acknowledge none / leader / all in-sync | Loss risk vs latency |
| Minimum in-sync size | Refuse writes when the set shrinks |
| All in-sync down: wait or resume anywhere | Outage vs possible loss |
| Idempotent producer | Drops repeated batches (sequence numbers) |
| Transactional id + epoch | Fences zombie producers |
| Atomic read-process-write | Exactly once inside the log only |

## Serving a Model You Host [ch25]
| Step | Note |
|---|---|
| Weight memory = parameters x bytes | 1B parameters at 4 bytes is 4 GB before cache |
| Quantize weights offline | Quantizing weights at serving time saves nothing |
| Quantize the cache on the fly | Its vectors are produced while serving |
| Apply the scale once per dot product | Keeps the inner loop integer |
| Verify on your task | Rounding errors mostly cancel, but not always |
