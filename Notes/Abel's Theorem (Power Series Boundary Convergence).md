---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!abstract] Theorem 1 (Abel's Theorem — Power Series Boundary Convergence)[^1]
> Let $\sum_{n=0}^\infty c_n z^n$ be a [[Power Series]] with radius of convergence $1$, and suppose $c_0 \geq c_1 \geq c_2 \geq \dots \geq 0$ with $\lim_{n \to \infty} c_n = 0$. Then $\sum c_n z^n$ converges at every point $z$ on the circle $|z| = 1$, except possibly at $z = 1$.

Proved via the [[Dirichlet Test]], taking $a_n = z^n$ (whose partial sums are bounded for $|z| = 1$, $z \neq 1$, since they form a finite geometric sum) and $b_n = c_n$.

Not to be confused with [[Abel's Theorem]] (which concerns continuity of a power series at an endpoint of its interval of convergence, once convergence there is already known) — the two results share a name and both concern boundary behavior of power series, but are logically distinct.

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=81)
