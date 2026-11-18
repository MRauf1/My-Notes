---
tags:
  - mathematics
  - pre_calculus
---

# Definition

> [!abstract] Theorem 1 (Rotation of Axes)[^1]
> If the positive $x$- and $y$-axes are rotated counter-clockwise through an angle $\theta$ to give axes $x'$ and $y'$, the coordinates $P(x, y)$ and $P(x', y')$ of a point are related by
> $$
> \begin{align}
> x &= x'\cos\theta - y'\sin\theta, & x' &= x\cos\theta + y\sin\theta \\
> y &= x'\sin\theta + y'\cos\theta, & y' &= -x\sin\theta + y\cos\theta
> \end{align}
> $$

> [!abstract] Theorem 2 (Eliminating the $xy$-Term)[^2]
> The equation $Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0$ with $B \neq 0$ becomes an equation in $x', y'$ with no $x'y'$-term after rotating the axes counter-clockwise through an angle $\theta$ with
> $$
> \begin{align}
> \cot(2\theta) = \frac{A - C}{B}
> \end{align}
> $$

> [!abstract] Theorem 3 (Discriminant of a Conic)[^3]
> If $Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0$ describes a non-degenerate [[Conic Section]], its graph is
> - a [[Hyperbola]] if $B^2 - 4AC > 0$,
> - a [[Parabola]] if $B^2 - 4AC = 0$,
> - an [[Ellipse]] or [[Circle]] if $B^2 - 4AC < 0$.

# Properties
- In matrix form, $(x, y)^\top = R_\theta (x', y')^\top$ with the [[Rotation Matrix]] $R_\theta$, and $(x', y')^\top = R_\theta^{\top}(x, y)^\top$ since $R_\theta^{-1} = R_{-\theta} = R_\theta^\top$.
- Derived from the [[Sum and Difference Identities]]: if $P$ has polar coordinates $(r, \varphi)$ relative to the new axes, then relative to the old axes its angle is $\varphi + \theta$, so $x = r\cos(\varphi + \theta) = x'\cos\theta - y'\sin\theta$ and $y = r\sin(\varphi + \theta) = x'\sin\theta + y'\cos\theta$.

# Questions
> [!question]- Why does the sign of $B^2 - 4AC$ determine the type of conic even when $B \neq 0$?
> The quadratic part is $\mathbf{x}^\top Q \mathbf{x}$ with $Q = \begin{bmatrix} A & B/2 \\ B/2 & C \end{bmatrix}$, and $B^2 - 4AC = -4\det Q$. A rotation replaces $Q$ by $R_\theta^\top Q R_\theta$, which has the same determinant, so the discriminant is invariant. After the rotation of Theorem 2, $B' = 0$ and the discriminant is $-4A'C'$: negative when $A', C'$ have the same sign (ellipse), positive when opposite (hyperbola), zero when one vanishes (parabola).

[^1]: [szprecalculus07042013.pdf](zotero://open-pdf/library/items/J3667KH4?page=986)
[^2]: [szprecalculus07042013.pdf](zotero://open-pdf/library/items/J3667KH4?page=989)
[^3]: [szprecalculus07042013.pdf](zotero://open-pdf/library/items/J3667KH4?page=991)
