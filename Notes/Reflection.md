---
tags:
  - mathematics
  - pre_calculus
---

# Definition

...

# [[Coordinate System|Coordinate Plane]] Reflection

For a [[Point|point]] $(x, y)$,

- Reflection about the x-[[Axis|axis]] is $(x, -y)$
- Reflection about the y-axis is $(-x, y)$
- Reflection about the [[Origin|origin]] is $(-x, -y)$[^1]

Reflection about the origin is a distinct transformation from reflection about the lines $y=x$ or $y=-x$: e.g. $(2,3) \mapsto (-2,-3)$ under origin reflection but $(2,3) \mapsto (3,2)$ under reflection about $y=x$. It coincides with neither line reflection in general; it is equivalent to a $180°$ [[Rotation|rotation]] about the origin, or to composing the $x$-axis and $y$-axis reflections.

# [[Function|Function]] Reflection

> [!info] Definition 1 (Function Reflection)
> For a function $f$
> - $-f(x)$ reflects the [[Graph|graph]] of $f(x)$ across the $x$-[[Axis|axis]]
> - $f(-x)$ reflects the graph of $f(x)$ across the $y$-axis[^2]

# Matrix Form
> [!info] Definition 2 (Reflection as a [[Scale Transformation]])[^3]
> Reflecting a vector across a coordinate axis is a [[Scale Transformation|scale]] with one negative scale factor:
> $$
> \begin{align}
> \text{reflect-x} = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}, \qquad \text{reflect-y} = \begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix}
> \end{align}
> $$

A general linear map is a reflection (rather than a rotation) exactly when it is an [[Orthogonal Matrix]] with $\det = -1$.

[^1]: [szprecalculus07042013.pdf](zotero://open-pdf/library/items/J3667KH4?page=22)
[^2]: [szprecalculus07042013.pdf](zotero://open-pdf/library/items/J3667KH4?page=138)
[^3]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=129&annotation=D9ZWGBPI)