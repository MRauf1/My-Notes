---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Sparse Sampling[^1]
> An online [[Planning|planning]] algorithm (Kearns, Mansour & Ng 2002) that computes $\pi^\star(s_0)$ for a single given state $s_0$ using a [[Generative Model (Reinforcement Learning)|generative model]]. Conceptually, it runs tabular [[Certainty-Equivalence (Reinforcement Learning)|certainty-equivalence]] with $n$ samples per state-action pair, chosen by the $|\mathcal{S}|$-free analysis. It generates data *lazily*: only for state-action pairs that contribute to computing $V^\star_{\widehat{M}}(s_0)$, truncated at the [[Effective Horizon]].

# Properties
- Uses roughly $(n|\mathcal{A}|)^{O(1/(1-\gamma))}$ samples to compute $\pi^\star(s_0)$, with no dependence on $|\mathcal{S}|$. That makes it usable when the state space is huge or infinite: exponential in the horizon, but independent of the number of states.
- Rests on the fact that, in the [[Certainty-Equivalence Sample Complexity]] analysis via $Q^\star_M$, the number of samples needed per $(s,a)$ does not depend on $|\mathcal{S}|$.
- A prototype for the family of Monte-Carlo tree search algorithms (which played a crucial role in AlphaGo).

[^1]: [Jiang, Notes on Tabular Methods (CS 542 notes), pp. 6–7](https://nanjiang.cs.illinois.edu/files/cs542f22/note3.pdf#page=6)
