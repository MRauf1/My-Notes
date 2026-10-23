---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Common Random Numbers[^1]
> To compare the effect of candidate input distributions $F, G, H, \dots$ on a simulation, drive every candidate with the same uniforms $U_i$: generate $X_i = F^{-1}(U_i)$, $X_i = G^{-1}(U_i)$, $X_i = H^{-1}(U_i)$, respectively, instead of simulating each candidate with independent random numbers.

Differences between the simulated outputs are then due to the distributions rather than to independent sampling noise, giving much sharper comparisons. [[Inverse Transform Sampling]] is the natural way to do this because it uses exactly one uniform per variate and is monotone in $U$, so large $U$ maps to large $X$ under every candidate. Complementary inversion $F^{-1}(1-U)$ breaks that correspondence, so ordinary inversion is required here.

# Properties
- A variance reduction technique of the [[Monte Carlo Method]], alongside [[Antithetic Variates]] and [[Stratified Sampling]], both of which also pair naturally with inversion.
- Inputs can be transferred between distributions via the [[QQ Transformation]].

[^1]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=6&annotation=YIPI2SQ8); [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=6&annotation=FLYWP7LE)
