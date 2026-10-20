---
tags:
  - mathematics
  - real_analysis
---

# Definition
> [!info] Definition 1 (Removable Discontinuity)[^1]
> Let $f$ be a real function defined in a neighborhood of $x_0$ and discontinuous at $x_0$ ([[Discontinuity]]). If both [[One-Sided Limit of Function|one-sided limits]] exist, are finite, and are equal,
> $$
> \begin{align}
> L = f(x_0^-) = f(x_0^+), \qquad L \neq f(x_0)
> \end{align}
> $$
> then $x_0$ is a removable discontinuity.

It is "removable" because redefining $f$ at the single point $x_0$,
$$
\begin{align}
g(x) = \begin{cases} f(x) & x \neq x_0 \\ L & x = x_0 \end{cases}
\end{align}
$$
yields a function $g$ continuous at $x_0$.

The term is sometimes broadened to points where $f$ is undefined but $\lim_{x \to x_0} f(x)$ exists ([[Removable Singularity]]). This is an abuse of terminology, since continuity and discontinuity are only defined at points of the [[Domain]].

# Properties
- Special case of [[Simple Discontinuity]] (first kind); contrast with [[Jump Discontinuity]], where $f(x_0^-) \neq f(x_0^+)$.
- Equivalently, $\lim_{x \to x_0} f(x)$ exists ([[Limit of Function and One-Sided Limit of Function Theorem]]) but differs from $f(x_0)$.

[^1]: [Classification of discontinuities — Wikipedia](https://en.wikipedia.org/wiki/Classification_of_discontinuities)
