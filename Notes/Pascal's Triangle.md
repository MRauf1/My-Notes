---
tags:
  - mathematics
  - pre_calculus
  - discrete_mathematics
---

# Definition

> [!info] Definition 1 (Pascal's Triangle)[^1]
> The triangular array whose row $n$ ($n = 0, 1, 2, \dots$) lists the binomial coefficients ([[Combination]])
> $$
> \begin{align}
> \binom{n}{0}, \binom{n}{1}, \dots, \binom{n}{n}
> \end{align}
> $$
> Each row begins and ends with $1$, and each interior entry is the sum of the two entries above it, by [[Pascal's Identity]] $\binom{n}{j} + \binom{n}{j+1} = \binom{n+1}{j+1}$.

# Properties
- Row $n$ gives the coefficients of $(a + b)^n$ in the [[Binomial Theorem]], so a binomial can be expanded without computing factorials.
- Rows are symmetric, $\binom{n}{j} = \binom{n}{n-j}$, and row $n$ sums to $2^n$ (set $a = b = 1$ in the [[Binomial Theorem]]).
- Generating row $n$ from row $n-1$ is convolution with $[1, 1]$, the recursion behind the [[Binomial Filter]].

[^1]: [szprecalculus07042013.pdf](zotero://open-pdf/library/items/J3667KH4?page=700)
