---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Monte Carlo Estimator[^1]
> To estimate $I = \int_\Omega f(x)\,d\mu(x)$: pick a density $p$ over $\Omega$ with respect to the same [[Measure (Measure Theory)|measure]] $\mu$, draw $X \sim p$, and set
> $$
> \begin{align}
> \langle I \rangle := \frac{f(X)}{p(X)}, \qquad \mathbb{E}[\langle I \rangle] = \int_\Omega \frac{f(x)}{p(x)}\,p(x)\,d\mu(x) = \int_\Omega f(x)\,d\mu(x) = I
> \end{align}
> $$
> Averaging $N$ i.i.d. draws gives
> $$
> \begin{align}
> \langle I \rangle_N = \frac{1}{N}\sum_{n=1}^N \frac{f(x_n)}{p(x_n)}, \qquad x_n \sim p \text{ i.i.d.}
> \end{align}
> $$

This importance-sampling construction is a single cancellation between $f$ and $p$; everything else in Monte Carlo methods concerns which $p$ to use, and what happens where the cancellation is not licensed (e.g. where $p(x) = 0$ but $f(x) \neq 0$).

Every run gives a different number: "is it right?" is not a question about the number on the screen, but about the distribution of $\langle I \rangle$. That distribution can fail three independent ways: centered in the wrong place ([[Bias|bias]]), spread too wide ([[Variance|variance]]), or never settling down as $N$ grows (inconsistency). See the [[Bias-Variance-MSE Decomposition of an Estimator|bias-variance-MSE decomposition]].

# Properties
- Unbiased: $\mathbb{E}[\langle I \rangle_N] = I$ for every $N$.
- Consistent: $\langle I \rangle_N \to I$ almost surely as $N \to \infty$, by the [[Strong Law of Large Numbers]] — see [[Bias and Consistency of an Estimator]] for how bias and consistency combine in general.
- Finite variance: $\mathrm{Var}[\langle I \rangle_N] < \infty$; see [[Monte Carlo Estimator Variance]] for its closed form and when it fails.
- Estimates the [[Lebesgue Integral (Measure Theory)|Lebesgue integral]] $I = \int_\Omega f\,d\mu$, and in particular the [[Forward Problem (Simulation)|forward simulator]] $F(\theta) = \mathbb{E}[\langle F(\theta) \rangle]$.
- Converges at the dimension-independent [[Monte Carlo Convergence Rate]] $O(1/\sqrt{N})$.
- Requires $f(x) \neq 0 \implies p(x) > 0$, or else it suffers [[Zero-Density Bias (Importance Sampling)|zero-density bias]].
- Compared across techniques by [[Monte Carlo Estimator Efficiency]], not by variance alone.
- Drawing $X \sim p$ is typically done via [[Inverse Transform Sampling]] or [[Rejection Sampling]].
- Its variance can be reduced without changing $p$ via [[Stratified Sampling]] or [[Control Variates]], or by choosing $p$ close to the [[Optimal Importance Sampling Distribution]].
- Instantiated recursively by [[Path Tracing (Recursive Estimator)|path tracing]] to estimate the [[Light Transport Equation]], and by extension the [[Path Integral (Light Transport)|path integral]] over [[Path Space]].

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
