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

**The semicolon in $f(x; \theta)$.** $f(x; \theta)$ is the pdf or pmf of $X$ when the parameter equals $\theta$. It is framed in the frequentist way, as opposed to the Bayesian way.
- $\theta$ is not a random variable here. It is a fixed but unknown constant in $\Omega$, so $f(x; \theta)$ is not a joint pdf of $(X, \theta)$. It is also not a conditional pdf in the probabilistic sense, since there is no distribution on $\theta$ to condition on.
- The semicolon separates the argument $x$, which is the variable of the function, from $\theta$, which indexes which member of the family $\{f(\cdot; \theta) : \theta \in \Omega\}$ is meant. It reads "the pdf of $X$ under the fixed parameter value $\theta$". For example, $f(x; \mu, \sigma^2)$ is the height of the normal curve at $x$ for frozen values of $\mu$ and $\sigma^2$.
- The vertical bar $f(x \mid \theta)$ is reserved for the Bayesian setting, where $\theta$ is itself a random variable with a prior. There, $f(x \mid \theta)$ is a genuine conditional density and $f(x \mid \theta)\pi(\theta)$ is a joint density ([[Bayes Estimator]], [[Bayes' Theorem]]). Numerically the two formulas coincide; the notation signals which interpretation of $\theta$ is in force.
- The same convention applies to $P_\theta$ and $E_\theta$ below, and to the [[Likelihood Function]] $L(\theta; \mathbf{x})$, a function of $\theta$ for fixed data.

# Properties
- The family $\{f(\cdot; \theta) : \theta \in \Omega\}$ is a parametric model ([[Statistical Learning Parametric Model]]); a nonparametric model cannot be indexed by a finite-dimensional $\theta$ ([[Statistical Learning Non-Parametric Model]]).
- Hypothesis testing partitions the parameter space, $\Omega = \omega_0 \cup \omega_1$ with $\omega_0 \cap \omega_1 = \emptyset$.
- The notation $P_\theta$ and $E_\theta$ means probability and expectation computed under the distribution $f(\cdot; \theta)$, i.e. assuming $\theta$ is the true parameter.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=241)
