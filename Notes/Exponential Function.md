---
tags: [mathematics, pre_calculus]
---

# Definition

> [!info] Definition 1 ([[Exponentiation|Exponential]] [[Function]])[^1]
> Given a fixed base $b \in \mathbb{R}$ such that $b > 0, b \neq 1$, the exponential function is
> $$
> \begin{align}
> f(x) = b^x
> \end{align}
> $$
> [[Domain]] is $(-\infty, \infty)$ and [[Range]] is $(0, \infty)$.
> $y = 0$ is a [[Horizontal Asymptote]].
> If $b > 1$, then $f$ is an [[Increasing Function]], $\lim_{x \rightarrow -\infty} = 0, \lim_{x \rightarrow \infty} = \infty$.
> If $0 < b < 1$, then $f$ is a [[Decreasing Function]], $\lim_{x \rightarrow -\infty} = \infty, \lim_{x \rightarrow \infty} = 0$.

# Graph
![[Pasted image 20250924113236.png]]

> [!info] Definition 2 (Exponential Function of [[Complex Number]])
> For $z = x + iy \in \mathbb{C}$
> $$
> \begin{align}
> e^z &= e^x \cdot e^{iy} = e^x (\cos(y) + i \sin(y)) \\
> |e^z| &= e^x = e^{Re(z)} \\
> Arg(z) &= y\ (\text{mod}\ 2 \pi)
> \end{align}
> $$
> $e^z$ is $2 \pi i$ periodic (i.e., $e^{z + 2 \pi i} = e^z$ since $e^{2 \pi i} = 1$)
> More generally, for $a \in \mathbb{C}$
> $$
> \begin{align}
> a^z = e^{ln(a) \cdot z}
> \end{align}
> $$
> which is [[Multi-Valued Function]], unless you use principal [[Logarithm Function]].

# Properties
- [[Bijective Function]]
- [[Continuous Function]]
- [[Smooth Function]]

## [[Inverse Function]]
- [[Logarithm Function]]

[^1]: [szprecalculus07042013.pdf](zotero://open-pdf/library/items/J3667KH4?page=430)