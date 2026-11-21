---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Degenerate Distribution[^1]
> A [[Random Variable]] $X$ has a degenerate distribution at a constant $a$ if $P(X = a) = 1$. Equivalently, $E[(X - a)^2] = 0$.

> [!abstract] Theorem 1 (Zero Mean-Square Characterization)[^2]
> For a [[Random Variable]] $X$ and a constant $a$,
> $$
> \begin{align}
> E[(X - a)^2] = 0 \iff P(X = a) = 1
> \end{align}
> $$

**Proof.** ($\Leftarrow$) $(X-a)^2 = 0$ with probability $1$, so its [[Expectation]] is $0$. ($\Rightarrow$) Apply [[Markov's Inequality]] to $u(X) = (X-a)^2 \geq 0$: for every $\varepsilon > 0$,
$$
\begin{align}
P(|X - a| \geq \varepsilon) = P\left((X-a)^2 \geq \varepsilon^2\right) \leq \frac{E[(X-a)^2]}{\varepsilon^2} = 0.
\end{align}
$$
Since $\{X \neq a\} = \bigcup_{n \geq 1} \{|X - a| \geq 1/n\}$, countable subadditivity gives $P(X \neq a) \leq \sum_n 0 = 0$. $\blacksquare$

This is the probabilistic form of "$g \geq 0$ and $\int g\,d\mu = 0$ imply $g = 0$ [[Almost Everywhere|a.e.]]", with $g = (X-a)^2$ and $\mu = P$. The passage from "$P(|X-a| \geq \varepsilon) = 0$ for every $\varepsilon$" to "$P(X \neq a) = 0$" needs countable additivity: it is a union over $n$, not a statement about a single $\varepsilon$.

# Properties
- The distribution of a constant: its [[Random Variable Support|support]] is the single point $\{a\}$ and its [[Cumulative Distribution Function|cdf]] is the unit step $F(x) = \mathbb{1}\{x \geq a\}$.
- $E(X) = a$ and $\text{Var}(X) = 0$; conversely $\text{Var}(X) = 0$ implies $X$ is degenerate at $\mu$, so the [[Standard Deviation]] is $0$ exactly for degenerate distributions.
- Its [[Moment Generating Function|mgf]] is $M(t) = e^{at}$ for all $t$.
- It is the equality case of [[Jensen's Inequality]] for strictly convex $\varphi$.

# Questions
> [!question]- Why does $P(|X-a| \geq \varepsilon) = 0$ for every $\varepsilon > 0$ imply $P(X = a) = 1$, and which axiom does the step use?
> $\{X \neq a\} = \bigcup_{n\geq 1}\{|X-a| \geq 1/n\}$ is a countable union of null events, so $P(X \neq a) \leq \sum_n P(|X-a|\geq 1/n) = 0$ by countable subadditivity, a consequence of countable additivity. No single $\varepsilon$ suffices, since $\{|X-a| \geq \varepsilon\}$ misses the values with $0 < |X - a| < \varepsilon$.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=92)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=95) (Markov's inequality, Thm 1.10.2; the characterization is a standard consequence)
