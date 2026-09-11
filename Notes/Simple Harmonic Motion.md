---
tags:
  - physics
  - introduction_to_physics
---

# Definition
> [!info] Simple Harmonic Motion[^1]
> The periodic back-and-forth motion executed by an object subject to a restoring [[Force]] directly proportional to its displacement from equilibrium (see [[Hooke's Law]]), governed by
> $$
> \begin{align}
> m\frac{d^2x}{dt^2} = -kx
> \end{align}
> $$

# Properties
- A direct consequence of applying [[Newton's Second Law]] to a linear restoring force: because the force — and hence the acceleration — always points back toward equilibrium and grows with distance from it, an object displaced from equilibrium continually overshoots and returns, producing sustained oscillation rather than settling at rest.
- Can be evolved forward in time step by step from the governing equation and an initial position and velocity, e.g. numerically via [[Euler's Method]]: at each small time step, the current position gives the force and hence the acceleration, the acceleration updates the velocity, and the velocity updates the position.

[^1]: [The Feynman Lectures on Physics, Vol. I, Ch. 9: Newton's Laws of Dynamics](https://www.feynmanlectures.caltech.edu/I_09.html)
