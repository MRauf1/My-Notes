---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Expectation of a Random Matrix[^1]
> Let $\mathbf{W} = [W_{ij}]$ be an $m \times n$ matrix of [[Random Variable|random variables]]. Its expectation is the matrix of entrywise [[Expectation|expectations]]
> $$
> \begin{align}
> E[\mathbf{W}] = [E(W_{ij})]
> \end{align}
> $$

Stringing out the matrix into an $mn \times 1$ [[Random Vector]] shows this is the same as the [[Mean Vector]] of that vector.

> [!abstract] Theorem 1 (Linearity for Random Matrices)[^1]
> Let $\mathbf{W}_1, \mathbf{W}_2$ be $m \times n$ random matrices, $\mathbf{A}_1, \mathbf{A}_2$ be $k \times m$ constant matrices, and $\mathbf{B}$ be an $n \times l$ constant matrix. Then
> $$
> \begin{align}
> E[\mathbf{A}_1 \mathbf{W}_1 + \mathbf{A}_2 \mathbf{W}_2] &= \mathbf{A}_1 E[\mathbf{W}_1] + \mathbf{A}_2 E[\mathbf{W}_2] \\
> E[\mathbf{A}_1 \mathbf{W}_1 \mathbf{B}] &= \mathbf{A}_1 E[\mathbf{W}_1] \mathbf{B}
> \end{align}
> $$

Each entry of $\mathbf{A}_1 \mathbf{W}_1 \mathbf{B}$ is a linear combination of the $W_{ij}$ with constant coefficients, so the theorem is entrywise linearity of expectation.

# Properties
- Expectation commutes with [[Matrix Transpose|transpose]] and [[Trace of Matrix Multiplication|trace]]: $E[\mathbf{W}^T] = E[\mathbf{W}]^T$, $E[\text{tr}\,\mathbf{W}] = \text{tr}\,E[\mathbf{W}]$.
- It does not commute with nonlinear maps such as products of random matrices, inverses, or determinants.
- The [[Covariance Matrix]] is the expectation of the random matrix $(\mathbf{X} - \boldsymbol{\mu})(\mathbf{X} - \boldsymbol{\mu})^T$.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=156)
