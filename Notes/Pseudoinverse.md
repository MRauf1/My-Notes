---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!info] Definition 1 (Pseudoinverse)[^1]
> Let $A = U \Sigma V^*$ be a [[Singular Value Decomposition Theorem|singular value decomposition]] of $A \in M_{m,n}(\mathbb{C})$ with $\text{rank}(A) = r$. The pseudoinverse $A^\dagger \in M_{n,m}(\mathbb{C})$ of $A$ is
> $$
> A^\dagger = V \Sigma^\dagger U^*
> $$
> where $\Sigma^\dagger \in M_{n,m}(\mathbb{R})$ has $(j,j)$ entry $\frac{1}{\sigma_j}$ for $1 \leq j \leq r$, and all other entries $0$.

> [!abstract] Theorem 2 (Exercise 5.2.15a -- Reduces to [[Matrix Inverse]] When Invertible)[^2]
> If $A$ is invertible, then $A^\dagger = A^{-1}$.

> [!abstract] Theorem 3 (Exercise 5.2.15b -- $\Sigma\Sigma^\dagger$ and $\Sigma^\dagger\Sigma$)[^2]
> $\Sigma \Sigma^\dagger \in M_m(\mathbb{R})$ is the diagonal matrix with $1$ in the first $r$ diagonal entries and $0$ elsewhere, and $\Sigma^\dagger \Sigma \in M_n(\mathbb{R})$ is the diagonal matrix with $1$ in the first $r$ diagonal entries and $0$ elsewhere.

> [!abstract] Theorem 4 (Exercise 5.2.15c -- $AA^\dagger$ and $A^\dagger A$ are Self-Adjoint)[^2]
> $(AA^\dagger)^* = AA^\dagger$ and $(A^\dagger A)^* = A^\dagger A$.

Theorem 3 identifies $\Sigma \Sigma^\dagger$ and $\Sigma^\dagger \Sigma$ as [[Orthogonal Projection Matrix|orthogonal projection matrices]] onto the span of the first $r$ standard basis vectors, and combined with $U, V$ being [[Unitary Matrix|unitary]], Theorem 4 confirms that $AA^\dagger$ and $A^\dagger A$ are themselves orthogonal projection matrices: $AA^\dagger$ projects onto the column space of $A$, and $A^\dagger A$ projects onto the [[Orthogonal Complement]] of its kernel.

> [!abstract] Theorem 5 (Exercise 5.2.15d -- Moore-Penrose Conditions)[^2]
> $AA^\dagger A = A$ and $A^\dagger A A^\dagger = A^\dagger$.

# Properties
- [[Singular Value Decomposition Theorem]]
- [[Matrix Inverse]]
- [[Matrix Conjugate Transpose]]
- [[Orthogonal Projection Matrix]]
- [[Unitary Matrix]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=330)
[^2]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=330)
