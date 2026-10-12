---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Causal Filter[^1]
> A [[Spatio-Temporal Filter|filter]] whose output depends only on present and past values of the input. Equivalently, its [[Impulse Response|impulse response]] satisfies
> $$
> \begin{align}
> h[n, m, t] = 0 \quad \text{for all } t < 0
> \end{align}
> $$
> so an impulse at $t = 0$ produces non-zero output only for $t \geq 0$.

# Types
- **Causal**: $h[n, m, t] = 0$ for all $t < 0$; output depends only on the past (and present).
- **Non-causal**: the output depends on future inputs.
- **Anti-causal**: the output depends only on the future, $h[n, m, t] = 0$ for all $t > 0$.

# Properties
- The condition on $h$ is necessary and sufficient: since $\ell_{out}[t] = \sum_\tau h[t - \tau]\ell_{in}[\tau]$, the terms with $\tau > t$ vanish for every input iff $h[t'] = 0$ for $t' < 0$.[^2]
- Many filters are non-causal with both causal and anti-causal components, e.g. the [[Spatio-Temporal Gaussian Filter|temporal Gaussian]], which is symmetric in $t$.
- Non-causal filters cannot be implemented in real time (on streamed signals). They are approximated by a causal filter by **bounding the temporal support and shifting the impulse response in time**, at the cost of an output delay equal to the shift. Offline (e.g. a video stored in memory) this is unnecessary.
- Causality is a constraint only in time; spatial filters have no preferred direction.[^2]
- Making a symmetric (zero-phase) filter causal by shifting adds a linear phase ([[Fourier Shift Theorem]]).[^2]

[^1]: [MIT Vision Book - Temporal Filters](https://visionbook.mit.edu/temporal_filters_v2.html)
[^2]: Added from general knowledge.
