---
tags:
  - statistics
  - bayesian_statistics
---

# Definition

Views [[Probability]] as - if an experiment was conducted many times and the [[Proportion]] of the times that [[Event]] $A$ occurs, the proportion would eventually converge to $P(A)$.[^1]

In a frequentist approach for inference, it bases all of it on the data and its distributions under the model, treating the parameters as fixed.

For this convergence to be meaningful, the repeated observations must be equivalent for the intended purpose, in particular made from equivalently prepared situations with the same degree of initial ignorance; the framework is inherently forward-looking, since probability is spoken of only for observations contemplated in the future.[^2]

# Properties
- The parameter $\mathbf{w}$ is fixed and determined by an estimator, and error bars on the estimate are obtained by considering the distribution of possible data sets $\mathcal{D}$, e.g. with the [[Bootstrap]].[^3]
- A widely used frequentist estimator is [[Maximum Likelihood Estimation|maximum likelihood]].[^4]
- Frequentist evaluation methods such as [[Cross-Validation]] offer protection against poor choices of prior in Bayesian methods and remain useful for [[Model Selection|model comparison]].[^5]
- There is no unique frequentist (or Bayesian) viewpoint, which has fueled the debate between the paradigms; in both, the [[Likelihood Function]] plays a central role, but it is used in fundamentally different ways.

[^2]: [The Feynman Lectures on Physics, Vol. I, Ch. 6: Probability](https://www.feynmanlectures.caltech.edu/I_06.html)
[^3]: [Bishop, 2006, p. 22](zotero://open-pdf/library/items/5G99AZ8U?page=42&annotation=69CVH8Q9)
[^4]: [Bishop, 2006, p. 23](zotero://open-pdf/library/items/5G99AZ8U?page=43&annotation=4KU9QTLZ)
[^5]: [Bishop, 2006, p. 23](zotero://open-pdf/library/items/5G99AZ8U?page=43&annotation=BX9FGPHT)

[^1]: [Bayesian Statistical Methods](zotero://open-pdf/library/items/ELV3M9SP?page=1)