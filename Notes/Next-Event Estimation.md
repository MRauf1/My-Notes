---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Next-Event Estimation[^1]
> At every vertex of a [[Local Path Sampling|locally sampled]] path, in addition to continuing the walk, sample a point $y$ directly on a source and connect to it — one extra visibility query per vertex.

Sampling the source directly beats waiting for a random walk to land on it; if the source is small, waiting means a variance the estimator cannot afford. The connection is a [[Geometric Term (Light Transport)|geometric term]] $\hat{G}$, visibility included. It fails when the connection is blocked, and when the scattering kernel at that vertex is nearly a delta function — a mirror connects to nothing.

# Properties
- Combined with the continuation of the walk via [[Multiple Importance Sampling]], since the two estimate the same path by two different, correlated strategies.

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
