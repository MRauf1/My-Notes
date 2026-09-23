---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!abstract] Theorem 1 (Theorem 6.28 -- Cramer's Rule)[^1]
> Suppose $A \in M_n(\mathbb{F})$, $\det A \neq 0$, and $b \in \mathbb{F}^n$. For $i = 1, \dots, n$, define $A_i$ to be the $n \times n$ matrix obtained from $A$ by replacing its $i$th column with $b$. Then the unique solution of the $n \times n$ [[Linear System of Equations|linear system]] $Ax = b$ is given by
> $$
> x_i = \frac{\det A_i}{\det A}
> $$
> for each $i = 1, \dots, n$.

Cramer's rule should be avoided for solving linear systems in practice. It is astronomically expensive for full matrices of nontrivial size and is useful mostly as a theoretical tool; use [[LU Decomposition]] instead.[^2]

# Properties
- [[Determinant]]
- [[Linear System of Equations]]
- [[Determinant Invertible Matrix Theorem]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=390)
[^2]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=99)
