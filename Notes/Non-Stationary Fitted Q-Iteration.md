---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Non-Stationary Fitted Q-Iteration[^1]
> [[Fitted Q-Iteration]] that, instead of the stationary greedy policy $\pi_{f_k}$, outputs the non-stationary policy
> $$
> \begin{align}
> \pi_{f_{k:0}} := \pi_{f_k}\circ\pi_{f_{k-1}}\circ\cdots\circ\pi_{f_0},
> \end{align}
> $$
> which at step $t = 1, \dots, k+1$ takes the [[Greedy Policy|greedy action]] of $f_{k-t+1}$, and arbitrary actions afterwards.

# Properties
- **Guarantee.** Apply the [[Non-Stationary Bellman Error Performance Difference Bound]] with $\pi = \pi^\star$. Each term is at most $\|f_{k-t+1} - \mathcal{T}f_{k-t}\|_{2,\nu}$ for a per-step distribution $\nu$, which [[Concentrability Coefficient|concentrability]] and one regression step ($\|f_j - \mathcal{T}f_{j-1}\|_\mu^2 \leq 2\epsilon$, as in the [[Fitted Q-Iteration Error Bound]]) bound by $\sqrt{2C\epsilon}$:
$$
\begin{align}
J(\pi^\star) - J(\pi_{f_{k:0}}) \leq \frac{2(1-\gamma^k)}{1-\gamma}\sqrt{2C\epsilon} + \gamma^k V_{max}.
\end{align}
$$
  This saves a horizon factor $\frac{1}{1-\gamma}$ over stationary FQI, as the non-stationary output policy does for [[Value Iteration]] (Scherrer & Lesner 2012).
- **Reduction for stationary FQI.** By the [[Performance Difference Lemma]],
$$
\begin{align}
J(\pi^\star) - J(\pi_{f_k}) = \frac{1}{1-\gamma}\mathbb{E}_{s\sim d^{\pi_{f_k}}}[V^\star(s) - Q^\star(s, \pi_{f_k})] \leq \frac{1}{1-\gamma}\mathbb{E}_{s\sim d^{\pi_{f_k}}}[V^\star(s) - V^{\pi_{f_{k:0}}}(s)],
\end{align}
$$
  and the right side is the non-stationary guarantee with $d^{\pi_{f_k}}$ as the initial distribution. This reproves the stationary $\frac{1}{(1-\gamma)^2}$ bound, with error propagation only along "simple" greedy policies: the data must cover the distributions of $(\pi^\star)^t$ and $\pi_{f_{k:k'}}$ started from $d^{\pi_{f_k}}$.
- The result might be improved by the periodic policy that repeats $\pi_{f_{k:0}}$ forever (Scherrer & Lesner 2012). Running the minimax algorithm also saves the horizon factor (Xie & Jiang 2020).

# Questions
> [!question]- In the reduction for stationary FQI, why is $Q^\star(s, \pi_{f_k}) \geq V^{\pi_{f_{k:0}}}(s)$?
> $Q^\star(s, \pi_{f_k})$ is the return of taking $\pi_{f_k}$'s action at $s$ and then acting optimally. $V^{\pi_{f_{k:0}}}(s)$ takes the same first action ($\pi_{f_k}$ is the first-step policy of $\pi_{f_{k:0}}$) and then follows $\pi_{f_{k-1}}\circ\cdots$, which is no better than optimal.

[^1]: [Jiang, Notes on Fitted Q-iteration (CS 542 notes), pp. 6–7](https://nanjiang.cs.illinois.edu/files/cs542f22/note5.pdf#page=6)
