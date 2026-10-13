---
tags:
  - mathematics
  - calculus
---

# Definition

> [!info] Definition 1 (Left-Sided [[Limit of Function]])[^1]
> $\lim_{x \rightarrow a^-} f(x) = L$ if for every number $\epsilon > 0$, there exists $\delta > 0$ such that
> $$
> \begin{align}
> a - \delta < x < a \implies |f(x) - L| < \epsilon
> \end{align}
> $$

Limit of a [[Function]] $f(x)$ as $x \rightarrow a$ is $L$ from the left whenever $f(x)$ is arbitrarily close to $L$ for values of $x$ that are arbitrarily close to $a$ and less than $a$.

> [!info] Definition 2 (Right-Sided [[Limit of Function]])
> $\lim_{x \rightarrow a^+} f(x) = L$ if for every number $\epsilon > 0$, there exists $\delta > 0$ such that
> $$
> \begin{align}
> a < x < a + \delta \implies |f(x) - L| < \epsilon
> \end{align}
> $$

Limit of a [[Function]] $f(x)$ as $x \rightarrow a$ is $L$ from the right whenever $f(x)$ is arbitrarily close to $L$ for values of $x$ that are arbitrarily close to $a$ and greater than $a$.

> [!info] Definition 3 (Sequential One-Sided Limits)[^2]
> Let $f$ be defined on $(a, b)$. For $a \leq x < b$, we write $f(x^+) = q$ if $f(t_n) \rightarrow q$ as $n \rightarrow \infty$ for all sequences $\{t_n\}$ in $(x, b)$ such that $t_n \rightarrow x$. For $a < x \leq b$, $f(x^-)$ is defined analogously using sequences in $(a, x)$.

For $x \in (a, b)$, $\lim_{t \rightarrow x} f(t)$ exists if and only if $f(x^+) = f(x^-) = \lim_{t \rightarrow x} f(t)$ ([[Limit of Function and One-Sided Limit of Function Theorem]]).

# Properties
- [[One-Sided Limit of Even Function]]
- Classify [[Discontinuity|discontinuities]]: [[Simple Discontinuity]] vs [[Discontinuity of the Second Kind]]
- [[Monotonic Function One-Sided Limit Theorem]]

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=141)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=103)
