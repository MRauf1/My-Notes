---
tags: [statistics, time_series_analysis]
---

# Definition

> [!info] Definition 1 (Mixed [[Autoregressive Process]] [[Moving Average Process]] [[Stochastic Process]])
> [[Stationary Stochastic Process]] $X_t$ is ARMA(p, q) if it is both an [[Causal Autoregressive Process]] AR(p) and [[Invertible Moving Average Process]] MA(q).
> It can be written as
> $$
> \begin{align}
> \phi(B) X_t = \theta(B) W_t
> \end{align}
> $$
> where $\phi(B)$ is the [[Autoregressive Operator]] and $\theta(B)$ is the [[Moving Average Operator]].
> To avoid parameter redundancy, ARMA(p, q) requires that $\phi(B)$ and $\theta(B)$ share no common factors.

Generalization of both [[Autoregressive Process]] and [[Moving Average Process]].

# Variants
- [[Autoregressive Integrated Moving Average Process]]