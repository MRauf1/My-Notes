---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] $\pi^\star$-Irrelevant Abstraction[^1]
> A [[State Abstraction|state abstraction]] $\phi$ of an MDP $M$ is $\pi^\star$-irrelevant if there exists an [[Optimal Policy|optimal policy]] $\pi^\star_M$ such that for all $s^{(1)}, s^{(2)}$ with $\phi(s^{(1)}) = \phi(s^{(2)})$, $\pi^\star_M(s^{(1)}) = \pi^\star_M(s^{(2)})$.

> [!info] $\epsilon_{\pi^\star}$-Approximate $\pi^\star$-Irrelevance[^2]
> $\phi$ is $\epsilon_{\pi^\star}$-approximate $\pi^\star$-irrelevant if there exists an abstract policy $\pi : \mathcal{S}_\phi \to \mathcal{A}$ whose lifted version satisfies $\|V^\star_M - V^{[\pi]_M}_M\|_\infty \leq \epsilon_{\pi^\star}$. The exact definition is the case $\epsilon_{\pi^\star} = 0$.

# Properties
- The most lenient notion in the [[State Abstraction Hierarchy Theorem|abstraction hierarchy]]: it only requires that some near-optimal policy can be expressed over $\mathcal{S}_\phi$, so it gives the largest generalization benefit.
- Value-based and model-based algorithms run on $\pi^\star$-irrelevant abstractions may break down. Only policy-search methods that directly optimize the return over a policy class keep their guarantees, owing to their robustness to agnosticity.
- Its approximation error is monotone: refining $\phi$ can only lower the best achievable $\epsilon_{\pi^\star}$, as with realizability assumptions in supervised learning.

[^1]: [Jiang, Notes on State Abstractions (CS 542 notes), p. 2](https://nanjiang.cs.illinois.edu/files/cs542f22/note4.pdf#page=2)
[^2]: [Jiang, Notes on State Abstractions (CS 542 notes), pp. 3, 5–6](https://nanjiang.cs.illinois.edu/files/cs542f22/note4.pdf#page=5)
