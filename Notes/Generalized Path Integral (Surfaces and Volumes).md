---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Generalized Path Integral (Surfaces and Volumes)[^1]
> Extends the [[Path Integral (Light Transport)|path integral]] to let vertices lie on a surface $\mathcal{M}$ or in a volume $\mathcal{V}$; everything else is unchanged. The measure becomes a product of area and volume measures, so within a single length $N$ the dimension is still not fixed — each vertex contributes 2 or 3 dimensions, and $\Omega_N$ becomes a union of its own. Per vertex: $f_s$ on a surface, $\mu_s f_p$ in the volume. Per segment, $G$ picks up transmittance and drops a cosine at any volume endpoint:
> $$
> \begin{align}
> \hat{G}(x\leftrightarrow y) = V(x\leftrightarrow y)\,\mathcal{T}(x\leftrightarrow y)\,\frac{c(x)\,c(y)}{\|x-y\|^2}, \qquad c(z) = \begin{cases} |\cos\theta_z| & z \in \mathcal{M} \\ 1 & z \in \mathcal{V} \end{cases}
> \end{align}
> $$

$I = \int_\Omega f\,d\mu$ still holds — nothing in the Monte Carlo estimation story changes, which is the point of building the path integral this way.

# Properties
- Reduces to the surface-only [[Geometric Term (Light Transport)|geometric term]] $G$ when every vertex is on $\mathcal{M}$ (transmittance $\equiv 1$).

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
