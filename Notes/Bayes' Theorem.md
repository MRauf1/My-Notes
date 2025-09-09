---
tags: statistics
---

# Definition

> [!info] Definition 1 (Bayes' Theorem)
> For [[Event|events]] $A, B$
> $$
> \begin{align}
> P(A | B) = \frac{P(B | A) P(A)}{P(B)}
> \end{align}
> $$

The original [[Probability|probability]] $P(A)$ is called the prior, while the new/updated [[Conditional Probability|conditional probability]] $P(A | B)$ is called the posterior.[^1] In other words, after experiencing an event $B$, the probability of event $A$ gets updated.

If $A$ is the unknown parameter, while $B$ is the probability of the data, then $P(B | A)$ is the likelihood of the data given the parameters.

If the prior is $1$ (no uncertainty about the prior), then the imperfect data will not update the prior (posterior = prior). Conversely, with perfect data, the prior becomes irrelevant.

[^1]: [Probability and Statistical Inference](zotero://open-pdf/library/items/RM5FREYV?page=45)