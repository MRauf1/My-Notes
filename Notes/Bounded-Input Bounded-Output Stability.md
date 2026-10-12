---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Bounded-Input Bounded-Output Stability[^1]
> A filter is **stable** if every bounded input produces a bounded output: for every input with $|\ell_{in}[n, m, t]| < A$ there exists $B$ such that $|\ell_{out}[n, m, t]| < B$.

# Properties
- **Criterion for LTI filters**:[^2] a [[Shift-Invariant System|LTI]] filter is stable iff its [[Impulse Response|impulse response]] is absolutely summable,
$$
\begin{align}
\sum_{n, m, t} |h[n, m, t]| < \infty, \qquad \text{in which case } |\ell_{out}| \leq A \sum_{n, m, t} |h[n, m, t]|
\end{align}
$$
  The source states only that the impulse response must be bounded; boundedness is necessary but not sufficient (e.g. the accumulator $h[t] = u[t]$ is bounded, yet a constant input yields an unbounded output).
- Every FIR filter (finite-support kernel) is stable; stability is a concern for [[Infinite Impulse Response Filter|IIR filters]], whose impulse response may diverge.
- The first-order recursion $\ell_{out}[t] = \ell_{in}[t] + \alpha \ell_{out}[t - 1]$ is stable iff $|\alpha| < 1$.

[^1]: [MIT Vision Book - Temporal Filters](https://visionbook.mit.edu/temporal_filters_v2.html)
[^2]: Added from general knowledge; corrects the source's statement.
