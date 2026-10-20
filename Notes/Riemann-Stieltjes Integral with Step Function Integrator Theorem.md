---
tags:
  - mathematics
  - real_analysis
---

# Definition
Let $I$ be the unit step function ([[Heaviside Function]] in Rudin's convention): $I(x) = 0$ for $x \leq 0$ and $I(x) = 1$ for $x > 0$.

> [!abstract] Theorem 1 (Single Jump)[^1]
> If $a < s < b$, $f$ is bounded on $[a, b]$, $f$ is continuous at $s$, and $\alpha(x) = I(x - s)$, then
> $$
> \begin{align}
> \int_a^b f \, d\alpha = f(s)
> \end{align}
> $$

> [!abstract] Theorem 2 (Countably Many Jumps)[^2]
> Suppose $c_n \geq 0$ for $n = 1, 2, 3, \dots$, $\sum c_n$ converges, $(s_n)$ is a sequence of distinct points in $(a, b)$, and
> $$
> \begin{align}
> \alpha(x) = \sum_{n=1}^\infty c_n I(x - s_n)
> \end{align}
> $$
> Let $f$ be continuous on $[a, b]$. Then
> $$
> \begin{align}
> \int_a^b f \, d\alpha = \sum_{n=1}^\infty c_n f(s_n)
> \end{align}
> $$

A function $\alpha$ of this form is called a pure step function. With such an integrator, the [[Riemann-Stieltjes Integral]] reduces to a finite or infinite [[Series]]; with a differentiable integrator it reduces to a [[Riemann Integral]] ([[Riemann-Stieltjes Integral with Differentiable Integrator Theorem]]). This makes it possible to study series and integrals simultaneously, rather than separately.[^3]

# Properties
- Theorem 1 is the rigorous form of the sifting property $\int f(x)\,\delta(x - s)\,dx = f(s)$ of the [[Dirac Delta Function]], with $d\alpha$ playing the role of $\delta(x - s)\,dx$.
- With $c_n = p_X(s_n)$, $\alpha$ is the [[Cumulative Distribution Function]] of a [[Discrete Random Variable]] and Theorem 2 gives $E[f(X)] = \sum f(s_n) p_X(s_n)$.
- Continuity of $f$ at the jump is needed: if $f$ and $\alpha$ share a discontinuity, $f$ need not be integrable ([[Functions that are Riemann-Stieltjes Integrable Theorem]]).

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=139&annotation=YEDTX7MZ)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=139&annotation=SDB3SMCN)
[^3]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=141&annotation=PX55TL9S)
