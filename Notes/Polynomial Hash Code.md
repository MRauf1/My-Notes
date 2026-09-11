---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Polynomial Hash Code
> A [[Hash Code]] construction for sequences of variable length (e.g. strings or arrays) that evaluates a polynomial modulo a prime, rather than the fixed-arity multiplicative combination used for objects with a constant number of components.[^1]

This rests on the fact that polynomials over prime fields behave essentially like ordinary polynomials:

> [!abstract] Theorem 5.4[^2]
> Let $p$ be a prime number, and let $f(z) = x_0 z^0 + x_1 z^1 + \cdots + x_{r-1} z^{r-1}$ be a non-trivial polynomial with coefficients $x_i \in \{0, \dots, p-1\}$. Then the equation $f(z) \bmod p = 0$ has at most $r - 1$ solutions for $z \in \{0, \dots, p-1\}$.

A sequence of integers $x_0, \dots, x_{r-1}$, each in $\{0, \dots, p-2\}$, is hashed using a random integer $z \in \{0, \dots, p-1\}$ via $$h(x_0, \dots, x_{r-1}) = \left(x_0 z^0 + \cdots + x_{r-1} z^{r-1} + (p-1) z^r\right) \bmod p.$$ The extra $(p-1)z^r$ term acts as an end-of-sequence marker: treating $p-1$ as an implicit final element $x_r$ that cannot occur elsewhere in the sequence (since every other $x_i \in \{0, \dots, p-2\}$) lets this formula distinguish a sequence from any of its proper prefixes, since it effectively hashes the infinite sequence $x_0, \dots, x_{r-1}, p-1, 0, 0, \dots$; two sequences of different lengths $r > r'$, one a prefix of the other, are therefore guaranteed to first differ at index $i = r'$.[^3]

# Properties
> [!abstract] Theorem 5.5[^4]
> Let $p > 2^w + 1$ be a prime, and let $x_0, \dots, x_{r-1}$ and $y_0, \dots, y_{r-1}$ each be sequences of $w$-bit integers in $\{0, \dots, 2^w - 1\}$ with $x_i \neq y_i$ for at least one index $i \in \{0, \dots, r-1\}$. Then $\Pr\{h(x_0, \dots, x_{r-1}) = h(y_0, \dots, y_{r-1})\} \leq (r-1)/p$.

> [!abstract] Theorem 5.6[^5]
> Let $p > 2^w + 1$ be a prime, and let $x_0, \dots, x_{r-1}$ and $y_0, \dots, y_{r'-1}$ be distinct sequences of $w$-bit integers in $\{0, \dots, 2^w - 1\}$. Then $\Pr\{h(x_0, \dots, x_{r-1}) = h(y_0, \dots, y_{r'-1})\} \leq \max\{r, r'\}/p$.

[^1]: [Morin, p. 120](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 120](zotero://select/library/items/HYS8NDAB)
[^3]: [Morin, p. 120](zotero://select/library/items/HYS8NDAB)
[^4]: [Morin, p. 120](zotero://select/library/items/HYS8NDAB)
[^5]: [Morin, p. 121](zotero://select/library/items/HYS8NDAB)
