---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Fourier Amplitude and Phase[^1]
> In polar form, the [[Discrete Fourier Transform|DFT]] of an image decomposes as
> $$
> \begin{align}
> \mathscr{L}[u, v] = \left| \mathscr{L}[u, v] \right| \exp\left(j \angle \mathscr{L}[u, v]\right)
> \end{align}
> $$
> where $|\mathscr{L}[u, v]|$ is the **amplitude** (magnitude) and $\angle \mathscr{L}[u, v]$ the **phase** at each [[Spatial Frequency|spatial frequency]] ([[Complex Number in Polar Coordinates]]).
> Here $j = \sqrt{-1}$ is the [[Imaginary Unit|imaginary unit]] (the signal processing notation for $i$).

The relative importance of amplitude and phase for the image content is revealed by reconstructing an image with the inverse DFT after removing one component: randomizing the phase (amplitude-only image), or replacing the amplitude with a generic, non-informative amplitude common to all images, such as the [[Natural Image Amplitude Spectrum|natural image spectrum]] (phase-only image; a random amplitude would instead give a very noisy image hiding the structure).

# Properties
- For many images, the phase carries most of the image information (the phase-only reconstruction is recognizable). However, this does not mean that all information is in the phase: the relative importance varies across images.
- The amplitude is most important for images with strong periodic patterns (e.g. pseudo-periodic textures), where it can be more informative than the phase. This observation is the basis of many image descriptors (e.g. the GIST scene descriptor).
- The amplitude is somewhat invariant to location (a translation only changes the phase, [[Fourier Shift Theorem]]), although it is not invariant to the relative location between different elements in the scene.
- The phase is a complex signal that does not make explicit any information about the image.
- The amplitude of natural images follows a characteristic decay with frequency ([[Natural Image Amplitude Spectrum]]).
- For filters, the analogous decomposition of the [[Transfer Function (Signal Processing)|transfer function]] gives the amplitude gain and phase shift.

[^1]: [MIT Vision Book - Fourier Analysis](https://visionbook.mit.edu/image_processing_fourier.html)
