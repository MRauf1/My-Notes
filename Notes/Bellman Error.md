---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Bellman Error
> For $f \in \mathbb{R}^{|\mathcal{S}\times\mathcal{A}|}$, the quantity $\|f - \mathcal{T}f\|_\infty$, measuring the violation of $f$ with respect to the [[Bellman Optimality Equation]], where $\mathcal{T}$ is the [[Bellman Optimality Operator]].

# Properties
- Controls the distance to $Q^\star$: $\|f - Q^\star\|_\infty \leq \|f - \mathcal{T}f\|_\infty / (1-\gamma)$.
- Used to check convergence of [[Value Iteration]] without knowing $Q^\star$, by monitoring $\|f_k - f_{k+1}\|_\infty = \|f_k - \mathcal{T}f_k\|_\infty$ across iterates $f_k = Q^{\star,k}$.
