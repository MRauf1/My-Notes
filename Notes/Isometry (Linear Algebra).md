---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!info] Definition 1 (Isometry)[^1]
> Let $V$ and $W$ be [[Normed Space]]s. A [[Linear Map]] $T: V \to W$ is an isometry if $T$ is surjective and $\lVert Tv \rVert = \lVert v \rVert$ for every $v \in V$. If there is an isometry $T: V \to W$, then $V$ and $W$ are isometric.

Every isometry is automatically injective: if $Tv = 0$, then $\lVert v \rVert = \lVert Tv \rVert = 0$, so $v = 0$ by definiteness of the norm, i.e. $T$ has trivial kernel. Since $T$ is also surjective by definition, every isometry is a [[Bijective Function|bijective]] linear map.

> [!abstract] Theorem 2 (Lemma 4.25 -- Isometry is an Isomorphism)[^2]
> Let $V$ and $W$ be [[Normed Space]]s. If $T \in \mathcal{L}(V, W)$ is an isometry, then $T$ is a [[Linear Map Isomorphism|isomorphism]].

Since an isomorphism forces $V$ and $W$ to have the same [[Dimension]] ([[Finite-Dimensional Vector Space|finite-dimensional]] spaces must have equal dimension, and [[Infinite-Dimensional Vector Space|infinite-dimensional]] spaces must have [[Basis|bases]] of equal cardinality), there cannot be an isometry between normed spaces of different dimension: the surjectivity already built into the definition forces the map to be bijective, so two spaces of different dimension can never be isometric.

> [!abstract] Theorem 3 (Theorem 4.26 -- Isometry Preserves Inner Product)[^3]
> Let $V$ and $W$ be [[Inner Product Space]]s. A surjective [[Linear Map]] $T: V \to W$ is an isometry if and only if $\langle Tv_1, Tv_2 \rangle = \langle v_1, v_2 \rangle$ for every $v_1, v_2 \in V$.

Geometrically, a linear map between inner product spaces that preserves the lengths of vectors must also preserve the angles between them, since the angle between $v_1, v_2$ is recovered from the norm and inner product via $\cos\theta = \frac{\langle v_1, v_2 \rangle}{\lVert v_1 \rVert \lVert v_2 \rVert}$.[^4] The linear maps between inner product spaces that respect the inner product structure are thus exactly the isometries.

> [!abstract] Theorem 4 (Theorem 4.27)[^5]
> Let $V$ and $W$ be [[Inner Product Space]]s. An invertible $T \in \mathcal{L}(V, W)$ is an isometry if and only if, for each $v \in V$ and $w \in W$,
> $$
> \langle Tv, w \rangle = \langle v, T^{-1} w \rangle
> $$

This condition says precisely that $T^{-1} = T^*$, the [[Adjoint]] of $T$.

> [!abstract] Theorem 5 (Theorem 4.28)[^6]
> Suppose $V$ and $W$ are [[Inner Product Space]]s and $(e_1, \dots, e_n)$ is an [[Orthonormal Basis]] of $V$. Then $T \in \mathcal{L}(V, W)$ is an isometry if and only if $(Te_1, \dots, Te_n)$ is an [[Orthonormal Basis]] of $W$.

> [!abstract] Theorem 6 (Corollary 4.29)[^7]
> Let $V$ and $W$ be [[Finite-Dimensional Vector Space|finite-dimensional]] [[Inner Product Space]]s. Then $V$ and $W$ are isometric if and only if $\dim V = \dim W$.

# Properties
- [[Linear Map Isomorphism]]
- [[Unitary Matrix]]
- [[Isometry Eigenvalue Modulus Theorem]]
- [[Singular Value]]
- [[Adjoint]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=296)
[^2]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=297)
[^3]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=297)
[^4]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=298)
[^5]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=298)
[^6]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=298)
[^7]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=300)
