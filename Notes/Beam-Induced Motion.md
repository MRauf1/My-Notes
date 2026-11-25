---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Beam-Induced Motion[^1]
> Movement of the specimen and its particles during exposure, caused by the electron beam: up to about $20$ Å, largest in the first frames of a movie. Its physical origin is not settled. One explanation is that energy deposited by inelastic scattering stresses the ice layer, which then buckles.

# Properties
- It blurs the image and is the largest contributor to the [[CTF Envelope Function|B-factor]].
- **The first frames are the problem.** The early dose ($\approx 1$–$3\ e^-/\text{Å}^2$) carries the least-damaged, highest-resolution signal but has the fastest motion, a "burst phase" too fast to track at current frame rates with so little signal per frame. This was still regarded as a primary resolution limit in 2021[^2].
- The largest motions are normal to the specimen plane, so tilting the specimen (used against [[Preferred Orientation]]) makes it worse.
- It is corrected after the fact by [[Motion Correction]].

[^1]: [Singer and Sigworth, 2020, p. 9](zotero://open-pdf/library/items/FKVQSKD6?page=9&annotation=4L7APZN7)
[^2]: [Devitrification reduces beam-induced movement in cryo-EM (IUCrJ, 2021)](https://journals.iucr.org/m/issues/2021/02/00/pw5016/index.html)
