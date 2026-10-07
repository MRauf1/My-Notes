---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Slutsky's Theorem[^1]
> Let $X_n, X, A_n, B_n$ be random variables and $a, b$ constants. If $X_n \xrightarrow{D} X$, $A_n \xrightarrow{P} a$, and $B_n \xrightarrow{P} b$, then
> $$
> \begin{align}
> A_n + B_n X_n \xrightarrow{D} a + bX
> \end{align}
> $$

Sequences converging in probability to constants can be treated as those constants inside a limit in distribution ([[Convergence in Distribution]], [[Convergence in Probability]]).

Owen's form:[^2] if $Y_n \xrightarrow{D} Y$ and $Z_n \xrightarrow{D} \tau$ for a constant $\tau$, then $Y_n + Z_n \xrightarrow{D} Y + \tau$, $Y_nZ_n \xrightarrow{D} \tau Y$, and, if $\tau \neq 0$, $Y_n/Z_n \xrightarrow{D} Y/\tau$ (convergence in distribution to a constant is equivalent to convergence in probability). More generally, $g(Y_n, Z_n) \xrightarrow{D} g(Y, \tau)$ for continuous $g$ (Knight, 2000, Ch. 3).

Plug-in CLT:[^3] with $0 < \sigma < \infty$, $\sqrt{n}(\bar{Y} - \mu)/\sigma \xrightarrow{D} N(0,1)$ and $s/\sigma \xrightarrow{D} 1$, so
$$
\begin{align}
\sqrt{n}\,\frac{\bar{Y} - \mu}{s} = \frac{\sqrt{n}(\bar{Y} - \mu)/\sigma}{s/\sigma} \xrightarrow{D} \frac{N(0,1)}{1} = N(0,1)
\end{align}
$$
which justifies the [[Monte Carlo Confidence Interval]].

# Properties
- The standard use is replacing an unknown parameter by a [[Consistent Estimator]]: from the [[Central Limit Theorem]], $\sqrt{n}(\bar{X} - \mu)/\sigma \xrightarrow{D} N(0,1)$, and since $S_n \xrightarrow{P} \sigma$, also $\sqrt{n}(\bar{X} - \mu)/S_n \xrightarrow{D} N(0, 1)$. This justifies large-sample [[Confidence Interval|confidence intervals]] $\bar{x} \pm z_{\alpha/2}s/\sqrt{n}$ and explains why the [[t-Distribution]] approaches $N(0,1)$.
- The limits of $A_n$ and $B_n$ must be constants: if they converge only in distribution, the joint behavior with $X_n$ is not determined.
- The special case $B_n = 1$, $A_n \xrightarrow{P} 0$ says an asymptotically negligible term does not change a limiting distribution; it is also a key step in the proof of the [[Delta Method]].

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=349)
[^2]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=40&annotation=Y2BP3PPI); [Owen](zotero://open-pdf/library/items/TXMSRRI3?page=40&annotation=854WR79L)
[^3]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=40&annotation=4NINES96); [Owen](zotero://open-pdf/library/items/TXMSRRI3?page=41&annotation=W9I3YA6S)
