---
tags:
  - mathematics
  - real_analysis
---

# Definition
> [!info] Definition 1 (Uniformly Differentiable Function)[^1]
> A function $f$ is uniformly differentiable on $[a, b]$ if for every $\varepsilon > 0$ there exists $\delta > 0$ such that
> $$
> \begin{align}
> \left| \frac{f(t) - f(x)}{t - x} - f'(x) \right| < \varepsilon
> \end{align}
> $$
> whenever $0 < |t - x| < \delta$, $a \leq x \leq b$, $a \leq t \leq b$.

A single $\delta$ works for all $x$, by analogy with [[Uniformly Continuous Function]] vs. [[Continuous Function]].

# Properties
- If $f'$ is continuous on $[a, b]$, then $f$ is uniformly differentiable on $[a, b]$.[^1] This also holds for vector-valued functions ([[Derivative of Vector-Valued Function]]).

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=123&annotation=TKDN4TH9); [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=124&annotation=D3BEMFX4)
