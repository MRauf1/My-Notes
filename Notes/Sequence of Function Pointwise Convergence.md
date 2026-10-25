---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!info] Definition 1 ([[Sequence of Function]] Pointwise [[Convergence]])[^1]
> Let $(f_n)$ be a [[Sequence]] of [[Real-Valued Function]] defined on the [[Set]] $S \subseteq R$. The sequence $(f_n)$ converges pointwise (i.e., at each point) to a function $f$ defined on $S$ if $\lim_{n \rightarrow \infty} f_n(x) = f(x)$ for all $x \in S$.
> Alternatively, it means that for each $\epsilon > 0$ and for each $x \in S$, there exists $N(x, \epsilon)$ such
> $$
> \begin{align}
> n > N \implies |f_n(x) - f(x)| < \epsilon
> \end{align}
> $$

Value of $N$ depends on both $\epsilon > 0$ and $x \in S$.

As such, points may converge at different rates to their limits, which can create [[Discontinuity]].

> [!info] Definition 2 (General Version)[^2][^3]
> Suppose $\{f_n\}$ is a [[Sequence of Function]] defined on a [[Set]] $E$, and suppose that $\{f_n(x)\}$ converges for every $x \in E$. Then $\{f_n\}$ converges (pointwise) on $E$ to the limit function
> $$
> \begin{align}
> f(x) = \lim_{n \rightarrow \infty} f_n(x) \quad (x \in E)
> \end{align}
> $$
> Similarly, if $\sum f_n(x)$ converges for every $x \in E$, the function $f(x) = \sum_{n=1}^{\infty} f_n(x)$ is called the sum of the series $\sum f_n$.

The main problem is whether properties of the $f_n$ (continuity, differentiability, integrability) are preserved by the limit $f$, and how $f_n'$ relates to $f'$ and $\int f_n$ to $\int f$.[^4] Continuity of the limit at a limit point $x$ is the question of whether $\lim_{t \to x} \lim_{n \to \infty} f_n(t) = \lim_{n \to \infty} \lim_{t \to x} f_n(t)$, i.e., whether two limit processes can be interchanged; under pointwise convergence alone they generally cannot.[^5]

# Properties
- [[Sequence of Function Uniform Convergence]] is a sufficient condition for interchanging limits ([[Uniform Convergence Interchange of Limits Theorem]]).
- [[Dini's Theorem]]: monotone pointwise convergence of continuous functions to a continuous limit on a compact set is uniform.
- On a [[Compact Set]], pointwise convergence of an [[Equicontinuity|equicontinuous]] sequence is uniform.

[^1]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=203)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=152&annotation=IGFCESF9)
[^3]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=153&annotation=K58GZKNS)
[^4]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=153&annotation=LZV3828U)
[^5]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=153&annotation=EBRWAB2W)
