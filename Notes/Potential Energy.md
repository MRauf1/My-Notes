---
tags:
  - physics
  - introduction_to_physics
---

# Definition
> [!info] Potential Energy[^1]
> $$\Delta U = F \cdot d$$
> The energy a system possesses by virtue of its configuration or position relative to a reference, rather than its motion; a change in potential energy equals the force acting against, times the distance through which that force acts.

# Properties
- Named for the interaction that stores it: [[Gravitational Potential Energy]] for gravitational forces, electrical potential energy for electrical forces, elastic potential energy for a deformed spring or material.
- Converts into [[Kinetic Energy]] as a system moves under the associated force, with the sum of the two conserved under [[Conservation of Energy]].
- Only well-defined for a [[Conservative Force]], since $\Delta U = -F\cdot d$ must depend only on the endpoints of the motion, not on the path taken between them.
- For a system of several objects interacting pairwise (e.g. under gravity), the total potential energy is the sum of the potential energies of every pair.
- Defined only up to an arbitrary additive constant, fixed by the choice of a reference point where $U=0$; physically meaningful quantities are always differences in potential energy, so the choice of reference does not matter.
- The force is recovered from the potential energy as its negative gradient, $\mathbf{F} = -\nabla U$ (i.e. $F_x = -\partial U/\partial x$, and similarly for $y,z$): the force points in the direction of steepest decrease of potential energy. Dividing both $U$ and $\mathbf F$ by the mass or charge of the object gives the analogous relation between a [[Gravitational Potential|gravitational]] or [[Electric Potential|electric]] potential and its associated field.

[^1]: [The Feynman Lectures on Physics, Vol. I, Ch. 4: Conservation of Energy](https://www.feynmanlectures.caltech.edu/I_04.html)
