---
tags:
  - mathematics
  - linear_algebra
  - computer_science
  - numerical_analysis
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

> [!info] Definition 6 (Pseudoinverse of a Full-Column-Rank Matrix)[^3]
> If $A \in \mathbb{R}^{m \times n}$ has full column rank, so that $A^TA$ is nonsingular, its pseudoinverse is
> $$
> \begin{align}
> A^+ = (A^TA)^{-1}A^T
> \end{align}
> $$
> Then $A^+A = I$, $P = AA^+$ is the [[Projector|orthogonal projector]] onto $\operatorname{span}(A)$, and the [[Linear Least Squares Problem|least squares]] solution of $Ax \cong b$ is $x = A^+b$.

> [!abstract] Theorem 7 (SVD Form Generalizes Definition 6)[^4]
> Define the pseudoinverse of a scalar $\sigma$ as $1/\sigma$ if $\sigma \neq 0$ and $0$ otherwise, and of a (possibly rectangular) diagonal matrix by transposing it and taking the scalar pseudoinverse of each entry. Then $A^+ = V\Sigma^+U^T$ (Definition 1) always exists, regardless of shape or rank; it equals $A^{-1}$ if $A$ is square and nonsingular, agrees with Definition 6 if $A$ has full column rank, and in all cases $A^+b$ is the least squares solution of $Ax \cong b$ of minimum Euclidean norm.

# Properties
- [[Linear Least Squares Problem]]
- [[Condition Number of a Matrix]] ($\operatorname{cond}(A) = \lVert A \rVert_2 \lVert A^+ \rVert_2$ for rectangular $A$)
- [[Singular Value Decomposition Theorem]]
- [[Matrix Inverse]]
- [[Matrix Conjugate Transpose]]
- [[Orthogonal Projection Matrix]]
- [[Unitary Matrix]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=330)
[^2]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=330)
[^3]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=134)
[^4]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=160)
