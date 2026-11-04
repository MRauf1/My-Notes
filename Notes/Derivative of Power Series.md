---
tags:
  - mathematics
  - calculus
---

# Definition

> [!abstract] Theorem 1 ([[Derivative]] of [[Power Series]])[^1]
> If $f(x) = \sum_{n=0}^{\infty} c_n (x - a)^n$ has [[Radius of Convergence]] $R > 0$, then $f$ is [[Differentiable Function|differentiable]] on $(a - R, a + R)$ and can be differentiated term by term:
> $$
> \begin{align}
> f'(x) = \frac{d}{dx}\left[\sum_{n=0}^{\infty} c_n (x - a)^n\right] = \sum_{n=0}^{\infty} \frac{d}{dx}[c_n (x - a)^n] = \sum_{n=1}^{\infty} n c_n (x - a)^{n-1}
> \end{align}
> $$
> The differentiated series has the same radius of convergence $R$.

Term-by-term differentiation is special to power series (inside the radius of convergence). For a general [[Infinite Series]] of functions it can fail.

# Properties
- **Radius preserved, endpoints not.** Differentiation keeps the [[Radius of Convergence]] $R$, but convergence at the endpoints $x = a \pm R$ can be lost, so the [[Interval of Convergence]] can shrink. Endpoints must be rechecked separately. Differentiation never *gains* an endpoint: at $x - a = \pm R$, $c_n (x-a)^n = (x - a) \cdot \frac{1}{n} \cdot n c_n (x-a)^{n-1}$, so if the derivative series converges there, so does the original (by Abel's test, since $\frac1n$ is monotone and bounded).
- Counterpart: [[Integral of Power Series]] also preserves $R$, but can only *gain* endpoints.
- Follows from the [[Power Series Convergence Theorem]].

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=786)
