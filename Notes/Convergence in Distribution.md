---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Convergence in Distribution[^1]
> Let $\{X_n\}$ be a sequence of random variables with cdfs $F_{X_n}$, and $X$ a random variable with cdf $F_X$. Let $C(F_X)$ be the set of points where $F_X$ is continuous. $X_n$ converges in distribution to $X$, written $X_n \xrightarrow{D} X$, if
> $$
> \begin{align}
> \lim_{n\to\infty} F_{X_n}(x) = F_X(x) \quad \text{for all } x \in C(F_X)
> \end{align}
> $$
> For random vectors the definition is the same with joint cdfs, at all continuity points of $F$.[^2]

The distribution of $X$ is the asymptotic (limiting) distribution of $\{X_n\}$. By convention one writes $X_n \xrightarrow{D} N(0, 1)$, putting a distribution on the right, and says "$X_n$ has a limiting standard normal distribution".[^3] Convergence is only required at continuity points of $F_X$, since at a jump of the limit the cdfs may approach from the wrong side (e.g. $X_n = 1/n$ converges to $0$, but $F_{X_n}(0) = 0 \not\to 1 = F_X(0)$).

**Interpretation.** Convergence in distribution only says that the statistical profiles (the cdfs) become the same. A single cdf can describe many different random variables, completely misaligned with each other or even defined on different sample spaces, so it does not force the random variables themselves to be close or track each other. For example, if $X \sim N(0,1)$ and $X_n = -X$ for all $n$, then $X_n \xrightarrow{D} X$ trivially, yet $|X_n - X| = 2|X|$ never shrinks. This is why it is called weak convergence, in contrast with [[Convergence in Probability]].[^3]

# Properties
- [[Convergence in Probability]] implies convergence in distribution; conversely, convergence in distribution to a constant $b$ implies convergence in probability to $b$.[^4]
- If $X_n \xrightarrow{D} X$ and $Y_n \xrightarrow{P} 0$, then $X_n + Y_n \xrightarrow{D} X$; more generally [[Slutsky's Theorem]].[^4]
- Continuous mapping:[^5] if $X_n \xrightarrow{D} X$ and $g$ is continuous on the support of $X$, then $g(X_n) \xrightarrow{D} g(X)$; the same holds for random vectors.[^2]
- MGF criterion:[^6] if the mgfs $M_{X_n}(t)$ exist on $(-h, h)$ and $\lim_n M_{X_n}(t) = M(t)$ for $|t| \leq h_1 \leq h$, where $M$ is the mgf of $X$, then $X_n \xrightarrow{D} X$. For random vectors this is an equivalence: $\mathbf{X}_n \xrightarrow{D} \mathbf{X}$ iff $M_n(\mathbf{t}) \to M(\mathbf{t})$ for all $\lVert\mathbf{t}\rVert < h$ ([[Moment Generating Function]], [[Characteristic Function (Probability)]] in general).
- A sequence converging in distribution is [[Bounded in Probability]].
- Affine maps of limiting normals:[^7] if $\mathbf{X}_n \xrightarrow{D} N_p(\boldsymbol{\mu}, \Sigma)$, then $A\mathbf{X}_n + \mathbf{b} \xrightarrow{D} N_m(A\boldsymbol{\mu} + \mathbf{b}, A\Sigma A^T)$ ([[Multivariate Normal Distribution Affine Transformation]]).
- The [[Central Limit Theorem]] is the central example; the [[Delta Method]] transfers it to smooth functions.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=343)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=367)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=344)
[^4]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=348)
[^5]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=349)
[^6]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=352)
[^7]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=368)
