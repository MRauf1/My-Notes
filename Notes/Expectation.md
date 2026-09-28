---
tags:
  - statistics
  - bayesian_statistics
  - mathematical_statistics
---

# Definition

> [!info] Definition 1 (Expectation of [[Discrete Random Variable]])[^1][^2]
> For a [[Discrete Random Variable|discrete RV]] $X$ with pmf $p(x)$, if $\sum_x |x|\,p(x) < \infty$, its expectation is
> $$
> \begin{align}
> E[X] = \mu = \sum_{x} x\, p(x)
> \end{align}
> $$

> [!info] Definition 2 (Expectation of [[Continuous Random Variable]])[^1][^2]
> For a [[Continuous Random Variable]] $X$ with pdf $f(x)$, if $\int_{-\infty}^{\infty} |x| f(x)\,dx < \infty$, its expectation is
> $$
> \begin{align}
> E[X] = \mu = \int_{-\infty}^{\infty} x f(x)\,dx
> \end{align}
> $$

The absolute convergence condition is part of the definition: without it the sum or integral could depend on the order of summation (or be of the form $\infty - \infty$), and the expectation is said not to exist.

The expectation is also known as the mathematical expectation, the expected value, or the [[Mean|mean]] $\mu$ of the random variable. It is the first [[Moment (Statistics)|moment]] of $X$, the arithmetic mean of the values of $X$ weighted by their probabilities.

Expectation measures the center of the distribution.

Expectation is a [[Linear Map|linear operator]].

# Properties

## Main

- $c$ is a [[Constant|constant]] $\implies E[c] = c$

> [!abstract] Theorem 1 (Expectation of a Function of a Random Variable)[^3]
> Let $Y = g(X)$.
> 1. If $X$ is continuous with pdf $f_X$ and $\int_{-\infty}^\infty |g(x)| f_X(x)\,dx < \infty$, then $E(Y)$ exists and $E(Y) = \int_{-\infty}^{\infty} g(x) f_X(x)\,dx$.
> 2. If $X$ is discrete with pmf $p_X$ and support $\mathcal{S}_X$, and $\sum_{x \in \mathcal{S}_X} |g(x)| p_X(x) < \infty$, then $E(Y)$ exists and $E(Y) = \sum_{x \in \mathcal{S}_X} g(x) p_X(x)$.

This avoids finding the distribution of $Y$ ([[Random Variable Transformation]]) first; $E[g(X)]$ is the [[Weighted Mean|weighted mean]] of $g(x)$.

> [!abstract] Theorem 1' (Expectation of a Function of a [[Random Vector]])[^4]
> Let $(X_1, X_2)$ be a random vector and $Y = g(X_1, X_2)$ for $g: \mathbb{R}^2 \to \mathbb{R}$.
> 1. Continuous case: if $\int_{-\infty}^\infty \int_{-\infty}^\infty |g(x_1, x_2)| f_{X_1, X_2}(x_1, x_2)\,dx_1\,dx_2 < \infty$, then $E(Y) = \int_{-\infty}^\infty \int_{-\infty}^\infty g(x_1, x_2) f_{X_1, X_2}(x_1, x_2)\,dx_1\,dx_2$.
> 2. Discrete case: if $\sum_{x_1}\sum_{x_2} |g(x_1, x_2)| p_{X_1, X_2}(x_1, x_2) < \infty$, then $E(Y) = \sum_{x_1}\sum_{x_2} g(x_1, x_2) p_{X_1, X_2}(x_1, x_2)$.

The same holds for an $n$-dimensional random vector with $n$-fold integrals or sums:[^5] if $\int \cdots \int |u(\mathbf{x})| f(\mathbf{x})\,d\mathbf{x} < \infty$ then $E[u(\mathbf{X})] = \int \cdots \int u(\mathbf{x}) f(\mathbf{x})\,d\mathbf{x}$, and linearity extends to $E\left[\sum_{j=1}^m k_j Y_j\right] = \sum_{j=1}^m k_j E[Y_j]$ for $Y_j = u_j(\mathbf{X})$ with existing expectations.

For a function of one component, the double integral collapses to the [[Marginal Distribution|marginal]]: $E[g(X_2)] = \iint g(x_2) f(x_1, x_2)\,dx_1\,dx_2 = \int g(x_2) f_{X_2}(x_2)\,dx_2$, by integrating out $x_1$ first.

## Linearity of Expectation

> [!abstract] Theorem 2 (Linearity of Expectation)[^3]
> If $E[g_1(X)]$ and $E[g_2(X)]$ exist, then for any constants $k_1, k_2$, $E[k_1 g_1(X) + k_2 g_2(X)]$ exists and
> $$
> \begin{align}
> E[k_1 g_1(X) + k_2 g_2(X)] = k_1 E[g_1(X)] + k_2 E[g_2(X)]
> \end{align}
> $$

> [!abstract] Theorem 2' (Linearity for Random Vectors)[^4]
> Let $(X_1, X_2)$ be a [[Random Vector]] and $Y_1 = g_1(X_1, X_2)$, $Y_2 = g_2(X_1, X_2)$ random variables whose expectations exist. Then for all real $k_1, k_2$,
> $$
> \begin{align}
> E(k_1 Y_1 + k_2 Y_2) = k_1 E(Y_1) + k_2 E(Y_2)
> \end{align}
> $$

- $c$ is a [[Constant|constant]] and $X$ is a RV $\implies E[cX] = c E[X]$
- $X$ and $Y$ are [[Random Variable|RVs]] $\implies E[X + Y] = E[X] + E[Y]$
- Linearity does not extend to products: in general $E[g_1(X) g_2(X)] \neq E[g_1(X)] E[g_2(X)]$ (e.g. $E[X^2] \neq (E[X])^2$ unless $\text{Var}(X) = 0$). For [[Independent Random Variable|independent]] $X, Y$, $E[XY] = E[X]E[Y]$ ([[Expectation of Product of Independent Random Variables]]).

## [[Conditional Expectation]]
- [[Law of Total Expectation]]

## [[Inequality]]
- [[Markov's Inequality]]
- [[Jensen's Inequality]]

[^1]: [Probability and Statistical Inference](zotero://open-pdf/library/items/RM5FREYV?page=59)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=77)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=78)
[^4]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=109)
[^5]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=151)
