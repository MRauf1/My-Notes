---
tags:
  - statistics
  - mathematical_statistics
---

# Definition

> [!abstract] Theorem 1 ([[Cumulative Distribution Function]] [[Function Transformation|Transformation]] Technique)[^1]
> Let $X$ be [[Continuous Random Variable]] with pdf $f_X$ and support $S_X$, an open interval. Let $Y = g(X)$ where $g$ is [[Differentiable Function|differentiable]] on $S_X$ with $g'(x) \neq 0$ for all $x \in S_X$ (so $g$ is [[Injective Function|one-to-one]]). Denote the inverse by $x = g^{-1}(y)$. Then $Y$ has the pdf
> $$
> \begin{align}
> f_Y(y) = f_X(g^{-1}(y)) \left|\frac{dx}{dy}\right|, \quad y \in S_Y
> \end{align}
> $$
> where $\frac{dx}{dy} = \frac{d[g^{-1}(y)]}{dy}$ and $S_Y = \{g(x) : x \in S_X\}$ is the [[Random Variable Support|support]] of $Y$.

Hogg et al. call $J = \frac{dx}{dy}$ the Jacobian of the transformation, for convenience; in most of mathematics it is the [[Jacobian Matrix|Jacobian]] of the inverse transformation $x = g^{-1}(y)$. The result is proved by first computing the cdf $F_Y(y) = P(g(X) \leq y)$ and differentiating; the absolute value covers decreasing $g$, where the inequality flips. It is the one-dimensional case of [[Change of Variables]].

**Corrected hypotheses.** Hogg et al. assume only that $g$ is one-to-one and differentiable on $S_X$. The theorem is false under those hypotheses alone, so the statement above adds $g' \neq 0$ and that $S_X$ is an interval.
- *$g' \neq 0$ is necessary.* Let $K \subset [0,1]$ be a fat Cantor set ([[Generalized Cantor Set]]) with $m(K) = \tfrac12$, and $g(x) = \int_0^x \operatorname{dist}(t, K)\,dt$. Then $g$ is $C^1$ and strictly increasing, since $g' = \operatorname{dist}(\cdot, K) > 0$ on the open dense set $[0,1] \setminus K$. But $g' = 0$ on $K$, so $m(g(K)) \leq \int_K g' = 0$. For $X \sim \mathcal{U}(0,1)$, $P(Y \in g(K)) = \tfrac12$ while $m(g(K)) = 0$, so $Y = g(X)$ has no pdf. Zeros of $g'$ on a null set (e.g. $g(x) = x^3$ at $0$, where $g^{-1}(y) = y^{1/3}$ is not differentiable) are harmless; see Theorem 3 of [[Random Variable Transformation]].
- *$S_X$ an interval* is used for "one-to-one and continuous $\Rightarrow$ strictly monotone". Under $g' \neq 0$ it also follows from Darboux's theorem, since $g'$ cannot change sign without vanishing. Then $\frac{dx}{dy} = 1/g'(x)$ by the [[Inverse Function Theorem]]. On a disconnected support, apply the result piece by piece.
- *Continuity of $f_X$* is used by Hogg's proof, which differentiates $F_Y = F_X \circ g^{-1}$ via the [[Fundamental Theorem of Calculus]], but not by the theorem. Substituting $x = g^{-1}(t)$ directly in $P(Y \leq y) = \int_{\{g(x) \leq y\}} f_X(x)\,dx$ gives $F_Y(y) = \int_{-\infty}^y f_X(g^{-1}(t)) \left|\frac{dx}{dt}\right| dt$ for any pdf $f_X$, which is the definition of a pdf of $Y$. Pdfs are unique only [[Almost Everywhere|a.e.]], so the formula gives *a* pdf of $Y$.

Algorithm, assuming $Y = g(X)$ is one-to-one:[^1]
1. Find the support $S_Y$ of $Y$.
2. Solve $y = g(x)$ for $x$, obtaining $x = g^{-1}(y)$.
3. Obtain $\frac{dx}{dy}$.
4. The pdf of $Y$ is $f_Y(y) = f_X(g^{-1}(y)) \left|\frac{dx}{dy}\right|$ for $y \in S_Y$.

# Properties
- Despite its name, this is the change-of-variable (Jacobian) formula for smooth one-to-one $g$; the general cdf approach for arbitrary $g$ is the [[Cumulative Distribution Function Method]].
- Multivariate version: [[Random Vector Transformation]], with $|dx/dy|$ replaced by the absolute Jacobian determinant $|J|$.
- For non-injective $g$, sum over one-to-one pieces or use the cdf method directly (see [[Random Variable Transformation]]).
- [[Inverse Transform Sampling]] is the special case where $g = F^{-1}$ (the inverse of the target CDF) and $X \sim \mathcal{U}[0,1]$.
- Increasing case via the CDF:[^2] for invertible increasing $\tau$ and $Y = \tau(X)$, $P(Y \leq y) = P(X \leq \tau^{-1}(y))$, so $f_Y(y) = f_X(\tau^{-1}(y))\frac{d}{dy}\tau^{-1}(y)$; the location-scale case $Y = \mu + \sigma X$ gives $f_Y(y) = \frac{1}{\sigma}f_X\!\left(\frac{y - \mu}{\sigma}\right)$ ([[Non-Uniform Random Variate Generation]]).

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=71)
[^2]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=15&annotation=Y5N865ZQ); [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=14&annotation=M67I74UJ)
