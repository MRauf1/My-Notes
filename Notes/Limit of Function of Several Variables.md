---
tags:
  - mathematics
  - calculus
---

# Definition

> [!info] Definition 1 (Limit of a Function of Two Variables)[^1]
> $\lim_{(x, y) \to (a, b)} f(x, y) = L$ if for every $\varepsilon > 0$ there is $\delta > 0$ such that $(x, y) \in D$ and $0 < \sqrt{(x - a)^2 + (y - b)^2} < \delta$ imply $|f(x, y) - L| < \varepsilon$.
>
> This is the [[Limit of Function]] on the [[Metric Space]] $\mathbb{R}^2$ with [[Euclidean Distance]].

# Properties
- Two-path test: if $f \to L_1$ along one path to $(a, b)$ and $f \to L_2 \neq L_1$ along another, the limit does not exist. Agreement along all lines is not enough, e.g. $\frac{xy^2}{x^2 + y^4}$ is $0$ on every line but $\frac{1}{2}$ along $x = y^2$.
- Existence is proved with $\varepsilon$–$\delta$ or by squeezing $|f(x, y) - L| \leq g(x, y) \to 0$ ([[Limit of Function Squeeze Theorem]]), often in polar coordinates.
- $f$ is continuous at $(a, b)$ if the limit equals $f(a, b)$ ([[Continuous Function]]). Polynomials, rational functions on their domains, and compositions of continuous functions are continuous.

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=940)
