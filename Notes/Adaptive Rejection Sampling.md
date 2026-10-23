---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Adaptive Rejection Sampling[^1]
> For a log-concave target density $f$, the tangent lines to $\log f$ lie above $\log f$, so their lower envelope is a piecewise linear upper bound and $g \propto \exp(\text{envelope})$ is a piecewise exponential [[Rejection Sampling|rejection]] proposal. Adaptive rejection sampling refines this envelope while sampling: whenever a proposal $x \sim g$ is rejected, a new tangent line to $\log f$ at $x$ is added to the envelope.

Log-concavity is what makes the tangents valid upper bounds; Owen presents the method in that setting.

# Properties
- $\log g$ approaches $\log f$ very quickly, so the acceptance rate $1/c$ rises toward $1$ as sampling proceeds.
- Sped up with a [[Squeeze Function (Rejection Sampling)|squeeze]] $h$: take $\log h$ piecewise linear through the tangent points $(x_k, \log f(x_k))$ on $[x_1, x_k]$ and $\log h = -\infty$ outside; by concavity the chords lie below $\log f$, and the squeeze accepts more points as segments are added.
- In practice one can stop updating $g$ once the rejection rate falls below a threshold, or precompute a piecewise linear approximation of $\log f$ for a target acceptance probability.

[^1]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=33&annotation=WZ7NHHKI); [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=34&annotation=6AHW665U)
