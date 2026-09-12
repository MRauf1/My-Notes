---
tags:
  - mathematics
  - pre_calculus
---

# Definition

> [!info] Definition 1 ([[Inverse]] [[Function]])[^1]
> Functions $f, g$ are inverses of each other if
> $$
> \begin{align}
> (f \circ g)(x) &= x, \forall x \in domain(f) \\
> (g \circ f)(x) &= x, \forall x \in domain(g)
> \end{align}
> $$
> Inverse of $f$ is unique and denoted as $f^{-1}$
> Inverse function of $f$ exists if and only if $f$ is [[Bijective Function]].

# Finding Inverse of a Function
1) Write $y = f(x)$
2) Switch $x$ and $y$
3) Solve $x = f(y)$ for $y$ to obtain $y = f^{-1}(x)$

# Properties
- $f(a) = b \iff g(b) = a$

## Uniqueness
- Inverse of a function $f$ is unique, and is denoted as $f^{-1}$

## [[Domain]] and [[Range]]
- Range of $f$ is the domain of $g$
- Range of $g$ is the domain of $f$

## [[Graph]]
- $(a, b)$ is on the graph of $f$ $\iff$ $(b, a)$ is on the graph of $g$ (Graphs of inverse functions are [[Reflection]] about the [[Line]] $y = x$)

## Existence
- For a function $f$ from a domain to its image (i.e. codomain restricted to the [[Range|range]]), the following are equivalent: $f$ is invertible $\iff$ $f$ is [[Injective Function|injective]] $\iff$ $f$ passes the [[Horizontal Line Test]].

[^1]: [szprecalculus07042013.pdf](zotero://open-pdf/library/items/J3667KH4?page=391)