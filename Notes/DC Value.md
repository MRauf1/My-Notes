---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] DC Value[^1]
> The mean value $\mu$ of a [[Signal (Signal Processing)|signal]]. For a finite signal of length $N$ (or a periodic signal with period $N$):
> $$
> \begin{align}
> \mu = \frac{1}{N} \sum_{n=0}^{N-1} \ell[n]
> \end{align}
> $$
> For an infinite length signal:
> $$
> \begin{align}
> \mu = \lim_{N \to \infty} \frac{1}{2N + 1} \sum_{n=-N}^{N} \ell[n]
> \end{align}
> $$

# Properties
- For an image, the DC component is the average intensity of the image.
- The name comes from "direct current": it is the zero-frequency component of the signal, i.e. the $k = 0$ coefficient of its [[Discrete Fourier Transform|Fourier transform]] divided by $N$.[^2]
- A filter scales the DC value of its input by its [[DC Gain]].
- Normalizing a kernel to zero mean (removing its DC component) is the first step of [[Normalized Cross Correlation]].

[^1]: [MIT Vision Book - Linear Image Filtering](https://visionbook.mit.edu/linear_image_filtering.html)
[^2]: Added from general knowledge.
