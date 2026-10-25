---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!info] Countable-Cocountable $\sigma$-Algebra[^1]
> A subset $E$ of an ambient [[Set]] $X$ is **co-countable** if its [[Set Complement|complement]] $E^c = X \setminus E$ is [[Countable Set|countable]]. If $X$ is uncountable,
> $$
> \begin{align}
> \mathcal{A} = \{E \subseteq X : E \text{ is countable or } E^c \text{ is countable}\}
> \end{align}
> $$
> is a [[Sigma-Field|$\sigma$-algebra]], the $\sigma$-algebra of countable or co-countable sets.

The ambient set is what complements are taken in. When $X$ is uncountable, a co-countable set is necessarily uncountable (the countable complement cannot absorb the uncountability of $X$), so countable sets are the "small" sets and co-countable sets the "huge" ones. On a countable $X$ every subset is both countable and co-countable, so the notion is trivial there.

A co-countable set is uncountable but structurally simple: it is $X$ minus a countable list of points. Unlike the [[Vitali Set]], nothing about it conflicts with countable additivity.

# Properties
- Closed under countable unions: $\bigcup_1^\infty E_j$ is countable if all $E_j$ are countable and co-countable otherwise.[^1]
- Every cofinite set (finite complement) is co-countable.
- On it, $\mu(E) = 0$ for countable $E$ and $\mu(E) = 1$ for co-countable $E$ defines a [[Measure (Measure Theory)|measure]].[^2]
- Coarser than the [[Borel Sigma-Algebra]] on $\mathbb{R}$: every countable set is Borel, but e.g. $[0,1]$ is neither countable nor co-countable.

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=34&annotation=53BKVY63)
[^2]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=38&annotation=HSNV8GAD)
