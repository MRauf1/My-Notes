---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Policy Iteration Exponential Convergence
> [[Policy Iteration]] converges exponentially fast in the [[Infinity Norm|infinity norm]]:
> $$
> \begin{align}
> \|Q^\star - Q^{\pi_{k+1}}\|_\infty \leq \gamma \|Q^\star - Q^{\pi_k}\|_\infty
> \end{align}
> $$

# Properties
- Holds despite the worst-case number of iterations for exact convergence being upper bounded only by the (generally exponential) $|\mathcal{A}|^{|\mathcal{S}|}$; for an approximate solution, [[Policy Iteration]] converges exponentially fast.
