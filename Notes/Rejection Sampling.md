---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Rejection Sampling[^1]
> Used when the CDF $F$ cannot be inverted, or the density $p$ cannot even be normalized. Take an envelope density $\tilde{p}$ with $p(x) \leq M\tilde{p}(x)$, and repeat:
> 1. Draw $x \sim \tilde{p}$, then $y \sim \mathcal{U}[0, M\tilde{p}(x))$.
> 2. If $y \leq p(x)$, return $x$; otherwise, go to 1.
>
> Accepted pairs $(x,y)$ are uniform under the graph of $p$, so their $x$-marginal is $p$, and the acceptance rate is $1/M$.

> [!info] Accept-Reject Algorithm[^2]
> Let $f$ be the target pdf and $g$ an instrumental pdf that is easy to sample, with $f(x) \leq Mg(x)$ for all $x$. With $Y \sim g$ and $U \sim \text{Uniform}(0, 1)$ independent:
> 1. Generate $Y$ and $U$.
> 2. If $U \leq \frac{f(Y)}{Mg(Y)}$, take $X = Y$; otherwise return to step 1.
>
> Then $X$ has pdf $f$.

> [!abstract] Theorem 1 (Acceptance-Rejection)[^4]
> Let $f$ and $g$ be probability density functions with $f(x) \leq cg(x)$ for all $x \in \mathbb{R}$ and some finite $c$, where $g$ can be sampled and $f/g$ computed. Repeatedly draw candidates $Y \sim g$ and accept $Y = y$ with probability
> $$
> \begin{align}
> A(y) = \frac{f(y)}{cg(y)}
> \end{align}
> $$
> (with $A(y) = 0$ when $g(y) = 0$). The first accepted value $X$ has density $f$.

![[Acceptance-Rejection Sampling Algorithm.png]]

Accepted candidates have density proportional to $A(y)g(y)$, and choosing $A \propto f/g$ gives $Ag \propto f$; indeed $g(y)A(y) = f(y)/c$ for all $y$.[^5] The bound $f \leq cg$ guarantees $A \leq 1$, so $g$ is unusable if $f/g$ is unbounded. The proof extends to $d$ dimensions by replacing $(-\infty, x]$ with rectangles $\prod_{j=1}^d (-\infty, x_j]$, and the method extends to discrete distributions.[^6]

> [!abstract] Theorem 2 (Geometric Interpretation)[^7]
> For a density $h$ on $\mathbb{R}$ and $M > 0$, let $S_M(h) = \{(x, z) \mid 0 \leq z \leq Mh(x),\ x \in \mathbb{R}\} \subset \mathbb{R}^2$.
> 1. If $(X, Z) \sim \mathcal{U}(S_M(h))$, then $X \sim h$.
> 2. If $X \sim h$ and $Z = Mh(X)U$ with $U \sim \mathcal{U}(0,1)$ independent of $X$, then $(X, Z) \sim \mathcal{U}(S_M(h))$.

So $(Y, cg(Y)U)$ is uniform under $cg$, and keeping only the points under $f$ leaves points uniform under $f$, whose horizontal components have density $f$.

![[Acceptance-Rejection Sampling Geometry.png]]

> [!abstract] Theorem 3 (Unnormalized Densities)[^8]
> Let $\tilde{f}(x) \geq 0$ with $0 < \int \tilde{f} < \infty$ and $\tilde{g}(x) \geq 0$ with $0 < \int \tilde{g} < \infty$, and suppose $\tilde{f}(x) \leq c\tilde{g}(x)$ for all $x$ and some $c < \infty$. Sample candidates $Y$ from the density proportional to $\tilde{g}$ and accept $Y = y$ with probability $\tilde{f}(y)/(c\tilde{g}(y))$. Then accepted values have density proportional to $\tilde{f}$, and the acceptance probability is
> $$
> \begin{align}
> \frac{\mathrm{vol}(S_{c_f}(f))}{\mathrm{vol}(S_{c c_g}(g))} = \frac{c_f}{c\,c_g}, \qquad c_f = \int \tilde{f}, \quad c_g = \int \tilde{g}
> \end{align}
> $$

This covers e.g. a well-known density restricted to a set whose probability is unknown.

**Multivariate case.**[^11] For a density $f$ on $\mathbb{R}^d$, find a density $g$ that can be sampled with $f(\mathbf{x}) \leq cg(\mathbf{x})$ for a known $c < \infty$, and run the same algorithm with vectors in place of scalars; on average $c$ draws from $g$ are needed per delivered sample. The geometry also carries over: with the $(d+1)$-dimensional region
$$
\begin{align}
S_c(f) = \{(\mathbf{x}, z) \mid 0 \leq z \leq cf(\mathbf{x}),\ \mathbf{x} \in \mathbb{R}^d\}
\end{align}
$$
$(\mathbf{X}, Z) \sim \mathcal{U}(S_c(f))$ implies $\mathbf{X} \sim f$, and conversely $\mathbf{X} \sim f$ with $Z \mid \mathbf{X} = \mathbf{x} \sim \mathcal{U}(0, cf(\mathbf{x}))$ implies $(\mathbf{X}, Z) \sim \mathcal{U}(S_c(f))$. Hence unnormalized $\tilde{f} \leq c\tilde{g}$ with acceptance probability $A(\mathbf{y}) = \tilde{f}(\mathbf{y})/(c\tilde{g}(\mathbf{y}))$ also work in $d$ dimensions.

In high dimensions the method degrades:[^12] finding $c = \sup_{\mathbf{x}} f(\mathbf{x})/g(\mathbf{x})$ becomes a $d$-dimensional optimization, and, more critically, $c$ is hard to keep small; e.g. the volume mismatch between cubes and balls grows strongly with $d$ ([[Curse of Dimensionality]]). It still works when the connection between $f$ and $g$ is inherently low-dimensional: for a radially symmetric $f$, accept-reject on the radius combined with a uniform direction on the unit [[Sphere|sphere]] has a constant $c$ coming only from the one-dimensional radius part.[^13]

# Properties
- The probability of acceptance is $1/M$, so the number of trials per sample is geometric with mean $M$; choose $M$ as small as possible.[^3]
- Normalizing constants can be ignored:[^3] if $f = kh$ and $g = ct$, then $f \leq Mg$ iff $h \leq M_2 t$ with $M_2 = cM/k$, and the test becomes $U \leq h(Y)/[M_2 t(Y)]$.
- Pro: needs only pointwise evaluations of $p$, and only up to a normalizing constant.
- Con: wastes samples, and $M$ grows brutally with dimension; use it only when [[Inverse Transform Sampling]] is unavailable.
- Made fast for monotone densities by the [[Ziggurat Algorithm]]; in high dimensions, [[Markov Chain Monte Carlo]] replaces it.
- With normalized densities the acceptance probability is $1/c$, so the number $N$ of proposals per accepted value is geometric, $P(N = k) = c^{-1}(1 - c^{-1})^{k-1}$, with $E(N) = c$.[^6]
- The optimal constant is $c = \sup_{x : f(x) > 0} f(x)/g(x)$, and always $c \geq 1$ since $1 = \int f \leq \int cg = c$.[^9]
- Speedups: [[Squeeze Function (Rejection Sampling)|squeeze functions]] that skip evaluating $f$, and [[Adaptive Rejection Sampling]] for log-concave $f$.
- The same "accept with probability proportional to target over proposal" idea yields the acceptance rule of the [[Metropolis-Hastings Algorithm]].[^5]
- One family of [[Non-Uniform Random Variate Generation]], used when no computable transformation of a fixed number of uniforms produces $F$.[^10]

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=314)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=315)
[^4]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=21&annotation=D62K8ER4); [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=22&annotation=GWAKI537); [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=22&annotation=N3A4IB4U)
[^5]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=22&annotation=V39QFNII); [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=22&annotation=GWAKI537)
[^6]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=22&annotation=TF5ACID2)
[^7]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=23&annotation=PW5INLE4); [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=23&annotation=LIDT2BSK); [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=24&annotation=P7776P9E)
[^8]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=25&annotation=Q49JTBHL); [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=25&annotation=2GRIFC7N); [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=25&annotation=ZW8D38MX)
[^9]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=23&annotation=M44ZYTGH)
[^10]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=21&annotation=D62K8ER4)
[^11]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/I5B7ZUIV?page=5&annotation=ZA9GZT3L); [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/I5B7ZUIV?page=5&annotation=E5PBKAP5); [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/I5B7ZUIV?page=5&annotation=RMZ9XWFB); [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/I5B7ZUIV?page=6&annotation=N9YJ226P)
[^12]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/I5B7ZUIV?page=6&annotation=UVPZ2FJU); [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/I5B7ZUIV?page=6&annotation=8JWWRUDK)
[^13]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/I5B7ZUIV?page=6&annotation=WJN9PNIY); [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/I5B7ZUIV?page=7&annotation=WE8PTKMF)
