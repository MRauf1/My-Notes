---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Three-Point Form of the Light Transport Equation[^1]
> Substituting the [[Geometric Term (Light Transport)|geometric term]] $G$ for the solid-angle measure removes directions from the equation entirely, turning a scattering event into a statement about three points:
> $$
> \begin{align}
> L(x'\to x'') = L_e(x'\to x'') + \int_\mathcal{M} L(x\to x')\,f_s(x\to x'\to x'')\,G(x\leftrightarrow x')\,dA(x)
> \end{align}
> $$
> and the [[Measurement Equation]] likewise becomes
> $$
> \begin{align}
> I = \int_\mathcal{M}\int_\mathcal{M} W_e(y\to x)\,L(y\to x)\,G(y\leftrightarrow x)\,dA(y)\,dA(x)
> \end{align}
> $$
> where arrows follow the direction particles travel.

# Properties
- The natural form for the [[Path Integral (Light Transport)|path integral]] over [[Path Space]], since every quantity is now indexed by surface points rather than directions.

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
