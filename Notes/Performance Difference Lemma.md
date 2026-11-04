---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!abstract] Performance Difference Lemma[^1]
> For a [[Markov Decision Process]], any policies $\pi, \pi'$, and any state $s \in \mathcal{S}$:
> $$
> \begin{align}
> V^{\pi'}(s) - V^\pi(s) = \frac{1}{1-\gamma}\,\mathbb{E}_{s' \sim d^{\pi',s}}\left[A^\pi(s', \pi')\right]
> \end{align}
> $$
> where $d^{\pi',s}$ is the normalized [[Discounted State Occupancy]] induced by $\pi'$ from starting state $s$, and $A^\pi$ is the [[Advantage Function]].

# Properties
- Immediately implies the [[Policy Improvement Theorem]]: in [[Policy Iteration]], the advantage terms are nonnegative, so $V^{\pi_k}(s) - V^{\pi_{k-1}}(s)$ decomposes into a sum of nonnegative terms.
- Generalized to an identity for arbitrary $f$ by the [[Performance Difference Bellman Error Decomposition]]. It drives the analyses of the [[Policy Gradient Stationary Point Suboptimality Bound]] and the [[Natural Policy Gradient Convergence Bound]].

# Questions
> [!question]- What is the proof idea of the performance difference lemma?
> Telescope through hybrid policies. $\pi_i$ follows $\pi'$ for the first $i$ steps, then $\pi$, so $\pi_0 = \pi$ and $\pi_\infty = \pi'$, and $V^{\pi'}(s) - V^\pi(s) = \sum_{i \geq 0}(V^{\pi_{i+1}}(s) - V^{\pi_i}(s))$. Consecutive hybrids share the roll-in up to $s_{i+1}$ and the roll-out after step $i+2$. They differ only in the action at $s_{i+1}$, contributing $\gamma^i\,\mathbb{E}[A^\pi(s_{i+1}, \pi')]$. Summing $\gamma^i\,\mathbb{P}[s_{i+1} = s' \mid s_1 = s, \pi']$ over $i$ gives $\frac{1}{1-\gamma} d^{\pi', s}(s')$.

> [!question]- Why is the expectation taken over $d^{\pi',s}$ (the new policy's occupancy) and not $d^{\pi,s}$?
> In the telescoping argument, the states where the two policies' actions are compared are reached by rolling in with $\pi'$. The advantage is that of the old policy $\pi$, because $\pi$ is followed afterwards. Swapping the roles gives a different identity: $V^\pi(s) - V^{\pi'}(s) = \frac{1}{1-\gamma}\mathbb{E}_{s' \sim d^{\pi,s}}[A^{\pi'}(s', \pi)]$.

[^1]: [Jiang, MDP Preliminaries (CS 542 notes), p. 6](https://nanjiang.cs.illinois.edu/files/cs542f22/note1.pdf#page=6)
