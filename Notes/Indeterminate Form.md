---
tags:
  - mathematics
  - calculus
---

# Definition

> [!info] Definition 1 (Indeterminate Form)[^1]
> A limit $\lim_{x \to a} F(x)$ built from component functions is an indeterminate form if the limits of the components alone do not determine it: depending on the functions, it may equal any number, $\pm\infty$, or fail to exist. The seven types are
> $$
> \begin{align}
> \frac{0}{0}, \quad \frac{\infty}{\infty}, \quad 0 \cdot \infty, \quad \infty - \infty, \quad 0^0, \quad \infty^0, \quad 1^\infty
> \end{align}
> $$

# Types
- Quotients $\frac{0}{0}$, $\frac{\infty}{\infty}$: apply [[L'Hospital's Rule]] directly.[^1]
- Product $0 \cdot \infty$: rewrite $fg = \frac{f}{1/g}$ or $\frac{g}{1/f}$ to get a quotient form.[^2]
- Difference $\infty - \infty$: combine into a single fraction (common denominator, rationalization or factoring).[^3]
- Powers $0^0$, $\infty^0$, $1^\infty$: write $f^g = e^{g \ln f}$ (or take logarithms), which turns them into a product of type $0 \cdot \infty$.[^4]

# Properties
- Not indeterminate: e.g. $\frac{0}{\infty} = 0$, $\infty \cdot \infty = \infty$, $\infty + \infty = \infty$, $0^{\infty} = 0$ (for $f > 0$) and $\infty^{\infty} = \infty$. These are determined by the [[Limit of Function]] laws and [[Infinite Limit of Function|infinite limits]].
- Basic example: $\lim_{x \to a} \frac{f(x) - f(a)}{x - a}$, the [[Derivative]], is always of type $\frac{0}{0}$ when $f$ is continuous at $a$.

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=337)
[^2]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=340)
[^3]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=341)
[^4]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=342)
