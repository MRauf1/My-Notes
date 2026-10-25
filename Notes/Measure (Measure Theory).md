---
tags:
  - computer_science
  - monte_carlo_methods
  - mathematics
  - measure_theory
---

# Definition
> [!info] Measure[^1]
> Given a set $\Gamma$, a measure $\mu$ is a function assigning a "size" to (measurable) subsets of $\Gamma$, satisfying for measurable $A, B \subseteq \Gamma$:
> $$
> \begin{align}
> \mu(A) \geq 0, \qquad \mu(A \cup B) = \mu(A) + \mu(B) \text{ if } A \cap B = \emptyset, \qquad \mu(\emptyset) = 0
> \end{align}
> $$

A [[Probability Space|probability measure]] $P$ is a measure with $P(\Omega) = 1$.

> [!info] Measure (Rigorous Definition)[^2]
> Let $X$ be a set equipped with a [[Sigma-Field|$\sigma$-algebra]] $\mathcal{M}$. A measure on $\mathcal{M}$ (or on $(X, \mathcal{M})$) is a function $\mu : \mathcal{M} \to [0, \infty]$ such that
> 1. $\mu(\emptyset) = 0$,
> 2. **(countable additivity)** if $\{E_j\}_1^\infty$ is a sequence of [[Disjoint Sets|disjoint]] sets in $\mathcal{M}$, then
> $$
> \begin{align}
> \mu\left(\bigcup_{j=1}^\infty E_j\right) = \sum_{j=1}^\infty \mu(E_j).
> \end{align}
> $$

Countable additivity implies finite additivity (take $E_j = \emptyset$ for $j > n$); a set function with only finite additivity is a [[Finitely Additive Measure]].[^3] The finite-additivity condition above is thus weaker than what a measure actually requires. The triple $(X, \mathcal{M}, \mu)$ is a [[Measure Space]].

A measure differs from an [[Outer Measure]] (defined on every subset, only countably *sub*additive) and from a [[Premeasure]] (defined on an [[Algebra of Sets|algebra]], additive only when the countable union stays in the algebra). The standard pipeline is premeasure $\to$ outer measure $\to$ measure ([[Carathéodory Extension Theorem]]).

# Types
- [[Finite Measure]], [[Sigma-Finite Measure]], [[Semifinite Measure]] — by "size".
- [[Complete Measure]], [[Saturated Measure]].
- [[Counting Measure]], [[Dirac Measure]].
- [[Lebesgue-Stieltjes Measure]] on $\mathbb{R}$, built from an increasing right-continuous function.
- [[Borel Measure]] $\mu_B$ — length of $[a,b)$; used for 1D integrals.
- [[Lebesgue Measure]] $\lambda$ — volume of a box; used on $\mathbb{R}^d$ and PDE domains.
- [[Area Measure]] $A$ — surface area; used on boundaries $\partial\Omega$ and scene geometry.
- [[Solid Angle Measure]] $\sigma$ — a set of directions; used for directions in 3D.
- [[Walk Space Measure]] $\mu_{\text{walk}}$ — product of area measures; used for random walks of any length.

# Properties
- [[Measure Basic Properties]]: monotonicity, subadditivity, continuity from below and above.
- Sets of measure zero are [[Null Set (Measure Theory)|null sets]]; statements holding off a null set hold [[Almost Everywhere]].
- Underlies the [[Lebesgue Integral (Measure Theory)|Lebesgue integral]] $I = \int_\Gamma f\,d\mu$: no coordinates, dimension, or smoothness required.

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
[^2]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=37&annotation=JZEQ8JKP)
[^3]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=38&annotation=LSYGIRKP)
