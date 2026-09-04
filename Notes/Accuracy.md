---
tags:
  - computer_science
  - numerical_analysis
---

# Definition

> [!info] Definition 1 (Accuracy)[^1]
> Accuracy refers to the closeness of a computed solution to the true solution of the problem under consideration.

Accuracy depends on both the [[Sensitivity|conditioning]] of the problem and the [[Stable Algorithm|stability]] of the algorithm: stability only guarantees that the computed result is exact for a nearby problem, and that nearby problem's solution is close to the true solution only if the problem is well-conditioned. Consequently, inaccuracy can result either from applying a stable algorithm to an ill-conditioned problem or from applying an unstable algorithm to a well-conditioned problem, whereas a stable algorithm applied to a well-conditioned problem yields an accurate solution.

Accuracy should not be confused with [[Precision]]: precision is the number of digits with which a number is expressed, whereas accuracy is the number of correct [[Significant Digits]].

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=37)
