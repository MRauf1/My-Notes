---
tags:
  - mathematics
  - optimization
---

# Definition
> [!info] Mirror Descent (Online Learning on the Simplex)[^1]
> In rounds $k = 1, \dots, K$ on a finite set $\mathcal{X}$, a learner proposes $p_k \in \Delta(\mathcal{X})$, then nature reveals an arbitrary (possibly adversarial) gain $f_k : \mathcal{X} \to [0,1]$. Mirror descent with mirror map $\psi$ updates
> $$
> \begin{align}
> p_{k+1} = \arg\max_{p\in\Delta(\mathcal{X})}\ \eta\langle p, f_k\rangle - D_\psi(p \,\|\, p_k),
> \end{align}
> $$
> where $D_\psi$ is the [[Bregman Divergence]] of $\psi$. With $\psi$ the negative entropy, $D_\psi$ is the [[Kullback-Leibler Divergence]], and from uniform $p_1$ the update is multiplicative:
> $$
> \begin{align}
> p_{k+1}(x) \propto p_k(x)\exp(\eta f_k(x)).
> \end{align}
> $$

> [!abstract] Regret Guarantee[^1]
> With an appropriate $\eta$, for every comparator $p \in \Delta(\mathcal{X})$,
> $$
> \begin{align}
> \sum_{k=1}^K\langle p - p_k, f_k\rangle = O\big(\sqrt{K\log|\mathcal{X}|}\big).
> \end{align}
> $$
> For the entropic update, $\sum_k\langle p - p_k, f_k\rangle \leq \frac{\ln|\mathcal{X}|}{\eta} + \frac{\eta K}{8}$, so $\eta = \sqrt{8\ln|\mathcal{X}|/K}$ gives $\sqrt{\frac{K}{2}\ln|\mathcal{X}|}$ (Cesa-Bianchi & Lugosi 2006, Thm. 2.2).

# Properties
- Average regret $O(\sqrt{\log|\mathcal{X}|/K}) \to 0$ against any fixed distribution, even for adversarial gains. The dependence on $|\mathcal{X}|$ is only logarithmic.
- [[Gradient Descent]] is mirror descent with $\psi = \frac{1}{2}\|\cdot\|_2^2$. Other mirror maps adapt the geometry to the domain, e.g. entropy for the simplex.
- Running it independently in each state, with $\mathcal{X} = \mathcal{A}$ and $f_k = Q^{\pi^{(k)}}(s,\cdot)/V_{max}$, is exactly [[Natural Policy Gradient]] with softmax policies.
- An [[Online Algorithm]]: it never sees future gains.

# Questions
> [!question]- What is the proof idea of the entropic regret bound $\frac{\ln|\mathcal{X}|}{\eta} + \frac{\eta K}{8}$?
> Track the potential $W_k = \sum_x\exp(\eta\sum_{j<k}f_j(x))$, so $p_k(x) = \exp(\eta\sum_{j<k}f_j(x))/W_k$. Lower bound: $\ln\frac{W_{K+1}}{W_1} \geq \eta\sum_k f_k(x) - \ln|\mathcal{X}|$ for every $x$. Upper bound: $\ln\frac{W_{k+1}}{W_k} = \ln\mathbb{E}_{x\sim p_k}[e^{\eta f_k(x)}] \leq \eta\langle p_k, f_k\rangle + \frac{\eta^2}{8}$ by Hoeffding's lemma, since $f_k \in [0,1]$. Sum over $k$, compare, and divide by $\eta$. The regret is linear in $p$, so the bound for every point mass gives it for every $p \in \Delta(\mathcal{X})$.

[^1]: [Jiang, Notes on Importance Sampling and Policy Gradient (CS 542 notes), p. 10](https://nanjiang.cs.illinois.edu/files/cs542f23/note6.pdf#page=10)
