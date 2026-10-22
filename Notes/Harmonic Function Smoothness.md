---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Harmonic Function Smoothness[^1]
> Let $u$ be a [[Harmonic Function]] in any open set $D$ of the plane. Then $u(x, y)$ possesses all partial derivatives of all orders in $D$.

**Proof idea.**[^2] Around any point of $D$, take a disk whose closure lies in $D$; inside it $u$ equals [[Poisson's Formula]] applied to its own boundary values. The [[Poisson Kernel]] is infinitely differentiable for $r < a$, so differentiating under the integral sign shows $u \in C^\infty$.

# Properties
- Holds in every dimension; harmonic functions are even [[Real Analytic Function|real analytic]].[^2]
- Weyl's lemma: a merely locally integrable weak solution of $\Delta u = 0$ is already smooth, so the Laplace equation admits no non-smooth solutions; contrast with the [[Wave Equation]], which propagates singularities.[^2]
- Parallels the [[Diffusion Equation Smoothing Theorem]]: both are consequences of a smooth integral kernel.
- A [[Smooth Function]] result, part of what makes the [[Laplace Equation]] [[Elliptic Partial Differential Equation|elliptic]].

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=182&annotation=ESKJUQF5)
[^2]: Added from general knowledge.
