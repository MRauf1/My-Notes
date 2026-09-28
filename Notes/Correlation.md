---
tags:
  - statistics
  - bayesian_statistics
  - mathematical_statistics
---

# Definition

> [!info] Definition 1 (Correlation Coefficient)[^1][^2]
> Let $X_1, X_2$ be [[Random Variable|random variables]] with standard deviations $\sigma_1 > 0$ and $\sigma_2 > 0$. Their correlation coefficient is
> $$
> \begin{align}
> \rho_{X_1, X_2} = Corr[X_1, X_2] = \frac{Cov[X_1, X_2]}{\sigma_{X_1} \sigma_{X_2}} = \frac{E[(X_1 - \mu_1)(X_2 - \mu_2)]}{\sigma_1 \sigma_2}
> \end{align}
> $$

Correlation is a scale-free summary of the joint relationship of the two random variables, unlike [[Covariance]], which depends on their scales. It is the covariance of the standardized variables $(X_1 - \mu_1)/\sigma_1$ and $(X_2 - \mu_2)/\sigma_2$, and it measures the degree of linearity between $X_1$ and $X_2$. It is one of many possible measures of dependence.

Geometrically, treating centered random variables as vectors with inner product $\langle U, V \rangle = E[UV]$, $\rho$ is the cosine of the angle between $X_1 - \mu_1$ and $X_2 - \mu_2$.

> [!abstract] Theorem 1 (Correlation Bounds)[^3]
> For all jointly distributed $(X_1, X_2)$ whose correlation coefficient exists,
> $$
> \begin{align}
> -1 \leq \rho \leq 1
> \end{align}
> $$
> with $\rho = \pm 1$ if and only if $X_2 = a + b X_1$ with probability one, where $\text{sign}(b) = \rho$.

Proof: $h(v) = E\{[(X_1 - \mu_1) + v(X_2 - \mu_2)]^2\} = \sigma_1^2 + 2v\rho\sigma_1\sigma_2 + v^2\sigma_2^2 \geq 0$ for all $v$, so its discriminant $4\rho^2\sigma_1^2\sigma_2^2 - 4\sigma_1^2\sigma_2^2 \leq 0$, i.e. $\rho^2 \leq 1$. This is the [[Cauchy-Schwarz Inequality]] for random variables. The discriminant is $0$ exactly when $\rho = \pm 1$, when $h$ has a root $v_0$ and $(X_1 - \mu_1) + v_0(X_2 - \mu_2) = 0$ with probability one: a degenerate, exactly linear relationship.

> [!abstract] Theorem 2 (Independence Implies Zero Correlation)[^3]
> If $X_1$ and $X_2$ are [[Independent Random Variable|independent]], then $Cov[X_1, X_2] = 0$ and hence $\rho = 0$.

The converse is false: uncorrelated variables can be dependent (e.g. $X_2 = X_1^2$ with $X_1$ symmetric about $0$). The contrapositive holds: if $\rho \neq 0$, then $X_1$ and $X_2$ are dependent. (Hogg et al. print this as "if $\rho = 0$ then $X$ and $Y$ are dependent", a typo for $\rho \neq 0$.)

# Properties
- Correlation of a variable with itself is always $1$ (when $\sigma > 0$).
- Invariant under positive affine maps: $Corr[aX_1 + b, cX_2 + d] = \text{sign}(ac)\,Corr[X_1, X_2]$ for $ac \neq 0$.
- For intermediate $|\rho| < 1$, under a linear conditional mean $\rho$ measures how tightly probability concentrates in a band around the line $E(X_2 | x_1) = \mu_2 + \rho \frac{\sigma_2}{\sigma_1}(x_1 - \mu_1)$ ([[Linear Conditional Expectation Theorem]]).
- $\rho^2$ is the fraction of $Var[X_2]$ explained by the best linear predictor of $X_2$ from $X_1$.
- Computable from the joint mgf via the means, variances, and covariance ([[Moment Generating Function of Random Vector]]).

[^1]: [Bayesian Statistical Methods](zotero://open-pdf/library/items/ELV3M9SP?page=24)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=142)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=143)
