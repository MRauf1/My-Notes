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

# Properties
- The standard use is replacing an unknown parameter by a [[Consistent Estimator]]: from the [[Central Limit Theorem]], $\sqrt{n}(\bar{X} - \mu)/\sigma \xrightarrow{D} N(0,1)$, and since $S_n \xrightarrow{P} \sigma$, also $\sqrt{n}(\bar{X} - \mu)/S_n \xrightarrow{D} N(0, 1)$. This justifies large-sample [[Confidence Interval|confidence intervals]] $\bar{x} \pm z_{\alpha/2}s/\sqrt{n}$ and explains why the [[t-Distribution]] approaches $N(0,1)$.
- The limits of $A_n$ and $B_n$ must be constants: if they converge only in distribution, the joint behavior with $X_n$ is not determined.
- The special case $B_n = 1$, $A_n \xrightarrow{P} 0$ says an asymptotically negligible term does not change a limiting distribution; it is also a key step in the proof of the [[Delta Method]].

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=349)
