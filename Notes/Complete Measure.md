---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!info] Complete Measure[^1]
> A [[Measure (Measure Theory)|measure]] $\mu$ on $(X, \mathcal{M})$ is complete if its domain contains all subsets of [[Null Set (Measure Theory)|null sets]]:
> $$
> \begin{align}
> N \in \mathcal{M},\ \mu(N) = 0,\ F \subseteq N \implies F \in \mathcal{M}.
> \end{align}
> $$

If $\mu(E) = 0$ and $F \subseteq E$, monotonicity gives $\mu(F) = 0$ *provided* $F \in \mathcal{M}$, which need not hold. Completeness removes that technicality.

# Properties
- Every measure can be made complete by enlarging its domain ([[Measure Completion Theorem]]).
- The restriction of an [[Outer Measure]] to its Carathéodory-measurable sets is complete ([[Carathéodory's Theorem]]).
- [[Lebesgue Measure]] on the Lebesgue $\sigma$-algebra is complete; its restriction to the [[Borel Sigma-Algebra]] is not.
- If $\mu$ is complete, so is its saturation ([[Saturated Measure]]).

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=39&annotation=B2AF5PNP)
