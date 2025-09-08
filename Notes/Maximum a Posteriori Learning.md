---
tags: computer_science, deep_learning
---

# Definition

> [!info] Definition
> $$
> \begin{align}
> \underset{f}{\mathrm{\arg \max}} [p(f | \{\mathbf{x}^{(i)}, \mathbf{y}^{(i)}\}_{i=1}^N)] = \\
> = \underset{f}{\mathrm{\arg \max}} [p(\{\mathbf{y}^{(i)}\}_{i=1}^N | \{\mathbf{x}^{(i)}\}_{i=1}^N, f) p(f)]
> \end{align}
> $$

Learning using [[Maximum a Posteriori|MAP]].[^1] Trying to infer the hypothesis $f$ that assigns the highest [[Probability|probability]] to the data given some prior.

[^1]: https://visionbook.mit.edu/intro_to_learning.html