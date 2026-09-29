---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Ziggurat Algorithm[^1]
> For a monotone decreasing density $f$ (e.g. one half of the normal or the exponential), cover $f$ with $n$ stacked horizontal layers of equal area — $n-1$ rectangles plus a base strip including the tail. To sample:
> 1. Choose a layer $i$ uniformly and draw $x$ uniformly within its width $[0, x_i]$.
> 2. If $x < x_{i+1}$ (the width of the layer above), $x$ lies entirely under $f$: accept immediately.
> 3. Otherwise perform a [[Rejection Sampling|rejection test]] of a uniform height against $f(x)$ in the overhanging wedge (or sample the tail separately for the base layer).

# Properties
- The fast path (step 2) needs only a table lookup, one uniform, and one comparison, and is taken with probability close to $1$ for $n \approx 128$–$256$ layers, making it much faster than the [[Box-Muller Transform]] for Gaussian variates.
- Exact: it is a [[Rejection Sampling|rejection sampler]] whose envelope hugs $f$ closely, so the rare slow paths do not bias the output.

[^1]: Monte Carlo Methods — Q&A Overview
