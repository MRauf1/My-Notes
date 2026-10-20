---
tags:
  - mathematics
  - real_analysis
---

# Definition
Throughout, $\alpha$ is monotonically increasing on $[a, b]$ and $\mathscr{R}(\alpha)$ is the class of functions integrable with respect to $\alpha$ ([[Riemann-Stieltjes Integral]]).

> [!abstract] Theorem 1 ([[Continuous Function]])[^1]
> If $f$ is continuous on $[a, b]$, then $f \in \mathscr{R}(\alpha)$ on $[a, b]$.

> [!abstract] Theorem 2 ([[Monotonic Function]])[^2]
> If $f$ is monotonic on $[a, b]$ and $\alpha$ is continuous on $[a, b]$, then $f \in \mathscr{R}(\alpha)$.

> [!abstract] Theorem 3 (Finitely Many [[Discontinuity|Discontinuities]])[^3]
> Suppose $f$ is bounded on $[a, b]$, $f$ has only finitely many points of discontinuity on $[a, b]$, and $\alpha$ is continuous at every point at which $f$ is discontinuous. Then $f \in \mathscr{R}(\alpha)$.

If $f$ and $\alpha$ have a common point of discontinuity, $f$ need not be in $\mathscr{R}(\alpha)$.[^4]

> [!abstract] Theorem 4 (Composition with Continuous Function)[^5]
> Suppose $f \in \mathscr{R}(\alpha)$ on $[a, b]$, $m \leq f \leq M$, $\phi$ is continuous on $[m, M]$, and $h(x) = \phi(f(x))$ on $[a, b]$. Then $h \in \mathscr{R}(\alpha)$ on $[a, b]$.

> [!abstract] Theorem 5 (Products and Absolute Values)[^6]
> If $f, g \in \mathscr{R}(\alpha)$ on $[a, b]$, then
> 1) $fg \in \mathscr{R}(\alpha)$;
> 2) $|f| \in \mathscr{R}(\alpha)$ and $\left| \int_a^b f \, d\alpha \right| \leq \int_a^b |f| \, d\alpha$.

Theorem 5 follows from Theorem 4 with $\phi(t) = t^2$ (using $4fg = (f+g)^2 - (f-g)^2$) and $\phi(t) = |t|$.

# Properties
- Special case $\alpha(x) = x$: [[Functions that are Riemann Integrable Theorem]] and [[Riemann Integral Triangle Inequality]].
- Proved via the [[Riemann-Stieltjes Integrable Theorem]] criterion; Theorem 1 uses [[Uniformly Continuous Function|uniform continuity]] on the compact $[a, b]$.
- Exactly which functions are Riemann integrable (Lebesgue's criterion): a bounded $f$ on $[a, b]$ is in $\mathscr{R}$ if and only if its set of discontinuities has [[Lebesgue Measure]] zero, i.e. $f$ is continuous almost everywhere.[^7]

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=134&annotation=PZD8W4ET)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=135&annotation=7QVQ7A5R)
[^3]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=135&annotation=5ILEKJPR)
[^4]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=136&annotation=BEKGGECT)
[^5]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=136&annotation=U564P5PI)
[^6]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=138&annotation=W4VRVI2F)
[^7]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=136&annotation=55MUIPUP)
