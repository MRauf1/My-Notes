---
tags:
  - physics
  - mechanics
---

# Definition
> [!info] Rigid Body[^1]
> An idealized extended object whose interparticle forces are so strong that the forces needed to move it do not deform it: the distance between every pair of its constituent particles stays fixed, $\lVert \mathbf{r}_i(t) - \mathbf{r}_j(t)\rVert = \text{constant}$ for all $i,j$ and all $t$.

# Properties
- Its configuration at any time is related to its initial configuration by a [[Rigid-Body Transformation]] (a translation plus a rotation).
- Its motion decomposes into the motion of its [[Center of Mass]] plus a rotation; once the center-of-mass motion is set aside, the only remaining motion is turning.
- For rotation about a fixed axis (*plane rotation*, or rotation in two dimensions), every point moves in a plane perpendicular to the axis, and the whole configuration is described by a single angle $\theta(t)$; its kinematics is described by [[Angular Velocity]] and [[Angular Acceleration]], and its dynamics by [[Torque]], [[Angular Momentum]], and [[Moment of Inertia]].
- Rotations in three dimensions are considerably subtler than plane rotation (e.g. torques no longer add as scalars).

[^1]: [The Feynman Lectures on Physics, Vol. I, Ch. 18: Rotation in Two Dimensions](https://www.feynmanlectures.caltech.edu/I_18.html)
