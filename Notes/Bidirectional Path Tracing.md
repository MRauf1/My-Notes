---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Bidirectional Path Tracing (BDPT)[^1]
> Grow a sub-path of $s$ vertices from a source and a sub-path of $t$ vertices from the sensor, and join them:
> $$
> \begin{align}
> \bar{x}_{s,t} = (y_0,\dots,y_{s-1}, z_{t-1},\dots,z_0), \qquad p_{s,t}(\bar{x}_{s,t}) = p^L(y_0,\dots,y_{s-1})\,p^E(z_0,\dots,z_{t-1})
> \end{align}
> $$
> Every pair $(s,t)$ with $s+t=k$ is a different strategy for sampling the same $k$-vertex paths — $k+1$ strategies in total. Path tracing is the case $s \in \{0,1\}$; particle tracing is $t \in \{0,1\}$; combining every $(s,t)$ via [[Multiple Importance Sampling]] over the whole table is bidirectional path tracing.

# Properties
- A generalization of [[Path Tracing (Recursive Estimator)|path tracing]] and particle tracing that combines both directions of [[Local Path Sampling]] via [[Multiple Importance Sampling]].

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
