---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!abstract] Theorem 1 ([[Limit Supremum]] and [[Limit Infimum]] [[Inequality]])[^1]
> Let $(s_n)$ be any [[Sequence]] of non-zero [[Real Number]],
> $$
> \begin{align}
> \lim \inf |\frac{s_{n+1}}{s_n}| \leq \lim \inf |s_n|^{1/n} \leq \lim \sup |s_n|^{1/n} \leq \lim \sup |\frac{s_{n+1}}{s_n}|
> \end{align}
> $$
> $\lim|\frac{s_{n+1}}{s_n}| = L \implies \lim |s_n|^{1/n} = L$ (not iff: the ratio limit existing is a stronger condition, the root limit can exist without it, e.g. an interleaved sequence).

This is exactly why the [[Infinite Series Root Test|root test]] is never weaker than the [[Infinite Series Ratio Test|ratio test]]: whenever $\limsup |a_{n+1}/a_n| < 1$ (ratio test shows convergence), $\limsup |a_n|^{1/n}$ is at most that same value, so the root test shows convergence too; whenever the root test is inconclusive ($\limsup |a_n|^{1/n} = 1$), the chain forces $\limsup |a_{n+1}/a_n| \geq 1$, so the ratio test is inconclusive as well.

[^1]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=91)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=77)