---
tags: statistics, statistical_learning
---

# Definition

A [[Greedy Algorithm]]. Can always be used.

- Start with the null model (only intercept)
- Fit $p$ models ($p$ is the number of possible parameters)
- Select the parameter with the lowest [[Residual Sum of Squares]] and fit the new model with all the previous parameters and this one together
- Repeat the process until some stopping criteria

[^1]: [Introduction to Statistical Learning with Python](zotero://open-pdf/library/items/9JTAJ2JI?page=96)