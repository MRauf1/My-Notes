---
tags: mathematics, pre_calculus
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

#TODO 
Put this in or not:
## Existence
Following statements are equivalent: (Page 394)
- $f$ is invertible
- $f$ is [[Injective Function]]
- $f$ passes the [[Horizontal Line Test]]
This is true only if it's a function from some domain to the image of the function (not an arbitrary range)

[^1]: [szprecalculus07042013.pdf](zotero://open-pdf/library/items/J3667KH4?page=391)