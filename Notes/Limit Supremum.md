---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!info] Definition 1 ([[Limit]] [[Supremum]])[^1]
> For a [[Sequence]] $(s_n)$, we have
> $$
> \begin{align}
> \lim \sup(s_n) = \lim_{N \rightarrow \infty} \sup\{s_n | n > N\} = \sup S
> \end{align}
> $$
> where $S$ is the [[Set]] of [[Subsequential Limit]] of $(s_n)$.
> If $(s_n)$ is not bounded above, then $\sup\{s_n | n > N\} = +\infty$ and $\lim \sup(s_n) = +\infty$.
> In general, $\lim \sup(s_n) \leq \sup\{s_n | n > N\}$

Largest value infinitely often approached.

# Properties
- [[Limit of Sequence With Limit Supremum And Limit Infimum]]
- [[Limit Supremum of Product of Sequences]]
- [[Limit Supremum and Infimum Inequality]]

> [!abstract] Theorem (Monotonicity under Termwise Inequality)[^2]
> Let $(s_n), (t_n)$ be sequences of real numbers with $s_n \leq t_n$ for all $n \geq N$, for some fixed $N$. Then $\limsup s_n \leq \limsup t_n$ (and likewise $\liminf s_n \leq \liminf t_n$, see [[Limit Infimum]]).

[^1]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=72)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=66)