---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] CTF Correction[^1]
> Undoing the effect of the [[Contrast Transfer Function]] on images: deconvolution by the PSF $h$, i.e. division by $H$ in Fourier space. It is ill-posed because of the zero crossings of $H$ and the decay of the envelope at high frequencies.
> - **Phase flipping** applies $\operatorname{sign}(H)$: it corrects the phase but not the amplitude, and preserves the noise statistics.
> - **[[Wiener Filter|Wiener filtering]]** applies $\overline{H}/(|H|^2 + 1/\mathrm{SSNR})$ with $\mathrm{SSNR} = \mathrm{PSD}_f/\mathrm{PSD}_b$ (byproducts of [[CTF Estimation]]): it corrects the amplitude too.

# Properties
- No correction of a single micrograph recovers the frequencies at zeros of $H$. Near the zeros and at high $|k|$, the signal is present but too weak to use.
- The lost frequencies are recovered only by combining images at different defoci: the multi-image Wiener filter used in [[2D Classification|2D class averages]] and in 3D reconstruction.
- Uncorrected, the CTF delocalizes the image of a particle and enlarges its support.

[^1]: [Singer and Sigworth, 2020, p. 10](zotero://open-pdf/library/items/FKVQSKD6?page=10&annotation=JLSDEHX3)
