---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Normalizing Flow Expressivity[^1]
> The question of which distributions a [[Normalizing Flow|normalizing flow]] can represent, given that its layers must be invertible and, for discrete flows, have cheap Jacobian determinants (usually via triangular Jacobians). In the limit the restriction costs nothing: triangular flows are universal, by the [[Knothe-Rosenblatt Rearrangement]]. In practice the limits are quantitative and topological: continuity, conditioning, depth, and data without a density.

# Properties
## Universality
- **Triangular maps suffice**: every absolutely continuous distribution is the pushforward of a standard normal under a single [[Monotone Triangular Map|monotone triangular map]], which is invertible with determinant $\prod_i \partial T_i / \partial x_i$. So requiring a [[Lower Triangular Matrix|lower-triangular]] Jacobian with positive diagonal guarantees invertibility and an $O(D)$ determinant without shrinking the set of reachable distributions.
- **Neural universality results**:[^2]
	- *Neural autoregressive flows*, with monotone neural-network transformers, are universal density approximators ([[Autoregressive Flow]]).
	- *Sum-of-squares polynomial flows* parameterize the triangular components as integrals of positive polynomials, directly mirroring the Knothe-Rosenblatt construction.
	- *Affine [[Coupling Flow|coupling flows]]* with permutations are universal approximators of diffeomorphisms, and hence distributionally universal.

## Caveats
Universality is an existence statement in the limit; it does not say the map is smooth, well-conditioned, or cheap to represent.
- **Topology**: a neural flow is continuous with continuous inverse, a homeomorphism of $\mathbb{R}^D$, so the pushforward of a Gaussian always has support $\mathbb{R}^D$, connected and without holes. A target with disconnected modes can only be approximated by thin, low-density bridges, and the flow's bi-[[Lipschitz Continuity|Lipschitz]] constant must diverge as the approximation improves. The Knothe-Rosenblatt map avoids this only by being discontinuous.[^3]
- **Conditioning and depth**: approximating hard targets may require very deep stacks or ill-conditioned layers; affine coupling flows can need ill-conditioning or large depth, finite-depth planar and radial flows provably cannot represent some simple distributions, and numerically, inverses can explode.[^4]
- **Ordering**: the triangular map depends on the variable order; a bad order makes the conditionals, and so the map, less smooth.
- **Data without a density**: the Knothe-Rosenblatt map requires an absolutely continuous target. Near-[[Mutually Singular Measures|singular]] data ([[Manifold Hypothesis]]) forces the Jacobian determinant toward $0$ and the inverse's Lipschitz constant toward $\infty$ ([[Manifold Overfitting]]). Here invertibility hurts, through dimension preservation rather than triangularity.
- **No bottleneck**: the latent has the full data dimension $D$, so every layer operates at full resolution ([[Multi-Scale Flow]] mitigates this).

## Evidence on why flows lagged
- **Invertible maps are not the bottleneck**: flow-matching models such as rectified-flow transformers ([[Flow Matching]]) and the [[Probability Flow ODE]] of diffusion models are [[Continuous Normalizing Flow|continuous normalizing flows]], invertible diffeomorphisms from noise to data, and they give state-of-the-art samples.[^5] They differ from classical flows in having free-form Jacobians (only a trace is needed) and in not being trained by maximum likelihood.
- **Triangular flows can compete**: transformer-based autoregressive flows (TarFlow, STARFlow), with triangular Jacobians, trained with noise augmentation, have been reported to reach sample quality close to diffusion models.[^6]
- **Verdict**: the triangular restriction is not what held flows back. More likely causes are weak per-layer transforms chosen for a cheap determinant (e.g. affine coupling), maximum-likelihood training on near-singular data, and the full-dimensional latent.

[^1]: Supplementary notes provided by the creator.
[^2]: Huang, Krueger, Lacoste & Courville (2018); Jaini, Selby & Yu (2019); Teshima et al. (2020) in `REFERENCES.md`.
[^3]: Cornish, Caterini, Deligiannidis & Doucet (2020); Dupont, Doucet & Teh (2019) in `REFERENCES.md`.
[^4]: Koehler, Mehta & Risteski (2021); Kong & Chaudhuri (2020); Behrmann, Vicol, Wang, Grosse & Jacobsen (2021) in `REFERENCES.md`.
[^5]: Lipman et al. (2023); Esser et al. (2024) in `REFERENCES.md`.
[^6]: Zhai et al. (2024); Gu et al. (2025) in `REFERENCES.md`.
