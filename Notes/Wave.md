---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Wave[^1]
> A disturbance $u(\mathbf{x}, t)$ of some quantity (displacement, pressure, field strength, probability amplitude) that propagates through space over time, typically carrying energy without net transport of the medium. The simplest example is a **travelling wave** in one dimension, which keeps its shape while moving at constant speed $c$:
> $$
> \begin{align}
> u(x, t) = f(x - ct) \quad (\text{moving in } +x), \qquad u(x, t) = g(x + ct) \quad (\text{moving in } -x).
> \end{align}
> $$

# Types
- [[Sinusoidal Wave]]: a single frequency; the building block for all others.
- [[Plane Wave]]: wavefronts are parallel planes.
- Spherical waves, standing waves, and wave packets (localized superpositions).

# Properties
- Every solution of the 1D [[Wave Equation]] $u_{tt} = c^2 u_{xx}$ is a sum $f(x - ct) + g(x + ct)$ of two travelling waves (d'Alembert).
- Waves of a linear equation obey the [[Superposition Principle (Partial Differential Equations)|superposition principle]], which gives [[Interference (Waves)|interference]].
- A general wave can be decomposed into sinusoidal waves ([[Fourier Transform]]).

[^1]: [Wave (Wikipedia)](https://en.wikipedia.org/wiki/Wave)
