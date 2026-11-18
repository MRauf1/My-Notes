---
tags:
  - mathematics
  - calculus
---

# Definition

> [!abstract] Theorem 1 (Method of Cylindrical Shells)[^1]
> The volume of the solid obtained by rotating about the $y$-axis the region under $y = f(x)$ from $a$ to $b$, where $f \geq 0$ is continuous and $0 \leq a < b$, is
> $$
> \begin{align}
> V = \int_a^b 2\pi x f(x)\,dx
> \end{align}
> $$

# Properties
- Mnemonic: $V = \int 2\pi\,(\text{radius})(\text{height})\,d(\text{thickness})$, a sum of thin cylindrical shells of volume $\approx 2\pi r h\,\Delta r$.
- Rotation about $x = c$ uses radius $|x - c|$; rotation about a horizontal line uses shells in $y$.
- Agrees with [[Volume by Slicing]] (washers); shells are preferable when the washer radii would require solving for $x$ in terms of $y$.

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=482)
