---
tags: [mathematics, complex_analysis]
---

# Definition

> [!abstract] Theorem 1 (Cauchy's Formula for a Ring)
> Let $f$ be [[Complex Analytic Function]] on $A = \{z | R_1 < |z - z_0| < R_2\}$ and fix $z \in A$. If $R_1 < r_1 < |z - z_0| < r_2 < R_2$, then
> $$
> \begin{align}
> f(z) = \frac{1}{2 \pi i} \oint_{\partial B(z_0, r_2)} \frac{f(w)}{w - z} dw - \frac{1}{2 \pi i} \oint_{\partial B(z_0, r_1)} \frac{f(w)}{w - z} dw
> \end{align}
> $$