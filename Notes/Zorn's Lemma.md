---
tags:
  - mathematics
  - measure_theory
  - topology
---

# Definition
> [!info] Zorn's Lemma[^1]
> If $X$ is a [[Partial Order|partially ordered set]] and every [[Total Order|linearly ordered]] [[Subset]] of $X$ has an [[Relation Upper Bound|upper bound]], then $X$ has a maximal element, i.e. an $x \in X$ such that $x \leq y$ implies $y = x$.

The standard tool for producing "maximal" objects whose existence cannot be built by countable recursion (e.g. bases of arbitrary vector spaces, maximal ideals, Hahn–Banach extensions).

> [!info] Zorn's Lemma (Strict Partial Order Form)[^2]
> Let $A$ be a set with a [[Strict Partial Order]] $\prec$. If every simply ([[Strict Total Order|totally]]) ordered subset of $A$ has an [[Relation Upper Bound|upper bound]] in $A$, then $A$ has a [[Relation Maximal Element|maximal element]].

# Properties
- Equivalent to the [[Hausdorff Maximal Principle]], the [[Well Ordering Principle (Set Theory)|well ordering principle]], and the [[Axiom of Choice]].[^1]
- A maximal element need not be the largest element, nor unique, because $X$ is only partially ordered.

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=18&annotation=9W5I46JX)
[^2]: [Topology (Munkres)](zotero://open-pdf/library/items/2AUACM23?page=72&annotation=SWKU78IX)
