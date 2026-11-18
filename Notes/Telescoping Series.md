---
tags:
  - mathematics
  - calculus
---

# Definition

> [!info] Definition 1 (Telescoping Series)[^1]
> An [[Infinite Series]] whose terms have the form $a_n = b_n - b_{n+1}$. Its partial sums collapse:
> $$
> \begin{align}
> s_n = \sum_{k=1}^{n} (b_k - b_{k+1}) = b_1 - b_{n+1}
> \end{align}
> $$
> so the series converges if and only if $\lim b_n$ exists, with sum $b_1 - \lim_{n \to \infty} b_n$.

# Properties
- Typically revealed by [[Partial Fractions]], e.g. $\frac{1}{n(n+1)} = \frac{1}{n} - \frac{1}{n+1}$, or by [[Logarithm Quotient Rule|log rules]], e.g. $\ln\frac{n}{n+1} = \ln n - \ln(n+1)$.
- The terms may also telescope with a gap: $b_n - b_{n+k}$ leaves $k$ surviving terms.

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=744)
