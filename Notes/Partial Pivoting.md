---
tags:
  - computer_science
  - numerical_analysis
---

# Definition
> [!info] Definition 1 (Partial Pivoting)[^1]
> In [[Gaussian Elimination]], partial pivoting chooses, for each column $k$, the entry of largest magnitude on or below the diagonal as the pivot. It is brought into position by a row interchange (a [[Permutation Matrix]] $P_k$). Hence
> $$
> \begin{align}
> MA = U, \qquad M = M_{n-1}P_{n-1} \cdots M_1 P_1
> \end{align}
> $$
> Equivalently, with $P = P_{n-1} \cdots P_1$,
> $$
> \begin{align}
> PA = LU
> \end{align}
> $$
> where $L$ is unit lower triangular. $Ax = b$ is solved by [[Forward-Substitution]] on $Ly = Pb$, then [[Back-Substitution]] on $Ux = y$.

It is called "partial" because only the current column is searched for a pivot. $M^{-1}$ is triangular only in a generalized (row-permuted) sense, so "LU" no longer literally means lower times upper, although it is equally useful. Alternatively, $P$ can be seen as the row ordering in which no interchanges would be needed for stability, though that ordering cannot be known in advance.[^2]

# Properties
- The multipliers satisfy $|m_i| \leq 1$.[^1]
- It is essential in practice for a numerically stable Gaussian elimination on general linear systems, and it is almost universally used.[^1]
- The [[Growth Factor]] can be as large as $2^{n-1}$ in the worst case, but this is extremely rare.
- If $A$ is [[Diagonally Dominant Matrix|diagonally dominant by columns]], no row interchanges occur.
- In implementations, rows are not physically swapped. A single auxiliary integer vector tracks the row order, since the net effect of all interchanges is one permutation of $1, \dots, n$.[^3]
- [[LUP Decomposition]]
- [[Complete Pivoting]]

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=91)
[^2]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=93)
[^3]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=98)
