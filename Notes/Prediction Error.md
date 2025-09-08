---
tags: statistics, statistical_learning
---

# Definition

> [!info] Definition 1 ([[Prediction]] Error)[^1]
> For a fixed $X, \hat{f}$,
> $$
> \begin{align}
> E[Y - \hat{Y}]^2 &= E[f(X) + \epsilon - \hat{f}(X)]^2 \\
> &= (f(X) - \hat{f}(X))^2 + Var[\epsilon]
> \end{align}
> $$
> where $(f(X) - \hat{f}(X))^2$ is the reducible error and $Var[\epsilon]$ is the irreducible error. 

# Types
- [[Reducible Error]]
- [[Irreducible Error]]

[^1]: [Introduction to Statistical Learning with Python](zotero://open-pdf/library/items/9JTAJ2JI?page=28)