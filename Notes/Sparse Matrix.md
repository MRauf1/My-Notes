---
tags:
  - computer_science
  - numerical_analysis
---

# Definition
> [!info] Definition 1 (Sparse Matrix)[^1]
> A matrix $A \in \mathbb{R}^{n \times n}$ is sparse if most of its entries are zero, i.e., the number of nonzeros $\operatorname{nnz}(A) \ll n^2$ (typically $\operatorname{nnz}(A) = O(n)$).

A symmetric sparse matrix corresponds to an undirected [[Graph]] on vertices $\{1, \dots, n\}$, with an edge $\{i, j\}$ whenever $a_{ij} \neq 0$. Eliminating variable $k$ connects all of its not-yet-eliminated neighbors into a clique. The new edges are the fill-in: entries that are zero in $A$ but nonzero in the factor $L$.[^2]

# Types
- [[Banded Matrix]] (nonzeros confined to a band)
- [[Tridiagonal Matrix]]

# Properties
## Storage and Basic Operations[^2]
- Coordinate format (COO): $3\operatorname{nnz}$ numbers (row, column, value).
- Compressed sparse row (CSR) / compressed sparse column (CSC): $2\operatorname{nnz} + n + 1$ numbers (values, column/row indices, row/column pointers).
- Matrix–vector product $Ax$: $\operatorname{nnz}$ multiplications and $\operatorname{nnz}$ additions, i.e., $O(\operatorname{nnz})$ versus $n^2$ for dense.
- The inverse $A^{-1}$ of an irreducible sparse matrix is generally completely dense ($n^2$ entries), so it should never be formed explicitly (see [[LU Decomposition]]).

## Sparse Direct Methods (Sparse Cholesky / LU)[^2][^3]
- Phases:
	1. Fill-reducing ordering: permute to $PAP^T$.
	2. Symbolic factorization: predict the nonzero pattern of $L$ via the elimination tree, in about $O(\operatorname{nnz}(L))$ time.
	3. Numeric factorization.
	4. Triangular solves.
- Work of numeric Cholesky: $\sum_{j} c_j^2$ multiplications to leading order, where $c_j$ is the number of nonzeros in column $j$ of $L$. Storage is $\operatorname{nnz}(L)$, and each solve costs about $2\operatorname{nnz}(L)$ multiplications.
- The factorization is computed once and reused for any number of right-hand sides at $O(\operatorname{nnz}(L))$ each.
- Finding the ordering that minimizes fill is NP-complete (Yannakakis 1981), so heuristics are used:
	- Reverse Cuthill–McKee: reduces bandwidth, then a [[Banded Matrix|band]] solver is applied.
	- (Approximate) minimum degree (AMD): a greedy choice of the vertex that creates the least fill.
	- Nested dissection: recursively remove small vertex separators and order the separator last.
- Complexity with nested dissection for $n$ unknowns (these bounds are optimal for these graphs):[^3][^4]

| Graph / problem | Factorization work | Storage $\operatorname{nnz}(L)$ = solve cost |
| --- | --- | --- |
| 2D grid, planar graphs (e.g., triangle meshes) | $O(n^{3/2})$ | $O(n \log n)$ |
| 3D grid | $O(n^2)$ | $O(n^{4/3})$ |

  For comparison, a band ordering of the $\sqrt{n} \times \sqrt{n}$ 2D grid ($\beta = \sqrt{n}$) gives $O(\beta^2 n) = O(n^2)$ work and $O(n^{3/2})$ storage.
- Pivoting conflicts with a fill-reducing ordering. Symmetric positive definite matrices need none, so the ordering can be fixed in advance. For nonsymmetric matrices, threshold partial pivoting accepts any pivot with $|a_{ik}| \geq \tau \max_i |a_{ik}|$ for some $\tau \in (0, 1]$, trading stability for sparsity.

## Iterative Methods[^2]
- They touch $A$ only through products $Ax$, at $O(\operatorname{nnz})$ per iteration, with $O(n)$ extra storage and no fill.
- Conjugate gradient (for symmetric positive definite $A$): $O(\sqrt{\kappa}\log(1/\epsilon))$ iterations to reach relative accuracy $\epsilon$, where $\kappa$ is the 2-norm [[Condition Number of a Matrix|condition number]]. It stores 4 vectors ($4n$).
	- For the 2D Poisson problem, $\kappa = O(n)$, giving $O(n^{3/2})$ total work, which matches nested dissection.
- GMRES (for general $A$): $k$ iterations cost $O(k \operatorname{nnz} + k^2 n)$ work and $O(kn)$ storage.
- Multigrid (for elliptic PDE discretizations): $O(n)$ work and storage, which is optimal.
- Preconditioning (e.g., incomplete Cholesky/LU, which drops fill) reduces the iteration count.

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=105)
[^2]: [Sparse matrix (Wikipedia)](https://en.wikipedia.org/wiki/Sparse_matrix)
[^3]: [Nested dissection (Wikipedia)](https://en.wikipedia.org/wiki/Nested_dissection)
[^4]: [Generalized Nested Dissection (Lipton, Rose, Tarjan 1979)](https://epubs.siam.org/doi/abs/10.1137/0716027)
