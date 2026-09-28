---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Linear Conditional Expectation Theorem[^1]
> Suppose $(X, Y)$ has a joint distribution with finite, positive variances. Denote the means and variances by $\mu_1, \mu_2$ and $\sigma_1^2, \sigma_2^2$, and let $\rho$ be the [[Correlation|correlation coefficient]]. If the [[Conditional Expectation]] $E(Y | X)$ is linear in $X$, then
> $$
> \begin{align}
> E(Y | X) &= \mu_2 + \rho \frac{\sigma_2}{\sigma_1}(X - \mu_1) \\
> E[\text{Var}(Y | X)] &= \sigma_2^2 (1 - \rho^2)
> \end{align}
> $$
> Symmetrically, if $E(X | Y)$ is linear, $E(X | Y) = \mu_1 + \rho \frac{\sigma_1}{\sigma_2}(Y - \mu_2)$ and $E[\text{Var}(X | Y)] = \sigma_1^2 (1 - \rho^2)$.

Writing $E(Y | x) = a + bx$, the [[Law of Total Expectation]] gives $\mu_2 = a + b\mu_1$, and taking expectations of $X \cdot E(Y | X)$ gives $E(XY) = a\mu_1 + b E(X^2)$; solving yields $b = \rho\sigma_2/\sigma_1$. The second formula then follows from the [[Law of Total Variance]], since $\text{Var}[E(Y | X)] = b^2\sigma_1^2 = \rho^2\sigma_2^2$.

This answers when $\rho$ describes a band of concentration: the probability for $(X, Y)$ clusters around the line $y = \mu_2 + \rho\frac{\sigma_2}{\sigma_1}(x - \mu_1)$, and the average squared spread about it is $\sigma_2^2(1 - \rho^2)$. So $\rho^2$ is the fraction of $\text{Var}(Y)$ explained by $X$, and $1 - \rho^2$ the fraction left over.

# Properties
- Since $E[\text{Var}(Y | X)] \geq 0$, the theorem gives $\rho^2 \leq 1$, verifying the correlation bound in the linear case.
- Corollary (constant conditional variance): if $\text{Var}(Y | x) = k > 0$ does not depend on $x$, then $k = \sigma_2^2(1 - \rho^2)$ for every $x$. With $\rho = 0$ each conditional distribution has the full marginal variance $\sigma_2^2$; with $\rho^2$ near $1$ each is tightly concentrated near its mean $\mu_2 + \rho\frac{\sigma_2}{\sigma_1}(x - \mu_1)$.
- Even when $E(Y | X)$ is not linear, the same line $\mu_2 + \rho\frac{\sigma_2}{\sigma_1}(X - \mu_1)$ is the best linear predictor of $Y$ (it minimizes $E[(Y - a - bX)^2]$), with mean squared error $\sigma_2^2(1 - \rho^2)$; linearity is what makes it equal to the conditional mean. This is the population version of the [[Simple Linear Regression]] line.
- The hypothesis holds for the bivariate normal distribution, where in addition $\text{Var}(Y | x)$ is constant.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=144)
