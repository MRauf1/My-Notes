---
tags:
  - computer_science
  - numerical_analysis
---

# Definition
> [!info] Definition 1 (Householder Transformation)[^1]
> A Householder transformation (elementary reflector) is a matrix of the form
> $$
> \begin{align}
> H = I - 2\frac{vv^T}{v^Tv}
> \end{align}
> $$
> where $v$ is a nonzero vector (the Householder vector). It satisfies $H = H^T = H^{-1}$, so $H$ is both [[Orthogonal Matrix|orthogonal]] and symmetric.

> [!abstract] Theorem 2 (Annihilating All but the First Component)[^2]
> Given a vector $a$, choose
> $$
> \begin{align}
> v = a - \alpha e_1, \qquad \alpha = -\operatorname{sign}(a_1) \lVert a \rVert_2
> \end{align}
> $$
> Then $Ha = \alpha e_1 = [\alpha, 0, \dots, 0]^T$.

From $\alpha e_1 = Ha = a - 2v\frac{v^Ta}{v^Tv}$ we get $v = (a - \alpha e_1)\frac{v^Tv}{2v^Ta}$; the scalar factor cancels in the formula for $H$, so $v = a - \alpha e_1$. Norm preservation forces $\alpha = \pm \lVert a \rVert_2$, and the sign is chosen opposite to $a_1$ to avoid [[Catastrophic Cancellation|cancellation]] in computing $v_1 = a_1 - \alpha$. To avoid unnecessary [[Overflow Level|overflow]] or [[Underflow Level|underflow]] when computing $\lVert a \rVert_2$, first divide $a$ by its component of largest magnitude; this does not change $H$.[^2]

Geometrically, $H$ reflects $a$ across one of the two hyperplanes $\operatorname{span}(v)^\perp = \{x : v^Tx = 0\}$ bisecting the angles between $a$ and the first coordinate axis, sending it to $\pm\lVert a \rVert_2 e_1$. With the [[Projector|orthogonal projector]] $P = vv^T/(v^Tv)$ onto $\operatorname{span}(v)$, $(I - P)a$ projects $a$ onto the hyperplane, and going twice as far gives $(I - 2P)a$, i.e., $H = I - 2P$. Either hyperplane works in exact arithmetic, but numerically one should choose the sign of $\alpha$ giving the point on the axis *farther* from $a$.[^3]

![[Householder Transformation as Reflection.png]]

> [!abstract] Theorem 3 (Annihilating the Last $m - k$ Components)[^4]
> For $a \in \mathbb{R}^m$ partitioned as $a = \begin{bmatrix} a_1 \\ a_2 \end{bmatrix}$ with $a_1 \in \mathbb{R}^{k-1}$, $1 \leq k < m$, the Householder vector
> $$
> \begin{align}
> v = \begin{bmatrix} 0 \\ a_2 \end{bmatrix} - \alpha e_k, \qquad \alpha = -\operatorname{sign}(a_k)\lVert a_2 \rVert_2
> \end{align}
> $$
> gives an $H$ that annihilates the last $m - k$ components of $a$ and leaves the first $k-1$ unchanged.

> [!abstract] Theorem 4 (Applying $H$ Without Forming It)[^4]
> For any vector $u$,
> $$
> \begin{align}
> Hu = u - \left( 2\frac{v^Tu}{v^Tv} \right) v
> \end{align}
> $$
> which needs only $v$ and is substantially cheaper than a general matrix-vector product.

# Properties
- Introduces many zeros in a column at once, which is efficient but can be too heavy-handed when zeros must be introduced selectively; then [[Givens Rotation|Givens rotations]] are preferable.[^5]
- A reflection, i.e., an [[Orthogonal Matrix]] with $\det H = -1$ ([[Reflection]]).
- [[Householder QR Factorization]]
- [[Projector]]
- [[Orthogonal Matrix]]

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=141)
[^2]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=142)
[^3]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=143)
[^4]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=144)
[^5]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=147)
