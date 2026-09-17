---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!info] Definition 1 (Multilinear Function)[^1]
> A function $D: M_n(\mathbb{F}) \to \mathbb{F}$ is multilinear if, writing $A$ by its columns $a_1, \dots, a_n \in \mathbb{F}^n$, $D(A)$ is linear as a function of each column $a_j$ separately, with the other columns held fixed: for every $a_1, \dots, a_n, b_j \in \mathbb{F}^n$, $c \in \mathbb{F}$, and $j = 1, \dots, n$,
> $$
> D(a_1, \dots, a_j + b_j, \dots, a_n) = D(a_1, \dots, a_j, \dots, a_n) + D(a_1, \dots, b_j, \dots, a_n)
> $$
> $$
> D(a_1, \dots, ca_j, \dots, a_n) = c \, D(a_1, \dots, a_j, \dots, a_n)
> $$

# Properties
- [[Alternating Multilinear Function]]
- [[Isoscopic Function]]
- [[Determinant]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=354)
