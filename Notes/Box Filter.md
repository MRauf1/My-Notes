---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Box Filter[^1]
> The [[Blur Filter|blur filter]] whose [[Convolution|convolution]] kernel is the 2D [[Box Function (Signal Processing)|box function]]
> $$
> \begin{align}
> \text{box}_{N,M}[n, m] =
> \begin{cases}
> 1 & \text{if } -N \le n \le N \text{ and } -M \le m \le M \\
> 0 & \text{otherwise}
> \end{cases}
> \end{align}
> $$
> Filtering an image $\ell_{\text{in}}$ gives
> $$
> \begin{align}
> \ell_{\text{out}}[n, m] = \text{box}_{N,M}[n, m] \circ \ell_{\text{in}}[n, m] = \sum_{k=-N}^{N} \sum_{l=-M}^{M} \ell_{\text{in}}[n - k, m - l]
> \end{align}
> $$
> i.e. the sum of the input pixels in the $(2N+1) \times (2M+1)$ rectangle around $(n, m)$. In practice the kernel is normalized by $(2N+1)(2M+1)$ ([[DC Gain]] $1$), so the output is the **average** of the pixels in that rectangle:
> $$
> \begin{align}
> \ell_{\text{out}}[n, m] = \frac{1}{(2N+1)(2M+1)} \sum_{k=-N}^{N} \sum_{l=-M}^{M} \ell_{\text{in}}[n - k, m - l]
> \end{align}
> $$

# Properties
- A [[Low-Pass Filter]]: it attenuates the high spatial-frequency content of the image.
- [[Separable Filter|Separable]]: $\text{box}_{N,M} = \text{box}_{N,0} \circ \text{box}_{0,M}$.
- For large boxes it can be computed efficiently, independently of the box size, with an integral image (summed-area table).
- Unnormalized [[DC Gain]] is $(2N+1)(2M+1)$.
- **Not a perfect blur**: its attenuation is not monotonic in spatial frequency (its [[Discrete Fourier Transform|DFT]] is a [[Discrete Sinc Function|discrete sinc]] with sidelobes). E.g. $\text{box}_1 = [1,1,1]$ leaves the highest frequency $[\dots, 1, -1, 1, -1, \dots]$ unchanged (up to sign), but maps the lower frequency $[\dots, 0.5, 0.5, -1, 0.5, 0.5, -1, \dots]$ to zero. This can cause artifacts.
- An even-size box such as $[1, 1]$ fixes this, but it is not centered at the origin and shifts the output by half a pixel; hence odd sizes are preferred.
- **Not closed under convolution**: convolving two boxes of length $L$ gives a triangular filter of length $2L - 1$, e.g. $[1,1,1] \circ [1,1,1] = [1,2,3,2,1]$; boxes of different lengths give a truncated triangle. So blurring twice with boxes is not equivalent to blurring once with a larger box.
- Both limitations are addressed by the [[Gaussian Filter]] and the [[Binomial Filter]].

[^1]: [MIT Vision Book - Blurring](https://visionbook.mit.edu/blurring_2.html)
