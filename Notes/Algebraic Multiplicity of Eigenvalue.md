---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!info] Definition 1 (Algebraic Multiplicity of Eigenvalue)[^1]
> Let $A \in M_n(\mathbb{F})$, where $\mathbb{F}$ is an [[Algebraically Closed Field]], and let $\lambda$ be an [[Eigenvalue]] of $A$. The [[Characteristic Polynomial]] $p_A(x)$ factors as
> $$
> p_A(x) = (-1)^n (x - \lambda)^k (x - c_1)^{k_1} \cdots (x - c_m)^{k_m}
> $$
> where the $c_j$ are distinct from each other and from $\lambda$. The power $k$ to which the factor $(x - \lambda)$ appears is the (algebraic) multiplicity of $\lambda$ as an eigenvalue of $A$.

> [!abstract] Theorem 2 (Proposition 6.22)[^2]
> If $\mathbb{F}$ is algebraically closed, every $A \in M_n(\mathbb{F})$ has $n$ eigenvalues, counted with multiplicity. If $\lambda_1, \dots, \lambda_m$ are the distinct eigenvalues of $A$ with respective multiplicities $k_1, \dots, k_m$, then
> $$
> p_A(x) = \prod_{j=1}^m (\lambda_j - x)^{k_j}
> $$

> [!abstract] Lemma 3 (Lemma 6.23 -- Triangular Case)[^3]
> Suppose $A \in M_n(\mathbb{F})$ is [[Upper Triangular Matrix|upper triangular]] and $\lambda$ is an eigenvalue of $A$. Then the multiplicity of $\lambda$ is the number of times $\lambda$ appears on the diagonal of $A$.

This algebraic multiplicity should be distinguished from the [[Geometric Multiplicity of Eigenvalue|geometric multiplicity]] of $\lambda$, $null(A - \lambda I_n)$: the geometric multiplicity is always at most the algebraic multiplicity, though the two need not be equal.

# Properties
- [[Characteristic Polynomial]]
- [[Geometric Multiplicity of Eigenvalue]]
- [[Eigenvalue]]
- [[Algebraically Closed Field]]
- [[Similar Matrix Characteristic Polynomial]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=381)
[^2]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=381)
[^3]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=381)
