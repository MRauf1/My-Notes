---
tags:
  - mathematics
  - abstract_algebra
---

# Definition

> [!info] Definition 1 (Affine Symmetry)
> Given an [[Affine Transformation|affine transformation]] $f: X \rightarrow X$ on an affine space $X$ and a subset $S \subseteq X$, $f$ is an affine symmetry of $S$ if
> $$
> \begin{align}
> f(S) = S
> \end{align}
> $$

An affine symmetry is a symmetry of an object under the wider group of [[Affine Transformation|affine transformations]] (which preserve points, lines, and ratios of distances along a line, but not necessarily distances or angles), rather than only under [[Isometry|isometries]]. Every isometry is an affine transformation, so every isometric symmetry of $S$ is also an affine symmetry of $S$, but the converse need not hold: a shear or non-uniform scaling that maps $S$ onto itself is an affine symmetry without being an isometry.

# Properties

- The affine symmetries of $S$ form a [[Group|group]] under [[Function Composition|composition]], as a subgroup of all affine transformations of $X$.
