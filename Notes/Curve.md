---
tags:
  - mathematics
  - differential_geometry
---

# Definition

> [!info] Definition 1 (Curve)[^1]
> Curve in $\mathbb{R}^n$ is a [[Function]] $\alpha: I \rightarrow \mathbb{R}^n$, where $I$ is an [[Interval Notation|open interval]].
> $$
> \begin{align}
> \alpha(t) = (\alpha_1(t), \dots, \alpha_n(t))
> \end{align}
> $$
> where $\alpha_i$ are its [[Euclidean Coordinate Function]].

One-dimensional object/space that is locally [[Euclidean 1-Space]]/"flat" embedded in some higher dimensional space. Doesn't have to be globally Euclidean.

One way of thinking of a curve is as a trip of a moving [[Point]] in $\mathbb{R}^n$.

The image of the curve is called the trace of the curve.

> [!info] Definition 3 (Curve, Rudin's Version)[^2]
> A continuous mapping $\gamma$ of an interval $[a, b]$ into $\mathbb{R}^k$ is called a curve in $\mathbb{R}^k$, or a curve on $[a, b]$. If $\gamma$ is one-to-one, it is an [[Arc]]. If $\gamma(a) = \gamma(b)$, it is a [[Closed Curve]].

A curve is a mapping, not a point set: each curve has an associated range in $\mathbb{R}^k$, but different curves may have the same range.[^3]

> [!info] Definition 2 (Negative of a Curve)
> Define $- \gamma$ as $[-\gamma](t) = \gamma(a + b - t)$ for $t \in [a, b]$.

Same curve, but traversed in the opposite direction.

# Types
- [[Smooth Curve]]
	- [[Piecewise Smooth Curve]]
- [[Closed Curve]]
- [[Simple Curve]]
- [[Arc]]
- [[Rectifiable Curve]]

# Properties
## [[Complex Number]]
- [[Jordan Curve Theorem]]

[^1]: [Elementary Differential Geometry](zotero://open-pdf/library/items/F6CCEWIU?page=31)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=145&annotation=B4BR6PHD)
[^3]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=145&annotation=5WYC4N8E)