---
tags:
  - computer_science
  - numerical_analysis
---

# Definition
> [!info] Definition 1 (Banded Matrix)[^1]
> A matrix $A$ is banded with bandwidth $\beta$ if
> $$
> \begin{align}
> a_{ij} = 0 \quad \text{for all } |i - j| > \beta
> \end{align}
> $$

# Types
- [[Tridiagonal Matrix]] ($\beta = 1$)

# Properties
- A banded system needs $O(\beta n)$ storage and its factorization $O(\beta^2 n)$ work. This is a large saving over a full system ($n^2$ storage, $n^3/3$ multiplications for LU) when $\beta \ll n$.[^2]
- Exact leading-order counts for $n \gg \beta$ (multiplications, with a similar number of additions):
	- Storage of the band: $(2\beta + 1)n$ entries, or $(\beta + 1)n$ if symmetric.
	- [[LU Decomposition|LU]] without pivoting: about $\beta^2 n$ multiplications. $L$ and $U$ keep lower/upper bandwidth $\beta$, so there is no fill outside the band.
	- LU with [[Partial Pivoting]]: row interchanges can widen $U$ to upper bandwidth $2\beta$. Storage becomes $(3\beta + 1)n$ and work about $2\beta^2 n$ multiplications.
	- Band [[Cholesky Decomposition|Cholesky]] (symmetric positive definite): about $\beta^2 n / 2$ multiplications plus $n$ square roots. $L$ keeps bandwidth $\beta$, and no pivoting is needed.
	- Each banded triangular solve ([[Forward-Substitution|forward]] or [[Back-Substitution|back]]): about $\beta n$ multiplications, so about $2\beta n$ per right-hand side.
- A [[Sparse Matrix]] can often be reordered (e.g., by reverse Cuthill–McKee) to reduce its bandwidth before applying a band solver.

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=105)
[^2]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=108)
