---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Probability Matching Prior
> A prior $\pi(\theta)$ is probability matching if the posterior $(1-\alpha)$ credible interval has frequentist coverage $1 - \alpha$, either exactly or up to a specified order in $n$:
> $$
> \begin{align}
> P_\theta\left(\theta \leq \theta_{1-\alpha}(X)\right) = 1 - \alpha + O(n^{-r})
> \end{align}
> $$
> for all $\theta$, where $\theta_{1-\alpha}(x)$ is the posterior $(1-\alpha)$ quantile.

Probability matching priors are the cases where the vertical (frequentist) and horizontal (Bayesian) slices agree at every sample size, not just asymptotically ([[Frequentist vs Bayesian Inference]]). The agreement comes from the symmetry of the model.

# Properties
- Normal mean with known variance and a flat prior: the 95% credible interval is exactly the 95% [[Confidence Interval]] $\bar{x} \pm 1.96\,\sigma/\sqrt{n}$.
- Location and scale families: the right Haar measure of the group gives credible intervals with exact frequentist coverage. It is $d\theta$ for a location parameter and $d\sigma/\sigma$ for a scale parameter ([[Location Parameter]], [[Scale Parameter]]).
- In one-parameter models, the Jeffreys prior $\pi(\theta) \propto \sqrt{I(\theta)}$ ([[Fisher Information]]) is first-order matching. Its coverage error is $O(n^{-1})$ instead of the generic $O(n^{-1/2})$ ([[Prior Distribution Selection]]).
- Without such a prior, agreement holds only asymptotically ([[Bernstein-von Mises Theorem]]).
