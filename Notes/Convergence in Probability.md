---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Convergence in Probability[^1]
> Let $\{X_n\}$ be a sequence of random variables and $X$ a random variable defined on the same [[Sample Space]]. $X_n$ converges in probability to $X$, written $X_n \xrightarrow{P} X$, if for all $\epsilon > 0$
> $$
> \begin{align}
> \lim_{n\to\infty} P[|X_n - X| \geq \epsilon] = 0, \quad \text{equivalently} \quad \lim_{n\to\infty} P[|X_n - X| < \epsilon] = 1
> \end{align}
> $$

> [!info] Multivariate Version[^2]
> For $p$-dimensional [[Random Vector|random vectors]] on the same sample space, $\mathbf{X}_n \xrightarrow{P} \mathbf{X}$ if $\lim_{n\to\infty} P[\lVert\mathbf{X}_n - \mathbf{X}\rVert \geq \epsilon] = 0$ for all $\epsilon > 0$, with the Euclidean [[Norm]].

The mass of the difference $X_n - X$ converges to $0$: for large $n$, $X_n$ and $X$ are close with high probability, outcome by outcome. Often the limit is a constant $a$, i.e. a [[Degenerate Distribution|degenerate]] random variable, written $X_n \xrightarrow{P} a$.

**Interpretation.** Because the definition compares $X_n(c)$ and $X(c)$ on the same outcomes $c$, convergence in probability means that as $n \to \infty$ the random variables $X_n$ and $X$ track each other so closely that they become essentially the same function on the sample space. Since they behave as the same variable, their distributions (cdfs) become the same too, which is why it implies [[Convergence in Distribution]] but not conversely.

# Properties
- For a sequence of real numbers, $a_n \to a$ is equivalent to $a_n \xrightarrow{P} a$.
- Algebra:[^1] if $X_n \xrightarrow{P} X$ and $Y_n \xrightarrow{P} Y$, then $X_n + Y_n \xrightarrow{P} X + Y$, $aX_n \xrightarrow{P} aX$ for a constant $a$, and $X_nY_n \xrightarrow{P} XY$.
- Continuous mapping:[^3] if $X_n \xrightarrow{P} a$ and $g$ is continuous at $a$, then $g(X_n) \xrightarrow{P} g(a)$; more generally, if $X_n \xrightarrow{P} X$ and $g$ is continuous, $g(X_n) \xrightarrow{P} g(X)$.
- Componentwise:[^2] $\mathbf{X}_n \xrightarrow{P} \mathbf{X}$ iff $X_{nj} \xrightarrow{P} X_j$ for every $j = 1, \dots, p$. This follows from $|v_j| \leq \lVert\mathbf{v}\rVert \leq \sum_{i=1}^p |v_i|$ for $\mathbf{v} \in \mathbb{R}^p$ (the printed upper index $n$ in Hogg's Lemma 5.4.1 should be $p$), which lets univariate results extend to vectors.
- The [[Weak Law of Large Numbers]] is the prototype: $\bar{X}_n \xrightarrow{P} \mu$. An [[Estimator]] converging in probability to its target is a [[Consistent Estimator]].
- Implies [[Convergence in Distribution]]; the converse holds when the limit is a constant.
- Weaker than almost sure convergence, which is the mode of the [[Strong Law of Large Numbers]].
- Stochastic order notation: $X_n = o_p(1)$ means $X_n \xrightarrow{P} 0$ ([[Little O]]).

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=338)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=365)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=339)
