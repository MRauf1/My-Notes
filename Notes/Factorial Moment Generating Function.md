---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Factorial Moment Generating Function[^1]
> Let $X$ be a [[Random Variable]] such that $K(t) = E\left(t^X\right)$ exists for all real $t$ in an open interval containing $t = 1$. Then $K$ is the factorial moment generating function of $X$, and
> $$
> \begin{align}
> K^{(m)}(1) = E[X(X-1)\cdots(X-m+1)]
> \end{align}
> $$
> the $m$th factorial [[Moment (Statistics)|moment]] of $X$.

# Properties
- $K(t) = M(\log t)$, where $M$ is the [[Moment Generating Function]].
- $E(X) = K'(1)$ and $\text{Var}(X) = K''(1) + K'(1) - [K'(1)]^2$.
- For $X$ taking values in $\{0, 1, 2, \dots\}$, $K(t) = \sum_k p_X(k) t^k$ is the probability generating function, and $p_X(k) = K^{(k)}(0)/k!$.
- Natural for count distributions such as the [[Poisson Distribution]] ($K(t) = e^{\lambda(t-1)}$) and [[Binomial Distribution]] ($K(t) = (1 - p + pt)^n$), whose factorial moments have simple closed forms.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=92)
