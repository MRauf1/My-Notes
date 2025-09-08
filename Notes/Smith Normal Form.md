---
tags: mathematics, abstract_algebra
---

# Definition

> [!info] Definition 1 (Smith Normal Form)
> [[Matrix]] $A \in M_{m \times n}(\mathbb{Z})$ is in Smith Normal Form if
> $$
> \begin{align}
> A = \begin{bmatrix}
> d_1 & 0 & \dots & 0 \\
> 0 & d_2 & \dots & 0 \\
> \vdots & \vdots & \vdots & \vdots \\
> 0 & 0 & \dots & d_k
> \end{bmatrix}
> \end{align}
> $$
> where $d_i \geq 0, d_i | d_{i + 1}$

Non-square [[Diagonal Matrix]] where the each diagonal term [[Divides]] the next diagonal term. All non-diagonal entries are 0.