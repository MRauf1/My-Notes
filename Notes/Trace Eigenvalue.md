---
tags:
  - mathematics
  - linear_algebra
---

# Definition

> [!abstract] Theorem 1 ([[Trace]] [[Eigenvalue]])[^1]
> Suppose that $dim(V) = n$ and $T$ has $n$ distinct [[Eigenvalue]] $\lambda_1, \dots, \lambda_n$. Then $tr(T) = \sum_{i=1}^n \lambda_i$.

> [!abstract] Theorem 2 (General Case -- Corollary 6.24)[^2]
> If $\mathbb{F}$ is [[Algebraically Closed Field|algebraically closed]] and $A \in M_n(\mathbb{F})$, then $tr(A) = \sum_{i=1}^n \lambda_i$, where $\lambda_1, \dots, \lambda_n$ are the [[Eigenvalue]] of $A$ counted with [[Algebraic Multiplicity of Eigenvalue|algebraic multiplicity]], without requiring $A$ to have $n$ distinct eigenvalues as in Theorem 1. Since a product $AB$ with $A \in M_{m, n}(\mathbb{F})$ and $B \in M_{n, m}(\mathbb{F})$ is itself a square matrix, this applies equally to $tr(AB)$.

Algebraic closedness of $\mathbb{F}$ is what guarantees all $n$ eigenvalues (with multiplicity) actually exist in $\mathbb{F}$ to sum; see [[Algebraic Multiplicity of Eigenvalue]].

# Properties
- [[Trace of Matrix Multiplication]]
- [[Determinant Eigenvalue]]
- [[Characteristic Polynomial]]

[^2]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=382)

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=234)