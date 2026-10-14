---
tags:
  - mathematics
  - real_analysis
---

# Definition
> [!abstract] Theorem 1 (Mean Value Inequality)[^1]
> Suppose $\mathbf{f}$ is a continuous mapping of $[a, b]$ into $\mathbb{R}^k$ and $\mathbf{f}$ is differentiable in $(a, b)$. Then there exists $x \in (a, b)$ such that
> $$
> \begin{align}
> |\mathbf{f}(b) - \mathbf{f}(a)| \leq (b - a) |\mathbf{f}'(x)|
> \end{align}
> $$

The [[Mean Value Theorem]] equality fails for vector-valued functions, but this inequality survives ([[Derivative of Vector-Valued Function]]).

# Properties
- Reduces to a bound on the real MVT by applying it to $\varphi(t) = \mathbf{z} \cdot \mathbf{f}(t)$ with $\mathbf{z} = \mathbf{f}(b) - \mathbf{f}(a)$ and using the [[Cauchy-Schwarz Inequality]].

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=122&annotation=XDLDP7CN)
