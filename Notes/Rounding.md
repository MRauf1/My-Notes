---
tags:
  - computer_science
  - numerical_analysis
---

# Definition

> [!info] Definition 1 (Rounding)[^1]
> Rounding is the process of choosing a nearby [[Floating-Point Number System|floating-point number]] $fl(x)$ to approximate a given real number $x$ that is not a [[Machine Number]]. The error introduced by this approximation is [[Rounding Error]].

# Types
- **Chop** (round toward zero): the base-$\beta$ expansion of $x$ is truncated after the $(p-1)$st digit, so $fl(x)$ is the next floating-point number toward zero from $x$.
- **Round to nearest** (round to even): $fl(x)$ is the nearest floating-point number to $x$; ties are broken toward the floating-point number whose last stored digit is even.

Round to nearest is the most accurate and unbiased rule, though more expensive to implement correctly, and is the default rounding rule in IEEE standard systems.

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=40)
