---
tags:
  - computer_science
  - machine_learning
---

# Definition
> [!info] Information Content (Self-Information)[^1][^2]
> The amount of information received on observing the value $x$ of a discrete random variable, viewed as the "degree of surprise":
> $$
> \begin{align}
> h(x) = -\log_2 p(x)
> \end{align}
> $$
> measured in bits (base $2$) or, with natural logarithms, in nats.

**Why the logarithm.** $h$ should be a monotonic function of $p(x)$ such that information from two unrelated events adds, $h(x, y) = h(x) + h(y)$. Unrelated events are statistically independent, $p(x, y) = p(x)\,p(y)$, and the logarithm is the function that turns this product into a sum.[^1]

# Properties
- The negative sign makes $h(x) \geq 0$; improbable events carry high information, and a certain event ($p(x) = 1$) carries none.[^2]
- The base of the logarithm is arbitrary and only fixes the unit: $1$ nat $= 1/\ln 2 \approx 1.443$ bits.
- Its expectation under $p(x)$ is the [[Entropy]].
- The negative log likelihood of a data point under a model is its information content under that model, linking error functions to coding length ([[Kullback-Leibler Divergence]]).

[^1]: [Bishop, 2006, p. 48](zotero://open-pdf/library/items/5G99AZ8U?page=68&annotation=RJ43J95Z)
[^2]: [Bishop, 2006, p. 49](zotero://open-pdf/library/items/5G99AZ8U?page=69&annotation=IQGRHYXI)
