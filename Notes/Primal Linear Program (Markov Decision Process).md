---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Primal Linear Program (Markov Decision Process)[^1]
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

# Questions
> [!question]- Prove that $V \geq \mathcal{T}V$ implies $V \geq V^\star$.
> $\mathcal{T}$ is monotone, so applying it to $V \geq \mathcal{T}V$ gives $\mathcal{T}V \geq \mathcal{T}^2 V$, and by induction $V \geq \mathcal{T}^n V$ for all $n$. Since $\mathcal{T}$ is a $\gamma$-contraction, $\mathcal{T}^n V \to V^\star$, so $V \geq V^\star$. Feasibility of $V^\star$ is $V^\star = \mathcal{T}V^\star$.

> [!question]- Why does the LP need $d_0(s) > 0$ for all $s$ to return $V^\star$?
> Every feasible $V$ satisfies $V \geq V^\star$, and $V^\star$ is feasible, so $V^\star$ is always *a* minimizer. Full support makes it the unique one: a feasible $V \neq V^\star$ has $V(s) > V^\star(s)$ at some $s$, and $d_0(s) > 0$ gives $d_0^\top V > d_0^\top V^\star$.
>
> Without full support, uniqueness can fail. Take $s_0$ with $d_0(s_0) = 0$ that no other state can transition into, and set $V = V^\star + c\,e_{s_0}$ with $c > 0$. The constraints at $s \neq s_0$ are unchanged. At $s_0$, the right-hand side grows by at most $\gamma c < c$. So $V$ is feasible with the same objective value.

[^1]: [Jiang, MDP Preliminaries (CS 542 notes), p. 10](https://nanjiang.cs.illinois.edu/files/cs542f22/note1.pdf#page=10)
