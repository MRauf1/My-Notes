---
tags:
  - mathematics
  - calculus
---

# Definition

> [!info] Definition 1 ([[Leonhard Euler|Euler's]] Number)[^2]
> $e$ is a number such that for an [[Exponential Function]] $f(x) = e^x$
> $$
> \begin{align}
> f'(0) = \lim_{h \rightarrow 0} \frac{e^h - 1}{h} = 1
> \end{align}
> $$

Euler's number is the base such that the [[Exponential Function]] $f(x) = b^x$ has a [[Slope]] of $1$ at the [[Tangent Line]] at the [[Point]] $(0, 1)$.[^1]

> [!info] Definition 2 (Euler's Number as a [[Limit of Function]])[^3]
> $$
> \begin{align}
> e &= \lim_{x \rightarrow 0} (1 + x)^{1/x} \\
> &= \lim_{n \rightarrow \infty} (1 + \frac{1}{n})^n
> \end{align}
> $$

> [!info] Definition 3 (Euler's Number as a Series)[^4]
> $$
> \begin{align}
> e = \sum_{n=0}^{\infty} \frac{1}{n!}
> \end{align}
> $$
> where $0! := 1$.

> [!abstract] Theorem (e is Irrational)[^5]
> $e$ is an [[Irrational Number]].

The factorial series in Definition 3 converges very rapidly: its partial sum through $n = N$ approximates $e$ with an error strictly between $0$ and $\frac{1}{N \cdot N!}$ — e.g. truncating at $N=10$ already approximates $e$ with error less than $10^{-7}$. This tight, explicit error bound is what makes the irrationality of $e$ easy to prove: if $e = p/q$ for integers $p, q$, the bound forces a contradiction once $N \geq q$.

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=1)
[^2]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=210)
[^3]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=254)
[^4]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=72)
[^5]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=74)