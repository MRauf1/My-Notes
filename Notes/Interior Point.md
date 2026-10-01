---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!info] Definition 1 (Interior [[Point]])[^1]
> In a [[Metric Space]] $(S, d)$ and $E \subseteq S$, [[Point]] $e \in E$ is interior to $E$ if for some $r > 0$, $\{s \in S | d(s, e) < r\} \subseteq E$.

Point is interior in $E$ if the point is sufficiently close to other points in $E$.

# Properties
> [!abstract] Theorem (Interior Points are Limit Points, in $\mathbb{R}^k$)
> Let $E \subseteq \mathbb{R}^k$ (with the standard Euclidean [[Metric]]) and $p \in E$ be an interior point of $E$. Then $p$ is also a [[Limit Point]] of $E$.

My interpretation: if $p$ is interior to $E$, some ball $B(p, \epsilon) \subseteq E$ entirely. Because the Euclidean metric has no isolated points — every ball contains infinitely many other points — points of that ball distinct from $p$ (e.g. a point at distance $\epsilon/2$) also belong to $E$, so every neighborhood of $p$ contains a point of $E$ other than $p$, making $p$ a limit point. This does **not** hold in an arbitrary [[Metric Space]]: e.g. under the discrete metric, every point is interior to the whole space, yet no point is a limit point of anything, since small enough neighborhoods are singletons.

[^1]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=99)