---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Degenerate Distribution[^1]
> A [[Random Variable]] $X$ has a degenerate distribution at a constant $a$ if $P(X = a) = 1$. Equivalently, $E[(X - a)^2] = 0$.

# Properties
- The distribution of a constant: its [[Random Variable Support|support]] is the single point $\{a\}$ and its [[Cumulative Distribution Function|cdf]] is the unit step $F(x) = \mathbb{1}\{x \geq a\}$.
- $E(X) = a$ and $\text{Var}(X) = 0$; conversely $\text{Var}(X) = 0$ implies $X$ is degenerate at $\mu$, so the [[Standard Deviation]] is $0$ exactly for degenerate distributions.
- Its [[Moment Generating Function|mgf]] is $M(t) = e^{at}$ for all $t$.
- It is the equality case of [[Jensen's Inequality]] for strictly convex $\varphi$.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=92)
