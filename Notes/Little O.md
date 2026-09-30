---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Little O (Deterministic)
> For functions or sequences, $f = o(g)$ (as $h \to 0$, or as $n \to \infty$) if
> $$
> \begin{align}
> \lim \frac{f}{g} = 0
> \end{align}
> $$
> i.e. $f$ is negligible compared with $g$. In particular $o(h)$ denotes any quantity with $o(h)/h \to 0$ as $h \to 0$ (e.g. $h^2 = o(h)$ and $o(h) + o(h) = o(h)$).[^1]

> [!info] Little O in Probability[^2]
> For sequences of random variables, $X_n = o_p(Y_n)$ if
> $$
> \begin{align}
> \frac{X_n}{Y_n} \xrightarrow{P} 0
> \end{align}
> $$
> ([[Convergence in Probability]]); in particular $X_n = o_p(1)$ means $X_n \xrightarrow{P} 0$.

$o$ is a strict asymptotic bound: $f$ grows strictly slower than $g$. By contrast, [[Big O]] $f = O(g)$ says $f$ grows at most as fast as $g$ up to a constant; so $f = o(g)$ implies $f = O(g)$. The stochastic counterpart of $O(1)$ is $O_p(1)$, [[Bounded in Probability]].

# Properties
- Theorem (Hogg 5.2.8):[^2] if $\{Y_n\}$ is [[Bounded in Probability]] and $X_n = o_p(Y_n)$, then $X_n \xrightarrow{P} 0$. Proof: $X_n = (X_n/Y_n) \cdot Y_n = o_p(1)\,O_p(1) = o_p(1)$.
- Arithmetic: $o_p(1) + o_p(1) = o_p(1)$ and $O_p(1)\,o_p(1) = o_p(1)$, so $o_p$ remainders vanish in limits by [[Slutsky's Theorem]].
- Used for Taylor remainders: $g(x) = g(\theta) + g'(\theta)(x - \theta) + o(|x - \theta|)$, which becomes the $o_p$ remainder in the [[Delta Method]].
- Appears in the axioms of the [[Poisson Process]], where the probability of two or more events in a short interval of length $h$ is $o(h)$.
- A type of [[Asymptotic Relationship]].

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=184)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=351)
