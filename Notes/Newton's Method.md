---
tags: mathetatics, calculus
---

# Definition

> [!info] Definition 1 ([[Isaac Newton]] Method)[^1]
> To solve an [[Equation]] $f(x) = 0$ (find $x$-intercept), the $x$-intercept can be approximated recursively by
> $$
> \begin{align}
> x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
> \end{align}
> $$
> given that $f'(x_n) \neq 0$

Newton's method approximates the $x$-intercept by finding the $x$-intercepts of the [[Tangent Line]] at the current point and successively improving the prediction.

It is not guaranteed to converge for all [[Function]].

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=378)