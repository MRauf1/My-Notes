---
tags:
  - mathematics
  - real_analysis
---

# Definition
> [!info] Lipschitz Continuity[^1]
> A function $f: X \to Y$ between [[Metric Space|metric spaces]] is Lipschitz continuous if there exists a constant $L \geq 0$ such that
> $$
> \begin{align}
> d_Y(f(x), f(x')) \leq L\, d_X(x, x') \quad \forall x, x' \in X
> \end{align}
> $$
> The smallest such $L$ is the **Lipschitz constant** of $f$.

# Properties
- Lipschitz continuity implies uniform continuity.
- If $L < 1$, $f: X \to X$ is a [[Contraction]] and, on a complete space, has a unique fixed point ([[Banach Fixed-Point Theorem]]).
- For differentiable $f: \mathbb{R}^n \to \mathbb{R}^m$ on a convex domain, the Lipschitz constant w.r.t. the Euclidean norm is $\sup_{\mathbf{x}} \|\mathbf{J}_f(\mathbf{x})\|_2$, the supremum of the largest [[Singular Value|singular value]] of the [[Jacobian Matrix]].
- **Composition**: $\mathrm{Lip}(g \circ f) \leq \mathrm{Lip}(g)\,\mathrm{Lip}(f)$. For a network layer $\mathrm{a}[\boldsymbol{\beta} + \boldsymbol{\Omega}\mathbf{h}]$ with activation slopes at most one, the Lipschitz constant is at most the largest singular value of $\boldsymbol{\Omega}$, which is how contractive [[Residual Flow|residual flows]] are made invertible.[^1]
- The critic of a [[Wasserstein GAN]] is constrained to be 1-Lipschitz, the dual form of the [[Wasserstein Distance]].

[^1]: [Prince, p. 316](zotero://open-pdf/library/items/BWT7FYX5?page=330&annotation=W5C73CL7); [Prince, p. 317](zotero://open-pdf/library/items/BWT7FYX5?page=331&annotation=7UL48MRD)
