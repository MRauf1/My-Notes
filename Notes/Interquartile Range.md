---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Interquartile Range[^1]
> For a [[Random Variable]] $X$ with first quartile $q_1 = \xi_{1/4}$ and third quartile $q_3 = \xi_{3/4}$ (see [[Quantile Function]]), the interquartile range is
> $$
> \begin{align}
> iq = q_3 - q_1
> \end{align}
> $$

The interval $[q_1, q_3]$ contains the middle half of the probability, so $iq$ measures the spread or dispersion of the distribution, while the [[Median]] $q_2 = \xi_{1/2}$ measures its center.

# Properties
- Exists for every distribution, unlike the [[Standard Deviation]], which requires a finite second moment.
- Robust: changing the distribution in the tails beyond $q_1$ and $q_3$ does not change $iq$.
- For a [[Normal Distribution]] $N(\mu, \sigma^2)$, $iq = 2 z_{0.75}\,\sigma \approx 1.349\,\sigma$.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=67)
