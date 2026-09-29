---
tags:
  - statistics
  - statistical_learning
---

# Definition

> [!info] Definition 1 (Naive [[Bayes' Theorem|Bayes]] Classifier)
> ...
> $$
> \begin{align}
> ...
> \end{align}
> $$

Naive Bayes Classifier, for a test observation with predictor vector $x$, it assigns the test observation to the class $j$ for which $P(Y = j | X = x)$ is maximized.[^1]

# Properties
- Rests on the assumption that the inputs are conditionally independent given the class, $p(\mathbf{x}_I, \mathbf{x}_B | \mathcal{C}_k) = p(\mathbf{x}_I | \mathcal{C}_k)\,p(\mathbf{x}_B | \mathcal{C}_k)$; the marginal $p(\mathbf{x}_I, \mathbf{x}_B)$ will typically not factorize under this model.[^2]
- Applies the [[Minimum Misclassification Rate Decision Rule]].

[^1]: [Introduction to Statistical Learning with Python](zotero://open-pdf/library/items/9JTAJ2JI?page=45)
[^2]: [Bishop, 2006, p. 46](zotero://open-pdf/library/items/5G99AZ8U?page=66&annotation=A6H63P2K)