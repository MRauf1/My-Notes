---
tags:
  - mathematics
  - pre_calculus
---

# Definition

> [!info] Definition 1 ($n$th Root of a Complex Number)[^1]
> For [[Complex Number|complex numbers]] $z, w$ and a natural number $n$, $w$ is an $n$th root of $z$ if $w^n = z$. No principal root is singled out.

> [!abstract] Theorem 2 (The $n$th Roots of a Complex Number)[^2]
> Let $z \neq 0$ have polar form $z = r\,\mathrm{cis}(\theta)$ ([[Complex Number in Polar Coordinates]]). Then $z$ has exactly $n$ distinct $n$th roots
> $$
> \begin{align}
> w_k = \sqrt[n]{r}\ \mathrm{cis}\!\left(\frac{\theta}{n} + \frac{2\pi}{n}k\right), \qquad k = 0, 1, \dots, n - 1
> \end{align}
> $$
> where $\sqrt[n]{r}$ is the real [[Nth Root]] of $r > 0$.

# Properties
- The roots lie on the circle of radius $\sqrt[n]{r}$ and form the vertices of a regular $n$-gon.
- For $z = 1$ these are the $n$th roots of unity $\mathrm{cis}(2\pi k / n)$.

# Questions
> [!question]- What is the proof idea of the $n$th-root formula?
> Existence: by [[De Moivre's Formula]], $w_k^n = r\,\mathrm{cis}(\theta + 2\pi k) = r\,\mathrm{cis}(\theta) = z$, since $\mathrm{cis}$ is $2\pi$-periodic. Distinctness: for $0 \leq j < k \leq n-1$ the arguments differ by $\frac{2\pi(k-j)}{n} \in (0, 2\pi)$, not a multiple of $2\pi$, so $w_j \neq w_k$. There are no others: $w^n = z$ is a degree-$n$ polynomial equation, which has at most $n$ roots ([[Fundamental Theorem of Algebra]] / [[Factor Theorem]]).

[^1]: [szprecalculus07042013.pdf](zotero://open-pdf/library/items/J3667KH4?page=1012)
[^2]: [szprecalculus07042013.pdf](zotero://open-pdf/library/items/J3667KH4?page=1013)
