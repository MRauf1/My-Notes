---
tags:
  - mathematics
  - calculus
---

# Definition

> [!info] Definition 1 (Taylor Polynomial)[^1]
> The $n$th-degree Taylor polynomial of $f$ at $a$ is the $n$th partial sum of its [[Taylor Series]]:
> $$
> \begin{align}
> T_n(x) = \sum_{i=0}^{n} \frac{f^{(i)}(a)}{i!}(x - a)^i
> \end{align}
> $$
> The remainder is $R_n(x) = f(x) - T_n(x)$.

# Properties
- $T_n$ is the unique polynomial of degree $\leq n$ that agrees with $f$ and its first $n$ derivatives at $a$ ([[Nth Derivative]]). $T_1$ is the [[Linear Approximation]].
- $f$ equals its Taylor series at $x$ exactly when $R_n(x) \to 0$ ([[Taylor Series Equal to Function Theorem]]). $|R_n|$ is bounded by [[Taylor's Inequality]], and the Lagrange form of $R_n$ is in [[Taylor's Theorem]].

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=793)
