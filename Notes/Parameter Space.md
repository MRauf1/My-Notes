---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Parameter and Parameter Space[^1]
> When the pdf or pmf of a random variable $X$ is known up to an unknown quantity $\theta$ (possibly a vector), we write it as $f(x; \theta)$ or $p(x; \theta)$ with $\theta \in \Omega$ for a specified set $\Omega$. $\theta$ is a parameter of the distribution, and $\Omega$ is the parameter space.

Hogg et al. classify ignorance about the distribution of $X$ in two ways:
1. $f$ or $p$ is completely unknown: nonparametric inference, e.g. [[Histogram|histograms]] and [[Kernel Density Estimation|kernel density estimates]].
2. The form of $f$ or $p$ is known down to $\theta$: parametric inference, where the problem reduces to learning $\theta$ from a sample ([[Estimator|estimation]], [[Confidence Interval|confidence intervals]], [[Statistical Hypothesis Test|tests]]).

# Properties
- The family $\{f(\cdot; \theta) : \theta \in \Omega\}$ is a parametric model ([[Statistical Learning Parametric Model]]); a nonparametric model cannot be indexed by a finite-dimensional $\theta$ ([[Statistical Learning Non-Parametric Model]]).
- Hypothesis testing partitions the parameter space, $\Omega = \omega_0 \cup \omega_1$ with $\omega_0 \cap \omega_1 = \emptyset$.
- The notation $P_\theta$ and $E_\theta$ means probability and expectation computed under the distribution $f(\cdot; \theta)$, i.e. assuming $\theta$ is the true parameter.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=241)
