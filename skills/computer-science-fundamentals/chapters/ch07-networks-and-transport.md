# Chapter 7: Networks, Transport and Naming

## Core Idea
A network moves bits between machines that share nothing but conventions. In this model the conventions are stacked (a physical signal, a local link, global addressing, reliable delivery, and names that humans can use), and each layer solves one problem the layer below leaves open: how to keep clocks aligned, how to find the other machine, how to be reliable over an unreliable path without flooding it, and how to avoid hard-coding addresses.

## 7.1 The layered model
- **Thesis**: split the problem into layers so each one can change without the others.
- **Mechanism**: an idealised seven-layer model: physical (cables carrying light or voltage), data link (connecting two adjacent nodes, for example with Ethernet or Wi-Fi), network (the internet protocol: every machine has an address; data travels as packets with the address in the header; routers and gateways forward them), transport (the transmission control protocol takes a stream, segments it, orders and acknowledges it), session (managing a connection between two machines, including authentication), presentation (translating data to a standard encoding), application (the web protocol, mail, file transfer). Real protocol suites do not map one-to-one to the seven layers (general knowledge): the practical stack has fewer layers and security (encryption) sits between transport and application.
- **Trade-off**: layering simplifies reasoning and creates overhead (headers, copies); a problem often lives in a layer you did not suspect.
- **Does not hold when**: you optimise across layers deliberately (for example moving reliability into the application).

## 7.2 Serial transmission and the clock problem
- **Thesis**: sending ones and zeros down one wire requires both sides to agree when each bit starts, and a long run of identical bits makes the receiver lose count.
- **Mechanism**: both ends agree a bit rate (the baud rate in old serial links). A start bit (always one) marks the beginning of a byte; the data bits follow; a stop bit ends the frame. A setting such as 8N1 means eight data bits, no parity, one stop bit. Clocks that run slightly differently stay in step only over a few bits, which is why the start and stop framing exists.
- **Trade-off**: framing costs bits; faster links need cleverer encodings.
- **Does not hold when**: the two ends share a clock wire.

## 7.3 Line coding: Manchester, 8b/10b, scrambled blocks
- **Thesis**: the signal on the wire must carry its own clock and have no net electrical bias, so data bits are re-encoded; later generations spend fewer extra bits to do it.
- **Mechanism**: Manchester encoding sends each bit as two phases (a one as low-then-high, a zero as high-then-low), so there is a transition in every bit and the receiver can lock to the beat; the cost is 100 per cent overhead, and it was used at the first speeds of Ethernet (one and ten megabits per second). Gigabit Ethernet, in the version described here (general knowledge: some copper variants use a different scheme), maps each byte into a ten-bit symbol (8b/10b): out of 1,024 possible patterns choose 256 (often with two alternatives per byte) that never contain too many zeros in a row and are balanced between ones and zeros ("DC balance", which lets the receiver's amplifier centre its threshold); keep a running count and pick the alternative that restores balance. Leftover valid patterns signal start of packet, end of packet and idle fill, so the line is always active; the link light on a port means both sides have locked onto this pattern. Overhead: two extra bits in every ten on the line (20 per cent of the line rate, 25 per cent on top of the payload). At 10 gigabit the scheme sends 64 data bits plus two header bits and scrambling the data with a shift-register that mixes in a pseudo-random sequence, so the data looks random, which is balanced and has few long runs, with probability rather than a lookup table; the receiver descrambles with the same circuit and synchronises after enough bits. The overhead is then about three per cent (2 bits in 66; 64b/66b).
- **Trade-off**: table-based codes guarantee the properties but their size explodes with block length; scrambling gives only probabilistic guarantees, with a header pair to guarantee a transition.
- **Does not hold when**: the medium is wireless, where modulation schemes replace these ideas.

## 7.4 Reliable delivery: sequence numbers, acknowledgements, windows
- **Thesis**: sending one packet and waiting for an acknowledgement is far too slow, so send a flight of packets and acknowledge cumulatively.
- **Mechanism**: each segment carries a sequence number; the receiver returns an acknowledgement number saying everything up to here has arrived (a cumulative acknowledgement). Packets in flight are those sent but not yet acknowledged. A packet is about 1,500 bytes. Two windows limit the flight: the receiver's window (how much the receiver can buffer, put in the header) and the sender's congestion window (how much the sender believes the network can carry). Loss signals: three duplicate acknowledgements of the same number (a packet is missing but later ones arrive) or a timeout (nothing returns, suggesting heavy congestion). The retransmission timeout is a multiple of the measured round-trip time, so the same algorithm works in a data centre, across a continent or over a satellite. Rules in the standards are marked as must, should or may; flavours of the protocol differ in the optional behaviour.
- **Trade-off**: acknowledgements carry little information (header space is scarce), so the sender infers the network's state indirectly.
- **Does not hold when**: loss is not a congestion signal (wireless links lose packets to noise, which the loss-based rule misreads as congestion, general knowledge) or when delay is used as the signal (some flavours do).

## 7.5 Congestion control: slow start and additive increase, multiplicative decrease
- **Thesis**: the sender probes for capacity by growing the window until something is lost, then cuts it sharply; the result is a sawtooth that shares the link roughly fairly.
- **Mechanism**: slow start: begin with a small window (typically about 10 segments in modern defaults; classic textbooks start at 1), double it each round (10, 20, 40, ...) until the first loss or until the slow-start threshold (ssthresh) is reached; it is called slow because it starts small, not because the growth is slow. Then additive increase, multiplicative decrease (AIMD): after each fully acknowledged round add one packet; on a loss event cut the window by half (on a timeout, restart more drastically). The most common variant today is a smoother curve called Cubic (stated as the flavour of the moment; check). Some variants watch the round-trip time rising and back off before loss.
- **Trade-off**: aggressiveness versus stability and fairness; short transfers never leave slow start, so most of their time is spent ramping up. The real traffic in a packet trace is messier than the textbook picture (security records, timers, parallel connections).
- **Does not hold when**: a path is controlled end-to-end by one party who can schedule traffic centrally.

## 7.6 Names: how DNS resolves a host name
- **Thesis**: humans use names, machines use addresses; a globally distributed, hierarchical, cached database maps one to the other.
- **Mechanism**: the browser or operating system checks its local cache first. If empty, a recursive resolver asks the root name servers, which point to the servers of the top-level domain (the part after the last dot), which point to the authoritative name server for the domain; that server holds the answer and is the source of truth. The answer returns down the chain and is cached for later. Record types in a domain's zone: SOA (who is in charge), A (name to address), CNAME (this name is an alias of another name), MX (mail), TXT (arbitrary text, often to prove ownership to third parties), NS (the name servers, normally at least two for reliability). A registrar sells the name, a registry operator keeps the data and propagates it.
- **Trade-off**: caching makes the system fast and makes changes propagate slowly (the time-to-live); one authoritative failure makes a domain unreachable.
- **Does not hold when**: you connect by address directly (internal addresses, test setups).

## 7.7 Routing as shortest path
- **Thesis**: choosing the route for packets is a shortest-path problem on a graph of routers and links.
- **Mechanism**: routing protocols apply shortest-path algorithms (ch2) to a graph whose edge weights represent cost; prefix-based tables (radix trees, ch3) make lookups efficient.
- **Trade-off**: cost metrics encode policy as well as distance.
- **Does not hold when**: the networks belong to different organisations that negotiate paths by policy rather than cost.

## 7.8 Addresses, ports and the path of a web request
- **Thesis**: a web page load is a stack of small, separate agreements: an address, a port, a reliable stream, a request, and a way to remember who you are.
- **Mechanism**: data travels as packets that routers forward independently and the receiver reassembles. A 32-bit address allows 2^32 (about 4.3 billion) hosts, too few, so many devices share one public address behind address translation, and a 128-bit scheme was designed to replace it. Transport chooses reliability or speed: TCP numbers, acknowledges and resends (reliable, slower to start), UDP sends without guarantees (fast, used where late data is useless). A port number names the service on the host (web traffic conventionally uses two ports, plain and encrypted). Over the stream, HTTP sends a request (GET asks for a resource, POST sends data) and receives a status code (200 success, 403 forbidden, 404 not found, 500 server error; ch10.1). HTTP keeps no memory between requests, so a cookie carries an identifier that the server maps to state (ch9.7). A domain is resolved to an address by DNS (7.6), and the service typically sits behind a rate limit that answers too many requests with an error.
- **Trade-off**: each layer hides detail and enables reuse; each hides a failure mode that you only meet by descending a layer.
- **Does not hold when**: a modern transport merges layers (encrypted transport over datagrams), so the textbook layer boundaries blur.


See also: `software-architecture` ch13 (TCP, TLS, HTTP versions, port exhaustion in services), ch16 (proxies, timeouts, balancers), ch10 of this skill (application protocols), ch9 (encryption on the wire).
