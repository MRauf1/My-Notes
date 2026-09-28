---
tags:
  - statistics
  - bayesian_statistics
  - mathematical_statistics
---

# Definition

> [!info] Definition 1 (Marginal Distribution)[^1][^2]
> For a [[Random Vector]] $(X_1, X_2)$ with [[Joint Probability Distribution]], the marginal distribution of $X_1$ is the distribution of $X_1$ alone:
> $$
> \begin{align}
> p_{X_1}(x_1) &= \sum_{x_2} p_{X_1, X_2}(x_1, x_2)\ \text{(Discrete)} \\
> f_{X_1}(x_1) &= \int_{-\infty}^{\infty} f_{X_1, X_2}(x_1, x_2)\,dx_2\ \text{(Continuous)}
> \end{align}
> $$
> for $x_1$ in the support of $X_1$. Its marginal cdf is
> $$
> \begin{align}
> F_{X_1}(x_1) = P[X_1 \leq x_1, -\infty < X_2 < \infty] = \lim_{x_2 \uparrow \infty} F_{X_1, X_2}(x_1, x_2)
> \end{align}
> $$

> [!info] Definition 2 (Marginal of a Group of Variables)[^3]
> For $X_1, \dots, X_n$ with joint pdf $f$, the marginal pdf of $X_1$ is the $(n-1)$-fold integral $f_1(x_1) = \int \cdots \int f(x_1, x_2, \dots, x_n)\,dx_2 \cdots dx_n$. More generally, the marginal pdf of any group of $k < n$ of the variables is their joint pdf, obtained by integrating $f$ over the remaining $n - k$ variables (sums for pmfs). For example, the marginal of $(X_2, X_4, X_5)$ from six variables is $\iiint f\,dx_1\,dx_3\,dx_6$.

To get the marginal of $X_1$, hold $x_1$ fixed and sum or integrate out $x_2$. The name comes from a table of the joint pmf, with rows indexed by $X_1$ values and columns by $X_2$ values: the row sums, written in the margin, give the pmf of $X_1$ and the column sums give the pmf of $X_2$.

Derivation: $\{X_1 \leq x_1\} = \{X_1 \leq x_1\} \cap \{-\infty < X_2 < \infty\}$, and the limit follows from the [[Continuity Theorem of Probability]]. Writing the cdf as $F_{X_1}(x_1) = \int_{-\infty}^{x_1} \left\{\int_{-\infty}^\infty f(w_1, x_2)\,dx_2\right\} dw_1$ (or the analogous sum), uniqueness of the [[Cumulative Distribution Function|cdf]] forces the braced quantity to be the pmf or pdf of $X_1$.

# Properties
- The marginals do not determine the joint distribution in general; many joint distributions share the same marginals. If the components are [[Independent Random Variable|independent]], the joint is the product of the marginals.
- If the joint pdf is symmetric, $f(x, y) = f(y, x)$, then $X$ and $Y$ have the same marginal distribution.
- The marginal mgf is the joint mgf with the other argument set to $0$ ([[Moment Generating Function of Random Vector]]).
- For a function of one component, $E[g(X_2)] = \iint g(x_2) f(x_1, x_2)\,dx_1\,dx_2 = \int g(x_2) f_{X_2}(x_2)\,dx_2$.
- In Bayesian inference, the marginal likelihood $P(Y) = \int P(Y | \theta) P(\theta)\,d\theta$ is a marginal distribution ([[Bayes' Theorem]]).

[^1]: [Bayesian Statistical Methods](zotero://open-pdf/library/items/ELV3M9SP?page=23)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=105)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=152)
