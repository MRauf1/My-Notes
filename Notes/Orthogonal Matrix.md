---
tags:
  - mathematics
  - abstract_algebra
---

# Definition

> [!info] Definition 1 (Orthogonal Matrix)
> [[Matrix|Matrix]] $P$ is orthogonal if
> $$
> \begin{align}
> P^T P = I
> \end{align}
> $$
> Equivalently,
> - $P P^T = I$
> - [[Column Vector|Columns]] of $P$ are an [[Orthonormal Basis|orthonormal basis]] of $R^n$
> - [[Row Vector|Rows]] of $P$ are an [[Orthonormal Basis|orthonormal basis]] of $R^n$

The [[Set|set]] of all special orthogonal matrices is $O(n) = \{P \in M_n(\mathbb{R}) | P\ \text{is orthogonal})\} \subseteq GL_n(\mathbb{R})$.

The complex analogue of an orthogonal matrix is a [[Unitary Matrix]] ($A^*A = I$), which coincides with the orthogonal condition when $A$ is real, since $A^* = A^T$ in that case.

All length-preserving linear transformations of $\mathbb{R}^2$ (i.e. all $2\times 2$ orthogonal matrices) are combinations of a [[Rotation Matrix|rotation]] and a reflection: every such map is either a single rotation, or a reflection across the $x$-axis followed by a rotation.

> [!abstract] Theorem 2 (Preservation of the Euclidean Norm)[^1]
> An orthogonal $Q$ preserves the Euclidean norm of every vector:
> $$
> \begin{align}
> \lVert Qv \rVert_2^2 = (Qv)^TQv = v^TQ^TQv = v^Tv = \lVert v \rVert_2^2
> \end{align}
> $$
> Hence multiplying both sides of a [[Linear Least Squares Problem|linear least squares problem]] by an orthogonal matrix leaves its solution unchanged.

Because they preserve norms, orthogonal transformations do not amplify error, so they can, e.g., solve square linear systems without [[Pivoting|pivoting]] for stability. However, orthogonalization methods are significantly more expensive than [[Gaussian Elimination]]-based ones, so the better numerics may or may not be worth the price.[^2]

# Properties

- $P^{-1} = P^T$
- [[Householder Transformation]] (reflections)
- [[Givens Rotation]] (rotations)
- [[QR Decomposition]]
- [[Unitary Matrix]]
- [[Special Orthogonal Matrix]]

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=139)
[^2]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=140)
