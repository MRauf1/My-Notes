---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!abstract] Theorem (Pointwise Convergence of Classical Fourier Series)[^1]
> 1. The classical Fourier series (full, sine, or cosine) of $f$ converges to $f(x)$ pointwise on $(a, b)$ provided that $f$ is continuous on $[a, b]$ and $f'$ is [[Piecewise Continuous Function|piecewise continuous]] on $[a, b]$.
> 2. More generally, if $f$ and $f'$ are only piecewise continuous on $[a, b]$, then the classical Fourier series converges at every point $x \in \mathbb{R}$, with sum
> $$
> \begin{align}
> \sum_n A_n X_n(x) &= \tfrac12\left[f(x^+) + f(x^-)\right] \quad \text{for all } a < x < b, \\
> \sum_n A_n X_n(x) &= \tfrac12\left[f_{\text{ext}}(x^+) + f_{\text{ext}}(x^-)\right] \quad \text{for all } -\infty < x < \infty,
> \end{align}
> $$
> where $f_{\text{ext}}$ is the extended function.

> [!abstract] Theorem (Whole-Line Form)[^2]
> If $f$ has period $2l$ on $\mathbb{R}$ and $f$, $f'$ are piecewise continuous, then the classical full [[Fourier Series]] converges to $\tfrac12[f(x^+) + f(x^-)]$ for all $-\infty < x < \infty$.

At a [[Jump Discontinuity]] the series converges to the average of the one-sided limits. The extension is the [[Odd Extension|odd]] (sine series) or [[Even Extension|even]] (cosine series) $2l$-periodic extension of $f$ on $(0, l)$, or the [[Periodic Extension]] (full series) of $f$ on $(-l, l)$; it is again piecewise continuous with piecewise continuous derivative, which is why the two statements are equivalent.[^3]

# Properties
- Intermediate in its hypotheses between the [[Fourier Series Uniform Convergence Theorem]] and the [[Fourier Series L2 Convergence Theorem]].[^4]
- Continuity of $f$ alone is not enough: something must be known about $f'$.[^5]
- Proved by writing the partial sum as a convolution with the [[Dirichlet Kernel]]; near a jump the convergence is not uniform ([[Gibbs Phenomenon]]).[^6]
- Classical form of Dirichlet's 1829 theorem; the hypothesis on $f'$ can be relaxed to bounded variation (Dirichlet–Jordan) or a Dini/Hölder condition.[^7]

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=141&annotation=D56N8AEG)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=141&annotation=W8XEVNQ4)
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=141&annotation=ATBT3T4K)
[^4]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=140&annotation=V7FA2XSL)
[^5]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=142&annotation=4N9KBAS6)
[^6]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=148&annotation=BJL3E8L3)
[^7]: Added from general knowledge.
