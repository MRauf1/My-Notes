---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!abstract] Theorem 1 ([[Infinite Series]] Ratio Test)[^1]
> Let [[Infinite Series]] $\sum a_n$ be made of non-zero terms
> 1) It is [[Absolutely Convergent Infinite Series]] if $\lim \sup |\frac{a_{n+1}}{a_n}| < 1$
> 2) It diverges if $\lim \inf |\frac{a_{n+1}}{a_n}| > 1$
> 3) Otherwise $\lim \inf |\frac{a_{n+1}}{a_n}| \leq 1 \leq \lim \sup |\frac{a_{n+1}}{a_n}|$ and the test gives no information

Worse test than the [[Infinite Series Root Test]] in that, if the root test gives no information, then the ratio test won't give information either. But the converse is not generally true — see [[Limit Supremum and Infimum Inequality]].

> [!abstract] Theorem 2 (Stronger Pointwise Divergence Criterion)[^2]
> Let $\sum a_n$ be an [[Infinite Series]] with $a_n \neq 0$ for all $n \geq n_0$, for some fixed $n_0$. If $\left| \frac{a_{n+1}}{a_n} \right| \geq 1$ for all $n \geq n_0$, then $\sum a_n$ diverges.

This is strictly stronger for proving divergence than concluding it from $\liminf |a_{n+1}/a_n| > 1$ alone. For example, if the ratio equals $1 + \frac{1}{n}$ for every $n$, it is always $\geq 1$, so Theorem 2 concludes divergence (since $|a_n|$ is then non-decreasing and cannot tend to $0$); yet $\liminf |a_{n+1}/a_n| = 1$ exactly, which Theorem 1's liminf/limsup-based criterion alone would leave inconclusive.

# Properties
- [[Limit Supremum and Infimum Inequality]]

[^1]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=111)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=76)