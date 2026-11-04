---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] State Abstraction[^1]
> For a [[Markov Decision Process]] with state space $\mathcal{S}$, a state abstraction (also called state aggregation or compression) is a mapping $\phi : \mathcal{S} \to \mathcal{S}_\phi$ onto a finite *abstract* state space $\mathcal{S}_\phi$. States with $\phi(s^{(1)}) = \phi(s^{(2)})$ are treated as the same state. Equivalently, $\phi$ is an [[Equivalence Relation|equivalence relation]] on $\mathcal{S}$, whose classes $\phi^{-1}(x)$ form a [[Partition|partition]].
>
> It is encoded by the $|\mathcal{S}_\phi| \times |\mathcal{S}|$ matrix $\Phi(x, s) = \mathbb{I}[\phi(s) = x]$. $\Phi P(s,a)$ collapses the next-state distribution over $\mathcal{S}$ to a distribution over $\mathcal{S}_\phi$.

> [!info] Lifting[^2]
> For a function $f$ on $\mathcal{S}_\phi$, its *lifted* version is the function on $\mathcal{S}$ given by $[f]_M(s) := f(\phi(s))$, or $[f]_M = \Phi^\top f$ in vector form. State-action functions and abstract policies $\pi : \mathcal{S}_\phi \to \mathcal{A}$ are lifted the same way. Lifted functions are exactly the functions that are piecewise constant on the classes of $\phi$.

# Types
Ordered from strictest to most lenient (see [[State Abstraction Hierarchy Theorem]]):
- [[Model-Irrelevant Abstraction]] (bisimulation)
- [[Q-Star-Irrelevant Abstraction]]
- [[Pi-Star-Irrelevant Abstraction]]

# Properties
- **Typical use.** Convert every tuple $(s, a, r, s')$ in a dataset to $(\phi(s), a, r, \phi(s'))$ and run any tabular algorithm over $\mathcal{S}_\phi$, e.g. [[Certainty-Equivalence (Reinforcement Learning)|certainty-equivalence]], which builds the [[Abstract Model (State Abstraction)|abstract model]]. This is always doable, but there may be no MDP over $\mathcal{S}_\phi$ that is the ground-truth process for the converted data.
- **Estimation vs. approximation.** Aggregating states pools their samples, raising the effective sample size and lowering *estimation error* (with $n$ samples per $(s,a)$, merging two states gives $2n$ per abstract pair). Aggregating dissimilar states incurs *approximation error*, which does not vanish with infinite data. Fine $\phi$ means low approximation error, coarse $\phi$ low estimation error ([[State Abstraction Finite Sample Bound]]). This is the general [[Approximation Error|approximation]]–estimation trade-off of statistical learning.
- Also reduces computational cost of planning, since the effective state space is smaller.

[^1]: [Jiang, Notes on State Abstractions (CS 542 notes), pp. 1–2](https://nanjiang.cs.illinois.edu/files/cs542f22/note4.pdf#page=1)
[^2]: [Jiang, Notes on State Abstractions (CS 542 notes), p. 5](https://nanjiang.cs.illinois.edu/files/cs542f22/note4.pdf#page=5)
