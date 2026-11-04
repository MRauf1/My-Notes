---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!abstract] Policy Iteration Exponential Convergence[^1]
> [[Policy Iteration]] converges exponentially fast in the [[Infinity Norm|infinity norm]]:
> $$
> \begin{align}
> \|Q^\star - Q^{\pi_{k+1}}\|_\infty \leq \gamma \|Q^\star - Q^{\pi_k}\|_\infty
> \end{align}
> $$

# Properties
- Holds despite the worst-case number of iterations for exact convergence being upper bounded only by the (generally exponential) $|\mathcal{A}|^{|\mathcal{S}|}$; for an approximate solution, [[Policy Iteration]] converges exponentially fast.
- Proof idea: (a) $\mathcal{T}^{\pi_{k+1}}Q^{\pi_k} \geq \mathcal{T}^{\pi}Q^{\pi_k}$ for all $\pi$ (greediness), and (b) $\mathcal{T}^{\pi_{k+1}}Q^{\pi_k} \leq Q^{\pi_{k+1}}$ ([[Policy Improvement Theorem]]). Then $0 \leq Q^\star - Q^{\pi_{k+1}} \leq \mathcal{T}^{\pi^\star}Q^\star - \mathcal{T}^{\pi^\star}Q^{\pi_k}$, and the $\gamma$-contraction of the [[Bellman Evaluation Operator]] $\mathcal{T}^{\pi^\star}$ finishes.

# Questions
> [!question]- In the proof, why is it important that $Q^\star - Q^{\pi_{k+1}} \geq 0$ elementwise?
> The argument only gives an elementwise *upper* bound $Q^\star - Q^{\pi_{k+1}} \leq \mathcal{T}^{\pi^\star}Q^\star - \mathcal{T}^{\pi^\star}Q^{\pi_k}$. Passing to $\|\cdot\|_\infty$ requires the left side to be nonnegative: for $0 \leq x \leq y$, $\|x\|_\infty \leq \|y\|_\infty$. That holds because $Q^\star \geq Q^\pi$ for every $\pi$. Then the $\gamma$-contraction of $\mathcal{T}^{\pi^\star}$ gives $\|Q^\star - Q^{\pi_{k+1}}\|_\infty \leq \gamma\|Q^\star - Q^{\pi_k}\|_\infty$.

[^1]: [Jiang, MDP Preliminaries (CS 542 notes), p. 7](https://nanjiang.cs.illinois.edu/files/cs542f22/note1.pdf#page=7)
