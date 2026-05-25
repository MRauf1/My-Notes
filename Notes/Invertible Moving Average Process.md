---
tags: statistics, time_series_analysis
---

# Definition

> [!info] Definition 1 (Invertible [[Moving Average Process]])
> [[Moving Average Process]] $X_t$ is invertible if it can be written as
> $$
> \begin{align}
> W_t = \sum_{j=0}^{\infty} \pi_j X_{t-j}
> \end{align}
> $$
> for constants $\pi_j$ satisfying $\sum_{j=0}^{\infty} \pi_j^2 < \infty$.
> If we mean-center $X_t$ as in [[Wold Decomposition]], then it can be written as 
> $$
> \begin{align}
> \pi(B) X_t = W_t
> \end{align}
> $$
> where $\pi(B)$ is the [[Invertible Representation Operator]]. If an [[Moving Average Process]] is invertible, then it has a $AR(\infty)$ [[Autoregressive Process]] representation.
> To check if [[Moving Average Process]] is invertible, take the [[Moving Average Operator]] and frame it as a [[Polynomial]] set to 0 $(\theta(z) = 0)$. If all of the $p$ roots of this equation lie outside of the unit circle ([[Absolute Value of Complex Number]] $> 1$), then it is invertible. Otherwise, it is not.

# [[Operator]]
- [[Invertible Representation Operator]]