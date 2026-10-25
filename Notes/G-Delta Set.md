---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!info] $G_\delta$ Set[^1]
> A $G_\delta$ set is a countable [[Set Intersection|intersection]] of [[Open Set|open sets]]:
> $$
> \begin{align}
> G = \bigcap_{j=1}^{\infty} U_j, \qquad U_j \text{ open}.
> \end{align}
> $$
> A countable union of $G_\delta$ sets is a $G_{\delta\sigma}$ set, and so on.

$\delta$ and $\sigma$ stand for the German *Durchschnitt* (intersection) and *Summe* (union); $G$ comes from *Gebiet* (open region).

# Properties
- Complements of $G_\delta$ sets are exactly the [[F-Sigma Set|$F_\sigma$ sets]] ([[DeMorgan's Laws]]).
- Every $G_\delta$ set is a Borel set ([[Borel Sigma-Algebra]]); $G_\delta, G_{\delta\sigma}, \dots$ are levels of the Borel hierarchy.
- Every Lebesgue–Stieltjes measurable set is a $G_\delta$ set minus a null set ([[Lebesgue-Stieltjes Measure Regularity]]).

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=35&annotation=UIGUQAM6)
