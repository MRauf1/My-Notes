---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Normalized Cross Correlation[^1]
> Let $\hat{h}$ be the kernel $h$ normalized to zero mean and unit norm, with support $[-N, N] \times [-N, N]$. The normalized cross-correlation of an image $\ell_{\text{in}}$ with $\hat{h}$ is the [[Cross Correlation (Signal Processing)|cross-correlation]] rescaled by the local standard deviation of the image:
> $$
> \begin{align}
> \ell_{\text{out}}[n, m] = \frac{1}{\sigma[n, m]} \sum_{k, l = -N}^{N} \ell_{\text{in}}[n + k, m + l] \, \hat{h}[k, l]
> \end{align}
> $$
> where the local mean and variance over the patch centered at $(n, m)$ of the same size as the kernel are
> $$
> \begin{align}
> \mu[n, m] &= \frac{1}{(2N + 1)^2} \sum_{k, l = -N}^{N} \ell_{\text{in}}[n + k, m + l] \\
> \sigma^2[n, m] &= \frac{1}{(2N + 1)^2} \sum_{k, l = -N}^{N} \left( \ell_{\text{in}}[n + k, m + l] - \mu[n, m] \right)^2
> \end{align}
> $$

# Properties
- Interpretation: at each location it is the [[Dot Product|dot product]] between the normalized template and the local image patch normalized to unit norm.
- Since $\hat{h}$ has zero mean, $\sum \hat{h}[k,l] \mu[n,m] = 0$, so the output equals the correlation of $\hat{h}$ with the mean-subtracted patch divided by $\sigma[n, m]$: up to the constant factor $2N + 1$ it is the cosine similarity (Pearson [[Correlation|correlation coefficient]]) between template and patch, bounded in $[-(2N+1), 2N+1]$ by Cauchy–Schwarz.[^2]
- Consequently it is invariant to affine changes of image intensity (gain and offset) within each patch, which makes template matching robust to illumination changes, unlike the plain cross-correlation that responds strongly to bright regions.[^2]

[^1]: [MIT Vision Book - Linear Image Filtering](https://visionbook.mit.edu/linear_image_filtering.html)
[^2]: Added from general knowledge.
