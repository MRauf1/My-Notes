---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Conditional PMF[^1]
> Let $X_1, X_2$ be discrete with joint pmf $p_{X_1, X_2}$ and [[Marginal Distribution|marginal pmfs]] $p_{X_1}, p_{X_2}$. For $x_1$ in the [[Random Variable Support|support]] of $X_1$ (so $p_{X_1}(x_1) > 0$), the conditional pmf of $X_2$ given $X_1 = x_1$ is
> $$
> \begin{align}
> p_{X_2 | X_1}(x_2 | x_1) = P(X_2 = x_2 | X_1 = x_1) = \frac{p_{X_1, X_2}(x_1, x_2)}{p_{X_1}(x_1)}, \quad x_2 \in \mathcal{S}_{X_2}
> \end{align}
> $$

> [!info] Conditional PDF[^1]
> Let $X_1, X_2$ be continuous with joint pdf $f_{X_1, X_2}$ and marginal pdfs $f_{X_1}, f_{X_2}$. For any fixed $x_1$ with $f_{X_1}(x_1) > 0$, the conditional pdf of $X_2$ given $X_1 = x_1$ is
> $$
> \begin{align}
> f_{X_2 | X_1}(x_2 | x_1) = \frac{f_{X_1, X_2}(x_1, x_2)}{f_{X_1}(x_1)}
> \end{align}
> $$

> [!info] Joint Conditional PDF ($n$ Variables)[^2]
> For $X_1, \dots, X_n$ with joint pdf $f$ and $f_1(x_1) > 0$, the joint conditional pdf of $X_2, \dots, X_n$ given $X_1 = x_1$ is
> $$
> \begin{align}
> f_{2, \dots, n | 1}(x_2, \dots, x_n | x_1) = \frac{f(x_1, x_2, \dots, x_n)}{f_1(x_1)}
> \end{align}
> $$
> More generally, the joint conditional pdf of any $n - k$ of the variables given values of the remaining $k$ is the joint pdf of all $n$ divided by the [[Marginal Distribution|marginal]] pdf of the $k$ given variables, provided the latter is positive. Pmfs and sums replace pdfs and integrals in the discrete case.

The roles are symmetric: $p_{X_1 | X_2}(x_1 | x_2) = p_{X_1, X_2}(x_1, x_2) / p_{X_2}(x_2)$ and $f_{X_1 | X_2}(x_1 | x_2) = f_{X_1, X_2}(x_1, x_2) / f_{X_2}(x_2)$. Common abbreviations are $p_{2|1}(x_2 | x_1)$, $f_{1|2}(x_1 | x_2)$, with $p_1, p_2, f_1, f_2$ for the marginals.

The discrete definition is exactly [[Conditional Probability]] of the events $\{X_2 = x_2\}$ and $\{X_1 = x_1\}$. In the continuous case $P(X_1 = x_1) = 0$, so that formula cannot be applied; the conditional pdf is defined by analogy, as the joint density restricted to the slice $X_1 = x_1$ and renormalized by the slice's total mass $f_{X_1}(x_1)$.

# Properties
- For each fixed conditioning value, the conditional pmf or pdf is a genuine pmf or pdf in the other variable: it is nonnegative and
$$
\begin{align}
\sum_{x_2} p_{2|1}(x_2 | x_1) = \frac{1}{p_1(x_1)} \sum_{x_2} p_{1,2}(x_1, x_2) = \frac{p_1(x_1)}{p_1(x_1)} = 1, \qquad \int_{-\infty}^\infty f_{2|1}(x_2 | x_1)\,dx_2 = \frac{f_1(x_1)}{f_1(x_1)} = 1
\end{align}
$$
  so all univariate probability results apply to it.
- Conditional probabilities: $P(a < X_2 < b | X_1 = x_1) = \int_a^b f_{2|1}(x_2 | x_1)\,dx_2$, written $P(a < X_2 < b | x_1)$ when unambiguous; sums replace integrals in the discrete case.
- Its mean and variance are the [[Conditional Expectation]] and [[Conditional Variance]].
- Rearranged, it is the [[Conditional Probability Multiplication Rule]] for densities: $f_{1,2}(x_1, x_2) = f_1(x_1) f_{2|1}(x_2 | x_1)$; combined with the marginal this gives [[Bayes' Theorem]] for densities.
- $f_{2|1}(x_2 | x_1) = f_2(x_2)$ for all $x_1$ in the support if and only if $X_1, X_2$ are [[Independent Random Variable|independent]].
- Conditioning on a probability-zero event is not intrinsically defined: the value of $f_{2|1}(\cdot | x_1)$ at a single $x_1$ depends on which version of the densities is used, and different ways of approaching the event $\{X_1 = x_1\}$ can give different answers (Borel-Kolmogorov paradox). Measure-theoretically, conditional distributions are defined only for almost every $x_1$.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=125)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=152)
