---
tags:
  - mathematics
  - linear_algebra
---

# Definition

> [!info] Definition 1 (Diagonal [[Matrix]])[^1]
> $n \times n$ [[Matrix]] $A$ is called diagonal if $a_{ij} = 0$ whenever $i \neq j$.

> [!abstract] Theorem 2 (In Terms of [[Eigenvalue]] and [[Eigenvector]])[^2]
> Let $\mathcal{B} = (v_1, \dots, v_n)$ be a [[Basis]] for $V$ and let $T \in \mathcal{L}(V)$. The [[Matrix]] $[T]_{\mathcal{B}}$ is diagonal if and only if for each $i = 1, \dots, n$, $v_i$ is an [[Eigenvector]] of $T$. Moreover, in this case, the $i$th diagonal entry of $[T]_{\mathcal{B}}$ is the [[Eigenvalue]] of $T$ corresponding to $v_i$.

The above theorem implies that a diagonal matrix always has $n$ [[Linearly Independent]] [[Eigenvector]]. Moreover, if all of the diagonal entries are distinct from each other, then the diagonal matrix has $n$ distinct [[Eigenvalue]].

Though they look different, the above 2 definitions are actually the same.

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=88)
[^2]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=212)