---
tags:
  - physics
  - introduction_to_physics
---

# Definition
> [!info] Spacetime Interval[^1]
> $$x^2+y^2+z^2-c^2t^2$$
> The combination of spatial and time coordinates of an event, measured from some origin event, that is left unchanged by a [[Lorentz Transformation]] between inertial frames — the four-dimensional analogue of the Euclidean distance to the origin, which is left unchanged by an ordinary rotation of spatial axes.

# Properties
- Plays the same role for the [[Lorentz Transformation]] that the squared distance $x^2+y^2+z^2$ plays for a spatial rotation: an invariant built from quantities that individually do change (here, space and time coordinates mix into one another, exactly as $x$ and $y$ mix under rotation).
- Motivates treating position and time together as a single four-component object in [[Spacetime]], of which ordinary three-component vectors become the spatial part; the [[Four-Momentum]] is the analogous four-component combination of momentum and energy, invariant in the same way.
- Its invariance is the geometric expression of the postulate, central to [[Special Relativity]], that the speed of light $c$ is the same in every inertial frame: an event on a light ray from the origin satisfies $x^2+y^2+z^2=c^2t^2$ in every frame.
- Unlike a squared Euclidean distance, its sign carries physical meaning: positive (in the $c^2t^2-x^2-y^2-z^2$ convention) is called time-like, negative is space-like, and zero is light-like (or null) — this classification determines whether the two events lie in each other's [[Light Cone]].
- The geometry in which this interval plays the role of invariant "distance" is [[Minkowski Space]], the flat, indefinite-signature geometry underlying special relativity.
- Equations involving the interval simplify if space and time are measured in the same units (e.g. seconds, with distance measured in light-seconds), so that $c=1$ and the interval reads $t^2-x^2-y^2-z^2$; this is the same idea, restricted to the single constant $c$, behind the broader convention of [[Planck Units]], which additionally sets $G=\hbar=k_B=1$.[^2]

[^1]: [The Feynman Lectures on Physics, Vol. I, Ch. 15: The Special Theory of Relativity](https://www.feynmanlectures.caltech.edu/I_15.html)
[^2]: [The Feynman Lectures on Physics, Vol. I, Ch. 17: Space-Time](https://www.feynmanlectures.caltech.edu/I_17.html)
