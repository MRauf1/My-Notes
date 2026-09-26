---
tags:
  - physics
  - introduction_to_physics
---

# Definition
> [!info] Four-Vector[^1]
> $$A^\mu = (A_t, A_x, A_y, A_z)$$
> A set of four quantities that transform under a [[Lorentz Transformation]] exactly as the coordinates $(t,x,y,z)$ of an [[Event (Physics)|event]] do; the four-dimensional generalization, in [[Minkowski Space]], of an ordinary three-component vector.

# Properties
- Added component-by-component, exactly like an ordinary vector; if a physical law equates two four-vectors, the equality must hold separately in each of the four components, in every choice of coordinate axes.
- Has an invariant squared "length," the Minkowski dot product of the four-vector with itself, $\sum{}' A^\mu A_\mu = A_t^2-A_x^2-A_y^2-A_z^2$, which (unlike a Euclidean length) can be positive, negative, or zero, and which is the same in every inertial frame.
- More generally, the scalar product of two four-vectors, $\sum{}' a^\mu b^\mu = a_tb_t - a_xb_x-a_yb_y-a_zb_z$, is likewise invariant under a Lorentz transformation.
- [[Four-Momentum]] is the four-vector combining a particle's energy and [[Relativistic Momentum|momentum]]; the [[Spacetime Interval]] is the squared length of the four-vector separating two events.
- A quantity with only three components, transforming correctly under spatial rotations but with no accompanying "time" component, cannot in general be part of a relativistically invariant law: rotations only mix the three spatial components among themselves, but a Lorentz transformation mixes space and time together, so completing a three-component law (e.g. [[Conservation of Momentum]]) into a relativistic one requires identifying and including its time component.

[^1]: [The Feynman Lectures on Physics, Vol. I, Ch. 17: Space-Time](https://www.feynmanlectures.caltech.edu/I_17.html)
