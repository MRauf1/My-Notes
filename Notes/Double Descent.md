---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Double Descent[^1]
> As [[Model Capacity|model capacity]] increases, the test error first follows the U-shaped [[Bias-Variance Tradeoff|bias-variance trade-off]], peaks where the model has just enough capacity to fit (memorize) the training data exactly, and then decreases again as capacity grows further, eventually falling below the minimum of the first part of the curve. The three parts are:
> - the **classical** (under-parameterized) regime,
> - the **critical** regime, where the error increases,
> - the **modern** (over-parameterized) regime.

# Properties
- An interaction of two phenomena: (1) test performance becomes temporarily worse when the model can just memorize the data, as the bias-variance trade-off predicts; (2) performance keeps improving past the point where all training data are fitted, which is puzzling since the data no longer even constrain the parameters uniquely.[^2]
- Once training loss is near zero, extra capacity cannot improve the training fit, so any change happens between training points and is governed by the model's [[Inductive Bias]]. Because of the [[Curse of Dimensionality]], training data in high dimensions are extremely sparse, so behaviour between data points is critical.[^3]
- **Putative explanation**: added capacity lets the model interpolate between data points increasingly smoothly, which is a sensible assumption absent other information. Near the interpolation threshold (parameters $\approx$ training examples), the model must contort itself to fit the data exactly, producing erratic predictions and the pronounced peak.[^4]
- Smoothness is *possible* with more capacity, but many zero-loss solutions are not smooth. The preference for smooth solutions is thought to come from [[Regularization|implicit regularization]]: the initialization may start in, and training never leave, a sub-domain of smooth functions, or the training algorithm may "prefer" smooth solutions.[^5]
- Present on the original data for some datasets (e.g. MNIST); for others it emerges or becomes more prominent with label noise. Coined by Belkin et al. (2019) for two-layer networks and random features; Nakkiran et al. (2021) showed it across datasets, architectures (CNNs, ResNets, transformers), and optimizers (SGD, Adam). It is also more pronounced under some regularization techniques.[^6]
- **Effective model complexity** (Nakkiran et al., 2021): the largest number of samples for which a given model *and training method* achieve zero training error. Test performance depends on this, so on the training algorithm and the length of training as well as on the model. Increasing the number of training iterations at fixed capacity gives **epoch-wise double descent**, modelled by different features being learned at different speeds (Pezeshki et al., 2022).[^7]
- Predicts that adding training data can sometimes *worsen* test performance: an over-parameterized model in the second descent can be pushed back into the critical regime if the data grow to match its capacity.[^8]
- Over-parameterization is necessary to interpolate data smoothly in high dimensions: there is a trade-off between the number of parameters and the Lipschitz constant of the model (Bubeck & Sellke, 2021).[^9]
- Related to benign overfitting ([[Model Capacity]], [[Overparameterized Model]]).

[^1]: [Prince, p. 129](zotero://open-pdf/library/items/BWT7FYX5?page=143&annotation=XKDWCDNK); [Prince, p. 129](zotero://open-pdf/library/items/BWT7FYX5?page=143&annotation=4HZZRQPZ)
[^2]: [Prince, p. 129](zotero://open-pdf/library/items/BWT7FYX5?page=143&annotation=TYKB4RGM)
[^3]: [Prince, p. 129](zotero://open-pdf/library/items/BWT7FYX5?page=143&annotation=XN6MRP3D); [Prince, p. 129](zotero://open-pdf/library/items/BWT7FYX5?page=143&annotation=JB4NBZ8F)
[^4]: [Prince, p. 129](zotero://open-pdf/library/items/BWT7FYX5?page=143&annotation=5LSEPTEE); [Prince, p. 131](zotero://open-pdf/library/items/BWT7FYX5?page=145&annotation=WDGUB22W)
[^5]: [Prince, p. 131](zotero://open-pdf/library/items/BWT7FYX5?page=145&annotation=9YMQS9XI); [Prince, p. 132](zotero://open-pdf/library/items/BWT7FYX5?page=146&annotation=9KNLV3D7); [Prince, p. 132](zotero://open-pdf/library/items/BWT7FYX5?page=146&annotation=SL9GTGVU)
[^6]: [Prince, p. 134](zotero://open-pdf/library/items/BWT7FYX5?page=148&annotation=S7X2IRPQ)
[^7]: [Prince, p. 134](zotero://open-pdf/library/items/BWT7FYX5?page=148&annotation=F7ILKSW4)
[^8]: [Prince, p. 134](zotero://open-pdf/library/items/BWT7FYX5?page=148&annotation=F53WCTNC)
[^9]: [Prince, p. 135](zotero://open-pdf/library/items/BWT7FYX5?page=149&annotation=UU84PM64)
