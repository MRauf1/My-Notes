---
tags:
  - computer_science
  - theoretical_computer_science
---

# Definition

> [!info] Definition 1 ([[Graph]] [[Distance]])[^1]
> On [[Graph]] $G$ with [[Vertex]] $v_1, v_2$, the distance between them, denoted as $d(v_1, v_2)$, is the length shortest [[Graph Path]] from $v_1$ to $v_2$.

# Properties
- [[Breadth-First Search]] visits every vertex reachable from a source $r$ in nondecreasing order of distance from $r$, making it the standard way to compute $d(r, \cdot)$ to every other vertex in an unweighted graph.[^2]

[^1]: [Building Blocks for Theoretical Computer Science](zotero://open-pdf/library/items/5IGT8C55?page=124)
[^2]: [Morin, p. 249](zotero://select/library/items/HYS8NDAB)