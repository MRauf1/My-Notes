---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!abstract] Theorem 1 (Theorem 6.3 -- Existence and Uniqueness of the Determinant)[^1]
> For each $n$, there is a unique [[Alternating Multilinear Function|alternating multilinear function]] $D: M_n(\mathbb{F}) \to \mathbb{F}$ such that $D(I_n) = 1$. This function is called the determinant, and the determinant of $A$ is denoted $\det(A)$.

> [!abstract] Lemma 2 (Lemma 6.8 -- Existence)[^2]
> For each $n$, there exists a determinant function on $M_n(\mathbb{F})$.

The existence half of Theorem 1 is established constructively, by cofactor expansion using the [[Matrix Minor|minors]] of $A$; the content above only records that such a function exists, not the expansion formula itself.

The uniqueness half of Theorem 1 is what makes the determinant powerful: it is not just a good detector of singularity ([[Isoscopic Function|Lemma 6.1]]), but a genuine [[Invariant of Matrix|matrix invariant]].

> [!abstract] Corollary 3 (Corollary 6.4)[^3]
> If $D: M_n(\mathbb{F}) \to \mathbb{F}$ is any [[Alternating Multilinear Function|alternating multilinear function]], then $D(A) = D(I_n) \det(A)$ for every $A \in M_n(\mathbb{F})$.

So every alternating multilinear function is just a scalar multiple of the determinant.

> [!info] Definition 4 (Determinant of a Linear Map)[^4]
> Let $V$ be finite-dimensional. The determinant of $T \in \mathcal{L}(V)$ is $\det(T) := \det([T]_{\mathcal{B}})$, where $\mathcal{B}$ is any [[Basis]] of $V$.

This is well-defined regardless of which basis $\mathcal{B}$ is chosen: matrices of $T$ with respect to different bases are [[Similar Matrix|similar]], and [[Similar Matrix Determinant|similar matrices have the same determinant]], so $\det(T)$ does not depend on the choice of $\mathcal{B}$.

# Properties
- [[Multilinear Function]]
- [[Alternating Multilinear Function]]
- [[Isoscopic Function]]
- [[Matrix Minor]]
- [[Invariant of Matrix]]
- [[Determinant Matrix Multiplication]]
- [[Determinant Invertible Matrix Theorem]]
- [[Similar Matrix Determinant]]
- [[Determinant Eigenvalue]]
- [[Laplace Expansion]]
- [[Triangular Matrix Determinant]]
- [[Determinant Matrix Transpose]]
- [[Determinant Conjugate Transpose Theorem]]
- [[Determinant Computation Algorithm]]
- [[Leibniz Formula for Determinant]]
- [[Hadamard's Inequality]]
- [[LDU Decomposition]]
- [[Permutation Matrix]]
- [[Determinant Volume Scaling Theorem]]
- [[Cramer's Rule]]
- [[Adjugate Matrix]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=356)
[^2]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=360)
[^3]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=357)
[^4]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=359)
