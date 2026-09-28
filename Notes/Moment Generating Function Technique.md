---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Moment Generating Function Technique[^1]
> To find the distribution of $Z = u(X_1, X_2)$, compute its [[Moment Generating Function|mgf]] directly from the joint distribution of $(X_1, X_2)$, using the expectation of a function of a [[Random Vector]]:
> $$
> \begin{align}
> M_Z(t) = E\left[e^{t u(X_1, X_2)}\right] = \int_{-\infty}^\infty \int_{-\infty}^\infty e^{t u(x_1, x_2)} f_{X_1, X_2}(x_1, x_2)\,dx_1\,dx_2
> \end{align}
> $$
> (sums replacing integrals in the discrete case). For $n$ variables,[^4] $Y = g(X_1, \dots, X_n)$ has $M_Y(t) = \int \cdots \int e^{t g(x_1, \dots, x_n)} f(x_1, \dots, x_n)\,dx_1 \cdots dx_n$. If $M_Z$ is recognized as the mgf of a known distribution, then $Z$ has that distribution.

The recognition step is justified by uniqueness of mgfs ([[Moment Generating Function Equal Distribution Theorem]]).

> [!abstract] Theorem 1 (MGF of a Linear Combination of Independent Random Variables)[^2]
> Let $X_1, \dots, X_n$ be [[Mutually Independent Random Variables|mutually independent]], with $X_i$ having mgf $M_i(t)$ for $-h_i < t < h_i$, $h_i > 0$. Let $T = \sum_{i=1}^n k_i X_i$ for constants $k_i$. Then
> $$
> \begin{align}
> M_T(t) = \prod_{i=1}^n M_i(k_i t), \quad -\min_i\{h_i\} < t < \min_i\{h_i\}
> \end{align}
> $$

Proof: $M_T(t) = E\left[\prod_i e^{t k_i X_i}\right] = \prod_i E\left[e^{(k_i t) X_i}\right]$ by independence. (Strictly, the interval should be $|t| < \min_i\{h_i / |k_i|\}$ over $k_i \neq 0$, so that each $k_i t$ lies in the domain of $M_i$; Hogg's interval assumes $|k_i| \leq 1$.)

> [!abstract] Corollary 1 (Sum of iid Random Variables)[^3]
> If $X_1, \dots, X_n$ are [[Independent and Identically Distributed|iid]] with common mgf $M(t)$ for $-h < t < h$, then $T = \sum_{i=1}^n X_i$ has mgf $M_T(t) = [M(t)]^n$ for $-h < t < h$.

# Properties
- Works well for linear functions, via Theorem 1. This gives closure results such as sums of independent [[Poisson Distribution|Poisson]], [[Normal Distribution|normal]], [[Gamma Distribution|gamma]], and [[Chi-Squared Distribution Addition|chi-squared]] variables.
- Limitations: it needs the mgf to exist near $0$ and to be recognizable; for non-linear $u$ the integral rarely has a familiar form, and the [[Cumulative Distribution Function Method]] is used instead. The [[Characteristic Function (Probability)|characteristic function]] removes the existence requirement.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=123)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=154)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=156)
[^4]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=165)
