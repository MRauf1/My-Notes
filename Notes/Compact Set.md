---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!info] Definition 1 (Compact [[Set]])[^1]
> [[Set]] $S$ is compact if every [[Open Cover]] of $S$ has a finite [[Subcover]].

A finite [[Set]] is always compact, since the entire [[Open Cover]] is itself already a finite [[Subcover]].[^2]

# Properties
- [[Heine-Borel Theorem]]
- [[Finite Intersection Property]]

> [!abstract] Theorem 2 (Compactness is Intrinsic)[^3]
> Let $(X, d)$ be a [[Metric Space]] and $K \subseteq Y \subseteq X$, where $Y$ inherits a [[Metric Space]] structure from $X$ by restricting $d$ to $Y$. Then $K$ is compact relative to $X$ if and only if $K$ is compact relative to $Y$.

Unlike being [[Open Set|open]] or [[Closed Set|closed]], which depend on the space a [[Subset]] is embedded in, compactness does not. It is therefore meaningful to speak of a "[[Compact Metric Space|compact metric space]]" on its own terms, with no reference to any ambient space — whereas "open space" or "closed space" would not be meaningful, since every [[Metric Space]] is both open and closed in itself.

> [!abstract] Theorem 3 (Compact Sets are Closed)[^4]
> Let $(X, d)$ be a [[Metric Space]] and $K \subseteq X$ be compact. Then $K$ is [[Closed Set|closed]] in $X$.

> [!abstract] Theorem 4 (Closed Subsets of Compact Sets are Compact)[^4]
> Let $(X, d)$ be a [[Metric Space]], $K \subseteq X$ be compact, and $F \subseteq K$ be [[Closed Set|closed]] in $X$. Then $F$ is compact.

> [!abstract] Corollary 5[^5]
> Let $(X, d)$ be a [[Metric Space]], $F \subseteq X$ be [[Closed Set|closed]], and $K \subseteq X$ be compact. Then $F \cap K$ is compact.

[^1]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=102)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=45)
[^3]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=46)
[^4]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=46)
[^5]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=47)