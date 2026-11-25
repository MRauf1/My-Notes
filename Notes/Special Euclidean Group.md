---
tags:
  - mathematics
  - abstract_algebra
  - cryoEM
---

# Definition
> [!info] Special Euclidean Group $SE(n)$[^1]
> The [[Group]] of orientation-preserving [[Rigid-Body Transformation|rigid-body transformations]] of $\mathbb{R}^n$. Its elements are pairs $g = (R, t)$ with $R \in SO(n)$ (the [[Group of Special Orthogonal Matrices]]) and $t \in \mathbb{R}^n$, acting by
> $$
> \begin{align}
> g \cdot x &= Rx + t, \\
> (R_2, t_2)(R_1, t_1) &= (R_2 R_1,\; R_2 t_1 + t_2).
> \end{align}
> $$
> Equivalently, $SE(n) \cong \mathbb{R}^n \rtimes SO(n)$, a [[Semidirect Product Group|semidirect product]] in which $SO(n)$ acts on translations by $R \cdot t = Rt$.

$R$ is the rotation part and $t$ the translation part. Together they form a **pose**: an element of $SE(3)$ fixes both the orientation and the position of a rigid object ([[Particle Pose]]).

# Properties
- Inverse: $(R, t)^{-1} = (R^{\top}, -R^{\top} t)$.
- In [[Homogeneous Coordinates]], $g$ is the matrix $\begin{pmatrix} R & t \\ 0 & 1 \end{pmatrix}$, and composition is matrix multiplication.
- It acts on functions (e.g. densities) by $(g \cdot f)(x) = f\big(g^{-1} \cdot x\big) = f\big(R^{\top}(x - t)\big)$.
- It is a Lie group of dimension $n(n+1)/2$: $6$ for $n = 3$, made of $3$ rotational and $3$ translational degrees of freedom.

[^1]: [Euclidean group (Wikipedia)](https://en.wikipedia.org/wiki/Euclidean_group)
