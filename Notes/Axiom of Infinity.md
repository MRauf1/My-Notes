---
tags:
  - mathematics
  - discrete_mathematics
---

# Definition

> [!info] Axiom of Infinity (ZF)[^1][^2]
> There exists a set $Z$ that contains the [[Empty Set|empty set]] and is closed under the successor operation $S(y) = y \cup \{y\}$:
> $$
> \begin{align}
> \exists Z \,\big[\, \varnothing \in Z \ \wedge\ \forall y\, (y \in Z \to y \cup \{y\} \in Z) \,\big].
> \end{align}
> $$
> A set with these two properties is called inductive.

This is the only axiom of ZF set theory that asserts the existence of an [[Infinite Set|infinite set]]. Every other infinite object in mathematics is built from the set it provides: $\mathbb{N}$, then $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$, sequences, series, and measures. Infinity is *postulated*. It cannot be derived from finite constructions.

# Properties
- **Von Neumann naturals.** Starting from $\varnothing$ and applying the successor operation gives $0 = \varnothing$, $1 = \{\varnothing\}$, $2 = \{\varnothing, \{\varnothing\}\}$, and so on, with $n = \{0, 1, \dots, n-1\}$. In ZFC the finite ordinals are identified with the natural numbers, and $\omega = \mathbb{N}$.[^2]
- **$\omega$ is the smallest inductive set.** Define $\omega = \bigcap \{ S \subseteq Z : S \text{ inductive} \}$; this set exists by the separation axiom. It is inductive. For any inductive $I$, the set $Z \cap I$ is an inductive subset of $Z$, so $\omega \subseteq I$.
- **Induction is a theorem.** If $S \subseteq \omega$ is inductive, then $\omega \subseteq S$ by minimality, so $S = \omega$. This is the induction axiom of the [[Peano Axioms]] (starting from $0$ instead of $1$) and the basis of [[Proof by Induction]]. The other Peano axioms also hold for $(\omega, 0, S)$, with $0 \neq S(n)$ because $n \in S(n)$.
- **$\omega$ is infinite.** $S : \omega \to \omega \setminus \{0\}$ is a bijection onto a proper subset, so $\omega$ is Dedekind-infinite and hence infinite ([[Infinite Set]], Theorem 1).
- **Uncountable sets come next.** Combined with the power set axiom, the axiom gives $\mathcal{P}(\omega)$, which is strictly larger than $\omega$ by [[Cantor's Theorem]]. So the axiom of infinity is the source of both countable and uncountable infinity.

# Questions

> [!question]- The axiom only says that *some* inductive set $Z$ exists. How do you get a canonical $\mathbb{N}$ and the principle of induction from it?
> Intersect all inductive subsets of $Z$: $\omega = \bigcap\{S \subseteq Z : S \text{ inductive}\}$, which exists by separation. $\omega$ is inductive and lies inside every inductive set $I$, because $Z \cap I$ is inductive, so it does not depend on the choice of $Z$. Induction is then just minimality: an inductive $S \subseteq \omega$ must equal $\omega$.

> [!question]- Why can't the existence of an infinite set be proved from the other axioms?
> Every other axiom (empty set, pairing, union, power set, separation, replacement, foundation) turns given sets into new sets in a way that, starting from finite sets, only ever yields finite sets. The hereditarily finite sets $V_\omega$ form a model of ZF minus Infinity (with Infinity negated). Any proof of an infinite set's existence from the other axioms would therefore be valid inside $V_\omega$, which has no infinite set. So infinity has to be added as an axiom.[^3]

[^1]: [Zermelo-Fraenkel Set Theory (Stanford Encyclopedia of Philosophy)](https://plato.stanford.edu/entries/set-theory/zf.html)
[^2]: [Set Theory, §2.1 and §3 (Stanford Encyclopedia of Philosophy)](https://plato.stanford.edu/entries/set-theory/)
[^3]: [Hereditarily finite set (Wikipedia)](https://en.wikipedia.org/wiki/Hereditarily_finite_set)
