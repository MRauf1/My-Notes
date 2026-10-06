---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Sampling (Signal Processing)[^1]
> The process of transforming a continuous [[Signal (Signal Processing)|signal]] $\ell(t)$ into a discrete one $\ell[n]$, $n \in \mathbb{Z}$, by recording its values only at discrete instants. For uniform sampling with **sampling period** $\Delta T$, the **sampling equation** is
> $$
> \begin{align}
> \ell[n] = \ell(n \, \Delta T)
> \end{align}
> $$

# Properties
- The sampling rate is $1/\Delta T$; e.g. a video camera capturing 30 frames per second has $\Delta T = 1/30$ s.
- Analytically, sampling is modeled by multiplying the continuous signal with a train of [[Dirac Delta Function|Dirac impulses]], using the sampling property $\ell(t)\delta(t - a) = \ell(a)\delta(t - a)$.[^2]
- A camera pixel value is itself a [[Point Sample]] of the image falling on the sensor.

[^1]: [MIT Vision Book - Linear Image Filtering](https://visionbook.mit.edu/linear_image_filtering.html)
[^2]: Added from general knowledge.
