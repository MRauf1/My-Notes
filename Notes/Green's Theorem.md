---
tags: [mathematics, complex_analysis]
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