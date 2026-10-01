# References

A compact list of fundamental papers referenced in the notes.

## Expressivity and Depth
- Montúfar, Pascanu, Cho & Bengio (2014). *On the Number of Linear Regions of Deep Neural Networks*. NeurIPS. [arXiv:1402.1869](https://arxiv.org/abs/1402.1869) — [[Linear Regions of ReLU Network]]
- Telgarsky (2016). *Benefits of Depth in Neural Networks*. COLT. [arXiv:1602.04485](https://arxiv.org/abs/1602.04485) — [[Depth Separation]]
- Eldan & Shamir (2016). *The Power of Depth for Feedforward Neural Networks*. COLT. [arXiv:1512.03965](https://arxiv.org/abs/1512.03965) — [[Depth Separation]]
- Lu, Pu, Wang, Hu & Wang (2017). *The Expressive Power of Neural Networks: A View from the Width*. NeurIPS. [arXiv:1709.02540](https://arxiv.org/abs/1709.02540) — [[Universal Approximation Theorem]], [[Width Efficiency]]

## Activation Functions
- Glorot, Bordes & Bengio (2011). *Deep Sparse Rectifier Neural Networks*. AISTATS. [PMLR 15](https://proceedings.mlr.press/v15/glorot11a.html) — [[ReLU Function]], [[Softplus Function]]
- Hendrycks & Gimpel (2016). *Gaussian Error Linear Units (GELUs)*. [arXiv:1606.08415](https://arxiv.org/abs/1606.08415) — [[Gaussian Error Linear Unit]], [[Swish Function]]

## Loss Functions
- Lin, Goyal, Girshick, He & Dollár (2017). *Focal Loss for Dense Object Detection*. ICCV. [arXiv:1708.02002](https://arxiv.org/abs/1708.02002) — [[Focal Loss]]

## Optimization
- Duchi, Hazan & Singer (2011). *Adaptive Subgradient Methods for Online Learning and Stochastic Optimization*. JMLR. [JMLR 12](https://jmlr.org/papers/v12/duchi11a.html) — [[AdaGrad]]
- Kingma & Ba (2015). *Adam: A Method for Stochastic Optimization*. ICLR. [arXiv:1412.6980](https://arxiv.org/abs/1412.6980) — [[Adam]]
- Loshchilov & Hutter (2019). *Decoupled Weight Decay Regularization*. ICLR. [arXiv:1711.05101](https://arxiv.org/abs/1711.05101) — [[AdamW]]
- Wilson, Roelofs, Stern, Srebro & Recht (2017). *The Marginal Value of Adaptive Gradient Methods in Machine Learning*. NeurIPS. [arXiv:1705.08292](https://arxiv.org/abs/1705.08292) — [[Adam]], [[Stochastic Gradient Descent]]
- Goyal et al. (2017). *Accurate, Large Minibatch SGD: Training ImageNet in 1 Hour*. [arXiv:1706.02677](https://arxiv.org/abs/1706.02677) — [[Learning Rate Warm-Up]], [[Batch Size]]

## Initialization and Normalization
- Glorot & Bengio (2010). *Understanding the Difficulty of Training Deep Feedforward Neural Networks*. AISTATS. [PMLR 9](https://proceedings.mlr.press/v9/glorot10a.html) — [[Xavier Initialization]]
- He, Zhang, Ren & Sun (2015). *Delving Deep into Rectifiers: Surpassing Human-Level Performance on ImageNet Classification*. ICCV. [arXiv:1502.01852](https://arxiv.org/abs/1502.01852) — [[He Initialization]], [[Parametric ReLU]]
- Ioffe & Szegedy (2015). *Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift*. ICML. [arXiv:1502.03167](https://arxiv.org/abs/1502.03167) — [[Batch Normalization]]

## Memory-Efficient Training
- Chen, Xu, Zhang & Guestrin (2016). *Training Deep Nets with Sublinear Memory Cost*. [arXiv:1604.06174](https://arxiv.org/abs/1604.06174) — [[Gradient Checkpointing]]
- Gomez, Ren, Urtasun & Grosse (2017). *The Reversible Residual Network: Backpropagation Without Storing Activations*. NeurIPS. [arXiv:1707.04585](https://arxiv.org/abs/1707.04585) — [[Gradient Checkpointing]]
- Huang et al. (2019). *GPipe: Efficient Training of Giant Neural Networks using Pipeline Parallelism*. NeurIPS. [arXiv:1811.06965](https://arxiv.org/abs/1811.06965) — [[Micro-Batching]]
