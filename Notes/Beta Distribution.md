---
tags:
  - statistics
  - bayesian_statistics
---

# Definition

> [!info] Definition 1 (Beta [[Probability Distribution]])
> Beta distribution, with [[Function Support]] $[0, 1]$, denoted as $Beta(\alpha, \beta)$ is
> $$
> \begin{align}
> f(x) = \begin{cases}\frac{\Gamma(\alpha + \beta)}{\Gamma(\alpha) \Gamma(\beta)} x^{\alpha - 1} (1 - x)^{\beta - 1} & x \in [0, 1] \\ 0 & x < 0\ \text{or}\ x > 1\end{cases}
> \end{align}
> $$

In particular, $Beta(\alpha = 1, \beta = 1)$ gives the [[Continuous Uniform Distribution]].[^2]

**Use.** The beta family is the standard model for a quantity confined to a bounded interval, where the gamma family (support $(0, \infty)$) does not apply.[^3] For known bounds $(a, b)$, rescale via $Y = (X - a)/(b - a)$ to $(0, 1)$. Its two [[Shape Parameter|shape parameters]] give a wide variety of shapes: uniform ($\alpha = \beta = 1$), symmetric bells ($\alpha = \beta > 1$), U-shapes ($\alpha, \beta < 1$), and skewed or J-shaped densities otherwise. It is the natural distribution for an unknown probability or proportion: $\alpha - 1$ and $\beta - 1$ act like counts of successes and failures, and it is the [[Conjugate Prior]] for the success probability of the [[Binomial Distribution]].

**Construction from gammas.**[^2] If $X_1 \sim \Gamma(\alpha, 1)$ and $X_2 \sim \Gamma(\beta, 1)$ are independent, then $Y_2 = X_1/(X_1 + X_2) \sim Beta(\alpha, \beta)$, and it is independent of $Y_1 = X_1 + X_2 \sim \Gamma(\alpha + \beta, 1)$ ([[Random Vector Transformation]] and the [[Independent Random Variable Factorization Theorem]]). The normalizing constant is $B(\alpha, \beta) = \Gamma(\alpha)\Gamma(\beta)/\Gamma(\alpha + \beta)$ ([[Gamma Function]]).

# Properties
## Basic Statistical Properties
- [[Beta Distribution Expectation]]
- [[Beta Distribution Variance]]
- $\mu = \frac{\alpha}{\alpha + \beta}$, $\sigma^2 = \frac{\alpha\beta}{(\alpha + \beta + 1)(\alpha + \beta)^2}$.[^2]

## Generalization
- [[Dirichlet Distribution]], the multivariate version on the probability simplex.

[^1]: [Bayesian Statistical Methods](zotero://open-pdf/library/items/ELV3M9SP?page=22)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=197)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=196)
