---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!info] Definition 1 (Space of Bounded Continuous Functions $\mathscr{C}(X)$)[^1]
> If $X$ is a [[Metric Space]], $\mathscr{C}(X)$ denotes the [[Set]] of all complex-valued, [[Continuous Function|continuous]], [[Bounded Function|bounded]] functions with domain $X$. Each $f \in \mathscr{C}(X)$ is associated with its [[Supremum Norm]]
> $$
> \begin{align}
> \lVert f \rVert = \sup_{x \in X} |f(x)|
> \end{align}
> $$
> and the distance between $f, g \in \mathscr{C}(X)$ is defined as $\lVert f - g \rVert$, which makes $\mathscr{C}(X)$ a [[Metric Space]].[^2]

Boundedness is redundant if $X$ is [[Compact Metric Space|compact]] ([[Continuous Function Compact Metric Space Theorem]]), so $\mathscr{C}(X)$ consists of all complex continuous functions on $X$ if $X$ is compact.[^1]

> [!abstract] Theorem 2 (Completeness of $\mathscr{C}(X)$)[^3]
> The [[Supremum Norm]] metric makes $\mathscr{C}(X)$ into a [[Complete Metric Space]].

Convergence in this metric is *exactly* [[Sequence of Function Uniform Convergence|uniform convergence]]: $\lVert f_n - f \rVert = \sup_{x \in X}|f_n(x) - f(x)| = M_n$, and $f_n \rightarrow f$ uniformly if and only if $M_n \rightarrow 0$. Pointwise convergence is not convergence in this metric (pointwise convergence is not induced by any norm on $\mathscr{C}(X)$ in general).[^2]

Hence the terminology: [[Closed Set|closed]] subsets of $\mathscr{C}(X)$ are called **uniformly closed** (they contain every uniform limit of their members), and the [[Closure Set|closure]] of $\mathcal{A} \subseteq \mathscr{C}(X)$ is called its **uniform closure** (the set of all uniform limits of sequences in $\mathcal{A}$).[^2]

## Relation to $L^p$ Spaces
- $\mathscr{C}(X)$ is a [[Banach Space]] (a complete [[Normed Space]]). The supremum norm is the continuous-function analogue of the $L^\infty$ (essential supremum) norm: for continuous functions on e.g. $[a, b]$ with [[Lebesgue Measure]], $\lVert f \rVert_{L^\infty} = \sup |f|$, so $\mathscr{C}([a, b])$ sits isometrically as a closed subspace of $L^\infty([a, b])$.
- For $1 \leq p < \infty$, $\mathscr{C}([a, b])$ is *not* complete under the $L^p$ norm $\lVert f \rVert_p = \left(\int |f|^p\right)^{1/p}$; it is [[Dense Subset|dense]] in $L^p([a, b])$, and $L^p$ is its completion ([[Completion of Metric Space]]).
- Uniform convergence on a bounded interval implies $L^p$ convergence, but not conversely.

# Properties
- Every uniformly convergent sequence of bounded functions is [[Sequence of Function Uniformly Bounded|uniformly bounded]].
- Compact subsets are characterized by the [[Arzelà-Ascoli Theorem]].
- Dense subalgebras are characterized by the [[Stone-Weierstrass Theorem]].
- Every metric space $X$ embeds isometrically into $\mathscr{C}(X)$, which yields the [[Completion of Metric Space]].

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=159&annotation=ZDDY4MLQ)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=160&annotation=5AM33AFB)
[^3]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=160&annotation=LD6DNFSB)
