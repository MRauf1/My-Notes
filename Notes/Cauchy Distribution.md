---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Cauchy Distribution[^1]
> A [[Continuous Random Variable]] $X$ has the standard Cauchy distribution if its pdf is
> $$
> \begin{align}
> f(x) = \frac{1}{\pi(1 + x^2)}, \quad -\infty < x < \infty
> \end{align}
> $$
> More generally, with location $x_0$ and scale $\gamma > 0$, $f(x) = \dfrac{1}{\pi\gamma\left[1 + \left(\frac{x - x_0}{\gamma}\right)^2\right]}$.

# Properties
- [[Cumulative Distribution Function|cdf]] $F(x) = \frac{1}{2} + \frac{1}{\pi}\arctan x$, so $F^{-1}(u) = \tan(\pi(u - \tfrac{1}{2}))$: if $U$ is uniform on $(0, 1)$ then $\tan(\pi(U - \tfrac12))$ is standard Cauchy ([[Inverse Transform Sampling]]).
- Heavy tails: $\int |x| f(x)\,dx = \infty$, so the [[Expectation|mean]] does not exist, nor does any moment of order $\geq 1$ ([[Moment (Statistics)]]); hence it has no [[Moment Generating Function|mgf]].
- Its [[Median]] and [[Mode]] are $x_0$, and its [[Interquartile Range]] is $2\gamma$; quantile-based summaries replace the missing mean and variance.
- [[Characteristic Function (Probability)|Characteristic function]] $\varphi(t) = e^{i x_0 t - \gamma|t|}$.
- Stable: if $X_1, \dots, X_n$ are [[Independent and Identically Distributed|iid]] standard Cauchy, the sample mean $\bar{X}$ is again standard Cauchy, so averaging does not concentrate it; the law of large numbers fails because the mean does not exist.
- The ratio $Z_1/Z_2$ of two independent standard [[Normal Distribution|normals]] is standard Cauchy; it is the [[t-Distribution]] with $1$ degree of freedom.
- If $X$ is standard Cauchy, so is $1/X$.
- Geometric origin: if a ray is emitted from $(0, 1)$ at a uniformly random angle $\Theta \in (-\pi/2, \pi/2)$ towards the $x$-axis, its intersection point $\tan \Theta$ is standard Cauchy.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=162)
