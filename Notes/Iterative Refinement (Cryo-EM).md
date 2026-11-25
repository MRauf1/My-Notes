---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Iterative Refinement (ML-EM)[^1]
> The [[Expectation-Maximization Algorithm]] for [[Cryo-EM Maximum Likelihood Reconstruction]], with the rotations as latent variables. Discretize $SO(3)$ into $U_1, \dots, U_S$. Iteration $t$ has two steps:
> - **E-step**: compute each image's responsibilities over rotations,
> $$
> \begin{align}
> \gamma_i^{(t)}(s) = \frac{\exp\!\big(-\|I_i - h_i \star P(U_s \circ \varphi^{(t)})\|^2 / 2\sigma^2\big)}{\sum_{s'=1}^S \exp\!\big(-\|I_i - h_i \star P(U_{s'} \circ \varphi^{(t)})\|^2 / 2\sigma^2\big)}.
> \end{align}
> $$
> - **M-step**: solve a weighted linear least-squares problem, which is a [[Tomographic Reconstruction]]:
> $$
> \begin{align}
> \varphi^{(t+1)} = \arg\min_{\varphi} \sum_{i=1}^n \sum_{s=1}^S \gamma_i^{(t)}(s)\, \big\|I_i - h_i \star P(U_s \circ \varphi)\big\|^2 .
> \end{align}
> $$

# Properties
- **Convergence.** The marginal likelihood never decreases, and iterates converge to a critical point, not necessarily the global maximum. In practice this needs a good initial map ([[Ab Initio Reconstruction]]) or several restarts.
- **Cost, for $L \times L$ images.**
  - $S = O(L^3)$ rotations: $O(L^2)$ viewing directions times $O(L)$ in-plane rotations.
  - Projections via the [[Fourier Slice Theorem]] and NUFFT cost $O(L^4)$.
  - Matching one image against one viewing direction and all its in-plane rotations costs $O(L^2\log L)$ (polar resampling and 1D FFTs over rings).
  - So the E-step costs $O(nL^4\log L)$, and the M-step (back-projection) costs the same.
  - With $n = 10^5$, $L = 200$, a $10\times10$ shift search and NUFFT constants, this exceeds $10^{17}$ flops. The $L^4$ scaling in resolution is the bottleneck.
- **Accelerations**:
  - *hard assignment* (projection matching): keep only the best rotation, justified when the pose posterior is peaked;
  - gridding instead of NUFFT;
  - *branch and bound*: prune poses using bounds from the previous iteration;
  - *adaptive EM*: coarse-to-fine pose grids keeping 99.9% of the probability, an order of magnitude faster near convergence;
  - *subspace EM*: PCA of images, with correlations precomputed against eigen-images.
- The regularized version is [[MAP Refinement (Cryo-EM)]].
- **Hard vs. soft assignment.** Hard assignment (projection matching) assigns each image its best-correlating projection and then reconstructs, as in EMAN2 and cisTEM. Soft assignment (ML-EM) weights all projections by their responsibilities, as in RELION and cryoSPARC. ML-EM was first used on 2D cryo-EM images by Sigworth.[^2]
- **General form.** For $y_i = L_{\theta_i}x + \varepsilon_i$ with $L_\theta$ linear and $\theta$ latent (in cryo-EM, 3D rotation plus 2D shift: 5 dimensions), EM marginalizes $\theta$. With a Gaussian prior on $x$, the M-step is a linear system. The distribution of $\theta$ is in general unknown and can be estimated within EM.

# Questions
> [!question]- Connection: How does ML-EM refinement correspond to EM for a Gaussian mixture, and where does the correspondence break?
> The dictionary, against [[Mixture of Gaussians]]:
> - a mixture component $s$ corresponds to a discretized rotation $U_s$;
> - a component mean corresponds to the predicted image $h_i \star P(U_s\circ\varphi)$;
> - the shared isotropic covariance corresponds to the noise $\sigma^2 I$;
> - the responsibilities are the same softmax formula.
>
> **Where it breaks:** in a GMM, each mean is a free parameter, updated independently as a weighted average. Here all $S$ "means" are tied through one structure $\varphi$ (and differ per image through $h_i$), so the M-step is a single coupled linear least-squares problem, a tomographic reconstruction. The mixing weights are also fixed (uniform over $SO(3)$), not learned.

[^1]: [Singer and Sigworth, 2020, p. 15](zotero://open-pdf/library/items/FKVQSKD6?page=15&annotation=PCVA7BNU)
[^2]: [Bendory et al., 2020, p. 9](zotero://open-pdf/library/items/N4ZIHINK?page=9&annotation=FW2YHFMF)
