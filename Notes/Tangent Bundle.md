---
tags:
  - mathematics
  - differential_geometry
---

# Definition
> [!info] Tangent Bundle[^1]
> The tangent bundle $TM$ of a space $M$ is the set of all [[Tangent Vector|tangent vectors]] at all points of $M$:
> $$\begin{align}
> TM = \bigsqcup_{p \in M} T_p M = \{(p, X) : p \in M,\ X \in T_p M\}
> \end{align}$$
> where $T_p M$ is the [[Tangent Space]] at $p$.

A [[Vector Field]] on $M$ is a choice of one tangent vector at every point, i.e. a (smooth) map $X: M \rightarrow TM$ with $X(p) \in T_pM$ (a *section* of $TM$). Expressions like $df(X)$ are used interchangeably for the pushforward of a single vector $X \in T_pM$ and of an entire vector field (a vector at every point of $M$).[^1]

# Properties
- Maps between spaces act on tangent bundles through their [[Tangent Map|differential]]: $df: TM \rightarrow TN$.
- The [[Shape Operator]] is a map $S: TM \rightarrow TM$.
- If $M$ is an $n$-dimensional [[Manifold]], $TM$ is itself a $2n$-dimensional manifold.

[^1]: [Crane, p. 29–30](zotero://open-pdf/library/items/9N6JDPI2?page=31&annotation=3VFM5YG7)
