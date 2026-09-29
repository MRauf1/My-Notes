---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Type I and Type II Errors[^1]
> For a [[Statistical Hypothesis Test]] with [[Critical Region]] $C$:
> - a Type I error occurs if $H_0$ is rejected when $H_0$ is true;
> - a Type II error occurs if $H_0$ is retained when $H_1$ is true.

| | $H_0$ true | $H_1$ true |
| --- | --- | --- |
| Reject $H_0$ | Type I error | correct decision (power) |
| Retain $H_0$ | correct decision | Type II error |

# Properties
- Seesaw effect: the two error probabilities generally cannot be minimized simultaneously. Shrinking $C$ lowers the Type I error probability but raises the Type II error probability; $C = \emptyset$ makes the first $0$ and the second $1$.
- Since Type I error is usually considered worse, its probability is bounded by the [[Size of a Test|size]] $\alpha$, and then the Type II error probability is minimized.
- For $\theta \in \omega_1$, $1 - P_\theta(\text{Type II error}) = P_\theta(\mathbf{X} \in C)$ is the [[Power Function (Statistics)|power]] at $\theta$, so minimizing Type II error is maximizing power.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=284)
