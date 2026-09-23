---
tags:
  - computer_science
  - numerical_analysis
---

# Definition
> [!info] Definition 1 (Induced Matrix Norm)[^1]
> Given a [[Vector Norm|vector norm]] $\lVert \cdot \rVert$, the corresponding matrix norm of an $m \times n$ [[Matrix]] $A$ is
> $$
> \begin{align}
> \lVert A \rVert = \max_{x \neq 0} \frac{\lVert Ax \rVert}{\lVert x \rVert}
> \end{align}
> $$
> Such a matrix norm is said to be induced by (or subordinate to) the vector norm.

Intuitively, the induced norm measures the maximum stretching $A$ does to any vector, as measured in the given vector norm. The [[Operator Norm]] is the special case induced by the 2-norm.

> [!info] Definition 2 (General Matrix Norm)[^2]
> More generally, a matrix norm is any real-valued function of a matrix satisfying, for all matrices $A, B$ and scalars $\gamma$:
> 1. $\lVert A \rVert > 0$ if $A \neq O$.
> 2. $\lVert \gamma A \rVert = |\gamma| \cdot \lVert A \rVert$.
> 3. $\lVert A + B \rVert \leq \lVert A \rVert + \lVert B \rVert$.
>
> Properties 1 and 2 together imply $\lVert A \rVert = 0 \iff A = O$.

# Types
- 1-norm (induced by the [[1-Norm]]), the maximum absolute column sum:[^2]
$$
\begin{align}
\lVert A \rVert_1 = \max_j \sum_{i=1}^m |a_{ij}|
\end{align}
$$
- $\infty$-norm (induced by the [[Infinity Norm]]), the maximum absolute row sum:[^2]
$$
\begin{align}
\lVert A \rVert_\infty = \max_i \sum_{j=1}^n |a_{ij}|
\end{align}
$$
- 2-norm (induced by the [[Vector Norm|2-norm]]), the [[Operator Norm]]. It is much harder to compute, as it equals the largest [[Singular Value]].

These agree with the corresponding vector norms for an $n \times 1$ matrix.

# Properties
- Every induced norm is a general matrix norm (Definition 2), and additionally satisfies the submultiplicative (consistency) conditions, which may fail for general matrix norms:[^2]
$$
\begin{align}
\lVert AB \rVert &\leq \lVert A \rVert \cdot \lVert B \rVert \\
\lVert Ax \rVert &\leq \lVert A \rVert \cdot \lVert x \rVert
\end{align}
$$
- [[Condition Number of a Matrix]]
- [[Frobenius Norm]] (a matrix norm that is not induced by any vector norm)
- [[p-Norm]]

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=75)
[^2]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=75)
