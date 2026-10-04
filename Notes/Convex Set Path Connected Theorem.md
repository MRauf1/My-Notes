---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!abstract] Theorem 1 ([[Convex Set]] [[Path Connected Metric Space]] Theorem)[^1]
> [[Convex Set]] $E \subseteq \mathbb{R}^n$ are always [[Path Connected Metric Space|path connected]] sets

> [!abstract] Theorem 2 (General Case: Convex Subsets of Any Normed Space)
> Let $(V, \lVert \cdot \rVert)$ be a [[Normed Space]] whose scalars contain $\mathbb{R}$ (e.g. a real or complex normed space, hence a [[Metric Space]] under $d(x, y) = \lVert x - y \rVert$, since the norm is always real-valued), and let $E \subseteq V$ be [[Convex Set|convex]]. Then $E$ is [[Path Connected Metric Space|path connected]].

Theorem 1 ($\mathbb{R}^n$) is the special case of Theorem 2 where $V = \mathbb{R}^n$ with the Euclidean norm. The convexity condition $tx + (1-t)y \in E$ only requires addition and REAL scalar multiplication, and the straight-line path $\alpha(t) = (1-t)x + ty$ for real $t \in [0, 1]$ is continuous in any normed space regardless of its scalar field, so the same argument carries over unchanged to $\mathbb{C}^n$, quaternionic spaces, and infinite-dimensional spaces (e.g. function spaces, [[Hilbert Space|Hilbert]] or [[Banach Space|Banach]] spaces).

> [!abstract] Corollary 3 (Convex Sets are Connected)
> Every [[Convex Set|convex]] subset of $\mathbb{R}^n$, or more generally of any real [[Normed Space]], is [[Connected Metric Space|connected]].

This follows immediately from Theorems 1–2 together with the fact that [[Path Connected Metric Space|path connectedness]] implies [[Connected Metric Space|connectedness]].

[^1]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=193)