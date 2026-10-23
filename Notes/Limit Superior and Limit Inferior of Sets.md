---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!info] Limit Superior and Limit Inferior of a Sequence of Sets[^1]
> For a [[Sequence]] of [[Set|sets]] $\{E_n\}_{n=1}^\infty$,
> $$
> \begin{align}
> \limsup_{n \to \infty} E_n &= \bigcap_{k=1}^{\infty} \bigcup_{n=k}^{\infty} E_n = \{x : x \in E_n \text{ for infinitely many } n\} \\
> \liminf_{n \to \infty} E_n &= \bigcup_{k=1}^{\infty} \bigcap_{n=k}^{\infty} E_n = \{x : x \in E_n \text{ for all but finitely many } n\}
> \end{align}
> $$

The set analogue of [[Limit Supremum]] and [[Limit Infimum]] of a real sequence: $\bigcup_{n \geq k} E_n$ plays the role of $\sup_{n \geq k} x_n$ and $\bigcap_{n \geq k} E_n$ that of $\inf_{n \geq k} x_n$.

# Properties
- $\liminf E_n \subseteq \limsup E_n$; when they are equal, the common set is called $\lim E_n$.
- For a [[Nondecreasing Sequence of Sets]], $\liminf E_n = \limsup E_n = \bigcup_n E_n$; for a [[Nonincreasing Sequence of Sets]], both equal $\bigcap_n E_n$.
- In terms of indicator functions, $\chi_{\limsup E_n} = \limsup \chi_{E_n}$ and $\chi_{\liminf E_n} = \liminf \chi_{E_n}$.
- By De Morgan's laws, $\left(\limsup E_n\right)^c = \liminf E_n^c$.

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=15&annotation=N6BDBPBE)
