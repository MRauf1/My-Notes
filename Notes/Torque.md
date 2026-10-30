---
tags:
  - physics
  - mechanics
---

# Definition
> [!info] Torque (Moment of Force)[^1]
> For plane rotation about a fixed axis, the torque of a [[Force]] $\mathbf{F}$ applied at $(x,y)$ is the quantity $\tau$ for which the [[Work]] done in a small rotation $\Delta\theta$ is $\Delta W = \tau\,\Delta\theta$. Since $\Delta W = F_x\Delta x + F_y \Delta y$ with $\Delta x = -y\Delta\theta$, $\Delta y = x\Delta\theta$,
> $$
> \begin{align}
> \tau = xF_y - yF_x = r\,F_{\text{tang}} = r F \sin\alpha = F \cdot (\text{lever arm}),
> \end{align}
> $$
> where $F_{\text{tang}}$ is the component of $\mathbf{F}$ perpendicular to the radius, $\alpha$ is the angle between $\mathbf{r}$ and $\mathbf{F}$, and the lever arm is the perpendicular distance from the axis to the line of action of $\mathbf{F}$.

> [!info] Torque in Three Dimensions
> The torque of $\mathbf{F}$ applied at $\mathbf{r}$ about the origin $O$ is the [[Cross Product]]
> $$
> \begin{align}
> \boldsymbol{\tau} = \mathbf{r} \times \mathbf{F},
> \end{align}
> $$
> whose component along the rotation axis $\hat{\mathbf{z}}$ is the planar torque $xF_y - yF_x$.

# Properties
- Rotational analog of force: force times distance is work, torque times angle is work. Torque is not a new idea independent of Newtonian mechanics; it is defined entirely in terms of forces.
- Only the tangential component of the force contributes; a purely radial force, or a force applied on the axis, produces no torque.
- In two dimensions, the total torque of several forces is the algebraic sum $\tau = \sum_i (x_iF_{y_i} - y_iF_{x_i})$; torques add as scalars only because all rotations are about the same axis, analogous to one-dimensional forces.
- Depends on the choice of axis: moving the axis changes every $(x_i, y_i)$ and generally changes the torque. Shifting the origin by $\mathbf{a}$ gives $\boldsymbol{\tau}' = \boldsymbol{\tau} - \mathbf{a}\times\mathbf{F}_{\text{net}}$, so the total torque is axis-independent when the net force vanishes (see [[Mechanical Equilibrium]]).
- Is the time rate of change of [[Angular Momentum]], $\tau = dL/dt$; summed over a system, only external torques survive (see [[Torque-Angular Momentum Theorem]]).
- For a [[Rigid Body]] about a fixed axis, $\tau = I\alpha$, with $I$ the [[Moment of Inertia]] and $\alpha$ the [[Angular Acceleration]].
- "Moment" in "moment of force" refers, as in mathematics (cf. [[Moment (Statistics)]]), to weighting by distance from an axis.

[^1]: [The Feynman Lectures on Physics, Vol. I, Ch. 18: Rotation in Two Dimensions](https://www.feynmanlectures.caltech.edu/I_18.html)
