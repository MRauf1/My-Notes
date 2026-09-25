---
tags:
  - mathematics
  - linear_algebra
  - computer_science
  - numerical_analysis
---

# Definition
> [!info] Definition 1 (p-Norm)[^1]
> For any $p \geq 1$, the $p$-norm on $\mathbb{R}^n$ or $\mathbb{C}^n$ is
> $$
> \lVert x \rVert_p = \left( \sum_{j=1}^n |x_j|^p \right)^{1/p}
> $$

The norm of a vector is the factor by which the corresponding unit sphere $\{x : \lVert x \rVert_p = 1\}$ must be expanded or shrunk to encompass the vector. The unit sphere is only "round" for $p = 2$.[^2]

![[Unit Spheres in p-Norms.png]]

# Types
- [[1-Norm]] ($p = 1$): $\lVert x \rVert_1 = \sum_{i=1}^n |x_i|$, also called the Manhattan norm (distance in "city blocks" in 2D).[^2]
- [[Vector Norm|2-Norm]] ($p = 2$): $\lVert x \rVert_2 = \left( \sum_{i=1}^n |x_i|^2 \right)^{1/2}$, also called the Euclidean norm (usual [[Euclidean Distance|distance]] in Euclidean space; comes from the standard [[Dot Product]]/[[Inner Product]]).[^2]
- [[Infinity Norm]] ($p = \infty$): $\lVert x \rVert_\infty = \max_{1 \leq i \leq n} |x_i|$, the limiting case $p \to \infty$.[^2]

# Properties
- Every $p$-norm is a [[Normed Space|norm]]: positive definite, absolutely homogeneous, and satisfies the [[Triangle Inequality]].
- $\lVert x \rVert_1 \geq \lVert x \rVert_2 \geq \lVert x \rVert_\infty$ for any $x \in \mathbb{R}^n$.[^3]
- All $p$-norms on $\mathbb{R}^n$ are equivalent (they differ by at most a constant depending on $n$): [[Norm Equivalence Inequalities (Finite-Dimensional)]]
- [[Induced Matrix Norm]]
- The [[Dual Norm]] of $\lVert \cdot \rVert_p$ is $\lVert \cdot \rVert_q$ with $\frac{1}{p} + \frac{1}{q} = 1$: [[Hölder's Inequality]]
- Only $p = 2$ comes from an [[Inner Product]] (the others violate the [[Parallelogram Identity]]), so the [[Cauchy-Schwarz Inequality]] only holds for $p = 2$.

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=287)
[^2]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=73)
[^3]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=74)
