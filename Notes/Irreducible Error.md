---
tags: statistics, statistical_learning
---

# Definition

For a [[Prediction]] task $\hat{Y} = \hat{f}(X)$, the independent error $\epsilon$ from $Y = f(X) + \epsilon$ is what causes the irreducible error.[^1]

Since $\epsilon$ is [[Independent Random Variable|independent]] of $X$ (which is the only feature we use to predict $Y$), this error cannot be reduced.

$\epsilon$ may represent unmeasured variables that are useful in predicting $Y$ or it may contain unmeasurable variation.

Irreducible error provides an [[Set Upper Bound]] on the accuracy of the prediction for $Y$ and a [[Set Lower Bound]] on the [[Prediction Error]].

[^1]: [Introduction to Statistical Learning with Python](zotero://open-pdf/library/items/9JTAJ2JI?page=27)