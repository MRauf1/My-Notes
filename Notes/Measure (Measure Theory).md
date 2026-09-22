---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Measure[^1]
> Given a set $\Gamma$, a measure $\mu$ is a function assigning a "size" to (measurable) subsets of $\Gamma$, satisfying for measurable $A, B \subseteq \Gamma$:
> $$
> \begin{align}
> \mu(A) \geq 0, \qquad \mu(A \cup B) = \mu(A) + \mu(B) \text{ if } A \cap B = \emptyset, \qquad \mu(\emptyset) = 0
> \end{align}
> $$

A [[Probability Space|probability measure]] $P$ is a measure with $P(\Omega) = 1$.

# Types
- [[Borel Measure]] $\mu_B$ — length of $[a,b)$; used for 1D integrals.
- [[Lebesgue Measure]] $\lambda$ — volume of a box; used on $\mathbb{R}^d$ and PDE domains.
- [[Area Measure]] $A$ — surface area; used on boundaries $\partial\Omega$ and scene geometry.
- [[Solid Angle Measure]] $\sigma$ — a set of directions; used for directions in 3D.
- [[Walk Space Measure]] $\mu_{\text{walk}}$ — product of area measures; used for random walks of any length.

# Properties
- Underlies the [[Lebesgue Integral (Measure Theory)|Lebesgue integral]] $I = \int_\Gamma f\,d\mu$: no coordinates, dimension, or smoothness required.

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
