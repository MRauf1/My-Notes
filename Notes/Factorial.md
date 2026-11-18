---
tags:
  - mathematics
  - pre_calculus
  - discrete_mathematics
---

# Definition

> [!info] Definition 1 (Factorial)[^1]
> For a [[Whole Number]] $n$, $n$ factorial, $n!$, is the term $f_n$ of the recursively defined [[Sequence]]
> $$
> \begin{align}
> f_0 = 1, \qquad f_n = n \cdot f_{n-1}, \quad n \geq 1
> \end{align}
> $$
> Informally, $n! = n (n-1) (n-2) \cdots 2 \cdot 1$, with $0! = 1$.

# Properties
- Recursive property: $n! = n\,(n-1)!$ for $n \geq 1$, which simplifies quotients such as $\frac{(n+1)!}{n!} = n + 1$.
- $n!$ counts the orderings of $n$ distinct objects ([[Permutation (Combinatorics)]]), and appears in the binomial coefficient $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ ([[Combination]]).
- Extended to non-integer arguments by the [[Gamma Function]]: $\Gamma(n+1) = n!$.
- Grows faster than any exponential $c^n$ (eventually), e.g. $n! > 3^n$ for $n \geq 7$, provable by [[Proof by Induction]].

[^1]: [szprecalculus07042013.pdf](zotero://open-pdf/library/items/J3667KH4?page=693)
