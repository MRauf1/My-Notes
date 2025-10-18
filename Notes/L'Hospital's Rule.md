---
tags: mathetatics, calculus
---

# Definition

> [!abstract] Theorem 1 (L'Hopital's Rule)[^1]
> Suppose $f, g$ are [[Differentiable Function]] and $g'(x) \neq 0$ on an open interval $I$ that contains $a$ (except possibly at $a$). Suppose that 1) $\lim_{x \rightarrow a} \frac{f(x)}{g(x)} = \frac{0}{0}$, or 2) $\lim_{x \rightarrow a} \frac{f(x)}{g(x)} = \frac{\pm \infty}{\pm \infty}$. Then
> $$
> \begin{align}
> \lim_{x \rightarrow a} \frac{f(x)}{g(x)} = \lim_{x \rightarrow a} \frac{f'(x)}{g'(x)}
> \end{align}
> $$
> assuming the right [[Limit of Function]] exists.

Intuitively, as the functions get closer to $a$, they start to look more like [[Linear Function]], thus, their ratios would be equal to the [[Ratio]] of their linear [[Slope]], which is the ratio of their [[Derivative]].

This works for [[One-Sided Limit of Function]] and [[Infinite Limit of Function]].

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=337)