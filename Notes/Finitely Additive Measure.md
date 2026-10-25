---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!info] Finitely Additive Measure[^1]
> A function $\mu : \mathcal{M} \to [0, \infty]$ on a [[Sigma-Field|$\sigma$-algebra]] $\mathcal{M}$ is a finitely additive measure if $\mu(\emptyset) = 0$ and, for [[Disjoint Sets|disjoint]] $E_1, \dots, E_n \in \mathcal{M}$,
> $$
> \begin{align}
> \mu\left(\bigcup_{j=1}^n E_j\right) = \sum_{j=1}^n \mu(E_j),
> \end{align}
> $$
> but $\mu$ is not required to be countably additive.

Every [[Measure (Measure Theory)|measure]] is finitely additive; the converse fails. The gap between the two is exactly a continuity condition.

# Properties
- A finitely additive measure is a measure if and only if it is continuous from below. If $\mu(X) < \infty$, it is a measure if and only if it is continuous from above ([[Measure Basic Properties]]).[^2]
- On an infinite set $X$ with $\mathcal{M} = \mathcal{P}(X)$, setting $\mu(E) = 0$ for finite $E$ and $\mu(E) = \infty$ for infinite $E$ gives a finitely additive measure that is not a measure.[^3]

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=38&annotation=LSYGIRKP)
[^2]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=40&annotation=XEGYUGLZ)
[^3]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=38&annotation=MRQF6WD5)
