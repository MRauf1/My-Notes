---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Weight Initialization[^1]
> The choice of initial parameter values before training a neural network. The weights $\boldsymbol{\Omega}$ must be scaled so that the magnitudes of activations in the forward pass and of gradients in the backward pass stay stable from layer to layer; otherwise gradients decrease or increase uncontrollably ([[Vanishing Gradients]], [[Exploding Gradients]]).

# Types
- **Variance-preserving random initialization**: [[He Initialization]] (ReLU), [[Xavier Initialization]] (Glorot; roughly linear or sigmoidal activations), and LeCun initialization.
- **Data-dependent initialization**: pass data through the network and normalize by the empirically observed variance, e.g. layer-sequential unit variance (orthonormal weights, then rescaled), GradInit (learned non-negative scale per weight matrix), and ActNorm (a learnable scale and offset per hidden unit, initialized from a batch to give zero mean and unit variance, then trained).
- **Architecture-specific**: e.g. orthogonal initialization for convolutional networks, Fixup for residual networks, and T-Fixup / DT-Fixup for transformers.

# Properties
- Closely related to [[Batch Normalization]], which normalizes the variance of each batch at every step as part of the network's processing.
- The [[Scaled Exponential Linear Unit]] makes activations tend to zero mean and unit variance automatically, within a certain range of inputs.

[^1]: [Prince, Ch. 7](zotero://select/library/items/T3V9WVXD)
