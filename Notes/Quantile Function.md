---
tags:
  - statistics
  - bayesian_statistics
  - mathematical_statistics
---

# Definition

> [!info] Definition 1 (Quantile)[^2]
> Let $0 < p < 1$. The quantile of order $p$ (the $(100p)$th percentile) of the distribution of a [[Random Variable]] $X$ is a value $\xi_p$ such that
> $$
> \begin{align}
> P(X < \xi_p) \leq p \quad \text{and} \quad P(X \leq \xi_p) \geq p
> \end{align}
> $$
> equivalently $F(\xi_p^-) \leq p \leq F(\xi_p)$, where $F$ is the [[Cumulative Distribution Function]].

> [!info] Definition 2 (Quantile [[Function]])[^1]
> For a [[Random Variable]] $X$, its $\tau$ quantile is the quantile function $Q(\tau)$ that is the solution to the following equation
> $$
> \begin{align}
> P(X \leq Q(\tau)) = F(Q(\tau)) = \tau
> \end{align}
> $$
> $Q(\tau)$ is the [[Inverse Function]] of the [[Cumulative Function]] $F(x)$
> $$
> \begin{align}
> Q(\tau) = F^{-1}(\tau)
> \end{align}
> $$

Definition 1 is not a typo: the two inequalities, one strict and one not, are what make it work for every distribution. Definition 2 requires $F(x) = p$ to have a solution, which fails whenever $F$ jumps over the level $p$ (e.g. every discrete distribution for most $p$). Definition 1 instead asks that $\xi_p$ is where $F$ crosses level $p$: at most $p$ of the mass lies strictly below $\xi_p$ and at least $p$ lies at or below it, i.e. $p$ lies between the left limit $F(\xi_p^-)$ and the value $F(\xi_p)$. For continuous $F$ the two inequalities collapse to $F(\xi_p) = p$, recovering Definition 2.

The general-purpose quantile function is the generalized inverse
$$
\begin{align}
Q(p) = F^{-1}(p) = \inf\{x : F(x) \geq p\}
\end{align}
$$
which always satisfies Definition 1 (it is the smallest quantile of order $p$) and is what [[Inverse Transform Sampling]] uses.

# Types
- [[Median]]: $\xi_{1/2}$, the second quartile $q_2$; a measure of center.
- Quartiles $q_1 = \xi_{1/4}$, $q_3 = \xi_{3/4}$, whose difference is the [[Interquartile Range]], a measure of spread.

# Properties
- Quantiles need not be unique, even for continuous random variables with pdfs: if $F$ is flat at level $p$ on an interval (a gap in the support), every point of that interval is a quantile of order $p$.
- If $\xi_p$ lies in the [[Random Variable Support|support]] of an absolutely [[Continuous Random Variable]], then it is the unique solution of $F_X(\xi_p) = p$, i.e. $\xi_p = F_X^{-1}(p)$ with $F_X^{-1}$ the ordinary inverse.
- Quantiles commute with increasing transformations: if $g$ is strictly increasing, $\xi_p(g(X)) = g(\xi_p(X))$.

[^1]: [Bayesian Statistical Methods](zotero://open-pdf/library/items/ELV3M9SP?page=20)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=67)
