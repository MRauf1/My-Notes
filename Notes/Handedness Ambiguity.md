---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Handedness Ambiguity[^1]
> Let $J = \operatorname{diag}(1, 1, -1)$ and let $f'(x) = f(Jx)$ be the mirror image of $f$. For every pose $R \in SO(3)$, the projection of $f$ at $R$ along the beam $e_z$ equals the projection of $f'$ at the pose $R' = JRJ \in SO(3)$:
> $$
> \begin{align}
> P_{e_z}\big(R'^{-1} \cdot f'\big) = P_{e_z}\big(R^{-1} \cdot f\big).
> \end{align}
> $$
> So from projection images alone, a structure and its mirror image cannot be distinguished: the chirality (hand) of the reconstruction is not identifiable.

# Properties
- The hand is fixed by external knowledge (e.g. α-helices are right-handed), or by a tilt pair: two images of the same field at known relative tilt[^1].
- In [[Single-Particle Analysis]] and [[Ab Initio Reconstruction]], it is a symmetry of the likelihood beyond the global rotation gauge of [[Particle Pose]].
- **The three intrinsic ambiguities** of cryo-EM reconstruction are a global 3D rotation, the 3D position of the molecule's centre, and the handedness.[^2]

# Questions
> [!question]- Prove the identity, and say where the projection is used.
> $R' = JRJ$ has $\det R' = \det R = 1$, so $R' \in SO(3)$. Then
> $$
> \begin{align}
> (R'^{-1} \cdot f')(x) = f'(R' x) = f(J\,JRJ\,x) = f(R J x) = (R^{-1} \cdot f)(Jx).
> \end{align}
> $$
> $J$ only flips $x_3$, and the projection $P_{e_z}$ integrates over $x_3 \in \mathbb{R}$, which is invariant under $x_3 \mapsto -x_3$. So both sides have the same projection. In 3D the volumes differ; only the projection (the loss of depth) makes them indistinguishable.

> [!question]- Why does a tilt pair resolve the hand?
> A known relative tilt $R_\theta$ between two images of the same particle constrains the poses to satisfy $R_2 = R_\theta R_1$. For the mirror solution, the poses are $J R_1 J$ and $J R_2 J = (J R_\theta J)(J R_1 J)$, so their relative rotation is $J R_\theta J$. That is the rotation by $-\theta$ about the same in-plane axis, which differs from the known $R_\theta$ when $\theta \neq 0$. Only one hand is consistent with the measured tilt direction.

[^1]: [Rosenthal & Henderson (2003), Optimal determination of particle orientation, absolute hand, and contrast loss in single-particle electron cryomicroscopy, J. Mol. Biol. 333:721–742](https://doi.org/10.1016/j.jmb.2003.07.013)
[^2]: [Bendory et al., 2020, p. 5](zotero://open-pdf/library/items/N4ZIHINK?page=5&annotation=RGH9P8YW)
