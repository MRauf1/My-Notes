---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!info] Measurable Space[^1]
> If $X$ is a [[Set]] and $\mathcal{M} \subseteq \mathcal{P}(X)$ is a [[Sigma-Field|$\sigma$-algebra]], the pair $(X, \mathcal{M})$ is a measurable space. The sets in $\mathcal{M}$ are called **measurable sets**.

"Measurable" means the space is equipped to carry a measure: $\mathcal{M}$ specifies which subsets are allowed to be measured, before any particular measure is chosen. $X$ may be countable or uncountable. Every set carries $\sigma$-algebras admitting well-defined measures (e.g. $\{\emptyset, X\}$, the [[Countable-Cocountable Sigma-Algebra]], or on $\mathbb{R}^n$ the [[Borel Sigma-Algebra]]); what fails for uncountable $X$ is only the combination of measuring *every* subset with a translation-invariant, countably additive length ([[Banach-Tarski Paradox]], [[Vitali Set]]).

# Properties
- For countable $X$, the usual choice $\mathcal{M} = \mathcal{P}(X)$ always works: any weights $f(x) \geq 0$ give the measure $\mu(E) = \sum_{x \in E} f(x)$.
- Adding a [[Measure (Measure Theory)|measure]] $\mu$ on $\mathcal{M}$ gives a [[Measure Space]] $(X, \mathcal{M}, \mu)$.
- The analogue in probability is a [[Sample Space]] with its [[Event|events]].

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=38&annotation=FXJPYTDK)
