---
tags:
  - statistics
  - mathematical_statistics
---

# Definition

> [!info] Definition 1 ([[Random Variable]] Equal in [[Probability Distribution]])[^1]
> Two [[Random Variable]] $X, Y$ are equal in distribution, written $X \overset{D}{=} Y$, if and only if $F_X(x) = F_Y(x)$ for all $x \in \mathbb{R}$.

Equality in distribution does not imply $X = Y$: the two may be very different functions, even on different [[Sample Space|sample spaces]]. For example, if $X$ is symmetric about $0$ then $X \overset{D}{=} -X$, yet $X \neq -X$ unless $X = 0$.

# Properties
- Equivalent to equality of [[Moment Generating Function|mgfs]] near $0$ when they exist ([[Moment Generating Function Equal Distribution Theorem]]), and always equivalent to equality of [[Characteristic Function (Probability)|characteristic functions]].

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=56)
