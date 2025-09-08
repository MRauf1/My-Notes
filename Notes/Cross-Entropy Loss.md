---
tags: computer_science, deep_learning
---

# Definition

> [!info] Definition 1 (Cross-Entropy Loss)
> $$
> \begin{align}
> L(\hat{y}, y) = - \sum_{K}^{k=1} y_k log(\hat{y}_k)
> \end{align}
> $$
> where $\hat{y}_k$ is the [[Probability Mass Function|pmf]] $\mathbf{p}$ representing the [[Probability|probability]] that the input is of class $k$.[^1] $\mathbf{p}$ is a [[Point|point]] on the $(K - 1)$-[[Simplex|simplex]] denoted by $\mathbf{p} \in \triangle^{(K - 1)}$.

Cross-entropy is the negative of the sum of the elementwise agreements between the ground truth and the prediction.

Minimizing the cross-entropy maximizes the log likelihood of the ground truth observation $\mathbf{y}$ under the model's prediction $\hat{\mathbf{y}}$.

[^1]: https://visionbook.mit.edu/intro_to_learning.html