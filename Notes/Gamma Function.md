---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Gamma Function[^1]
> For $\alpha > 0$, the gamma function is the [[Improper Riemann Integral|improper integral]]
> $$
> \begin{align}
> \Gamma(\alpha) = \int_0^\infty y^{\alpha - 1} e^{-y}\,dy
> \end{align}
> $$
> which exists and is positive for every $\alpha > 0$.

# Properties
- $\Gamma(1) = \int_0^\infty e^{-y}\,dy = 1$.
- Recursion:[^2] for $\alpha > 1$, [[Integration by Parts]] gives $\Gamma(\alpha) = (\alpha - 1)\Gamma(\alpha - 1)$.
- Factorials: for a positive integer $n$, $\Gamma(n) = (n - 1)!$, which motivates $0! = \Gamma(1) = 1$; hence the name factorial function. It is the standard extension of the factorial to non-integer arguments.
- $\Gamma(1/2) = \sqrt{\pi}$ (from the Gaussian integral), so $\Gamma(n + 1/2) = \frac{(2n)!}{4^n n!}\sqrt{\pi}$.
- Scaling: $\int_0^\infty x^{\alpha-1} e^{-x/\beta}\,dx = \Gamma(\alpha)\beta^\alpha$, the normalizing constant of the [[Gamma Distribution]].
- Beta function: $B(\alpha, \beta) = \int_0^1 y^{\alpha-1}(1-y)^{\beta-1}\,dy = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha + \beta)}$, the normalizing constant of the [[Beta Distribution]].
- Extends by analytic continuation to all complex numbers except $0, -1, -2, \dots$; for large $\alpha$, Stirling's formula $\Gamma(\alpha) \approx \sqrt{2\pi/\alpha}\,(\alpha/e)^\alpha$.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=189)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=190)
