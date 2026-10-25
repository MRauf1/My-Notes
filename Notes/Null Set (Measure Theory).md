---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!info] Null Set[^1]
> If $(X, \mathcal{M}, \mu)$ is a [[Measure Space]], a set $E \in \mathcal{M}$ with $\mu(E) = 0$ is a null set (or $\mu$-null set).

Not to be confused with the empty set: a null set is "negligible" for $\mu$ but may be large, even uncountable (the [[Cantor Set]] is a Lebesgue null set of cardinality $\mathfrak{c}$).

# Properties
- Any countable union of null sets is null, by subadditivity ([[Measure Basic Properties]]).[^1]
- A measurable subset of a null set is null by monotonicity, but a subset of a null set need not be measurable; measures for which it always is are [[Complete Measure|complete]].
- Statements failing only on a null set hold [[Almost Everywhere]].
- Every countable subset of $\mathbb{R}$ is a [[Lebesgue Measure|Lebesgue]] null set; a nonempty open set never is.

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=39&annotation=CQLV3T4J)
