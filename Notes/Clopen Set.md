---
tags:
  - mathematics
  - complex_analysis
---

# Definition

> [!info] Definition 1 (Clopen [[Set]])
> [[Set]] that is both [[Open Set]] and [[Closed Set]].

"Open" and "closed" are not opposites (unlike a door) — a set can be neither, one, or both. Sets that are both open and closed are clopen.

My interpretation: the entire underlying set $X$ of a [[Metric Space]] $(X, d)$ is automatically both open and closed as a subset of itself (every point of $X$ trivially has a neighborhood contained in $X$, and $X$ has no limit points outside itself), and likewise $\emptyset$ is always clopen in any space. More generally, every [[Subset]] $Y$ of a metric space is clopen *relative to itself* — see [[Relatively Open Set]] for how this relates to whether $Y$ is open/closed relative to a larger ambient space.

# Examples
- $\emptyset$ and the full space $X$ are always clopen, in any [[Metric Space]].
- The entire real line $\mathbb{R}$ is clopen in itself: it is open (every point has room around it) and closed (its complement, $\emptyset$, is open).
- In a [[Disconnected Metric Space]], each separated piece is clopen relative to the whole space — e.g. in $(0,1) \cup (2,3) \subseteq \mathbb{R}$, the piece $(0,1)$ is both open and closed relative to that space.