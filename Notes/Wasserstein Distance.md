---
tags:
  - computer_science
  - machine_learning
---

# Definition
> [!info] Wasserstein Distance (Earth Mover's Distance)[^1][^2]
> The minimum work needed to transport the probability mass of one distribution to create the other, where work is mass multiplied by distance moved. For distributions $Pr(\mathbf{x})$ and $q(\mathbf{x})$, minimize over **transport plans** $\pi(\mathbf{x}_1, \mathbf{x}_2) \geq 0$, the mass moved from $\mathbf{x}_1$ to $\mathbf{x}_2$, whose marginals are the two distributions:
> $$
> \begin{align}
> D_w\left[Pr(\mathbf{x}), q(\mathbf{x})\right] = \min_{\pi[\bullet, \bullet]}\left[\iint \pi(\mathbf{x}_1, \mathbf{x}_2) \cdot \|\mathbf{x}_1 - \mathbf{x}_2\| \, d\mathbf{x}_1 d\mathbf{x}_2\right], \quad \int \pi(\mathbf{x}_1, \mathbf{x}_2)\, d\mathbf{x}_2 = Pr(\mathbf{x}_1), \quad \int \pi(\mathbf{x}_1, \mathbf{x}_2)\, d\mathbf{x}_1 = q(\mathbf{x}_2)
> \end{align}
> $$
>
> **Discrete case** (earth mover's distance) over $K$ bins with cost $|i - j|$ of moving a unit of mass from bin $i$ to bin $j$ and transport plan matrix $\mathbf{P}$:
> $$
> \begin{align}
> D_w\left[Pr(x) \,\|\, q(x)\right] = \min_{\mathbf{P}}\left[\sum_{i,j} P_{ij} \cdot |i - j|\right], \quad \sum_j P_{ij} = Pr(x = i), \quad \sum_i P_{ij} = q(x = j), \quad P_{ij} \geq 0
> \end{align}
> $$

# Properties
- **Well-behaved for disjoint distributions**: it remains finite and informative when the supports do not overlap and decreases smoothly as the distributions approach each other, unlike the [[Jensen-Shannon Divergence]], which saturates.[^1]
- **Linear program**: the discrete case is a [[Linear Programming|linear program]] in primal form $\min \mathbf{c}^T\mathbf{p}$ s.t. $\mathbf{A}\mathbf{p} = \mathbf{b}$, $\mathbf{p} \geq \mathbf{0}$, with $\mathbf{p}$ the vectorized $P_{ij}$, $\mathbf{c}$ the distances, and $\mathbf{A}\mathbf{p} = \mathbf{b}$ the marginal constraints. Its dual $\max \mathbf{b}^T\mathbf{f}$ s.t. $\mathbf{A}^T\mathbf{f} \leq \mathbf{c}$ has the same optimum:[^3][^4]
$$
\begin{align}
D_w\left[Pr(x) \,\|\, q(x)\right] = \max_{\mathbf{f}}\left[\sum_i Pr(x = i) f_i - \sum_j q(x = j) f_j\right], \quad |f_{i+1} - f_i| \leq 1
\end{align}
$$
  i.e. an optimization over values $\{f_i\}$ whose adjacent entries change by at most one.
- **Kantorovich–Rubinstein duality** (continuous dual): the maximum over functions $f$ with [[Lipschitz Continuity|Lipschitz constant]] at most one (absolute gradient at most one):[^2]
$$
\begin{align}
D_w\left[Pr(\mathbf{x}), q(\mathbf{x})\right] = \max_{f[\mathbf{x}]}\left[\int Pr(\mathbf{x}) f[\mathbf{x}]\, d\mathbf{x} - \int q(\mathbf{x}) f[\mathbf{x}]\, d\mathbf{x}\right]
\end{align}
$$
  This form only needs expectations, so it can be estimated from samples; it is the basis of the [[Wasserstein GAN]].
- **General case**: the $p$-Wasserstein distance $W_p(p, q) = \left(\inf_{\gamma \in \Gamma(p, q)} \mathbb{E}_{(\mathbf{a}, \mathbf{b}) \sim \gamma}\|\mathbf{a} - \mathbf{b}\|^p\right)^{1/p}$ over couplings $\gamma$; the above is $W_1$, and the [[Fréchet Inception Distance]] uses $W_2$ between Gaussians. $W_p$ is a [[Metric|metric]] on probability distributions.
- Computing the primal requires solving a constrained minimization each time, which is easy for small discrete systems but not in high dimensions.[^3]

[^1]: [Prince, p. 284](zotero://open-pdf/library/items/BWT7FYX5?page=298&annotation=5I685ZVX); [Prince, p. 284](zotero://open-pdf/library/items/BWT7FYX5?page=298&annotation=X94QYTMP)
[^2]: [Prince, p. 286](zotero://open-pdf/library/items/BWT7FYX5?page=300&annotation=FZFKPFZT)
[^3]: [Prince, p. 285](zotero://open-pdf/library/items/BWT7FYX5?page=299&annotation=EZVCDZ3C)
[^4]: [Prince, p. 286](zotero://open-pdf/library/items/BWT7FYX5?page=300&annotation=W6W6WZ6F)
