---
tags:
  - computer_science
  - numerical_analysis
---

# Definition
> [!info] Simpson's Rule[^1]
> A quadrature rule that integrates piecewise-quadratic interpolants of $f$. In $d = 1$, the composite rule with $n$ points has error $O(n^{-4})$ when $f$ has a continuous (bounded) fourth derivative. The straightforward tensor-product extension to $d$ dimensions has error $O(n^{-4/d})$.

# Properties
- Calculus form (even $n$): $S_n = \frac{\Delta x}{3}[f(x_0) + 4f(x_1) + 2f(x_2) + \dots + 4f(x_{n-1}) + f(x_n)]$; also $S_{2n} = \frac13 T_n + \frac23 M_n$ ([[Trapezoidal Rule]], [[Midpoint Rule]]). Error $|E_S| \le \frac{K(b-a)^5}{180 n^4}$ for $|f^{(4)}| \le K$.[^S]
- In $d = 1$ it is far faster than the $O(n^{-1/2})$ [[Monte Carlo Convergence Rate]]: Simpson's rule with $n$ points is about as accurate as [[Simple Monte Carlo]] with $An^8$ points, where $A$ depends on how the fourth derivative of $f$ compares to its variance.
- Useless for large $d$ because of the $O(n^{-4/d})$ rate ([[Curse of Dimensionality]]).
- Its rate requires smoothness; on non-smooth integrands it can do badly, where Monte Carlo does not.

[^1]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=17&annotation=HJT5NJQU); [Owen](zotero://open-pdf/library/items/TXMSRRI3?page=17&annotation=IA2TVW8I); [Owen](zotero://open-pdf/library/items/TXMSRRI3?page=17&annotation=LEXAWK3Q)
[^S]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=552)
