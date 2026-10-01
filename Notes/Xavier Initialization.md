---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Xavier Initialization[^1]
> Also called **Glorot initialization** (Glorot & Bengio, 2010): initialize the weights of a layer with fan-in $D_h$ and fan-out $D_{h'}$ with zero mean and variance
> $$
> \begin{align}
> \sigma^2_\Omega = \frac{2}{D_h + D_{h'}}
> \end{align}
> $$
> balancing preservation of activation variance in the forward pass against gradient variance in the backward pass, for activations that are roughly linear around zero.[^2]

# Properties
- Does not account for the effect of the [[ReLU Function|ReLU]], and so differs from [[He Initialization]] by a factor of two.
- Essentially the same idea appeared earlier (LeCun et al., 2012, $\sigma^2_\Omega = 1/D_h$) for sigmoidal activations. These naturally bound each layer's outputs, but large pre-activations still fall into the flat regions of the [[Sigmoid Function|sigmoid]] and give very small gradients, so sensible initialization still matters.
- A uniform version samples from $U\left[-\sqrt{6/(D_h + D_{h'})}, \sqrt{6/(D_h + D_{h'})}\right]$, which has the same variance.[^2]

[^1]: [Prince, Ch. 7](zotero://select/library/items/T3V9WVXD)
[^2]: Exact formulas added from general knowledge of Glorot & Bengio (2010) and LeCun et al. (2012).
