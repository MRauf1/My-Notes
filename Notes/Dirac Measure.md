---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!info] Dirac Measure (Point Mass)[^1]
> For $x_0 \in X$, the Dirac measure (point mass) at $x_0$ is the measure on $\mathcal{P}(X)$
> $$
> \begin{align}
> \delta_{x_0}(E) = \begin{cases} 1 & x_0 \in E \\ 0 & x_0 \notin E \end{cases}
> \end{align}
> $$
> i.e. $\mu(E) = \sum_{x \in E} f(x)$ with $f(x_0) = 1$ and $f(x) = 0$ for $x \neq x_0$.

A special case of the weighted [[Counting Measure]]. The same name is used for its restriction to any smaller $\sigma$-algebra on $X$.

# Properties
- A [[Finite Measure]] (indeed a probability measure).
- Integration against it evaluates: $\int g\,d\delta_{x_0} = g(x_0)$, which is the rigorous meaning of the [[Dirac Delta Function]].
- Its [[Cumulative Distribution Function|distribution function]] on $\mathbb{R}$ is the [[Heaviside Function|Heaviside step]] at $x_0$; it is the [[Lebesgue-Stieltjes Measure]] of that step function.

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=38&annotation=KZAMA5UJ)
