---
tags:
  - mathematics
  - discrete_mathematics
  - topology
---

# Definition

> [!info] Definition 1 (Strict [[Total Order]])[^1]
> A [[Relation]] $R$ is a strict total order if it is a [[Strict Partial Order]] and satisfies [[Trichotomy]]: for all $x, y \in A$, $xRy \lor yRx \lor x = y$.

> [!info] Definition 2 (Order Relation / Simple Order / Linear Order)[^2]
> A [[Relation]] $C$ on a [[Set]] $A$ is an order relation (simple order, linear order) if it satisfies:
> 1. (Comparability) For all $x, y \in A$ with $x \neq y$, $xCy$ or $yCx$.
> 2. (Nonreflexivity, [[Irreflexive Relation|irreflexivity]]) For no $x \in A$ does $xCx$ hold.
> 3. ([[Transitive Relation|Transitivity]]) If $xCy$ and $yCz$, then $xCz$.

# Properties
- Comparability alone does not exclude both $xCy$ and $yCx$ holding, but nonreflexivity and transitivity together do: $xCy \land yCx \implies xCx$, a contradiction. Hence for any $x, y \in A$ exactly one of $xCy$, $x = y$, $yCx$ holds, i.e. the relation is [[Antisymmetric Relation|antisymmetric]] (in fact asymmetric) and Definitions 1 and 2 coincide with [[Set Order]].
- A [[Set]] equipped with an order relation is an [[Ordered Set]]; it induces [[Open Interval in Ordered Set|open intervals]], the [[Dictionary Order]] on products, and [[Order Isomorphism|order isomorphisms]].

[^1]: [HOW TO PROVE IT: A Structured Approach, Second Edition](zotero://open-pdf/library/items/THI2Q4PN?page=218)
[^2]: [Topology (Munkres)](zotero://open-pdf/library/items/2AUACM23?page=26)
