---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!info] Definition 1 (Permutation Matrix)[^1]
> Let $\sigma \in S_n$ be a [[Permutation]]. The permutation matrix $A_\sigma \in M_n(\mathbb{F})$ has entries
> $$
> (A_\sigma)_{ij} = \begin{cases} 1 & \text{if } \sigma(i) = j \\ 0 & \text{otherwise} \end{cases}
> $$

$A_\sigma$ is exactly the matrix of the [[Linear Map]] on $\mathbb{F}^n$ that permutes the coordinates of a vector according to $\sigma$.

> [!abstract] Theorem 2 (Homomorphism Property)[^2]
> $A_{\sigma_1 \circ \sigma_2} = A_{\sigma_1} A_{\sigma_2}$.

So $\sigma \mapsto A_\sigma$ is a [[Group Homomorphism]] from the [[Symmetric Group]] $S_n$ into $GL_n(\mathbb{F})$, giving $S_n$ a natural representation as $n \times n$ matrices.

# Properties
- [[Permutation]]
- [[Symmetric Group]]
- [[Permutation Sign]]
- [[LUP Decomposition]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=371)
[^2]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=372)
