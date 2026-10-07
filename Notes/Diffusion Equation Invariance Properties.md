---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Diffusion Equation Invariance Properties[^1]
> If $u(\mathbf{x}, t)$ solves $u_t = k\Delta u$ on $\mathbb{R}^n$, then so do:
> 1. **Translations**: $u(\mathbf{x} - \mathbf{y}, t)$ for any fixed $\mathbf{y}$ (and $u(\mathbf{x}, t - s)$).
> 2. **Derivatives**: $u_{x_i}$, $u_t$, $u_{x_i x_j}$, etc.
> 3. **Linear combinations** of solutions (linearity).
> 4. **Integrals** of solutions: if $S$ is a solution, so is $\displaystyle v(\mathbf{x}, t) = \int_{\mathbb{R}^n} S(\mathbf{x} - \mathbf{y}, t)\, g(\mathbf{y})\, d\mathbf{y}$ for any $g$ for which the integral converges (a limiting form of 3).
> 5. **Dilations**: $u(\sqrt{a}\,\mathbf{x}, a t)$ for any $a > 0$, since $v_t = a u_t$ and $\Delta v = a \Delta u$.
>
> (In $n$-D, rotations $u(R\mathbf{x}, t)$ are also solutions, since $\Delta$ is rotation-invariant.)

The dilation property encodes the parabolic scaling $x \sim \sqrt{t}$: space and time are linked by $x^2/t$, so diffusion spreads a distance proportional to $\sqrt{kt}$, not $t$. This is the same $\sqrt{t}$ law as the [[Random Walk Mean Squared Displacement]].

# Properties
- Strategy for solving the whole-line problem: solve for one special datum (the step function, which is dilation invariant, so its solution is a function of $x/\sqrt{4kt}$ only), differentiate (2) to get the [[Diffusion Kernel (Partial Differential Equations)|diffusion kernel]], then translate and superpose (1, 4) to get $u = S * \phi$ for arbitrary $\phi$.
- Properties 1, 3, 4 hold for every linear constant-coefficient PDE ([[Superposition Principle (Partial Differential Equations)]]); 5 is specific to the parabolic scaling (the [[Wave Equation]] instead scales as $u(a\mathbf{x}, a t)$).

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=59&annotation=SMUR5FY7); [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=59&annotation=ZFBUDWPP)
