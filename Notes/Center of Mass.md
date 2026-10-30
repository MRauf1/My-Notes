---
tags:
  - physics
  - mechanics
---

# Definition
> [!info] Center of Mass[^1]
> For a system of particles with [[Mass|masses]] $m_i$ at positions $\mathbf{r}_i$ and total mass $M = \sum_i m_i$, the center of mass is the mass-weighted average position
> $$
> \begin{align}
> \mathbf{R} = \frac{1}{M}\sum_i m_i \mathbf{r}_i,
> \end{align}
> $$
> or $\mathbf{R} = \frac{1}{M}\int \mathbf{r}\, dm$ for a continuous body.

> [!info] Center of Mass Theorem[^1]
> The total external [[Force]] on any system of particles equals its total mass times the acceleration of its center of mass:
> $$
> \begin{align}
> \mathbf{F}_{\text{ext}} = \sum_i m_i \frac{d^2\mathbf{r}_i}{dt^2} = \frac{d^2 (M\mathbf{R})}{dt^2} = M\frac{d^2\mathbf{R}}{dt^2}.
> \end{align}
> $$

# Properties
- Need not be a point of the material itself; it is a mathematically defined mean position.
- The proof relies on [[Newton's Third Law]]: internal forces between pairs of particles cancel when [[Newton's Second Law]] is summed over all particles, leaving only external forces.
- If $\mathbf{F}_{\text{ext}} = \mathbf{0}$, the center of mass moves with constant velocity (in particular, stays at rest if initially at rest), no matter how the parts of the system whirl, jiggle, or rearrange internally — equivalent to [[Conservation of Momentum]], since the total momentum is $\mathbf{P} = M\,d\mathbf{R}/dt$.
- Its motion can be treated separately from the internal motions of the object; for a [[Rigid Body]], what remains after removing center-of-mass motion is pure rotation.
- For two mutually orbiting bodies, the center of mass is their [[Barycenter]].

[^1]: [The Feynman Lectures on Physics, Vol. I, Ch. 18: Rotation in Two Dimensions](https://www.feynmanlectures.caltech.edu/I_18.html)
