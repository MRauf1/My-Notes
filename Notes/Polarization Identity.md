---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!abstract] Theorem 1 (Polarization Identity)
> Let $V$ be an [[Inner Product Space]] over $\mathbb{F}$ with norm $\lVert \cdot \rVert$ induced by the [[Inner Product]]. For $v, w \in V$, the inner product can be recovered from the norm alone:
> - If $\mathbb{F} = \mathbb{R}$:
> $$
> \langle v, w \rangle = \frac{1}{4}\left(\lVert v + w \rVert^2 - \lVert v - w \rVert^2\right)
> $$
> - If $\mathbb{F} = \mathbb{C}$:
> $$
> \langle v, w \rangle = \frac{1}{4}\left(\lVert v + w \rVert^2 - \lVert v - w \rVert^2 + i \lVert v + iw \rVert^2 - i \lVert v - iw \rVert^2\right)
> $$

The complex case reduces to the real case since the imaginary terms vanish when $V$ is a real vector space. This identity is the constructive half of the [[Jordan-von Neumann Theorem]]: once a [[Normed Space]] is known to satisfy the [[Parallelogram Identity]], the polarization identity is precisely the formula that defines the inner product from which the norm must have come.

# Properties
- [[Jordan-von Neumann Theorem]]
- [[When Banach Space is Hilbert Space Theorem]]
- [[Parallelogram Identity]]
- [[Inner Product Space]]
