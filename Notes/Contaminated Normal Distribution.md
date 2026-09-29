---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Contaminated Normal Distribution[^1]
> Let $Z \sim N(0, 1)$ and, independently, $I_{1-\epsilon} \sim$ [[Bernoulli Distribution|Bernoulli]]$(1 - \epsilon)$ for a contamination proportion $0 < \epsilon < 1$, and let $\sigma_c > 1$. The standardized contaminated normal variable is
> $$
> \begin{align}
> W = Z I_{1-\epsilon} + \sigma_c Z (1 - I_{1-\epsilon})
> \end{align}
> $$
> with cdf and pdf
> $$
> \begin{align}
> F_W(w) = (1 - \epsilon)\Phi(w) + \epsilon\,\Phi\left(\frac{w}{\sigma_c}\right), \qquad f_W(w) = (1 - \epsilon)\phi(w) + \frac{\epsilon}{\sigma_c}\phi\left(\frac{w}{\sigma_c}\right)
> \end{align}
> $$
> where $\Phi, \phi$ are the standard [[Normal Distribution|normal]] cdf and pdf.

It models data that are mostly "good" (standard normal) but occasionally outliers from a normal with larger spread. The cdf follows from the [[Law of Total Probability]] over the value of $I_{1-\epsilon}$.

# Properties
- $E(W) = 0$ and $\text{Var}(W) = 1 + \epsilon(\sigma_c^2 - 1)$.
- General form $X = a + bW$ with $b > 0$: $E(X) = a$, $\text{Var}(X) = b^2[1 + \epsilon(\sigma_c^2 - 1)]$, and $F_X(x) = (1-\epsilon)\Phi\left(\frac{x - a}{b}\right) + \epsilon\,\Phi\left(\frac{x - a}{b\sigma_c}\right)$.
- A two-component [[Mixture Distribution]] of normals with equal means; its tails are heavier than a normal with the same variance, which is why it is used to study the robustness of estimators.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=209)
