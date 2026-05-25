---
tags: mathetatics, calculus
---

# Definition

> [!info] Definition 1 (Continuous [[Function]])[^1]
> [[Function]] $f$ is continuous at $a$ if
> 1) $f(a)$ is defined ($a$ is in the [[Domain]] of $f$)
> 2) $\lim_{x \rightarrow a} f(x)$ exists
> 3) $\lim_{x \rightarrow a} f(x) = f(a)$
> Alternatively, $f$ is continuous at $a$ if, for every [[Sequence]] $(x_n)$ in the [[Domain]] of $f$, $\lim_{n \rightarrow \infty} f(x_n) = f(a)$

If a function is continuous at $a$, then the [[Limit of Function Direct Substitution Property]] can be applied to the function.

If a function is continuous at every point of its domain, then the graph of the function has no gaps.

> [!info] Definition 2 (Epsilon-Delta Definition of Continuity)[^2]
> $f$ is continuous at $a$ if and only if for each $\epsilon > 0$, there exists $\delta > 0$ such that
> $$
> \begin{align}
> (x \in Domain(f) \land |x - a| < \delta) \implies |f(x) - f(a)| < \epsilon
> \end{align}
> $$

> [!info] Definition 3 (Continuous [[Function]] for [[Real-Valued Function]])[^1]
> [[Function]] $f$ is continuous at $\mathbf{a}$ if
> 1) $f(\mathbf{a})$ is defined ($\mathbf{a}$ is in the [[Domain]] of $f$)
> 2) $\lim_{\mathbf{x} \rightarrow \mathbf{a}} f(\mathbf{x})$ exists
> 3) $\lim_{\mathbf{x} \rightarrow \mathbf{a}} f(\mathbf{x}) = f(\mathbf{a})$

> [!info] Definition 4 (Continuous [[Function]] on [[Metric Space]])[^3]
> Given [[Metric Space]] $(S_1, d_1), (S_2, d_2)$, a [[Function]] $f: S_1 \rightarrow S_2$ is continuous at $s_0$ if for each $\epsilon > 0$, there exists $\delta > 0$ such that
> $$
> \begin{align}
> d_1(s, s_0) < \delta \implies d_2(f(s), f(s_0)) < \epsilon
> \end{align}
> $$

# Examples
## Continuous at Every Number in Their Domain
- [[Polynomial Function]]
- [[Rational Function]]
- [[Nth Root]] [[Function]]
- [[Trigonometric Function]]
- [[Inverse Trigonometric Function]]
- [[Exponential Function]]
- [[Logarithm Function]]

# Types
- [[One-Sided Continuous Function]]
- [[Continuous Function on Interval]]
- [[Piecewise Continuous Function]]

# Properties
- [[Continuous Function Inverse]]
- [[Continuous Function Strictly Increasing Inverse Theorem]]
- [[Continuous Function Composition]]
- [[Intermediate Value Theorem]]

## Arithmetic Properties
- [[Continuous Function Addition Rule]]
- [[Continuous Function Subtraction Rule]]
- [[Continuous Function Scalar Product Rule]]
- [[Continuous Function Product Rule]]
- [[Continuous Function Quotient Rule]]
- [[Continuous Function Absolute Value Rule]]
- [[Continuous Function Composition Rule]]

## [[Bounded Set]]
- [[Continuous Function Bounded Theorem]]

## [[Topology]]
- [[Continuous Function on Metric Space Theorem]]
- [[Continuous Function Compact Metric Space Theorem]]

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=147)
[^2]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=135)
[^3]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=175)