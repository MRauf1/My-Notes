---
tags:
  - statistics
  - bayesian_statistics
  - mathematical_statistics
---

# Definition

> [!info] Definition 1 ([[Independent Events|Independent]] [[Random Variable]])[^1][^2]
> Let $X_1, X_2$ have joint pdf $f(x_1, x_2)$ [joint pmf $p(x_1, x_2)$] and marginal pdfs [pmfs] $f_1(x_1), f_2(x_2)$ [$p_1(x_1), p_2(x_2)$]. $X_1$ and $X_2$ are independent if and only if
> $$
> \begin{align}
> f(x_1, x_2) \equiv f_1(x_1) f_2(x_2) \qquad [p(x_1, x_2) \equiv p_1(x_1) p_2(x_2)]
> \end{align}
> $$
> Random variables that are not independent are dependent.

Two random variables are independent iff their [[Joint Probability Distribution]] factors into a product of their [[Marginal Distribution|marginal distributions]].

**Motivation.**[^2] By the [[Conditional Distribution|conditional pdf]], always $f(x_1, x_2) = f_{2|1}(x_2 | x_1) f_1(x_1)$. If $f_{2|1}(x_2 | x_1)$ does not depend on $x_1$, then
$$
\begin{align}
f_2(x_2) = \int_{-\infty}^\infty f_{2|1}(x_2 | x_1) f_1(x_1)\,dx_1 = f_{2|1}(x_2 | x_1) \int_{-\infty}^\infty f_1(x_1)\,dx_1 = f_{2|1}(x_2 | x_1)
\end{align}
$$
so $f(x_1, x_2) = f_1(x_1) f_2(x_2)$: learning $X_1$ tells nothing about the distribution of $X_2$.

**Meaning of the identity $\equiv$.**[^2] The product $f_1(x_1) f_2(x_2)$ is positive exactly on the product space $\mathcal{S}_1 \times \mathcal{S}_2 = \{(x_1, x_2) : x_1 \in \mathcal{S}_1, x_2 \in \mathcal{S}_2\}$. The identity need not hold at every point: the equality may fail on a set $A$ as long as $A$ is negligible. Here $A = \{(x_1, x_2) \in \mathbb{R}^2 : f(x_1, x_2) \neq f_1(x_1) f_2(x_2)\}$ is a subset of the whole plane $\mathbb{R}^2$, not only of $\mathcal{S}$ or $\mathcal{S}_1 \times \mathcal{S}_2$. Hogg et al. require $P(A) = 0$. Read literally with $P$ the joint distribution, that is too weak: it would ignore a region where $f = 0$ but $f_1 f_2 > 0$. For example, with $f(x_1, x_2) = 8 x_1 x_2$ on $0 < x_1 < x_2 < 1$, the failure set includes the triangle $x_2 < x_1$, which has joint probability $0$, yet $X_1, X_2$ are dependent. The correct condition is that $A$ has zero area (Lebesgue measure zero, e.g. finitely many points or curves). That implies probability $0$ under both the joint density $f$ and the product density $f_1 f_2$. Changing a density on such a set changes no probability. In the discrete case there is no such slack: the identity must hold at every point.

# Properties
- [[Independent Random Variable Factorization Theorem]]: independence iff $f(x_1, x_2) \equiv g(x_1) h(x_2)$ on a product support.
- [[Independent Random Variable Equivalent Conditions]]: via the [[Joint Cumulative Distribution Function|joint cdf]], rectangle probabilities, and the joint mgf.
- [[Expectation of Product of Independent Random Variables]]: $E[u(X_1) v(X_2)] = E[u(X_1)] E[v(X_2)]$.
- The support of an independent pair is (up to a set of zero area) a product set; if the support is bounded by a curve that is neither horizontal nor vertical, the variables are dependent.

## [[Conditional Probability]]
- If $X_1, X_2$ are independent, then $f_{X_1 | X_2}(x_1 | X_2 = x_2) = \frac{f(x_1, x_2)}{f_{X_2}(x_2)} = f_{X_1}(x_1)$

[^1]: [Bayesian Statistical Methods](zotero://open-pdf/library/items/ELV3M9SP?page=26)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=133)
