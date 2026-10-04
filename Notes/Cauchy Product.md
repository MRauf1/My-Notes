---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!info] Definition 1 (Cauchy Product of Two Series)[^1]
> Given two [[Infinite Series]] $\sum_{n=0}^\infty a_n$ and $\sum_{n=0}^\infty b_n$ of complex numbers, put
> $$
> \begin{align}
> c_n = \sum_{k=0}^n a_k b_{n-k}, \qquad n = 0, 1, 2, \dots
> \end{align}
> $$
> The series $\sum_{n=0}^\infty c_n$ is called the Cauchy product of the two given series.

Motivated by formally multiplying two [[Power Series]] $\sum a_n z^n$ and $\sum b_n z^n$ term by term and collecting the terms with the same power of $z$; setting $z = 1$ recovers the definition above. [[Multiplication of Power Series]] is the specialization of this notion to two power series sharing a positive radius of convergence.

# Properties
- [[Mertens' Theorem]]

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=83)
