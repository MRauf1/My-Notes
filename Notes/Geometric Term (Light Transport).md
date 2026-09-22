---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Geometric Term (Light Transport)[^1]
> Rewriting the [[Light Transport Equation|rendering-equation integral]] over points $y$ on $\mathcal{M}$ rather than over directions $\omega$ requires a change of measure from solid angle at $x$ to area at $y$:
> $$
> \begin{align}
> d\sigma(\omega) = \frac{|\cos\theta_y|}{\|x-y\|^2}\,dA(y) \implies \int(\cdots)\,d\sigma(\omega) = \int_\mathcal{M}(\cdots)\,G(x\leftrightarrow y)\,dA(y)
> \end{align}
> $$
> $$
> \begin{align}
> G(x\leftrightarrow y) := V(x\leftrightarrow y)\,\frac{|\cos\theta_x|\,|\cos\theta_y|}{\|x-y\|^2}
> \end{align}
> $$
> where $V \in \{0,1\}$ is visibility, replacing the ray trace that only made sense for a direction.

The Jacobian $|\cos\theta_y|/\|x-y\|^2$ comes from carrying a surface patch $dy$ at $y$, with normal $n_y$, back to the solid angle it subtends at $x$: projecting $dy$ onto the direction $\omega_i$ gives a cross-sectional patch $dy^\perp = |\cos\theta_y|\,dy$, and the cone through it shrinks in proportion to the squared distance, giving $d\sigma(\omega) = dy^\perp/\|x-y\|^2$. The $|\cos\theta_x|$ factor is the same argument run from the other end. $V$ is the only part of $G$ that is not simply a change of variables.

Among the factors of a path's contribution, $V$ is the odd one out: every other factor (emission, scattering kernels, cosines, inverse-square falloff, transmittance) varies smoothly with the vertex positions, while $V$ does not. This makes $V$ expensive — each evaluation is a ray query against the whole scene — and makes the path contribution discontinuous in the vertex positions, which is why quadrature is hopeless here, why variance does not fall as neatly as the smooth factors suggest, and why differentiating a light transport simulator naively gives the wrong answer (see [[Interchange of Differentiation and Expectation]] and [[Five Obstacles to Differentiating Monte Carlo Estimators]]).

# Properties
- Used to write the [[Light Transport Equation]] in [[Three-Point Form of the Light Transport Equation|three-point form]].
- Generalized to [[Generalized Path Integral (Surfaces and Volumes)|paths with volume vertices]] by additionally picking up transmittance and dropping the cosine at a volume endpoint.

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
