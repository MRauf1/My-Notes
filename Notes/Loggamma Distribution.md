---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Loggamma Distribution[^1]
> $X$ has a loggamma distribution $\log\Gamma(\alpha, \beta)$ with $\alpha > 0$, $\beta > 0$ if its pdf is
> $$
> \begin{align}
> f(x) = \frac{1}{\Gamma(\alpha)\beta^\alpha} x^{-(1+\beta)/\beta}(\log x)^{\alpha - 1}, \quad x > 1
> \end{align}
> $$
> and zero elsewhere.

It is the distribution of $X = e^Y$ for $Y \sim$ [[Gamma Distribution|$\Gamma(\alpha, \beta)$]], by the [[Cumulative Distribution Function Transformation Technique|change-of-variable]] formula: $f_X(x) = f_Y(\log x)/x$.

# Properties
- Heavy right tail: the density decays like a power of $x$ (times a log factor), so only moments of order $k < 1/\beta$ exist; in particular $E(X) = (1 - \beta)^{-\alpha}$ for $\beta < 1$ (the gamma mgf at $t = 1$).
- Used as a heavy-tailed component in [[Mixture Distribution|mixtures]], e.g. for insurance claim sizes.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=235)
