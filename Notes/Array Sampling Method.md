---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Array Sampling Method[^1]
> Suppose $p_k = n_k/N$ for integers $n_k \geq 0$ summing to $N$. Build an array $A$ of length $N$ containing $n_k$ copies of each $k$, draw $Z \sim \mathcal{U}\{1, \dots, N\}$ ([[Discrete Uniform Distribution]]), and deliver $X = A_Z$.

A lookup-table instance of the discrete transformation method: if $P(Z = j) = q_j$ and $X = \tau(Z)$, then $p_k = \sum_j q_j \mathbf{1}\{\tau(j) = k\}$.[^2]

# Properties
- $O(1)$ per sample at the cost of $O(N)$ storage.
- When $A$ is sorted it is a [[QQ Transformation]] of $Z$; when $p$ changes during the simulation, $A$ can be updated in place without keeping it sorted (e.g. simulating preferential attachment random graphs).[^3]
- Resampling data, $X = x_I$ with $I \sim \mathcal{U}\{1, \dots, M\}$, is the case of one copy per data point and samples the [[Empirical Distribution Function|empirical distribution]] ([[Bootstrap]]).

[^1]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=20&annotation=A53CF36R)
[^2]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=20&annotation=JZUWT34A)
[^3]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=21&annotation=ANUL36VV)
