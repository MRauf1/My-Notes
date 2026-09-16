---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!abstract] Lemma 1 (Existence of Maximizer)[^1]
> Let $V$ and $W$ be finite-dimensional [[Inner Product Space]]s, and let $T \in \mathcal{L}(V, W)$. Then there is a vector $u \in V$ with $\lVert u \rVert = 1$ such that $\lVert Tv \rVert \leq \lVert Tu \rVert$ whenever $v \in V$ and $\lVert v \rVert = 1$.

> [!info] Definition 2 (Operator Norm)[^2]
> Let $V$ and $W$ be finite-dimensional [[Inner Product Space]]s, and let $T \in \mathcal{L}(V, W)$. The operator norm (also called the spectral norm) of $T$ is
> $$
> \lVert T \rVert_{op} := \max_{v \in V, \, \lVert v \rVert = 1} \lVert Tv \rVert
> $$
> Lemma 1 guarantees this maximum is attained, so the operator norm is well-defined.

> [!info] Definition 3 (Operator Norm of a Matrix)[^3]
> If $A \in M_{m,n}(\mathbb{F})$, the operator norm (also called the spectral norm or induced norm, often denoted $\lVert A \rVert_2$) of $A$ is the operator norm of the [[Linear Map]] in $\mathcal{L}(\mathbb{F}^n, \mathbb{F}^m)$ whose matrix is $A$:
> $$
> \lVert A \rVert_{op} = \max_{v \in \mathbb{F}^n, \, \lVert v \rVert = 1} \lVert Av \rVert
> $$

An equivalent formulation of Definition 2/3 is that $\lVert T \rVert_{op}$ is the smallest number $C$ such that
$$
\lVert Tv \rVert \leq C \lVert v \rVert
$$
for every $v \in V$ (compare [[Linear Map Norm Continuity]]). Lemma 1 says there is at least one unit vector $v$ for which equality holds for $C = \lVert T \rVert_{op}$.

> [!abstract] Theorem 4 (Operator Norm is a Norm)[^4]
> Let $V$ and $W$ be finite-dimensional [[Inner Product Space]]s. Then the operator norm is a [[Normed Space|norm]] on $\mathcal{L}(V, W)$.

> [!abstract] Theorem 5 (Sub-multiplicativity)[^5]
> The operator norm of composed linear maps/matrices $A$ and $B$ satisfies
> $$
> \lVert AB \rVert_{op} \leq \lVert A \rVert_{op} \cdot \lVert B \rVert_{op}
> $$

# Properties
- [[Frobenius Norm]]
- [[Eigenvalue Bound by Operator Norm]]
- [[Rank-1 Matrix Operator Norm]]
- [[Operator Norm and Frobenius Norm Inequality]]
- [[Condition Number of a Matrix]]
- [[Unitary Matrix Norm]]
- [[Unitarily Invariant Norm]]
- [[Singular Value]]
- [[Low-Rank Matrix Approximation Theorem]]
- [[Adjoint]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=290)
[^2]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=291)
[^3]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=292)
[^4]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=291)
[^5]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=291)
