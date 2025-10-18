---
tags: computer_science, numerical_analysis
---

# Definition

> [!info] Definition 1 (Relative Condition Number)[^1]
> $$
> \begin{align}
> \text{Relative Condition Number} &= \frac{|(f(\hat{x}) - f(x)) / f(x)|}{|(\hat{x} - x) / x|}\\ 
> &= \frac{|(\hat{y} - y)| / y}{|(\hat{x} - x)| / x} \\
> &= \frac{|\Delta y / y|}{|\Delta x / x|} \\
> &= \frac{|\text{Relative Forward Error}|}{|\text{Relative Backward Error}|}
> \end{align}
> $$

A problem is ill-conditioned/sensitive if the condition number is much larger than 1.

> [!abstract] Theorem 2 (Condition Number of Inverse Problem)
> Given a condition number $\kappa$ for a problem, the condition number of the inverse problem is $\frac{1}{\kappa}$.
> Thus, if the condition number is close to 1, then both problems are well-conditioned. If it's not, then one of them is ill-conditioned.

[^1]: [Scientific Computing](zotero://open-pdf/library/items/UQ4SGXEK?page=25)