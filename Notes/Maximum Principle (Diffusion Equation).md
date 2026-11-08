---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Maximum Principle (Diffusion Equation)[^1][^2]
> **Weak form.** If $u$ satisfies the [[Diffusion Equation]] $u_t = k u_{xx}$ in the rectangle $0 \le x \le l$, $0 \le t \le T$, then the maximum of $u$ over the rectangle is attained on the bottom ($t = 0$) or on the lateral sides ($x = 0$ or $x = l$).
>
> **Strong form.** The maximum cannot be attained anywhere else (corners allowed) unless $u$ is constant.
>
> **Minimum principle.** The same holds for the minimum, by applying the maximum principle to $-u$.
>
> **$n$-D form.** If $u_t = k\Delta u$ in $D \times (0, T]$ for a bounded domain $D \subset \mathbb{R}^n$, then
> $$
> \begin{align}
> \max_{\bar{D} \times [0, T]} u = \max_{\Gamma} u, \qquad \Gamma = (\bar{D} \times \{0\}) \cup (\partial D \times [0, T]),
> \end{align}
> $$
> where $\Gamma$ is the parabolic boundary. If $D$ is connected and the maximum is attained at an interior point $(\mathbf{x}_0, t_0)$, $t_0 > 0$, then $u$ is constant on $\bar{D} \times [0, t_0]$.

![[Diffusion Maximum Principle Parabolic Boundary.png]]

**Interpretation.**[^3] In a rod with no internal heat source, the hottest and coldest spots can occur only initially or at an end. A hot spot at $t = 0$ cools off unless heat is fed in at an end; if you burn one end, the maximum temperature stays at that end and it is cooler away from it. The same holds for the concentration of a substance diffusing along a tube. In a "movie" of the solution, the maximum drops and the minimum rises: diffusion smooths the solution out. The top edge $t = T$ is excluded from $\Gamma$ because the future cannot feed back into the past.

# Generalizations
> [!abstract] Generalization 1 (Linear Second-Order Parabolic Operators)[^5]
> Let $U \subset \mathbb{R}^n$ be bounded and open, $U_T = U \times (0, T]$, and $\Gamma_T = \bar U_T \setminus U_T$ the parabolic boundary. Let $L$ be uniformly elliptic as in [[Maximum Principle (Laplace Equation)]], with bounded coefficients $a^{ij}, b^i, c$ that may depend on $(x, t)$. Let $u$ be $C^2$ in $x$ and $C^1$ in $t$ on $U_T$, and continuous on $\bar U_T$.
> 1. **Weak form, $c \equiv 0$.** If $u_t + Lu \leq 0$ in $U_T$, then $\max_{\bar U_T} u = \max_{\Gamma_T} u$.
> 2. **Weak form, $c \geq 0$.** If $u_t + Lu \leq 0$, then $\max_{\bar U_T} u \leq \max_{\Gamma_T} u^+$.
> 3. **Strong form** ($U$ connected, $c \equiv 0$). If $u_t + Lu \leq 0$ and $u$ attains $\max_{\bar U_T} u$ at $(x_0, t_0) \in U_T$, then $u$ is constant on $\bar U_{t_0}$. Only the **past** of $(x_0, t_0)$ is forced; the future is not.
> 4. **Comparison, any bounded $c$.** If $u_t + Lu \leq v_t + Lv$ in $U_T$ and $u \leq v$ on $\Gamma_T$, then $u \leq v$ in $U_T$.
>
> The [[Diffusion Equation]] is the case $L = -k\Delta$.

Proof of 4. Set $w = e^{-\mu t}(u - v)$ with $\mu \geq \sup c^-$. Then $w_t + Lw + \mu w = e^{-\mu t}\big[(u-v)_t + L(u-v)\big] \leq 0$, and the zeroth-order coefficient $c + \mu$ is $\geq 0$, so 2 gives $\max w \leq \max_{\Gamma_T} w^+ = 0$. The exponential weight absorbs any bounded growth term. This is why parabolic comparison needs no sign condition on $c$, whereas the elliptic version needs $c \geq 0$ (or a positive principal eigenvalue).

> [!abstract] Generalization 2 (Nonlinear Parabolic Equations)[^6]
> For $u_t + F(x, t, u, Du, D^2u) = 0$ with $F$ degenerate elliptic (nonincreasing in $D^2u$, as in [[Maximum Principle (Laplace Equation)]]) and under structure conditions on $F$, a viscosity subsolution $u$ and a viscosity supersolution $v$ with $u \leq v$ on $\Gamma_T$ satisfy $u \leq v$ in $U_T$.
>
> **Reaction–diffusion.** For $u_t = \Delta u + f(u)$ with $f$ Lipschitz, comparison of classical sub- and supersolutions already follows from Generalization 1.4. Write $f(u) - f(v) = -c(x,t)(u - v)$, where $c = -\frac{f(u)-f(v)}{u-v}$ is bounded by the Lipschitz constant, so $u - v$ satisfies a linear inequality with bounded $c$.

Hyperbolic equations have no analogue: see the scope table in [[Maximum Principle (Laplace Equation)]].

# Properties
- Proof idea: an interior maximum has $u_t = 0$ (or $u_t \ge 0$ on the top edge) and $u_{xx} \le 0$, which does not contradict $u_t = k u_{xx}$ when $u_{xx} = 0$; perturbing to $v = u + \epsilon x^2$ gives the strict "diffusion inequality" $v_t - k v_{xx} = -2k\epsilon < 0$, which rules out an interior maximum.[^4]
- Gives uniqueness and stability in the uniform sense for the Dirichlet problem ([[Diffusion Equation Well-Posedness]]).
- Fails for the [[Wave Equation]]: waves carry their amplitude around without damping ([[Wave and Diffusion Equation Comparison]]).
- Also holds for subsolutions $u_t \le k \Delta u$ (max) and supersolutions (min), and on the whole line for bounded solutions: $\inf \phi \le u(x, t) \le \sup \phi$.
- The time-independent case is the [[Maximum Principle (Laplace Equation)]] for [[Harmonic Function|harmonic functions]].

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=54&annotation=N5GCRVV8)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=54&annotation=HM2L2QR9); [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=54&annotation=VE6A6KY5)
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=55&annotation=7MC24ZCG)
[^4]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=55&annotation=LKFPFSP6)
[^5]: [Partial Differential Equations, 2nd ed. (Evans, AMS GSM 19)](https://bookstore.ams.org/gsm-19-r), §7.1.4.
[^6]: [User's guide to viscosity solutions of second order partial differential equations (Crandall, Ishii, Lions, 1992)](https://www.ams.org/journals/bull/1992-27-01/S0273-0979-1992-00266-5/), §8.
