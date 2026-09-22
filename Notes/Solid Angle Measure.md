---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Solid Angle Measure[^1]
> The measure $\sigma$ that assigns to a set of directions its solid angle; used to integrate over directions in three dimensions. One direction is a point on $\mathbb{S}^2$; a set of directions is a patch on it, and the patch's solid angle is the area it covers on the unit sphere — steradians, $4\pi$ for all directions, $2\pi$ for a hemisphere.

On a sphere of radius $r$, the patch subtended by $d\theta, d\phi$ has area $dA = (r\,d\theta)(r\sin\theta\,d\phi) = r^2\sin\theta\,d\theta\,d\phi$ in only one of its two dimensions, so
$$
\begin{align}
d\sigma = dA/r^2 = \sin\theta\,d\theta\,d\phi
\end{align}
$$
Dividing by $r^2$ is what makes it an angle rather than an area: on a sphere twice as big, the same set of directions covers four times the area, and $dA/r^2$ is unchanged.

# Properties
- An instance of a [[Measure (Measure Theory)|measure]].
- The $\sin\theta$ factor is the Jacobian used directly in [[BSDF Importance Sampling]].

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
