---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!abstract] Theorem 1 (Mean Value Theorem)[^1]
> Let $f$ be a [[Continuous Function]] on $[a, b]$ and [[Differentiable Function]] on $(a, b)$, then there is a number $c \in (a, b)$ such that $f'(c) = \frac{f(b) - f(a)}{b - a}$.

There is a number $c$ whose [[Tangent Line]]'s [[Slope]] is equal to the [[Slope]] of the [[Secant Line]] between $(b, f(b)), (a, f(a))$. Or in other words, the instantaneous rate of change equals the [[Average Rate of Change]] over the interval.

Generalization of [[Rolle's Theorem]].

![[Pasted image 20251017173051.png]]

> [!abstract] Theorem 2 (Generalized Mean Value Theorem)[^2]
> Let $f, g$ be [[Continuous Function]] on $[a, b]$ that are [[Differentiable Function]] on $(a, b)$. Then there exists at least one $x$ in $(a, b)$ such that
> $$
> \begin{align}
> f'(x) [g(b) - g(a)] = g'(x) [f(b) - f(a)]
> \end{align}
> $$
> We get the standard version by setting $g(x) = x$ for all $x$.

Differentiability is not required at the endpoints.[^3] Taylor's theorem ([[Taylor's Theorem]]) with $n = 1$ is exactly the mean value theorem.[^4]

# Properties
- [[Mean Value Theorem for Riemann Integral]]
- [[Fermat's Theorem]]: the key step in the proof.
- [[Monotonic Function Derivative Theorem]]
- [[Derivative Limit Theorem]]
- Fails for complex/vector-valued functions ([[Derivative of Vector-Valued Function]]); see [[Mean Value Inequality for Vector-Valued Function]] instead.

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=320)
[^2]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=250)
[^3]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=116&annotation=8MZJYNH9); [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=117&annotation=JRXLEYVB); [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=117&annotation=XSKN8EKL)
[^4]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=120&annotation=FLU8RYCZ)
