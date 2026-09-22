---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Interchange of Differentiation and Expectation[^1]
> Differentiating a Monte Carlo estimator is not, in general, the same as estimating the derivative:
> $$
> \begin{align}
> \frac{d}{d\theta}\mathbb{E}[X_\theta] \neq \mathbb{E}\left[\frac{d}{d\theta}X_\theta\right]
> \end{align}
> $$
> Exchanging the derivative and the expectation requires regularity that a general parametrized random variable $X_\theta$ does not have.

Equality holds when the pointwise derivative $\frac{d}{d\theta}X_\theta$ exists and is dominated by an integrable random variable uniformly in a neighborhood of $\theta$ — the hypothesis of the [[Dominated Convergence Theorem]] applied to the difference quotients $\frac{X_{\theta+h}-X_\theta}{h}$. Continuity of $X_\theta$ in $\theta$ alone is not sufficient to license the exchange.

What breaks the domination hypothesis in Monte Carlo simulation is a term supported on the set where the integrand jumps discontinuously in $\theta$ (e.g. a visibility boundary in [[Forward Problem (Simulation)|rendering or particle transport]]). This set has [[Measure (Measure Theory)|measure]] zero, which is exactly why i.i.d. sampling from the forward distribution never lands on it, and exactly why its contribution to the true derivative is nevertheless not small. Recovering this missing term is the [[Reynolds Transport Theorem|boundary term]] of the Leibniz rule for a moving domain.

# Properties
- One of the [[Five Obstacles to Differentiating Monte Carlo Estimators|five obstacles]] to differentiating a Monte Carlo simulator.

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
