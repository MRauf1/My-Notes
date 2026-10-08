---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Separation of Variables[^1][^2]
> To solve a [[Homogeneous Linear Partial Differential Equation]] with homogeneous [[Boundary Condition|boundary conditions]] on a bounded interval $0 < x < l$, look for **separated solutions**
> $$
> \begin{align}
> u(x, t) = X(x)\, T(t)
> \end{align}
> $$
> of the PDE and the boundary conditions, then build the general solution as a (possibly infinite) linear combination of them, choosing the coefficients to match the [[Initial Condition|initial data]]. Substituting $XT$ into $u_t = k u_{xx}$ or $u_{tt} = c^2 u_{xx}$ and dividing by $XT$ makes each side depend on one variable only, so both equal a constant $-\lambda$:
> $$
> \begin{align}
> -X'' = \lambda X \quad (\text{plus the boundary conditions on } X), \qquad T' = -\lambda k T \ \ \text{or} \ \ T'' = -\lambda c^2 T.
> \end{align}
> $$
> The spatial problem is an [[Eigenfunction|eigenvalue problem]]; if $\{\lambda_n, X_n\}$ is the complete list of its eigenvalues and eigenfunctions, then[^3][^4]
> $$
> \begin{align}
> u(x, t) = \sum_n T_n(t) X_n(x), \qquad T_n(t) = \begin{cases} A_n e^{-\lambda_n k t} & \text{(diffusion)}, \\ A_n \cos(\sqrt{\lambda_n}\, c t) + B_n \sin(\sqrt{\lambda_n}\, c t) & \text{(waves)}, \end{cases}
> \end{align}
> $$
> provided the initial data can be expanded in the $X_n$: $\phi = \sum A_n X_n$ (and, for waves, $\psi = \sum \sqrt{\lambda_n}\, c\, B_n X_n$).

**Temporal factors for non-positive eigenvalues.** For $\lambda = 0$ the factors become $T = A$ (diffusion) and $T = A + Bt$ (waves).[^5] For $\lambda = -\gamma^2 < 0$ they become $A e^{+\gamma^2 k t}$ (diffusion) and $A e^{\gamma c t} + B e^{-\gamma c t}$ (waves): a single negative eigenvalue makes the solution grow exponentially, for diffusion and waves alike.[^6][^7]

**Why completeness matters.** It is critically important to find *all* the eigenvalues: if even one were missing, there would be initial data that the series could not represent, and the problem could not be solved.[^8] How the eigenvalues are indexed ($\lambda_0$, $\lambda_1$, ...) is immaterial, but a consistent numbering helps display their dependence on parameters.

**Spectral reading.** The method is the [[Spectral Theorem]] in disguise. The spatial operator $A = -d^2/dx^2$ with homogeneous boundary conditions is symmetric on $L^2(0, l)$, so its eigenfunctions form an orthogonal basis and the PDE $u_t = -kAu$ (or $u_{tt} = -c^2 A u$) decouples into one scalar [[Ordinary Differential Equation]] per eigenfunction. The solution is a function of the operator applied to the data, exactly like [[Function of a Matrix|$f(A)$ for a diagonalizable matrix]]:[^9]
$$
\begin{align}
u(t) = e^{-ktA}\phi = \sum_n e^{-k\lambda_n t} \langle \phi, \hat X_n \rangle \hat X_n, \qquad u(t) = \cos\!\big(ct\sqrt{A}\big)\phi + \frac{\sin\!\big(ct\sqrt{A}\big)}{c\sqrt{A}}\psi,
\end{align}
$$
with $\hat X_n = X_n / \|X_n\|$. Diffusion damps mode $n$ at rate $k\lambda_n$; waves oscillate mode $n$ at angular frequency $c\sqrt{\lambda_n}$; the [[Schrödinger Equation]] $u_t = i u_{xx}$ rotates mode $n$ by the phase $e^{-i\lambda_n t}$ (with Neumann conditions, $u = \tfrac12 A_0 + \sum_{n \ge 1} A_n e^{-i(n\pi/l)^2 t}\cos\frac{n\pi x}{l}$),[^10] a [[Unitary Matrix|unitary]] evolution that preserves $\|u\|_{L^2}$.

# Properties
- Relies on the [[Superposition Principle (Partial Differential Equations)]]: finite sums of separated solutions are solutions; the infinite sums require convergence theory ([[Fourier Series]]).
- Building blocks by boundary condition: [[Dirichlet Eigenvalue Problem on an Interval]] (sines, [[Fourier Sine Series]]), [[Neumann Eigenvalue Problem on an Interval]] (cosines, [[Fourier Cosine Series]]), [[Mixed Eigenvalue Problem on an Interval]], [[Robin Eigenvalue Problem on an Interval]].
- Applications: [[Diffusion Equation on a Finite Interval]], [[Wave Equation on a Finite Interval]].
- Long-time behavior and stability are read off the bottom of the spectrum: diffusion decays iff $\lambda_{\min} > 0$, tends to a steady state iff $\lambda_{\min} = 0$, and blows up exponentially iff $\lambda_{\min} < 0$.[^9]
- The same template works in higher dimensions with $A = -\Delta$ ([[Laplacian Operator]]) and on graphs with the [[Graph Laplacian Matrix]], where the eigenvectors are a graph Fourier basis.[^9]

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=96&annotation=868XTIZX)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=96&annotation=H7NA23AL)
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=110&annotation=PM2ECJV9)
[^4]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=111&annotation=8GFH64YG)
[^5]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=103&annotation=MW3XQS2X)
[^6]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=111&annotation=ZUVVITAR)
[^7]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=112&annotation=E56ANY6G)
[^8]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=110&annotation=CG4Z52VJ)
[^9]: Spectral-theory connections added from general knowledge.
[^10]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=104&annotation=XLES3PT5)
