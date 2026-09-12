---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!info] Definition 1 (Normed Space)[^1]
> Let $\mathbb{F}$ be either $\mathbb{R}$ or $\mathbb{C}$, and let $V$ be a [[Vector Space]] over $\mathbb{F}$. A norm on $V$ is a real-valued function on $V$, written $\lVert v \rVert$, such that the following properties hold:
> 1) Nonnegativity: For each $v \in V$, $\lVert v \rVert \geq 0$.
> 2) Definiteness: If $\lVert v \rVert = 0$, then $v = 0$.
> 3) Positive Homogeneity: For each $v \in V$ and $a \in \mathbb{F}$, $\lVert av \rVert = |a| \lVert v \rVert$.
> 4) [[Triangle Inequality]]: For each $v, w \in V$, $\lVert v + w \rVert \leq \lVert v \rVert + \lVert w \rVert$.
> A [[Vector Space]] together with a norm is a normed space.

A normed space is the general concept; an [[Inner Product Space]] is a special case of a normed space, since every inner product $\langle \cdot, \cdot \rangle$ induces a norm $\lVert v \rVert = \sqrt{\langle v, v \rangle}$ satisfying all of the properties above. However, not every norm comes from an inner product — see [[1-Norm]] and [[Infinity Norm]] for examples of norms that do not arise from any inner product (this can be verified with the [[Parallelogram Identity]]).

It is a type of [[Metric Space]]. You define the distance $d(x, y)$ between two [[Vector]] using the [[Norm]] of their difference: $d(x, y) = \Vert{}x - y\Vert{}$. They are always [[Connected Metric Space]]. If they are also [[Complete Metric Space]], then they are [[Banach Space]]. In particular, all [[Finite-Dimensional Vector Space|finite-dimensional]] normed spaces are [[Complete Metric Space]].

# Types
- [[Inner Product Space]]

# Properties
- [[Triangle Inequality]]
- [[Parallelogram Identity]]
- [[Strictly Convex Space]]
- [[Jordan-von Neumann Theorem]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=287)
