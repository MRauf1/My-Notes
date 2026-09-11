---
tags:
  - mathetatics
  - calculus
---

# Definition

> [!info] Definition 1 ([[Leonhard Euler]] Method)[^1]
> For a [[Differential Equation]] $\frac{dy}{dx} = F(x, y)$ with $y(x_0) = y_0$, given a step size $h$ such that $x_n = x_{n - 1} + h$, the approximation is
> $$
> \begin{align}
> y_{n} = y_{n - 1} + h F(x_{n - 1}, y_{n - 1})
> \end{align}
> $$

Smaller step sizes give better approximations.

# Properties
- Applied to [[Newton's Second Law]], evolves position and velocity together at each time step: the current position gives the force and hence acceleration, the acceleration updates the velocity, and the velocity updates the position — a numerical scheme for integrating the equations of motion (e.g. [[Simple Harmonic Motion]]) when no closed-form solution is used directly.

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=627)