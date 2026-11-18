---
tags:
  - mathematics
  - linear_algebra
---

# Definition

> [!info] Definition 1 (Binary Linear Code)[^1]
> A binary linear code is a [[Vector Subspace|subspace]] $C \subseteq \mathbb{F}_2^n$. A linear encoding is a [[Bijective Function|bijective]] [[Linear Map]] $T: \mathbb{F}_2^k \to C$, equivalently an injective linear map $\mathbb{F}_2^k \to \mathbb{F}_2^n$ with [[Linear Map Image|range]] $T = C$.
>
> Its matrix $A \in M_{n,k}(\mathbb{F}_2)$ is the encoding matrix, with $\ker A = \{0\}$ and $C(A) = C$ ([[Matrix Column Space]]). Data $x \in \mathbb{F}_2^k$ is encoded as $y = Ax$.

# Properties
- Errors are detected and corrected using a [[Parity-Check Matrix]].
- Example: the Hamming code encodes $\mathbb{F}_2^4$ into $\mathbb{F}_2^7$ and corrects any single bit error.
- Arithmetic is in $\mathbb{F}_2$ ([[Modular Arithmetic]]), so a single bit error is $z = y + e_i$.

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=150)
