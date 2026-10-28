---
tags:
  - mathematics
  - topology
---

# Definition
> [!info] Open Interval in Ordered Set[^1]
> Let $X$ be a [[Set]] with an order relation $<$ (a [[Strict Total Order]]) and let $a < b$. The open interval in $X$ is
> $$
> \begin{align}
> (a, b) = \{x \in X \mid a < x < b\}.
> \end{align}
> $$

> [!info] Immediate Predecessor and Immediate Successor[^1]
> If $(a, b) = \emptyset$, then $a$ is called the immediate predecessor of $b$, and $b$ is called the immediate successor of $a$.

This generalizes the open intervals of $\mathbb{R}$ (see [[Interval Notation]]) to an arbitrary [[Ordered Set]]; these intervals are the building blocks of the order topology.

# Properties
- In $\mathbb{Z}^+$, every $n$ has immediate successor $n + 1$. In $\mathbb{R}$ or $\mathbb{Q}$, no element has an immediate successor, since between any $x < y$ there is $z$ with $x < z < y$ (property (8) of a [[Linear Continuum]]).
- Immediate predecessors/successors are preserved by [[Order Isomorphism|order isomorphisms]], so they help distinguish order types.

[^1]: [Topology (Munkres)](zotero://open-pdf/library/items/2AUACM23?page=27&annotation=TF9GUDL5)
