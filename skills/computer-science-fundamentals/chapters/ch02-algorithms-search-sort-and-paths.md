# Chapter 2: Algorithms for Searching, Sorting, Paths and Decisions

## Core Idea
An algorithm is a procedure plus an argument that it works and a statement of what it costs. In this model each classic algorithm teaches one reusable move (halve the space, recurse on smaller pieces, expand the cheapest frontier first, add a guess about the remaining distance, sample instead of enumerate) and each has a precondition that decides whether the move is right.

## 2.1 Binary search
- **Thesis**: on sorted data you can discard half of the remaining candidates with each comparison, so lookup costs logarithmic time instead of linear.
- **Mechanism**: keep a left and a right boundary around the region still possible; compare the target with the middle element; move the left boundary just above the middle or the right boundary just below it; stop when the element is found or the boundaries cross. With ten million items the worst case is about 23 comparisons, against ten million for a linear scan (figures as stated). Doubling the data adds one step.
- **Trade-off**: the data must be sorted and randomly addressable. If you sort once and look up many times, the sorting cost is repaid; if you look up once, a linear scan is cheaper than sorting first.
- **Does not hold when**: the data is unsorted, changes constantly, or is stored in a structure without positional access (a linked list); a hash set gives constant-time membership with no order. A built-in "is x in list" on an unsorted list is a hidden linear search, which is a common cause of slow code. Implementation traps: index arithmetic and off-by-one at the boundaries (the midpoint is rounded down).

## 2.2 Quicksort and recursion
- **Thesis**: sorting reduces to partitioning around a pivot and sorting the two sides the same way; recursion needs a base case that stops it.
- **Mechanism**: choose a pivot (the middle element, or simply the first); send everything smaller to one list and everything larger to another; sort each list recursively; join smaller + pivot + larger. The recursion ends when a list is empty, because every call receives strictly fewer elements (the pivot is removed). In a language with list filters the whole algorithm is five lines: the empty list is returned unchanged; otherwise combine the sorted smaller part, the pivot, and the sorted larger part.
- **Trade-off**: the short version builds new lists (a clarity-first form); in-place versions are faster in memory use. Pivot choice decides the balance of the two sides: general knowledge, a consistently bad pivot degrades it towards quadratic time, an average pivot gives n log n.
- **Does not hold when**: the data is nearly sorted and the pivot is naive, or memory is tight (then use an in-place or a different sort).

## 2.3 Recursion, the call stack and the base case
- **Thesis**: a function that calls itself needs a terminating condition, because each call occupies stack memory.
- **Mechanism**: each call pushes a frame on the short-term call stack; without a base case frames pile up until a stack overflow error. The stack is limited and short-lived; long-lived data lives on the heap (ch6).
- **Trade-off**: recursion is natural for trees and divide-and-conquer; deep recursion on large inputs needs an iterative form or tail-call support.
- **Does not hold when**: the language guarantees tail-call elimination for the pattern used.

## 2.4 Shortest paths: Dijkstra's algorithm
- **Thesis**: the cheapest way to a node is found by always expanding the cheapest unfinished node next, which guarantees the first time the destination is taken from the queue its distance is final (for non-negative costs, general knowledge).
- **Mechanism**: give the start distance 0 and everything else infinity ("not seen yet"). Keep a priority queue ordered by current distance. Repeatedly take the node with the smallest distance, mark it finished, and for each neighbour compute distance-via-this-node; if smaller than the stored value, replace it and record this node as the neighbour's predecessor. Finished nodes are never revisited. Follow predecessors back from the destination to get the route. Edge weights model difficulty (a motorway is a low number); a detour that looks longer can be cheaper in total. Uses: navigation, network routing.
- **Trade-off**: it explores in all directions in order of cost, like a flood fill, which wastes effort when the destination is in a known direction or the graph is dense or uniform.
- **Does not hold when**: edge costs can be negative (use another algorithm), or the graph is so large that exhaustive expansion is unaffordable.

## 2.5 A*: add a guess about the distance left
- **Thesis**: if you can estimate the remaining distance, order the queue by cost-so-far plus estimated remaining cost, and the search aims at the goal.
- **Mechanism**: the algorithm is Dijkstra with a second number per node. The cost so far (call it g) is what is stored and compared when deciding whether a route to a node improved; the queue is ordered by g plus the heuristic h. A straight-line distance is a natural h on a map. Nodes that are far from the goal sink in the queue and are expanded later. On a uniform grid, where plain Dijkstra floods outward, A* goes more directly.
- **Trade-off**: speed depends on the quality of h. To keep the result optimal the estimate must never overestimate the remaining cost and should be consistent (an overestimate or an inconsistent estimate loses the guarantee); an inaccurate estimate gives a path that may not be shortest or loses the speed gain. The extra bookkeeping is two values per node.
- **Does not hold when**: no sensible estimate exists (then it degenerates into Dijkstra), or the graph is small enough that none of this matters.

## 2.6 Algorithm families
- **Thesis**: most algorithms are an instance of a few strategies; naming the strategy tells you what to check.
- **Mechanism**: brute force (try everything; correct, rarely scalable); divide and conquer (binary search, quicksort); dynamic programming (break into overlapping sub-problems and store each answer, memoisation, so a call already computed is reused); greedy (take the best local choice; Dijkstra is the example given; safe only when the problem has the right structure); backtracking (explore options incrementally and undo, like a maze).
- **Trade-off**: greedy and heuristic methods are fast and can be wrong; dynamic programming trades memory for time.
- **Does not hold when**: sub-problems do not overlap (memoisation then only costs memory) or the local best is globally bad (greedy fails).

## 2.7 Decision-making when the model is unknown: Monte Carlo tree search
- **Thesis**: when you cannot list all states and probabilities, and you cannot think for as long as you like, you can still decide by sampling simulated futures and growing a search tree, one node per trial, and the answer improves the longer you run it.
- **Mechanism**: a Markov decision process has states, actions, uncertain outcomes and costs; value iteration solves it exactly but needs the full model (all probabilities) and enumerates all states, with memory and time that grow quickly. The sampling alternative needs only a simulator: give it a state and an action and it returns one next state, like rolling a die without the probabilities printed on it. Each trial has four steps: selection (walk down the existing tree choosing actions), expansion (add one new node), simulation (a roll-out to the end with a cheap, often random policy, to initialise how good the new node is), and backup (send the result up the path and update averages and visit counts). Plan briefly, act, then plan again from the new state (interleaving planning and acting). Selection uses an upper-confidence rule: value of an action, minus (for a cost) an exploration bonus that grows with the log of the parent's visits and shrinks with the action's own visits; unvisited actions get an infinite bonus, so each action is tried once first. This is the bandit idea (several slot machines, unknown payouts) applied at every node.
- **Trade-off**: exploration versus exploitation: spend too long on promising options and you never learn about better ones; spend too long exploring and you waste time. The method is an anytime algorithm: stopping early gives a usable answer and more time does not make it worse. In infinite time the estimates are right; in finite time they can be badly biased by a few unlucky samples early on.
- **Does not hold when**: probabilities of rare catastrophic outcomes matter (a very unlikely puncture is hard to sample, and all probabilities are only approximations of reality), or the model is small and known (then solve it exactly).

## 2.8 A gallery of unusual algorithms, with the idea each one teaches
- **Thesis**: several well-known specialised algorithms are worth knowing as moves, not as code.
- **Mechanism**:
  - Simulated annealing: start with a high "temperature" so that worse solutions are often accepted (explore), lower it gradually so that only improvements survive (exploit); avoids getting stuck on a local peak that pure hill-climbing would reach.
  - Constraint-driven procedural generation (collapse of a superposition of possible tiles): start with every tile possible everywhere, repeatedly pick a cell, choose one tile consistent with the rules (for example, roads must connect), propagate constraints to neighbours; result is random but locally coherent.
  - Diffusion models: add noise step by step until the image is random, then learn to reverse the steps; see `ai-ml-concepts`.
  - Marching cubes: treat the eight corners of a cube in a scalar field as bits (is the value above the threshold?), giving 256 cases that index a pre-computed table of polygons; march through the volume to build a surface mesh (used to render scans).
  - Fault-tolerant agreement among distrustful machines (Byzantine fault tolerance): a leader announces a proposal, the others reply with agreement, after a threshold they commit; tolerates up to about one third of nodes being faulty or malicious. Basis of some consensus protocols; see `software-architecture` ch02.
  - Flocking: three local rules per bird (avoid crowding, match the heading of neighbours, move towards the centre of nearby flock-mates) produce complex group patterns with no global program: emergence.
  - Right-to-left string search with skip tables: compare the end of the pattern first; on a mismatch use two precomputed tables (bad character, partial match) to skip many positions; counter-intuitively gets faster as the pattern grows, which is why command-line text search is fast.
  - Joke algorithms: sleeping for a time proportional to each value and printing on waking "sorts" by delegating the work to the scheduler, and random shuffling until sorted: both are teaching jokes, useless in practice.
  - Quantum factoring: a polynomial-time algorithm is known on paper, but current machines are far too small; any quoted records change quickly (unverified; do not rely on figures).
- **Trade-off**: specialised algorithms win on their niche and are misapplied elsewhere.
- **Does not hold when**: the problem does not match the algorithm's precondition (for example annealing on a problem with a smooth single peak is wasted effort).

See also: ch3 (the structures these algorithms run on), ch7 (routing uses shortest paths), `ai-ml-concepts` ch04 (optimisation as learning).
