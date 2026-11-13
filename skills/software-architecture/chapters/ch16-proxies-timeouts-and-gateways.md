# Chapter 16: Proxies, Timeouts, Load Balancing and Gateways

## Core Idea
A proxy is a machine that makes requests on someone else's behalf; every proxy adds a hop, a second connection and a set of clocks. In this model the architect decides where traffic is terminated (layer 4 or layer 7), which side owns each timeout, how requests are spread, and which cross-cutting concerns (authentication, rate limits, discovery) live at the edge. Most proxy incidents are timeout or pooling mistakes, not algorithm choices.

## 16.1 What a proxy changes on the wire
- **Thesis**: a proxy splits one end-to-end connection into two, and the server never sees the original client unless told.
- **Mechanism**: without a proxy the client resolves the name, opens a TCP connection to the server, and sends the request. With a forward proxy the client connects to the proxy; the request carries the target in a host header (added in HTTP/1.1 precisely so proxies know where to forward); the proxy opens its own connection and forwards the request. Proxies commonly add headers carrying the original client address so the server can apply regional rules or blocks. Connections between proxy and server are pooled and shared between clients, which saves resources but risks leaking one client's response to another if state is bound to a connection. For secure traffic the client sends a tunnel request (CONNECT) and the proxy blindly relays bytes: it sees addresses and sizes, not content. A TLS-terminating or inspecting proxy can read everything by presenting its own certificate; that is how debugging proxies and corporate inspection work and requires the client to trust the proxy's certificate authority.
- **Trade-off**: visibility and control versus trust: a terminating proxy is a full man in the middle, so install no certificate you do not control.
- **Does not hold when**: traffic is end-to-end encrypted with certificate pinning (the proxy can only tunnel).

## 16.2 Layer 4 versus layer 7
- **Thesis**: a layer-4 balancer forwards connections; a layer-7 balancer understands requests. Pick the lowest layer that does the job.
- **Mechanism**: L4 forwards bytes after the TCP handshake, keeps the protocol end to end (HTTP/2, WebSocket, custom), is cheap and cannot route by path, header or cookie. L7 terminates TLS, parses requests, routes by content, rewrites, authenticates, caches, retries and compresses; it must speak every protocol version you want to preserve (ch13 13.3). A web server and a proxy in one process is a complexity trade-off: a dedicated proxy is simpler to reason about (position).
- **Trade-off**: features versus CPU, latency and failure surface.
- **Does not hold when**: you have one backend and no routing needs.

## 16.3 Timeouts: every hop needs its own clock
- **Thesis**: a request that no longer matters still consumes a connection, a thread and memory; timeouts are how a proxy decides a client or backend is not worth keeping. Missing timeouts were a factor in several large outages (ch15).
- **Mechanism**: on the client side of a reverse proxy: (a) idle timeout: the client sends nothing for too long; (b) send/ack timeout: the proxy wrote data and the client does not acknowledge, which should be shorter than the idle timeout and is not configurable in every proxy; (c) request-read timeout: the whole request must arrive within a bound, the defence against slow-send attacks in which a client dribbles one segment at a time so the idle timer keeps resetting; set it from the legitimate maximum (an upload may need more); (d) keep-alive: how long a connection may wait between requests. On the backend side: (e) connect timeout, short (a second or a few) since the backend is nearby; (f) response timeout: the time waiting for the backend to answer, the most important one, set from measured latency with a buffer (for example the observed maximum plus margin) per endpoint, not one value for all; some proxies separate header and body timers, others keep one simpler knob. Return a timeout error to the client rather than hang.
- **Trade-off**: tight timeouts shed useful slow work and cause retries; loose ones let slow clients and dead backends pin resources.
- **Does not hold when**: legitimately long operations exist (uploads, reports, long polling); give them a separate route or an async job (ch07 7.7).
- **Rule**: timeouts across a chain should shrink from the caller inward, otherwise an inner service works on a request the outer one has already abandoned (see 3.7).

## 16.4 Load-balancing algorithms
- **Thesis**: static algorithms are simple and ignore server state; dynamic ones adapt and cost monitoring.
- **Mechanism**: static: round robin (rotate; fine for stateless homogeneous servers), sticky round robin (same client to same server to keep related data warm; uneven load), weighted round robin (weights reflect capacity; manual), hash-based (hash of client address or URL picks the server; good for cache locality, reshuffles when the pool changes unless consistent hashing is used, ch05 5.3). Dynamic: least connections (route to the server with the fewest open requests; connections can pile up unevenly), least response time (route to the fastest; needs continuous measurement and ignores queue depth). Choose static for stateless tiers and dynamic for heterogeneous or long-running requests.
- **Trade-off**: overhead and complexity versus adaptation.
- **Does not hold when**: a hot key or large request dominates (balance by request cost or split the key, ch05 5.6).

## 16.5 Request coalescing with hash routing
- **Thesis**: when many clients ask for the same item at once, send one query and fan the answer out.
- **Mechanism**: a data-access service keeps an in-flight task per query; the first request starts the task, concurrent identical requests subscribe to it. For it to work the balancer must send identical requests to the same instance, so route by a hash of the entity (consistent hashing). A viral announcement read by a hundred thousand clients becomes a handful of database queries.
- **Trade-off**: hot instances for hot keys; in-flight state to manage.
- **Does not hold when**: requests differ per user or results cannot be shared.

## 16.6 API gateway
- **Thesis**: one entry point lets clients stay ignorant of the backend layout and gives one place for cross-cutting policy.
- **Mechanism**: routing, authentication, rate limiting, response aggregation, protocol translation, retries, circuit breaking, response caching and logging. A mobile screen can be assembled from several services behind one call.
- **Trade-off**: the gateway is on every request and becomes a single point of failure and a bottleneck if under-provisioned; policy logic accumulates.
- **Does not hold when**: a single service serves the client directly.

## 16.7 Service discovery
- **Thesis**: in elastic environments addresses change, so callers look up where a service currently runs.
- **Mechanism**: instances register on start and deregister on stop; callers query a registry (DNS-based, dedicated registry or the orchestrator's built-in discovery). Hard cases: registry unavailable (cache last known), dead instances not removed (health checks, timeouts), mass ejection under network trouble (cap the share removed, ch15 15.3).
- **Trade-off**: more moving parts and a new dependency for every call.
- **Does not hold when**: a small fixed set of hosts.

## 16.8 Delegated authorization (OAuth 2) in one picture
- **Thesis**: let a third party act on a user's behalf without giving it the password, with limited scope and revocable access.
- **Mechanism**: roles: resource owner (the user), resource server (holds the data), client (the third party), authorization server (may be part of the resource server). The client sends the user to the authorization server with its client id and requested scope; the user authenticates there and consents; an authorization code returns to the client; the client exchanges code, client id and client secret (known only to it and the authorization server) for an access token; it calls the resource server with the token. Tokens expire and can be revoked; a refresh token gets a new access token without asking again.
- **Trade-off**: more redirects and moving parts; the client secret must be kept server-side.
- **Does not hold when**: first-party only, with no third party (a simple session or token may do).

## 16.9 Microservices and message queues: when the split pays
- **Thesis**: splitting a system into services trades function calls for network calls.
- **Mechanism**: separate services let teams deploy and scale independently and pick technology, but each call can time out or fail, and you need monitoring, logging, error handling and discovery. A shared queue decouples producers and consumers in time (delivery guarantees at-most-once, at-least-once or exactly-once; ch07 7.6) and shifts effort to handling partial failure and consistency. Persistent connections (WebSocket) are stateful and need reconnection logic, heartbeats and fallbacks behind proxies and firewalls.
- **Trade-off**: autonomy versus distributed-systems complexity.
- **Does not hold when**: a small team and a simple domain; a modular single deployable is cheaper (position).
