---
tags: statistics, bayesian_statistics
---

# Definition

> [!info] Definition 1 (Bayes' Theorem)
> For [[Event|events]] $A, B$
> $$
> \begin{align}
> P(A | B) = \frac{P(B | A) P(A)}{P(B)}
> \end{align}
> $$

> [!info] Definition 2 (Bayes' Theorem in Bayesian Inference)[^2]
> For data $Y$ and parameters $\theta$, the Bayes' Theorem is
> $$
> \begin{align}
> P(\theta | Y) = \frac{P(Y | \theta) P(\theta)}{P(Y)} \propto P(Y | \theta) P(\theta)
> \end{align}
> $$
> where $P(Y)$ can be expressed as the [[Marginal Distribution]] $P(Y) = \int P(Y | \theta) P(\theta) d\theta$


The original [[Probability|probability]] $P(\theta)$ is called the prior, while the new/updated [[Conditional Probability|conditional probability]] $P(\theta | Y)$ is called the posterior.[^1] $P(Y | \theta)$ is the likelihood of the data given the parameters. In other words, given the observed data $Y$, the probability of parameters $\theta$ gets updated.

If the prior is $1$ (no uncertainty about the prior), then the imperfect data will not update the prior (posterior = prior). Conversely, with perfect data, the prior becomes irrelevant.

#TODO 
Do I have the likelihood function correct? Look into it.
Does the likelihood function for $\theta$ ($L(\theta | Y)$) equal the above probability $P(Y | \theta)$?

[^1]: [Probability and Statistical Inference](zotero://open-pdf/library/items/RM5FREYV?page=45)
[^2]: [Bayesian Statistical Methods](zotero://open-pdf/library/items/ELV3M9SP?page=34)