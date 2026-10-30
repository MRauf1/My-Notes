---
tags:
  - physics
  - mechanics
---

# Definition
> [!info] Mechanical Equilibrium[^1]
> An object is in mechanical equilibrium, balanced for both translation and rotation, if and only if
> $$
> \begin{align}
> \sum_i \mathbf{F}_i = \mathbf{0} \qquad \text{and} \qquad \sum_i \boldsymbol{\tau}_i = \mathbf{0},
> \end{align}
> $$
> i.e. the net [[Force]] and the net [[Torque]] both vanish.

# Properties
- The torque condition follows from the work definition of torque: in equilibrium no [[Work]] is done by the forces in a small displacement, so $\Delta W = \tau\,\Delta\theta = 0$ for every small rotation, forcing $\tau = 0$.
- If the net force is zero, the net torque is the same about every axis (since $\boldsymbol{\tau}' = \boldsymbol{\tau} - \mathbf{a}\times\mathbf{F}_{\text{net}}$), so it suffices to verify zero net torque about any single axis.

[^1]: [The Feynman Lectures on Physics, Vol. I, Ch. 18: Rotation in Two Dimensions](https://www.feynmanlectures.caltech.edu/I_18.html)
