---
tags:
  - computer_science
  - machine_learning
---

# Definition
> [!info] Priors in Light of the Bitter Lesson[^1]
> The [[Bitter Lesson]] does not say priors are useless; it says that priors which cap what computation can achieve (hand-built human knowledge) lose in the long run to general methods that scale. A prior is worth pursuing if it **composes with scale** (it keeps helping, or at least does not hurt, at $100\times$ the compute), or if it matters **where scale cannot reach**.

The methods that won under the bitter lesson are themselves full of priors: convolution (translation equivariance), attention (permutation equivariance), residual connections, and objectives like next-token prediction or denoising. These are general structural [[Inductive Bias|inductive biases]] that grow more useful as data and compute grow, unlike hand-engineered features that impose a ceiling. The warning in the other direction is real: AlphaFold 3 replaced much of AlphaFold 2's hand-designed equivariant structure module with a diffusion module plus scale, and improved.

# Properties
- **Regimes scale cannot reach**: scaling needs a large stream of data from the distribution of interest.
	- *Per-instance problems* (reconstructing one scene from a few views, one patient's scan, one physical system) give a single data set of fixed size, so the prior determines what is recovered.
	- *Ill-posed [[Inverse Problem|inverse problems]]*: when many latent causes produce the same measurements, more measurements of the same kind cannot break the non-identifiability; the prior is mathematically necessary, not merely convenient.
	- *Scarce or expensive data*: medicine, science, robotics, safety-critical long tails.
- **Priors expressed in a form that scales**, reconciling the [[Probability Bayesian Framework|Bayesian perspective]] with the bitter lesson:
	- *Learned priors inside Bayesian inference*: a [[Generative Model|generative model]] trained at scale supplies the prior $p(\mathbf{x})$, and an exact forward model supplies the likelihood $p(\mathbf{y} | \mathbf{x})$, e.g. diffusion posterior sampling[^2] and score distillation for text-to-3D.[^3] Scale learns the prior; Bayesian machinery uses it.
	- *Priors as data-generating processes*: prior-data fitted networks train a transformer on samples from a specified prior so that it learns to approximate the [[Predictive Distribution|posterior predictive]].[^4] Designing a better prior becomes designing a better simulator, which is a graphics problem.
	- *Pretraining as learning a prior*: in-context learning can be read as implicit Bayesian inference,[^5] so prompting and fine-tuning play the role of the posterior update, and choosing the pretraining distribution and objective is prior design.
- **Uncertainty and decisions**: scaling improves point predictions but does not by itself supply calibrated epistemic uncertainty. The [[Reject Option]], re-weighting for new class priors, revising the loss matrix ([[Minimum Expected Loss Decision Rule]]), [[Novelty Detection]], active learning, Bayesian optimization, and safe exploration all need posteriors, not just accurate outputs.
- **Guarantees and extrapolation**: a learned invariance holds only approximately and only near the training data, whereas a built-in one (an exact symmetry, a conservation law, physically valid light transport, a hard constraint) holds everywhere; structure beats statistics when correctness outside the data or verifiability is required.
- **Efficiency when data runs out**: scaling laws are power laws with small exponents, so each improvement costs multiplicatively more data and compute, and high-quality data is finite.[^6] A prior that improves the constant or the exponent of the scaling curve changes where performance ends up at a fixed budget, which is more than faster convergence.
- **Understanding why scaling works**: the Bayesian lens is a theory of [[Generalization|generalization]] ([[Bayesian Occam's Razor]], simplicity biases of gradient-based training, and the view that deep learning succeeds through good architectural priors combined with flexibility[^7]), and so predicts where scaling will fail, which the bitter lesson, as a historical observation, cannot.
- **Research heuristic**: avoid hand-built features for problems with large, cheap data sets; pursue priors that are general and composable with scale (symmetries, objectives, inference procedures, simulators) or essential where scale cannot go (single-instance, ill-posed, scarce-data, and decision-critical problems). For vision and graphics, the most promising overlap is learned generative priors combined with exact differentiable physical forward models inside a Bayesian inverse-problem formulation.

[^1]: [Sutton, The Bitter Lesson](zotero://open-pdf/library/items/7HZ94VF3?page=1)
[^2]: [Chung et al., Diffusion Posterior Sampling for General Noisy Inverse Problems (ICLR 2023)](https://arxiv.org/abs/2209.14687)
[^3]: [Poole et al., DreamFusion: Text-to-3D using 2D Diffusion (ICLR 2023)](https://arxiv.org/abs/2209.14988)
[^4]: [Müller et al., Transformers Can Do Bayesian Inference (ICLR 2022)](https://arxiv.org/abs/2112.10510)
[^5]: [Xie et al., An Explanation of In-context Learning as Implicit Bayesian Inference (ICLR 2022)](https://arxiv.org/abs/2111.02080)
[^6]: [Villalobos et al., Will We Run Out of Data? Limits of LLM Scaling Based on Human-Generated Data](https://arxiv.org/abs/2211.04325)
[^7]: [Wilson and Izmailov, Bayesian Deep Learning and a Probabilistic Perspective of Generalization (NeurIPS 2020)](https://arxiv.org/abs/2002.08791)
