---
tags:
  - physics
  - introduction_to_physics
---

# Definition
> [!info] Newton's Cannonball[^1]
> An orbit is a continuous state of falling that never lands: a projectile launched horizontally falls the same vertical distance in a given time as one simply dropped from rest, because horizontal and vertical motion are independent. If the projectile is launched fast enough, the surface it falls toward curves away from underneath it at exactly the rate it falls, so it keeps falling forever without ever getting closer to the surface — tracing out a closed orbit instead of a landing trajectory.

The key intuition is that an orbiting object never stops falling; it just never hits the ground, because the ground curves away beneath it at the same rate it descends. Only enough horizontal speed is needed to match the curvature of the fall to the curvature of the surface — nothing holds the object up, and nothing needs to.

# Example
> [!example]- Minimum Orbital Speed at Earth's Surface
> Near Earth's surface, an object dropped from rest falls about $16$ feet in the first second. For a horizontally-launched projectile to stay at the same height above the (nearly spherical) Earth, the horizontal distance $x$ it covers in that second must be the mean proportional between the $16$ feet fallen and the Earth's diameter (about $8000$ miles):
> $$
> \begin{align}
> x = \sqrt{\left(\frac{16\ \text{ft}}{5280\ \text{ft/mi}}\right) \times 8000\ \text{mi}} \approx 5\ \text{mi}
> \end{align}
> $$
> So a projectile launched horizontally at roughly $5$ miles per second falls $16$ feet every second, exactly matching the $16$ feet by which the Earth's surface curves away beneath it in that same second — it never gets any closer to the ground, and instead coasts in a circular orbit just above the surface. This is approximately the orbital speed of a satellite in low Earth orbit.

# Properties
- A direct consequence of [[Newton's Law of Universal Gravitation]] together with the independence of horizontal and vertical motion under a purely radial force: horizontal velocity is unaffected by a force directed straight down (toward the center).
- Explains why no tangential [[Force]] is required to sustain an orbit: inertia ([[Newton's First Law]]) alone carries the orbiting body forward in a straight line, while gravity supplies only the inward (centripetal) deviation from that line.

[^1]: [The Feynman Lectures on Physics, Vol. I, Ch. 7: The Theory of Gravitation](https://www.feynmanlectures.caltech.edu/I_07.html)
