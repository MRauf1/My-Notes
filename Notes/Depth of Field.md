---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Depth of Field)[^1]
> The region of the world around a camera's plane of focus within which a point is imaged with a [[Circle of Confusion]] smaller than some tolerance, and so appears acceptably sharp.

# Properties
- Narrowing the [[Aperture]] (increasing the [[F-Number]]) enlarges the depth of field, at the cost of reducing the light reaching the sensor plane.
- For a tolerable circle of confusion diameter $C$, [[F-Number|f-number]] $N$, and [[Focal Length (Lens)|focal length]] $f$, when the focal distance is much larger than $f$, the depth of field is approximately
> $$
> \begin{align}
> D \approx \frac{2NCU^2}{f^2}
> \end{align}
> $$
> where $U$ is the distance from the camera to the plane of focus.

[^1]: [MIT Vision Book - Lenses](https://visionbook.mit.edu/lenses.html)
