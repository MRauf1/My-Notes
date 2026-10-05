---
tags:
  - computer_science
  - computer_vision
---

# Definition

> [!info] Definition
> $$
> \begin{align}
> x_{out}[i] = \gamma \frac{x_{in}[i] - \mathbb{E}[x_{in}[i]]}{\sqrt{Var[x_{in}[i]]}} + \beta
> \end{align}
> $$
> where $\gamma, \beta$ are learnable parameters to allow the layer be expressive enough to output values with non-zero mean and non-zero variance

[[Normalization Layer|Normalization layer]] that standardizes the input with respect to the [[Mean|mean]] and [[Variance|variance]] of the batch of the inputs per channel.[^1]

Due to the reliance on the batch for each datapoint, it violates the assumption that the datapoints are processed independently and identically (iid).

At test time, the standard approach is to aggregate the statistics from the training dataset, but using test batch statistics can be useful to achieve invariance to changes in the statistics from the training data to the test data.

If a batch is stored as a [[Tensor]] $\mathbf{X} \in \mathbb{R}^{N_{batch}\times C}$, batchnorm standardizes each element by the mean and variance of its column (over the batch), which is a "transpose" of what [[Layer Normalization|layernorm]] does, standardizing by the mean and variance of each row (over the channels of a datapoint) instead.

> [!info] Batch Normalization (Prince's Formulation)[^2]
> For each hidden unit $h$ separately, compute the empirical [[Mean|mean]] and standard deviation over the batch $\mathcal{B}$:
> $$
> \begin{align}
> m_h = \frac{1}{|\mathcal{B}|}\sum_{i\in\mathcal{B}} h_i, \qquad s_h = \sqrt{\frac{1}{|\mathcal{B}|}\sum_{i\in\mathcal{B}} (h_i - m_h)^2}
> \end{align}
> $$
> standardize, then scale by $\gamma$ and shift by $\delta$:
> $$
> \begin{align}
> h_i \leftarrow \frac{h_i - m_h}{s_h + \epsilon}, \qquad h_i \leftarrow \gamma h_i + \delta \qquad \forall i \in \mathcal{B}
> \end{align}
> $$
> where $\epsilon$ prevents division by zero when $s_h = 0$. Afterwards the activations have mean $\delta$ and standard deviation $\gamma$ across the batch, both learned during training.

![[Normalization Schemes.png]]

# Properties
- **Parameter count**: applied independently to each hidden unit; a network with $K$ layers of $D$ hidden units has $KD$ offsets $\delta$ and $KD$ scales $\gamma$. In a [[Convolutional Neural Network|CNN]], statistics are computed over both the batch and the spatial positions, giving $KC$ offsets and $KC$ scales for $K$ layers of $C$ channels.[^3]
- **Test time**: there is no batch, so $m_h$ and $s_h$ are computed over the whole training dataset and frozen in the final network.[^3]
- **Scale invariance**: if the weights and biases feeding an activation are multiplied by $a > 0$, the activation and $s_h$ are both multiplied by $a$, and the normalization cancels this. Hence a large family of weights produces the same function (redundancy), while $\gamma, \delta$ add extra parameters to compensate, which is inefficient but beneficial.[^4]
	- This invariance to the scales of the weight matrices decreases the importance of tuning the [[Learning Rate|learning rate]]; even an exponentially increasing [[Learning Rate Schedule|learning rate schedule]] is possible (Li & Arora, 2019).[^5]
- **Benefits**:[^6]
	- *Stable forward propagation*: with $\delta = 0$, $\gamma = 1$ at initialization, each output activation has unit [[Variance|variance]]; in a residual network the variance then grows only linearly instead of exponentially ([[Residual Network Variance at Initialization]]).
	- *Higher learning rates*: empirically and theoretically, BN makes the loss surface and its gradient change more smoothly (reduces [[Shattered Gradients]]), so higher learning rates can be used, which improve test performance. Santurkar et al. (2018) also show that the distance to the nearest optimum from any initialization is smaller with BN.[^7]
	- *[[Regularization]]*: the normalization of an example depends on the other (random) members of the batch, which injects noise ([[Noise Injection (Regularization)]]); [[Ghost Batch Normalization]] preserves this noise for large batches.
	- Makes [[Sigmoid Function|sigmoid]] activations more practical, as inputs are less likely to fall into saturated extremes, and reduces the tendency of deep ReLU hidden units to be always active or always inactive at initialization.[^8]
- **Gradient explosion without skip connections**: in ReLU networks without [[Residual Connection|residual connections]], BN increases gradient magnitudes by a factor $\sqrt{\pi/(\pi-1)} \approx 1.21$ per layer (Yang et al., 2019). This also occurs along paths of a residual network, but removing the $2^K$ forward-pass growth outweighs the $1.21^K$ backward-pass growth, so BN overall stabilizes training.[^9]
- **Why it works is not well understood**: the original motivation, reducing [[Internal Covariate Shift]], has been challenged; the smoother-loss-landscape explanation is currently favored.[^7]
- Monte Carlo batch normalization (Teye et al., 2018) uses BN's stochasticity to estimate the predictive uncertainty of neural networks.[^10]

[^1]: https://visionbook.mit.edu/neural_nets.html
[^2]: [Prince, p. 192](zotero://open-pdf/library/items/BWT7FYX5?page=206&annotation=FFG3FKX6); [Prince, p. 193](zotero://open-pdf/library/items/BWT7FYX5?page=207&annotation=5ZGDHIR3)
[^3]: [Prince, p. 194](zotero://open-pdf/library/items/BWT7FYX5?page=208&annotation=EXFZNBP5)
[^4]: [Prince, p. 194](zotero://open-pdf/library/items/BWT7FYX5?page=208&annotation=8W5N5VLU)
[^5]: [Prince, p. 204](zotero://open-pdf/library/items/BWT7FYX5?page=218&annotation=CMK76ZLJ)
[^6]: [Prince, p. 194](zotero://open-pdf/library/items/BWT7FYX5?page=208&annotation=82VD6Y8W); [Prince, p. 194](zotero://open-pdf/library/items/BWT7FYX5?page=208&annotation=QXYSXZTD); [Prince, p. 194](zotero://open-pdf/library/items/BWT7FYX5?page=208&annotation=CMD6WQSW)
[^7]: [Prince, p. 204](zotero://open-pdf/library/items/BWT7FYX5?page=218&annotation=JUBLEA25); [Prince, p. 204](zotero://open-pdf/library/items/BWT7FYX5?page=218&annotation=JGZ9ISIE)
[^8]: [Prince, p. 203](zotero://open-pdf/library/items/BWT7FYX5?page=217&annotation=DYXUY3KJ)
[^9]: [Prince, p. 203](zotero://open-pdf/library/items/BWT7FYX5?page=217&annotation=ZKTXT2JP)
[^10]: [Prince, p. 204](zotero://open-pdf/library/items/BWT7FYX5?page=218&annotation=IWF2TIB4)