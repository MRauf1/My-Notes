---
tags:
  - mathematics
  - complex_analysis
---

# Definition
> [!info] Complex Exponential Function[^1]
> For $z \in \mathbb{C}$, the [[Exponential Function|exponential]] is defined by its [[Power Series]]:
> $$
> \begin{align}
> e^z = \exp(z) = \sum_{n=0}^{\infty} \frac{z^n}{n!} = 1 + z + \frac{z^2}{2!} + \frac{z^3}{3!} + \cdots
> \end{align}
> $$
> The series converges absolutely for every $z$ (infinite radius of convergence, by the [[Power Series Ratio Test|ratio test]]), and on $\mathbb{R}$ it agrees with the real exponential $e^x$. For $z = x + iy$,
> $$
> \begin{align}
> e^{x + iy} = e^x\big(\cos y + i \sin y\big).
> \end{align}
> $$

The properties of the real exponential carry over to complex arguments; the most famous instance is [[Euler's Identity]], $e^{i\theta} = \cos\theta + i\sin\theta$.

# Properties
- **Product rule**: $e^{z + w} = e^z e^w$ for all $z, w \in \mathbb{C}$.
- **First-order approximation**: $e^z = 1 + z + O(|z|^2)$ as $z \to 0$, so $e^z \approx 1 + z$ for small $|z|$.
- **Modulus and argument**: $|e^{z}| = e^{\operatorname{Re} z}$ and $\arg e^{z} = \operatorname{Im} z$ (mod $2\pi$); in particular $|e^{i\theta}| = 1$ ([[Absolute Value of Complex Number]]).
- **Never zero**: $e^z e^{-z} = e^0 = 1$, so $e^z \neq 0$.
- **Periodic with period $2\pi i$**: $e^{z + 2\pi i} = e^z$. As a function of real $\theta$, $e^{i\theta}$ is $2\pi$-periodic, and its graph $\theta \mapsto (\theta, \cos\theta, \sin\theta)$ is a helix.
- **Polar form**: every $z \neq 0$ is $z = |z|\, e^{i\arg z}$ ([[Complex Number in Polar Coordinates]]).
- **Conjugation**: $\overline{e^z} = e^{\bar z}$ ([[Complex Conjugate]]), since the series has real coefficients.

# Questions
> [!question]- Prove $e^{z+w} = e^z e^w$ from the series.
> Both series converge absolutely, so their [[Cauchy Product]] converges to the product:
> $$
> \begin{align}
> e^z e^w = \sum_{n=0}^{\infty} \sum_{k=0}^{n} \frac{z^k}{k!}\frac{w^{n-k}}{(n-k)!} = \sum_{n=0}^{\infty} \frac{1}{n!}\sum_{k=0}^{n}\binom{n}{k} z^k w^{n-k} = \sum_{n=0}^{\infty} \frac{(z+w)^n}{n!} = e^{z+w}.
> \end{align}
> $$
> The middle step is the [[Binomial Theorem]], which needs $zw = wz$ (true in $\mathbb{C}$). Absolute convergence (of at least one factor) is what licenses the Cauchy product.

> [!question]- Derive Euler's identity from the power series.
> Put $z = i\theta$ and split even and odd $n$. Since $i^{2m} = (-1)^m$ and $i^{2m+1} = (-1)^m i$,
> $$
> \begin{align}
> e^{i\theta} = \sum_{m=0}^{\infty} \frac{(-1)^m\theta^{2m}}{(2m)!} + i\sum_{m=0}^{\infty}\frac{(-1)^m\theta^{2m+1}}{(2m+1)!} = \cos\theta + i\sin\theta.
> \end{align}
> $$
> Splitting the series into two is valid because it converges absolutely.

> [!question]- Connection: Which property of $e^z$ fails for the [[Matrix Exponential]], and why?
> Dictionary: $z \mapsto A$ (a square matrix), same series $e^A = \sum_n A^n/n!$, which converges absolutely for every $A$; $|e^z| = e^{\operatorname{Re} z} \mapsto \|e^A\| \le e^{\|A\|}$. The product rule becomes $e^{A+B} = e^A e^B$ **only if $AB = BA$**: the Cauchy-product proof above uses the binomial theorem, which needs commutativity. Where it breaks: for non-commuting $A, B$, the correction is given by Duhamel's formula ([[Duhamel's Principle]]) or the Baker–Campbell–Hausdorff series. This is the same commutation condition that decides whether a propagator $\exp(\Delta t\,L)$ factors along a basis.

[^1]: [Sigworth, p. 2](zotero://open-pdf/library/items/6DH254TU?page=2&annotation=SBH4BIJL)
