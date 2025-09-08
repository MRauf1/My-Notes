---
tags: mathematics, abstract_algebra
---

# Definition

> [!info] Definition 1 (Coset)
> For $H \leq G$, $g \in G$, $H$ has left and right cosets which are found by left/right multiplying $H$ by $g$

# Types
- [[Left Coset]]
- [[Right Coset]]

# Properties

Unless specified, all properties that holds for left cosets also hold for right cosets

## [[Disjoint Sets]]
- For $H \leq G$, if $X, Y \subseteq G$ are left $H$ cosets, then either 
	1) $X, Y$ are disjoint, or
	2) $X = Y$
- In other words, the distinct left cosets are pairwise disjoint

## [[Cardinality]]
- Every left coset has the same cardinality as $H$
- [[Lagrange's Theorem]]
	- [[Generalized Lagrange's Theorem]]
- [[Order Theorem]]

## Left vs. Right Cosets
- There is the same number of left cosets as right cosets because there exists a [[Bijective|bijection]] between the two

## Other
- The following are equivalent
	- $a \in bH$
	- $b \in aH$
	- $aH = bH$
	- $a^{-1}b \in H$
	- $b^{-1}a \in H$