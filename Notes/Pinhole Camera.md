---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Pinhole Camera)[^1]
> The simplest camera: a light-tight enclosure with a small hole, the pinhole, that lets light pass, and a projection surface on which the illumination intensity is sensed as a function of position. For any point on the projection surface, the light that reaches it comes from only one direction, along the straight line joining that surface position and the pinhole, forming an image of the scene on the projection plane.

![[Pinhole Camera Coordinate Systems.png]]

# Properties
- First described by [[Alhacen's Theory of Vision|Alhacen]] in his Book of Optics, alongside the related [[Camera Obscura]].
- The role of a camera, generally, is to organize the [[Light Ray|light rays]] arriving from every direction into a set of position-indexed intensity measurements, since the intensity reflecting off a single diffuse surface, as given by the [[Lambertian Reflectance Model]], alone reveals very little about the incoming light from any particular direction.
- Its imaging geometry is described using [[World Coordinate System|world]], [[Camera Coordinate System|camera]], and [[Image Coordinate System|image]] coordinates, and gives rise to the [[Perspective Projection Equations]].
- Suffers from a dim image, since only a small [[Aperture|aperture]] can be used before light from many surface positions begins to land on the same sensor position; a [[Lens]] overcomes this limitation by focusing a wider aperture's light back to a single point per surface position.
- Viewed as a [[Camera as Linear System|linear system]], $\ell_s = \mathbf{A}\ell_w$, its [[Imaging Matrix]] $\mathbf{A}$ is approximately the identity matrix, since each sensor measurement depends only on the single scene element it directly faces.

[^1]: [MIT Vision Book - Imaging](https://visionbook.mit.edu/imaging.html)
