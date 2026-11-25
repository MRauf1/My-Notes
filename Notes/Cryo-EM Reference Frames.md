---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Cryo-EM Reference Frames[^1]
> - The **specimen (tomogram) frame** has axes fixed to the slab: $x, y$ in the plane of the untilted slab, $z$ along the $0^\circ$ beam.
> - The **molecule frame** has axes fixed to the reference structure $f$.
>
> The view of copy $i$ (pose $R_i$) in the image taken at tilt $\theta$ has total orientation $R_\theta R_i$. By the [[Fourier Slice Theorem]], in the molecule frame it measures $\hat f$ on the central plane
> $$
> \begin{align}
> \Pi_{i,\theta} = \big((R_\theta R_i)^{\top} e_z\big)^{\perp} = R_i^{\top}\big(R_\theta^{\top} e_z\big)^{\perp},
> \end{align}
> $$
> using $(Qv)^{\perp} = Q\,v^{\perp}$ for $Q \in SO(3)$.

![[Cryo-EM Fourier Frames.png]]

# Properties
- **[[Single-Particle Analysis]]**: $\theta = 0$ only, so there is one slice $R_i^{\top} e_z^{\perp}$ per particle, indexed by the [[Particle Pose]]. There is no specimen-frame reconstruction, because one projection of a field cannot be inverted.
- **[[Cryo-Electron Tomography]]**:
  - In the specimen frame, the slices $(R_\theta^{\top} e_z)^{\perp}$ are indexed by the tilt only: one fan hinged on $k_y$, shared by every copy. This yields the [[Tomogram]] and its [[Missing Wedge]] $W$.
  - In the molecule frame, copy $i$ contributes the same fan rotated by $R_i^{\top}$, hinged on $R_i^{\top} e_y$, so its missing region is $R_i^{\top} W$.
  - The change of frame is the alignment step of [[Subtomogram Averaging]].
- In both methods, the final structure is assembled in the molecule frame, where the unknowns are the poses $R_i$.

[^1]: [Singer & Sigworth (2020), Computational Methods for Single-Particle Cryo-EM](https://arxiv.org/abs/2003.13828)
