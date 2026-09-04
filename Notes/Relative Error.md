---
tags:
  - computer_science
  - numerical_analysis
---

# Definition

> [!info] Definition 1 (Relative [[Error]])[^1]
> $$
> \begin{align}
> \text{Relative error} = \frac{\text{Absolute error}}{\text{true value}}
> \end{align}
> $$

Relative error is undefined if the true value is zero.[^2] It can equivalently be expressed as
$$
\begin{align}
\text{Approximate value} = (\text{true value}) \times (1 + \text{relative error}).
\end{align}
$$

If an approximate value has a relative error of about $10^{-p}$, then its decimal representation has about $p$ correct [[Significant Digits]].

[^1]: [Scientific Computing](zotero://open-pdf/library/items/UQ4SGXEK?page=17)
[^2]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=26)