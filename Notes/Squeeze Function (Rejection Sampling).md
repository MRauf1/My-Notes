---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Squeeze Function[^1]
> In [[Rejection Sampling|acceptance-rejection sampling]] with acceptance probability $A(y) = f(y)/(cg(y))$, a lower squeeze is a cheaply computed function $L$ with $L(y) \leq A(y)$ for all $y$. Given the candidate $Y = y \sim g$ and $U = u \sim \mathcal{U}(0,1)$:
> 1. If $u \leq L(y)$, accept immediately without evaluating $f(y)$.
> 2. Otherwise accept iff $u \leq A(y)$.
>
> An upper squeeze $H(y) \geq A(y)$ rejects immediately when $u > H(y)$.

![[Acceptance-Rejection Sampling with Squeeze Algorithm.png]]

The output distribution is unchanged, since every early decision agrees with the exact test; only the expensive evaluation of $f$ (often a single call to $\log$, $\exp$ or $\cos$, which still costs far more than plain arithmetic) is avoided.

# Properties
- The running time of acceptance-rejection is proportional to $c$ times the cost of generating and testing one proposal; a squeeze lowers the testing cost.
- The probability that $L$ decides a proposal is the fraction of the area under $(x, A(x))$ that also lies under $(x, L(x))$; a good $L$ lies just barely below $A$.
- A lower squeeze pays off more than an upper one: a proposal lands under $f$ with probability $1/c$ and above it with probability $1 - 1/c$, so when $c \approx 1$ there are few rejections for $H$ to speed up.
- Squeezes can be cascaded, $L_1 \leq \dots \leq L_s \leq A \leq H_r \leq \dots \leq H_1$, but one well-chosen lower bound is usually all that is used.
- Built into [[Adaptive Rejection Sampling]]; the fast path of the [[Ziggurat Algorithm]] is a squeeze.

[^1]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=26&annotation=CY5P8Y22)
