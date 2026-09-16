---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!abstract] Theorem 1 (Exercise 4.5.12a)[^1]
> If $V$ is a [[Normed Space]], $T \in \mathcal{L}(V)$ is an [[Isometry (Linear Algebra)|isometry]], and $\lambda$ is an [[Eigenvalue]] of $T$, then $|\lambda| = 1$.

> [!abstract] Theorem 2 (Exercise 4.5.12b)[^1]
> If $U \in M_n(\mathbb{C})$ is [[Unitary Matrix|unitary]] and $\lambda$ is an eigenvalue of $U$, then $|\lambda| = 1$.

Theorem 2 is a special case of Theorem 1, since a unitary matrix is the isometry of $\mathbb{C}^n$ acting on itself: if $Tv = \lambda v$ for $v \neq 0$, then $\lVert v \rVert = \lVert Tv \rVert = \lVert \lambda v \rVert = |\lambda| \lVert v \rVert$, and since $\lVert v \rVert \neq 0$, it follows that $|\lambda| = 1$.

This does not mean the only eigenvalues an isometry can have are $\pm 1$: it only forces $\lambda$ to lie on the unit circle in $\mathbb{C}$, i.e. $\lambda = e^{i\theta}$ for some $\theta$. Over $\mathbb{C}$ — e.g. for a general unitary matrix — $\lambda$ can be any point on the unit circle. The restriction to $\lambda \in \{-1, 1\}$ only arises for a **real** eigenvalue of a **real** isometry (such as an [[Orthogonal Matrix|orthogonal matrix]]), since a real number of modulus $1$ must be $\pm 1$; a real orthogonal matrix can still have genuinely complex eigenvalues, which occur in conjugate pairs $e^{\pm i \theta}$ and need not equal $\pm 1$.

# Properties
- [[Eigenvalue]]
- [[Eigenvalue Bound by Operator Norm]]
- [[Isometry (Linear Algebra)]]
- [[Unitary Matrix]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=306)
