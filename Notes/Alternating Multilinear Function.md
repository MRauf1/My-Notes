---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!info] Definition 1 (Alternating Multilinear Function)[^1]
> A [[Multilinear Function]] $D: M_n(\mathbb{F}) \to \mathbb{F}$ is alternating if, writing $A$ by its columns $a_1, \dots, a_n$, $D(A) = 0$ whenever there are $i \neq j$ with $a_i = a_j$.

An alternating multilinear function is exactly a [[Multilinear Function|multilinear]] function that is also [[Isoscopic Function|isoscopic]].

> [!abstract] Lemma 2 (Lemma 6.2 -- Column Swap Negates the Value)[^2]
> Suppose $D: M_n(\mathbb{F}) \to \mathbb{F}$ is alternating multilinear. Given $A \in M_n(\mathbb{F})$ and $1 \leq i < j \leq n$, let $B$ be the matrix obtained from $A$ by exchanging its $i$th and $j$th columns. Then $D(B) = -D(A)$.

# Properties
- [[Multilinear Function]]
- [[Isoscopic Function]]
- [[Determinant]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=355)
[^2]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=355)
