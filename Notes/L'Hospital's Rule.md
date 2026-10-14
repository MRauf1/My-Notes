---
tags:
  - mathematics
  - calculus
---

# Definition

> [!abstract] Theorem 1 (L'Hopital's Rule)[^1]
> Suppose $f, g$ are [[Differentiable Function]] and $g'(x) \neq 0$ on an open interval $I$ that contains $a$ (except possibly at $a$). Suppose that 1) $\lim_{x \rightarrow a} f(x) = \lim_{x \rightarrow a} g(x) = 0$, or 2) $\lim_{x \rightarrow a} |g(x)| = + \infty$. Then
> $$
> \begin{align}
> \lim_{x \rightarrow a} \frac{f(x)}{g(x)} = \lim_{x \rightarrow a} \frac{f'(x)}{g'(x)}
> \end{align}
> $$
> assuming the right [[Limit of Function]] exists.

Intuitively, as the functions get closer to $a$, they start to look more like [[Linear Function]], thus, their ratios would be equal to the [[Ratio]] of their linear [[Slope]], which is the ratio of their [[Derivative]].

This works for [[One-Sided Limit of Function]] and [[Infinite Limit of Function]].

> [!abstract] Theorem 2 (L'Hospital's Rule, Extended Version)[^2]
> Suppose $f$ and $g$ are real and differentiable in $(a, b)$, and $g'(x) \neq 0$ for all $x \in (a, b)$, where $-\infty \leq a < b \leq +\infty$. Suppose
> $$
> \begin{align}
> \frac{f'(x)}{g'(x)} \rightarrow A \quad \text{as } x \rightarrow a.
> \end{align}
> $$
> If $f(x) \rightarrow 0$ and $g(x) \rightarrow 0$ as $x \rightarrow a$, or if $g(x) \rightarrow +\infty$ as $x \rightarrow a$, then
> $$
> \begin{align}
> \frac{f(x)}{g(x)} \rightarrow A \quad \text{as } x \rightarrow a.
> \end{align}
> $$
> The analogous statement holds if $x \rightarrow b$, or if $g(x) \rightarrow -\infty$.

Limits here are in the sense of [[Limit of Function in Extended Real Number System]], so $a$, $b$ and $A$ may be infinite. In the $\infty$ case, only $g$ needs to diverge; nothing is assumed about $f$.

You can keep reapplying this rule as long as the answer remains indeterminate.

# Properties
- Proved using the generalized [[Mean Value Theorem]].
- Fails for complex-valued functions ([[Derivative of Vector-Valued Function]]).

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=337)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=118&annotation=5MVUFXJC)
