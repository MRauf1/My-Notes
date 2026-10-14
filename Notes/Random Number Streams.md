---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Random Number Streams[^1]
> Multiple streams of random numbers are two or more sequences $(x^{(1)}_i)_{i \geq 1}, (x^{(2)}_i)_{i \geq 1}, \dots$ such that each stream behaves like a sequence of [[Independent and Identically Distributed|i.i.d.]] $U(0,1)$ random variables, and the streams appear [[Mutually Independent Random Variables|statistically independent]] of each other.

Moderately complicated simulations need two or more streams (e.g. one per source of randomness, or one per parallel worker).[^1]

# Types
- **Manual seed management:** obtain separate streams from a single [[Pseudorandom Number Generator]] by carefully saving and restoring its state with `getseed()` and `setseed()` ([[Random Number Generator Seed]]).[^2]
- **Built-in multiple streams (preferred):** use a generator that natively supplies multiple streams and takes care of their seeds.[^3] Modern examples include jump-ahead/substream generators and counter-based generators (e.g. Philox), where each stream is indexed by a key.

[^1]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/GBISVAQW?page=6&annotation=FH5XCNLB)
[^2]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/GBISVAQW?page=6&annotation=W4HNZVSB)
[^3]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/GBISVAQW?page=7&annotation=CAV4BTZI)
