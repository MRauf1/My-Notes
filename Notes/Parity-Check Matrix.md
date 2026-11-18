---
tags:
  - mathematics
  - linear_algebra
---

# Definition

> [!info] Definition 1 (Parity-Check Matrix)[^1]
> A parity-check matrix for a [[Linear Code|linear encoding]] with encoding matrix $A \in M_{n,k}(\mathbb{F}_2)$ is a matrix $B \in M_{m,n}(\mathbb{F}_2)$ with
> $$
> \begin{align}
> \ker B = C(A)
> \end{align}
> $$
> ([[Kernel Vector Subspace|kernel]], [[Matrix Column Space|column space]]). A received word $z$ is a codeword iff $Bz = 0$.

> [!abstract] Proposition 2 (Error Detection)[^1]
> If a linear encoding has a parity-check matrix whose columns are all nonzero, the encoding is error-detecting: if exactly one bit is flipped, $z = y + e_i$, then $Bz = Be_i = b_i \neq 0$.

# Properties
- If the columns of $B$ are also distinct, the encoding is error-correcting for single errors: $Bz = b_i$ identifies the flipped position $i$. The Hamming code takes the columns of $B \in M_{3,7}(\mathbb{F}_2)$ to be all seven nonzero vectors of $\mathbb{F}_2^3$.
- $BA = 0$, since $C(A) \subseteq \ker B$; by the [[Rank-Nullity Theorem]], $\operatorname{rank} B = n - k$ when $B$ has $n - k$ rows.

# Questions
> [!question]- Why do distinct nonzero columns of $B$ make single-bit errors correctable?
> If $y$ is a codeword and $z = y + e_i$, then $Bz = By + Be_i = 0 + b_i = b_i$. Nonzero columns make $Bz \neq 0$, so the error is detected. Distinct columns mean $b_i$ determines $i$ uniquely, so Bob flips bit $i$ back to recover $y$, then solves $Ax = y$ (unique since $\ker A = 0$).

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=151)
