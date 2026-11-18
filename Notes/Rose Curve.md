---
tags:
  - mathematics
  - pre_calculus
---

# Definition

> [!info] Definition 1 (Rose Curve)[^1]
> A (polar) rose is the graph in the [[Polar Coordinate System]] of
> $$
> \begin{align}
> r = a\cos(n\theta) \quad \text{or} \quad r = a\sin(n\theta), \qquad a \neq 0,\ n \in \mathbb{N},\ n \geq 2
> \end{align}
> $$

# Properties
- Petal count: $n$ petals if $n$ is odd, $2n$ petals if $n$ is even. Each petal has length $|a|$.
- For odd $n$ the whole curve is traced once on $0 \leq \theta \leq \pi$; for even $n$ it takes $0 \leq \theta \leq 2\pi$.
- $n = 1$ gives a [[Circle]] through the origin rather than a rose.

# Questions
> [!question]- Why does $r = a\cos(n\theta)$ have $n$ petals for odd $n$ but $2n$ for even $n$?
> $r(\theta + \pi) = a\cos(n\theta + n\pi) = (-1)^n r(\theta)$. In polar coordinates $(-r, \theta + \pi)$ and $(r, \theta)$ are the same point. For odd $n$, the point at $\theta + \pi$ is $(-r(\theta), \theta + \pi) = (r(\theta), \theta)$, so the second half-turn retraces the first and only the $n$ petals traced on $[0, \pi]$ appear. For even $n$, $(r(\theta), \theta + \pi)$ is the reflection of $(r(\theta), \theta)$ through the origin, which lands on new petals, giving $2n$.

[^1]: [szprecalculus07042013.pdf](zotero://open-pdf/library/items/J3667KH4?page=962)
