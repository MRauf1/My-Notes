---
tags:
  - physics
  - mechanics
---

# Definition
> [!info] Angular Momentum[^1]
> For a particle with [[Momentum]] $\mathbf{p}$ at $(x,y)$, the angular momentum about the axis through the origin (perpendicular to the plane) is
> $$
> \begin{align}
> L = x\,m\frac{dy}{dt} - y\,m\frac{dx}{dt} = xp_y - yp_x = r\,p_{\text{tang}} = p \cdot (\text{lever arm}),
> \end{align}
> $$
> where $p_{\text{tang}}$ is the component of $\mathbf{p}$ perpendicular to the radius and the lever arm is the perpendicular distance from the axis to the line of the momentum. The total angular momentum of a system is the sum $L = \sum_i L_i$ over its particles.

> [!info] Angular Momentum in Three Dimensions
> $$
> \begin{align}
> \mathbf{L} = \mathbf{r} \times \mathbf{p},
> \end{align}
> $$
> whose component along the rotation axis $\hat{\mathbf{z}}$ is $xp_y - yp_x$ (see [[Cross Product]]).

# Properties
- Rotational analog of [[Momentum]], with exactly the same algebraic form in terms of $\mathbf{p}$ as [[Torque]] has in terms of $\mathbf{F}$.
- Its time derivative is the torque: $dL/dt = \tau$ (for a particle, $\frac{d}{dt}(xp_y - yp_x) = xF_y - yF_x$ since $\dot{x}p_y - \dot{y}p_x = 0$).
- The form $xp_y - yp_x$ remains correct relativistically when $\mathbf{p}$ is the [[Relativistic Momentum]].
- Only the tangential part of the momentum counts: what matters is how much the particle goes *around* the origin, not how fast it moves away from it. The momentum lever arm is generally different from the lever arm of the force on the particle.
- Depends on the position of the axis about which it is computed.
- Rate at which the radius vector sweeps out area is $dA/dt = L/(2m)$; hence [[Kepler's Second Law]] (equal areas in equal times) is precisely [[Conservation of Angular Momentum]] under a central force, which exerts no torque.
- For a [[Rigid Body]] in plane rotation, $L = I\omega$, where $I$ is the [[Moment of Inertia]] and $\omega$ the [[Angular Velocity]].
- The rate of change of total angular momentum of a system equals the external torque: [[Torque-Angular Momentum Theorem]].

[^1]: [The Feynman Lectures on Physics, Vol. I, Ch. 18: Rotation in Two Dimensions](https://www.feynmanlectures.caltech.edu/I_18.html)
