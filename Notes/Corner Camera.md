---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Corner Camera)[^1]
> A [[Computational Camera]] technique that recovers information about a scene hidden around a vertical edge (a corner) by observing the subtle intensity variations that the hidden scene casts onto a visible surface, such as the ground, near the edge.

![[Corner Camera Geometry.png]]

# Properties
- The observed intensities on the visible surface are related to the hidden scene's radiance by an integral over the visible directions around the corner, analogous to integrating a [[Lambertian Reflectance Model|Lambertian]] surface's reflected intensity over incoming light directions.
- Recovers an approximately one-dimensional image of the hidden scene as a function of the azimuthal angle around the corner.
- A real-world example of a general, non-identity [[Imaging Matrix|imaging matrix]] in a [[Computational Camera]], recovering an image from measurements that do not themselves resemble one.

[^1]: [MIT Vision Book - The Camera as a Linear System](https://visionbook.mit.edu/camera_as_linsys.html)
