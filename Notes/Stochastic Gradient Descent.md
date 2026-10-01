---
tags:
  - computer_science
  - computer_vision
---

# Definition

A type of [[Gradient Descent|gradient descent]], where instead of calculating the [[Gradient Vector|gradients]] of all training data (expensive), the algorithm samples (without replacement) a batch of training data and calculates the gradient for that batch. Then it continues for a different batch until all batches have been used up ($1$ epoch has finished).[^1]

Less accurate than full gradient descent, but is faster and less expensive to computer, which creates a tradeoff between accuracy and speed.

For a [[Cost Function]] that is the average of per-example losses, $J(\theta) = \frac{1}{N}\sum_{i=1}^N \mathcal{L}(f_\theta(\mathbf{x}^{(i)}), \mathbf{y}^{(i)})$, SGD estimates the full gradient by averaging over a randomly sampled batch of [[Batch Size|size]] $B$:
$$
\begin{align}
\tilde{\mathbf{g}} = \frac{1}{N}\sum_{b=1}^B \nabla_\theta \mathcal{L}(f_\theta(\mathbf{x}^{(b)}), \mathbf{y}^{(b)})
\end{align}
$$

Because a random batch is sampled, SGD may be able to jump over small bumps in the loss curvature.

SGD can implicitly regularize the learning problem; for example, for linear problems (i.e., $f_\theta$ linear) with multiple parameter settings that minimize the loss, SGD will often converge specifically to the solution with minimum parameter norm.

# Cons
- Need to normalize the inputs
- The learning rate is not adaptive

# Properties
- Prince's update for batch $\mathcal{B}_t$ with per-example losses $\ell_i$: $\boldsymbol{\phi}_{t+1} \leftarrow \boldsymbol{\phi}_t - \alpha \sum_{i \in \mathcal{B}_t} \partial \ell_i[\boldsymbol{\phi}_t] / \partial \boldsymbol{\phi}$. The noise means each step moves downhill only on average, so SGD can temporarily move uphill and jump between valleys of the loss.[^2]
- A batch can range from a single example to the whole dataset; the latter, **full-batch gradient descent**, is ordinary gradient descent. One pass through the dataset is an **epoch** ([[Batch Size]]).
- Alternative view: deterministic gradient descent on a loss function that changes with every batch, whose expected value and expected gradient match those of the full loss.
- Advantages: updates are sensible even if not optimal, since each improves the fit to some data; sampling without replacement lets all examples contribute equally; gradients are cheaper; it can in principle escape local minima; it reduces the chance of getting stuck near [[Saddle Point|saddle points]]; and there is evidence it finds parameters that generalize well.
- Does not converge in the traditional sense; near the global minimum all batches have small gradients, so the parameters stop changing much. It is usually paired with a [[Learning Rate Schedule]].
- As the learning rate tends to zero, SGD approaches a stochastic differential equation depending on the learning-rate-to-batch-size ratio, which is related to the width of the minimum found (Jastrzębski et al., 2018). Wider minima are preferred, since small parameter errors then barely affect test performance; generalization improves when the batch-size-to-learning-rate ratio is low (He et al., 2019; Smith et al., 2018; Goyal et al., 2018).

[^1]: https://visionbook.mit.edu/gradient_descent.html
[^2]: [Prince, Ch. 6](zotero://select/library/items/T3V9WVXD)
