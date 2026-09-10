---
tags:
  - mathematics
  - real_analysis
  - linear_algebra
---

# Definition

> [!info] Definition 1 ([[Triangle]] [[Inequality]])[^1]
> $\forall a, b \in \mathbb{R}$, 
> $$
> |a + b| \leq |a| + |b|
> $$

> [!info] Definition 2 (Reverse Triangle Inequality)[^1]
> $\forall a, b \in \mathbb{R}$,
> $$
> \big| |a| - |b| \big| \leq |a - b|
> $$

> [!abstract] Corollary 3 ([[Distance]] Triangle Inequality)
> $\forall a, b, c \in \mathbb{R}, dist(a, c) \leq dist(a, b) + dist(b, c)$

The [[Length]] of a side of a [[Triangle]] is less than or equal to the [[Addition]] of the lengths of the other two sides.

> [!info] Definition 4 (Generalized, [[Normed Space]])[^2]
> For any $v, w \in V$ in a [[Normed Space]] $V$,
> $$
> \lVert v + w \rVert \leq \lVert v \rVert + \lVert w \rVert
> $$
> and for any $u, v, w \in V$,
> $$
> \lVert u - v \rVert \leq \lVert u - w \rVert + \lVert w - v \rVert
> $$

> [!abstract] Proposition 5 (Generalized Reverse Triangle Inequality)[^3]
> If $V$ is a [[Normed Space]], then for any $v, w \in V$,
> $$
> \big| \lVert v \rVert - \lVert w \rVert \big| \leq \lVert v - w \rVert
> $$

# Equality Cases
- Equality in $\lVert v + w \rVert = \lVert v \rVert + \lVert w \rVert$ **and** equality in $\big| \lVert v \rVert - \lVert w \rVert \big| = \lVert v - w \rVert$ hold under the exact same condition: $v$ and $w$ point in the same direction, i.e. $v = cw$ or $w = cv$ for some real $c \geq 0$ (equivalently, $v, w \geq 0$ multiples of one another; either vector may be $0$).
- This is a *stronger* condition than merely being [[Collinear]] (a multiple of each other by any scalar, positive or negative), which is the equality condition for [[Cauchy-Schwarz Inequality]]. If $v, w \neq 0$ are collinear with a **negative** scalar (they point in opposite directions), then both inequalities above are strict, even though the Cauchy-Schwarz inequality $|\langle v, w \rangle| \leq \lVert v \rVert \lVert w \rVert$ is still an equality, since it only depends on $|\langle v, w \rangle|$, which is insensitive to the sign of the scalar.
- In every other case (linearly independent $v, w$, or collinear with a negative scalar), all of the inequalities above are strict.

# Properties
- [[Normed Space]]
- [[Cauchy-Schwarz Inequality]]
- [[Triangle Inequality (Geometry)]]

[^1]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=29)
[^2]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=252)
[^3]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=289)