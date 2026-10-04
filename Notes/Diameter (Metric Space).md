---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!info] Definition 1 (Diameter of a Set)[^1]
> Let $(X, d)$ be a [[Metric Space]] and $E \subseteq X$ nonempty. Let $S$ be the set of all real numbers of the form $d(p, q)$ with $p, q \in E$. The diameter of $E$ is $\operatorname{diam}(E) = \sup S$.

> [!abstract] Theorem 2 (Cauchy Sequences via Diameter)[^2]
> Let $(X,d)$ be a [[Metric Space]] and $\{p_n\}$ a [[Sequence]] in $X$. For $N \in \mathbb{N}$, let $E_N = \{p_N, p_{N+1}, p_{N+2}, \dots\}$. Then $\{p_n\}$ is a [[Cauchy Sequence]] if and only if $\lim_{N \to \infty} \operatorname{diam}(E_N) = 0$.

> [!abstract] Theorem 3[^3]
> Let $(X, d)$ be a [[Metric Space]].
> (a) If $E \subseteq X$ and $E^-$ is its [[Closure Set|closure]], then $\operatorname{diam}(E^-) = \operatorname{diam}(E)$.
> (b) If $\{K_n\}$ is a sequence of [[Compact Set|compact]] subsets of $X$ with $K_n \supseteq K_{n+1}$ for all $n$, and $\lim_{n \to \infty} \operatorname{diam}(K_n) = 0$, then $\bigcap_{n=1}^{\infty} K_n$ consists of exactly one point.

# Properties
- [[Finite Intersection Property]]
- [[Nested Interval Theorem]]

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=61)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=61)
[^3]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=61)
