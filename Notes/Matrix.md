---
tags:
  - mathematics
  - linear_algebra
---

# Definition

> [!info] Definition 1 (Matrix)
> For $m, n \in \mathbb{N}$, $m \times n$ ($m$ rows, $n$ columns) matrix $A$ over [[Field|field]] $\mathbb{F}$ is a doubly indexed collection of items
> $$
> \begin{align}
> A = [a_{ij}]_{1 \leq i \leq m, 1 \leq j \leq n}
> \end{align}
> $$
> The [[Number|number]] $a_{ij}$ is the $(i, j)$ entry of $A$ and is denoted by $[A]_{ij}$

The set of all $m \times n$ matrices over field $\mathbb{F}$ is denoted by $M_{m,n}(\mathbb{F})$.[^1] The set of all $n \times n$ matrices over field $\mathbb{F}$ is denoted by $M_n(\mathbb{F})$.[^1]

A matrix acts as a [[Finite-Dimensional Linear Operator]] through [[Matrix-Vector Multiplication]].

> [!info] Definition 2 ([[Coordinates]] Version)[^2]
> Let $V$ and $W$ be $n$-dimensional and $m$-dimensional [[Vector Space]] over $\mathbb{F}$, respectively, and let $T: V \rightarrow W$ be a [[Linear Map]]. Suppose that $V$ has a [[Basis]] $\mathcal{B}_V = (v_1, \dots, v_n)$ and $W$ has a [[Basis]] $\mathcal{B}_W = (w_1, \dots, w_m)$. For each $1 \leq j \leq n$, define the scalars $a_{ij}$ for $1 \leq i \leq m$ to be the [[Coordinates]] of $Tv_j$ in the [[Basis]] $\mathcal{B}_W$. In other words, $Tv_j = a_{1j} w_1 + \dots + a_{mj} w_m$.
> The [[Matrix]] of $T$ with respect to $\mathcal{B}_V$ and $\mathcal{B}_W$ is the [[Matrix]] $A = [a_{ij}]_{1 \leq i \leq m; 1 \leq j \leq n}$. We denote this [[Matrix]] as $[T]_{\mathcal{B}_V, \mathcal{B}_W}$.
> When $V = W$ and $\mathcal{B}_V = \mathcal{B}_W = \mathcal{B}$, we simply write $[T]_{\mathcal{B}}$ and refer to it as the [[Matrix]] of $T$ with respect to $\mathcal{B}$.

The $j$th column of $[T]_{\mathcal{B}_V, \mathcal{B}_W}$ is the coordinate representation of $[Tv_j]_{\mathcal{B}_W}$.

> [!abstract] Theorem 3 (Lemma)
> Let $T: V \rightarrow W$ be a [[Linear Map]]. Suppose that $V$ has a [[Basis]] $\mathcal{B}_V$ and $W$ has a [[Basis]] $\mathcal{B}_W$, and let $A = [T]_{\mathcal{B}_V, \mathcal{B}_W}$. Then for any $v \in V$, $[Tv]_{\mathcal{B}_W} = A [v]_{\mathcal{B}_V}$.

Which [[Linear Map]] a given [[Matrix]] defines depends completely on the [[Basis]] we're working in.

# Representation
- [[Matrix of Linear Map]]
- [[Matrix Simple Representation]]

# Types
- [[Diagonal Matrix]]
- [[Diagonalizable Matrix]]
- [[Lower Triangular Matrix]]
- [[Upper Triangular Matrix]]
- [[Change of Basis Matrix]]
- [[Similar Matrix]]

# Properties
## [[Operation]]
- [[Matrix Multiplication]]
- [[Matrix Transpose]]
- [[Matrix Conjugate Transpose]]
- [[Matrix Inverse]]
- [[Linear Map Image]]
- [[Matrix Column Space]]
- [[Kernel]]

## Eigens
- [[Eigenvector]]
- [[Eigenvalue]]
- [[Eigenspace]]
- [[Trace]]
- [[Determinant]]

## [[Invariant of Matrix]]
- [[Similar Matrix Eigenvalue]]
- [[Similar Matrix Rank-Nullity]]
- [[Similar Matrix Trace]]
- [[Similar Matrix Geometric Multiplicity of Eigenvalue]]

## [[Rank]]-[[Nullity]]
- [[Rank]]
- [[Nullity]]
- [[Rank-Nullity Theorem]]

## Decomposition
- [[LU Decomposition]]
- [[LUP Decomposition]]

## Other
- [[Matrix Equivalence Invertible Basis RREF]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=30)
[^2]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=207)