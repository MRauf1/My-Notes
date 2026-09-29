---
tags:
  - statistics
  - bayesian_statistics
---

# Definition

Views [[Probability]] from both the [[Probability Objective Interpretation]] and [[Probability Subjective Interpretation]].[^1]

In a Bayesian framework, for inference, unlike [[Probability Frequentist Framework]] for inference, the Bayesians treat the parameters as random.

# Properties
- Quantifies uncertainty and revises it precisely in light of new evidence via [[Bayes' Theorem]], and then supports optimal actions via [[Decision Theory]].[^2]
- Using probability for degrees of belief is not ad hoc: by [[Cox's Theorem]], common-sense axioms for rational belief force the sum and product rules.[^3]
- The machinery of probability describes uncertainty in model parameters $\mathbf{w}$, and even in the choice of model itself.[^4]
- There is only a single data set $\mathcal{D}$, the one actually observed; uncertainty in the parameters is expressed through a probability distribution over $\mathbf{w}$, in contrast to the [[Probability Frequentist Framework|frequentist]] distribution over possible data sets.[^5]
- Prior knowledge enters naturally, avoiding extreme conclusions from little data (e.g. estimating $P(\text{heads}) = 1$ after three heads, as [[Maximum Likelihood Estimation|maximum likelihood]] does).[^6]
- Full Bayesian prediction marginalizes over parameters ([[Predictive Distribution]]), which avoids [[Overfitting|over-fitting]]; see [[Maximum Likelihood vs Maximum a Posteriori Estimation]] for the intermediate point-estimate case.

[^1]: [Bayesian Statistical Methods](zotero://open-pdf/library/items/ELV3M9SP?page=1)
[^2]: [Bishop, 2006, p. 21](zotero://open-pdf/library/items/5G99AZ8U?page=41&annotation=6U6NDTRR)
[^3]: [Bishop, 2006, p. 21](zotero://open-pdf/library/items/5G99AZ8U?page=41&annotation=EQMAW866)
[^4]: [Bishop, 2006, p. 22](zotero://open-pdf/library/items/5G99AZ8U?page=42&annotation=GBXB8RKB)
[^5]: [Bishop, 2006, p. 23](zotero://open-pdf/library/items/5G99AZ8U?page=43&annotation=8J6ISJH4)
[^6]: [Bishop, 2006, p. 23](zotero://open-pdf/library/items/5G99AZ8U?page=43&annotation=I67L46V2)