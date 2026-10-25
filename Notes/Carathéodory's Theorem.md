---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!abstract] Theorem 1.11 (Carathéodory's Theorem)[^1]
> If $\mu^*$ is an [[Outer Measure]] on $X$, the collection $\mathcal{M}$ of [[Carathéodory Measurable Set|$\mu^*$-measurable sets]] is a [[Sigma-Field|$\sigma$-algebra]], and the restriction of $\mu^*$ to $\mathcal{M}$ is a [[Complete Measure|complete measure]].

The fundamental step from outer measures to measures: the Carathéodory criterion filters out the badly behaved subsets (such as the [[Vitali Set]]), leaving a $\sigma$-algebra on which subadditivity upgrades to countable additivity.

# Properties
- Applied to the outer measure induced by a [[Premeasure]], it yields the [[Carathéodory Extension Theorem]].
- Produces [[Lebesgue Measure]] and every [[Lebesgue-Stieltjes Measure]] from length-type premeasures on intervals.
- Completeness is automatic: if $\mu^*(N) = 0$, then every subset of $N$ is $\mu^*$-measurable.

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=42&annotation=NN92FB9E)
