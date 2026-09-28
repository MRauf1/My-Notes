---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Cumulative Distribution Function Method[^1]
> Let $\mathbf{X} = (X_1, \dots, X_n)^T$ be a [[Random Vector]] with known joint distribution and let $Y = g(\mathbf{X})$ for any (measurable) $g: \mathbb{R}^n \to \mathbb{R}$. Then the [[Cumulative Distribution Function|cdf]] of $Y$ is the probability of a region in $\mathbf{x}$-space,
> $$
> \begin{align}
> F_Y(y) = P[g(\mathbf{X}) \leq y] = P[\mathbf{X} \in A_y], \qquad A_y = \{\mathbf{x} : g(\mathbf{x}) \leq y\}
> \end{align}
> $$
> computed as
> $$
> \begin{align}
> F_Y(y) = \int \cdots \int_{A_y} f_{\mathbf{X}}(\mathbf{x})\,d\mathbf{x} \quad \text{(continuous)}, \qquad F_Y(y) = \sum_{\mathbf{x} \in A_y} p_{\mathbf{X}}(\mathbf{x}) \quad \text{(discrete)}
> \end{align}
> $$
> If $F_Y$ is differentiable, the pdf of $Y$ is $f_Y(y) = F_Y'(y)$.

This is the most general method: it needs no injectivity, no differentiability of $g$, and no auxiliary variables, because it uses only the definition of the cdf and the equality of events $\{g(\mathbf{X}) \leq y\} = \{\mathbf{X} \in A_y\}$. The change-of-variable formulas ([[Cumulative Distribution Function Transformation Technique]], [[Random Vector Transformation]]) are derived from it for the special case of smooth one-to-one $g$.

**Procedure.**
1. Find the [[Random Variable Support|support]] of $Y$, i.e. the range of $g$ on the support of $\mathbf{X}$.
2. For each $y$, describe the sublevel set $A_y = \{\mathbf{x} : g(\mathbf{x}) \leq y\}$ intersected with the support of $\mathbf{X}$. Its shape often changes as $y$ crosses critical values, so $F_Y$ is typically piecewise.
3. Compute $P[\mathbf{X} \in A_y]$ by iterated integration ([[Fubini's Theorem]]) with $y$-dependent limits, or by summation. It is often easier to compute the complement $P[g(\mathbf{X}) > y]$.
4. Differentiate in $y$ (by the Leibniz integral rule when $y$ appears in the limits) to get $f_Y$; check $F_Y$ for jumps first.
5. Check for atoms: if $g$ is constant on a set of positive probability, $F_Y$ jumps there and $Y$ is a discrete or [[Mixture Random Variable|mixture]] random variable, which no density formula would reveal.

**Joint version.** For $\mathbf{Y} = (g_1(\mathbf{X}), \dots, g_k(\mathbf{X}))$, the [[Joint Cumulative Distribution Function]] is $F_{\mathbf{Y}}(\mathbf{y}) = P[g_1(\mathbf{X}) \leq y_1, \dots, g_k(\mathbf{X}) \leq y_k]$, the probability of an intersection of sublevel sets, and the joint pdf is the mixed partial $\partial^k F_{\mathbf{Y}} / \partial y_1 \cdots \partial y_k$.

**$n$ variables to $n$ variables.**[^2] For $\mathbf{Y} = (u_1(\mathbf{X}), \dots, u_n(\mathbf{X}))$ with $\mathbf{X}$ continuous,
$$
\begin{align}
F_{\mathbf{Y}}(\mathbf{y}) = \int \cdots \int_{A_{\mathbf{y}}} f_{\mathbf{X}}(\mathbf{x})\,d\mathbf{x}, \qquad A_{\mathbf{y}} = \{\mathbf{x} : u_1(\mathbf{x}) \leq y_1, \dots, u_n(\mathbf{x}) \leq y_n\}
\end{align}
$$
and $g(\mathbf{y}) = \frac{\partial^n F_{\mathbf{Y}}}{\partial y_1 \cdots \partial y_n}(\mathbf{y})$. When $u$ is smooth and one-to-one, substituting $\mathbf{x} = w(\mathbf{y}')$ turns this into $F_{\mathbf{Y}}(\mathbf{y}) = \int_{\mathbf{y}' \leq \mathbf{y}} f(w(\mathbf{y}'))\,|J|\,d\mathbf{y}'$, and the mixed partial recovers the Jacobian formula of [[Random Vector Transformation]]; when it is only piecewise one-to-one, $A_{\mathbf{y}}$ splits over the pieces and the sum over $|J_i|$ appears. In practice, for $n$ outputs it is often easier to use the Jacobian formula, and to reserve the cdf method for a single (or a few) outputs $Y = g(X_1, \dots, X_n)$, where it avoids introducing $n - 1$ auxiliary variables and integrating them back out.

**$n$ iid inputs.** If $X_1, \dots, X_n$ are [[Independent and Identically Distributed|iid]] with cdf $F$ and pdf $f$, the region $A_y$ often factors because the joint density is a product:
- Maximum: $P[\max_i X_i \leq y] = P[X_1 \leq y, \dots, X_n \leq y] = F(y)^n$, so $f_{\max}(y) = n F(y)^{n-1} f(y)$.
- Minimum: $P[\min_i X_i > y] = [1 - F(y)]^n$, so $F_{\min}(y) = 1 - [1 - F(y)]^n$ and $f_{\min}(y) = n[1 - F(y)]^{n-1} f(y)$.
- $k$th order statistic: $P[X_{(k)} \leq y] = \sum_{j=k}^n \binom{n}{j} F(y)^j [1 - F(y)]^{n-j}$, the probability that at least $k$ of the $n$ variables fall below $y$ (a [[Binomial Distribution]] tail).
- Sum: $F_{S_n}(y) = P[X_1 + \dots + X_n \leq y]$ is the integral of $\prod_i f(x_i)$ over a half-space; differentiating gives the $n$-fold [[Convolution Formula|convolution]] $f^{*n}$.
- Norm: $F_{\lVert \mathbf{X} \rVert}(r) = P[\mathbf{X} \in \text{ball of radius } r]$, computed in spherical coordinates when the joint density is radially symmetric.

**Geometric form of the derivative.** For smooth $g$ with $\nabla g \neq 0$ on the level set, differentiating $F_Y(y) = \int_{\{g \leq y\}} f_{\mathbf{X}}$ with respect to $y$ gives the rate at which probability crosses the moving boundary $\{g = y\}$, which by the coarea formula is
$$
\begin{align}
f_Y(y) = \int_{\{\mathbf{x} : g(\mathbf{x}) = y\}} \frac{f_{\mathbf{X}}(\mathbf{x})}{\lVert \nabla g(\mathbf{x}) \rVert}\,dS(\mathbf{x})
\end{align}
$$
a surface integral over the level set. The factor $1/\lVert \nabla g \rVert$ is the thickness of the shell $\{y < g \leq y + dy\}$ per unit $dy$; in one dimension it reduces to $\sum_{x : g(x) = y} f_X(x)/|g'(x)|$, the piecewise one-to-one formula of [[Random Variable Transformation]]. This is the same moving-boundary computation as the [[Reynolds Transport Theorem]].

# Properties
- Standard applications: maxima and minima, $F_{\max(X_1, X_2)}(y) = F_{X_1, X_2}(y, y)$ and $P[\min(X_1, X_2) > y] = P[X_1 > y, X_2 > y]$ (the route to order statistics); sums, products, ratios, and norms $\lVert \mathbf{X} \rVert$ via the regions $x_1 + x_2 \leq y$, $x_1 x_2 \leq y$, $x_1 / x_2 \leq y$, $\lVert \mathbf{x} \rVert \leq y$.
- Differentiating the cdf of $X_1 + X_2$ gives the [[Convolution Formula]].
- Also valid for univariate $Y = g(X)$, the case $n = 1$ (e.g. $F_{X^2}(y) = F_X(\sqrt{y}) - F_X((-\sqrt{y})^-)$).
- Alternatives when the region is hard to describe: the [[Moment Generating Function Technique]] for linear combinations, and the one-to-one Jacobian method with an auxiliary variable.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=116)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=163)
