---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Moment Generating Function of a Random Vector[^1]
> Let $\mathbf{X} = (X_1, X_2)^T$ be a [[Random Vector]]. If $E\left(e^{t_1 X_1 + t_2 X_2}\right)$ exists for $|t_1| < h_1$ and $|t_2| < h_2$ with $h_1, h_2 > 0$, it is the moment generating function of $\mathbf{X}$. With $\mathbf{t} = (t_1, t_2)^T$,
> $$
> \begin{align}
> M_{X_1, X_2}(\mathbf{t}) = E\left[e^{\mathbf{t}^T \mathbf{X}}\right]
> \end{align}
> $$

The vector form mirrors the univariate [[Moment Generating Function]] $E(e^{tX})$, with the product $tX$ replaced by the inner product $\mathbf{t}^T \mathbf{X}$. For $n$ components,[^3] if $E[\exp(t_1 X_1 + \dots + t_n X_n)]$ exists for $-h_i < t_i < h_i$, $h_i > 0$, the joint mgf is $M(\mathbf{t}) = E[e^{\mathbf{t}^T\mathbf{X}}]$ for $\mathbf{t} \in B = \{\mathbf{t} : -h_i < t_i < h_i\}$. It uniquely determines the joint distribution, hence all marginals: the mgf of $X_i$ is $M(0, \dots, 0, t_i, 0, \dots, 0)$, that of $(X_i, X_j)$ is $M$ with all other arguments $0$, and so on. $X_1, \dots, X_n$ are [[Mutually Independent Random Variables|mutually independent]] if and only if $M(t_1, \dots, t_n) = \prod_{i=1}^n M(0, \dots, 0, t_i, 0, \dots, 0)$.

# Properties
- Uniqueness: if it exists, it uniquely determines the joint distribution of $\mathbf{X}$.
- The [[Marginal Distribution|marginal]] mgfs are $M_{X_1}(t_1) = M_{X_1, X_2}(t_1, 0)$ and $M_{X_2}(t_2) = M_{X_1, X_2}(0, t_2)$.
- Mixed partial derivatives at $\mathbf{0}$ give mixed moments:[^2] differentiating under the integral, $\frac{\partial^{k+m} M(t_1, t_2)}{\partial t_1^k \partial t_2^m} = \iint x_1^k x_2^m e^{t_1 x_1 + t_2 x_2} f(x_1, x_2)\,dx_1\,dx_2$, so $\frac{\partial^{k+m} M}{\partial t_1^k \partial t_2^m}(\mathbf{0}) = E\left(X_1^k X_2^m\right)$ (sums in the discrete case); in particular the gradient at $\mathbf{0}$ is the [[Mean Vector]].
- Hence the first and second moments, and the [[Correlation]] coefficient, follow from the joint mgf:[^2]
$$
\begin{align}
\mu_1 &= \frac{\partial M(0,0)}{\partial t_1}, \quad \mu_2 = \frac{\partial M(0,0)}{\partial t_2}, \quad \sigma_1^2 = \frac{\partial^2 M(0,0)}{\partial t_1^2} - \mu_1^2, \quad \sigma_2^2 = \frac{\partial^2 M(0,0)}{\partial t_2^2} - \mu_2^2 \\
\text{Cov}(X_1, X_2) &= \frac{\partial^2 M(0,0)}{\partial t_1 \partial t_2} - \mu_1 \mu_2
\end{align}
$$
- $M_{\mathbf{X}}(\mathbf{t})$ is the univariate mgf of the projection $\mathbf{t}^T \mathbf{X}$ evaluated at $1$, so knowing the distribution of every linear combination $\mathbf{t}^T\mathbf{X}$ determines the distribution of $\mathbf{X}$ (Cramér-Wold idea).
- $X_1, X_2$ are [[Independent Random Variable|independent]] if and only if $M_{X_1, X_2}(t_1, t_2) = M_{X_1}(t_1) M_{X_2}(t_2)$ near $\mathbf{0}$ ([[Independent Random Variable Equivalent Conditions]]).

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=112)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=147)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=154)
