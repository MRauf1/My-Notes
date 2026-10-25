---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!info] $F_\sigma$ Set[^1]
> An $F_\sigma$ set is a countable [[Set Union|union]] of [[Closed Set|closed sets]]:
> $$
> \begin{align}
> H = \bigcup_{j=1}^{\infty} F_j, \qquad F_j \text{ closed}.
> \end{align}
> $$
> A countable intersection of $F_\sigma$ sets is an $F_{\sigma\delta}$ set, and so on.

$F$ comes from the French *fermé* (closed); $\sigma$ from the German *Summe* (union).

# Properties
- Complements of $F_\sigma$ sets are exactly the [[G-Delta Set|$G_\delta$ sets]] ([[DeMorgan's Laws]]).
- Every $F_\sigma$ set is a Borel set ([[Borel Sigma-Algebra]]).
- Every countable subset of $\mathbb{R}$ (e.g. $\mathbb{Q}$) is $F_\sigma$, as a countable union of singletons.
- Every Lebesgue–Stieltjes measurable set is an $F_\sigma$ set plus a null set ([[Lebesgue-Stieltjes Measure Regularity]]).

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=35&annotation=UIGUQAM6)
