---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] He Initialization[^1]
> For a layer with [[ReLU Function|ReLU]] activations whose weight matrix $\boldsymbol{\Omega}$ maps a layer of dimension $D_h$ (fan-in) to one of dimension $D_{h'}$ (fan-out), initialize the weights with zero mean and variance
> $$
> \begin{align}
> \sigma^2_\Omega = \frac{2}{D_h}
> \end{align}
> $$
> so that the variance of the pre-activations is preserved from layer to layer in the forward pass (He et al., 2015).

# Properties
- **Backward-pass version**: the backward pass multiplies by $\boldsymbol{\Omega}^T$, so preserving the variance of the gradients $\partial \ell / \partial \mathbf{f}_k$ instead requires $\sigma^2_\Omega = 2 / D_{h'}$.
- When $\boldsymbol{\Omega}$ is not square ($D_h \neq D_{h'}$), both conditions cannot hold at once; a compromise uses the mean $(D_h + D_{h'})/2$ as the number of terms:
$$
\begin{align}
\sigma^2_\Omega = \frac{4}{D_h + D_{h'}}
\end{align}
$$
- The "backward-pass He initialization" is therefore not about initializing gradients: it scales the random weights by fan-out so that backpropagated gradients neither vanish nor explode on the way to the early layers. Frameworks expose this choice, e.g. PyTorch's `torch.nn.init.kaiming_normal_(..., mode='fan_in')` (default, forward) versus `mode='fan_out'` (backward).[^2]
- The factor $2$ compensates for ReLU zeroing half of its inputs on average; without it, the rule reduces to the [[Xavier Initialization|Glorot / Xavier]] form, which differs by this factor of two.
- Prevents the [[Vanishing Gradients|vanishing]] and [[Exploding Gradients|exploding gradient]] problems at initialization ([[Weight Initialization]]).

[^1]: [Prince, Ch. 7](zotero://select/library/items/T3V9WVXD)
[^2]: Supplementary notes provided by the creator.
