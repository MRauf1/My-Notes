---
tags:
  - physics
  - mechanics
---

# Definition
> [!info] Angular Velocity[^1]
> For a body in plane rotation about a fixed axis, with angular position $\theta(t)$ measured in radians, the angular velocity is the rate of change of the angle:
> $$
> \begin{align}
> \omega = \frac{d\theta}{dt}.
> \end{align}
> $$
> In three dimensions it is a vector $\boldsymbol{\omega}$ directed along the instantaneous rotation axis (by the right-hand rule) with magnitude $\lvert d\theta/dt\rvert$.

# Properties
- Rotational analog of [[Velocity Vector|velocity]] $v = ds/dt$: the angle $\theta$ (how far the body has gone *around*) replaces the distance $s$ (how far it has gone *along*). Measured in rad/s.
- Refers to the angular change of the position of the whole [[Rigid Body]] over time, not to any particular angle drawn on the object.
- A particle at $(x,y)$, a distance $r$ from the axis, turning through $\Delta\theta$ is displaced by $\Delta x = -y\,\Delta\theta$, $\Delta y = x\,\Delta\theta$, so its velocity is
$$
\begin{align}
v_x = -\omega y, \qquad v_y = \omega x, \qquad v = \sqrt{v_x^2+v_y^2} = \omega r.
\end{align}
$$
- In three dimensions, the velocity of a point of a rigid body at position $\mathbf{r}$ relative to a point on the axis is $\mathbf{v} = \boldsymbol{\omega} \times \mathbf{r}$ (see [[Cross Product]]); the planar formulas are its components for $\boldsymbol{\omega} = \omega\hat{\mathbf{z}}$.
- Its time derivative is the [[Angular Acceleration]].
- Uniform circular motion at angular velocity $\omega$ has [[Centripetal Acceleration]] of magnitude $\omega^2 r$.

[^1]: [The Feynman Lectures on Physics, Vol. I, Ch. 18: Rotation in Two Dimensions](https://www.feynmanlectures.caltech.edu/I_18.html)
