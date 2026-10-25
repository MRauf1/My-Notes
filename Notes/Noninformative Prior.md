---
tags:
  - statistics
  - bayesian_statistics
---

# Definition
> [!info] Noninformative Prior[^1]
> A [[Prior Distribution]] intended to play a minimal role in the [[Posterior Distribution]], so that inferences are unaffected by information external to the current data ("let the data speak for themselves"). Also called a reference, vague, flat, or diffuse prior.

The motivation is that, when the prior has no population basis, it can be difficult to construct.

# Types
- **Uniform on a location parameter.** If $p(y - \theta \mid \theta) = f(y - \theta)$ is free of $\theta$ and $y$, then $y - \theta$ is a pivotal quantity and $\theta$ a pure [[Location Parameter]]. Requiring $y - \theta$ to remain pivotal under the posterior, $p(y - \theta \mid y) = f(y - \theta)$, together with $p(y - \theta \mid y) \propto p(\theta)\, p(y - \theta \mid \theta)$, forces[^2][^3]
$$
\begin{align}
p(\theta) \propto \text{const} \quad \text{on } (-\infty, \infty)
\end{align}
$$
- **$1/\theta$ on a scale parameter.** If $p(y/\theta \mid \theta) = g(y/\theta)$ is free of $\theta$ and $y$, then $u = y/\theta$ is pivotal and $\theta$ a pure [[Scale Parameter]]. By [[Change of Variables]], $p(y \mid \theta) = \frac{1}{\theta}p(u \mid \theta)$ and $p(\theta \mid y) = \frac{y}{\theta^2}p(u \mid y)$. Setting both $p(u \mid \theta)$ and $p(u \mid y)$ to $g(u)$ gives $p(\theta \mid y) = \frac{y}{\theta}p(y \mid \theta)$, hence[^4]
$$
\begin{align}
p(\theta) \propto \frac{1}{\theta} \iff p(\log\theta) \propto 1 \iff p(\theta^2) \propto \frac{1}{\theta^2}
\end{align}
$$
- [[Jeffreys Prior]]: $p(\theta) \propto J(\theta)^{1/2}$, invariant to reparameterization.

# Properties
- Usually [[Improper Prior|improper]]; the posterior must be checked for propriety.
- For the binomial and other single-parameter models, different principles give slightly different noninformative priors, but for location and scale parameters all principles agree on the two forms above.[^5] These are also the right Haar measures of the translation and scaling groups ([[Probability Matching Prior]]).
- Even these principles can mislead, by suggesting priors that yield improper posteriors (e.g. uniform on the log of a hierarchical variance).[^6]
- Problems with the search for noninformative priors:[^7]
  1. If the likelihood truly dominates, the choice among relatively flat priors cannot matter; canonizing one "reference" prior encourages automatic, possibly inappropriate use.
  2. **No scale-free notion of flatness.** A density flat in one parameterization is not flat in another. This is the essential difficulty with Laplace's principle of insufficient reason: on what scale should it apply? E.g. $p(\sigma^2) \propto 1/\sigma^2$ is exactly uniform in $\phi = \log\sigma^2$, since $p(\phi) = p(\sigma^2)\left|\frac{d\sigma^2}{d\phi}\right| \propto \frac{1}{\sigma^2}\sigma^2 = 1$. For discrete distributions the analogous difficulty is choosing the "atoms" of equal probability.
  3. Averaging over competing models with improper priors is ill-defined.
- Nevertheless useful when quantifying real prior knowledge is not worth the effort, provided one checks that the posterior is proper and assesses the sensitivity of inferences to these assumptions of convenience.[^7]
- In multiparameter problems, Gelman et al. prefer [[Hierarchical Model|hierarchical models]] and [[Weakly Informative Prior|weakly informative priors]] to pure noninformative priors.

[^1]: [Gelman et al., p. 51](zotero://open-pdf/library/items/HDF44SF4?page=61&annotation=FEESI5NA)
[^2]: [Gelman et al., p. 53](zotero://open-pdf/library/items/HDF44SF4?page=63&annotation=8VPVKHBC)
[^3]: [Gelman et al., p. 54](zotero://open-pdf/library/items/HDF44SF4?page=64&annotation=GFBBHK8C)
[^4]: [Gelman et al., p. 54](zotero://open-pdf/library/items/HDF44SF4?page=64&annotation=GKE5IS3I)
[^5]: [Gelman et al., p. 53](zotero://open-pdf/library/items/HDF44SF4?page=63&annotation=3S2DAKDQ)
[^6]: [Gelman et al., p. 54](zotero://open-pdf/library/items/HDF44SF4?page=64&annotation=3SUJ9DYU)
[^7]: [Gelman et al., p. 54](zotero://open-pdf/library/items/HDF44SF4?page=64&annotation=TBM6RC9R)
