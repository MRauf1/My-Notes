---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Theorem 1 (Discrete One-to-One Transformation)[^1]
> Let $(X_1, X_2)$ be a discrete [[Random Vector]] with joint pmf $p_{X_1, X_2}$ and [[Random Variable Support|support]] $\mathcal{S}$. Let $y_1 = u_1(x_1, x_2)$, $y_2 = u_2(x_1, x_2)$ define a one-to-one transformation of $\mathcal{S}$ onto $\mathcal{T}$, with single-valued inverse $x_1 = w_1(y_1, y_2)$, $x_2 = w_2(y_1, y_2)$. Then $(Y_1, Y_2) = (u_1(X_1, X_2), u_2(X_1, X_2))$ has joint pmf
> $$
> \begin{align}
> p_{Y_1, Y_2}(y_1, y_2) = \begin{cases} p_{X_1, X_2}[w_1(y_1, y_2), w_2(y_1, y_2)] & (y_1, y_2) \in \mathcal{T} \\ 0 & \text{elsewhere} \end{cases}
> \end{align}
> $$

> [!abstract] Theorem 2 (Continuous One-to-One Transformation)[^2]
> Let $(X_1, X_2)$ have a jointly continuous distribution with pdf $f_{X_1, X_2}$ and support $\mathcal{S}$, and let $(Y_1, Y_2) = T(X_1, X_2) = (u_1(X_1, X_2), u_2(X_1, X_2))$ with $T$ one-to-one, $\mathcal{T} = T(\mathcal{S})$, and inverse $x_1 = w_1(y_1, y_2)$, $x_2 = w_2(y_1, y_2)$. Assume the first-order partials of $w_1, w_2$ are continuous and the Jacobian
> $$
> \begin{align}
> J = \det \frac{\partial(x_1, x_2)}{\partial(y_1, y_2)} = \begin{vmatrix} \frac{\partial x_1}{\partial y_1} & \frac{\partial x_1}{\partial y_2} \\ \frac{\partial x_2}{\partial y_1} & \frac{\partial x_2}{\partial y_2} \end{vmatrix}
> \end{align}
> $$
> is not identically zero on $\mathcal{T}$. Then
> $$
> \begin{align}
> f_{Y_1, Y_2}(y_1, y_2) = \begin{cases} f_{X_1, X_2}[w_1(y_1, y_2), w_2(y_1, y_2)]\,|J| & (y_1, y_2) \in \mathcal{T} \\ 0 & \text{elsewhere} \end{cases}
> \end{align}
> $$

Proof of Theorem 2: for any region $B \subseteq \mathcal{T}$ with $A = T^{-1}(B)$, one-to-one-ness gives $P[(X_1, X_2) \in A] = P[(Y_1, Y_2) \in B]$, and the [[Change of Variables]] formula for double integrals gives
$$
\begin{align}
P[(X_1, X_2) \in A] = \iint_A f_{X_1, X_2}(x_1, x_2)\,dx_1\,dx_2 = \iint_B f_{X_1, X_2}[w_1(y_1, y_2), w_2(y_1, y_2)]\,|J|\,dy_1\,dy_2
\end{align}
$$
Since $B$ is arbitrary, the last integrand is the joint pdf of $(Y_1, Y_2)$. $J$ plays the role of $dx/dy$ in the univariate [[Cumulative Distribution Function Transformation Technique]] and, like it, is the Jacobian of the inverse map (Hogg et al. call it the Jacobian of the transformation).

**Why the discrete case needs no Jacobian.** A pmf is the probability of an event, $p_{\mathbf{Y}}(\mathbf{y}) = P(\mathbf{Y} = \mathbf{y})$. Because the map is a bijection $\mathcal{S} \to \mathcal{T}$, $\mathbf{Y} = \mathbf{y} \iff \mathbf{X} = w(\mathbf{y})$, so on the [[Sample Space]]
$$
\begin{align}
\{c \in \mathcal{C} : \mathbf{Y}(c) = \mathbf{y}\} = \{c \in \mathcal{C} : \mathbf{X}(c) = w(\mathbf{y})\}
\end{align}
$$
These are the same set of outcomes, so $P$ assigns them the same number: $P(\mathbf{Y} = \mathbf{y}) = p_{\mathbf{X}}(w(\mathbf{y}))$. The points are only relabeled; there is no volume to rescale.

**Why the continuous case does.** A continuous vector puts probability $0$ on every point, so a pdf is not a probability but probability per unit volume, $f_{\mathbf{X}}(\mathbf{x}) \approx P(\mathbf{X} \in \Delta V_{\mathbf{x}}) / \text{Vol}(\Delta V_{\mathbf{x}})$. A smooth map sends a small rectangle of area $dx_1\,dx_2$ to a small parallelogram of area $dy_1\,dy_2$, with $dx_1\,dx_2 = |J|\,dy_1\,dy_2$ ([[Determinant]] as the area scale factor of the [[Jacobian Matrix]]). The probability inside is conserved, $f_{\mathbf{X}}(\mathbf{x})\,dx_1\,dx_2 = f_{\mathbf{Y}}(\mathbf{y})\,dy_1\,dy_2$, hence $f_{\mathbf{Y}}(\mathbf{y}) = f_{\mathbf{X}}(w(\mathbf{y}))\,|J|$. The Jacobian compensates for the box stretching or shrinking while its mass stays fixed.

**Measure-theoretic unification.** Both pmf and pdf are [[Density with Respect to a Measure|densities]] (Radon-Nikodym derivatives) $dP/d\mu$, with different reference measures $\mu$:

| | Continuous | Discrete |
| --- | --- | --- |
| Reference measure $\mu$ | [[Lebesgue Measure]] $\lambda$ (area, volume) | Counting measure $\#$ |
| $P(A)$ | $\int_A f\,d\lambda$ | $\int_A p\,d\# = \sum_{\mathbf{x} \in A} p(\mathbf{x})$ |
| Meaning of density | probability per unit volume | probability per point |
| Under a bijection | volume scales by $\lvert J \rvert$ | a point maps to a point: $\#$ is invariant |
| Transformation rule | needs the factor $\lvert J \rvert$ | needs no factor |

Precisely, $|J|$ is itself a Radon-Nikodym derivative: the measure $B \mapsto \lambda(T^{-1}(B))$ on $\mathbf{y}$-space satisfies $\lambda(T^{-1}(B)) = \int_B |J|\,d\lambda$, so $|J| = \frac{d(\lambda \circ T^{-1})}{d\lambda}$. For counting measure, $\#(T^{-1}(B)) = \#(B)$ for $B \subseteq \mathcal{T}$, so the corresponding derivative is identically $1$.

> [!abstract] Theorem 3 ($n$-Dimensional One-to-One Transformation)[^3]
> Let $X_1, \dots, X_n$ be continuous with joint pdf $f(x_1, \dots, x_n)$, and let $y_i = u_i(x_1, \dots, x_n)$, $i = 1, \dots, n$, define a one-to-one transformation of $\mathcal{S}$ onto $\mathcal{T}$ with inverse $x_i = w_i(y_1, \dots, y_n)$. Assume the first partial derivatives of the inverse functions are continuous and the $n \times n$ Jacobian
> $$
> \begin{align}
> J = \det\left[\frac{\partial x_i}{\partial y_j}\right]_{i,j=1}^n = \begin{vmatrix} \frac{\partial x_1}{\partial y_1} & \cdots & \frac{\partial x_1}{\partial y_n} \\ \vdots & & \vdots \\ \frac{\partial x_n}{\partial y_1} & \cdots & \frac{\partial x_n}{\partial y_n} \end{vmatrix}
> \end{align}
> $$
> is not identically zero on $\mathcal{T}$. Then $Y_i = u_i(X_1, \dots, X_n)$ have joint pdf
> $$
> \begin{align}
> g(y_1, \dots, y_n) = f[w_1(y_1, \dots, y_n), \dots, w_n(y_1, \dots, y_n)]\,|J|, \quad (y_1, \dots, y_n) \in \mathcal{T}
> \end{align}
> $$
> and zero elsewhere.

This is a corollary of the $n$-fold [[Change of Variables]] theorem $\int \cdots \int_A f(\mathbf{x})\,d\mathbf{x} = \int \cdots \int_B f(w(\mathbf{y}))\,|J|\,d\mathbf{y}$ for $B = T(A)$, exactly as in two dimensions.

> [!abstract] Theorem 4 (Piecewise One-to-One Transformation)[^4]
> Suppose the transformation is not one-to-one, but $\mathcal{S}$ is a union of $k$ mutually disjoint sets $A_1, \dots, A_k$ such that the map is one-to-one from each $A_i$ onto $\mathcal{T}$, with inverse $x_j = w_{ji}(y_1, \dots, y_n)$ and Jacobian $J_i = \det[\partial w_{ji} / \partial y_l]$ (continuous partials, $J_i$ not identically zero). Then
> $$
> \begin{align}
> g(y_1, \dots, y_n) = \sum_{i=1}^k f[w_{1i}(y_1, \dots, y_n), \dots, w_{ni}(y_1, \dots, y_n)]\,|J_i|, \quad (y_1, \dots, y_n) \in \mathcal{T}
> \end{align}
> $$
> and zero elsewhere. The pdf of any single $Y_i$, say $Y_1$, is the [[Marginal Distribution|marginal]] $g_1(y_1) = \int \cdots \int g(y_1, \dots, y_n)\,dy_2 \cdots dy_n$.

Each point of $\mathcal{T}$ has exactly one preimage in each $A_i$, so $\{\mathbf{Y} \in B\}$ is the disjoint union of the events $\{\mathbf{X} \in A_i \cap T^{-1}(B)\}$; applying Theorem 3 to each and adding gives the sum. It is the density version of the discrete preimage sum in [[Random Variable Transformation]]. Hogg's hypothesis that every $A_i$ maps onto all of $\mathcal{T}$ can be relaxed: if $A_i$ maps one-to-one onto $\mathcal{T}_i \subseteq \mathcal{T}$, the sum runs only over the pieces with $\mathbf{y} \in \mathcal{T}_i$, and a boundary set of zero volume between pieces may be ignored.

# Techniques
- One-to-one change of variables: Theorems 1 and 2. For a single function $Y_1 = u_1(X_1, X_2)$, introduce an auxiliary $Y_2$ (often $Y_2 = X_2$) to make the map one-to-one, then take the [[Marginal Distribution]] of $Y_1$ by summing or integrating out $y_2$.
- [[Cumulative Distribution Function Method]]: works for arbitrary, non-injective, dimension-reducing transformations.
- [[Moment Generating Function Technique]]: best for linear combinations, especially of independent variables.
- [[Convolution Formula]]: the pdf of $X_1 + X_2$, obtained from Theorem 2 with $Y_1 = X_1 + X_2$, $Y_2 = X_2$.

# Properties
- Multivariate generalization of the univariate [[Random Variable Transformation]]; the $n$-dimensional version replaces $J$ by the $n \times n$ Jacobian determinant of the inverse map.
- If $T$ is only piecewise one-to-one, sum over the pieces (Theorem 4), as in the univariate case.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=116)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=118)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=160)
[^4]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=164)
