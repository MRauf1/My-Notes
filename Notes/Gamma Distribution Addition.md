---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Gamma Distribution Addition[^1]
> Let $X_1, \dots, X_n$ be [[Mutually Independent Random Variables|independent]] with $X_i \sim \Gamma(\alpha_i, \beta)$ (common scale $\beta$). Then
> $$
> \begin{align}
> Y = \sum_{i=1}^n X_i \sim \Gamma\left(\sum_{i=1}^n \alpha_i, \beta\right)
> \end{align}
> $$

Proof: by the [[Moment Generating Function Technique]], $M_Y(t) = \prod_i (1 - \beta t)^{-\alpha_i} = (1 - \beta t)^{-\sum \alpha_i}$ for $t < 1/\beta$. In the waiting-time picture, waiting for $\alpha_1$ events and then for $\alpha_2$ more events in the same [[Poisson Process]] is waiting for $\alpha_1 + \alpha_2$ events.

# Properties
- Requires a common scale $\beta$.
- Special cases: a sum of $k$ iid [[Exponential Distribution|exponentials]] with mean $\beta$ is $\Gamma(k, \beta)$; a sum of independent [[Chi-Squared Distribution|chi-squared]] variables is chi-squared with the summed degrees of freedom ([[Chi-Squared Distribution Addition]]).

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=193)
