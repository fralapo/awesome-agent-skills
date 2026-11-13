# Chapter 13: Networking and Protocols

## Core Idea
Every request pays a stack of setup costs (connection, encryption, protocol negotiation) before the first useful byte, and every long-lived connection holds kernel state. In this model the architect chooses protocols by counting round trips, head-of-line blocking and per-connection state, and treats the connection layer as a finite resource (ports, queues, memory) that fails in ways that look like application bugs.

## 13.1 The cost stack before the first byte
- **Thesis**: connect, secure, negotiate, then request; each step is one or more network round trips.
- **Mechanism**: a TCP connection needs a three-way handshake (one round trip). Secure HTTP adds a TLS handshake (two round trips in TLS 1.2, one in TLS 1.3, zero on resumption with some risk), which together with certificate checks is often a few hundred milliseconds across regions. Only then does the request leave. HTTP/1.0 repeated all of this per resource; keep-alive connections, multiplexing and session resumption exist to pay it once.
- **Trade-off**: long-lived connections save latency but cost memory and complicate load balancing and shutdown.
- **Does not hold when**: the client and server are in the same rack and the handshake is microseconds, or the request is so rare that reuse never happens.

## 13.2 HTTP/1.1, HTTP/2 and HTTP/3
- **Thesis**: each version removes the previous version's bottleneck and exposes the next one lower in the stack.
- **Mechanism**: HTTP/1.1 keeps connections open and allows chunked responses and conditional caching, but one connection carries one response at a time (head-of-line blocking at the request level), so browsers open about six connections per host and sites resorted to domain sharding and bundled assets. HTTP/2 uses a binary framing layer on one connection: requests and responses are split into frames tagged with a stream id and interleaved (multiplexing), with stream priorities and header compression that remembers earlier headers. It still runs on TCP, so one lost packet stalls every stream until retransmission (head-of-line blocking at the transport level). HTTP/3 runs on a UDP-based transport with independent streams, integrated TLS 1.3 (connection plus encryption in one round trip, sometimes zero) and connection ids that survive a switch from Wi-Fi to mobile data. Adoption: HTTP/1.1 is still common for simple sites, HTTP/2 serves a majority of web requests, HTTP/3 is growing.
- **Trade-off**: HTTP/2 needs a client and every intermediary that understands it; HTTP/3 needs UDP to pass firewalls and more CPU in user space.
- **Does not hold when**: traffic is a few large downloads (the gain is for many small requests), or the network is clean and low-latency (the gap shrinks).

## 13.3 HTTP/2 pitfalls in real chains
- **Thesis**: a protocol upgrade helps only if every hop supports it, and some features can backfire.
- **Mechanism**: (a) A layer-7 balancer that terminates TLS and speaks HTTP/1.1 to clients and backends discards the benefit: the client reverts to six connections. A layer-4 balancer just forwards the TCP stream and keeps HTTP/2 end to end. (b) Server push sends resources the client may already have cached; used carelessly it wastes bandwidth multiplied by the number of clients. (c) HTTP/2 is deployed over TLS in practice, and the protocol is negotiated inside the TLS handshake through an extension, so no extra upgrade round trip is needed. (d) A demo with a hundred small images showed multiplexing cut load time from tens of seconds to a few seconds on a slow mobile profile; the gain grows with latency and request count.
- **Trade-off**: an L4 balancer cannot route by path or header; an L7 balancer must be HTTP/2-aware.
- **Does not hold when**: you serve one big file per page.

## 13.4 What HTTPS adds, and why TLS 1.3 is faster and safer
- **Thesis**: plain HTTP gives a message format with no privacy, no proof of server identity and no integrity; TLS adds the three. HTTPS is HTTP inside a TLS tunnel, not a different protocol.
- **Mechanism**: the client hello lists supported protocol versions and ciphers; the server answers with its choices and a certificate (domain name, public key, signature by a trusted authority). The client rejects expired, wrong-host or untrusted-chain certificates and the server must prove it holds the matching private key. TLS 1.2 allowed key exchange by encrypting a secret with the server's public key: if the server's private key leaks later, recorded traffic can be decrypted, and the negotiation of many options costs extra round trips. TLS 1.3 removed that mode and many legacy options: each side generates temporary key material, the public parts are exchanged, and both compute the same secret independently (ephemeral Diffie-Hellman), so the secret is never sent and old sessions stay safe after a key leak (forward secrecy). Bulk data then uses fast symmetric encryption; the slower asymmetric work is only for identity and key agreement.
- **Trade-off**: a termination point (proxy, balancer) sees plaintext; encryption costs CPU and handshake latency.
- **Does not hold when**: traffic is on a trusted link inside one machine or an already-encrypted tunnel (even then, zero-trust designs encrypt internally).

## 13.5 TCP congestion control: slow start and congestion avoidance
- **Thesis**: a new connection starts small and grows; a loss makes it shrink hard. Short-lived connections never reach full speed.
- **Mechanism**: the sender limits data in flight by a congestion window, starting at one segment. In slow start it grows exponentially (each acknowledgement adds a segment) until a threshold, then in congestion avoidance it grows linearly (one segment per round trip). A lost segment (timer expiry) is read as congestion: the threshold is cut to half the data in flight, the window restarts at one segment, and slow start runs again with a lower threshold (never below two segments). The receiver's window (flow control) also caps the sender.
- **Trade-off**: fairness and stability on the open internet versus throughput on lossy or high-latency paths.
- **Does not hold when**: a transport that does not use loss as the signal (for example receiver-driven schemes inside a datacenter).

## 13.6 Ephemeral port exhaustion
- **Thesis**: a connection is identified by four values (source address and port, destination address and port); when three are fixed, only the source port varies, and that range is finite.
- **Mechanism**: the kernel picks the source port from an ephemeral range of roughly 28,000 to 32,000 ports by default on Linux. A service that opens a new connection to the same backend for every request, and keeps it open (idle keep-alive pings, long timeouts), exhausts the range after a few tens of thousands of connections. New requests then block waiting for a port, requests time out, a proxy in front times out too, and the symptom looks like a slow server. Other services on the same host also fail to connect. Inbound clients are rarely the problem because they bring many different source addresses.
- **Trade-off**: reuse (pooling, multiplexing) removes the problem but needs a protocol that supports concurrent requests per connection.
- **Does not hold when**: connections go to many different destinations (each tuple is distinct), although some kernels treat the source port as unique across destinations.
- **Rule**: count connections per host while debugging, check for a pool that is not reused, widen the range only as a stopgap.

## 13.7 The listening socket: backlog and accept queues
- **Thesis**: listening is not accepting; the kernel holds half-open and completed connections in two bounded queues until the application takes them.
- **Mechanism**: a SYN goes to the first queue, the kernel replies, the final ACK moves the connection to the accept queue, and the application must call accept to get a file descriptor. If the application is slow, the accept queue fills and new connections are dropped or time out. A flood of SYNs that never complete fills the first queue (SYN flood). Binding without an address means "all interfaces": an internal admin or database port becomes public on a host with a public address, the usual cause of exposed datastores.
- **Trade-off**: convenience defaults versus explicit binding.
- **Does not hold when**: the host has only one interface in a private network. Still bind explicitly.

## 13.8 Five ways to manage connections across cores
- **Thesis**: single-threaded loops are simple and bottleneck on one core; adding threads brings shared state, locks and imbalance.
- **Mechanism**: (1) one thread accepts and works: any slow task delays accepts. (2) One acceptor hands each connection to a worker (a fixed pool, several connections per worker): connections are unequal, so some workers are busy and others idle. (3) The acceptor also reads, parses requests and dispatches *requests* (not connections) to workers: balanced, with a dispatcher that may become the bottleneck. (4) Several threads or processes listen on the same port with the address-reuse option; the kernel spreads accepts, as busy proxies do. (5) Keep the application single-threaded and stateless, run one copy per core (containers) and spread connections with a layer-4 rule: simplest code, needs state outside. Multithreading adds its own hazards: an unprotected increment lost between two threads, locks, and the cost of coordination.
- **Trade-off**: load balance versus coordination cost versus simplicity.
- **Does not hold when**: one core suffices, or work is I/O bound and an event loop handles it.

## 13.9 Streams versus messages: why a datacenter may not want TCP
- **Thesis (position, from a proposal for datacenters only)**: TCP's design assumes a byte stream on the open internet; datacenter services exchange small request-response messages over very fast links, and five properties of TCP hurt them.
- **Mechanism**: (1) stream orientation: the transport does not know where a message starts or ends, so each application invents framing, a read may return part of a message or several, and spreading a connection's reads over threads is awkward; load balancing across cores needs a dispatcher thread or static assignment that creates hot spots. (2) Connections: per-connection state (about two kilobytes of kernel state each, more with buffers) and a setup phase. (3) Fair sharing: round-robin among segments makes short messages wait behind long ones; preferring the message with the least remaining work gives better latency. (4) Sender-driven congestion control reacting to queue overflow takes a round trip to notice and fills switch buffers. (5) In-order delivery makes complete messages wait for earlier ones. The proposed alternative is message-based, connectionless, receiver-driven (the receiver grants permission to send the rest of long messages, with the first bytes sent unscheduled), uses priorities and sprays packets over paths; it is not API-compatible with TCP and is meant to appear under an RPC framework. The same authors would not use it for streaming web content or video.
- **Trade-off**: gains for short messages, loss of generality; a new transport is a rewrite for apps that call sockets directly. Hardware offload of the transport is limited by connection-state memory and hard to patch.
- **Does not hold when**: traffic crosses the open internet, is a continuous stream, or needs the ecosystem of middleboxes and tooling that TCP has.

## 13.10 Message boundaries and request smuggling
- **Thesis**: when a protocol offers several ways to mark the end of a message, two parsers can disagree.
- **Mechanism**: HTTP/1.1 marks a body's end by a length header or by chunked encoding. If a front proxy and a backend interpret a request with both differently, an attacker can hide a second request that the proxy never inspects and the backend executes (for example an admin call the proxy blocks). The root cause is the stream model with ambiguous framing; binary framing with explicit lengths removes most of it.
- **Trade-off**: strict parsers reject odd but legal traffic.
- **Does not hold when**: a single parser handles the whole path.
