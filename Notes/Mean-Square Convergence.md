---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Mean-Square ($L^2$) Convergence[^1]
> An infinite series $\sum_{n=1}^\infty f_n(x)$ converges to $f(x)$ in the mean-square (or $L^2$) sense in $(a, b)$ if
> $$
> \begin{align}
> \int_a^b \left| f(x) - \sum_{n=1}^N f_n(x) \right|^2 dx \to 0 \quad \text{as } N \to \infty,
> \end{align}
> $$
> i.e. the partial sums converge to $f$ in the [[L2 Norm|$L^2$ metric]]. The integral replaces the maximum of uniform convergence.

# Types
Modes of convergence of a series on $(a, b)$, with $S_N = \sum_{n \le N} f_n$:[^2][^3]
- Pointwise: $|f(x) - S_N(x)| \to 0$ for each $a < x < b$ ([[Sequence of Function Pointwise Convergence]]).
- Uniform: $\max_{a \le x \le b} |f(x) - S_N(x)| \to 0$, endpoints included ([[Sequence of Function Uniform Convergence]]).
- Mean-square: as above.

# Properties
- Uniform convergence is stronger than both pointwise and $L^2$ convergence (on a bounded interval, $\int_a^b |f - S_N|^2 \le (b - a)\max|f - S_N|^2$).[^4]
- Pointwise and $L^2$ convergence are independent: neither implies the other in general (tall thin spikes converge pointwise to $0$ but not in $L^2$; a "typewriter" sequence of moving bumps converges in $L^2$ but at no point).[^5]
- The natural mode for Fourier series: every square-integrable function's [[Eigenfunction Expansion]] converges in this sense ([[Fourier Series L2 Convergence Theorem]]), and it is equivalent to [[Parseval's Theorem|Parseval's equality]].

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=138&annotation=ZNVHZCUA)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=137&annotation=WGTGH6B9); [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=138&annotation=6ICIIXR7)
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=138&annotation=92NA4RY4)
[^4]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=138&annotation=GSRIH2ZP)
[^5]: Added from general knowledge.
