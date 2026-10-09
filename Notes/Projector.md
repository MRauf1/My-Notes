---
tags:
  - computer_science
  - numerical_analysis
---

# Definition
> [!info] Definition 1 (Projector)[^1]
> A square matrix $P$ is a projector if it is idempotent:
> $$
> \begin{align}
> P^2 = P
> \end{align}
> $$
> It projects any vector onto the subspace $\operatorname{span}(P)$, and leaves unchanged any vector already in that subspace.

> [!info] Definition 2 (Orthogonal Projector)[^1]
> A projector $P$ that is also symmetric ($P^T = P$) is an orthogonal projector.

> [!abstract] Theorem 3 (Complementary Projector)[^1]
> If $P$ is an orthogonal projector, then $P_\perp = I - P$ is an orthogonal projector onto the [[Orthogonal Complement]] $\operatorname{span}(P)^\perp$, and every $v \in \mathbb{R}^m$ splits into mutually orthogonal pieces
> $$
> \begin{align}
> v = (P + (I - P))v = Pv + P_\perp v, \qquad Pv \in \operatorname{span}(P),\ P_\perp v \in \operatorname{span}(P)^\perp
> \end{align}
> $$

> [!abstract] Theorem 4 (Explicit Orthogonal Projectors onto $\operatorname{span}(A)$)[^2]
> 1. If $A \in \mathbb{R}^{m \times n}$ has full column rank, then $P = A(A^TA)^{-1}A^T$ is an orthogonal projector onto $\operatorname{span}(A)$.
> 2. If $Q \in \mathbb{R}^{m \times n}$ has orthonormal columns ($Q^TQ = I$) spanning $\operatorname{span}(A)$, then $P = QQ^T$ is an orthogonal projector onto $\operatorname{span}(Q) = \operatorname{span}(A)$.
>
> In particular, for a nonzero vector $v$, the orthogonal projector onto $\operatorname{span}(v)$ is $P = vv^T / (v^Tv)$.

These are the matrix forms of the [[Orthogonal Projection]]; see [[Orthogonal Projection Matrix]] for the same formulas over $\mathbb{C}$. Projection onto $\operatorname{span}(A)$ is what the [[Linear Least Squares Problem|least squares solution]] computes: $y = Pb = Ax$.[^2]

# Properties
- Using 1, $P = AA^+$ with $A^+ = (A^TA)^{-1}A^T$ the [[Pseudoinverse]].[^3]
- $I - 2P$ for $P = vv^T/(v^Tv)$ is the [[Householder Transformation]] (reflection across $\operatorname{span}(v)^\perp$).[^4]
- [[Orthogonal Projection]]
- [[Orthogonal Projection Matrix]]
- [[Orthogonal Decomposition Theorem]]

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=131)
[^2]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=132)
[^3]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=134)
[^4]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=142)
