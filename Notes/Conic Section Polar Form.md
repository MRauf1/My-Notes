---
tags:
  - mathematics
  - pre_calculus
---

# Definition

> [!abstract] Theorem 1 (Polar Form of a Conic)[^1]
> For $e, d > 0$, each of
> $$
> \begin{align}
> r = \frac{ed}{1 - e\cos\theta}, \quad r = \frac{ed}{1 + e\cos\theta}, \quad r = \frac{ed}{1 - e\sin\theta}, \quad r = \frac{ed}{1 + e\sin\theta}
> \end{align}
> $$
> is the graph in the [[Polar Coordinate System]] of a [[Conic Section]] with a focus at the origin, eccentricity $e$ ([[Conic Section Eccentricity]]) and directrix $x = -d$, $x = d$, $y = -d$, $y = d$ respectively.
> - $0 < e < 1$: [[Ellipse]] with major axis $\frac{2ed}{1 - e^2}$ and minor axis $\frac{2ed}{\sqrt{1 - e^2}}$.
> - $e = 1$: [[Parabola]] with focal diameter $2d$.
> - $e > 1$: [[Hyperbola]] with transverse axis $\frac{2ed}{e^2 - 1}$.

> [!abstract] Theorem 2 (Rotated Polar Form)[^2]
> For $\ell > 0$, $e \geq 0$ and $\varphi$, the graph of
> $$
> \begin{align}
> r = \frac{\ell}{1 - e\cos(\theta - \varphi)}
> \end{align}
> $$
> is a conic with eccentricity $e$ and a focus at the origin. If $e = 0$ it is the [[Circle]] of radius $\ell$. If $e \neq 0$, the directrix contains the point with polar coordinates $(-d, \varphi)$, where $d = \ell / e$.

# Properties
- Derivation: with focus at the origin and directrix $x = -d$, the definition $r = e\,(d + r\cos\theta)$ solves to $r = \frac{ed}{1 - e\cos\theta}$.
- Replacing $\theta$ by $\theta - \varphi$ rotates the conic by $\varphi$ ([[Rotation of Axes]]).

[^1]: [szprecalculus07042013.pdf](zotero://open-pdf/library/items/J3667KH4?page=995)
[^2]: [szprecalculus07042013.pdf](zotero://open-pdf/library/items/J3667KH4?page=997)
