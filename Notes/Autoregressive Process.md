---
tags: [statistics, time_series_analysis]
---

# Definition


> [!info] Definition 1 ([[Autoregressive]] [[Stochastic Process]])
> [[Stochastic Process]] $X_t$ is called $p$-th order Autoregressive Process AR(p) if it satisfies the equation
> $$
> \begin{align}
> X_t &= \phi_1 X_{t - 1} + \dots + \phi_p X_{t - p} + W_t \\
> \phi(B) X_t &= W_t
> \end{align}
> $$
> where $X_t$ is [[Stationary Stochastic Process]], $W_t$ is [[White Noise Process]], and $\phi(B)$ is the [[Autoregressive Operator]]
> Not always, but sometimes it's convenient to assume that $E[X_t] = 0$.

Regression/prediction of current value as a function of past values.

# Variants
- [[Autoregressive Moving Average Process]]

# Types
- [[Causal Autoregressive Process]]

# [[Operator]]
- [[Autoregressive Operator]]

# Properties
## [[Auto Covariance]]
- $\gamma(h) = \sigma^2_w \sum_{j=0}^{\infty} \psi_j \psi_{j + h}$ for $h \geq 0$

## [[Auto Correlation]]
- $\rho(h) = \frac{\sum_{j=0}^{\infty \psi_j \psi_{j + h}}}{\sum_{j=0}^{\infty} \psi_j^2}$ for $h \geq 0$
### [[Partial Auto Correlation]]
- $\phi_{hh} = 0$ for $k > p$