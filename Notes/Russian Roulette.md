---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Russian Roulette[^1]
> Adds one extra draw in front of the two [[Path Tracing (Recursive Estimator)|path-tracing]] steps to terminate the recursion with probability one. Fix a constant $q \in (0,1)$ in advance, and draw $\xi \sim \mathcal{U}[0,1]$:
> - If $\xi \geq q$, return $L_e(x,\omega)$ — the walk ends here.
> - Otherwise, draw $\omega_i \sim p$, set $y = \mathrm{rayTrace}(x,\omega_i)$, and return the one-sample estimate divided by $q$:
> $$
> \begin{align}
> L_e(x,\omega) + \frac{1}{q}\langle L(y,-\omega_i)\rangle\,\frac{f_s(x,\omega_i\to\omega)\,|\cos\theta_i|}{p(\omega_i)}
> \end{align}
> $$

The walk now stops with probability one — its length is geometric, $\mathbb{P}[\text{length} > N] = q^N \to 0$, so every realization is finite and the expected number of vertices is $1/(1-q)$; nothing is truncated.

Writing $\langle I \rangle$ for the contribution the coin decides about, the first moment is untouched:
$$
\begin{align}
\mathbb{E}[\langle I \rangle_{\mathrm{RR}}] = q \cdot \frac{\mathbb{E}[\langle I \rangle]}{q} + (1-q)\cdot 0 = \mathbb{E}[\langle I \rangle]
\end{align}
$$
The second moment is not: squaring keeps the $1/q^2$, but the coin only pays out $q$ of the time:
$$
\begin{align}
\mathrm{Var}[\langle I \rangle_{\mathrm{RR}}] = \frac{\mathrm{Var}[\langle I \rangle]}{q} + \frac{1-q}{q}\,\mathbb{E}^2[\langle I \rangle]
\end{align}
$$
Both terms blow up as $q \to 0$, so killing a walk is cheap only when what it would have carried, $\mathbb{E}^2[\langle I \rangle]$, is small; good practice sets $q$ from how much the walk is still carrying, rather than from a fixed schedule.

# Properties
- Unbiased for every choice of $q \in (0,1)$; removes the truncation bias of a fixed recursion depth $D$ at the cost of added [[Monte Carlo Estimator Variance|variance]].

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
