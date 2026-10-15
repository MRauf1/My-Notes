---
tags:
  - mathematics
  - differential_geometry
---

# Definition
> [!info] Topological Disk[^1]
> A topological disk is any shape obtainable by continuously deforming the unit disk $D^2 = \{x \in \mathbb{R}^2 : \|x\| \le 1\}$ in the plane without tearing it, puncturing it, or gluing its edges together; i.e., any space homeomorphic to $D^2$ (or to the open disk, when used as a neighborhood).

**Dimension.** The disk is intrinsically **2-dimensional**: it is the local model for *surfaces* (2-[[Manifold|manifolds]]), regardless of whether the surface sits in $\mathbb{R}^3$ or elsewhere. It is not specific to "3D manifolds". The general $n$-dimensional version is the **topological $n$-ball**: a space homeomorphic to
$$\begin{align}
B^n = \{x \in \mathbb{R}^n : \|x\| < 1\},
\end{align}$$
and an $n$-manifold is a space in which every point has a neighborhood that is a topological $n$-ball ($B^n \cong \mathbb{R}^n$). Special cases: $B^1$ is an open interval (curves), $B^2$ is the disk (surfaces), $B^3$ is a solid ball (volumes). Combinatorially, this matches the [[Simplicial Manifold]] condition: the star of each vertex is a combinatorial $n$-ball, equivalently its link is a simplicial $(n-1)$-sphere (the boundary of the ball).

# Properties
- Every point of a surface has a small neighborhood that is a topological disk; this is the most basic sense in which a surface "looks like" Euclidean space.[^2]
- In a [[Simplicial Surface]], the closed star of every interior vertex is a combinatorial disk made of triangles.

[^1]: [Crane, p. 8](zotero://open-pdf/library/items/9N6JDPI2?page=9&annotation=JJ7SBX7I)
[^2]: [Crane, p. 8](zotero://open-pdf/library/items/9N6JDPI2?page=9&annotation=C6E3JGS5)
