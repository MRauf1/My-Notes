---
tags:
  - statistics
  - statistical_learning
---

# Definition

> [!info] Definition 1 ([[Bias]]-[[Variance]] Tradeoff)[^1]
> Test [[Mean Squared Error]] can be decomposed into
> $$
> \begin{align}
> E[y_0 - \hat{f}(x_0)]^2 = Var[\hat{f}(x_0)] + (Bias[\hat{f}(x_0)])^2 + Var[\epsilon]
> \end{align}
> $$
> To minimize the error, need to simultaneously achieve low [[Variance]] and low [[Bias]].
> [[Variance]] refers to how much $\hat{f}$ would change if we estimated it using a different training data set. [[Bias]] refers to the error introduced by approximating a real-life problem by a much simpler model.


> [!abstract] Derivation for Least Squares (Prince)[^2]
> Let $\mu[\mathbf{x}] = \mathbb{E}_y[y[\mathbf{x}]]$ be the true function mean, $\sigma^2 = \mathbb{E}_y[(\mu[\mathbf{x}] - y[\mathbf{x}])^2]$ the noise, and $L[\mathbf{x}] = (f[\mathbf{x}, \boldsymbol{\phi}] - y[\mathbf{x}])^2$. Since $\mathbb{E}_y[y[\mathbf{x}]] = \mu[\mathbf{x}]$, the cross term vanishes:
> $$
> \begin{align}
> \mathbb{E}_y[L[\mathbf{x}]] &= (f[\mathbf{x}, \boldsymbol{\phi}] - \mu[\mathbf{x}])^2 + 2(f[\mathbf{x}, \boldsymbol{\phi}] - \mu[\mathbf{x}])(\mu[\mathbf{x}] - \mathbb{E}_y[y[\mathbf{x}]]) + \mathbb{E}_y[(\mu[\mathbf{x}] - y[\mathbf{x}])^2] \\
> &= (f[\mathbf{x}, \boldsymbol{\phi}] - \mu[\mathbf{x}])^2 + \sigma^2
> \end{align}
> $$
> The parameters depend on the training set $\mathcal{D}$, so write $f[\mathbf{x}, \boldsymbol{\phi}[\mathcal{D}]]$ with mean $f_\mu[\mathbf{x}] = \mathbb{E}_{\mathcal{D}}[f[\mathbf{x}, \boldsymbol{\phi}[\mathcal{D}]]]$. Repeating the argument over $\mathcal{D}$,
> $$
> \begin{align}
> \mathbb{E}_{\mathcal{D}}\left[\mathbb{E}_y[L[\mathbf{x}]]\right] = \underbrace{\mathbb{E}_{\mathcal{D}}\left[(f[\mathbf{x}, \boldsymbol{\phi}[\mathcal{D}]] - f_\mu[\mathbf{x}])^2\right]}_{\text{variance}} + \underbrace{(f_\mu[\mathbf{x}] - \mu[\mathbf{x}])^2}_{\text{bias}} + \underbrace{\sigma^2}_{\text{noise}}
> \end{align}
> $$

## Relationship Between Noise and Variance
Noise and variance are causally related but are different quantities, and they enter the decomposition as separate additive terms.[^3]
- **What varies.** Noise $\sigma^2$ is the spread of the *target* $y$ around $\mu[\mathbf{x}]$ for a fixed input; it is a property of the data-generating process alone and would remain even with infinite data and a perfect model. Variance is the spread of the *fitted function* $f[\mathbf{x}, \boldsymbol{\phi}[\mathcal{D}]]$ across training sets; it is a property of the estimator (model, training procedure, and dataset size).
- **Why they are linked.** Variance exists largely *because* the training targets are noisy: with finite data, the learner cannot tell systematic structure in $\mu[\mathbf{x}]$ from noise, so each training set's particular noise realization leaks into the fit. For ordinary least squares with $p$ parameters and $N$ examples, the average variance of the fit at the training inputs is exactly $\sigma^2 p / N$: variance is proportional to the noise, grows with capacity $p$, and shrinks with data $N$.
- **But variance is not only noise.** Even with $\sigma^2 = 0$, the fit can differ across datasets because different inputs $\mathbf{x}$ are sampled, leaving different gaps to interpolate, and because stochastic training and initialization converge to different solutions.
- **Why the terms separate.** The test target is drawn independently of the training set, so the test noise is uncorrelated with the fit's deviation and the cross term vanishes; the training noise shows up *inside* the variance term, the test noise as the separate $\sigma^2$.
- **Practical consequence.** Noise is irreducible. Variance is the *propagated* effect of training noise and can be reduced by more data, regularization, or averaging models (ensembling); this is why label noise sharpens the [[Double Descent]] peak, where the model fits the noise exactly.

In general, more flexible models have high [[Variance]] and low [[Bias]].

This additive decomposition is [[Bias-Variance Decomposition Specificity to Squared Error Loss|specific to squared-error loss]]; other loss functions (e.g. 0-1 loss) do not admit the same clean additive bias/variance split.

The general [[Bias-Variance-MSE Decomposition of an Estimator]] drops the irreducible-error term $\mathrm{Var}[\epsilon]$ and applies to any estimator of a fixed, deterministic quantity rather than only to a fitted predictive model.

# Properties
- **Three sources of test error** (Prince): *noise*, the inherent uncertainty in the true input-output mapping ([[Irreducible Error]]); *bias*, the systematic deviation of the model from the true function mean because it is not flexible enough; and *variance*, the uncertainty in the fitted model due to the particular training set sampled (plus any randomness of a stochastic learning algorithm). Their relative contributions depend on the inherent uncertainty of the task, the amount of training data, and the choice of model.[^4]
- They are present in every task but combine additively only for regression with a least-squares loss ([[Bias-Variance Decomposition Specificity to Squared Error Loss]]).
- **Reducing variance**: more training data averages out the noise and samples the input space well; adding training data almost always improves test performance.[^5]
- **Reducing bias**: increasing [[Model Capacity|capacity]], i.e. more hidden units or layers. But for a fixed-size training set variance typically increases with capacity, so more capacity does not necessarily reduce test error; much of the extra power models the noise ([[Overfitting]]). This suggests an optimal intermediate capacity.
- The classical U-shaped curve is not the whole story for over-parameterized models ([[Double Descent]]).

[^1]: [Introduction to Statistical Learning with Python](zotero://open-pdf/library/items/9JTAJ2JI?page=42)
[^2]: [Prince, p. 123](zotero://open-pdf/library/items/BWT7FYX5?page=137&annotation=6E8WN68K); [Prince, p. 123](zotero://open-pdf/library/items/BWT7FYX5?page=137&annotation=P68A4JYE); [Prince, p. 124](zotero://open-pdf/library/items/BWT7FYX5?page=138&annotation=AIZ9U6V7); [Prince, p. 124](zotero://open-pdf/library/items/BWT7FYX5?page=138&annotation=XEZ25D8Q); [Prince, p. 124](zotero://open-pdf/library/items/BWT7FYX5?page=138&annotation=R3B4F22E)
[^3]: Creator-requested elaboration; the $\sigma^2 p / N$ result is the standard least-squares variance from general knowledge.
[^4]: [Prince, p. 118](zotero://open-pdf/library/items/BWT7FYX5?page=132&annotation=IV4FGBA9); [Prince, p. 122](zotero://open-pdf/library/items/BWT7FYX5?page=136&annotation=N3GSEUUA); [Prince, p. 122](zotero://open-pdf/library/items/BWT7FYX5?page=136&annotation=YR5T4ZSE); [Prince, p. 123](zotero://open-pdf/library/items/BWT7FYX5?page=137&annotation=MP7AR3DU); [Prince, p. 124](zotero://open-pdf/library/items/BWT7FYX5?page=138&annotation=7MCDX94G)
[^5]: [Prince, p. 124](zotero://open-pdf/library/items/BWT7FYX5?page=138&annotation=CYBF7G6N); [Prince, p. 125](zotero://open-pdf/library/items/BWT7FYX5?page=139&annotation=K4N9V7NU); [Prince, p. 125](zotero://open-pdf/library/items/BWT7FYX5?page=139&annotation=H9VVVX7G); [Prince, p. 125](zotero://open-pdf/library/items/BWT7FYX5?page=139&annotation=Z6I8MP5N); [Prince, p. 125](zotero://open-pdf/library/items/BWT7FYX5?page=139&annotation=G3FTCTDS); [Prince, p. 125](zotero://open-pdf/library/items/BWT7FYX5?page=139&annotation=CZIKACLV); [Prince, p. 125](zotero://open-pdf/library/items/BWT7FYX5?page=139&annotation=Z7IICKM5)
