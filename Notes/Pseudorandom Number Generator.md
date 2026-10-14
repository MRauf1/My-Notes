---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Pseudorandom Number Generator[^1]
> A pseudorandom number generator (PRNG) is a deterministic algorithm with a finite internal state $s \in \mathcal{S}$ that, on each call `rand()`, performs
> $$
> \begin{align}
> s &\leftarrow \mathrm{update}(s) \\
> x &= f(s)
> \end{align}
> $$
> and returns $x$, a simulated draw from the [[Standard Uniform Distribution]] $U(0,1)$. Successive outputs $x_1, x_2, \dots$ are meant to behave like [[Independent and Identically Distributed|i.i.d.]] $U(0,1)$ random variables.

In practice, [[Monte Carlo Method|Monte Carlo]] uses pseudorandom numbers instead of genuinely random ones from a [[Physical Random Number Generator]].[^2] Because pseudorandom numbers dominate practice, they are usually just called "random numbers".[^3]

**Advantages over physical randomness.**[^2]
- **Reproducibility:** restarted in the same state, a PRNG re-delivers the same output, so a simulation can be rerun after changing parameters or fixing a bug ([[Random Number Generator Seed]]).
- **Storage:** only the code and a small state need to be stored, whereas a truly random sequence is incompressible and would have to be stored in full to be replayed.
- **Speed:** PRNGs produce numbers far faster than physical sources.

**Caveat.** No PRNG perfectly simulates genuine randomness, so an application may *resonate* with some flaw of the generator and give a misleading Monte Carlo answer.[^3] Safeguards: recompute the answer with two or more generators of quite different design, or test the generator on a version of the problem whose answer is known exactly.

# Properties
- Since $\mathcal{S}$ is finite, the state sequence eventually revisits a previous state and the output becomes periodic ([[Random Number Generator Period]]).
- Fully determined by its starting state, which is set through a [[Random Number Generator Seed]].
- Complex simulations need several mutually independent-looking [[Random Number Streams]].
- **Predictability:** the most widely used Monte Carlo generators are simple recursions; observing a sequence of outputs often lets one infer the internal state and predict future values.[^4] Such generators are unsuitable for cryptography (which needs a cryptographically secure PRNG), though this is harmless for Monte Carlo sampling.
- Its output lives on the floating-point unit interval rather than the mathematical one ([[Standard Uniform Distribution]], [[Floating-Point Number System]]).
- Supplies the uniform inputs that [[Inverse Transform Sampling]], the [[Box-Muller Transform]], etc. turn into non-uniform variates.

[^1]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/GBISVAQW?page=5&annotation=4RWW2SHJ)
[^2]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/GBISVAQW?page=3&annotation=R4D7VJPV); [Owen](zotero://open-pdf/library/items/GBISVAQW?page=3&annotation=YJVFYI8J); [Owen](zotero://open-pdf/library/items/GBISVAQW?page=4&annotation=T4BNIG3N); [Owen](zotero://open-pdf/library/items/GBISVAQW?page=4&annotation=BR52ELD7)
[^3]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/GBISVAQW?page=4&annotation=AWVEZ9AS)
[^4]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/GBISVAQW?page=4&annotation=EG3ERFSI)
