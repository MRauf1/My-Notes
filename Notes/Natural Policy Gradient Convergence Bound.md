---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!abstract] Natural Policy Gradient Convergence Bound[^1]
> Run $K$ iterations of [[Natural Policy Gradient]] with exact $Q^{\pi^{(k)}} \in [0, V_{max}]$ and a suitable $\eta$, and let $\hat{\pi}$ be the uniform mixture of $\pi^{(1)}, \dots, \pi^{(K)}$, so $J(\hat{\pi}) = \frac{1}{K}\sum_k J(\pi^{(k)})$. Then for every comparator policy $\pi$ (e.g. $\pi^\star$),
> $$
> \begin{align}
> J(\pi) - J(\hat{\pi}) = O\left(\frac{V_{max}}{1-\gamma}\sqrt{\frac{\log|\mathcal{A}|}{K}}\right).
> \end{align}
> $$

> [!abstract] With Estimated Q-Functions[^2]
> If the update uses $f^{\pi^{(k)}} \approx Q^{\pi^{(k)}}$, then $J(\pi) - J(\hat{\pi}) = \text{(I)} + \text{(II)} + \text{(III)}$, where
> $$
> \begin{align}
> \text{(I)} &= \frac{1}{K}\sum_{k=1}^K\frac{1}{1-\gamma}\mathbb{E}_{d^\pi}\big[f^{\pi^{(k)}}(s,\pi) - f^{\pi^{(k)}}(s,\pi^{(k)})\big], \\
> \text{(II)} &= \frac{1}{K}\sum_{k=1}^K\frac{1}{1-\gamma}\mathbb{E}_{d^\pi}\big[f^{\pi^{(k)}}(s,\pi^{(k)}) - Q^{\pi^{(k)}}(s,\pi^{(k)})\big], \\
> \text{(III)} &= -\frac{1}{K}\sum_{k=1}^K\frac{1}{1-\gamma}\mathbb{E}_{d^\pi}\big[f^{\pi^{(k)}}(s,\pi) - Q^{\pi^{(k)}}(s,\pi)\big].
> \end{align}
> $$
> (I) is the mirror-descent regret on $f^{\pi^{(k)}}$ and obeys the same bound. With $\mathcal{T}^\pi$ the [[Bellman Evaluation Operator]],
> $$
> \begin{align}
> \text{(II)} + \text{(III)} = \frac{1}{K(1-\gamma)}\left(\sum_{k=1}^K\mathbb{E}_{d^{\pi^{(k)}}}\big[f^{\pi^{(k)}} - \mathcal{T}^{\pi^{(k)}}f^{\pi^{(k)}}\big] - \sum_{k=1}^K\mathbb{E}_{d^\pi}\big[f^{\pi^{(k)}} - \mathcal{T}^{\pi^{(k)}}f^{\pi^{(k)}}\big]\right).
> \end{align}
> $$

# Properties
- **Proof (exact case).** By the [[Performance Difference Lemma]] with the comparator's occupancy,
$$
\begin{align}
J(\pi) - J(\hat{\pi}) = \frac{1}{K(1-\gamma)}\sum_s d^\pi(s)\sum_{k=1}^K\big(Q^{\pi^{(k)}}(s,\pi) - Q^{\pi^{(k)}}(s,\pi^{(k)})\big),
\end{align}
$$
  after exchanging the sums over $s$ and $k$. The inner sum is the per-state [[Mirror Descent]] regret, $O(V_{max}\sqrt{K\log|\mathcal{A}|})$. With the entropic constant it is $V_{max}\sqrt{\frac{K}{2}\ln|\mathcal{A}|}$, giving $\frac{V_{max}}{1-\gamma}\sqrt{\frac{\ln|\mathcal{A}|}{2K}}$.
- The exchange of sums needs every $k$ to use the *same* distribution $d^\pi$. That's why the performance difference is expanded under the comparator's occupancy, not under $d^{\pi^{(k)}}$.
- No distribution-mismatch coefficient appears with exact Q-functions, unlike the [[Policy Gradient Stationary Point Suboptimality Bound]].
- **On-policy estimation** (fit $f^{\pi^{(k)}}$ by regression on Monte Carlo returns from $\pi^{(k)}$; Agarwal et al. 2020): (II) is controlled when the class realizes $Q^{\pi^{(k)}}$, but (III) needs $d^{\pi^{(k)}}$ to cover $d^\pi$, a coverage coefficient like PG's.
- **Off-policy estimation** (FQE or its minimax variant on data from $\mu$; Xie et al. 2021): under [[Bellman Completeness]], $\|f^{\pi^{(k)}} - \mathcal{T}^{\pi^{(k)}}f^{\pi^{(k)}}\|_{2,\mu}$ is small, and the clean form of (II) + (III) shows $\mu$ only needs to cover $d^\pi$ and $d^{\pi^{(k)}}$. Moreover, $\frac{1}{1-\gamma}\mathbb{E}_{d^{\pi^{(k)}}}[f - \mathcal{T}^{\pi^{(k)}}f] = \mathbb{E}_{d_0}[f(s,\pi^{(k)})] - J(\pi^{(k)})$ ([[Bellman Residual Telescoping Identity]]). A pessimistic estimate with $\mathbb{E}_{d_0}[f(s,\pi^{(k)})] \leq J(\pi^{(k)})$ makes that term non-positive, so only the comparator $\pi$ needs coverage. This is a special case of the [[Performance Difference Bellman Error Decomposition]].

# Questions
> [!question]- Why is the output the uniform *mixture* of the iterates, and what does mixing mean here?
> The regret bound controls the average $\frac{1}{K}\sum_k(J(\pi) - J(\pi^{(k)}))$, not the last iterate. A trajectory-level mixture (draw $k$ uniformly once, then run $\pi^{(k)}$ for the whole episode) has return exactly $\frac{1}{K}\sum_k J(\pi^{(k)})$, since $J$ is linear in the mixing weights at the trajectory level. A per-step mixture of action distributions would instead be a different stationary policy, whose value is not this average.

> [!question]- In the exact-case proof, why must the performance difference be expanded under $d^\pi$ rather than under $d^{\pi^{(k)}}$?
> The per-state mirror-descent guarantee bounds $\sum_k(Q^{\pi^{(k)}}(s,\pi) - Q^{\pi^{(k)}}(s,\pi^{(k)}))$ for each fixed $s$. To use it, the sum over $k$ must be moved inside $\sum_s d(s)$, which requires the same weight $d(s)$ for all $k$. The form $\mathbb{E}_{d^\pi}[A^{\pi^{(k)}}(s,\pi)]$ uses the fixed comparator occupancy. The alternative form under $d^{\pi^{(k)}}$ would change the weights with $k$.

[^1]: [Jiang, Notes on Importance Sampling and Policy Gradient (CS 542 notes), pp. 10–11](https://nanjiang.cs.illinois.edu/files/cs542f23/note6.pdf#page=10)
[^2]: [Jiang, Notes on Importance Sampling and Policy Gradient (CS 542 notes), pp. 11–12](https://nanjiang.cs.illinois.edu/files/cs542f23/note6.pdf#page=11)
