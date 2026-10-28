---
tags:
  - statistics
  - bayesian_statistics
---

# Definition
> [!info] Bayesian Posterior Simulation Strategy[^1]
> A recipe for computing simple Bayesian posteriors (not fully general; a precursor to successive-approximation methods):
> 1. Write the [[Likelihood Function]] $p(y \mid \theta)$, dropping factors free of $\theta$.
> 2. Write the [[Posterior Distribution|posterior]] $p(\theta \mid y) \propto p(\theta)\, p(y \mid \theta)$. Use well-formulated prior information if available; otherwise a [[Weakly Informative Prior]] or temporarily $p(\theta) \propto \text{constant}$, to be refined later.
> 3. Form a crude estimate of $\theta$ as a starting point and a check on the next step.
> 4. Draw $\theta^1, \dots, \theta^S$ from $p(\theta \mid y)$, and use them to compute the posterior of any function of $\theta$ of interest.
> 5. For predictive quantities, draw each $\tilde{y}^s \sim p(\tilde{y} \mid \theta^s)$, giving draws from the posterior [[Predictive Distribution]].

# Properties
- Step 4 is the hard part for nonconjugate models. With one or two parameters, draws can be made by computing the posterior on a grid; in high dimensions, [[Markov Chain Monte Carlo]] and related methods are used, sometimes combined with analytic steps (e.g. [[Marginal Posterior Distribution|marginal and conditional simulation]]).[^1]
- Draws of $\theta$ and $\tilde{y}$ are reused to check model fit against data and substantive knowledge.[^1]
- **Why few conjugate multiparameter models is not a handicap:**[^2] (i) with few parameters, nonconjugate posteriors are handled by simple simulation; (ii) sophisticated models can often be written hierarchically or conditionally ([[Hierarchical Model]]), with effective computational strategies; (iii) a normal approximation to the posterior ([[Bernstein-von Mises Theorem]]) lets the conjugate normal structure apply well beyond explicitly normal sampling models.
- Posterior inferences are only as good as the model and the experiment that produced the data: a correctly computed 95% posterior interval can still miss the true value under model or measurement error.[^3]
- Built on [[Monte Carlo Method|Monte Carlo]] summaries of the draws ([[Monte Carlo Estimator]]).

[^1]: [Gelman et al., p. 78](zotero://open-pdf/library/items/HDF44SF4?page=88&annotation=DA4ADNBP)
[^2]: [Gelman et al., p. 78](zotero://open-pdf/library/items/HDF44SF4?page=88&annotation=A8SFBX6H)
[^3]: [Gelman et al., p. 67](zotero://open-pdf/library/items/HDF44SF4?page=77&annotation=TBR7U9N5)
