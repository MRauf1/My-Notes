---
tags: statistics, statistical_learning
---

# Definition

Combination of [[Forward Selection]] and [[Backward Selection]].

- Start with the null model (only intercept)
- Fit $p$ models ($p$ is the number of possible parameters)
- Select the parameter with the lowest [[Residual Sum of Squares]] and fit the new model with all the previous parameters and this one together
- Whenever a [[P-Value]] of one of the parameters becomes greater than a threshold, remove that parameter
- Repeat the process until some stopping criteria

This results in a model whose parameters are all statistically significant (p-values are low).

[^1]: [Introduction to Statistical Learning with Python](zotero://open-pdf/library/items/9JTAJ2JI?page=96)