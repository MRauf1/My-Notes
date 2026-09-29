---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Kernel Density Estimator[^1]
> Let $X_1, \dots, X_n$ be a [[Random Sample]] from a continuous pdf $f$. The rectangular-kernel estimate of $f$ at a point $x$, with $h > 0$, is
> $$
> \begin{align}
> \hat{f}(x) = \frac{\#\{x - h < X_i < x + h\}}{2hn} = \frac{1}{2hn}\sum_{i=1}^n I_i(x), \qquad I_i(x) = \begin{cases} 1 & x - h < X_i < x + h \\ 0 & \text{otherwise} \end{cases}
> \end{align}
> $$
> More generally, for a kernel $K \geq 0$ with $\int K = 1$ and bandwidth $h$,
> $$
> \begin{align}
> \hat{f}(x) = \frac{1}{nh}\sum_{i=1}^n K\left(\frac{x - X_i}{h}\right)
> \end{align}
> $$
> and the rectangular case is $K(u) = \frac12\mathbb{1}\{|u| < 1\}$.

Motivation: by the [[Mean Value Theorem for Riemann Integral]], $P(x - h < X < x + h) = \int_{x-h}^{x+h} f(t)\,dt = 2hf(\xi) \approx 2hf(x)$ for some $|\xi - x| < h$, and the left side is estimated by the proportion of the sample in the window. Each observation spreads a unit of probability mass over a small window around itself, and the estimate is the sum of these bumps.

# Properties
- Approximately unbiased: $E[\hat{f}(x)] = f(\xi) \to f(x)$ as $h \to 0$.
- The bandwidth controls a [[Bias-Variance Tradeoff]]: small $h$ gives low bias but a noisy, spiky estimate; large $h$ gives a smooth estimate but blurs features. Consistency requires $h \to 0$ and $nh \to \infty$.
- Unlike the [[Histogram]], it does not depend on an arbitrary bin origin, and a smooth kernel (e.g. Gaussian) gives a smooth estimate; the choice of $h$ matters much more than the choice of $K$.
- A nonparametric approach to [[Density Estimation]]; it is the convolution of the empirical distribution with the scaled kernel ([[Convolution Formula]]).

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=248)
