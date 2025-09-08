---
tags: mathematics, abstract_algebra
---

# Definition

> [!info] Definition 1 (Congruent Modulo)
> For $n \in \mathbb{N}$, $a, b \in \mathbb{Z}$ are congruent modulo $n$, denoted as $a \equiv b\ (\text{mod}\ n)$ if $n | (a - b)$, or alternatively, $tn = a - b$ for some $t \in \mathbb{Z}$

# Properties

- Congruence is an [[Equivalence Relation]]
- The following are equivalent:
	- $a \equiv b\ (\text{mod} n)$
	- $[a]_n = [b]_n$
	- $rem_n(a) = rem_n(b)$
	- $[a]_n \cap [b]_n \neq \emptyset$
- $a \equiv a'\ (\text{mod}\ n) \land b \equiv b'\ (\text{mod}\ n) \implies$
	- $a + b \equiv a' + b'\ (\text{mod}\ n)$
	- $ab \equiv a'b'\ (\text{mod}\ n)$

## [[Binomial Theorem]]/Prime Properties
- For $p$ is a [[Prime Number]]
	- $(a + b)^p \equiv a^p + b^p\ (\text{mod}\ p)$
	- [[Fermat's Little Theorem]]
	- [[Two Prime Fermat]]