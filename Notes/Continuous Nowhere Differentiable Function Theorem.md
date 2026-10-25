---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!abstract] Theorem 1 (Continuous Nowhere [[Differentiable Function]] Theorem)[^1]
> There exists a real [[Continuous Function]] on the real line which is nowhere [[Differentiable Function|differentiable]].

Such a function is constructed as a [[Sequence of Function Uniform Convergence|uniformly convergent]] [[Infinite Series]] of continuous functions (via the [[Weierstrass M-Test]]), so it is continuous by the [[Uniform Limit of Continuous Functions Theorem]], while the derivatives of the partial sums blow up. The classical example is Weierstrass's function $W(x) = \sum_{n=0}^{\infty} a^n \cos(b^n \pi x)$ with $0 < a < 1$, $b$ an odd integer, and $ab > 1 + \tfrac{3\pi}{2}$.[^2]

# Properties
- Uniform convergence does not preserve differentiability; compare [[Uniform Limit of Derivatives Theorem]].
- Continuous nowhere differentiable functions are "typical": they form a residual set in the [[Space of Bounded Continuous Functions]] $\mathcal{C}([a, b])$, by the [[Baire Category Theorem]].

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=163&annotation=YAK4YAZ8)
[^2]: [Weierstrass function - Wikipedia](https://en.wikipedia.org/wiki/Weierstrass_function)
