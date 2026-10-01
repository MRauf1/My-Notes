---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Adam[^1]
> **Adaptive moment estimation**: a [[Gradient-Based Learning|gradient-based]] optimizer that keeps exponential moving averages of the gradient and of its pointwise square,
> $$
> \begin{align}
> \mathbf{m}_{t+1} &\leftarrow \beta \cdot \mathbf{m}_t + (1 - \beta)\frac{\partial L[\boldsymbol{\phi}_t]}{\partial \boldsymbol{\phi}} \\
> \mathbf{v}_{t+1} &\leftarrow \gamma \cdot \mathbf{v}_t + (1 - \gamma)\left(\frac{\partial L[\boldsymbol{\phi}_t]}{\partial \boldsymbol{\phi}}\right)^2
> \end{align}
> $$
> corrects their bias toward zero at the start of training,
> $$
> \begin{align}
> \tilde{\mathbf{m}}_{t+1} \leftarrow \frac{\mathbf{m}_{t+1}}{1 - \beta^{t+1}}, \qquad \tilde{\mathbf{v}}_{t+1} \leftarrow \frac{\mathbf{v}_{t+1}}{1 - \gamma^{t+1}}
> \end{align}
> $$
> and updates
> $$
> \begin{align}
> \boldsymbol{\phi}_{t+1} \leftarrow \boldsymbol{\phi}_t - \alpha \cdot \frac{\tilde{\mathbf{m}}_{t+1}}{\sqrt{\tilde{\mathbf{v}}_{t+1}} + \epsilon}
> \end{align}
> $$
> with pointwise square root and division, momentum coefficients $\beta, \gamma \in [0, 1)$, and a small $\epsilon$ preventing division by zero.

[[Gradient-Based Learning]] optimizer.


# Pros
- No need to normalize the inputs (although it could help?)
- Learning rate is adaptive

# Properties
- **Motivation**: normalizing the gradient as $\boldsymbol{\phi}_{t+1} \leftarrow \boldsymbol{\phi}_t - \alpha\, \mathbf{m}_{t+1} / (\sqrt{\mathbf{v}_{t+1}} + \epsilon)$ with the raw gradient $\mathbf{m}$ and squared gradient $\mathbf{v}$ leaves only the sign in each coordinate, moving a fixed distance $\alpha$ along each axis. This makes good progress in every direction even when the loss is much steeper in some, but it never converges and bounces around the minimum. Adam adds momentum to both statistics so that it can converge.
- The bias correction matters only early: since $\beta, \gamma < 1$, the denominators approach one.
- Usually used stochastically, with both statistics computed from mini-batches ([[Stochastic Gradient Descent]]), so the trajectory is noisy.
- Compensates for gradient magnitudes that depend on depth in the network, balancing changes across layers; it is less sensitive to the initial learning rate and does not need complex [[Learning Rate Schedule|learning rate schedules]], though [[Learning Rate Warm-Up]] helps because its statistics are noisy early in training.
- Builds on [[AdaGrad]] and [[RMSProp]]; variants include [[AdamW]] (decoupled weight decay), NAdam ([[Nesterov Accelerated Momentum]]), and rectified Adam.
- **SGD vs. Adam**: SGD with momentum has been reported to find minima that generalize better (Wilson et al., 2017). But SGD is a special case of Adam ($\beta = 0$, $\gamma \to 1$, once the bias correction approaches one), so the gap more likely reflects Adam's default hyperparameters: with tuned hyperparameters Adam performs as well as SGD and converges faster (Choi et al., 2019).

[^1]: [Prince, Ch. 6](zotero://select/library/items/T3V9WVXD)
