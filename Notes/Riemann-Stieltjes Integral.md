---
tags:
  - mathematics
  - real_analysis
---

# Definition
> [!info] Definition 1 (Riemann-Stieltjes Integral)[^1]
> Let $\alpha$ be a [[Monotonic Function|monotonically increasing]] function on $[a, b]$ (so $\alpha$ is [[Bounded Function|bounded]], since $\alpha(a), \alpha(b)$ are finite). For a [[Partition]] $P = \{x_0, \dots, x_n\}$ of $[a, b]$, write
> $$
> \begin{align}
> \Delta \alpha_i = \alpha(x_i) - \alpha(x_{i-1}) \geq 0
> \end{align}
> $$
> For any real [[Bounded Function]] $f$ on $[a, b]$, with $M_i = \sup_{[x_{i-1}, x_i]} f$ and $m_i = \inf_{[x_{i-1}, x_i]} f$, define the upper and lower sums
> $$
> \begin{align}
> U(P, f, \alpha) = \sum_{i=1}^n M_i \Delta \alpha_i, \qquad L(P, f, \alpha) = \sum_{i=1}^n m_i \Delta \alpha_i
> \end{align}
> $$
> and the upper and lower integrals
> $$
> \begin{align}
> \overline{\int_a^b} f \, d\alpha = \inf_P U(P, f, \alpha), \qquad \underline{\int_a^b} f \, d\alpha = \sup_P L(P, f, \alpha)
> \end{align}
> $$
> with the $\inf$ and $\sup$ taken over all partitions of $[a, b]$. If they are equal, their common value
> $$
> \begin{align}
> \int_a^b f \, d\alpha = \int_a^b f(x) \, d\alpha(x)
> \end{align}
> $$
> is the Riemann-Stieltjes integral (or Stieltjes integral) of $f$ with respect to $\alpha$ over $[a, b]$. We then say $f$ is integrable with respect to $\alpha$ in the Riemann sense and write $f \in \mathscr{R}(\alpha)$.

Taking $\alpha(x) = x$ recovers the [[Riemann Integral]] (in its [[Darboux Integral|upper/lower sum]] form), written $f \in \mathscr{R}$. In general, $\alpha$ need not even be continuous.[^2]

The integral depends on $f$, $\alpha$, $a$, $b$, but not on the variable of integration, which plays the same role as the index of summation in $\sum_{i=1}^n c_i$: $\int_a^b f(x)\,d\alpha(x) = \int_a^b f(y)\,d\alpha(y)$. It may be omitted, though inserting it is often convenient.[^3]

Intuitively, $\alpha$ is a cumulative weighting ("measuring stick") that says how much mass is assigned to each region of $[a, b]$; $\Delta\alpha_i$ replaces the length $\Delta x_i$. Changing $\alpha$ changes the value of the integral:
- $\alpha(x) = x$: every subinterval is weighted by its length (the [[Riemann Integral]]).
- $\alpha$ with integrable derivative: $d\alpha = \alpha'(x)\,dx$, so $\alpha'$ acts as a density/weight function ([[Riemann-Stieltjes Integral with Differentiable Integrator Theorem]]).
- $\alpha$ with jumps: each jump concentrates a point mass, so the integral picks up $f(s) \cdot (\text{jump at } s)$, turning integrals into (finite or infinite) series ([[Riemann-Stieltjes Integral with Step Function Integrator Theorem]]). This is the rigorous counterpart of the sifting property of the [[Dirac Delta Function]].
- $\alpha = F_X$ a [[Cumulative Distribution Function]]: $\int g \, dF_X = E[g(X)]$ ([[Expectation]]), covering discrete, continuous, and mixed distributions with one formula.

$\alpha(x) = x$ is the "default" choice in physics because Euclidean space is homogeneous (translation-invariant): a displacement $dx$ is weighted the same everywhere. Non-uniform weightings still appear, but are usually absorbed into the integrand as a density $\rho = \alpha'$, a Jacobian/volume element ([[Change of Variables]]), or a Dirac delta, rather than written as $d\alpha$.

# Types
- [[Riemann Integral]] ($\alpha(x) = x$)
- [[Riemann-Stieltjes Integral of Vector-Valued Function]]

# Properties
- [[Refinement of Partition]] and [[Darboux Sums of 2 Partitions Lemma]]: refining increases $L$ and decreases $U$; hence $\underline{\int} f\,d\alpha \leq \overline{\int} f\,d\alpha$.
- For every $P$, $m[\alpha(b) - \alpha(a)] \leq L(P, f, \alpha) \leq U(P, f, \alpha) \leq M[\alpha(b) - \alpha(a)]$ where $m \leq f \leq M$, so upper and lower integrals exist for every bounded $f$.
- [[Riemann-Stieltjes Integrable Theorem]] (Cauchy-type criterion)
- [[Functions that are Riemann-Stieltjes Integrable Theorem]]
- [[Riemann-Stieltjes Integral Basic Properties]]
- [[Riemann-Stieltjes Integral with Step Function Integrator Theorem]]
- [[Riemann-Stieltjes Integral with Differentiable Integrator Theorem]]
- [[Riemann-Stieltjes Integral Change of Variable Theorem]]
- [[Hölder's Inequality]] holds for $\int \cdot \, d\alpha$.
- Generalized further by the [[Lebesgue Integral (Measure Theory)|Lebesgue integral]] with respect to the Lebesgue-Stieltjes measure $\mu((x, y]) = \alpha(y) - \alpha(x)$.

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=131&annotation=6NKAP77G)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=131&annotation=74VDQ2GZ)
[^3]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=132&annotation=6W6WYB38)
