---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Random Number Generator Period[^1]
> Let $x_i \leftarrow$ `rand()` for $i \geq 1$ be the outputs of a [[Pseudorandom Number Generator]]. If the generator's state when $x_{i_0}$ is produced equals its state when $x_{i_0 - P}$ was produced, then
> $$
> \begin{align}
> x_i = x_{i-P} \quad \text{for all } i \geq i_0,
> \end{align}
> $$
> so from $i_0$ on the generator is a deterministic cycle with **period** $P$. Under the simplifying assumption of a fixed period, $x_{i+P} = x_i$ for all $i$.

A period must exist because the state variable has finite size: the generator cannot run forever without revisiting a state, after which it repeats values it already delivered.[^1] Some generators cycle with different periods depending on their starting state.

# Properties
- **$\sqrt{P}$ guideline:** do not use more than about $\sqrt{P}$ random numbers from a given generator.[^2] (Interpretation: among $n$ genuinely random draws from $P$ equally likely values, repeats are expected once $n \approx \sqrt{P}$ by the birthday argument, while a full-period generator never repeats within a period, so beyond roughly $\sqrt{P}$ draws its non-randomness becomes detectable.)
- A generator with state space $\mathcal{S}$ has $P \leq |\mathcal{S}|$. Modern generators (e.g. the Mersenne Twister, $P = 2^{19937} - 1$) have periods so large that the guideline is rarely binding.
- Related: [[Random Number Generator Seed]], [[Random Number Streams]].

[^1]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/GBISVAQW?page=5&annotation=LNLA9VQ7); [Owen](zotero://open-pdf/library/items/GBISVAQW?page=5&annotation=YGJSS4E4)
[^2]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/GBISVAQW?page=5&annotation=CBW4JJCT)
