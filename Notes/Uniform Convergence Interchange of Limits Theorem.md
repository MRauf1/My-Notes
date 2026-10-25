---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!abstract] Theorem 1 ([[Sequence of Function Uniform Convergence|Uniform Convergence]] Interchange of Limits Theorem)[^1]
> Suppose $f_n \rightarrow f$ uniformly on a [[Set]] $E$ in a [[Metric Space]]. Let $x$ be a [[Limit Point]] of $E$, and suppose that
> $$
> \begin{align}
> \lim_{t \rightarrow x} f_n(t) = A_n \quad (n = 1, 2, 3, \dots)
> \end{align}
> $$
> Then $\{A_n\}$ converges, and
> $$
> \begin{align}
> \lim_{t \rightarrow x} f(t) = \lim_{n \rightarrow \infty} A_n
> \end{align}
> $$
> In other words,
> $$
> \begin{align}
> \lim_{t \rightarrow x} \lim_{n \rightarrow \infty} f_n(t) = \lim_{n \rightarrow \infty} \lim_{t \rightarrow x} f_n(t)
> \end{align}
> $$

Limit processes cannot in general be interchanged without affecting the result; uniform convergence is a sufficient condition for the interchange.[^2]

Asking whether the limit of a [[Sequence of Function]] of [[Continuous Function|continuous functions]] is continuous at a limit point $x$ is the same as asking whether $\lim_{t \to x} \lim_{n \to \infty} f_n(t) = \lim_{n \to \infty} \lim_{t \to x} f_n(t)$, since continuity of $f$ at $x$ means $\lim_{t \to x} f(t) = f(x)$.[^3]

# Properties
## [[Corollary]]
- [[Uniform Limit of Continuous Functions Theorem]]

## Related
- [[Uniform Limit of Integrals Theorem]] (interchange of limit and integral)
- [[Uniform Limit of Derivatives Theorem]] (interchange of limit and derivative)

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=158&annotation=AK9BS5G2)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=153&annotation=RP7SW7VE)
[^3]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=153&annotation=EBRWAB2W)
