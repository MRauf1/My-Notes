---
tags:
  - statistics
  - categorical_variable_prediction
  - mathematical_statistics
---

# Definition

> [!info] Definition 1 (Law of Total [[Expectation]])
> The expectation of the [[Conditional Expectation]] with [[Random Variable]] $X, Y$ is
> $$
> \begin{align}
> E[X] = E[E[X | Y]]
> \end{align}
> $$

> [!abstract] Theorem 1 (Law of Total Expectation, Hogg Theorem 2.3.1(a))[^1]
> Let $(X_1, X_2)$ be a [[Random Vector]] such that $\text{Var}(X_2)$ is finite. Then
> $$
> \begin{align}
> E[E(X_2 | X_1)] = E(X_2)
> \end{align}
> $$

Proof (continuous case): writing the joint pdf as $f_{1,2}(x_1, x_2) = f_1(x_1) f_{2|1}(x_2 | x_1)$ ([[Conditional Distribution]]),
$$
\begin{align}
E(X_2) = \int\!\!\int x_2 f_{1,2}(x_1, x_2)\,dx_2\,dx_1 = \int \left[\int x_2 f_{2|1}(x_2 | x_1)\,dx_2\right] f_1(x_1)\,dx_1 = \int E(X_2 | x_1)\, f_1(x_1)\,dx_1 = E[E(X_2 | X_1)]
\end{align}
$$

**Interpretation.** $E[X_2 | X_1]$ is a random variable in which only $X_1$ remains random; $X_2$ has already been averaged out. The outer expectation therefore integrates only over $x_1$, against the [[Marginal Distribution|marginal]] of $X_1$. The law says averaging in two stages (first within each slice $X_1 = x_1$, then across slices weighted by how likely each slice is) gives the overall average. It is the expectation version of the [[Law of Total Probability]], which is the special case $X_2 = \mathbb{1}_A$.

# Properties
- Finite variance is Hogg's hypothesis (needed for part (b), the [[Law of Total Variance]]); part (a) holds whenever $E|X_2| < \infty$.
- Also called the tower property or law of iterated expectations.
- $E[X_2 | X_1]$ and $X_2$ share the mean $\mu_2$, so either can serve as a guess at $\mu_2$; the [[Law of Total Variance]] shows the conditional mean is the more reliable one.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=130)
