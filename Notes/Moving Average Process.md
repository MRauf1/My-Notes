---
tags: [statistics, time_series_analysis]
---

# Definition

> [!info] Definition 1 ([[Moving Average]] [[Stochastic Process]])
> [[Stochastic Process]] $X_t$ is called $q$-th order Moving Average  Process MA(q) if it satisfies the equation
> $$
> \begin{align}
> X_t &= W_t + \theta_1 W_{t - 1} + \dots + \theta_q W_{t - q} \\
> X_t &= \theta(B) W_t
> \end{align}
> $$
> where $X_t$ is [[Stationary Stochastic Process]], $W_t$ is [[White Noise Process]], and $\theta(B)$ is the [[Moving Average Operator]].

# Variants
- [[Autoregressive Moving Average Process]]

# Types
- [[Invertible Moving Average Process]]

# [[Operator]]
- [[Moving Average Operator]]

# Properties
## [[Auto Covariance]]
- $\gamma(h) = \begin{cases}\sigma^2_w \sum_{j=0}^{q-h} \theta_j \theta_{j + h} & 0 \leq h \leq q \\ 0 & h > q \end{cases}$

## [[Auto Correlation]]
- $\rho(h) = \begin{cases}\frac{\sum_{j=0}^{q-h} \theta_j \theta_{j + h}}{1 + \theta_1^2 + \dots + \theta_q^2} & 0 \leq h \leq q \\ 0 & h > q\end{cases}$