---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Power Function of a Test[^1]
> The power function of a [[Critical Region]] $C$ is
> $$
> \begin{align}
> \gamma_C(\theta) = P_\theta[(X_1, \dots, X_n) \in C], \quad \theta \in \omega_1
> \end{align}
> $$
> Its value at $\theta$ is the power of the test at $\theta$: the probability that the test detects the alternative $\theta$ when it is the true parameter.

Power is $1 - P_\theta(\text{Type II error})$ ([[Type I and Type II Errors]]), so maximizing power is minimizing the Type II error probability.

# Properties
- Comparison: given two critical regions $C_1, C_2$ of the same [[Size of a Test|size]] $\alpha$, $C_1$ is better than $C_2$ if $\gamma_{C_1}(\theta) \geq \gamma_{C_2}(\theta)$ for all $\theta \in \omega_1$; a test that is best for every alternative is uniformly most powerful.
- The same formula evaluated on $\omega_0$ gives the Type I error probabilities, whose maximum is the size.
- Power typically increases with the sample size and with the distance of $\theta$ from $\omega_0$.
- Not to be confused with the algebraic [[Power Function]] $f(x) = ax^n$.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=285)
