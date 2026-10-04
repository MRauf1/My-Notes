---
tags:
  - mathematics
  - complex_analysis
---

# Definition

See [[Open Set]].

> [!info] Definition 1 (Interior of a Set)[^1]
> Let $(S, d)$ be a [[Metric Space]] and $E \subseteq S$. The interior of $E$, denoted $E^{\circ}$, is the set of all [[Interior Point|interior points]] of $E$.

> [!abstract] Theorem 2 ($E^{\circ}$ is Always Open)[^1]
> Let $(S, d)$ be a [[Metric Space]] and $E \subseteq S$. Then $E^{\circ}$ is an [[Open Set]].

> [!abstract] Theorem 3 ($E^{\circ}$ is the Largest Open Subset)[^1]
> Let $(S, d)$ be a [[Metric Space]] and $E \subseteq S$. If $G \subseteq E$ and $G$ is [[Open Set|open]], then $G \subseteq E^{\circ}$.

> [!abstract] Theorem 4 (Interior-Closure Duality)[^1]
> Let $(S, d)$ be a [[Metric Space]] and $E \subseteq S$, with [[Set Complement|complement]] $E^c = S \setminus E$. Then $(E^{\circ})^c = (E^c)^-$, i.e. the complement of the interior of $E$ equals the [[Closure Set|closure]] of the complement of $E$.

Also recall $E$ is open if and only if $E^{\circ} = E$ — see [[Open Set]].

# Properties
- $E^{\circ} = E \setminus \partial E$, where $\partial E$ is [[Boundary Set]]

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=52)