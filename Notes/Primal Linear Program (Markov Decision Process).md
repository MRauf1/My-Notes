---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Primal Linear Program (Markov Decision Process)
> For a [[Markov Decision Process]] with initial state distribution $d_0$, the [[Linear Programming (Markov Decision Process)|LP]]
> $$
> \begin{align}
> \min_{V \in \mathbb{R}^{\mathcal{S}}} \; & d_0^\top V \\
> \text{s.t.} \; & V \geq \mathcal{T}V
> \end{align}
> $$
> using the [[Bellman Optimality Operator]] $\mathcal{T}$, with decision variable $V$ (a candidate [[Value Function]]).

# Properties
- The constraint $V \geq \mathcal{T}V$ is nonlinear due to the $\max_a$ inside $\mathcal{T}$; for each $s$, it is equivalent to the $|\mathcal{A}|$ linear constraints $V(s) \geq R(s,a) + \gamma\,\mathbb{E}_{s'\sim P(s,a)}[V(s')]$, $\forall a \in \mathcal{A}$, giving $|\mathcal{S}|$ decision variables and $|\mathcal{S}\times\mathcal{A}|$ constraints in total.
- $V \geq \mathcal{T}V \Rightarrow V \geq V^\star$, and $V^\star$ is feasible; consequently, when $d_0$ is fully supported on $\mathcal{S}$ (i.e. $d_0(s) > 0 \; \forall s$), minimizing $d_0^\top V$ yields the optimal solution $V = V^\star$.
- Its dual is the [[Dual Linear Program (Markov Decision Process)|dual LP]].
