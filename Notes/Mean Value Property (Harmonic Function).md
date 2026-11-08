---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Mean Value Property (Harmonic Function)[^1]
> Let $u$ be a [[Harmonic Function]] in a disk $D$, continuous on its closure. Then the value of $u$ at the center equals its average over the circumference:
> $$
> \begin{align}
> u(\mathbf{x}_0) = \frac{1}{2\pi a}\oint_{|\mathbf{x} - \mathbf{x}_0| = a} u \, ds .
> \end{align}
> $$

**General case.**[^2] If $\Delta u = 0$ in an open set containing the closed ball $\bar B(\mathbf{x}_0, a) \subset \mathbb{R}^n$, then $u(\mathbf{x}_0)$ equals the average of $u$ over the sphere $\partial B(\mathbf{x}_0, a)$ and also over the ball $B(\mathbf{x}_0, a)$. Conversely, a continuous function with the mean value property on all small spheres is harmonic.

# Generalizations
> [!abstract] Generalization 1 (Sub- and Superharmonic Functions; the Laplacian as Deviation from the Mean)[^3]
> If $u \in C^2(U)$ and $\Delta u \geq 0$ (subharmonic), then for every closed ball $\bar B(x, r) \subset U$,
> $$
> \begin{align}
> u(x) \leq \frac{1}{|\partial B(x,r)|}\int_{\partial B(x,r)} u \, dS, \qquad u(x) \leq \frac{1}{|B(x,r)|}\int_{B(x,r)} u \, dy,
> \end{align}
> $$
> with the inequalities reversed for superharmonic functions ($\Delta u \leq 0$). More precisely, for any $u \in C^2$,
> $$
> \begin{align}
> \frac{1}{|\partial B(x,r)|}\int_{\partial B(x,r)} u \, dS = u(x) + \frac{r^2}{2n}\,\Delta u(x) + o(r^2) \quad (r \to 0),
> \end{align}
> $$
> so $\Delta u(x)$ measures how far $u(x)$ is from its spherical averages. On a Riemannian manifold the same leading-order expansion holds over geodesic spheres, with the Laplace–Beltrami operator in place of $\Delta$.

Proof idea: $\phi(r) = \frac{1}{|\partial B(x,r)|}\int_{\partial B(x,r)} u\,dS$ satisfies $\phi'(r) = \frac{r}{n}\frac{1}{|B(x,r)|}\int_{B(x,r)} \Delta u\,dy$ and $\phi(0^+) = u(x)$. A sign on $\Delta u$ gives monotonicity, and Taylor expanding $\Delta u$ about $x$ gives the expansion.

> [!abstract] Generalization 2 (Heat Equation: Mean Value over Heat Balls)[^3]
> Let $\Phi(x, t) = (4\pi t)^{-n/2} e^{-|x|^2/(4t)}$ be the heat kernel, and define the **heat ball**
> $$
> \begin{align}
> E(x, t; r) = \left\{(y, s) \in \mathbb{R}^{n+1} : s \leq t,\ \Phi(x - y, t - s) \geq r^{-n}\right\}.
> \end{align}
> $$
> If $u_t = \Delta u$ in $U_T$ and $E(x, t; r) \subset U_T$, then
> $$
> \begin{align}
> u(x, t) = \frac{1}{4r^n}\iint_{E(x,t;r)} u(y, s)\,\frac{|x - y|^2}{(t - s)^2}\,dy\,ds.
> \end{align}
> $$
> The average is weighted and lies entirely in the past of $(x, t)$, matching the time direction of the [[Maximum Principle (Diffusion Equation)]]. It gives the strong maximum principle for the [[Heat Equation]] the same way the spherical mean gives it for [[Harmonic Function|harmonic functions]].

> [!abstract] Generalization 3 (Variable-Coefficient Elliptic Operators: Probabilistic Mean Value)[^4]
> Let $\mathcal{A} = \tfrac12\sum_{i,j} a^{ij}(x)\partial_{ij} + \sum_i b^i(x)\partial_i$ (with $a = \sigma\sigma^\top$) be the generator of the diffusion $dX_t = b(X_t)\,dt + \sigma(X_t)\,dW_t$. Let $U$ be bounded with exit time $\tau$ satisfying $\mathbb{E}_x[\tau] < \infty$. If $\mathcal{A}u = 0$ in $U$ and $u \in C^2(U) \cap C(\bar U)$, then by Dynkin's formula
> $$
> \begin{align}
> u(x) = \mathbb{E}_x\big[u(X_\tau)\big].
> \end{align}
> $$
> For $\mathcal{A} = \tfrac12\Delta$, $X$ is [[Brownian Motion]], and for $U = B(x, r)$ the exit position is uniformly distributed on the sphere by rotation invariance. That is exactly the spherical mean value property. For general $\mathcal{A}$, the exit distribution from a ball (the *harmonic measure* of $\mathcal{A}$) is not uniform, so no fixed averaging kernel exists. This representation, together with the **Harnack inequality** $\sup_V u \leq C\inf_V u$ for nonnegative solutions on $V \subset\subset U$, takes over the role of the mean value property.[^5]

The exact spherical mean value property is therefore special to the Laplacian: it encodes the rotation invariance of $\Delta$, i.e. of Brownian motion. For the heat equation it survives as a weighted average over heat balls. For general elliptic operators only the probabilistic average and Harnack-type inequalities remain. Hyperbolic equations have no averaging property at all, since they transport rather than smooth.

# Properties
- Proof: set $r = 0$ in [[Poisson's Formula]], where the [[Poisson Kernel]] is identically $1$ (or note $u(0) = \tfrac12 A_0$ in the [[Laplace Equation in a Disk|series solution]]).[^1]
- Implies the strong [[Maximum Principle (Laplace Equation)]]: an interior maximum forces $u$ to equal the maximum on every small circle, hence on the connected domain.[^2]
- Basis of the [[Walk on Spheres]] Monte Carlo solver. Generalization 3 is why walk-on-spheres is specific to $\Delta$: with variable coefficients, the exit distribution from a sphere is no longer uniform, and one must simulate the diffusion itself.
- Analogue of the [[Mean Value Theorem]] in spirit only: it is an averaging identity, not a derivative identity.[^2]

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=181&annotation=9CCS3ZDT)
[^2]: Added from general knowledge.
[^3]: [Partial Differential Equations, 2nd ed. (Evans, AMS GSM 19)](https://bookstore.ams.org/gsm-19-r), §2.2.2–2.2.3 and §2.3.2.
[^4]: [Stochastic Differential Equations: An Introduction with Applications, 6th ed. (Øksendal)](https://doi.org/10.1007/978-3-642-14394-6), Ch. 7 and 9.
[^5]: [Elliptic Partial Differential Equations of Second Order (Gilbarg, Trudinger)](https://doi.org/10.1007/978-3-642-61798-0), Ch. 8–9 (Harnack inequalities of Moser and Krylov–Safonov).
