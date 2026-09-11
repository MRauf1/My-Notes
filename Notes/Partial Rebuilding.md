---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Partial Rebuilding (`rebuild(u)`)[^1]
> A rebalancing technique that deconstructs the subtree rooted at a node $u$ and reconstructs it into a perfectly balanced subtree: traverse $u$'s subtree, gather all its nodes into a sorted array $a$, then recursively rebuild — with $m = \lfloor \text{length}(a)/2 \rfloor$, $a[m]$ becomes the new root, $a[0], \dots, a[m-1]$ are recursively rebuilt into the left subtree, and $a[m+1], \dots, a[\text{length}(a)-1]$ into the right subtree.

# Properties
- A call to `rebuild(u)` takes $O(\text{size}(u))$ time, where $\text{size}(u)$ is the number of nodes in $u$'s subtree.[^2]
- The resulting subtree has minimum height: no [[Binary Tree]] with $\text{size}(u)$ nodes has a smaller height.[^2]
- Used by [[Scapegoat Tree]] to restore balance after `add(x)`/`remove(x)`, instead of the local, per-node restructuring that a [[Tree Rotation]] performs in a [[Treap]].

[^1]: [Morin, p. 165](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 166](zotero://select/library/items/HYS8NDAB)
