---
tags: [mathematics, complex_analysis]
---

# Definition

> [!abstract] Theorem 1 (Cauchy's Theorem)
> Let $\gamma$ be [[Simple Curve]] [[Closed Curve]] [[Piecewise Smooth Curve]], $f$ [[Complex Analytic Function]] on $D$, and $D \supseteq |\gamma| \cup \text{inside}(\gamma)$. Then
> $$
> \begin{align}
> \int_{\gamma} f(z) dz = 0
> \end{align}
> $$
> More generally, if $\Omega$ is [[Domain (Topology)]] as in [[Green's Theorem]], and $f$ is [[Complex Analytic Function]] on [[Open Set]] $D \supseteq \Omega \cup \partial \Omega$, then
> $$
> \begin{align}
> \int_{\partial \Omega} f(z) dz = \oint_{\gamma} f(z) dz + \sum_{j = 1}^k \oint_{\gamma_j} f(z) dz = 0
> \end{align}
> $$
> where $\partial \Omega$ is traversed as in [[Green's Theorem]] and the [[Piecewise Smooth Curve]] $\gamma_1, \dots, \gamma_k$ are inside $\gamma$.