---
tags:
  - statistics
  - mathematical_statistics
---

# Definition

> [!info] Definition 1 ([[Random Variable]] [[Function Transformation|Transformation]])[^1]
> Given a random variable $X$ with known distribution and a [[Function]] $g$, the transformed random variable is $Y = g(X)$, i.e. $Y(c) = g(X(c))$. The problem is to find the distribution of $Y$. If $X$ has space $\mathcal{D}_X$, then $Y$ has space $\mathcal{D}_Y = \{g(x) : x \in \mathcal{D}_X\}$.

> [!abstract] Theorem 1 (Discrete Transformation, One-to-One Case)[^1]
> For a [[Discrete Random Variable]] $X$ with pmf $p_X$ and a [[Injective Function|one-to-one]] $g$,
> $$
> \begin{align}
> p_Y(y) = P[g(X) = y] = P[X = g^{-1}(y)] = p_X(g^{-1}(y)), \quad y \in \mathcal{D}_Y
> \end{align}
> $$

> [!abstract] Theorem 2 (Discrete Transformation, General Rule)
> For a [[Discrete Random Variable]] $X$ with pmf $p_X$ and any $g$,
> $$
> \begin{align}
> p_Y(y) = P[g(X) = y] = \sum_{x \in \mathcal{D}_X : g(x) = y} p_X(x), \quad y \in \mathcal{D}_Y
> \end{align}
> $$
> Theorem 1 is the case where $g$ is one-to-one: the sum then has a single term.

> [!abstract] Theorem 3 (Continuous Transformation, Piecewise One-to-One)[^2]
> Let $X$ be a [[Continuous Random Variable]] with pdf $f_X$ and support $S_X$, and $Y = g(X)$. Suppose $S_X = A_0 \cup A_1 \cup \dots \cup A_k$ (disjoint, $k \le \infty$) with $P(X \in A_0) = 0$, each $A_i$ ($i \geq 1$) open, and $g_i := g|_{A_i}$ strictly monotone and differentiable with $g_i' \neq 0$ on $A_i$. Let $B_i = g(A_i)$. Then $Y$ is continuous with
> $$
> \begin{align}
> f_Y(y) = \sum_{i \geq 1} f_X\big(g_i^{-1}(y)\big)\left|\frac{d}{dy} g_i^{-1}(y)\right| \mathbf{1}_{B_i}(y) = \sum_{x \in g^{-1}(y) \setminus A_0} \frac{f_X(x)}{|g'(x)|}
> \end{align}
> $$
> This is the continuous counterpart of Theorem 2: the same preimage sum, with each point weighted by $1/|g'(x)|$. The case $k = 1$, $A_0 = \emptyset$ is [[Cumulative Distribution Function Transformation Technique|the one-to-one Jacobian formula]].

Casella & Berger state Theorem 3 for finite $k$ and $f_X$ continuous on each $A_i$. Neither restriction is needed: apply the one-to-one [[Change of Variables]] on each piece and sum, with Tonelli justifying the swap of sum and integral. The hypothesis $g' \neq 0$ off a null set is essential: if $g$ is constant on a set of positive probability, $Y$ has an atom and no pdf. Isolated zeros of $g'$ (e.g. $x = 0$ for $g(x) = x^2$) go into $A_0$. For vectors, $|g'|$ becomes $|\det J_g|$ ([[Random Vector Transformation]]).

**Why pdfs need the Jacobian but cdfs don't.** A cdf value is the probability of an event, and $\{Y \leq y\} = \{X \leq g^{-1}(y)\}$ (for increasing $g$) is the same set of outcomes, so $F_Y = F_X \circ g^{-1}$ with no correction factor. A pdf is probability *per unit length*, $f_Y = dF_Y/dy$, and the chain rule converts "per unit $x$" into "per unit $y$". The invariant quantity is $f_X(x)\,dx = f_Y(y)\,dy$, not $f$ itself. As a result, for strictly monotone $g$:
- **Invariant** (defined by probabilities of events): cdf values, [[Quantile Function|quantiles]] ($\xi_p^Y = g(\xi_p^X)$ for increasing $g$, $\xi_p^Y = g(\xi_{1-p}^X)$ for decreasing $g$), and in particular the [[Median]].
- **Not invariant** (defined by the pdf's values): the pdf itself and the [[Mode]]. In general $\operatorname{mode}(g(X)) \neq g(\operatorname{mode}(X))$, because the factor $|dx/dy|$ moves the maximum. The two agree for affine $g$, where the factor is constant. (The mean is not invariant either, $E[g(X)] \neq g(E[X])$, but for a different reason: nonlinearity of $g$, not the Jacobian.)

This is why **MAP depends on the parametrization while the MLE does not** ([[Maximum Likelihood vs Maximum a Posteriori Estimation]]). The posterior $p(\theta | \mathcal{D})$ is a density *in $\theta$*, so under $\eta = g(\theta)$ it becomes $p(\eta | \mathcal{D}) = p(g^{-1}(\eta) | \mathcal{D}) \left|\frac{d\theta}{d\eta}\right|$, and its mode (the MAP estimate) moves. The likelihood $L(\theta) = p(\mathcal{D} | \theta)$ is a density in the *data*, but only a function of $\theta$. Reparametrizing relabels its argument, $L^*(\eta) = L(g^{-1}(\eta))$, with no Jacobian, so $\hat{\eta} = g(\hat{\theta})$ ([[Maximum Likelihood Estimator Invariance]]).

Hogg et al. say that for non-one-to-one $g$ there is no overall rule, but there is: Theorem 2 always holds. What lacks a single formula is computing the preimage, which depends on $g$. The practical recipe is: list the points of $\mathcal{D}_Y$, and for each $y$ collect the $x$ values mapping to it and add their probabilities.

# Techniques
- **Pmf (preimage) method**, discrete case: Theorems 1 and 2.
- **Cdf method**, any case ([[Cumulative Distribution Function Method]]): compute $F_Y(y) = P(g(X) \leq y) = P(X \in \{x : g(x) \leq y\})$ directly, then differentiate for a pdf. It handles non-monotone $g$ by splitting the set $\{x : g(x) \leq y\}$ into intervals (e.g. for $Y = X^2$, $F_Y(y) = F_X(\sqrt{y}) - F_X\big((-\sqrt{y})^-\big)$ for $y \geq 0$).
- **Change-of-variable (Jacobian) method**, continuous one-to-one $g$: [[Cumulative Distribution Function Transformation Technique]], $f_Y(y) = f_X(g^{-1}(y)) \left|\frac{dx}{dy}\right|$.
- **Piecewise one-to-one extension**, continuous non-monotone $g$: Theorem 3.
- **Mgf method** ([[Moment Generating Function Technique]]): compute $M_Y(t) = E[e^{t g(X)}]$ and recognize it, using the [[Moment Generating Function Equal Distribution Theorem]]. Most useful for sums of [[Independent Random Variable|independent]] variables.
- For functions of several random variables, see [[Random Vector Transformation]].
- [[Inverse Transform Sampling]] is the special case where the transformation is an inverse cdf applied to a uniform variable.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=63)
[^2]: Casella & Berger, *Statistical Inference* (2nd ed.), Theorem 2.1.8
