---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Welford's Algorithm (One-Pass Variance Update)[^1]
> To compute $S_n = \sum_{i=1}^n (y_i - \hat{\mu}_n)^2$ stably in a single pass, start with $\hat{\mu}_1 = y_1$, $S_1 = 0$, and for $i = 2, \dots, n$ update
> $$
> \begin{align}
> \delta_i &= y_i - \hat{\mu}_{i-1} \\
> \hat{\mu}_i &= \hat{\mu}_{i-1} + \frac{1}{i}\,\delta_i \\
> S_i &= S_{i-1} + \frac{i-1}{i}\,\delta_i^2
> \end{align}
> $$
> Then $s^2 = S_n/(n-1)$ is the [[Sample Variance]].

Motivation: the textbook formula for $s$ can lose accuracy when $n$ is large and $\sigma \ll |\mu|$, e.g. the one-pass form $\sum y_i^2 - n\hat{\mu}^2$ subtracts two nearly equal large numbers ([[Catastrophic Cancellation]]). With $n > 10^9$ routine on modern hardware, this matters for Monte Carlo.[^2]

# Properties
- Each update only adds small, centered quantities, avoiding cancellation; it also needs $O(1)$ memory, so the samples need not be stored.
- Used to compute $s$ for the [[Monte Carlo Confidence Interval]].
- A simpler, easily parallelized alternative for confidence intervals is the [[Paired Difference Variance Estimator]].

[^1]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=21&annotation=L6GFHXEP)
[^2]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=21&annotation=Y5AHH8HV)
