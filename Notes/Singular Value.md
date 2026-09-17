---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!info] Definition 1 (Singular Value)[^1]
> Let $V$ and $W$ be [[Finite-Dimensional Vector Space|finite-dimensional]] [[Inner Product Space]]s and let $T \in \mathcal{L}(V, W)$. The singular values of $T$ are the numbers $\sigma_1 \geq \dots \geq \sigma_p \geq 0$, where $p = \min\{m, n\}$: $\sigma_1, \dots, \sigma_r$ are as given by the [[Singular Value Decomposition Theorem]], and $\sigma_j = 0$ for $r+1 \leq j \leq p$.

Singular values are always [[Real Number]] and non-negative.

> [!info] Definition 2 (Singular Value of a Matrix)[^7]
> Let $A \in M_{m,n}(\mathbb{C})$ with $A = U \Sigma V^*$ as in the matrix form of the [[Singular Value Decomposition Theorem]], and $p = \min\{m,n\}$. The singular values of $A$ are the diagonal entries $\sigma_j$ of $\Sigma$ for $1 \leq j \leq r$, together with $\sigma_j := 0$ for $r+1 \leq j \leq p$. The columns of $U$ are the left singular vectors of $A$, and the columns of $V$ are the right singular vectors of $A$.

> [!abstract] Proposition 8 (Proposition 5.5 -- Relation to Eigenvalues of $A^*A$ and $AA^*$)[^8]
> Let $A \in M_{m,n}(\mathbb{F})$ have singular values $\sigma_1 \geq \dots \geq \sigma_p$, where $p = \min\{m,n\}$. Then for each $j = 1, \dots, p$, $\sigma_j^2$ is an [[Eigenvalue]] of $A^*A$ and of $AA^*$. Whichever of $A^*A$, $AA^*$ is the $p \times p$ matrix has exactly $\sigma_1^2, \dots, \sigma_p^2$ as eigenvalues; if the other is larger, it has eigenvalues $\sigma_1^2, \dots, \sigma_p^2$ together with $0$.

So the singular values of $A$ are precisely the square roots of the eigenvalues of $A^*A$ and of $AA^*$.

> [!abstract] Proposition 9 (Proposition 5.6 -- Frobenius Norm in Terms of Singular Values)[^9]
> If $\sigma_1, \dots, \sigma_r$ are the positive singular values of $A \in M_{m,n}(\mathbb{C})$, then
> $$
> \lVert A \rVert_F = \sqrt{\sum_{j=1}^r \sigma_j^2}
> $$

Together with $\lVert A \rVert_{op} = \sigma_1$ (the length of the longest semi-axis of the ellipsoid image of the unit sphere under $A$), this shows the [[Operator Norm]] measures the maximum distortion produced by $A$, while the [[Frobenius Norm]] measures a kind of average distortion.[^10]

> [!abstract] Theorem 10 (Exercise 5.2.5)[^11]
> The singular values of $A^*$ are the same as the singular values of $A$.

> [!abstract] Theorem 11 (Exercise 5.2.8)[^11]
> If $A = \text{diag}(\lambda_1, \dots, \lambda_n)$, then the singular values of $A$ are $|\lambda_1|, \dots, |\lambda_n|$ (though not necessarily in that order).

> [!abstract] Theorem 12 (Exercise 6.2.3b)[^12]
> If $\sigma_1, \dots, \sigma_n$ are the singular values of $A \in M_n(\mathbb{C})$, then $|\det(A)| = \sigma_1 \cdots \sigma_n$.

> [!abstract] Theorem 2 (Largest Singular Value is the Operator Norm)[^2]
> The largest singular value of $T$ equals its [[Operator Norm]]: $\sigma_1 = \lVert T \rVert_{op}$.

> [!abstract] Lemma 3 (Lemma 5.2)[^3]
> Let $V, W$ be finite-dimensional inner product spaces and $T \in \mathcal{L}(V, W)$. Let $e \in V$ be a unit vector such that $\lVert T \rVert_{op} = \lVert Te \rVert$. Then for any $u \in V$ with $\langle u, e \rangle = 0$, we have $\langle Tu, Te \rangle = 0$.

Lemma 3 is the key technical step used to build the [[Singular Value Decomposition Theorem|SVD]] inductively: the vector achieving the operator norm becomes the first singular vector pair, and the lemma shows the orthogonal complement can be handled independently by the same argument, producing the next singular value/vector pair, and so on.

> [!abstract] Theorem 4 (Theorem 5.3 -- Uniqueness of Singular Values)[^4]
> The singular vectors in the [[Singular Value Decomposition Theorem|SVD]] are not unique, but the singular values are: if $(e_1, \dots, e_n), (f_1, \dots, f_m)$ and $(\tilde{e}_1, \dots, \tilde{e}_n), (\tilde{f}_1, \dots, \tilde{f}_m)$ both give a singular value decomposition of $T \in \mathcal{L}(V, W)$ with $\text{rank}(T) = r$, with corresponding singular values $\sigma_1 \geq \dots \geq \sigma_r > 0$ and $\tilde\sigma_1 \geq \dots \geq \tilde\sigma_r > 0$, then $\sigma_j = \tilde\sigma_j$ for all $j \in \{1, \dots, r\}$.

For example, for the identity map $I: V \to V$, every [[Orthonormal Basis]] $(e_1, \dots, e_n)$ satisfies $I(e_j) = e_j$, so the singular vectors depend entirely on the choice of basis; the singular values, however, are always $\sigma_j = 1$ for every $j$, regardless of that choice.

> [!abstract] Theorem 5 (Exercise 5.1.8)[^5]
> $T \in \mathcal{L}(V, W)$ is [[Invertible Linear Map|invertible]] if and only if $\dim V = \dim W$ and all the singular values of $T$ are nonzero.

> [!abstract] Theorem 6 (Exercise 5.1.10)[^6]
> Suppose $T \in \mathcal{L}(V, W)$ is invertible with singular values $\sigma_1 \geq \dots \geq \sigma_n$. Then
> $$
> \sigma_n = \min_{\lVert v \rVert = 1} \lVert Tv \rVert = \lVert T^{-1} \rVert_{op}^{-1}
> $$

> [!abstract] Theorem 7 (Exercise 5.1.11)[^6]
> If $V$ is a finite-dimensional inner product space and all the singular values of $T \in \mathcal{L}(V)$ are $1$, then $T$ is an [[Isometry (Linear Algebra)|isometry]].

# Properties
- [[Singular Value Decomposition Theorem]]
- [[Operator Norm]]
- [[Frobenius Norm]]
- [[Isometry (Linear Algebra)]]
- [[Invertible Linear Map]]
- [[Rank]]
- [[Rank Matrix Transpose]]
- [[Condition Number of a Matrix]]
- [[Pseudoinverse]]
- [[Determinant]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=315)
[^2]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=311)
[^3]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=310)
[^4]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=313)
[^5]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=316)
[^6]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=316)
[^7]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=319)
[^8]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=319)
[^9]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=322)
[^10]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=323)
[^11]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=329)
[^12]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=375)
