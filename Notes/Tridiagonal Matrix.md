---
tags:
  - computer_science
  - numerical_analysis
---

# Definition
> [!info] Definition 1 (Tridiagonal Matrix)[^1]
> A tridiagonal matrix is a [[Banded Matrix]] with bandwidth $\beta = 1$, i.e., $a_{ij} = 0$ whenever $|i - j| > 1$. Its only nonzeros are the main diagonal $d_i$, the subdiagonal $a_i$ and the superdiagonal $c_i$.

> [!info] Definition 2 (Tridiagonal Algorithm / Thomas Algorithm)
> [[Gaussian Elimination]] without pivoting, specialized to tridiagonal systems:
> 1. Factor: for $i = 2, \dots, n$, set $m_i = a_i / d_{i-1}$ and $d_i \leftarrow d_i - m_i c_{i-1}$.
> 2. Forward: for $i = 2, \dots, n$, set $b_i \leftarrow b_i - m_i b_{i-1}$.
> 3. Back: $x_n = b_n / d_n$, and $x_i = (b_i - c_i x_{i+1}) / d_i$ for $i = n-1, \dots, 1$.

# Properties
- Storage: $3n - 2$ entries (plus $n$ for the right-hand side). $L$ and $U$ are bidiagonal and overwrite the same storage.
- Work (exact counts):
	- Factor: $n - 1$ divisions, $n - 1$ multiplications and $n - 1$ subtractions.
	- Forward: $n - 1$ multiplications and $n - 1$ subtractions.
	- Back: $n$ divisions, $n - 1$ multiplications and $n - 1$ subtractions.
	- Total about $8n$ floating-point operations, so $O(n)$ versus $n^3/3$ multiplications for dense LU.
- Stable without pivoting if $A$ is [[Diagonally Dominant Matrix|diagonally dominant]] or symmetric [[Positive Definite Matrix|positive definite]]. Otherwise [[Partial Pivoting]] is needed, which widens $U$ to upper bandwidth 2 (still $O(n)$).
- [[Symmetric Indefinite Factorization]] (Aasen's method reduces a symmetric matrix to tridiagonal form)

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=105)
