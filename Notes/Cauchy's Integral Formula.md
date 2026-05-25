---
tags: mathematics, complex_analysis
---

# Definition

> [!abstract] Theorem 1 (Cauchy's Formula)
> Let $D$ be [[Domain (Topology)]], $f: D \rightarrow \mathbb{C}$ [[Complex Analytic Function]]. Assume that $\gamma$ is [[Simple Curve]] [[Closed Curve]] [[Piecewise Smooth Curve]] in counter-clockwise direction and $D \supseteq |\gamma| \cup \text{inside}(\gamma)$. Then, for all $z_0 \in \mathbb{C} \setminus |\gamma|$, we have
> $$
> \begin{align}
> \frac{1}{2 \pi i} \int_{\gamma} \frac{f(z)}{z - z_0} dz = \begin{cases}f(z_0) & z_0 \in \text{inside}(\gamma) \\ 0 & z_0 \in \text{outside}(\gamma)\end{cases}
> \end{align}
> $$

If $f$ is [[Complex Analytic Function]] on [[Domain (Topology)]] containing $|\gamma|$ and $\text{inside}(\gamma)$, the values of $f$ on $\text{inside}(\gamma)$ can be determined by its values on $|\gamma|$.

# Consequences

> [!abstract] Theorem 2 ([[Power Series]] Representation of [[Complex Analytic Function]] Theorem)
> If $f$ is [[Complex Analytic Function]] on [[Open Set]] $D$ and if [[Epsilon Neighborhood]] $B(z_0, R) \subseteq D$, then $f(z) = \sum_{k=0}^{\infty} a_k (z - z_0)^k$ for $z \in B(z_0, R)$, where $a_k = \frac{1}{2 \pi i} \oint_{|w - z_0| = r} \frac{f(w)}{(w - z_0)^{k + 1}} dw$, $0 < r < R$, and the [[Power Series]] has [[Radius of Convergence]] $\geq R$. Moreover, the [[Power Series]] representation is unique.

> [!abstract] Corollary 3 (Corollary)
> If $f$ is [[Complex Analytic Function]] on [[Open Set]] $D$ and $B(z_0, R) \subseteq D$, then $f$ is infinitely [[Differentiable Function]] on $D$ and the coefficients of its [[Power Series]] on $B(z_0, R)$ are
> $$
> \begin{align}
> a_k = \frac{1}{2 \pi i} \oint_{|w - z_0| = r} \frac{f(w)}{(w - z_0)^{k + 1}} dw = \frac{f^{(k)}(z_0)}{k!}
> \end{align}
> $$

> [!abstract] Corollary 4 (Corollary)
> If $f$ is [[Complex Analytic Function]] on [[Open Set]] $D$, then it is infinitely [[Differentiable Function]] on $D$.

> [!abstract] Corollary 5 (Identity Theorem)
> If $f$ is [[Complex Analytic Function]] on [[Domain (Topology)]] $D$ and for some $z_0 \in D$, $f^{(n)}(z_0) = 0$ for all $n = 0, 1, 2, \dots$, then $f = 0$ on $D$.

# Alternative Version of Identity Theorem

> [!abstract] Lemma 6 (Lemma)
> Let $D \subseteq \mathbb{C}$ be a [[Domain (Topology)]] and $f: D \rightarrow \mathbb{C}$ [[Complex Analytic Function]]. Assume that for some [[Sequence]] $(z_n)$ of distinct members of $D$ that converges to a [[Point]] $z_0 \in D$, $f(z_n) = 0$. Then $f = 0$ on $D$.

> [!abstract] Corollary 7 (Corollary)
> Let $D$ be a [[Domain (Topology)]], $f, g: D \rightarrow \mathbb{C}$. If $f = g$ on a [[Set]] that has a limit point in $D$, then $f = g$.