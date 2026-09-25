---
tags:
  - mathematics
  - differential_geometry
  - linear_algebra
---

# Definition

> [!info] Definition 1 (Cauchy-Schwarz [[Inequality]])[^1]
> For [[Vector]] $\mathbf{v}, \mathbf{w} \in \mathbb{R}^n$,
> $$
> \begin{align}
> |\mathbf{v} \cdot \mathbf{w}| \leq ||\mathbf{v}|| \cdot ||\mathbf{w}||
> \end{align}
> $$

The above is an equality if and only if one [[Vector]] is a [[Multiple]] of the other [[Vector]] (they are [[Collinear]]) — **any** scalar multiple, positive or negative, suffices, since the left side is an absolute value. This is weaker than the equality condition for the [[Triangle Inequality]], which additionally requires the multiple to be nonnegative (the vectors must point in the *same* direction).

> [!info] Definition 2 (Equality)
> For [[Vector]] $\mathbf{v}, \mathbf{w} \in \mathbb{R}^n$,
> $$
> \begin{align}
> \mathbf{v} \cdot \mathbf{w} = ||\mathbf{v}|| \cdot ||\mathbf{w}|| \cdot \cos(\theta)
> \end{align}
> $$
> where $\theta$ is the [[Angle]] between $\mathbf{v}$ and $\mathbf{w}$.

Both of the above are generalized using [[Inner Product]].

> [!info] Definition 3 (Cauchy-Schwarz Inequality in an Inner Product Space)[^2]
> Let $V$ be an [[Inner Product Space]] with induced norm $\lVert u \rVert = \sqrt{\langle u, u \rangle}$. Then for all $u, v \in V$,
> $$
> \begin{align}
> |\langle u, v \rangle| \leq \lVert u \rVert \, \lVert v \rVert
> \end{align}
> $$

Cauchy-Schwarz applies to **any** norm that is induced by an inner product — e.g. the Euclidean norm on $\mathbb{R}^n$/$\mathbb{C}^n$, the $L^2$ norm on functions, and the [[Frobenius Norm|Frobenius (Hilbert-Schmidt) norm]] on matrices/operators (see [[Frobenius Inner Product Space]]). It does **not** apply to arbitrary norms such as the $L^p$/[[p-Norm]]s with $p \neq 2$ (e.g. [[1-Norm|$L^1$]] or [[Infinity Norm|$L^\infty$]]):
- A norm is induced by an inner product iff it satisfies the [[Parallelogram Identity]]; the $p$-norms with $p \neq 2$ violate it, so no inner product exists for them and Cauchy-Schwarz cannot even be stated there.
- The naive bound $|\langle x, y \rangle| \leq \lVert x \rVert_p \lVert y \rVert_p$ (same norm on both sides) is false for $p > 2$: for $p = \infty$ and $x = y = (1, \dots, 1) \in \mathbb{R}^n$, the left side is $n$ while the right side is $1$. (For $p < 2$ it is true but not tight, since $\lVert \cdot \rVert_2 \leq \lVert \cdot \rVert_p$.)
- The correct replacement is [[Hölder's Inequality]]: $\left| \sum_i x_i y_i \right| \leq \lVert x \rVert_p \lVert y \rVert_q$ with $\frac{1}{p} + \frac{1}{q} = 1$, or for an arbitrary norm, $|\langle x, y \rangle| \leq \lVert x \rVert \, \lVert y \rVert_*$ using the [[Dual Norm]]. Cauchy-Schwarz is the case $p = q = 2$, where the norm is self-dual.

# Properties
- [[Triangle Inequality]]
- [[Hölder's Inequality]] (generalization to $p$-norms and dual norms)
- [[Parallelogram Identity]]

[^1]: [Elementary Differential Geometry](zotero://open-pdf/library/items/F6CCEWIU?page=60)
[^2]: [Cauchy–Schwarz inequality — Wikipedia](https://en.wikipedia.org/wiki/Cauchy%E2%80%93Schwarz_inequality)
