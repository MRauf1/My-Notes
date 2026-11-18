---
tags:
  - mathematics
  - real_analysis
---

# Definition
> [!abstract] Theorem 1 (Length of $C^1$ Curve)[^1]
> If $\gamma$ is a [[Curve (Real Analysis)|curve]] on $[a, b]$ and $\gamma'$ is continuous on $[a, b]$, then $\gamma$ is [[Rectifiable Curve|rectifiable]] and
> $$
> \begin{align}
> \Lambda(\gamma) = \int_a^b |\gamma'(t)| \, dt
> \end{align}
> $$

# Properties
- Proof: the [[Riemann-Stieltjes Integral of Vector-Valued Function|vector-valued triangle inequality]] gives $|\gamma(x_i) - \gamma(x_{i-1})| = \left|\int_{x_{i-1}}^{x_i} \gamma'\right| \leq \int_{x_{i-1}}^{x_i} |\gamma'|$, so $\Lambda(\gamma) \le \int_a^b |\gamma'|$. For the reverse inequality, [[Uniformly Continuous Function|uniform continuity]] of $\gamma'$ makes $|\gamma'(t)| \le |\gamma'(x_i)| + \varepsilon$ on each fine subinterval.
- Justifies the [[Curve Arc Length]] formula of differential geometry.

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=146&annotation=HADZH62H)
