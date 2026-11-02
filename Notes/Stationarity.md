---
tags:
  - statistics
  - time_series_analysis
---

# Definition

> [!info] Definition 1 (Stationarity)[^1]
> A [[Stochastic Process]] $\{X_t\}$ is strictly stationary if its probabilistic behavior is invariant under time shifts: for every $k$, all times $t_1, \dots, t_k$, and every shift $h$,
> $$
> \begin{align}
> (X_{t_1}, \dots, X_{t_k}) \overset{d}{=} (X_{t_1 + h}, \dots, X_{t_k + h})
> \end{align}
> $$
> It is weakly (second-order) stationary if it has finite [[Variance|variance]], a constant mean, and a covariance $\operatorname{Cov}(X_t, X_s)$ that depends only on the lag $t - s$.

Strict stationarity with finite variance implies weak stationarity; the converse holds for Gaussian processes.

# Types
- [[Non-Stationary Stochastic Process]]
- [[Trend Stationary Stochastic Process]]
- [[Stationary Stochastic Process]]
- [[Joint Stationary Stochastic Process]]

[^1]: [Stationary Process (Wikipedia)](https://en.wikipedia.org/wiki/Stationary_process)
