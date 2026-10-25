---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!abstract] Theorem 1.16 (Borel Measures on $\mathbb{R}$ from Increasing Functions)[^1]
> If $F : \mathbb{R} \to \mathbb{R}$ is any [[Increasing Function|increasing]], right continuous function, there is a unique [[Borel Measure]] $\mu_F$ on $\mathbb{R}$ such that
> $$
> \begin{align}
> \mu_F((a, b]) = F(b) - F(a) \qquad \text{for all } a, b.
> \end{align}
> $$
> If $G$ is another such function, $\mu_F = \mu_G$ iff $F - G$ is constant. Conversely, if $\mu$ is a Borel measure on $\mathbb{R}$ that is finite on all bounded Borel sets and
> $$
> \begin{align}
> F(x) = \begin{cases} \mu((0, x]) & x > 0 \\ 0 & x = 0 \\ -\mu((-x, 0]) & x < 0 \end{cases}
> \end{align}
> $$
> then $F$ is increasing and right continuous, and $\mu = \mu_F$.

> [!info] Lebesgue–Stieltjes Measure[^2]
> The complete measure obtained from $F$ via the [[Carathéodory Extension Theorem]] (whose domain strictly contains $\mathcal{B}_\mathbb{R}$) is the [[Measure Completion Theorem|completion]] of $\mu_F$. It is also denoted $\mu_F$ and called the Lebesgue–Stieltjes measure associated to $F$.

**Motivation.**[^3] If $\mu$ is a [[Finite Measure|finite]] Borel measure and $F(x) = \mu((-\infty, x])$, then $F$ is increasing (monotonicity) and right continuous (continuity from above, since $(-\infty, x] = \bigcap_n (-\infty, x_n]$ for $x_n \downarrow x$), and $\mu((a, b]) = F(b) - F(a)$. The theorem runs this backwards: an increasing right-continuous $F$ determines a measure. $F(x) = x$ gives length, i.e. [[Lebesgue Measure]].

**Construction.**[^4] The building blocks are **h-intervals** (half-open): sets $(a, b]$, $(a, \infty)$, or $\emptyset$, with $-\infty \leq a < b < \infty$. They form an [[Elementary Family]] (intersections are h-intervals; complements are an h-interval or a disjoint union of two), so their finite disjoint unions form an [[Algebra of Sets|algebra]] $\mathcal{A}$ generating $\mathcal{B}_\mathbb{R}$. By Proposition 1.15, for disjoint h-intervals[^5]
$$
\begin{align}
\mu_0\left(\bigcup_{j=1}^n (a_j, b_j]\right) = \sum_{j=1}^n [F(b_j) - F(a_j)], \qquad \mu_0(\emptyset) = 0
\end{align}
$$
is a [[Premeasure]] on $\mathcal{A}$; Carathéodory extension then produces $\mu_F$.

# Properties
- The theory works equally with intervals $[a, b)$ and left-continuous $F$.[^2]
- For a finite Borel measure, $\mu = \mu_F$ with $F(x) = \mu((-\infty, x])$ its [[Cumulative Distribution Function]]; this differs from the $F$ of Theorem 1.16 by the constant $\mu((-\infty, 0])$.[^2]
- Integrals against $\mu_F$ generalize the [[Riemann-Stieltjes Integral]] $\int g\,dF$.
- Regularity: outer regular by open sets, inner regular by compact sets, and determined up to null sets by $G_\delta$/$F_\sigma$ sets ([[Lebesgue-Stieltjes Measure Regularity]]).
- A jump of $F$ at $x_0$ of size $c$ gives an atom $\mu_F(\{x_0\}) = c$; a step $F$ yields a [[Dirac Measure]].

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=48&annotation=Y2SPDTQP)
[^2]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=48&annotation=XUVVCF95)
[^3]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=46&annotation=569UFGHI)
[^4]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=46&annotation=HSZIAKC2)
[^5]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=46&annotation=9YD2N4UP)
