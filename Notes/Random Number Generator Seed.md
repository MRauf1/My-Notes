---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Random Number Generator Seed[^1]
> A seed is a value passed to a function `setseed(seed)` that sets the internal state of a [[Pseudorandom Number Generator]], making its subsequent output repeatable. The seed may be a direct encoding of the full state, or simply an integer that `setseed` expands into a full state.

# Properties
- **Default seeding:** when no seed is set, some generators seed themselves from a hidden, unreproducible source such as the system clock; others use a prespecified default seed and give the same numbers on every run. The latter is better because it is reproducible; clock seeding damages the reproducibility of the code itself and of every application calling it.[^2]
- **Best practice:** always set a seed explicitly, even when the generator does not require it, so that interesting simulation results can be repeated (e.g. to track down a bug in the code consuming the random numbers).[^2]
- Together with `getseed()`, which reads off the current state, seeding can be used to manage separate [[Random Number Streams]].[^3]
- Related: [[Random Number Generator Period]].

[^1]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/GBISVAQW?page=5&annotation=4B6QEM97)
[^2]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/GBISVAQW?page=5&annotation=55XBBYAA)
[^3]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/GBISVAQW?page=6&annotation=W4HNZVSB)
