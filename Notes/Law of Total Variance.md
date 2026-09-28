---
tags:
  - statistics
  - categorical_variable_prediction
  - mathematical_statistics
---

# Definition

> [!info] Definition 1 (Law of Total [[Variance]])
> The variance of a  [[Random Variable]] $X$ in relation to its [[Conditional Expectation]] and [[Conditional Variance]] with respect to a RV $Y$ is
> $$
> \begin{align}
> Var[X] = E[Var[X | Y]] + Var[E[X | Y]]
> \end{align}
> $$

> [!abstract] Corollary 1 (Conditioning Reduces Variance, Hogg Theorem 2.3.1(b))[^1]
> Let $(X_1, X_2)$ be a [[Random Vector]] such that $\text{Var}(X_2)$ is finite. Then
> $$
> \begin{align}
> \text{Var}[E(X_2 | X_1)] \leq \text{Var}(X_2)
> \end{align}
> $$

It follows from Definition 1 because $E[\text{Var}(X_2 | X_1)] \geq 0$, with equality if and only if $\text{Var}(X_2 | X_1) = 0$ with probability one, i.e. $X_2$ is a function of $X_1$.

The total variance splits into the average within-slice spread $E[\text{Var}(X_2 | X_1)]$ and the spread of the slice means $\text{Var}[E(X_2 | X_1)]$; conditioning discards the first part.

**Interpretation.**[^2] $X_2$ and $E(X_2 | X_1)$ have the same mean $\mu_2$ ([[Law of Total Expectation]]), so both are unbiased guesses at an unknown $\mu_2$, but $E(X_2 | X_1)$ has smaller variance and is the more reliable guess: after observing $(x_1, x_2)$, prefer $E(X_2 | x_1)$ to $x_2$. Applied with $X_1$ a sufficient statistic, this is the Rao-Blackwell theorem: conditioning an unbiased estimator on a sufficient statistic never increases its variance.

# Properties
- Analogous to the decomposition of total sum of squares into within-group and between-group parts in ANOVA.
- In prediction, $\text{Var}[E(X_2 | X_1)]$ is the variance of $X_2$ explained by $X_1$, and $E[\text{Var}(X_2 | X_1)]$ is the irreducible error of the best predictor $E(X_2 | X_1)$ (cf. [[Bias-Variance Tradeoff]]).

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=130)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=131)
