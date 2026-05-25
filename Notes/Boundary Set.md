---
tags: mathematics, real_analysis
---

# Definition

> [!info] Definition 1 (Boundary Set)[^1]
> Boundary of [[Set]] $E$ is the [[Set]] $E^- \setminus E^{\circ}$, where $E^-$ is [[Closure Set]] and $E^{\circ}$ is [[Interior Set]].
> [[Point]] in this [[Set]] are called boundary points.

Boundary of $[a, b]$ and $(a, b)$ is both $\{a, b\}$.

> [!info] Definition 2 (Boundary of [[Set]])
> Given a [[Set]] $S$, 
> $$
> \begin{align}
> \partial S = \{z \in S | \forall \epsilon > 0, B(z, \epsilon) \cap S \neq \emptyset \land B(z, \epsilon) \cap S^C \neq \emptyset\}
> \end{align}
> $$
> where $B(z, \epsilon)$ is the [[Epsilon Neighborhood]] of [[Point]] $z$

Any neighborhood of $z$ contains points in $S$ and points not in $S$.

# Properties
- [[Boundary Set Basic Properties]]

[^1]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=100)