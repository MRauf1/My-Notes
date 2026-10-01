---
tags:
  - statistics
  - statistical_learning
---

# Definition

For a $x\%$ confidence interval, it is an [[Interval Notation|interval]] such that with $x\%$ probability, the interval will contain the true unknown value of the parameter.[^1] The estimate $\pm$ z-score $\times$ standard error form is not general: it relies on the estimator being (approximately) normally distributed, which does not hold for every parameter or sample size.

> [!info] Definition 2 (Confidence Interval)[^2]
> Let $X_1, \dots, X_n$ be a sample on $X$ with pdf $f(x; \theta)$, $\theta \in \Omega$, let $0 < \alpha < 1$, and let $L = L(X_1, \dots, X_n)$ and $U = U(X_1, \dots, X_n)$ be two [[Statistic|statistics]]. $(L, U)$ is a $(1 - \alpha)100\%$ confidence interval for $\theta$ if
> $$
> \begin{align}
> P_\theta[\theta \in (L, U)] = 1 - \alpha
> \end{align}
> $$
> $1 - \alpha$ is the confidence coefficient (confidence level).

**Interpretation.**[^3] The randomness is in the endpoints, not in $\theta$. Once the sample is drawn, the realized interval $(l, u)$ either traps $\theta$ or it does not. The procedure is a Bernoulli trial with success probability $1 - \alpha$: over $M$ independent $(1-\alpha)100\%$ intervals, about $(1 - \alpha)M$ trap their parameters, which is the sense in which one is "$(1-\alpha)100\%$ confident" about a particular $(l, u)$. The Bayesian counterpart, a [[Credible Interval|credible interval]], makes a probability statement about $\theta$ itself.

# Types
- $t$-interval for a normal mean: $\bar{x} \pm t_{\alpha/2, n-1}\,s/\sqrt{n}$ ([[Student's Theorem]]), where $s/\sqrt{n}$ is the [[Standard Error]] of $\bar{X}$.[^3]
- Large-sample interval $\bar{x} \pm z_{\alpha/2}\,s/\sqrt{n}$, justified by the [[Central Limit Theorem]].[^4]
- [[Two-Sample Confidence Interval for Difference of Means]], [[Difference of Proportions Confidence Interval]].
- [[Exact Confidence Interval for Discrete Distribution]], [[Distribution-Free Confidence Interval for Quantile]], [[Percentile Bootstrap Confidence Interval]].
- Related but different: the [[Tolerance Interval]], which covers a proportion of the population rather than a parameter.

# Properties
- Efficiency:[^3] among intervals with the same confidence coefficient, $(L_1, U_1)$ is more efficient than $(L_2, U_2)$ if $E_\theta(U_1 - L_1) \leq E_\theta(U_2 - L_2)$ for all $\theta \in \Omega$.
- Duality with tests: the interval consists of the $\theta_0$ not rejected by a level-$\alpha$ [[Statistical Hypothesis Test]] of $H_0: \theta = \theta_0$.
- Coverage is a frequentist, vertical-slice property that must hold at every $\theta$. A Bayesian credible interval has exactly this coverage only under a [[Probability Matching Prior]], and approximately for large $n$ in regular models ([[Bernstein-von Mises Theorem]], [[Frequentist vs Bayesian Inference]]).

[^1]: [Introduction to Statistical Learning with Python](zotero://open-pdf/library/items/9JTAJ2JI?page=84)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=254)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=255)
[^4]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=256)
