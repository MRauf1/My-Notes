---
tags:
  - mathematics
  - linear_algebra
---

# Definition

> [!info] Definition 1 ([[Matrix]] [[Multiplication]])[^1]
> Let $A \in M_{m, n}(\mathbb{F})$ and $B \in M_{n, p}(\mathbb{F})$. The product $AB$ is the unique $m \times p$ [[Matrix]] over $\mathbb{F}$ such that for all $v \in \mathbb{F}^p$, $A(Bv) = (AB)v$.
> The number of columns of $A$ must be equal to the number of rows $B$.
> In particular, $[AB]_{ij} = \sum_{k=1}^n a_{ik} b_{kj}$.
> Alternatively, one can view $AB$ as $\begin{bmatrix}\mid & & \mid\\Ab_1 & \dots & Ab_p\\ \mid & & \mid\end{bmatrix}$. In other words, the $j$th column of $AB$ is $A$ times the $j$th column of $B$. It then follows that every column of $AB$ is a [[Linear Combination]] of the columns of $A$. Or we could also say that every row of $AB$ is a [[Linear Combination]] of the rows of $B$. Also, the $(i, j)$th entry of $AB$ is the $i$th row of $A$ times the $j$th column of $B$.

> [!abstract] Theorem 2 (Using [[Coordinates]])[^2]
> Let $U, V, W$ be [[Finite-Dimensional Vector Space]] with [[Basis]] $\mathcal{B}_U, \mathcal{B}_V, \mathcal{B}_W$ respectively, and suppose that $T \in \mathcal{L}(U, V)$ and $S \in \mathcal{L}(V, W)$. Then $[ST]_{\mathcal{B}_U, \mathcal{B}_W} = [S]_{\mathcal{B}_V, \mathcal{B}_W} [T]_{\mathcal{B}_U, \mathcal{B}_V}$.

# Properties
- [[Matrix Multiplication Basic Properties]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=111)
[^2]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=213)