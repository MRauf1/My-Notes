---
tags:
  - statistics
  - introduction_to_statistics
  - mathematical_statistics
---

# Definition

> [!info] Definition 1 ([[Probability Function|Probability]] Density Function)[^1][^2]
> For an (absolutely) [[Continuous Random Variable]] $X$, a pdf is a function $f_X$ such that
> $$
> \begin{align}
> F_X(x) = \int_{-\infty}^x f_X(t)\,dt
> \end{align}
> $$
> where $F_X$ is the [[Cumulative Distribution Function]]. Probabilities are computed by [[Riemann Integral|integration]]: $P(a < X \leq b) = \int_a^b f_X(t)\,dt$, the area under $y = f_X(x)$ between $a$ and $b$.

If $f_X$ is continuous at $x$, the [[Fundamental Theorem of Calculus]] gives $\frac{d}{dx} F_X(x) = f_X(x)$. The density value itself is not a probability: $P(X = x) = 0$ for all $x$, while $f_X(x)$ can be any nonnegative number.

# Properties
- [[Probability Density Function Definitional Properties]]: $f_X(x) \geq 0$ and $\int_{-\infty}^\infty f_X(t)\,dt = 1$.
- Not unique: changing $f_X$ at countably many points (more generally, on a set of length zero) leaves every probability unchanged.
- Its positive set is the [[Random Variable Support|support]].
- Transforms under $Y = g(X)$ via the Jacobian ([[Cumulative Distribution Function Transformation Technique]]).

[^1]: [Probability and Statistical Inference](zotero://open-pdf/library/items/RM5FREYV?page=52)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=65)
