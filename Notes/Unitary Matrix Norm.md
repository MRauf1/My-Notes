---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!abstract] Theorem 1 (Exercise 4.5.14a)[^1]
> If $U \in M_n(\mathbb{C})$ is [[Unitary Matrix|unitary]], then $\lVert U \rVert_{op} = 1$.

> [!abstract] Theorem 2 (Exercise 4.5.14b)[^1]
> If $U \in M_n(\mathbb{C})$ is [[Unitary Matrix|unitary]], then $\lVert U \rVert_F = \sqrt{n}$.

Since $U$ is unitary, it is an [[Isometry (Linear Algebra)|isometry]] of $\mathbb{C}^n$: $\lVert Uv \rVert = \lVert v \rVert$ for every $v$, so the maximum defining the [[Operator Norm]] is attained at every unit vector, giving $\lVert U \rVert_{op} = 1$. For the [[Frobenius Norm]], $\lVert U \rVert_F^2 = tr(U^*U) = tr(I_n) = n$, so $\lVert U \rVert_F = \sqrt{n}$.

# Properties
- [[Operator Norm]]
- [[Frobenius Norm]]
- [[Unitary Matrix]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=307)
