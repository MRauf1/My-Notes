---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Walk on Spheres[^1]
> To solve the Laplace equation $\Delta u = 0$ on $\Omega$ with Dirichlet boundary data $u = g$ on $\partial\Omega$ at a point $x_0$: repeatedly jump from $x_k$ to a uniformly random point $x_{k+1}$ on the largest sphere $S(x_k, r_k)$ centered at $x_k$ and contained in $\Omega$, $r_k = \operatorname{dist}(x_k, \partial\Omega)$, until $r_k < \epsilon$. Then
> $$
> \begin{align}
> u(x_0) \approx g(\bar{x}_K)
> \end{align}
> $$
> where $\bar{x}_K$ is the boundary point closest to the final $x_K$; averaging over walks estimates $u(x_0)$.

# Properties
- Justified by the mean value property of [[Harmonic Function|harmonic functions]], $u(x) = \frac{1}{|S(x,r)|}\int_{S(x,r)} u$, applied recursively; equivalently $u(x_0) = \mathbb{E}[g(W_\tau)]$ where $W$ is a Brownian motion from $x_0$ and $\tau$ its first exit time from $\Omega$ (Kakutani's theorem). Each jump samples exactly where Brownian motion first exits the sphere, skipping its intermediate [[Random Walk|random walk]].
- Extends to the Poisson equation $\Delta u = f$ by adding, at each step, a Monte Carlo estimate of the source term weighted by the sphere's Green's function.
- The expected number of steps grows only like $O(\log(1/\epsilon))$, and the method needs no mesh — only a distance query to $\partial\Omega$ — much like [[Path Tracing (Recursive Estimator)|path tracing]] needs only ray queries.
- Estimates $u$ pointwise, independently at each query point.

[^1]: Monte Carlo Methods — Q&A Overview
