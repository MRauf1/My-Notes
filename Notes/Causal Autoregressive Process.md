---
tags: statistics, time_series_analysis
---

# Definition

> [!info] Definition 1 (Causal [[Autoregressive Process]])
> [[Autoregressive Process]] $X_t$ is said to be causal or have causal representation if it can be written as
> $$
> \begin{align}
> X_t = \mu + \sum_{j=0}^{\infty} \psi_j W_{t-j}
> \end{align}
> $$
> for constants $\psi_j$ satisfying $\sum_{j=0}^{\infty} \psi_j^2 < \infty$
> If we mean-center $X_t$ as in [[Wold Decomposition]], then it can be written as 
> $$
> \begin{align}
> X_t = \psi(B) W_t
> \end{align}
> $$
> where $\psi(B)$ is the [[Causal Representation Operator]]. If an [[Autoregressive Process]] is causal, then it has a $MA(\infty)$ [[Moving Average Process]] representation.
> To check if [[Autoregressive Process]] is causal, take the [[Autoregressive Operator]] and frame it as a [[Polynomial]] set to 0 $(\phi(z) = 0)$. If all of the $p$ roots of this equation lie outside of the unit circle ([[Absolute Value of Complex Number]] $> 1$), then it is causal. Otherwise, it is not.

If $X_t$ is causal, then it does not depend on the future.

# [[Operator]]
- [[Causal Representation Operator]]