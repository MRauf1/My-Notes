---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Performance Difference Lemma
> For a [[Markov Decision Process]], any policies $\pi, \pi'$, and any state $s \in \mathcal{S}$:
> $$
> \begin{align}
> V^{\pi'}(s) - V^\pi(s) = \frac{1}{1-\gamma}\,\mathbb{E}_{s' \sim d^{\pi',s}}\left[A^\pi(s', \pi')\right]
> \end{align}
> $$
> where $d^{\pi',s}$ is the normalized [[Discounted State Occupancy]] induced by $\pi'$ from starting state $s$, and $A^\pi$ is the [[Advantage Function]].

# Properties
- Immediately implies the [[Policy Improvement Theorem]]: in [[Policy Iteration]], the advantage terms are nonnegative, so $V^{\pi_k}(s) - V^{\pi_{k-1}}(s)$ decomposes into a sum of nonnegative terms.
