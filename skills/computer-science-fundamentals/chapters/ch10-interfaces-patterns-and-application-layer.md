# Chapter 10: Interfaces, Design Patterns and Programming Paradigms

## Core Idea
Above the machine, software is organised by conventions for how pieces talk (APIs) and how code is shaped (paradigms and patterns). In this model a convention earns its place only if it removes a recurring problem more cheaply than it adds ceremony; every pattern in this chapter has a language in which it is unnecessary.

## 10.1 APIs and REST
- **Thesis**: an application programming interface lets one program request data from another with code instead of clicks; the dominant style organises data as resources on addresses.
- **Mechanism**: a resource has a URI. A client sends a request over HTTP: a start line with a method and the URI, headers with metadata (for example the format the client accepts, or credentials), and optionally a body. Methods express intent: GET reads, POST creates, PATCH updates, DELETE removes. The server runs some code (usually reading a database) and returns a response: a status code (the 200 range means success, 400 range means the request was wrong, 500 range means the server failed), headers, and a body, usually JSON. The architecture is stateless: each exchange is independent, the two parties store nothing about each other between requests, which makes behaviour predictable and scaling easy. A web framework maps methods and addresses to handler functions; middleware are functions that sit between request and handler; an API gateway in front adds routing, authentication and limits.
- **Trade-off**: one URI per resource can force many requests (under-fetching) or oversized responses (over-fetching).
- **Does not hold when**: the interaction is a stream or a conversation (then use a persistent connection), or the operations are not resource-shaped.

## 10.2 GraphQL
- **Thesis**: let the client describe exactly the data it wants through one entry point, backed by a typed schema.
- **Mechanism**: the server declares types with fields (a required field is marked), relationships (a creator has a list of videos; a video belongs to a creator), a query type as entry point and a mutation type for changes; resolver code, in any language, fetches the data. The client writes a query whose shape mirrors the JSON returned. Because the schema is explorable, tools can autocomplete queries.
- **Trade-off**: removes under- and over-fetching; shifts work to the server (a client can ask for expensive nested data, general knowledge) and complicates HTTP-level caching (general knowledge). See `software-architecture` for gateways and API design in systems.
- **Does not hold when**: the API is small and the same few shapes are always requested.

## 10.3 Design patterns: what they are and when they hurt
- **Thesis**: a design pattern is a named solution to a recurring structure problem; knowing the names lets you recognise and discuss them, and using one wrongly adds boilerplate.
- **Mechanism**: a well-known catalogue lists 23 patterns in three groups: creational (how objects are created), structural (how objects relate) and behavioural (how objects communicate). A pattern is not copy-paste code: it needs judgment. The book is influential and criticised (position).
- **Trade-off**: shared vocabulary against over-engineering.
- **Does not hold when**: the language already provides the feature.

## 10.4 Ten patterns, each with its own exit
- **Singleton**: exactly one instance of a type, created through a static accessor with a private constructor. A module-level global object or a module system gives the same effect in many languages, making the pattern boilerplate there; in languages without such features it can matter.
- **Prototype**: create new objects by cloning an existing object instead of instantiating a class; behaviour lookups follow a prototype chain, giving a flat alternative to deep class hierarchies. Extending built-in prototypes is considered bad practice.
- **Builder**: construct an object step by step through methods that each return the object (method chaining), deferring or delegating parts of construction; useful when the constructor has too many options; fell out of style where options objects or named parameters exist.
- **Factory**: a function or method decides which concrete type to create, so conditional logic (for example one button type per platform) lives in one place.
- **Facade**: a simplified interface in front of several complicated subsystems (turn the plumbing and electrics on or off with one call); most packages are facades of some kind; risk: hides capabilities and can leak when you need the details.
- **Proxy**: a stand-in object that intercepts reads and writes of a target; used for reactive user interfaces (a data change triggers a re-render), lazy loading and avoiding duplication of large objects.
- **Iterator**: a standard way to walk a collection by repeatedly asking for the next value until done; pull-based; the for-each loop is the common form; a custom iterator can express a range with a step.
- **Observer**: many subscribers register interest in events from one subject; push-based, one-to-many; the basis of event streams and live data updates.
- **Mediator**: a hub that coordinates objects so they need not know each other (an air-traffic controller between planes and runways); request-handling middleware is a practical example; risk: the mediator becomes a god object.
- **State**: replace conditional logic on an internal state with one object per state that implements the same methods; the object delegates to the current state and changes behaviour as the state changes without changing its interface; related to finite-state machines.
- **Trade-off (common)**: each adds indirection; benefits show when the variation is real.
- **Does not hold when (common)**: there is only one variant, or a plain function or data structure is enough.

## 10.5 Paradigms
- **Thesis**: the same problem can be expressed declaratively (what the result is) or imperatively (how to produce it); most general-purpose languages mix styles.
- **Mechanism**: declarative and functional style describes outcomes and avoids explicit control flow; imperative style uses statements such as conditionals and loops, and sequences of state changes; object-oriented style bundles data (properties) and behaviour (methods) into classes that are instantiated into objects, with inheritance letting a subclass extend and override a parent. Code is built from expressions (producing values) and statements (doing things); functions take arguments and may return nothing (void); dynamic programming and memoisation are algorithmic styles, not paradigms (see ch2).
- **Trade-off**: a style that fits the problem reduces code; inheritance couples subclasses to parents.
- **Does not hold when**: a team's conventions or the language's idioms decide otherwise.

See also: `software-architecture` ch17 and ch18 (domain modelling, coupling, hexagonal designs), `software-engineering-practice`, `coding-with-agents`.
