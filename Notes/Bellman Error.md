---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Bellman Error[^1]
> For $f \in \mathbb{R}^{|\mathcal{S}\times\mathcal{A}|}$, the quantity $\|f - \mathcal{T}f\|_\infty$, measuring the violation of $f$ with respect to the [[Bellman Optimality Equation]], where $\mathcal{T}$ is the [[Bellman Optimality Operator]].

# Properties
- Controls the distance to $Q^\star$: $\|f - Q^\star\|_\infty \leq \|f - \mathcal{T}f\|_\infty / (1-\gamma)$.
- Used to check convergence of [[Value Iteration]] without knowing $Q^\star$, by monitoring $\|f_k - f_{k+1}\|_\infty = \|f_k - \mathcal{T}f_k\|_\infty$ across iterates $f_k = Q^{\star,k}$.
- For two MDPs, $\|Q^\star_{\widehat{M}} - Q^\star_M\|_\infty \leq \frac{1}{1-\gamma}\|Q^\star_{\widehat{M}} - \mathcal{T}_M Q^\star_{\widehat{M}}\|_\infty$: the Bellman residual of an approximate $Q$ under the *true* operator. Bounding it from data is subtle when $Q^\star_{\widehat{M}}$ is estimated from the same samples, since concentration inequalities need the evaluated function to be independent of the data ([[Certainty-Equivalence Sample Complexity]]).[^2]
- Converted into decision loss in one step, with $\frac{2}{1-\gamma}$, by the [[Bellman Error Performance Difference Bound]].

# Questions
> [!question]- Prove $\|f - Q^\star\|_\infty \leq \|f - \mathcal{T}f\|_\infty / (1-\gamma)$.
> Since $Q^\star = \mathcal{T}Q^\star$: $\|f - Q^\star\|_\infty \leq \|f - \mathcal{T}f\|_\infty + \|\mathcal{T}f - \mathcal{T}Q^\star\|_\infty \leq \|f - \mathcal{T}f\|_\infty + \gamma\|f - Q^\star\|_\infty$ by the $\gamma$-contraction of the [[Bellman Optimality Operator]]. Rearranging gives the bound. Small successive differences of [[Value Iteration]] iterates therefore certify closeness to $Q^\star$, up to the factor $1/(1-\gamma)$.

[^1]: [Jiang, MDP Preliminaries (CS 542 notes), p. 10](https://nanjiang.cs.illinois.edu/files/cs542f22/note1.pdf#page=10)
[^2]: [Jiang, Notes on Tabular Methods (CS 542 notes), p. 6](https://nanjiang.cs.illinois.edu/files/cs542f22/note3.pdf#page=6)
