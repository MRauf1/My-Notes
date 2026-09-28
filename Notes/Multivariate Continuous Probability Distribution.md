---
tags:
  - statistics
  - bayesian_statistics
  - mathematical_statistics
---

# Definition

> [!info] Definition 1 ([[Multivariate Probability Distribution]] [[Continuous]])
> [[Multivariate Probability Distribution]] where the [[Random Variable]] are [[Continuous]]. The pdf is
> $$
> \begin{align}
> f(x_1, \dots, x_n)
> \end{align}
> $$

> [!info] Definition 2 (Continuous Random Vector and Joint PDF)[^1]
> A [[Random Vector]] $(X_1, X_2)$ is of the continuous type if its [[Joint Cumulative Distribution Function]] $F_{X_1, X_2}$ is continuous. It usually has a representation
> $$
> \begin{align}
> F_{X_1, X_2}(x_1, x_2) = \int_{-\infty}^{x_1} \int_{-\infty}^{x_2} f_{X_1, X_2}(w_1, w_2)\,dw_2\,dw_1, \quad (x_1, x_2) \in \mathbb{R}^2
> \end{align}
> $$
> and the nonnegative integrand $f_{X_1, X_2}$ is the joint probability density function. Then
> $$
> \begin{align}
> \frac{\partial^2 F_{X_1, X_2}(x_1, x_2)}{\partial x_1 \partial x_2} = f_{X_1, X_2}(x_1, x_2)
> \end{align}
> $$
> except possibly on events of probability zero.

For $n$ variables, $X_1, \dots, X_n$ are of the continuous type if $F_{\mathbf{X}}(\mathbf{x}) = \int_{-\infty}^{x_1} \cdots \int_{-\infty}^{x_n} f(w_1, \dots, w_n)\,dw_n \cdots dw_1$, and then $\frac{\partial^n}{\partial x_1 \cdots \partial x_n} F_{\mathbf{X}}(\mathbf{x}) = f(\mathbf{x})$ except possibly on a set of probability zero. A function $f$ is essentially a joint pdf if it is nonnegative for all real arguments and integrates to $1$ over $\mathbb{R}^n$.[^2]

For an event $A \subseteq \mathcal{D}$,
$$
\begin{align}
P[(X_1, X_2) \in A] = \iint_A f_{X_1, X_2}(x_1, x_2)\,dx_1\,dx_2
\end{align}
$$
the volume under the surface $z = f_{X_1, X_2}(x_1, x_2)$ over $A$. The [[Double Riemann Integral]] is computed as iterated one-dimensional integrals ([[Fubini's Theorem]]). By convention $f$ is extended by zero outside $\mathcal{D}$, so $\iint_{\mathcal{D}}$ can be written $\int_{-\infty}^\infty \int_{-\infty}^\infty$.

# Properties
## Definitional Properties
- [[Multivariate Continuous Probability Distribution Definitional Properties]]: $f_{X_1, X_2}(x_1, x_2) \geq 0$ and $\iint_{\mathcal{D}} f_{X_1, X_2}(x_1, x_2)\,dx_1\,dx_2 = 1$, which essentially characterize joint pdfs.

## Other
- Its support $\mathcal{S} = \{(x_1, x_2) : f(x_1, x_2) > 0\} \subseteq \mathcal{D}$ ([[Random Variable Support]]).
- The [[Marginal Distribution|marginal pdf]] of $X_1$ is obtained by integrating out $x_2$.
- Rectangle probabilities are corner differences of the cdf, the two-dimensional [[Fundamental Theorem of Calculus]] (see [[Joint Cumulative Distribution Function]]).

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=103)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=150)
