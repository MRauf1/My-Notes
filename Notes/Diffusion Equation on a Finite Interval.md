---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Diffusion Equation on a Finite Interval[^1][^2][^3]
> By [[Separation of Variables]], $u_t = k u_{xx}$ on $0 < x < l$, $t > 0$, with $u(x, 0) = \phi(x)$, is solved by an eigenfunction series whose modes decay exponentially at rates set by the eigenvalues.
>
> **Dirichlet** ($u(0, t) = u(l, t) = 0$):
> $$
> \begin{align}
> u(x, t) = \sum_{n=1}^\infty A_n e^{-(n\pi/l)^2 k t}\sin\frac{n\pi x}{l}, \qquad \phi(x) = \sum_{n=1}^\infty A_n \sin\frac{n\pi x}{l}.
> \end{align}
> $$
> **Neumann** ($u_x(0, t) = u_x(l, t) = 0$):
> $$
> \begin{align}
> u(x, t) = \frac12 A_0 + \sum_{n=1}^\infty A_n e^{-(n\pi/l)^2 k t}\cos\frac{n\pi x}{l}, \qquad \phi(x) = \frac12 A_0 + \sum_{n=1}^\infty A_n \cos\frac{n\pi x}{l}.
> \end{align}
> $$
> For each $t$ the solution is a [[Fourier Sine Series|sine]] / [[Fourier Cosine Series|cosine]] series in $x$ provided the initial data are.

**Long-time behavior.** Every Neumann term except the first decays exponentially, so $u \to \tfrac12 A_0$, a constant: insulated ends make the substance spread out evenly.[^4][^5] (Passing to the limit term by term requires a convergence theorem.) In the Dirichlet case every term decays and $u \to 0$. With Robin conditions the bottom eigenvalue can be negative and $u$ can grow ([[Robin Eigenvalue Problem on an Interval]]).

**Energy, Parseval, and decay.**[^6] Note that the *eigenvalues* are fixed numbers; what decays are the modal *amplitudes* $A_n e^{-k\lambda_n t}$, each at rate $k\lambda_n$. By orthogonality ([[Parseval's Theorem]] for the cosine basis, $\|1\|^2 = l$, $\|\cos\frac{n\pi x}{l}\|^2 = \frac l2$), in the Neumann case
$$
\begin{align}
\|u(t)\|_{L^2}^2 &= \frac{l}{4}A_0^2 + \frac{l}{2}\sum_{n=1}^\infty A_n^2 e^{-2k\lambda_n t}, \\
D[u(t)] = \int_0^l u_x^2\, dx &= \frac{l}{2}\sum_{n=1}^\infty \lambda_n A_n^2 e^{-2k\lambda_n t}, \qquad \lambda_n = \left(\frac{n\pi}{l}\right)^2,
\end{align}
$$
where $D$ is the [[Dirichlet Energy]]: the spectrum diagonalizes both the mass and the energy. Consequences:
- $\frac{d}{dt}\tfrac12\|u\|^2 = -k\, D[u] \le 0$: diffusion is the $L^2$ gradient flow of $k D$, dissipating energy (the opposite of [[Wave Equation Energy Conservation]]); $D[u(t)]$ itself is nonincreasing.
- The zero mode is untouched: $\tfrac12 A_0 = \frac1l\int_0^l\phi$ is the conserved total amount, and the factor $\tfrac12$ is exactly what makes it the mean.
- **Spectral gap.** $\|u(t) - \tfrac12 A_0\|_{L^2} \le e^{-k\pi^2 t/l^2}\|\phi - \tfrac12 A_0\|_{L^2}$; the equilibration rate is $k\lambda_1$, the first nonzero eigenvalue (Poincaré–Wirtinger constant). In the Dirichlet case, $\|u(t)\| \le e^{-k\pi^2 t/l^2}\|\phi\|$.
- **Smoothing.** Rates $k\lambda_n \propto n^2$ kill high frequencies fastest, so $A_n e^{-k\lambda_n t}$ decays faster than any power of $n$ for $t > 0$ and $u$ is $C^\infty$ ([[Diffusion Equation Smoothing Theorem]]); run backward, the factors $e^{+k\lambda_n t}$ explode ([[Diffusion Equation Well-Posedness]]).

# Properties
- Uses the [[Dirichlet Eigenvalue Problem on an Interval]] and [[Neumann Eigenvalue Problem on an Interval]]; Robin and mixed conditions work the same way with $T_n = A_n e^{-\lambda_n k t}$.
- The solution operator is the heat semigroup $e^{-ktA}$ of $A = -d^2/dx^2$; its integral kernel $\sum_n e^{-k\lambda_n t}\hat X_n(x)\hat X_n(y)$ is the heat kernel of the interval, the finite-interval counterpart of the [[Diffusion Kernel (Partial Differential Equations)|diffusion kernel]] (and equal to its sum over [[Method of Reflection|reflected images]]).[^6]
- Finite-interval counterpart of [[Diffusion Equation on the Half-Line]]; the corresponding wave problem is [[Wave Equation on a Finite Interval]].

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=99&annotation=KWTNU2A5)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=99&annotation=442X4GJB)
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=102&annotation=C5GJDYGC)
[^4]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=102&annotation=YTAVV624)
[^5]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=103&annotation=7P2GB4L3)
[^6]: Energy/Parseval/spectral-gap connections added from general knowledge.
