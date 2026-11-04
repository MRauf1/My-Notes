---
tags:
  - statistics
  - mathematical_statistics
  - reinforcement_learning
---

# Definition
> [!abstract] Empirical Distribution L1 Concentration Bound[^1]
> Let $P$ be a distribution on a finite set $\mathcal{S}$, and let $\widehat{P} = \frac{1}{n}\sum_{i=1}^n \mathbf{e}_{s_i}$ be the empirical distribution of $n$ i.i.d. samples $s_i \sim P$ (the [[Multinomial Distribution Maximum Likelihood Estimation|multinomial MLE]]). With probability at least $1 - \delta$,
> $$
> \begin{align}
> \|\widehat{P} - P\|_1 \leq 2\sqrt{\frac{1}{2n}\ln\frac{2^{|\mathcal{S}|}}{\delta}} = \sqrt{\frac{2}{n}\Big(|\mathcal{S}|\ln 2 + \ln\frac{1}{\delta}\Big)} = \tilde{O}\Big(\sqrt{|\mathcal{S}|/n}\Big).
> \end{align}
> $$

# Properties
- **Proof.**
  1. Use the dual representation of the [[1-Norm]]: $\|v\|_1 = \max_{u \in \{-1,1\}^{|\mathcal{S}|}} u^\top v$.
  2. For a fixed $u$, $u^\top\widehat{P} = \frac{1}{n}\sum_i u^\top\mathbf{e}_{s_i}$ is an average of i.i.d. variables in $[-1, 1]$ with mean $u^\top P$. One-sided [[Hoeffding's Inequality]] gives $u^\top(\widehat{P} - P) \leq 2\sqrt{\frac{1}{2n}\ln\frac{1}{\delta'}}$ with probability $1 - \delta'$.
  3. A union bound ([[Boole's Inequality]]) over the $2^{|\mathcal{S}|}$ sign vectors with $\delta' = \delta/2^{|\mathcal{S}|}$ finishes the proof.
- Improves the entrywise approach: bounding each $|\widehat{P}(s') - P(s')|$ separately and summing gives $|\mathcal{S}|\sqrt{\frac{1}{2n}\ln\frac{2|\mathcal{S}|}{\delta}} = \tilde{O}(|\mathcal{S}|/\sqrt{n})$. The union bound costs only a $\ln 2^{|\mathcal{S}|} = O(|\mathcal{S}|)$ term inside the square root.
- A one-sided bound per $u$ suffices because the maximum over $u$ already includes $-u$, which saves a factor of $2$ inside the log. One can also skip $u = \pm\mathbf{1}$, for which $u^\top(\widehat{P} - P) \equiv 0$.
- $\|\widehat{P} - P\|_1$ is twice the total variation distance. In [[Certainty-Equivalence Sample Complexity]] this bound improves the $|\mathcal{S}|$ dependence to $\sqrt{|\mathcal{S}|}$.

# Questions
> [!question]- What is the proof idea of the $\ell_1$ concentration bound?
> Write $\|\widehat{P} - P\|_1 = \max_{u \in \{-1,1\}^{|\mathcal{S}|}} u^\top(\widehat{P} - P)$. Each fixed $u$ turns the vector deviation into a scalar average of i.i.d. bounded variables $u^\top\mathbf{e}_{s_i} \in [-1, 1]$, so Hoeffding's inequality applies. A union bound over the $2^{|\mathcal{S}|}$ choices of $u$ makes it uniform, and the max is then controlled.

> [!question]- Why is this tighter than summing per-coordinate Hoeffding bounds, and what does the union bound cost?
> Summing $|\mathcal{S}|$ coordinate errors, each of order $\sqrt{\ln(|\mathcal{S}|/\delta)/n}$, gives $|\mathcal{S}|/\sqrt{n}$: the errors are added in the worst case as if they all had the same sign. Testing against sign vectors directly captures the joint deviation. The price is a union bound over $2^{|\mathcal{S}|}$ events, but it enters only as $\ln 2^{|\mathcal{S}|} = |\mathcal{S}|\ln 2$ under the square root, giving $\sqrt{|\mathcal{S}|/n}$.

[^1]: [Jiang, Notes on Tabular Methods (CS 542 notes), pp. 4–5](https://nanjiang.cs.illinois.edu/files/cs542f22/note3.pdf#page=4)
