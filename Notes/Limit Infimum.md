---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!info] Definition 1 ([[Limit]] [[Infimum]])[^1]
> For a [[Sequence]] $(s_n)$, we have
> $$
> \begin{align}
> \lim \inf(s_n) = \lim_{N \rightarrow \infty} \inf\{s_n | n > N\} = \inf S
> \end{align}
> $$
> where $S$ is the [[Set]] of [[Subsequential Limit]] of $(s_n)$.
> If $(s_n)$ is not bounded below, then $\inf\{s_n | n > N\} = -\infty$ and $\lim \inf(s_n) = -\infty$.
> In general, $\lim \inf(s_n) \geq \inf\{s_n | n > N\}$ for any fixed $N$, since $\inf\{s_n | n > N\}$ is non-decreasing in $N$.

Smallest value infinitely often approached.

> [!info] Definition 2 (Sup-Inf Form)[^2]
> Every sequence $\{x_n\}$ in $\mathbb{R}$ has a limit inferior in the [[Extended Real Number Set]]:
> $$
> \begin{align}
> \liminf_{n \to \infty} x_n = \sup_{k \geq 1} \left( \inf_{n \geq k} x_n \right)
> \end{align}
> $$
> $\{x_n\}$ converges in $\mathbb{R}$ if and only if $\liminf x_n = \limsup x_n$ and this value is finite, in which case the limit is that common value.

The set analogue is [[Limit Superior and Limit Inferior of Sets]].

# Properties
- [[Limit of Sequence With Limit Supremum And Limit Infimum]]
- [[Limit Supremum and Infimum Inequality]]
- Monotonicity under termwise inequality: if $s_n \leq t_n$ for all $n \geq N$ (some fixed $N$), then $\liminf s_n \leq \liminf t_n$ — see [[Limit Supremum]].

[^1]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=72)

[^2]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=24&annotation=A2LD3Y7R)
