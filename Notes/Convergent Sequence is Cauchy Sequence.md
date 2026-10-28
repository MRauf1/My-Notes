---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!abstract] Lemma 1
> [[Convergent Sequence]] are [[Cauchy Sequence]].[^1]

> [!abstract] Theorem 2 (General [[Metric Space]])[^2]
> In any [[Metric Space]] $(S, d)$, if $s_n \to s$, then $(s_n)$ is a [[Cauchy Sequence]]: given $\epsilon > 0$, choose $N$ with $d(s_n, s) < \epsilon/2$ for $n > N$, so that
> $$
> \begin{align}
> m, n > N \implies d(s_m, s_n) \leq d(s_m, s) + d(s, s_n) < \epsilon
> \end{align}
> $$

# Properties
- The converse (Cauchy $\implies$ convergent) fails in general: a Cauchy sequence may "want" to converge to a point that is missing from the space, e.g. rationals approximating $\sqrt{2}$ in $\mathbb{Q}$, or $1/n$ in the open interval $(0, 1)$.
- The converse holds precisely in a [[Complete Metric Space]], e.g. $\mathbb{R}$, [[Set of Complex Numbers|$\mathbb{C}$]], and $\mathbb{R}^k$; in these spaces, Cauchy $\iff$ convergent.[^2]

[^1]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=75)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=62)
