---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Probability Integral Transform[^1]
> If $X$ has a continuous cdf $F$, then $F(X) \sim \text{Uniform}(0, 1)$. Consequently, if $Y_1 < \dots < Y_n$ are the [[Order Statistic|order statistics]] of a [[Random Sample]] from a continuous distribution with cdf $F$, then $Z_i = F(Y_i)$ have joint pdf
> $$
> \begin{align}
> h(z_1, \dots, z_n) = n!, \quad 0 < z_1 < z_2 < \dots < z_n < 1
> \end{align}
> $$
> and zero elsewhere, i.e. they are the order statistics of a uniform $(0, 1)$ sample.

$F$ is a monotone map that sends each value to the probability mass below it, and since that mass is spread continuously, the image is uniform: $P(F(X) \leq u) = P(X \leq F^{-1}(u)) = u$.

# Properties
- Its converse is [[Inverse Transform Sampling]]: if $U \sim \text{Uniform}(0, 1)$, then $F^{-1}(U)$ has cdf $F$.
- Composing it with inversion gives the [[QQ Transformation]] $G^{-1}(F(X)) \sim G$.
- $F(Y_k) \sim$ [[Beta Distribution|Beta]]$(k, n - k + 1)$, so $E[F(Y_k)] = k/(n+1)$ ([[Sample Quantile]]), and the coverage $F(Y_j) - F(Y_i) \sim \text{Beta}(j - i, n - j + i + 1)$ does not depend on $F$; this makes [[Tolerance Interval|tolerance intervals]] and quantile intervals distribution-free.
- Under a simple null hypothesis with a continuous [[Test Statistic]], the [[P-Value]] $1 - F_{H_0}(T)$ is uniform on $(0, 1)$ for the same reason.
- **Multivariate version**: applying it to the successive conditional cdfs $F(x_i \mid x_{<i})$ (Rosenblatt transform) maps any absolutely continuous random vector to independent uniforms; composed with conditional quantile functions it gives the [[Knothe-Rosenblatt Rearrangement]].[^2]
- Continuity is essential: for a discrete $X$, $F(X)$ takes only finitely or countably many values.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=332)
[^2]: Supplementary notes provided by the creator.
