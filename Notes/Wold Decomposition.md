---
tags: statistics, time_series_analysis
---

# Definition

> [!info] Definition 1 (Wold Decomposition)
> A [[Stationary Stochastic Process]] $X_t$ can be written as a [[Linear Combination]] of [[White Noise Process]]
> $$
> \begin{align}
> X_t = \mu + \sum_{j=0}^{\infty} \psi_j W_{t - j}
> \end{align}
> $$
> where $\psi_j$ satisfy $\sum_{j=0}^{\infty} \psi_j^2 < \infty$ and $\psi_0 = 1$
> Its expectation and [[Auto Covariance]] are $E[X_t] = \mu$ and $\gamma(h) = \sigma_w^2 \sum_{j=0}^{\infty} \psi_{j + h} \psi_j$
> If we mean-center $X_t$ by $X'_t = X_t - \mu$ (and write $X'_t$ as $X_t$), then it can be written as
> $$
> \begin{align}
> X_t = \psi(B) W_t
> \end{align}
> $$
> where $\psi(B)$ is the [[Causal Representation Operator]]. This describes the [[Stationary Stochastic Process]] as a $MA(\infty)$ [[Moving Average Process]] Representation.
