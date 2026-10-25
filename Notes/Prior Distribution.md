---
tags:
  - statistics
  - bayesian_statistics
---

# Definition
> [!info] Prior Distribution[^1]
> In a Bayesian model for parameters $\theta$ and data $y$, the joint [[Joint Probability Distribution|probability distribution]] factors as
> $$
> \begin{align}
> p(\theta, y) = p(\theta)\, p(y \mid \theta)
> \end{align}
> $$
> The [[Marginal Distribution|marginal]] $p(\theta)$ is the prior distribution: the uncertainty about $\theta$ before the data $y$ are observed.

Two basic interpretations:[^2]
- **Population interpretation**: the prior represents a population of possible parameter values from which the current $\theta$ was drawn.
- **State-of-knowledge interpretation**: we express our knowledge and uncertainty about $\theta$ as if its value were a random realization from the prior. Often no relevant population exists except in hypothetical contemplation.

# Types
- [[Conjugate Prior]]
- [[Noninformative Prior]] (e.g. [[Jeffreys Prior]])
- [[Weakly Informative Prior]]
- Proper vs [[Improper Prior]]

# Properties
- The prior should include all plausible values of $\theta$, but need not be realistically concentrated around the true value, since the information in the data often far outweighs any reasonable prior specification.[^2]
- Its parameters are called [[Hyperparameter|hyperparameters]].[^3]
- The second factor $p(y \mid \theta)$ is the [[Data Distribution]]; conditioning the joint on observed $y$ turns the prior into the [[Posterior Distribution]] via [[Bayes' Theorem]].
- Averaging the data distribution over the prior gives the [[Prior Predictive Distribution]].
- Under the [[Probability Bayesian Framework]], the prior encodes the state of knowledge about $\theta$ as a probability distribution.
- How to choose it: [[Prior Distribution Selection]], [[Conjugate Prior]], [[Probability Matching Prior]].

[^1]: [Gelman et al., p. 6](zotero://open-pdf/library/items/HDF44SF4?page=16&annotation=BF4BS4G6)
[^2]: [Gelman et al., p. 34](zotero://open-pdf/library/items/HDF44SF4?page=44&annotation=C9BT4SQP)
[^3]: [Gelman et al., p. 34](zotero://open-pdf/library/items/HDF44SF4?page=44&annotation=S8A6Y8V2)
