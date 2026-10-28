---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!abstract] Theorem 1 (Inverse Transform Sampling, Continuous)[^1]
> Given the [[Cumulative Distribution Function]] $F(a) := \mathbb{P}[X \leq a]$, draw $\xi \sim \mathcal{U}[0,1]$ and return $F^{-1}(\xi)$.
> Proof: $F$ is non-decreasing, so for any $a$,
> $$
> \begin{align}
> F^{-1}(\xi) \leq a \iff F\big(F^{-1}(\xi)\big) \leq F(a) \iff \xi \leq F(a)
> \end{align}
> $$
> hence $\mathbb{P}[X \leq a] = \mathbb{P}[\xi \leq F(a)] = F(a)$.

> [!abstract] Theorem 2 (Inverse Transform Sampling, Discrete)[^1]
> Given a cumulative mass function $F$, draw $\xi \sim \mathcal{U}[0,1]$ and return $\min\{x \in \mathbb{Z} : F(x) \geq \xi\}$, which can be computed by binary search in $O(\log N)$.

One uniform random number in, one sample out, with no wasted draws — this is the method to use whenever $F$ can be inverted. As one instance, the [[Exponential Distribution|exponential distribution]] $p(x;\lambda) = \lambda e^{-\lambda x}$ has CDF $F(x) = 1 - e^{-\lambda x}$, so inversion gives the closed form $x = -\log(1-\xi)/\lambda$ — the waiting time between events in a random walk (e.g. how far a photon travels before an interaction).

The discrete version is used to pick which sampling strategy to apply, which term of a series to estimate, which stratum to land in, or which kind of event happens next — any discrete choice weighted by probabilities.

In Hogg et al.'s formulation:[^2] if $U \sim \text{Uniform}(0, 1)$ and $F$ is a continuous cdf, then $X = F^{-1}(U)$ has cdf $F$. Generating observations from a specified distribution this way is called Monte Carlo generation; e.g. for $\Gamma(1, \beta)$, $F^{-1}(u) = -\beta\log(1 - u)$.

> [!info] Definition 1 (Generalized Inverse CDF)[^4]
> For a [[Cumulative Distribution Function|CDF]] $F$, define
> $$
> \begin{align}
> F^{-1}(u) = \inf\{x \mid F(x) \geq u\}, \quad 0 < u < 1
> \end{align}
> $$
> extended by $F^{-1}(1) = \lim_{u \to 1^-} F^{-1}(u)$ and $F^{-1}(0) = \lim_{u \to 0^+} F^{-1}(u)$, which are $\pm\infty$ for unbounded distributions such as $\mathcal{N}(0,1)$.

> [!abstract] Theorem 3 (Inversion, General)[^5]
> Let $F$ be any CDF with generalized inverse $F^{-1}$. If $U \sim \mathcal{U}(0,1)$ and $X = F^{-1}(U)$, then $X \sim F$.

The ordinary inverse breaks down in two ways:[^3] if $f = 0$ on an interval $[a, b]$, then $F$ is flat there and has no unique inverse at $u = F(a)$; and if $F$ jumps at an atom $x$, i.e. $F(x) > F(x^-)$, then no $x'$ solves $F(x') = u$ for $u \in [F(x^-), F(x))$. The generalized inverse fixes both: the set $\{x \mid F(x) \geq u\}$ is never empty and attains its infimum because $F$ is right-continuous,[^4] which yields the equivalence $F^{-1}(u) \leq x \iff u \leq F(x)$ and hence $P(X \leq x) = P(U \leq F(x)) = F(x)$. When $f > 0$ on all of $\mathbb{R}$, $F$ is continuous and strictly increasing and $F^{-1}$ is the ordinary inverse.[^3] The values $u = 0, 1$ have probability zero but can arise numerically, hence the extension.

**Complementary inversion.**[^6] Since $1 - U \sim \mathcal{U}(0,1)$, also $F^{-1}(1 - U) \sim F$; this is sometimes simpler (e.g. $X = -\log U$ for $\mathrm{Exp}(1)$, $X = \mathbf{1}\{U \leq p\}$ for $\mathrm{Bern}(p)$), but it reverses the order between $U$ and $X$, so ordinary inversion is needed when large $X$ must correspond to large $U$.

**Finite discrete case.**[^7] If $P(X = k) = p_k > 0$ for $k = 1, \dots, N$ with cumulative sums $P_k = \sum_{i=1}^k p_i$ and $P_0 = 0$, then
$$
\begin{align}
F^{-1}(u) = k \quad \text{where } P_{k-1} < u \leq P_k
\end{align}
$$
computed by tabulating $\{(k, P_k) \mid 0 \leq k \leq N\}$ and searching for $k$.

**Infinitely many values.**[^8] Tabulation is impossible, but a closed form may allow inverting a continuous CDF and truncating to an integer (e.g. the [[Geometric Distribution]] as a floored exponential), or a numerical search without tabulation if $F$ has a closed form. Sometimes numerical inversion for discrete distributions is so expensive that it erases the benefits of inversion.

**Numerical inversion.**[^9] Without a closed-form $F^{-1}$:
- If $F$ is available in closed form and continuous, solve $F(x) = u$ numerically (root finding).
- If only the density $f = F'$ is available, build an approximation to $F$ by numerical integration and invert it.
- If only the [[Characteristic Function (Probability)|characteristic function]] $\varphi(t) = \int e^{itx} f(x)\,dx$ is available, recover $f(x) = \frac{1}{2\pi}\int e^{-itx}\varphi(t)\,dt$ by Fourier inversion, then integrate to $F$ and invert.

# Properties
- The converse statement is the [[Probability Integral Transform]]: $F(X) \sim \text{Uniform}(0, 1)$.
- Related to the general [[Cumulative Distribution Function Transformation Technique]] for transforming a random variable's density, of which inversion is the special case where the transformation is the CDF itself and the input variable is $\mathcal{U}[0,1]$.
- When $F^{-1}$ has no closed form (e.g. the normal distribution requires $\mathrm{erf}^{-1}$), a dedicated transform such as the [[Box-Muller Transform]] or [[Rejection Sampling]] is used instead.
- Used to sample a [[Free-Flight Distance Sampling|free-flight distance]] in a homogeneous medium, and the cosine-weighted case underlying [[BSDF Importance Sampling]].
- The gold standard method of [[Non-Uniform Random Variate Generation]]: one uniform per variate, available in principle for every distribution, but often hard to compute.[^10]
- Because $X$ is a monotone function of a single $U$, inversion is the natural partner of [[Common Random Numbers]], [[Antithetic Variates]] and [[Stratified Sampling]].[^11]
- Generalizes to transforming between arbitrary distributions via the [[QQ Transformation]] $G^{-1}(F(X))$.
- Multivariate generalizations: [[Sequential Inversion]] (inverting conditional CDFs component by component) and [[Copula-Marginal Sampling]] (inverting marginal CDFs applied to a dependent uniform vector).
- Sampling order statistics in reverse: $Y_{(r)} = F^{-1}(X)$ with $X \sim \text{Beta}(r, n - r + 1)$ produces the $r$th [[Order Statistic]] of $n$ iid draws from $F$ with a single variate.

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=310)
[^3]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=4&annotation=ZE5I8WSV); [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=4&annotation=AY8HGU9G)
[^4]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=4&annotation=6N8FHHRN); [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=5&annotation=U87I2VDH)
[^5]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=5&annotation=2X2IUIH9)
[^6]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=6&annotation=FLYWP7LE); [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=6&annotation=LQWC4Y4N); [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=7&annotation=MYJGH23J)
[^7]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=11&annotation=ZB5YFXPE); [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=12&annotation=9EV54MH3)
[^8]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=13&annotation=VX7L6ERU); [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=13&annotation=7YIVDXDW)
[^9]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=13&annotation=36FFAK6R)
[^10]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=3&annotation=BW43RZPD); [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=4&annotation=FNDWBTRT)
[^11]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=6&annotation=YIPI2SQ8)
