---
tags:
  - computer_science
  - numerical_analysis
---

# Definition
> [!info] Definition 1 (Elementary Elimination Matrix / Gauss Transformation)[^1]
> Given a vector $a$ with $a_k \neq 0$, the elementary elimination matrix $M_k$ annihilates all entries of $a$ below position $k$:
> $$
> \begin{align}
> M_k a = \begin{bmatrix} 1 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \ddots & \vdots & \vdots & & \vdots \\ 0 & \cdots & 1 & 0 & \cdots & 0 \\ 0 & \cdots & -m_{k+1} & 1 & \cdots & 0 \\ \vdots & & \vdots & \vdots & \ddots & \vdots \\ 0 & \cdots & -m_n & 0 & \cdots & 1 \end{bmatrix} \begin{bmatrix} a_1 \\ \vdots \\ a_k \\ a_{k+1} \\ \vdots \\ a_n \end{bmatrix} = \begin{bmatrix} a_1 \\ \vdots \\ a_k \\ 0 \\ \vdots \\ 0 \end{bmatrix}, \quad m_i = \frac{a_i}{a_k}, \ i = k+1, \dots, n
> \end{align}
> $$
> i.e., $M_k$ adds a multiple of row $k$ to each subsequent row, with multipliers $m_i$ chosen to produce zeros. Here $a_k$ is the pivot.

It is a product of $n - k$ [[Elementary Matrix|elementary matrices]] of [[Row Operations|row operation]] type R1, all sharing the same source row $k$.

# Properties
- $M_k$ is a unit [[Lower Triangular Matrix]], hence nonsingular.[^1]
- $M_k = I - m_k e_k^T$, where $m_k = [0, \dots, 0, m_{k+1}, \dots, m_n]^T$ and $e_k$ is the $k$th column of $I$.[^1]
- $L_k := M_k^{-1} = I + m_k e_k^T$, i.e., the same as $M_k$ with the signs of the multipliers reversed.[^1]
- For $j > k$, since $e_k^T m_j = 0$, the product is their "union":[^1]
$$
\begin{align}
M_k M_j = I - m_k e_k^T - m_j e_j^T, \qquad L_k L_j = I + m_k e_k^T + m_j e_j^T
\end{align}
$$
  The order matters: this does not hold for the reverse product.
- [[Gaussian Elimination]]

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=87)
