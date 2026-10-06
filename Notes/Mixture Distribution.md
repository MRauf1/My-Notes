---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Finite Mixture Distribution[^1]
> Let $f_1, \dots, f_k$ be pdfs with supports $\mathcal{S}_i$, means $\mu_i$, and variances $\sigma_i^2$, and let $p_1, \dots, p_k > 0$ be mixing probabilities with $\sum_i p_i = 1$. The mixture pdf on $\mathcal{S} = \bigcup_i \mathcal{S}_i$ is
> $$
> \begin{align}
> f(x) = \sum_{i=1}^k p_i f_i(x), \qquad F(x) = \sum_{i=1}^k p_i F_i(x)
> \end{align}
> $$
> (pmfs are handled the same way).

> [!info] Compound (Continuous) Mixture[^2]
> Let $f(x | \theta)$ be a pdf for each value of a parameter $\theta$, and let $g(\theta)$ be a pdf for $\theta$ (the weighting function). The compound pdf is
> $$
> \begin{align}
> h(x) = \int_\theta g(\theta)\,f(x | \theta)\,d\theta
> \end{align}
> $$
> with a sum when $\theta$ is discrete. Mixing is also called compounding.

A mixture is drawn in two stages: first pick a component (or a parameter value $\theta$) at random according to the mixing distribution, then draw $X$ from that component. The joint pdf of $(X, \theta)$ is $f(x|\theta)g(\theta)$, and the compound pdf is the [[Marginal Distribution]] of $X$, i.e. the [[Law of Total Probability]] for densities. A finite mixture is the case where $\theta$ is discrete with pmf $p_i$.

**Roles of $X$ and the "original distribution".** $X$ is the observed variable throughout. Its "original distribution" is the component, or [[Conditional Distribution|conditional]], distribution $f(x | \theta)$: the law of $X$ if $\theta$ were known (e.g. Poisson with rate $\theta$). The mixture is not treated as the original distribution. Rather, the compound pdf $h(x)$ is the unconditional distribution of that same $X$ once the uncertainty about $\theta$ is averaged out. So the original distribution is the conditional one, and the mixture is its marginal.

# Properties
- Mean: $E(X) = \sum_i p_i\mu_i = \mu$, a weighted average of the component means ([[Law of Total Expectation]]).[^1]
- Variance:[^3]
$$
\begin{align}
\text{Var}(X) = \sum_{i=1}^k p_i\sigma_i^2 + \sum_{i=1}^k p_i(\mu_i - \mu)^2
\end{align}
$$
  the average within-component variance plus the variance of the component means, since the cross terms integrate to zero. This is the [[Law of Total Variance]] with the component label as the conditioning variable, so a mixture is more spread out than its average component.
- A mixture is not a [[Linear Combination of Random Variables]]: the pdf $\sum p_i f_i$ is a weighted average of densities, whereas $\sum a_i X_i$ is a weighted sum of random variables with a convolution-type pdf, and their means and variances follow different rules.[^3]
- Compounding typically thickens tails: Poisson with a gamma-distributed rate gives the [[Negative Binomial Distribution]], and a gamma with a gamma-distributed rate gives the (generalized) [[Pareto Distribution]].
- Examples: the [[Contaminated Normal Distribution]], the [[Mixture of Gaussians]] (a [[Latent Variable Model|latent variable model]] with a categorical latent), and the prior predictive $\int p(y|\theta)p(\theta)\,d\theta$ in [[Bayes' Theorem|Bayesian inference]].
- Not to be confused with a [[Mixture Random Variable]], whose cdf mixes a discrete and a continuous part (though such a variable is itself a two-component mixture in this sense).

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=234)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=236)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=235)
