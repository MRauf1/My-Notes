---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Robin Eigenvalue Problem on an Interval[^1][^2]
> For given constants $a_0, a_l$, the [[Eigenfunction|eigenvalue problem]]
> $$
> \begin{align}
> -X'' = \lambda X, \qquad X'(0) - a_0 X(0) = 0, \qquad X'(l) + a_l X(l) = 0.
> \end{align}
> $$
> Both conditions are $\partial X/\partial n + aX = 0$ with the outward normal ($n = -1$ at $x = 0$, $n = +1$ at $x = l$), which is why the signs are opposite. For heat, $a > 0$ means radiation (energy leaves), $a < 0$ absorption (energy enters), $a = 0$ insulation; for a string, $a > 0$ means the string shares energy with the endpoints, $a < 0$ gains energy from them.[^3][^4]
>
> **Positive eigenvalues** $\lambda = \beta^2$, $\beta > 0$, are the roots of
> $$
> \begin{align}
> (\beta^2 - a_0 a_l)\tan\beta l = (a_0 + a_l)\beta, \qquad X(x) = \cos\beta x + \frac{a_0}{\beta}\sin\beta x
> \end{align}
> $$
> (the exceptional case $\cos\beta l = 0$ occurs when $\beta = \sqrt{a_0 a_l}$, "intersection at infinity").[^5][^6]
>
> **Zero** is an eigenvalue (eigenfunction $X = 1 + a_0 x$) iff $a_0 + a_l = -a_0 a_l l$.[^7]
>
> **Negative eigenvalues** $\lambda = -\gamma^2$, $\gamma > 0$, are the roots of
> $$
> \begin{align}
> \tanh\gamma l = -\frac{(a_0 + a_l)\gamma}{\gamma^2 + a_0 a_l}, \qquad X(x) = \cosh\gamma x + \frac{a_0}{\gamma}\sinh\gamma x.
> \end{align}
> $$
> There are never nonreal eigenvalues, and there are always infinitely many positive ones: the right side of the $\tan$ equation runs from the origin to the $\beta$-axis, so it crosses every branch of $\tan\beta l$ except possibly the first.[^8][^9]

# Complete Classification
Let
$$
\begin{align}
h = a_0 + a_l + a_0 a_l l, \qquad \text{equivalently} \qquad (1 + a_0 l)(1 + a_l l) = 1 + l h.
\end{align}
$$
The sign of $h$, together with the number of negative coefficients, decides everything below the positive spectrum:[^10][^11]

| Boundary coefficients | $h > 0$ | $h = 0$ | $h < 0$ |
| --- | --- | --- | --- |
| $a_0 = a_l = 0$ (Neumann) | — | $\lambda_0 = 0$, rest positive | — |
| $a_0, a_l \ge 0$, not both $0$ (radiation/insulation) | all positive | — | — |
| exactly one negative (absorption at one end) | all positive | $\lambda_0 = 0$, rest positive | one negative, rest positive |
| both negative (absorption at both ends) | **two** negative, rest positive | one negative, $\lambda_1 = 0$, rest positive | one negative, rest positive |

Book's cases as instances:
- *Case 1* ($a_0, a_l > 0$): only positive eigenvalues, with $\frac{n^2\pi^2}{l^2} < \lambda_n < \frac{(n+1)^2\pi^2}{l^2}$ ($n = 0, 1, 2, \dots$) and $\beta_n - \frac{n\pi}{l} \to 0$, so large eigenvalues approach the Neumann ones.[^12]
- *Case 2* ($a_0 < 0 < a_l$, $a_0 + a_l > 0$, more radiation than absorption): $h > 0$ ("much more radiation", (14)) gives an eigenvalue $0 < \lambda_0 < (\pi/2l)^2$ and all positive; $h = 0$ gives $\lambda_0 = 0$; $h < 0$ (18) gives exactly one negative eigenvalue $\lambda_0 < 0$: the "missing" positive $\lambda_0$ reappears below zero.[^13][^14]
- For one absorbing end with $a_0 + a_l \le 0$ (absorption at least balancing radiation), automatically $h < 0$, so there is always a negative eigenvalue.

A zero eigenvalue requires $a_0$ or $a_l$ negative and the length tuned exactly to $l = -(a_0 + a_l)/(a_0 a_l)$, unless $a_0 = a_l = 0$.[^7]

# Spectral Reading
Every row of the table follows from the quadratic form.[^11] Integrating by parts,
$$
\begin{align}
\lambda \int_0^l |X|^2\, dx = Q(X) := \int_0^l |X'|^2\, dx + a_0 |X(0)|^2 + a_l |X(l)|^2,
\end{align}
$$
the [[Dirichlet Energy]] plus boundary energy. Hence:
- **Realness.** The operator is symmetric on $L^2(0, l)$, so $\lambda \in \mathbb{R}$.
- **Positivity.** If $a_0, a_l \ge 0$ then $Q \ge 0$, and $Q = 0$ only for constants with $a_0 = a_l = 0$.
- **At most two negative eigenvalues.** $Q$ is the nonnegative Neumann form plus one rank-one term per endpoint, and a rank-one negative perturbation can push at most one eigenvalue below zero (min–max / Cauchy interlacing). So #negative $\le$ #negative coefficients; testing $X \equiv 1$ gives $Q = a_0 + a_l$, so at least one negative eigenvalue whenever $a_0 + a_l < 0$.
- **Monotonicity and bracketing.** By the Courant–Fischer min–max principle every $\lambda_n$ is strictly increasing in $a_0$ and $a_l$, and $\lambda_n \to \lambda_n^{\text{Dirichlet}}$ as $a \to +\infty$. Thus, indexing from $n = 0$, $\lambda_n^{\text{Neumann}} \le \lambda_n^{\text{Robin}} \le \lambda_n^{\text{Dirichlet}}$ for $a_0, a_l \ge 0$, which is exactly the bound $n^2\pi^2/l^2 < \lambda_n < (n+1)^2\pi^2/l^2$ of Case 1. Eigenvalues cross zero only on the curve $h = 0$, which is why the sign of $h$ counts them.
- **Boundary-localized modes.** For strong absorption ($a \to -\infty$) each negative eigenvalue is $\approx -a^2$ with eigenfunction $\approx e^{-|a|\,\text{dist}(x, \text{end})}$, a mode trapped at the absorbing end.

# Properties
- The $a_0 = a_l = 0$ case is the [[Neumann Eigenvalue Problem on an Interval]]; $a \to \infty$ recovers the [[Dirichlet Eigenvalue Problem on an Interval]]; one end Dirichlet and the other $a = 0$ is the [[Mixed Eigenvalue Problem on an Interval]].
- Arises from the [[Robin Boundary Condition]] in [[Separation of Variables]], giving $u = \sum_n T_n(t)X_n(x)$.
- **Physical consequence (heat in a rod).** With $a_0 < 0 < a_l$ and $a_0 + a_l > 0$, there is a negative eigenvalue iff the absorption is large enough, $|a_0| > a_l/(1 + a_l l)$; then[^15]
$$
\begin{align}
u(x, t) = A_0 e^{+\gamma_0^2 k t}\left(\cosh\gamma_0 x + \frac{a_0}{\gamma_0}\sinh\gamma_0 x\right) + \sum_{n=1}^\infty A_n e^{-\beta_n^2 k t}\left(\cos\beta_n x + \frac{a_0}{\beta_n}\sin\beta_n x\right),
\end{align}
$$
  and the rod gets hotter without bound (unless $A_0 = 0$). If $|a_0| < a_l/(1 + a_l l)$ all eigenvalues are positive and the temperature decays to zero. For waves, a negative eigenvalue likewise gives exponential growth through $(A_0 e^{\gamma_0 c t} + B_0 e^{-\gamma_0 c t})X_0(x)$.[^16]
- Stability of the [[Diffusion Equation on a Finite Interval]] with Robin conditions is therefore decided by the sign of the bottom eigenvalue $\lambda_0$, i.e. by $h$ and the signs of $a_0, a_l$.

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=104&annotation=S3DFPU4F)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=105&annotation=ANRF3S4P)
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=105&annotation=NZI62QTE)
[^4]: Outward-normal form added for consistency with [[Robin Boundary Condition]].
[^5]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=105&annotation=WHJYQ5H3)
[^6]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=106&annotation=R5B8KDSX)
[^7]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=108&annotation=37QHFGBV)
[^8]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=109&annotation=AJVP8TMZ)
[^9]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=110&annotation=8TJFBYCB)
[^10]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=110&annotation=SJ4U5SY6)
[^11]: Completion of the case summary (Strauss Exercise 4.3.8 and the remaining sign cases) and spectral arguments derived from general knowledge: zero eigenvalue $X = 1 + a_0 x$ requires $h = 0$; $\lambda_0$ is increasing in $a_0, a_l$ and changes sign only across $h = 0$.
[^12]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=106&annotation=DM9LIQU8)
[^13]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=108&annotation=3L9GUF3F)
[^14]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=110&annotation=GH55ZAY5)
[^15]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=111&annotation=BMAHZHZL)
[^16]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=112&annotation=E56ANY6G)
