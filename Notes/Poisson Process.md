---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Poisson Process[^1]
> Let $X_t$ count the occurrences of some event in the interval $(0, t]$, and write $g(k, t) = P(X_t = k)$. $\{X_t\}$ is a Poisson process with rate $\lambda > 0$ if
> 1. $g(1, h) = \lambda h + o(h)$,
> 2. $\sum_{k=2}^\infty g(k, h) = o(h)$,
> 3. the numbers of occurrences in nonoverlapping intervals are independent,
>
> where $o(h)/h \to 0$ as $h \to 0$. Then $X_t$ has a [[Poisson Distribution]] with parameter $\lambda t$.

Axioms 1 and 2 say that in a very short interval of length $h$ there is either no event or one event, with probability of one event proportional to $h$; axiom 3 says events do not influence each other. The "time" axis can be any continuous measure of exposure, e.g. length of wire or area of a surface.

**Connection to the gamma distribution.**[^2] Counting and waiting are two views of the same process. The waiting time $W_k$ until the $k$th event exceeds $w$ exactly when fewer than $k$ events occur in $(0, w]$:
$$
\begin{align}
\{W_k > w\} = \{X_w \leq k - 1\}
\end{align}
$$
so the Poisson cdf of the count determines the distribution of the wait. The result is that $W_k \sim$ [[Gamma Distribution|Gamma]]$(k, 1/\lambda)$ (shape $k$, scale $1/\lambda$). Equivalently, the interarrival times $T_1, T_2, \dots$ (time between successive events) are [[Independent and Identically Distributed|iid]] [[Exponential Distribution|exponential]] with mean $1/\lambda$, and $W_k = T_1 + \dots + T_k$ is gamma by [[Gamma Distribution Addition]]. Intuitively: $\lambda$ events are expected per unit time, so the first event is expected at time $1/\lambda$, and waiting for $k$ events means adding $k$ independent memoryless waits.

# Properties
- $E(X_t) = \text{Var}(X_t) = \lambda t$.
- Memorylessness of the exponential interarrival times is the continuous-time form of axiom 3: the process restarts afresh at every instant.
- Merging independent Poisson processes gives a Poisson process with the summed rate ([[Poisson Distribution Addition]]); randomly thinning one with probability $p$ gives a Poisson process with rate $p\lambda$.
- Used for photon arrivals, radioactive decay, and free-flight distances in participating media, where the exponential waiting time is sampled by [[Inverse Transform Sampling]].

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=184)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=193)
