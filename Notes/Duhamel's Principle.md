---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Duhamel's Principle[^1][^2][^3]
> If you can solve the homogeneous equation, you can solve the inhomogeneous one. Let the **source operator** $s(t)$ map data to the solution of the homogeneous problem at time $t$ (an [[Linear Operator|operator]]: it transforms functions into functions). Then the solution of the forced problem is the superposition of homogeneous solutions started at each earlier time $s$ with the forcing $f(\cdot, s)$ as data:
> $$
> \begin{align}
> \text{1st order in time } (u_t + Au = f,\ u(0) = \phi): \quad & u(t) = s(t)\phi + \int_0^t s(t - s) f(s)\, ds, \
> \text{2nd order in time } (u_{tt} + Au = f,\ u(0) = \phi,\ u_t(0) = \psi): \quad & u(t) = s'(t)\phi + s(t)\psi + \int_0^t s(t - s) f(s)\, ds,
> \end{align}
> $$
> where in the second case $s(t)\psi$ solves the homogeneous problem with zero initial position and initial velocity $\psi$.

**The ODE analogy.**[^2] For the scalar/matrix ODE $du/dt + Au = f(t)$, $u(0) = \phi$, variation of parameters gives
$$
\begin{align}
u(t) = e^{-tA}\phi + \int_0^t e^{(s - t)A} f(s)\, ds,
\end{align}
$$
with $e^{-tA}$ the [[Matrix Exponential]] ([[First Order Linear Ordinary Differential Equation]]). Duhamel's principle is the same formula with the propagator $e^{-tA}$ replaced by the PDE's source operator $s(t)$: think of $f(s)\,ds$ as a small impulse injected at time $s$, which then evolves freely for the remaining time $t - s$.

# Properties
- **Diffusion:** $s(t)\phi = S(\cdot, t) * \phi$ with $S$ the [[Diffusion Kernel (Partial Differential Equations)|diffusion kernel]] ([[Inhomogeneous Diffusion Equation]]).
- **Waves:** $s(t)\psi = \frac{1}{2c}\int_{x - ct}^{x + ct}\psi(y)\, dy$, and $s'(t)\phi = \frac12[\phi(x + ct) + \phi(x - ct)]$ recovers [[D'Alembert's Formula]]; the Duhamel integral becomes $\frac{1}{2c}\iint_\Delta f$ over the characteristic triangle ([[Inhomogeneous Wave Equation]]).
- Relies only on linearity ([[Superposition Principle (Partial Differential Equations)]]); the source operators form a [[Semigroup]], $s(t)s(\tau) = s(t + \tau)$, in the first-order case.
- Combined with the [[Method of Reflection]] it handles forcing on half-lines and intervals.

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=80&annotation=SRF943HC)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=79&annotation=NREHNHGN)
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=89&annotation=5LU5VSIW); [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=90&annotation=PLKGDLVJ)
