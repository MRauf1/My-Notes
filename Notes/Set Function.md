---
tags:
  - statistics
  - introduction_to_statistics
  - mathematical_statistics
---

# Definition
> [!info] Set Function[^1][^2]
> A [[Function]] that maps [[Set|sets]] to [[Real Number|real numbers]]. For example, [[Probability|probability]] $P(A)$ of [[Event|event]] $A$ is a set function.

Set functions in probability are usually built from a point function $f$ by
$$
\begin{align}
Q(A) = \int_A f(x)\,dx \quad \text{or} \quad Q(A) = \sum_{x \in A} f(x)
\end{align}
$$
where $\int_A$ is the ordinary [[Riemann Integral|(Riemann) integral]] over a one-dimensional set $A$ and $\sum_A$ is the sum over all $x \in A$.

Whether the endpoints of an interval are included matters only for sums, not for integrals. A single point has length zero, so for an (integrable) $f$,
$$
\begin{align}
\int_{(1,4)} f = \int_{[1,4)} f = \int_{(1,4]} f = \int_{[1,4]} f = \int_1^4 f(x)\,dx
\end{align}
$$
and all four are equally valid. For a sum, $\sum_{x \in [1,4]} f(x)$ includes the terms $f(1)$ and $f(4)$ while $\sum_{x \in (1,4)} f(x)$ does not. This is why endpoints are irrelevant for a [[Continuous Random Variable]] ([[Continuous Random Variable Probability Inequality Theorem]]) but crucial for a [[Discrete Random Variable]].

# Properties
- A set function defined by an integral or sum over a nonnegative $f$ is additive over [[Disjoint Set Union|disjoint unions]]: $Q(A \cup B) = Q(A) + Q(B)$ when $A \cap B = \emptyset$.
- A [[Measure (Measure Theory)|measure]] is a countably additive nonnegative set function on a [[Sigma-Field]].

[^1]: [Probability and Statistical Inference](zotero://open-pdf/library/items/RM5FREYV?page=15)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=23)
