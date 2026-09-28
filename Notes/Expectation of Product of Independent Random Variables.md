---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Expectation of Product of Independent Random Variables[^1]
> Suppose $X_1$ and $X_2$ are [[Independent Random Variable|independent]] and $E[u(X_1)]$ and $E[v(X_2)]$ exist. Then
> $$
> \begin{align}
> E[u(X_1) v(X_2)] = E[u(X_1)]\,E[v(X_2)]
> \end{align}
> $$
> In particular, with $u, v$ the identity, $E(X_1 X_2) = E(X_1) E(X_2)$.

Proof (continuous case): $E[u(X_1) v(X_2)] = \iint u(x_1) v(x_2) f_1(x_1) f_2(x_2)\,dx_1\,dx_2 = \int u f_1 \cdot \int v f_2$, by [[Fubini's Theorem]] applied to the product density.

For $n$ [[Mutually Independent Random Variables|mutually independent]] variables,[^2] $E\left[\prod_{i=1}^n u_i(X_i)\right] = \prod_{i=1}^n E[u_i(X_i)]$.

# Properties
- Without independence, the [[Expectation]] of a product is generally not the product of the expectations.
- Hence independent variables are uncorrelated: $\text{Cov}(X_1, X_2) = E(X_1 X_2) - E(X_1) E(X_2) = 0$ ([[Covariance]]). The converse fails: $E(X_1 X_2) = E(X_1) E(X_2)$ does not imply independence.
- The converse does hold if the identity is required for all bounded $u, v$ (or all $u = e^{t_1 x_1}, v = e^{t_2 x_2}$ when mgfs exist), which is the MGF criterion in [[Independent Random Variable Equivalent Conditions]].
- Gives $M_{X_1 + X_2}(t) = M_{X_1}(t) M_{X_2}(t)$ and $\text{Var}(X_1 + X_2) = \text{Var}(X_1) + \text{Var}(X_2)$ for independent $X_1, X_2$.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=138)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=154)
