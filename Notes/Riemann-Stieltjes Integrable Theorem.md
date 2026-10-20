---
tags:
  - mathematics
  - real_analysis
---

# Definition
> [!abstract] Theorem 1 (Integrability Criterion)[^1]
> Let $f$ be bounded and $\alpha$ monotonically increasing on $[a, b]$. Then $f \in \mathscr{R}(\alpha)$ on $[a, b]$ ([[Riemann-Stieltjes Integral]]) if and only if for every $\epsilon > 0$ there exists a [[Partition]] $P$ such that
> $$
> \begin{align}
> U(P, f, \alpha) - L(P, f, \alpha) < \epsilon
> \end{align}
> $$

> [!abstract] Theorem 2 (Consequences of the Criterion)[^2]
> Suppose $U(P, f, \alpha) - L(P, f, \alpha) < \epsilon$ for $P = \{x_0, \dots, x_n\}$.
> 1) The inequality holds (with the same $\epsilon$) for every [[Refinement of Partition|refinement]] of $P$.
> 2) If $s_i, t_i \in [x_{i-1}, x_i]$ are arbitrary, then $\sum_{i=1}^n |f(s_i) - f(t_i)| \Delta\alpha_i < \epsilon$.
> 3) If moreover $f \in \mathscr{R}(\alpha)$, then
> $$
> \begin{align}
> \left| \sum_{i=1}^n f(t_i) \Delta\alpha_i - \int_a^b f \, d\alpha \right| < \epsilon
> \end{align}
> $$

Part 3 says that Riemann-Stieltjes sums $\sum f(t_i)\Delta\alpha_i$ (generalizing the [[Riemann Sum]]) approximate the integral, regardless of the choice of tags $t_i$.

# Properties
- Special case $\alpha(x) = x$: [[Darboux Integrable Theorem]].
- Part 1 follows from [[Darboux Sums of 2 Partitions Lemma]]; part 2 since $f(s_i), f(t_i) \in [m_i, M_i]$ gives $|f(s_i) - f(t_i)| \leq M_i - m_i$.
- The main tool for proving [[Functions that are Riemann-Stieltjes Integrable Theorem]].

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=133&annotation=FFGF3FEB)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=134&annotation=K6H77GU8)
