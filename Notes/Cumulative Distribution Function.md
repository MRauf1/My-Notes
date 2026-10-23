---
tags:
  - statistics
  - bayesian_statistics
  - mathematical_statistics
---

# Definition

> [!info] Definition 1 ([[Cumulative Function|Cumulative]] Distribution Function)[^1][^2]
> For a [[Random Variable]] $X$, its cdf is
> $$
> \begin{align}
> F_X(x) = P_X((-\infty, x]) = P(\{c \in \mathcal{C} : X(c) \leq x\}) = P(X \leq x), \quad x \in \mathbb{R}
> \end{align}
> $$

Every random variable has a cdf, and it determines the distribution completely. How it relates to the pmf or pdf depends on the type of $X$:
- Discrete: $F_X$ is a step function, and the [[Probability Mass Function]] is the jump size, $p_X(x) = F_X(x) - F_X(x^-)$.
- Absolutely continuous: $F_X(x) = \int_{-\infty}^x f_X(t)\,dt$, and $F_X'(x) = f_X(x)$ at every $x$ where the [[Probability Density Function]] $f_X$ is continuous.
- [[Mixture Random Variable|Mixture]]: $F_X$ has jumps but is not a step function.

# Properties
- [[Cumulative Distribution Function Basic Properties]]
- [[Random Variables Equal in Distribution]]
- Its (generalized) inverse is the [[Quantile Function]].
- Multivariate version: [[Joint Cumulative Distribution Function]].
- Expectations of discrete, continuous, and mixed random variables unify as the [[Riemann-Stieltjes Integral]] $E[g(X)] = \int g(x)\,dF_X(x)$, with $F_X$ as integrator ([[Expectation]]).
- Its generalized inverse $F^{-1}(u) = \inf\{x \mid F(x) \geq u\}$ always exists (by right-continuity) and drives [[Inverse Transform Sampling]].[^3]

[^1]: [Bayesian Statistical Methods](zotero://open-pdf/library/items/ELV3M9SP?page=19)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=55)
[^3]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=4&annotation=XSDQY29L); [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=4&annotation=6N8FHHRN)
