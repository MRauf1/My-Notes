---
tags:
  - statistics
  - bayesian_statistics
  - mathematical_statistics
---

# Definition

> [!info] Definition 1 ([[Conditional Probability|Conditional]] [[Expectation]])
> For [[Random Variable]] $X, Y$, the expectation of $X$ given $Y = y$ is
> $$
> \begin{align}
> E[X | Y = y] &= \sum_{all\ x} x f(x | y)\ \text{(Discrete)} \\
> E[X | Y = y] &= \int_{all\ x} x f(x | y) dx\ \text{(Continuous)}
> \end{align}
> $$

> [!info] Definition 2 (Conditional Expectation of a Function)[^1]
> For a function $u(X_2)$, the conditional expectation of $u(X_2)$ given $X_1 = x_1$, if it exists, is
> $$
> \begin{align}
> E[u(X_2) | x_1] = \int_{-\infty}^\infty u(x_2)\, f_{2|1}(x_2 | x_1)\,dx_2
> \end{align}
> $$
> with a sum against $p_{2|1}(x_2 | x_1)$ in the discrete case, where $f_{2|1}$ is the [[Conditional Distribution|conditional pdf]]. With $u(x_2) = x_2$ this is the conditional mean $E(X_2 | x_1)$.

For $n$ variables,[^4] $E[u(X_2, \dots, X_n) | x_1] = \int \cdots \int u(x_2, \dots, x_n) f_{2, \dots, n|1}(x_2, \dots, x_n | x_1)\,dx_2 \cdots dx_n$, provided $f_1(x_1) > 0$ and the integral converges absolutely, using the joint [[Conditional Distribution|conditional pdf]]; $h(X_1) = E[u(X_2, \dots, X_n) | X_1]$ is again a random variable.

> [!info] Definition 3 (Conditional Expectation as a Random Variable)[^2]
> $E[u(X_2) | x_1]$ is a function of $x_1$, say $h(x_1)$. Substituting the random variable, $E[u(X_2) | X_1] = h(X_1)$ is a random variable with its own distribution, mean, and variance.

**Interpretation.** In $E[X_2 | X_1]$, only $X_1$ is random: $X_2$ has already been averaged out against the conditional distribution given $X_1$. So the expectation of this random variable, $E\big[E[X_2 | X_1]\big]$, is an integral over $x_1$ alone, against the marginal distribution of $X_1$:
$$
\begin{align}
E\big[E[X_2 | X_1]\big] = \int_{-\infty}^\infty E[X_2 | x_1]\, f_1(x_1)\,dx_1
\end{align}
$$
This is the [[Law of Total Expectation]]. Geometrically, $E[X_2 | X_1]$ is the best prediction of $X_2$ using only the information in $X_1$: it minimizes $E[(X_2 - g(X_1))^2]$ over all functions $g$, i.e. it is the orthogonal projection of $X_2$ onto the space of (square-integrable) functions of $X_1$.

# Properties
- Linearity: $E[a\,u(X_2) + b\,v(X_2) | X_1] = a\,E[u(X_2) | X_1] + b\,E[v(X_2) | X_1]$.
- Taking out what is known:[^3] a function of the conditioning variable acts as a constant, $E[u(X_2) | X_2] = u(X_2)$ and $E(X_1 + X_2 | X_2) = E(X_1 | X_2) + X_2$. More generally, $E[g(X_2)\,h(X_1, X_2) | X_2] = g(X_2)\,E[h(X_1, X_2) | X_2]$.
- [[Law of Total Expectation]]: $E[E(X_2 | X_1)] = E(X_2)$.
- [[Law of Total Variance]]: $\text{Var}[E(X_2 | X_1)] \leq \text{Var}(X_2)$.
- If $X_1, X_2$ are [[Independent Random Variable|independent]], $E[u(X_2) | X_1] = E[u(X_2)]$, a constant.
- If $E(X_2 | X_1)$ is linear in $X_1$, it equals $\mu_2 + \rho\frac{\sigma_2}{\sigma_1}(X_1 - \mu_1)$ ([[Linear Conditional Expectation Theorem]]).
- The spread of the conditional distribution around the conditional mean is the [[Conditional Variance]].

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=127)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=128)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=132)
[^4]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=153)
