---
tags:
  - physics
  - mechanics
---

# Definition
> [!info] Moment of Inertia[^1]
> For a [[Rigid Body]] rotating about a fixed axis, the moment of inertia is the sum of its particles' [[Mass|masses]] times their squared distances $r_i$ from the axis:
> $$
> \begin{align}
> I = \sum_i m_i r_i^2 \qquad \left(\text{or } I = \int r^2\, dm \text{ for a continuous body}\right),
> \end{align}
> $$
> so that the [[Angular Momentum]] is $L = I\omega$, with $\omega$ the [[Angular Velocity]].

# Properties
- Rotational analog of [[Mass]] ("inertia against turning"): $L = I\omega$ parallels $p = mv$, and $\tau = dL/dt = I\alpha$ parallels $F = ma$ (see [[Torque]], [[Angular Acceleration]]).
- Depends not only on the masses but on how far they are from the axis; moving the same masses farther out increases the resistance to angular acceleration.
- Depends on the choice of axis.
- Unlike mass, the moment of inertia of a body can be changed (by rearranging its parts); with no external torque, [[Conservation of Angular Momentum]] then forces $I_1\omega_1 = I_2\omega_2$.
- The rotational [[Kinetic Energy]] of a rigid body about a fixed axis is $\frac{1}{2}I\omega^2$, since $\sum_i \frac{1}{2}m_i(\omega r_i)^2$.

[^1]: [The Feynman Lectures on Physics, Vol. I, Ch. 18: Rotation in Two Dimensions](https://www.feynmanlectures.caltech.edu/I_18.html)
