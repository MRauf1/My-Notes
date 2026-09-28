---
tags:
  - statistics
  - bayesian_statistics
  - mathematical_statistics
---

# Definition

> [!info] Definition 1 ([[Conditional Probability|Conditional]] [[Variance]])[^1]
> For [[Random Variable]] $X, Y$, the conditional variance of $X$ given $Y = y$ is
> $$
> \begin{align}
> Var[X | Y = y] = E[(X - \mu_{X | y})^2 | Y = y]
> \end{align}
> $$
> where $\mu_{X | y} = E[X | Y = y]$ is the [[Conditional Expectation|conditional mean]].

It is the variance of the [[Conditional Distribution]] of $X$ given $Y = y$. In Hogg et al.'s notation, $\text{Var}(X_2 | x_1) = E\{[X_2 - E(X_2 | x_1)]^2 | x_1\}$.

# Properties
- Computational formula: $\text{Var}(X_2 | x_1) = E(X_2^2 | x_1) - [E(X_2 | x_1)]^2$, the [[Variance Basic Properties|usual shortcut]] applied to the conditional distribution.
- Like the conditional mean, $\text{Var}(X_2 | x_1)$ is a function of $x_1$, so $\text{Var}(X_2 | X_1)$ is a random variable.
- [[Law of Total Variance]]: $\text{Var}(X_2) = E[\text{Var}(X_2 | X_1)] + \text{Var}[E(X_2 | X_1)]$.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=127)
