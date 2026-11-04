---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Realizability (Reinforcement Learning)[^1]
> A function class $\mathcal{F} \subset \mathbb{R}^{\mathcal{S}\times\mathcal{A}}$ is realizable if it contains the optimal [[Action-Value Function|action-value function]]:
> $$
> \begin{align}
> Q^\star \in \mathcal{F}.
> \end{align}
> $$
> For policy evaluation of $\pi$, the condition is $Q^\pi \in \mathcal{F}$.

# Properties
- The minimal representational assumption for value-based learning with function approximation. It is monotone: any superset of a realizable class is realizable.
- Implied by [[Bellman Completeness]] for finite $\mathcal{F}$, but strictly weaker. Realizability alone is generally not enough for the iterative regression of [[Fitted Q-Iteration]], whose targets $\mathcal{T}f$ for $f \neq Q^\star$ need not lie in $\mathcal{F}$.
- In the [[Fitted Q-Iteration Fast Rate]], realizability of the regression target makes the excess squared loss equal $\|f - \mathcal{T}f'\|_\mu^2$, whose variance it then controls.

[^1]: [Jiang, Notes on Fitted Q-iteration (CS 542 notes), p. 1](https://nanjiang.cs.illinois.edu/files/cs542f22/note5.pdf#page=1)
