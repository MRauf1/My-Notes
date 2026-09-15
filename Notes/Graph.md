---
tags:
  - computer_science
  - theoretical_computer_science
---

# Definition

> [!info] Definition 1 (Graph)[^1]
> Graph $G$ is $(V, E)$ where $V$ is the [[Set]] of [[Vertex]] and $E$ is the [[Set]] of [[Edge]].

By convention, when treating $G$ algorithmically, $n = |V|$ and $m = |E|$ denote its vertex and edge counts, and $V$ is taken to be $\{0, \dots, n-1\}$, so any further data associated with a vertex can be stored in an array of length $n$.[^2] A vertex $v_j$ is **reachable** from $v_i$ if there is a [[Graph Path|path]] from $v_i$ to $v_j$.[^2]

# Operations
Typical operations on a graph data structure:[^3]
- `add_edge(i, j)` / `remove_edge(i, j)`: add or remove the edge $(i, j)$.
- `has_edge(i, j)`: check whether $(i, j) \in E$.
- `out_edges(i)`: list every $j$ with $(i, j) \in E$.
- `in_edges(i)`: list every $j$ with $(j, i) \in E$.

# Representations
- [[Adjacency Matrix]]: constant-time edge queries/updates, $O(n^2)$ space — good for dense graphs.
- [[Adjacency Lists]]: constant-time `add_edge`/`out_edges`, $O(n+m)$ space — good for sparse graphs and for traversal algorithms.

# Types
- [[Simple Graph]]
- [[Tree]]

## Substructure
- [[Subgraph]]

## Direction
- [[Undirected Graph]]
- [[Directed Graph]]

## [[Graph Cycle]]
- [[Acyclic Graph]]

## Connectivity
- [[Connected Graph]]

# Examples
- [[Complete Graph]]
- [[Cycle Graph]]
- [[Wheel Graph]]
- [[Bipartite Graph]]

# Properties
- [[Graph Isomorphism]]

## Walks
- [[Graph Walk]]
- [[Graph Path]]
- [[Graph Cycle]]
- [[Graph Euler Circuit]]

## Connectivity
- [[Graph Connected Components]]

## Distance
- [[Graph Distance]]
- [[Graph Diameter]]

## Coloring
- [[Graph Coloring]]

## Exploration
- [[Breadth-First Search]] and [[Depth-First Search]] can both explore a graph from a source vertex to find every reachable vertex in $O(n+m)$ time when the graph is stored as an [[Adjacency Lists|Adjacency List]].

[^1]: [Building Blocks for Theoretical Computer Science](zotero://open-pdf/library/items/5IGT8C55?page=115)
[^2]: [Morin, p. 240](zotero://select/library/items/HYS8NDAB)
[^3]: [Morin, p. 240](zotero://select/library/items/HYS8NDAB)