---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!abstract] Theorem 1 (Weierstrass Approximation Theorem)[^1]
> If $f$ is a [[Continuous Function|continuous]] complex function on $[a, b]$, there exists a [[Sequence]] of [[Polynomial|polynomials]] $P_n$ such that
> $$
> \begin{align}
> \lim_{n \rightarrow \infty} P_n(x) = f(x)
> \end{align}
> $$
> [[Sequence of Function Uniform Convergence|uniformly]] on $[a, b]$. If $f$ is real, the $P_n$ may be taken real.

Equivalently, the set of continuous functions on $[a, b]$ is the uniform closure of the set of polynomials on $[a, b]$ ([[Algebra of Functions]]); i.e., polynomials are [[Dense Subset|dense]] in $\mathscr{C}([a, b])$ ([[Space of Bounded Continuous Functions]]).[^2]

> [!abstract] Corollary 2[^3]
> For every interval $[-a, a]$ there is a sequence of real polynomials $P_n$ such that $P_n(0) = 0$ and
> $$
> \begin{align}
> \lim_{n \rightarrow \infty} P_n(x) = |x|
> \end{align}
> $$
> uniformly on $[-a, a]$.

Corollary 2 is the key lemma in the proof of the [[Stone-Weierstrass Theorem]]: it lets a uniformly closed algebra contain $|f|$, hence $\max(f, g)$ and $\min(f, g)$, whenever it contains $f, g$.

# Properties
- Generalized by the [[Stone-Weierstrass Theorem]].

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=168&annotation=TZIQ3YAQ)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=170&annotation=HB5K9JEK)
[^3]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=170&annotation=T4F6D28T)
