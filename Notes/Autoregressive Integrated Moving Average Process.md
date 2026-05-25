---
tags: statistics, time_series_analysis
---

# Definition

> [!info] Definition 1 ([[Autoregressive Process]] Integrated [[Moving Average Process]] [[Stochastic Process]])
> [[Stochastic Process]] $X_t$ is ARIMA(p, d, q) process if $\nabla^d X_t = (1 - B)^d X_t$ is [[Autoregressive Moving Average Process]] ARMA(p, q). It can be written as
> $$
> \begin{align}
> \phi(B) (1 - B)^d X_t = \alpha + \theta(B) W_t
> \end{align}
> $$
> where $\alpha = \delta(1 - \phi_1 - \dots - \phi_p)$ and $\delta = E[\nabla^d X_t]$.
