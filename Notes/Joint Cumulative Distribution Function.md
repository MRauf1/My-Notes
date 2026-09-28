---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Joint Cumulative Distribution Function[^1]
> For a [[Random Vector]] $(X_1, X_2)$, the joint cdf is
> $$
> \begin{align}
> F_{X_1, X_2}(x_1, x_2) = P[\{X_1 \leq x_1\} \cap \{X_2 \leq x_2\}] = P[X_1 \leq x_1, X_2 \leq x_2], \quad (x_1, x_2) \in \mathbb{R}^2
> \end{align}
> $$
> More generally, for $\mathbf{X} = (X_1, \dots, X_n)^T$, $F_{\mathbf{X}}(\mathbf{x}) = P[X_1 \leq x_1, \dots, X_n \leq x_n]$.

The expression is well defined because each $\{X_i \leq x_i\}$ is an [[Event]] of the original [[Sample Space]] $\mathcal{C}$, and so is their [[Set Intersection|intersection]]. The joint cdf uniquely determines the induced distribution $P_{X_1, X_2}$.

> [!abstract] Theorem 1 (Rectangle Probability)[^1]
> For $a_1 < b_1$ and $a_2 < b_2$,
> $$
> \begin{align}
> P[a_1 < X_1 \leq b_1, a_2 < X_2 \leq b_2] = F(b_1, b_2) - F(a_1, b_2) - F(b_1, a_2) + F(a_1, a_2)
> \end{align}
> $$
> so the probability of every rectangle $(a_1, b_1] \times (a_2, b_2]$ is expressed through the cdf.

> [!abstract] Theorem 2 (Box Probability in $n$ Dimensions)
> For $\mathbf{a} < \mathbf{b}$ componentwise, let $\mathbf{c}_I$ be the corner of the box with $c_{I,i} = a_i$ for $i \in I$ and $c_{I,i} = b_i$ for $i \notin I$. Then
> $$
> \begin{align}
> P[\mathbf{a} < \mathbf{X} \leq \mathbf{b}] = \sum_{I \subseteq \{1, \dots, n\}} (-1)^{|I|} F(\mathbf{c}_I) = \Delta^{(1)}_{a_1, b_1} \cdots \Delta^{(n)}_{a_n, b_n} F
> \end{align}
> $$
> where $\Delta^{(i)}_{a_i, b_i} G = G|_{x_i = b_i} - G|_{x_i = a_i}$ is the difference operator in coordinate $i$. The sum runs over the $2^n$ corners, with sign $-1$ for each coordinate set to its lower endpoint.

**Connection to [[Probability of Set Union|inclusion-exclusion]].** Theorem 2 is the inclusion-exclusion formula in disguise. Let $A_i = \{\mathbf{X} \leq \mathbf{b}, X_i \leq a_i\}$. Then
$$
\begin{align}
\{\mathbf{a} < \mathbf{X} \leq \mathbf{b}\} = \{\mathbf{X} \leq \mathbf{b}\} \setminus \bigcup_{i=1}^n A_i, \qquad \bigcap_{i \in I} A_i = \{\mathbf{X} \leq \mathbf{c}_I\}
\end{align}
$$
so every intersection of the $A_i$ is again a lower orthant with probability $F(\mathbf{c}_I)$. Therefore $P = F(\mathbf{b}) - P\left(\bigcup_i A_i\right) = F(\mathbf{b}) - \sum_{I \neq \emptyset} (-1)^{|I|+1} F(\mathbf{c}_I)$, which is Theorem 2. For $n = 2$ this is $P(A \setminus (B \cup C)) = P(A) - P(B) - P(C) + P(B \cap C)$.

**Connection to the iterated [[Fundamental Theorem of Calculus]].** For an absolutely continuous vector with joint pdf $f$, $F(\mathbf{x}) = \int_{-\infty}^{x_1} \cdots \int_{-\infty}^{x_n} f(\mathbf{w})\,d\mathbf{w}$, so Theorem 2 also equals $\int_{\mathbf{a}}^{\mathbf{b}} f$. This is the $n$-fold FTC:

> [!abstract] Theorem 3 ($n$-Fold Iterated Fundamental Theorem of Calculus)
> If $G$ is $C^n$ on a neighborhood of the box $[\mathbf{a}, \mathbf{b}] \subseteq \mathbb{R}^n$, then
> $$
> \begin{align}
> \int_{a_1}^{b_1} \cdots \int_{a_n}^{b_n} \frac{\partial^n G}{\partial x_1 \cdots \partial x_n}\,dx_n \cdots dx_1 = \Delta^{(1)}_{a_1, b_1} \cdots \Delta^{(n)}_{a_n, b_n} G = \sum_{I \subseteq \{1, \dots, n\}} (-1)^{|I|} G(\mathbf{c}_I)
> \end{align}
> $$
> For $n = 2$: $\int_{a_1}^{b_1} \int_{a_2}^{b_2} \frac{\partial^2 G}{\partial x_1 \partial x_2}\,dx_2\,dx_1 = G(b_1, b_2) - G(a_1, b_2) - G(b_1, a_2) + G(a_1, a_2)$.

Proof: by [[Fubini's Theorem]], integrate one coordinate at a time; each one-dimensional integral of a partial derivative is the FTC, $\int_{a_i}^{b_i} \partial_i H\,dx_i = \Delta^{(i)} H$, and $\Delta^{(i)}$ commutes with differentiation and integration in the other coordinates.

**Connection to [[Green's Theorem]] and Stokes' theorem.** Each FTC step is the generalized Stokes theorem $\int_\Omega d\omega = \int_{\partial\Omega} \omega$ on a single interval, whose oriented boundary is $\{b_i\} - \{a_i\}$; the sign $(-1)^{|I|}$ of a corner is its orientation in the boundary of the box viewed as a product of oriented intervals. For $n = 2$ it is literally Green's theorem: with $M = 0$ and $N = \partial G / \partial x_2$,
$$
\begin{align}
\iint_{[a_1,b_1] \times [a_2,b_2]} \frac{\partial^2 G}{\partial x_1 \partial x_2}\,dA = \oint_{\partial R} \frac{\partial G}{\partial x_2}\,dx_2
\end{align}
$$
and the boundary integral lives only on the two vertical edges, each contributing a one-dimensional FTC: $[G(b_1, b_2) - G(b_1, a_2)] - [G(a_1, b_2) - G(a_1, a_2)]$. The difference from Stokes is that Stokes lowers the dimension once (from $\Omega$ to the $(n-1)$-dimensional $\partial\Omega$), while here the integrand is a pure mixed partial (a very special [[Exterior Derivative|exact form]]), which lets the reduction be repeated all the way down to the $0$-dimensional corners of the box.

**Why the probabilistic version needs no differentiability.** Theorem 3 needs smooth $G$, but Theorem 1 and Theorem 2 do not: they follow from the axioms of [[Probability]] alone (via inclusion-exclusion), so they hold for every random vector, whether discrete, continuous, mixed, or without any density. When a density exists, $\int_{\text{box}} f = \Delta \cdots \Delta F$ holds even if $f$ is discontinuous and $F$ is not twice differentiable everywhere; the mixed partial $\partial^n F / \partial x_1 \cdots \partial x_n$ equals $f$ only at continuity points of $f$ (in general, except on a set of probability zero). The derivative relation is the fragile one; the difference formula is the robust definition, and it is exactly how a cdf defines a measure on boxes (the Lebesgue-Stieltjes construction).

# Properties
- Marginal cdfs are limits of the joint cdf: $F_{X_1}(x_1) = \lim_{x_2 \uparrow \infty} F(x_1, x_2)$ (see [[Marginal Distribution]]).
- A function $F: \mathbb{R}^n \to [0, 1]$ is a joint cdf if and only if it is right-continuous in each coordinate, tends to $0$ when any coordinate tends to $-\infty$ and to $1$ when all tend to $+\infty$, and every box difference $\Delta^{(1)} \cdots \Delta^{(n)} F \geq 0$ ($n$-increasing). Being nondecreasing in each coordinate separately is not enough.
- The mixed partial $\frac{\partial^2 F}{\partial x_1 \partial x_2} = f$ recovers the joint pdf of a [[Multivariate Continuous Probability Distribution]] except possibly on events of probability zero.
- Generalizes the univariate [[Cumulative Distribution Function]] and its interval formula $P(a < X \leq b) = F(b) - F(a)$, the case $n = 1$ of Theorem 2.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=102)
