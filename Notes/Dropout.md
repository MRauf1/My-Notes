---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Dropout[^1]
> A [[Regularization|regularization]] method that clamps a random subset (typically 50%) of hidden units to zero at each iteration of [[Stochastic Gradient Descent|SGD]].

# Properties
- Makes the network less dependent on any one hidden unit and encourages smaller weights, so that the presence or absence of a given unit changes the function less.
- Removes undesirable "kinks" far from the training data that do not affect the loss: when several units conspire to create such a kink, dropping one changes the output substantially in the half-space where it was active, and subsequent gradient steps compensate, gradually eliminating these large unnecessary changes between data points.[^2]
- **Inference**:[^3]
	- **Weight scaling inference rule**: run the full network with all units active and multiply the weights by one minus the dropout probability, since more units are active than during any training iteration. (Implementations usually use the equivalent *inverted dropout*, scaling activations by $1/(1-p)$ during training instead.)[^4]
	- **Monte Carlo dropout**: run the network several times with different random units dropped and combine the results, like an [[Ensemble Learning|ensemble]] that does not require training or storing multiple networks.
- Equivalent to multiplicative Bernoulli noise on the activations, which generalizes to [[Noise Injection (Regularization)|injecting noise]] elsewhere in the network.[^5]
- Combines multiple models, makes the function smoother, and finds wider minima ([[Regularization]]).

[^1]: [Prince, p. 147](zotero://open-pdf/library/items/BWT7FYX5?page=161&annotation=2U7TCMBA)
[^2]: [Prince, p. 147](zotero://open-pdf/library/items/BWT7FYX5?page=161&annotation=U3CDEX8D); [Prince, p. 148](zotero://open-pdf/library/items/BWT7FYX5?page=162&annotation=8YV25M2V)
[^3]: [Prince, p. 148](zotero://open-pdf/library/items/BWT7FYX5?page=162&annotation=F42NTSD9)
[^4]: Inverted dropout added from general knowledge.
[^5]: [Prince, p. 149](zotero://open-pdf/library/items/BWT7FYX5?page=163&annotation=76BUIMJ6)
