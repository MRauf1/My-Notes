---
tags:
  - computer_science
  - theoretical_computer_science
---

# Definition

> [!info] Definition 1 ([[Graph]] Walk)[^1]
> Walk of length $k$ is a [[Finite]] [[Sequence]] of [[Vertex]] $a = v_1, \dots, v_n = b$ and [[Edge]] $e_1, \dots, e_{n-1}$ in which $e_i$ connects $v_i$ to $v_{i + 1}$ for all $i$.
> One of the two is sufficient to describe a walk.

# Types
- [[Graph Path]]
- [[Graph Cycle]]

## Closed vs Open
- [[Closed Graph Walk]]
- [[Open Graph Walk]]

# Properties
- The number of walks of length $L$ from node $m$ to node $n$ is entry $(m, n)$ of the $L$th power of the [[Adjacency Matrix]].[^2]

[^1]: [Building Blocks for Theoretical Computer Science](zotero://open-pdf/library/items/5IGT8C55?page=122)
[^2]: [Prince, p. 245](zotero://open-pdf/library/items/BWT7FYX5?page=259&annotation=EJ8KERTG)
