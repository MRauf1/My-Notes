---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!abstract] Non-Stationary Bellman Error Performance Difference Bound[^1]
> Let $f_0, \dots, f_k \in \mathbb{R}^{\mathcal{S}\times\mathcal{A}}$ be arbitrary, let $\hat{\pi} := \pi_{f_{k:0}} = \pi_{f_k}\circ\pi_{f_{k-1}}\circ\cdots\circ\pi_{f_0}$ be the non-stationary policy that takes the [[Greedy Policy|greedy action]] of $f_{k-t+1}$ at step $t = 1, \dots, k+1$ and arbitrary actions afterwards, and let $\pi$ be any (possibly non-stationary) comparator policy. Then
> $$
> \begin{align}
> J(\pi) - J(\hat{\pi}) \leq \sum_{t=1}^k\gamma^{t-1}\Big(\mathbb{E}_{d^\pi_t}[\mathcal{T}f_{k-t} - f_{k-t+1}] + \mathbb{E}_{d^{\hat{\pi}}_t}[f_{k-t+1} - \mathcal{T}f_{k-t}]\Big) + \gamma^k V_{max},
> \end{align}
> $$
> where $d^\pi_t$ is the distribution of $(s_t, a_t)$ under $\pi$ from $d_0$ and $\mathcal{T}$ is the [[Bellman Optimality Operator]].

# Properties
- Non-stationary version of the [[Bellman Error Performance Difference Bound]] $J(\pi) - J(\pi_f) \leq \frac{1}{1-\gamma}(\mathbb{E}_{d^\pi}[\mathcal{T}f - f] + \mathbb{E}_{d^{\pi_f}}[f - \mathcal{T}f])$. That bound needs a self-consistent $f$ (small $\|f - \mathcal{T}f\|$), whereas FQI only controls $\|f_t - \mathcal{T}f_{t-1}\|$. Here $\hat{\pi}$ is greedy for the non-stationary function $f_{k:0} := f_k\circ f_{k-1}\circ\cdots\circ f_0$, which *is* self-consistent step to step. The extra $\gamma^k V_{max}$ is the truncation error after step $k$ ([[Truncated Value Function]]).
- With $\pi = \pi^\star$, bounding the right side by data requires $\mu$ to cover the *per-step* distributions of $(\pi^\star)^t$ for $t \leq k$ and of $\pi_{f_{k:k'}}$ for $0 \leq k' \leq k$ (from $d_0$). This is the guarantee behind [[Non-Stationary Fitted Q-Iteration]].
- For the minimax algorithm $\arg\min_{f\in\mathcal{F}}\max_{g\in\mathcal{F}}\mathcal{L}_D(f; f) - \mathcal{L}_D(g; f)$ (Chen & Jiang 2019; Xie & Jiang 2020), the stationary bound applies directly, with the coverage taken over the whole discounted [[State-Action Occupancy|occupancy]] instead.

# Questions
> [!question]- Why does this bound need $\mu$ to cover each per-step distribution $d^\pi_t$ separately, while the stationary bound for the minimax algorithm only needs coverage of the occupancy $d^\pi$?
> FQI controls each regression error $\|f_t - \mathcal{T}f_{t-1}\|_{2,\mu}$ separately, and each term of the sum pairs a different function difference with a different $d^\pi_t$. So the change of measure from $d^\pi_t$ to $\mu$ must be done term by term. For the minimax algorithm one controls the single quantity $\|f - \mathcal{T}f\|_\mu$, and the stationary bound averages it under $d^\pi = (1-\gamma)\sum_t\gamma^{t-1}d^\pi_t$ as a whole, so only $d^\pi/\mu$ needs bounding, which can be much smaller than $\max_t d^\pi_t/\mu$.

[^1]: [Jiang, Notes on Fitted Q-iteration (CS 542 notes), pp. 6–7](https://nanjiang.cs.illinois.edu/files/cs542f22/note5.pdf#page=6)
