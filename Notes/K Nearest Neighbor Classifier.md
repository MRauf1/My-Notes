---
tags: statistics, statistical_learning
---

# Definition

> [!info] Definition 1 (K Nearest Neighbor Classifier)[^1]
> ...
> $$
> \begin{align}
> P(Y = j | X = x) = \frac{1}{K} \sum_{i \in N_0} I(y_i = j)
> \end{align}
> $$
> Where $I(y_i = j)$ is the [[Indicator Function]].

K Nearest Neighbor, for a given new observation, calculates the [[Distance]] with all of the existing observations, and assigns a predicted label based on the nearest $K$ observations, where the predicted label is the one that appears the most in the nearest $K$ observations.

The lower the $K$, the more flexible the model is.

#TODO 
Connection between KNN and Bayes Classifier (page 46-47)

[^1]: [Introduction to Statistical Learning with Python](zotero://open-pdf/library/items/9JTAJ2JI?page=47)