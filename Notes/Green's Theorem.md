---
tags:
  - mathematics
  - complex_analysis
  - calculus
---

# Definition

> [!abstract] Theorem 1 (Green's Theorem)
> Let $D \subseteq \mathbb{R}^2$ be [[Open Set]]. Assume that $\Omega$ is [[Bounded Set|bounded]] [[Domain (Topology)]] and $\Omega \cup \partial \Omega \subseteq D$. Also assume that $\partial \Omega$ consists of finitely many [[Disjoint Sets|disjoint]] [[Simple Curve]] [[Closed Curve]] [[Piecewise Smooth Curve]]: $\gamma, \gamma_1, \dots, \gamma_k$ ($\Omega \subseteq \text{inside}(\gamma) \land |\gamma_1|, \dots, |\gamma_k| \subseteq \text{inside}(\gamma)$). We traverse $\gamma$ in counter-clockwise direction, while we traverse $\gamma_1, \dots, \gamma_k$ in clockwise direction. Then, if $M, N: D \rightarrow \mathbb{R}$ are [[Continuous Function]] [[Differentiable Function]], we have
> $$
> \begin{align}
> \int_{\partial \Omega} M dx + N dy &= \oint_{\gamma} M dx + N dy + \sum_{j = 1}^k \oint_{\gamma_j} M dx + N dy \\
> &= \int \int_{\Omega} (N_x - M_y) dx dy
> \end{align}
> $$

![[Pasted image 20260405205419.png]]

All curves in $\partial \Omega$ are traversed in the direction so that $\Omega$ stays to the left.

> [!abstract] Theorem 2 (Green's Theorem Calculus)[^1]
> Let $C$ be positively oriented (counter-clockwise), [[Piecewise Smooth Curve]], [[Simple Curve]], [[Closed Curve]], and let $D$ be the region bounded by $C$. If $P, Q$ have [[Continuous Function]] [[Partial Derivative]] on an [[Open Set|open region]] that contains $D$, then
> $$
> \begin{align}
> \int_C P dx + Q dy &= \int \int_D (\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}) dA \\
> \oint_C F \cdot dr &= \int \int_D (curl(F)) \cdot k dA \\
> \oint_C F \cdot n ds &= \int \int_D div(F(x, y)) dA
> \end{align}
> $$

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=1140)