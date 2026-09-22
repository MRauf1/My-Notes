---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Bellman Optimality Operator
> For a [[Markov Decision Process]] $M$, the operator $\mathcal{T}_M : \mathbb{R}^{|\mathcal{S}\times\mathcal{A}|} \to \mathbb{R}^{|\mathcal{S}\times\mathcal{A}|}$ (or simply $\mathcal{T}$) defined, for $f \in \mathbb{R}^{|\mathcal{S}\times\mathcal{A}|}$, by
> $$
> \begin{align}
> (\mathcal{T}f)(s,a) := R(s,a) + \gamma \langle P(s,a), V_f \rangle
> \end{align}
> $$
> where $V_f(\cdot) := \max_{a\in\mathcal{A}} f(\cdot, a)$.

# Properties
- $Q^\star$ is the fixed point of $\mathcal{T}$: $Q^\star = \mathcal{T}Q^\star$, giving a concise restatement of the [[Bellman Optimality Equation]].
- $\mathcal{T}$ is a $\gamma$-[[Contraction]] under the [[Infinity Norm|infinity norm]]: $\|\mathcal{T}f - \mathcal{T}f'\|_\infty \leq \gamma\|f-f'\|_\infty$ for any $f, f' \in \mathbb{R}^{|\mathcal{S}\times\mathcal{A}|}$. This property drives the convergence of [[Value Iteration]].
