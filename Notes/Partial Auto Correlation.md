---
tags: statistics, time_series_analysis
---

# Definition

> [!info] Definition 1 (Partial [[Auto Correlation]])
> For [[Random Variable]] $X, Y, Z$, the partial correlation between $X, Y$ given $Z$ is obtained by
> 1) [[Regression|Regressing]] $X$ on $Z$ to obtain $\hat{X}$
> 2) [[Regression|Regressing]] $Y$ on $Z$ to obtain $\hat{Y}$
> 3) $\rho_{XY|Z} = Corr[X - \hat{X}, Y - \hat{Y}]$
> For [[Stationary Stochastic Process]] $X_t$, its partial correlation is
> $$
> \begin{align}
> \phi_{hh} = Corr[X_{t + h} - \hat{X}_{t + h}, X_t - \hat{X}_t]
> \end{align}
> $$
> where $\hat{X}_{t + h}$ is the [[Regression]] of $X_{t + h}$ on $\{X_{t + h - 1, \dots, X_{t + 1}}\}$ and $\hat{X}_{t}$ is the [[Regression]] of $X_{t}$ on $\{X_{t + h - 1, \dots, X_{t + 1}}\}$.