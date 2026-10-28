---
tags:
  - statistics
  - bayesian_statistics
---

# Definition
> [!info] Pivotal Quantity[^1]
> A nontrivial function $Q(y, \theta)$ of the data $y$ and the [[Estimand]] $\theta$ whose sampling distribution $p(Q \mid \theta)$ is independent of all parameters and of the data.

# Properties
- Normal model with unknown mean and variance:[^1] $y_1, \dots, y_n \overset{iid}{\sim} N(\mu, \sigma^2)$ gives
$$
\begin{align}
\frac{\bar{y} - \mu}{s/\sqrt{n}} \,\Big|\, \mu, \sigma^2 \sim t_{n-1}
\end{align}
$$
  ([[Student's Theorem]], [[t-Distribution]]), free of the [[Nuisance Parameter]] $\sigma^2$. Under the noninformative prior $p(\mu, \sigma^2) \propto \sigma^{-2}$, its posterior is also $t_{n-1}$, which does not depend on the data, so the Bayesian [[Credible Interval]] for $\mu$ coincides with the classical $t$ [[Confidence Interval]].
- Location and scale pivots, $y - \theta$ and $y/\theta$, characterize pure [[Location Parameter|location]] and [[Scale Parameter|scale]] parameters; requiring them to stay pivotal a posteriori yields the uniform and $1/\theta$ [[Noninformative Prior|noninformative priors]].
- Inverting $P(a < Q(y, \theta) < b) = 1 - \alpha$ for $\theta$ is the standard construction of a frequentist [[Confidence Interval]].

[^1]: [Gelman et al., p. 66](zotero://open-pdf/library/items/HDF44SF4?page=76&annotation=6JZI6GYL)
