---
tags: mathematics, pre_algebra, discrete_mathematics
---

# Definition

> [!info] Definition 1 (Prime Number)[^2]
> A number $n$ is prime if
> $$
> \begin{align}
> n > 1 \land \neg (\exists a \in \mathbb{N} \exists b \in \mathbb{N} (1 < a < n \land 1 < b < n \land ab = n))
> \end{align}
> $$

[[Natural Number|Natural number]] $>1$ with only two [[Factor|factors]]: $1$ and itself.[^1] To test whether a number is prime or not, it is enough to check if any of the smaller primes are factors or not.

Number $1$ is neither prime nor composite.

> [!example]- Example 1 (Prime Number)
> > [!example]- Examples 1.1 (Prime Number)
> > $$
> > \begin{align}
> > 7 = 7 \cdot 1
> > \end{align}
> > $$

# Properties

- Number $2$ is the only [[Even Number|even]] prime number. 
- There are [[Infinity|infinitely]] many prime numbers.
- Every natural number $>1$ is either a prime number or a [[Multiplication|product]] of prime numbers.[^3]
- Let $p$ be a prime number and $a, b$ be non-zero integers. $p | ab \implies (p | a \lor p | b)$ (This can be extended to a product of $n$ non-zero integers)

[^1]: [Prealgebra2e-WEB.pdf](zotero://open-pdf/library/items/W4QW2QZI?page=167)
[^2]: [HOW TO PROVE IT: A Structured Approach, Second Edition](zotero://open-pdf/library/items/THI2Q4PN?page=169)
[^3]: [HOW TO PROVE IT: A Structured Approach, Second Edition](zotero://open-pdf/library/items/THI2Q4PN?page=171)