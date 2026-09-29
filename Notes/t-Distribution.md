---
tags:
  - statistics
  - statistical_learning
  - mathematical_statistics
---

# Definition
> [!info] Student's t-Distribution[^2]
> Let $W \sim N(0, 1)$ and $V \sim$ [[Chi-Squared Distribution|$\chi^2(r)$]] be independent. Then
> $$
> \begin{align}
> T = \frac{W}{\sqrt{V/r}}
> \end{align}
> $$
> has the t-distribution with $r$ degrees of freedom, with pdf
> $$
> \begin{align}
> g_1(t) = \frac{\Gamma[(r+1)/2]}{\sqrt{\pi r}\,\Gamma(r/2)}\frac{1}{(1 + t^2/r)^{(r+1)/2}}, \quad -\infty < t < \infty
> \end{align}
> $$

The pdf is found by the [[Random Vector Transformation|change-of-variable]] technique on $(W, V)$ and integrating out the auxiliary variable. The distribution is determined by the single parameter $r$, the degrees of freedom of the chi-squared variable. It was discovered by W. S. Gosset, who published under the pseudonym "Student".[^3]

Intuitively, $T$ is a standard normal whose scale is itself estimated: the denominator $\sqrt{V/r}$ is a noisy estimate of $1$, and the extra noise fattens the tails. This is why it appears when a normal mean is standardized by an estimated rather than known standard deviation ([[Student's Theorem]]).

For $n \geq 30$, it is similar to the [[Normal Distribution]].[^1]

# Properties
- Symmetric about $0$ ($g_1(-t) = g_1(t)$), with median $0$ and a unique mode at $0$: mound shaped like the normal but with heavier tails.
- As $r \to \infty$, it converges to $N(0, 1)$.
- Moments:[^3] $E(T^k)$ exists only for $k < r$, with $E(T^k) = E(W^k)\,\frac{2^{-k/2}\,\Gamma\left(\frac{r-k}{2}\right)}{\Gamma\left(\frac{r}{2}\right)\,r^{-k/2}}$. Hence $E(T) = 0$ for $r > 1$ and $\text{Var}(T) = \frac{r}{r - 2}$ for $r > 2$.
- $r = 1$ gives the [[Cauchy Distribution]], which has no mean.
- $T^2 \sim$ [[F-Distribution|$F(1, r)$]].
- Used in the $t$-test and $t$ confidence intervals ([[t-Test Statistic]]).

[^1]: [Introduction to Statistical Learning with Python](zotero://open-pdf/library/items/9JTAJ2JI?page=86)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=226)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=228)
