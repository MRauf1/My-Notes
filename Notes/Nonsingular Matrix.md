---
tags:
  - computer_science
  - numerical_analysis
---

# Definition
> [!info] Definition 1 (Nonsingular Matrix)[^1]
> An $n \times n$ [[Matrix]] $A$ is nonsingular if it satisfies any one of the following equivalent conditions:
> 1. $A$ has an inverse, i.e., there is an $n \times n$ matrix $A^{-1}$ such that $AA^{-1} = A^{-1}A = I$ (see [[Matrix Inverse]]).
> 2. $\det(A) \neq 0$ (see [[Determinant]]).
> 3. $\operatorname{rank}(A) = n$, i.e., $A$ has $n$ linearly independent rows/columns (see [[Rank]]).
> 4. For any vector $z \neq 0$, $Az \neq 0$, i.e., $A$ annihilates no nontrivial vector (its [[Kernel]] is $\{0\}$).
>
> Otherwise, $A$ is singular.

> [!abstract] Theorem 2 (Solutions of a Square Linear System)[^1]
> - If $A$ is nonsingular, then $Ax = b$ has the unique solution $x = A^{-1}b$ for every $b$.
> - If $A$ is singular, there is $z \neq 0$ with $Az = 0$ (by Condition 4). Hence if $x$ solves $Ax = b$, then so does $x + \gamma z$ for every scalar $\gamma$, since $A(x + \gamma z) = b$. So a consistent singular square system has infinitely many solutions, and an inconsistent one has none.

# Properties
- [[Solution of Linear System]]
- [[Determinant Invertible Matrix Theorem]]
- [[Condition Number of a Matrix]] (measures how close a nonsingular matrix is to being singular)

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=71)
