---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Physical Random Number Generator[^1]
> A physical (true, hardware) random number generator produces genuinely random numbers by measuring a physical random process, rather than by a deterministic recursion as in a [[Pseudorandom Number Generator]].

# Properties
Drawbacks for [[Monte Carlo Method|Monte Carlo]] simulation:[^1]
- **Not replayable:** the physical source cannot be restarted, so rerunning a simulation (after a parameter change or bug fix) requires storing the entire sequence.
- **Storage:** truly random sequences are incompressible, so storing them takes a lot of space.
- **Speed:** they usually cannot supply numbers nearly as fast as pseudorandom numbers can be generated.
- **May fail randomness tests:** this need not cast doubt on the physics or on the tests; the usual interpretation is that the hardware recording and processing the random source introduces flaws.

[^1]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/GBISVAQW?page=3&annotation=YJVFYI8J); [Owen](zotero://open-pdf/library/items/GBISVAQW?page=4&annotation=T4BNIG3N); [Owen](zotero://open-pdf/library/items/GBISVAQW?page=4&annotation=BR52ELD7)
