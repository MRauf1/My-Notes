---
tags:
  - statistics
  - mathematical_statistics
---

# Definition

> [!abstract] Theorem 1 (Jensen's [[Inequality]])[^1]
> If $\phi$ is [[Convex Function]] on open interval $I$ and $X$ is a [[Random Variable]] whose support is contained in $I$ and has finite [[Expectation]], then
> $$
> \begin{align}
> \phi(E[X]) \leq E[\phi(X)]
> \end{align}
> $$
> If $\phi$ is [[Strictly Convex Function]], then the [[Inequality]] is strict unless $X$ is a constant [[Random Variable]].

# Properties
- **Concave form**: for a concave $g$ the inequality reverses, $g(E[Y]) \geq E[g(Y)]$.[^2] With $g = \log$,
$$
\begin{align}
\log\left[\int Pr(y)\,h[y]\,dy\right] \geq \int Pr(y) \log\left[h[y]\right] dy
\end{align}
$$
  for any positive function $h$, since $h[y]$ is itself a random variable and $Pr(y)$ was arbitrary. This gives the [[Evidence Lower Bound]] and Gibbs' inequality for the [[Kullback-Leibler Divergence]].

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=97)
[^2]: [Prince, p. 331](zotero://open-pdf/library/items/BWT7FYX5?page=345&annotation=AJX78G6M); [Prince, p. 332](zotero://open-pdf/library/items/BWT7FYX5?page=346&annotation=564EQC9X)