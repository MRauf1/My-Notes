---
tags:
  - mathematics
  - linear_algebra
---

# Definition

> [!info] Definition 1 ([[Inner Product]] [[Space]])[^1]
> Let $V$ be a [[Vector Space]] over [[Field]] $\mathbb{F}$. An [[Inner Product]] is an [[Operation]] on $V$, written $\langle v, w \rangle$ such that the following properties hold:
> 1) [[Inner Product]] of 2 [[Vector]] is [[Scalar]]: For each $v, w \in V$, $\langle v, w \rangle \in \mathbb{F}$
> 2) [[Distributive Property]]: For each $u, v, w \in V$, $\langle u + v, w \rangle = \langle u, w \rangle + \langle v, w \rangle$
> 3) [[Homogeneity]]: For each $v, w \in V$ and $a \in \mathbb{F}$, $\langle av, w \rangle = a \langle v, w \rangle$
> 4) [[Symmetry]]: For each $v, w \in V$, $\langle v, w \rangle = \overline{\langle w, v \rangle}$
> 5) [[Non-Negativity]]: For each $v \in V$, $\langle v, v \rangle \geq 0$
> 6) [[Definiteness]]: If $\langle v, v \rangle = 0$, then $v = 0$
> A [[Vector Space]] with [[Inner Product]] is an Inner Product Space.

Every inner product space is a [[Normed Space]]: the norm $\lVert v \rVert = \sqrt{\langle v, v \rangle}$ induced by the inner product satisfies all of the [[Normed Space]] axioms.[^2] An Inner Product Space is thus a special case of a [[Normed Space]]; not every norm on a [[Normed Space]] comes from an inner product.

If it is also [[Complete Metric Space]], then it is [[Hilbert Space]]. In particular, all [[Finite-Dimensional Vector Space|finite-dimensional]] inner product spaces are [[Complete Metric Space]].

# Types
- [[Dot Product Space]]
- [[Frobenius Inner Product Space]]

# Properties
- [[Inner Product Basic Properties]]
- [[Pythagorean Theorem for Inner Product Space]]
- [[Cauchy-Schwarz Inequality]]
- [[Gram-Schmidt Algorithm]]
- [[Orthonormal Basis Finite-Dimensional Inner Product Space]]
- [[Bessel's Inequality]]
- [[Orthogonal Complement]]
- [[Orthogonal Direct Sum]]
- [[Orthogonal Decomposition Theorem]]
- [[Orthogonal Projection]]
- [[Orthogonal Projection Matrix]]
- [[Best Approximation Theorem]]
- [[Jordan-von Neumann Theorem]]
- [[Polarization Identity]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=246)
[^2]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=287)