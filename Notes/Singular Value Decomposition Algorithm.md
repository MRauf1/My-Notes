---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!abstract] Algorithm 1 (Algorithm 5.17 -- Finding an SVD)[^1]
> To find a [[Singular Value Decomposition Theorem|singular value decomposition]] of $A \in M_{m,n}(\mathbb{F})$:
> 1. Find the [[Eigenvalue|eigenvalues]] of $A^*A$. The square roots of the largest $p = \min\{m,n\}$ of them are the [[Singular Value|singular values]] $\sigma_1 \geq \dots \geq \sigma_p$ of $A$.
> 2. Find an [[Orthonormal Basis|orthonormal basis]] for each eigenspace of $A^*A$; arrange the resulting vectors $(v_1, \dots, v_n)$ so their corresponding eigenvalues are in decreasing order. Let $V$ have these as its columns.
> 3. Let $r = rank(A)$. For $1 \leq j \leq r$, define $u_j := \frac{1}{\sigma_j} Av_j$, and extend $(u_1, \dots, u_r)$ to an orthonormal basis $(u_1, \dots, u_m)$ of $\mathbb{F}^m$. Let $U$ have these as its columns.
> Then, with $\Sigma \in M_{m,n}(\mathbb{F})$ having $\sigma_j$ in position $(j,j)$ for $1 \leq j \leq p$ and $0$ elsewhere, $A = U \Sigma V^*$ is an SVD of $A$.

# Properties
- [[Singular Value Decomposition Theorem]]
- [[Singular Value]]
- [[Eigenvalue]]
- [[Orthonormal Basis]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=336)
