---
tags:
  - statistics
  - bayesian_statistics
---

# Definition
> [!info] Bayesian Inference[^1][^2]
> The process of fitting a probability model to data and summarizing the result by a probability distribution on the model parameters and on unobserved quantities such as predictions for new observations. Its essential characteristic is the explicit use of probability to quantify uncertainty in inferences.

> [!info] Bayesian Data Analysis[^3]
> An idealized three-step process:
> 1. Set up a full probability model: a [[Joint Probability Distribution]] $p(\theta, y) = p(\theta)\,p(y \mid \theta)$ for all observable and unobservable quantities, consistent with knowledge of the scientific problem and the data collection process.
> 2. Condition on observed data: compute and interpret the [[Posterior Distribution]] $p(\theta \mid y)$ of the unobserved quantities of interest.
> 3. Evaluate the fit of the model and the implications of the posterior: how well the model fits the data, whether the conclusions are reasonable, and how sensitive the results are to the modeling assumptions of step 1. In response, alter or expand the model and repeat.

The technical core is the posterior $p(\theta \mid y) \propto p(\theta)\,p(y \mid \theta)$: the primary task of any application is to develop the model $p(\theta, y)$ and compute summaries of $p(\theta \mid y)$.[^4]

A finer-grained workflow:
1) Define the data model
2) Obtain the likelihood function
3) Specify a prior density
4) Determine the posterior
5) Use the posterior to make [[Inference]]

# Properties
- A form of [[Statistical Inference]]; its [[Estimand|estimands]] are parameters (via the posterior) and observables (via the [[Prior Predictive Distribution]] and posterior [[Predictive Distribution]]).
- Model components: [[Prior Distribution]] $p(\theta)$ and [[Data Distribution]] $p(y \mid \theta)$; the data affect inference only through the [[Likelihood Function]], so it obeys the [[Likelihood Principle]].[^5]
- The usual starting assumption is [[Exchangeability]] of the data, modeled as iid given $\theta$; multi-level data use a [[Hierarchical Model]].
- Common-sense interpretation of conclusions: a [[Credible Interval]] directly has high probability of containing the unknown quantity ([[Frequentist vs Bayesian Inference]]).
- Philosophical basis: [[Probability Bayesian Framework]].
- When the posterior's normalizing constant is intractable, it is sampled by [[Markov Chain Monte Carlo]].

[^1]: [Gelman et al., p. 1](zotero://open-pdf/library/items/HDF44SF4?page=11&annotation=TFGB8IG4)
[^2]: [Gelman et al., p. 3](zotero://open-pdf/library/items/HDF44SF4?page=13&annotation=IRCHE8N4)
[^3]: [Gelman et al., p. 3](zotero://open-pdf/library/items/HDF44SF4?page=13&annotation=PC55PE8P)
[^4]: [Gelman et al., p. 7](zotero://open-pdf/library/items/HDF44SF4?page=17&annotation=C69MVM7Y)
[^5]: [Gelman et al., p. 7](zotero://open-pdf/library/items/HDF44SF4?page=17&annotation=PU6SRI86)
