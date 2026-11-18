---
tags:
  - mathematics
  - pre_calculus
---

# Definition

> [!abstract] Theorem 1 (Arithmetic Series)[^1]
> The sum of the first $n$ terms of an [[Arithmetic Sequence]] $a_k = a + (k - 1)d$, $k \geq 1$, is
> $$
> \begin{align}
> S = \sum_{k=1}^{n} a_k = n \, \frac{a_1 + a_n}{2} = \frac{n}{2}\big(2a + (n - 1)d\big)
> \end{align}
> $$

# Properties
- A [[Finite Series]]. The case $a = d = 1$ is the [[Linear Series]] $\sum_{i=1}^n i = \frac{n(n+1)}{2}$.
- $S$ is $n$ times the average of the first and last terms.
- Counterpart: [[Geometric Series]].

# Questions
> [!question]- What is the proof idea of the arithmetic series formula?
> Write $S$ forward and in reverse and add term by term. The $k$th pair is $a_k + a_{n+1-k} = \big(a + (k-1)d\big) + \big(a + (n-k)d\big) = 2a + (n-1)d = a_1 + a_n$, independent of $k$. So $2S = n(a_1 + a_n)$. Alternatively, by linearity, $S = na + d\sum_{k=1}^{n}(k-1) = na + d\,\frac{n(n-1)}{2}$ using the [[Linear Series]].

[^1]: [szprecalculus07042013.pdf](zotero://open-pdf/library/items/J3667KH4?page=678)
