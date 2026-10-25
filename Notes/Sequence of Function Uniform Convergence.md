---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!info] Definition 1 ([[Sequence of Function]] Uniform Convergence)[^1]
> Let $(f_n)$ be a [[Sequence]] of [[Real-Valued Function]] defined on the [[Set]] $S \subseteq R$. The sequence $(f_n)$ converges uniformly on $S$ to a function $f$ defined on $S$ if for each $\epsilon > 0$, there exists $N(\epsilon)$ such that
> $$
> \begin{align}
> (\forall x \in S \land n > N) \implies |f_n(x) - f(x)| < \epsilon
> \end{align}
> $$

Value of $N$ depends only on $\epsilon > 0$. Stronger condition than [[Sequence of Function Pointwise Convergence]].

Unlike pointwise convergence, the "gap" between $(f_n)$ and $f$ must shrink at the same rate across the entire [[Domain]].

> [!info] Definition 2 (Alternative Definition)[^2]
> [[Sequence of Function]] $(f_n)$ on [[Set]] $S \subseteq \mathbb{R}$ converges uniformly to [[Function]] $f$ on $S$ if and only if
> $$
> \begin{align}
> \lim_{n \rightarrow \infty} \sup\{|f_n(x) - f(x)| : x \in S\} = 0
> \end{align}
> $$

> [!info] Definition 3 (General Version)[^3]
> A [[Sequence of Function]] $\{f_n\}$ converges uniformly on a [[Set]] $E$ to a function $f$ if for every $\epsilon > 0$ there is an integer $N$ such that $n \geq N$ implies
> $$
> \begin{align}
> |f_n(x) - f(x)| \leq \epsilon \quad \text{for all } x \in E
> \end{align}
> $$
> The series $\sum f_n(x)$ converges uniformly on $E$ if the sequence of partial sums $s_n(x) = \sum_{i=1}^{n} f_i(x)$ converges uniformly on $E$.

For pointwise convergence, $N$ depends on $\epsilon$ and $x$; for uniform convergence, one $N$ works for all $x \in E$.[^3]

> [!abstract] Theorem 4 (Supremum Criterion)[^4]
> Suppose $\lim_{n \to \infty} f_n(x) = f(x)$ for $x \in E$. Put $M_n = \sup_{x \in E} |f_n(x) - f(x)|$. Then $f_n \rightarrow f$ uniformly on $E$ if and only if $M_n \rightarrow 0$ as $n \rightarrow \infty$.

Theorem 4 says that uniform convergence is exactly convergence in the [[Supremum Norm]] metric of the [[Space of Bounded Continuous Functions]].

# Types
- [[Sequence of Function Locally Uniform Convergence]]

# Properties
## Convergence
- Uniform convergence implies [[Sequence of Function Pointwise Convergence]]
- On a bounded interval, uniform convergence implies [[Mean-Square Convergence]]

- Uniform convergence does not imply [[Absolutely Convergent Infinite Series|absolute convergence]] of a series, and absolute convergence (even for all $x$) does not imply uniform convergence.[^5][^6]
- If $\{f_n\}$ and $\{g_n\}$ converge uniformly on $E$, then $\{f_n + g_n\}$ converges uniformly on $E$; if, in addition, they are sequences of [[Bounded Function|bounded functions]], then $\{f_n g_n\}$ converges uniformly on $E$.[^7]
- Every uniformly convergent sequence of [[Bounded Function|bounded functions]] is [[Sequence of Function Uniformly Bounded|uniformly bounded]].[^8]
- [[Cauchy Criterion for Uniform Convergence Theorem]]
- [[Weierstrass M-Test]]
- [[Uniform Convergence Interchange of Limits Theorem]]

## [[Continuity]]
- [[Dini's Theorem]] (partial converse)
- On a [[Compact Metric Space]], a uniformly convergent sequence in $\mathscr{C}(K)$ is [[Equicontinuity|equicontinuous]]; see [[Arzelà-Ascoli Theorem]].
- [[Uniform Limit of Continuous Functions Theorem]]

## [[Riemann Integral]]
- [[Uniform Limit of Integrals Theorem]]

## [[Derivative]]
- [[Uniform Limit of Derivatives Theorem]]
- [[Continuous Nowhere Differentiable Function Theorem]]

## Approximation
- [[Weierstrass Approximation Theorem]]
- [[Stone-Weierstrass Theorem]]

[^1]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=204)
[^2]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=207)
[^3]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=156&annotation=9ATTB3GX)
[^4]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=157&annotation=YGUVGM7A)
[^5]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=175&annotation=L84PHL5X)
[^6]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=175&annotation=ZI2NTQMX)
[^7]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=174&annotation=53LRR77R)
[^8]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=174&annotation=T3HJZSH7)
