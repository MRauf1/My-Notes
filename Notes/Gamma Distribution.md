---
tags:
  - statistics
  - bayesian_statistics
  - mathematical_statistics
---

# Definition

> [!info] Definition 1 (Gamma [[Probability Distribution]])[^1][^2]
> Gamma distribution, with [[Function Support]] $(0, \infty)$, denoted as $Gamma(\alpha, \theta)$ is 
> $$
> \begin{align}
> f(x) = \begin{cases}\frac{1}{\Gamma(\alpha) \theta^{\alpha}} x^{\alpha - 1} exp[-x/\theta] & x > 0\\ 0 & x \leq 0\end{cases}
> \end{align}
> $$
> with $\alpha > 0$, $\theta > 0$, where $\Gamma(\alpha)$ is the [[Gamma Function]]. The second parameter can alternatively be $\lambda = 1 / \theta$. Hogg et al. write the scale as $\beta$, i.e. $\Gamma(\alpha, \beta)$.

$\alpha$ is the [[Shape Parameter]], while $\theta$ is the [[Scale Parameter]]. $\lambda$ is the rate parameter.

**Intuition.** The gamma distribution is a flexible model for positive, right-skewed quantities: lifetimes, failure times, service times, and waiting times. For integer $\alpha = k$, it is the waiting time until the $k$th event of a [[Poisson Process]] with rate $\lambda = 1/\theta$, i.e. the sum of $k$ independent exponential waiting times each with mean $\theta$; general $\alpha > 0$ interpolates this "number of events waited for" continuously. Small $\alpha$ gives a sharply decreasing density concentrated near $0$, and as $\alpha$ grows the distribution becomes more symmetric and bell-shaped (approximately normal, by the central limit theorem applied to the sum of exponentials).

**Connection to the Poisson distribution.**[^3] The count of events and the waiting time are two descriptions of the same Poisson process: the wait for the $k$th event exceeds $w$ exactly when fewer than $k$ events occur by time $w$. So if counts in time $w$ are [[Poisson Distribution|Poisson]]$(\lambda w)$, the waiting time to the $k$th event is $Gamma(k, 1/\lambda)$, and $P(W_k > w) = \sum_{x=0}^{k-1} e^{-\lambda w}(\lambda w)^x/x!$.

# Types
- [[Exponential Distribution]]: $Gamma(1, \theta)$, the waiting time to the first event.
- Erlang distribution: $Gamma(k, \theta)$ with integer $k$, the waiting time to the $k$th event.
- [[Chi-Squared Distribution]]: $Gamma(r/2, 2)$, with $r$ degrees of freedom.

# Properties
## Basic Statistical Properties
- [[Gamma Distribution Expectation]]
- [[Gamma Distribution Variance]]
- [[Moment Generating Function|mgf]]:[^2] $M(t) = (1 - \theta t)^{-\alpha}$ for $t < 1/\theta$, which gives $\mu = \alpha\theta$ and $\sigma^2 = \alpha\theta^2$.

## Other
- [[Gamma Distribution Addition]]: independent gammas with a common scale add their shapes.
- Ratios of independent gammas with common scale give the [[Beta Distribution]], and normalized vectors of them the [[Dirichlet Distribution]]; the sum is independent of the proportions.
- The [[Conjugate Prior]] for a Poisson rate and for the precision of a normal.
- Mixing over a gamma-distributed rate gives thick-tailed distributions: the [[Negative Binomial Distribution]] (from a Poisson) and the [[Pareto Distribution]] (from a gamma).
- $e^X$ has the [[Loggamma Distribution]].

[^1]: [Bayesian Statistical Methods](zotero://open-pdf/library/items/ELV3M9SP?page=21)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=190)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=193)
