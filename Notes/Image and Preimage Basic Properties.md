---
tags:
  - mathematics
  - discrete_mathematics
---

# Definition

> [!abstract] Theorem 1 (Images of Unions and Intersections)[^1]
> Let $f: A \to B$ and $W, X \subseteq A$ ([[Image]]). Then
> $$
> \begin{align}
> f(W \cup X) &= f(W) \cup f(X) \\
> f(W \cap X) &\subseteq f(W) \cap f(X)
> \end{align}
> $$
> with equality in the second if $f$ is an [[Injective Function]].

> [!abstract] Theorem 2 (Preimages Preserve Set Operations)[^2]
> Let $f: A \to B$ and $Y, Z \subseteq B$ ([[Preimage]]). Then
> $$
> \begin{align}
> f^{-1}(Y \cup Z) &= f^{-1}(Y) \cup f^{-1}(Z) \\
> f^{-1}(Y \cap Z) &= f^{-1}(Y) \cap f^{-1}(Z) \\
> f^{-1}(Y \setminus Z) &= f^{-1}(Y) \setminus f^{-1}(Z)
> \end{align}
> $$
> and the same holds for arbitrary unions and intersections of [[Indexed Family of Sets|indexed families]].

> [!abstract] Theorem 3 (Composing Image and Preimage)[^2]
> For $X \subseteq A$ and $Y \subseteq B$,
> $$
> \begin{align}
> X \subseteq f^{-1}(f(X)), \qquad f(f^{-1}(Y)) \subseteq Y
> \end{align}
> $$
> with equality in the first if $f$ is injective, and in the second if $f$ is a [[Surjective Function]].

# Properties
- Preimages commute with all set operations because $x \in f^{-1}(Y)$ is the statement $f(x) \in Y$, so $\cup, \cap, \setminus$ pass through unchanged. Images only commute with unions, since $y \in f(X)$ is the existential statement $\exists x \in X\,(f(x) = y)$, and $\exists$ distributes over $\lor$ but not over $\land$ ([[Quantifier Distributive Laws]]).
- Counterexample for intersections: $f(1) = f(2) = 5$, $W = \{1\}$, $X = \{2\}$ gives $f(W \cap X) = \varnothing \ne \{5\} = f(W) \cap f(X)$.
- These are why [[Continuous Function|continuity]] and measurability are defined through preimages.

# Questions
> [!question]- Why does $f(W \cap X) = f(W) \cap f(X)$ need injectivity, while the preimage version needs nothing?
> $y \in f(W) \cap f(X)$ gives $w \in W$ and $x \in X$ with $f(w) = f(x) = y$, but $w$ and $x$ may differ, so no single witness lies in $W \cap X$. Injectivity forces $w = x$. For preimages, $x \in f^{-1}(Y \cap Z) \iff f(x) \in Y \land f(x) \in Z \iff x \in f^{-1}(Y) \cap f^{-1}(Z)$ involves no existential witness at all.

[^1]: [HOW TO PROVE IT: A Structured Approach, Second Edition](zotero://open-pdf/library/items/THI2Q4PN?page=272)
[^2]: [HOW TO PROVE IT: A Structured Approach, Second Edition](zotero://open-pdf/library/items/THI2Q4PN?page=273)
