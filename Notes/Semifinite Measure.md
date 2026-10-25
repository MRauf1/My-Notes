---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!info] Semifinite Measure[^1]
> A [[Measure (Measure Theory)|measure]] $\mu$ on $(X, \mathcal{M})$ is semifinite if for each $E \in \mathcal{M}$ with $\mu(E) = \infty$ there exists $F \in \mathcal{M}$ with $F \subseteq E$ and $0 < \mu(F) < \infty$.

A semifinite measure has no "purely infinite" sets: every set of infinite measure can be probed by subsets of finite positive measure.

# Properties
- Every [[Sigma-Finite Measure|$\sigma$-finite measure]] is semifinite, but not conversely.[^2]
- **Semifinite part.** For any measure $\mu$, define[^3]
$$
\begin{align}
\mu_0(E) = \sup\{\mu(F) : F \subseteq E,\ \mu(F) < \infty\}.
\end{align}
$$
  Then $\mu_0$ is a semifinite measure, called the semifinite part of $\mu$; if $\mu$ is semifinite, $\mu = \mu_0$.
- Every measure decomposes as $\mu = \mu_0 + \nu$, where $\nu$ is a measure (in general not unique) taking only the values $0$ and $\infty$.[^4]
- For the measure $\mu(E) = \sum_{x \in E} f(x)$ on $\mathcal{P}(X)$: $\mu$ is semifinite iff $f(x) < \infty$ for every $x$ ([[Counting Measure]]).

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=38&annotation=V62UTMST)
[^2]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=40&annotation=4TGNLQAY)
[^3]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=40&annotation=XZJ8JWG9)
[^4]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=41&annotation=DZRMSF3N)
