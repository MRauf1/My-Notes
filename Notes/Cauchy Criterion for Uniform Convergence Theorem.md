---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!abstract] Theorem 1 ([[Sequence of Function Uniformly Cauchy|Cauchy]] Criterion for [[Sequence of Function Uniform Convergence|Uniform Convergence]] Theorem)[^1]
> A [[Sequence of Function]] $(f_n)$ is defined and [[Sequence of Function Uniformly Cauchy]] on [[Set]] $S \subseteq \mathbb{R}$ if and only if $(f_n)$ converges uniformly on $S$ to some [[Function]] $f$ on $S$.

> [!abstract] Theorem 2 ([[Infinite Series]] Version)[^2]
> [[Infinite Series of Functions]] $\sum_{k=0}^{\infty} g_k$ is defined and [[Sequence of Function Uniformly Cauchy|uniformly cauchy]] on [[Set]] $S \subseteq \mathbb{R}$ if and only if $\sum_{k=0}^{\infty} g_k$ converges uniformly on $S$ to some [[Function]] $g$ on $S$.

> [!abstract] Theorem 3 (General Version)[^3]
> The [[Sequence of Function]] $\{f_n\}$, defined on a [[Set]] $E$, converges uniformly on $E$ if and only if for every $\epsilon > 0$ there exists an integer $N$ such that $m \geq N$, $n \geq N$, $x \in E$ implies
> $$
> \begin{align}
> |f_n(x) - f_m(x)| \leq \epsilon
> \end{align}
> $$

Theorem 3 holds for complex-valued functions on an arbitrary set $E$, not only $E \subseteq \mathbb{R}$. It is equivalent to the completeness of the [[Space of Bounded Continuous Functions]] under the [[Supremum Norm]].

# Properties
## [[Corollary]]
- [[Weierstrass M-Test]]

[^1]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=212)
[^2]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=215)
[^3]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=156&annotation=B64TLHIB)
