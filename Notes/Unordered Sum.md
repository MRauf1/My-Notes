---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!info] Unordered Sum[^1]
> Let $X$ be an arbitrary [[Set]] and $f: X \to [0, \infty]$. The sum of $f$ over $X$ is
> $$
> \begin{align}
> \sum_{x \in X} f(x) = \sup\left\{ \sum_{x \in F} f(x) : F \subseteq X,\ F \text{ finite} \right\}.
> \end{align}
> $$

No ordering of $X$ is involved, so the value is independent of any enumeration; for nonnegative terms this agrees with the usual sum of a [[Series]] for every rearrangement.

# Properties
> [!abstract] Proposition (Reduction to Ordinary Series)[^1]
> Let $A = \{x : f(x) > 0\}$. If $A$ is uncountable, then $\sum_{x \in X} f(x) = \infty$. If $A$ is countably infinite, then
> $$
> \begin{align}
> \sum_{x \in X} f(x) = \sum_{n=1}^{\infty} f(g(n))
> \end{align}
> $$
> where $g: \mathbb{N} \to A$ is any [[Bijective Function|bijection]] and the right side is an ordinary infinite series.

- A finite unordered sum forces $f$ to be nonzero on at most a [[Countable Set|countable]] set.
- It is the integral of $f$ with respect to counting measure on $X$ (see [[Lebesgue Integral (Measure Theory)]]).
- Takes values in the [[Extended Real Number Set]].

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=24&annotation=29VBHMLB)
