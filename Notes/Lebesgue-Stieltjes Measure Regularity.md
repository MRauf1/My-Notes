---
tags:
  - mathematics
  - measure_theory
---

# Definition
Fix a complete [[Lebesgue-Stieltjes Measure]] $\mu$ on $\mathbb{R}$ associated to an increasing, right continuous $F$, with domain $\mathcal{M}_\mu$. By construction, for $E \in \mathcal{M}_\mu$,[^1]
$$
\begin{align}
\mu(E) = \inf\left\{\sum_{j=1}^\infty [F(b_j) - F(a_j)] : E \subseteq \bigcup_{j=1}^\infty (a_j, b_j]\right\} = \inf\left\{\sum_{j=1}^\infty \mu((a_j, b_j]) : E \subseteq \bigcup_{j=1}^\infty (a_j, b_j]\right\}.
\end{align}
$$

> [!abstract] Lemma 1.17 (Covering by Open Intervals)[^2]
> For any $E \in \mathcal{M}_\mu$,
> $$
> \begin{align}
> \mu(E) = \inf\left\{\sum_{j=1}^\infty \mu((a_j, b_j)) : E \subseteq \bigcup_{j=1}^\infty (a_j, b_j)\right\}.
> \end{align}
> $$

> [!abstract] Theorem 1.18 (Outer and Inner Regularity)[^3]
> If $E \in \mathcal{M}_\mu$, then
> $$
> \begin{align}
> \mu(E) = \inf\{\mu(U) : U \supseteq E,\ U \text{ open}\} = \sup\{\mu(K) : K \subseteq E,\ K \text{ compact}\}.
> \end{align}
> $$

> [!abstract] Theorem 1.19 (Structure Modulo Null Sets)[^4]
> If $E \subseteq \mathbb{R}$, the following are equivalent:
> 1. $E \in \mathcal{M}_\mu$.
> 2. $E = V \setminus N_1$ where $V$ is a [[G-Delta Set|$G_\delta$ set]] and $\mu(N_1) = 0$.
> 3. $E = H \cup N_2$ where $H$ is an [[F-Sigma Set|$F_\sigma$ set]] and $\mu(N_2) = 0$.

> [!abstract] Proposition 1.20 (Approximation by Finite Unions of Intervals)[^5]
> If $E \in \mathcal{M}_\mu$ and $\mu(E) < \infty$, then for every $\epsilon > 0$ there is a set $A$ that is a finite union of open intervals such that $\mu(E \triangle A) < \epsilon$.

Theorem 1.19 says that all measurable sets, in particular all Borel sets, have a simple form *modulo null sets*: one step beyond open or closed sets. This contrasts sharply with the transfinite hierarchy needed to build Borel sets exactly from open sets ([[Borel Sigma-Algebra]], Proposition 1.23).[^6]

# Properties
- Each measurable set is squeezed between an $F_\sigma$ set and a $G_\delta$ set of the same measure: $H \subseteq E \subseteq V$ with $\mu(V \setminus H) = 0$.
- Consequently $\mathcal{M}_\mu$ is the [[Measure Completion Theorem|completion]] of $\mathcal{B}_\mathbb{R}$ under $\mu$.
- Proposition 1.20 uses the [[Symmetric Difference]] as the measure of approximation error; it underlies density arguments (e.g. step functions dense in $L^1$).
- Applies in particular to [[Lebesgue Measure]].

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=48&annotation=MMQCI399)
[^2]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=48&annotation=HK3BR974)
[^3]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=49&annotation=B4R4KD6L)
[^4]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=49&annotation=WVI4SYMF)
[^5]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=50&annotation=9X5RQ7WV)
[^6]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=50&annotation=Y8UFTFEU)
