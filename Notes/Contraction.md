---
tags:
  - mathematics
  - real_analysis
---

# Definition
> [!info] Contraction
> On a [[Metric Space]] $(X, d)$, a map $T: X \to X$ is a $\gamma$-contraction, for $\gamma \in [0, 1)$, if
> $$
> \begin{align}
> d(Tx, Tx') \leq \gamma\, d(x, x'), \quad \forall x, x' \in X
> \end{align}
> $$

# Properties
- A contraction on a [[Complete Metric Space]] has a unique fixed point, to which iterating $T$ from any starting point converges.
- The [[Bellman Optimality Operator]] is a $\gamma$-contraction under the [[Infinity Norm|infinity norm]], which underlies the convergence of [[Value Iteration]].
