---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!abstract] Theorem 1 (Dominated Convergence Theorem)[^1]
> Suppose $(f_n)$ is a [[Sequence]] of [[Riemann Integrable Function]] on $[a, b]$ and $f_n$ [[Sequence of Function Pointwise Convergence|converge pointwise]] to $f$ where $f$ is [[Riemann Integrable Function]] on $[a, b]$. If there exists $M > 0$ such that $|f_n(x)| \leq M$ for all $n$ and all $x \in [a, b]$, then
> $$
> \begin{align}
> \lim_{n \rightarrow \infty} \int_a^b f_n(x) dx = \int_a^b \lim_{n \rightarrow \infty} f_n(x) dx
> \end{align}
> $$

> [!abstract] Theorem 2 (Improper Riemann Integral Version)[^2]
> Suppose $g$ and $f_n$ ($n = 1, 2, 3, \dots$) are defined on $(0, \infty)$, are Riemann-integrable on $[t, T]$ whenever $0 < t < T < \infty$, $|f_n| \leq g$, $f_n \rightarrow f$ [[Sequence of Function Uniform Convergence|uniformly]] on every compact subset of $(0, \infty)$, and $\int_0^\infty g(x)\,dx < \infty$. Then
> $$
> \begin{align}
> \lim_{n \rightarrow \infty} \int_0^\infty f_n(x)\,dx = \int_0^\infty f(x)\,dx
> \end{align}
> $$

Theorem 2 is a weak form of Lebesgue's dominated convergence theorem for the [[Lebesgue Integral (Measure Theory)|Lebesgue integral]]. Even for the Riemann integral, uniform convergence can be replaced by pointwise convergence if the limit $f$ is assumed Riemann-integrable (Cunningham 1967; Kestelman 1970).[^2]

# Properties
- Strengthens the [[Uniform Limit of Integrals Theorem]] by replacing uniform convergence with domination.
- Its hypothesis, applied to a difference quotient, is what licenses the [[Interchange of Differentiation and Expectation]].

[^1]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=297)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=176&annotation=JXH3FH9A)
