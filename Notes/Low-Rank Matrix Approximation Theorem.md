---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!abstract] Theorem 1 (Theorem 5.8 -- Best Approximation in [[Operator Norm]])[^1]
> Let $A \in M_{m,n}(\mathbb{C})$ be fixed with positive [[Singular Value|singular values]] $\sigma_1 \geq \dots \geq \sigma_r > 0$. Then for any $B \in M_{m,n}(\mathbb{C})$ with [[Rank]] $k < r$,
> $$
> \lVert A - B \rVert_{op} \geq \sigma_{k+1}
> $$
> and equality is achieved for $B = \sum_{j=1}^k \sigma_j u_j v_j^*$, using the notation of the outer-product form of the [[Singular Value Decomposition Theorem|SVD]].

$\sigma_{k+1}$ is a *lower bound* on $\lVert A - B \rVert_{op}$ that holds for **every** rank-$k$ matrix $B$: no rank-$k$ matrix can approximate $A$ (in operator norm) more closely than $\sigma_{k+1}$. Since the truncated SVD $B = \sum_{j=1}^k \sigma_j u_j v_j^*$ actually attains this bound with equality, it cannot be beaten by any other rank-$k$ matrix — making it a best rank-$k$ approximation of $A$ in the operator norm.

> [!abstract] Theorem 2 (Theorem 5.9 -- Best Approximation in [[Frobenius Norm]])[^2]
> Let $A \in M_{m,n}(\mathbb{C})$ be fixed with positive singular values $\sigma_1 \geq \dots \geq \sigma_r > 0$. Then for any $B \in M_{m,n}(\mathbb{C})$ with rank $k < r$,
> $$
> \lVert A - B \rVert_F \geq \sqrt{\sum_{j=k+1}^r \sigma_j^2}
> $$
> and equality is achieved for the same truncated SVD $B = \sum_{j=1}^k \sigma_j u_j v_j^*$.

Together, Theorems 1 and 2 imply the surprising fact that the best rank-$k$ approximation of $A$ is the *same* matrix regardless of whether "best" is judged using the operator norm or the Frobenius norm — even though, in general, what counts as the "best" approximation depends heavily on the choice of norm.

This gives a practical way to compress a matrix: approximating $A$ by a lower-rank matrix reduces the amount of data needed to describe it (a rank-$k$ matrix needs only $(m+n)k$ numbers, versus $mn$ for the full matrix), which is important for making large computations feasible.

# Properties
- [[Singular Value Decomposition Theorem]]
- [[Singular Value]]
- [[Rank]]
- [[Operator Norm]]
- [[Frobenius Norm]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=324)
[^2]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=326)
