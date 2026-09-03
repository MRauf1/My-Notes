---
tags:
  - mathematics
  - linear_algebra
---

# Definition

> [!info] Definition 1 (Diagonalizable [[Matrix]])[^2]
> [[Matrix]] $A \in M_n(\mathbb{F})$ is diagonalizable if $A$ is [[Similar Matrix]] to a [[Diagonal Matrix]].

> [!abstract] Theorem 2 (Alternative)
> [[Matrix]] $A \in M_n(\mathbb{F})$ is diagonalizable if and only if there is a [[Basis]] $(v_1, \dots, v_n)$ of $\mathbb{F}^n$ such that for each $i = 1, \dots, n$, $v_i$ is an [[Eigenvector]] of $A$.
> In that case, $A = S \begin{bmatrix}\lambda_1 & & 0 \\ & \ddots & \\ 0 & & \lambda_n \end{bmatrix} S^{-1}$ where $Av_i = \lambda_i v_i$ and $S = \begin{bmatrix}\mid & & \mid \\ v_1 & \dots & v_n \\ \mid & & \mid \end{bmatrix}$ ($S$ is the [[Eigenvector Matrix]] and the middle [[Matrix]] is the [[Matrix]] of [[Eigenvalue]] ([[Diagonal Matrix]])).

# Properties
- [[Diagonalizable Matrix Linear Map]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=224)