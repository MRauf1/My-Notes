---
tags: [mathematics, complex_analysis]
---

# Definition

> [!info] Definition 1 (Laurent [[Infinite Series]])
> Laurent series is an [[Infinite Series]] of the form
> $$
> \begin{align}
> \sum_{k = - \infty}^{\infty} a_k (z - z_0)^k = \sum_{k=0}^{\infty} a_k (z - z_0)^k + \sum_{k=1}^{\infty} \frac{a_{-k}}{(z - z_0)^k}
> \end{align}
> $$
> Where the [[Infinite Series]] on the right hand side are [[Power Series]] (the 2nd one is not exactly a power series, but close enough if you let $w = \frac{1}{z - z_0}$).
> The inner and outer [[Radius of Convergence]] are
> $$
> \begin{align}
> R_I &= \limsup_{k \rightarrow \infty} |a_{-k}|^{\frac{1}{k}} \\
> R_O &= \frac{1}{\limsup_{k \rightarrow \infty} |a_k|^{\frac{1}{k}}}
> \end{align}
> $$
> If $R_I < R_O$, then $\{z | R_I < |z - z_0| < R_O\}$ is called the [[Ring of Convergence]] (or annulus of convergence).

# Properties
- [[Laurent Series Representation]]