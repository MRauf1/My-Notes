---
tags:
  - mathematics
  - discrete_mathematics
---

# Definition

> [!info] Definition 1 (Closure of a Set Under a Function)[^1]
> Let $f: A \to A$. A set $C \subseteq A$ is closed under $f$ if $\forall x \in C\,(f(x) \in C)$. For $B \subseteq A$, the closure of $B$ under $f$ is the smallest set $C$ with $B \subseteq C \subseteq A$ that is closed under $f$.

> [!abstract] Theorem 2 (Existence)[^1]
> The closure of $B$ under $f$ always exists, and can be built in two ways:
> $$
> \begin{align}
> \text{(top-down)} \quad &\bigcap \{C \mid B \subseteq C \subseteq A,\ C \text{ closed under } f\} \\
> \text{(bottom-up)} \quad &\bigcup_{n \in \mathbb{Z}^+} B_n, \qquad B_1 = B,\ B_{n+1} = f(B_n)
> \end{align}
> $$

# Properties
- The top-down construction works because the family is nonempty ($A$ itself is in it), and an intersection of closed sets is closed ([[Collection of Set]]).
- The bottom-up construction is closed because $x \in B_n \Rightarrow f(x) \in B_{n+1}$. It is the smallest because [[Proof by Induction]] on $n$ shows every $B_n \subseteq C$ for any closed $C \supseteq B$.
- The same works for a family of functions, or for functions $f: A \times A \to A$ ([[Operation Closure]]). Example: the closure of the primes under multiplication is $\{n \in \mathbb{Z} \mid n \geq 2\}$, by the [[Natural Number Prime Factorization|prime factorization]] of integers $\geq 2$.
- Same "smallest superset with a property" pattern as [[Reflexive Closure]], [[Symmetric Closure]] and [[Transitive Closure]].

[^1]: [HOW TO PROVE IT: A Structured Approach, Second Edition](zotero://open-pdf/library/items/THI2Q4PN?page=317)
