---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Reynolds Transport Theorem (Leibniz Rule for a Moving Domain)[^1]
> The derivative of a parameter-dependent integral over a domain $\Omega(\theta)$ that itself moves with $\theta$ splits into an interior and a boundary term:
> $$
> \begin{align}
> \frac{d}{d\theta}\int_{\Omega(\theta)} f = \underbrace{\int_{\Omega(\theta)} \frac{\partial f}{\partial \theta}}_{\text{interior}} + \underbrace{\int_{\partial\Omega(\theta)} f\,(v\cdot n)}_{\text{boundary}}
> \end{align}
> $$
> where $v$ is the velocity of a point on the boundary $\partial\Omega(\theta)$ with respect to $\theta$, and $n$ is the outward unit normal to $\partial\Omega(\theta)$.

The interior term is what naive automatic differentiation computes: it differentiates the integrand while treating the domain as fixed. The boundary term is what naive automatic differentiation misses entirely, since it arises purely from the domain's motion rather than from any pointwise change in $f$.

Interpretation: the interior term captures the continuous variation of $f$ inside $\Omega(\theta)$, while the boundary term captures the effect of $\Omega(\theta)$'s motion sweeping across a discontinuity of $f$ at its edge — so, informally, the interior/boundary split mirrors a continuous/discontinuous split of the integrand's dependence on $\theta$.

There are two ways to recover the boundary term:
- Sample the boundary explicitly: locate the discontinuity and integrate over it directly (edge sampling, then path-space boundary integrals).
- Reparameterize: change variables so that the discontinuity no longer moves with $\theta$, absorbing the boundary term back into an interior term of the reparameterized integrand.

# Properties
- When $\Omega(\theta)$ does not depend on $\theta$, $v\cdot n = 0$ and the boundary term vanishes, recovering ordinary [[Interchange of Differentiation and Expectation|differentiation under the integral sign]].
- Repairs the [[Interchange of Differentiation and Expectation|interchange of differentiation and expectation]] for integrands whose discontinuity moves with $\theta$.

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
