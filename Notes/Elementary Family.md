---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!info] Elementary Family[^1]
> An elementary family is a collection $\mathcal{E}$ of subsets of $X$ such that
> 1. $\emptyset \in \mathcal{E}$,
> 2. $E, F \in \mathcal{E} \implies E \cap F \in \mathcal{E}$,
> 3. $E \in \mathcal{E} \implies E^c$ is a finite [[Disjoint Set Union|disjoint union]] of members of $\mathcal{E}$.

The abstraction of "simple building blocks" such as intervals or rectangles: intersecting two blocks gives a block, and the complement of a block can be tiled by finitely many blocks.

# Properties
> [!abstract] Proposition 1.7[^2]
> If $\mathcal{E}$ is an elementary family, the collection $\mathcal{A}$ of finite disjoint unions of members of $\mathcal{E}$ is an [[Algebra of Sets|algebra]].

- The h-intervals $(a, b]$, $(a, \infty)$, $\emptyset$ in $\mathbb{R}$ form an elementary family; the resulting algebra carries the [[Premeasure]] that builds every [[Lebesgue-Stieltjes Measure]].[^3]
- Measurable rectangles $A \times B$ form an elementary family, used for product measures.

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=36&annotation=IJDRCSEZ)
[^2]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=36&annotation=LDPWSTFV)
[^3]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=46&annotation=HSZIAKC2)
