# Chapter 01: Continuous Delivery Foundations

## Core Idea
In this model, continuous delivery is a way of working in which the software is **always in a releasable state**, and software development is treated as an exercise in learning and in managing complexity. Everything else (pipeline, automation, small steps, tests) is machinery for getting fast, trustworthy feedback on whether the latest change is safe to release.

## 1.1 Releasable at all times
- **Thesis**: the defining property is not "we deploy often" but "any commit could be released, and we know within hours or less whether it can".
- **Mechanism**: analysis, design, coding, testing and deployment are done continuously and together, not as separate stages. A wrong analysis or a bad design is discovered in hours or days instead of months. Work is finished when it is in a releasable state, not when an interim measure (lines of code, partial definitions of done, feature counts) says so.
- **Trade-off**: requires technical discipline (automation, small changes, shared mainline) and organisational support (autonomous teams, culture), not only tools.
- **Does not hold when**: the artefact cannot be produced or verified repeatedly (some hardware or regulated releases); then aim for "as close to releasable as the domain permits" and automate the rest.

## 1.2 Two foundations: learning and complexity
- **Thesis (position)**: software development is mostly a learning and discovery activity, so it needs fast feedback; scaling it needs managed complexity.
- **Mechanism**: plans always miss things that cannot be known in advance. Start by assuming you may be wrong (about the product idea and about the solution), work in small experiments, control the variables (automate, version-control nearly everything), measure, and learn. Software has high cost of creation and near-zero cost of reproduction, so the hard problem is design, not production.
- **Trade-off**: experiments sometimes fail; the process has to make failure cheap and visible.
- **Does not hold when**: the problem is genuinely well understood and low risk; even then the feedback loops still cost little.

## 1.3 Cycle time as the driver
- **Thesis**: measure the time from idea to working software in users' hands (cycle time or lead time) and reduce it relentlessly; it exposes every bottleneck.
- **Mechanism**: a short cycle forces small teams, little coordination, automation of testing, configuration and deployment, and waste removal. Two contrasting cases: an order-management system where the smallest change took 103 days to reach production (effectively no feedback), and a far more complex low-latency exchange system where any change produced a verdict on releasability in about 57 minutes (stated as roughly 56 to 57 minutes in different places). The aim is releasability within a day, ideally within an hour.
- **Trade-off**: the cycle is only as short as its slowest manual step; shortening it requires investment first.
- **Does not hold when**: you optimise the metric instead of the outcome (see ch08).

## 1.4 The deployment pipeline
- **Thesis**: a deployment pipeline is a machine that takes every commit in at one end and produces a releasable artefact (or a rejection) at the other.
- **Mechanism**: each commit creates a **release candidate**. The pipeline's job is to **falsify** it: tests can never prove software good, but one deterministic failing test proves it is not good enough, so the candidate is discarded and the team commits a fix or a revert. If nothing rejects the candidate by the end of the pipeline, there is no more work to do before release. A pipeline that only runs developer tests, or only deploys, is not a pipeline in this sense.
- **Trade-off**: tests must be reliable (ch04); flaky or intermittent tests destroy the signal.
- **Does not hold when**: the pipeline is used as a rubber stamp to satisfy process.

## 1.5 Stages and their tests
- **Thesis**: different stages answer different questions with different test types.
- **Mechanism**:
  - **Commit stage**: developer-centred tests, fast and narrowly focused; target feedback under about five minutes and about 80% of mistakes caught. Tests cannot start the whole application, touch disk, network or other processes. It is the natural output of test-driven development (ch03).
  - **Acceptance stage**: user-centred tests of the whole system in a production-like environment whose deployment and configuration are automated; includes anything else that decides releasability (performance, security, scalability, resilience). Tests are written from an external user's point of view.
  - **Production stage**: get the tested candidate to users with techniques such as blue-green deployment, canary release and observability.
  - **Manual testing**: exploratory only (is it sensible, pleasant?). Manual regression testing is rejected in this model because humans are not repeatable enough.
- **Trade-off**: the 5-minute / 80% targets are stated rules of thumb for a first stage; large systems find them hard but reportedly feasible. Treat them as targets, not laws.
- **Does not hold when**: the system cannot be started in a test environment; then simulate boundaries and test in accurate clones.

## 1.6 Continuous delivery vs continuous deployment
- **Thesis**: delivery means always releasable; deployment means every passing change is pushed to production automatically.
- **Mechanism**: delivery keeps release timing a business decision (sometimes many times a second, sometimes not). Deployment makes sense in some industries and not in others.
- **Trade-off**: deploying every commit needs strong automated verification and observability; not deploying every commit leaves a gap between "ready" and "live".
- **Does not hold when**: regulation or context forbids unattended releases; stay at delivery.

## 1.7 Seven techniques (as a checklist)
Reduce cycle time; automate nearly everything; control the variables; work in small steps; make evidence-based decisions; work in small empowered teams; apply lean and agile principles. Everything stays in version control: code, tests, dependencies, configuration, infrastructure and deployment definitions ("all change to production flows through version control").

## 1.8 Myths
- It is not mainly about tools or automation; tools help, mindset and discipline decide.
- It is not "deploy every commit"; it is "always releasable".
- It is not only for large technology companies; it suits start-ups in discovery mode, and has been used for safety-critical and large-scale systems (position: stated examples are unverified in the source).
- Claims that adopters earn more and retain staff better rest on survey research; treat the strength of the evidence as correlational (see ch08).

## Cross-references
For delivery reliability, rollback and overload design see `software-architecture`. Chapter 02 covers the integration practice delivery depends on; chapter 04 the test reliability it requires.
