---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Multiple Importance Sampling (MIS)[^1]
> A single random walk augmented with [[Next-Event Estimation|next-event connections]] does not build one path — every vertex it reaches closes a path of its own, sharing a prefix (the walk traced once) and therefore correlated rather than independent. Each such path can be sampled two ways — connect at its last vertex, or let the walk continue and land on the source by chance — giving the same path two different densities.
>
> Given $K$ sampling strategies with densities $p_1, \dots, p_K$ over the same measure, $n_k$ samples from each, and weights $w_k$ with $\sum_k w_k(\bar{x}) = 1$ wherever $f \neq 0$:
> $$
> \begin{align}
> \langle I \rangle_{\mathrm{MIS}} = \sum_{k=1}^K \frac{1}{n_k}\sum_{j=1}^{n_k} w_k(\bar{x}_{k,j})\,\frac{f(\bar{x}_{k,j})}{p_k(\bar{x}_{k,j})}
> \end{align}
> $$

Unbiased for any such weights, since the weights partition each path's contribution rather than reweighting the integral. The workhorse choice is the balance heuristic, $w_k \propto n_k p_k$. Two preconditions matter: the strategies must share the same measure — not a formality — and each strategy's density $p_k$ must be evaluable at a sample some other strategy drew; delta tracking cannot do this, which is the cost of using it.

# Properties
- Combines [[Next-Event Estimation]] with continued random-walk sampling.
- Combines the full table of strategies in [[Bidirectional Path Tracing]].

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
