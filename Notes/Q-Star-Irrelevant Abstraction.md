---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] $Q^\star$-Irrelevant Abstraction[^1]
> A [[State Abstraction|state abstraction]] $\phi$ of an MDP $M$ is $Q^\star$-irrelevant if for all $s^{(1)}, s^{(2)}$ with $\phi(s^{(1)}) = \phi(s^{(2)})$ and all $a \in \mathcal{A}$, $Q^\star_M(s^{(1)}, a) = Q^\star_M(s^{(2)}, a)$, where $Q^\star_M$ is the optimal [[Action-Value Function|action-value function]].

> [!info] $\epsilon_{Q^\star}$-Approximate $Q^\star$-Irrelevance[^2]
> $\phi$ is $\epsilon_{Q^\star}$-approximate $Q^\star$-irrelevant if there exists an abstract Q-function $f : \mathcal{S}_\phi \times \mathcal{A} \to \mathbb{R}$ with $\|[f]_M - Q^\star_M\|_\infty \leq \epsilon_{Q^\star}$, i.e. $Q^\star_M$ is within $\epsilon_{Q^\star}$ of a function that is piecewise constant on the classes of $\phi$.

# Properties
- Intermediate in the [[State Abstraction Hierarchy Theorem|abstraction hierarchy]]: implied by [[Model-Irrelevant Abstraction|model-irrelevance]], and it implies [[Pi-Star-Irrelevant Abstraction|$\pi^\star$-irrelevance]].
- Aggregated states can have very different rewards and dynamics, yet the Bellman update treats $Q^\star_M$ identically at them: $R(s^{(1)}, a) + \gamma\langle P(s^{(1)}, a), V^\star_M\rangle = R(s^{(2)}, a) + \gamma\langle P(s^{(2)}, a), V^\star_M\rangle$. That is why the [[Abstract Model (State Abstraction)|abstract model]] still recovers a near-optimal $Q^\star$ ([[Q-Star-Irrelevant Abstract Model Bound]]).
- The compression does not preserve rewards or dynamics, so guarantees of tabular algorithms (e.g. Q-learning, Delayed Q-learning) extend only with new analyses, not automatically.
- Corresponds to a standard supervised-learning *realizability* assumption on the function class of lifted Q-functions. Its approximation error is monotone under refinement.

[^1]: [Jiang, Notes on State Abstractions (CS 542 notes), p. 2](https://nanjiang.cs.illinois.edu/files/cs542f22/note4.pdf#page=2)
[^2]: [Jiang, Notes on State Abstractions (CS 542 notes), pp. 3–6, 8](https://nanjiang.cs.illinois.edu/files/cs542f22/note4.pdf#page=5)
