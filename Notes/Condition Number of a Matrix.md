---
tags:
  - mathematics
  - linear_algebra
  - numerical_analysis
---

# Definition
> [!info] Definition 1 (Condition Number of a Matrix)[^1]
> The condition number of an invertible matrix $A \in M_n(\mathbb{C})$ is
> $$
> \kappa(A) = \lVert A \rVert_{op} \lVert A^{-1} \rVert_{op}
> $$

This is a special case of the [[Relative Condition Number]], specialized to the problem of solving the linear system $Ax = b$ using the [[Operator Norm]] of $A$ and $A^{-1}$.

> [!abstract] Theorem 2 (Condition Number is at Least 1)[^1]
> $\kappa(A) \geq 1$ for every invertible $A \in M_n(\mathbb{C})$.

> [!abstract] Theorem 3 (Relative Error Bound)[^2]
> Suppose $A^{-1}$ is known and used to solve $Ax = b$, but there is some error $h \in \mathbb{C}^n$ in $b$, i.e. the system actually solved is $Ay = b + h$. Then
> $$
> \frac{\lVert A^{-1} h \rVert}{\lVert x \rVert} \leq \kappa(A) \frac{\lVert h \rVert}{\lVert b \rVert}
> $$
> That is, the condition number of $A$ bounds the relative error in the computed solution in terms of the relative error in the input $b$.

The error in the computed solution is $A^{-1}h$, and its size can be bounded directly using the [[Operator Norm]] of $A^{-1}$: $\lVert A^{-1} h \rVert \leq \lVert A^{-1} \rVert_{op} \lVert h \rVert$. The operator norm of $A^{-1}$ tells us how an error of a given size in $b$ propagates to an error in the solution of $Ax = b$.

# Properties
- [[Relative Condition Number]]
- [[Operator Norm]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=294)
[^2]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=295)
