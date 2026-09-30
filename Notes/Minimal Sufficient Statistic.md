---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Minimal Sufficient Statistic[^1]
> A set of jointly [[Sufficient Statistic|sufficient statistics]] is minimal sufficient if it is sufficient for the parameters and is a function of every other set of sufficient statistics for those same parameters.

Minimal sufficient statistics are what remains after changing from one set of sufficient statistics to another, reducing the number of statistics each time, until no further reduction is possible without losing sufficiency. In the partition view, the minimal sufficient statistic induces the coarsest partition of the sample space that is still sufficient.

# Properties
- Dimension: with $k$ parameters, there are often $k$ jointly minimal sufficient statistics, and a single one for one parameter. This is not always the case, however. For example, the location family of the [[Cauchy Distribution]] has the order statistics as its minimal sufficient statistic.
- MLE criterion:[^2] the [[Maximum Likelihood Estimation|MLE]] $\hat{\theta}$ is a function of any sufficient statistic (Theorem 7.3.2). So if $\hat{\theta}$ is itself sufficient, it is minimal. This shows that the sufficient statistics of most standard models are minimal:
  - $\bar{X}$ for $N(\theta, \sigma^2)$ with $\sigma^2$ known;
  - $\bar{X}$ for [[Poisson Distribution|Poisson]]$(\theta)$;
  - $Y_n = \max X_i$ for the uniform on $(0, \theta)$;
  - $(\bar{X}, \frac{n-1}{n}S^2)$ for $N(\theta_1, \theta_2)$.
- Not unique:[^3] any one-to-one transformation of a minimal sufficient statistic is minimal sufficient. The link between minimal sufficiency and the MLE fails in many interesting models, where the MLE is not sufficient.
- Likelihood-ratio characterization (Lehmann-Scheffé): $T$ is minimal sufficient if, for all sample points $\mathbf{x}, \mathbf{y}$, the ratio $f(\mathbf{x}; \theta)/f(\mathbf{y}; \theta)$ is free of $\theta$ exactly when $T(\mathbf{x}) = T(\mathbf{y})$. Equivalently, the minimal sufficient statistic indexes the shape of the likelihood function.
- A complete sufficient statistic is minimal (Bahadur), but a minimal sufficient statistic need not be complete ([[Complete Family (Statistics)]]). When it is not complete, an [[Ancillary Statistic]] can still carry information ([[Basu's Theorem]]).

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=471&annotation=XSDKVMSM)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=471&annotation=7PCMYYZJ)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=472&annotation=F6NVV27K)
