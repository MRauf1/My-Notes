---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Paraxial Approximation)[^1]
> The assumption, commonly used in analyzing imaging systems, that all light rays deviate only by a small angle from the optical axis.

# Properties
- Used together with the [[Thin Lens Approximation]] to derive simple expressions for how a [[Lens]] surface must bend incoming light rays to focus them, such as the [[Lensmaker's Equation]].
- The small-angle behavior justifies replacing $\sin\theta$ with $\theta$ in the relevant ray-bending relations.
- The wave-optics version, for a beam along $z$, drops $\partial_z^2u$ for the slowly varying envelope $u$, turning the Helmholtz or [[Schrödinger Equation]] into a first-order evolution in $z$. This is the propagation step of the [[Cryo-EM Forward Model]].

[^1]: [MIT Vision Book - Lenses](https://visionbook.mit.edu/lenses.html)
