---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Schrödinger Equation[^1]
> The complex-valued wave function $u(\mathbf{x}, t)$ of a particle of mass $m$ in a potential $V(\mathbf{x})$ satisfies, on all of space $\mathbb{R}^3$,
> $$
> \begin{align}
> i\hbar \, u_t = -\frac{\hbar^2}{2m} \Delta u + V(\mathbf{x}) u, \qquad \iiint_{\mathbb{R}^3} |u|^2 \, d\mathbf{x} = 1,
> \end{align}
> $$
> where $\hbar$ is Planck's constant divided by $2\pi$ and $\Delta$ is the [[Laplacian Operator]]. For an electron (charge $-e$) about a nucleus of atomic number $Z$ at the origin (hydrogen: $Z = 1$), $V = -\dfrac{Z e^2}{r}$ in Gaussian units ($-\dfrac{Z e^2}{4\pi\varepsilon_0 r}$ in SI), $r = |\mathbf{x}|$.

# Properties
- Linear, homogeneous, first order in time and second order in space, with complex coefficient $i$.
- Needs one [[Initial Condition]] $u(\mathbf{x}, t_0) = \phi(\mathbf{x})$.
- Posed on all of space, so there is no boundary; the normalization $\int |u|^2 = 1$ replaces [[Boundary Condition|boundary conditions]] and makes $|u|^2$ a [[Probability Density Function]] of the particle's position.
- On an interval $u_t = i u_{xx}$ separates into $T = e^{-i\lambda t}$ times the same spatial [[Eigenfunction|eigenfunctions]] as diffusion, e.g. $u = \tfrac12 A_0 + \sum A_n e^{-i(n\pi/l)^2 t}\cos\frac{n\pi x}{l}$ with Neumann conditions ([[Separation of Variables]]).[^2]

- **Time-independent form.** For a state of definite energy $E$, $u = \psi(\mathbf{x})e^{-iEt/\hbar}$, and $\big(-\tfrac{\hbar^2}{2m}\Delta + V\big)\psi = E\psi$: an eigenvalue problem for the Hamiltonian. In free space ($V = 0$) its solutions include the [[Plane Wave|plane waves]] $e^{i\mathbf{k}\cdot\mathbf{x}}$ with $E = \hbar^2|\mathbf{k}|^2/2m$, i.e. de Broglie wavelength $\lambda = h/p$ ([[Wave-Particle Duality]]).
- **Born rule**: $|u|^2$ is the probability density of detecting the particle, which for a beam is the measured intensity.
- **High-energy (paraxial) form, used in electron microscopy.** For a fast electron (charge $-e$, potential energy $-eV$ in an electrostatic potential $V$) travelling along $z$, write $\psi = e^{ikz}u$ and neglect $\partial_z^2 u$, since the envelope varies slowly on the scale of $\lambda$:
$$
\begin{align}
\partial_z u = \frac{i}{2k}\nabla_\perp^2 u + i\sigma V u, \qquad \sigma = \frac{me}{\hbar^2 k} = \frac{2\pi m e\lambda}{h^2},
\end{align}
$$
with relativistically corrected $m$ and $\lambda$; $\sigma$ is the interaction constant ([[Projection Approximation]]). This "time-like" evolution in $z$ is a Schrödinger equation in two transverse dimensions, and it is the propagation step of the [[Cryo-EM Forward Model]].

# Questions
> [!question]- Derive the paraxial equation $\partial_z u = \frac{i}{2k}\nabla_\perp^2 u + i\sigma Vu$ from the time-independent equation.
> With potential energy $-eV$: $-\frac{\hbar^2}{2m}\Delta\psi - eV\psi = E\psi$, i.e. $\Delta\psi + k^2\psi + \frac{2me}{\hbar^2}V\psi = 0$ with $k^2 = 2mE/\hbar^2$. Substituting $\psi = e^{ikz}u$ gives $\Delta\psi = e^{ikz}\big(\nabla_\perp^2 u + \partial_z^2 u + 2ik\,\partial_z u - k^2u\big)$. So
> $$
> \begin{align}
> \nabla_\perp^2 u + \partial_z^2 u + 2ik\,\partial_z u + \frac{2me}{\hbar^2}Vu = 0.
> \end{align}
> $$
> Dropping $\partial_z^2 u$ (slowly varying envelope, $|\partial_z^2 u| \ll k|\partial_z u|$) and dividing by $2ik$: $\partial_z u = \frac{i}{2k}\nabla_\perp^2 u + i\frac{me}{\hbar^2 k}Vu$.

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=29&annotation=QB56EPAP)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=104&annotation=XLES3PT5)
