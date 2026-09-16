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

# Properties

- $P^{-1} = P^T$
- [[Unitary Matrix]]
- [[Special Orthogonal Matrix]]