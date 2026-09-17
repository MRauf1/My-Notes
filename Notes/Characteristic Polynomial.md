---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!info] Definition 1 (Characteristic Polynomial)[^1]
> Let $A \in M_n(\mathbb{F})$. The polynomial $p_A(x) = \det(A - xI_n)$ is the characteristic polynomial of $A$.

This definition is motivated by the fact that $\lambda$ is an [[Eigenvalue]] of $A$ if and only if $A - \lambda I_n$ is singular, and a matrix is singular if and only if its [[Determinant]] is zero.

> [!abstract] Proposition 2 (Proposition 6.18)[^2]
> Let $A \in M_n(\mathbb{F})$. Then $\lambda \in \mathbb{F}$ is an eigenvalue of $A$ if and only if $p_A(\lambda) = 0$.

So the eigenvalues of $A$ are exactly the roots of its characteristic polynomial.

> [!abstract] Proposition 3 (Proposition 6.19)[^3]
> $p_A(x)$ is a polynomial of degree $n$, with leading term $(-x)^n$.

> [!abstract] Proposition 4 (Proposition 6.20)[^4]
> If $A \in M_n(\mathbb{F})$ has $n$ distinct eigenvalues $\lambda_1, \dots, \lambda_n$, then
> $$
> p_A(x) = \prod_{j=1}^n (\lambda_j - x)
> $$

Some algorithms for computing the roots of a polynomial $p(x)$ actually run this correspondence in reverse: they construct a matrix $A$ whose characteristic polynomial is $p(x)$, then compute the eigenvalues of $A$ by other numerical means.[^5]

> [!abstract] Proposition 5 (Proposition 6.25 -- Coefficients Give Trace and Determinant)[^6]
> If $A \in M_n(\mathbb{F})$, the coefficient of $x^{n-1}$ in $p_A(x)$ is $(-1)^{n-1} tr(A)$, and the constant term of $p_A(x)$ is $\det(A)$.

# Properties
- [[Eigenvalue]]
- [[Algebraic Multiplicity of Eigenvalue]]
- [[Similar Matrix Characteristic Polynomial]]
- [[Cayley-Hamilton Theorem]]
- [[Trace]]
- [[Determinant]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=378)
[^2]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=378)
[^3]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=378)
[^4]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=379)
[^5]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=379)
[^6]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=382)
