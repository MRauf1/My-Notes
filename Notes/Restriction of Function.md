---
tags:
  - mathematics
  - topology
---

# Definition
> [!info] Restriction of Function[^1]
> Let $f: A \to B$ be a [[Function]] and $A_0 \subseteq A$. The restriction of $f$ to $A_0$ is the function $f|_{A_0}: A_0 \to B$ whose rule is
> $$
> \begin{align}
> f|_{A_0} = \{(a, f(a)) \mid a \in A_0\}.
> \end{align}
> $$
> $f|_{A_0}$ is read "$f$ restricted to $A_0$".

The restriction keeps the rule of $f$ and only shrinks its [[Domain]]; it is the opposite operation to an [[Extension of Function]] ($f$ is an extension of $f|_{A_0}$).

# Properties
- $f|_{A_0} = f \circ \iota$, where $\iota: A_0 \hookrightarrow A$ is the inclusion map (see [[Function Composition]]).
- Restricting an [[Injective Function]] gives an injective function; restricting the domain may destroy surjectivity.
- Used in the recursion formula of the [[Principle of Recursive Definition]], $h(i) = \rho(h|_{\{1, \dots, i-1\}})$.

[^1]: [Topology (Munkres)](zotero://open-pdf/library/items/2AUACM23?page=19&annotation=73CT2ZNU)
