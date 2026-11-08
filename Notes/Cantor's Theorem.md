---
tags:
  - mathematics
  - discrete_mathematics
---

# Definition

> [!abstract] Theorem 1 (Cantor's Theorem)[^1]
> The [[Power Set]] $\mathcal{P}(\mathbb{Z}^+)$ is uncountable: no function $f: \mathbb{Z}^+ \to \mathcal{P}(\mathbb{Z}^+)$ is [[Surjective Function|onto]].

> [!abstract] Theorem 2 (Cantor's Theorem, General Form)[^2]
> For every [[Set]] $A$, no function $f: A \to \mathcal{P}(A)$ is [[Surjective Function|onto]]. Hence $A$ and $\mathcal{P}(A)$ are not equinumerous, and since $a \mapsto \{a\}$ is an [[Injective Function|injection]] $A \to \mathcal{P}(A)$,
> $$
> \begin{align}
> |A| < |\mathcal{P}(A)|.
> \end{align}
> $$

Proof (diagonalization), by [[Proof by Contradiction|contradiction]]. Given any $f: A \to \mathcal{P}(A)$, let
$$
\begin{align}
D = \{a \in A : a \notin f(a)\} \in \mathcal{P}(A).
\end{align}
$$
If $D = f(d)$ for some $d \in A$, then by the definition of $D$, $d \in D \iff d \notin f(d) = D$, a contradiction. So $D$ is not in the image of $f$. The set $D$ differs from each $f(a)$ at the single test point $a$; listing the answers to "$a \in f(a)$?" in a table indexed by $(a, a')$, $D$ flips the diagonal, which is why the method is called diagonalization.

# Properties
- For finite $A$, $|\mathcal{P}(A)| = 2^{|A|} > |A|$ by counting. Cantor's theorem says the strict inequality persists for infinite sets, so there is no largest cardinality: $|A| < |\mathcal{P}(A)| < |\mathcal{P}(\mathcal{P}(A))| < \cdots$. For infinite $A$ the counting argument is circular, because "$2^{|A|} > |A|$" for infinite cardinals *is* Cantor's theorem.
- Composing with the injection $\mathcal{P}(\mathbb{Z}^+) \to \mathbb{R}$ that writes $A$ as the decimal $0.d_1d_2\ldots$ with $d_n = 7$ if $n \in A$ and $d_n = 3$ otherwise shows that $\mathbb{R}$ is uncountable ([[Cardinality of the Continuum]]).[^3]
- Equivalent to the [[Set of Binary Sequences Uncountability Theorem]], since a subset of $\mathbb{N}$ is the same as its indicator sequence.
- The same diagonal construction underlies Russell's paradox ($D = \{x : x \notin x\}$), Grelling's heterological paradox, the liar sentence (see [[Proposition]]), the undecidability of the halting problem, and Gödel's first incompleteness theorem. In each paradox, the contradiction refutes a hidden surjectivity assumption, e.g. that every definable property is named by some object in the collection.

# Questions
> [!question]- Why is the diagonal set $D = \{a : a \notin f(a)\}$ different from every $f(a)$?
> At the test point $a$: if $a \in f(a)$ then $a \notin D$, and if $a \notin f(a)$ then $a \in D$. So $D$ and $f(a)$ disagree about membership of $a$, hence $D \neq f(a)$ for every $a \in A$.

> [!question]- Does the theorem hold for $A = \varnothing$, and what does the proof's $D$ become?
> Yes. $\mathcal{P}(\varnothing) = \{\varnothing\}$ is nonempty, while the only function $\varnothing \to \mathcal{P}(\varnothing)$ is the empty function, whose image is empty, so it is not onto. The proof's $D$ is $\varnothing$, which is indeed not in the (empty) image.

> [!question]- Why can't you prove $|A| < |\mathcal{P}(A)|$ for infinite $A$ by noting $|\mathcal{P}(A)| = 2^{|A|}$?
> For infinite cardinals, $2^{|A|}$ is *defined* as the cardinality of the set of functions $A \to \{0,1\}$, which is $|\mathcal{P}(A)|$. The claim $2^{|A|} > |A|$ is then a restatement of Cantor's theorem, not evidence for it; finite counting doesn't transfer, since e.g. $|\mathbb{N}| = |2\mathbb{N}|$ although $2\mathbb{N} \subsetneq \mathbb{N}$.

> [!question]- Connection: Which paradox is Cantor's theorem in disguise, and what assumption does that paradox actually refute?
> Grelling's (and Russell's). Dictionary: adjective $w$ $\leftrightarrow$ element $a$; "$w$ describes $x$" $\leftrightarrow$ $x \in f(a)$; "heterological" $\leftrightarrow$ $D$; "'heterological' is heterological" $\leftrightarrow$ "$d \in D$" with $f(d) = D$. The paradox assumes that the property "heterological" is itself named by an adjective, i.e. that the naming map is onto. Cantor's argument shows that assumption is false, just as it refutes $D = f(d)$. Russell's paradox is the case "every collection is a set", which ZFC blocks by restricting comprehension.

[^1]: [HOW TO PROVE IT: A Structured Approach, Second Edition](zotero://open-pdf/library/items/THI2Q4PN?page=332)
[^2]: [HOW TO PROVE IT: A Structured Approach, Second Edition](zotero://open-pdf/library/items/THI2Q4PN?page=335)
[^3]: [HOW TO PROVE IT: A Structured Approach, Second Edition](zotero://open-pdf/library/items/THI2Q4PN?page=334)
