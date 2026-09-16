---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!info] Definition 1 (Adjoint)[^1]
> Let $V$ and $W$ be [[Inner Product Space]]s, and let $T \in \mathcal{L}(V, W)$. A [[Linear Map]] $S \in \mathcal{L}(W, V)$ is an adjoint of $T$ if $\langle Tv, w \rangle = \langle v, Sw \rangle$ for every $v \in V$ and $w \in W$. We then write $S = T^*$.

Intuitively, the adjoint is the operator that lets you move $T$ across an inner product from one argument to the other, the way integration by parts moves a derivative from one factor to the other. $T$ maps $V \to W$; its adjoint $T^*$ maps in the opposite direction, $W \to V$, and is defined purely by how it interacts with the inner product, without reference to any basis. This is why $T^*$ is the correct abstract generalization of the [[Matrix Conjugate Transpose|conjugate transpose]] (and, over $\mathbb{R}$, the transpose): the transpose of a matrix is exactly the operation that swaps which vector, input or "measuring" vector, the map is allowed to act on inside a dot product, and the adjoint is what that idea means once "dot product" is replaced by an arbitrary inner product on possibly different spaces $V, W$.

Its usefulness comes from how much structure it lets you read off a map $T$ just from its relationship to $T^*$:
- **It classifies the important operator types.** A map is an [[Isometry (Linear Algebra)|isometry]] (norm- and angle-preserving) exactly when $T^{-1} = T^*$; a [[Unitary Matrix|unitary/orthogonal matrix]] is exactly one with $A^{-1} = A^*$; a [[Self-Adjoint Linear Map|self-adjoint operator]] ($T^* = T$, i.e. Hermitian/symmetric) is exactly the kind with real eigenvalues and orthogonal eigenvectors. Nearly every "nice" class of linear map in an inner product space is a statement about how $T$ relates to $T^*$.
- **It reveals the hidden structure of $T$ itself.** The [[Adjoint Kernel Range Theorem|kernel and range of $T$ and $T^*$]] are orthogonal complements of each other, and $A^*A$, $AA^*$ are what drive the [[Singular Value Decomposition Theorem|singular value decomposition]]: the singular values of $T$ are the square roots of the eigenvalues of $T^*T$.
- **It is the linear-algebra ancestor of backpropagation.** Whenever a computation is a composition of linear maps, propagating a gradient backward through it means multiplying by the adjoint (transpose) of each map in reverse order — the same idea underlies adjoint methods for sensitivity analysis in numerical simulation and PDE-constrained optimization.

> [!abstract] Lemma 2 (Lemma 5.11 -- Uniqueness)[^2]
> If $T \in \mathcal{L}(V, W)$ has an adjoint, then its adjoint is unique.

So $T^*$ (if it exists) is the one and only operator satisfying $\langle Tv, w \rangle = \langle v, T^*w \rangle$ for every $v \in V, w \in W$.

> [!abstract] Theorem 3 (Theorem 5.12 -- Existence)[^3]
> If $V$ is a [[Finite-Dimensional Vector Space|finite-dimensional]] [[Inner Product Space]] and $W$ is any [[Inner Product Space]], then every $T \in \mathcal{L}(V, W)$ has an adjoint.

The same symbol used for the [[Matrix Conjugate Transpose]] of a matrix is used for the adjoint of a linear map because, with respect to orthonormal bases, they coincide:

> [!abstract] Theorem 4 (Theorem 5.13 -- Matrix of the Adjoint)[^4]
> Suppose $\mathcal{B}_V$ and $\mathcal{B}_W$ are [[Orthonormal Basis|orthonormal bases]] of $V$ and $W$, respectively. Then for $T \in \mathcal{L}(V, W)$,
> $$
> [T^*]_{\mathcal{B}_V, \mathcal{B}_W} = [T]_{\mathcal{B}_V, \mathcal{B}_W}^*
> $$

This only holds when **both** $\mathcal{B}_V$ and $\mathcal{B}_W$ are orthonormal.

> [!abstract] Proposition 5 (Proposition 5.14 -- Basic Properties)[^5]
> Let $U, V, W$ be finite-dimensional inner product spaces, $S, T \in \mathcal{L}(U, V)$, and $R \in \mathcal{L}(V, W)$. Then:
> 1. $(T^*)^* = T$
> 2. $(S + T)^* = S^* + T^*$
> 3. $(aT)^* = \bar{a} T^*$ (the adjoint is conjugate-linear in scalars)
> 4. $(RT)^* = T^*R^*$
> 5. If $T$ is invertible, then $(T^{-1})^* = (T^*)^{-1}$

> [!abstract] Theorem 6 (Exercise 5.3.10a -- [[Trace]] of the Adjoint)[^6]
> $tr(T^*) = \overline{tr(T)}$.

> [!abstract] Theorem 7 (Exercise 5.3.13)[^6]
> $T^*T = 0$ if and only if $T = 0$.

> [!abstract] Theorem 8 (Exercise 5.3.14)[^6]
> $\lVert T^* \rVert_{op} = \lVert T \rVert_{op}$.

> [!abstract] Theorem 9 (Exercise 5.3.15)[^6]
> $\lVert T^*T \rVert_{op} = \lVert TT^* \rVert_{op} = \lVert T \rVert_{op}^2$.

Property 5 of Proposition 5 identifies exactly when an [[Isometry (Linear Algebra)|isometry]] exists: Theorem 4.27 says an invertible $T$ is an isometry iff $\langle Tv, w \rangle = \langle v, T^{-1}w \rangle$, i.e. iff $T^{-1} = T^*$.

# Properties
- [[Matrix Conjugate Transpose]]
- [[Isometry (Linear Algebra)]]
- [[Self-Adjoint Linear Map]]
- [[Unitary Matrix]]
- [[Adjoint Kernel Range Theorem]]
- [[Trace]]
- [[Operator Norm]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=331)
[^2]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=332)
[^3]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=332)
[^4]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=333)
[^5]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=333)
[^6]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=339)
