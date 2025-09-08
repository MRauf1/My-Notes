---
tags: mathematics, abstract_algebra
---

# Definition

> [!info] Definition 1 (Symmetries of Unit Disk)
> [[Group]] $D$ of symmetries of unit [[Disk]] ($\{(x, y, 0) | x^2 + y^2 \leq 1\}$) with $D \leq SO(3)$ and [[Symmetry]] operations
> There are two elements $A$ of $D$
> 1) $A(e_3) = e_3$ ([[Rotation]])
> 2) $A(e_3) = -e_3$ ([[Reflection]]/Flip)

The rotations and flip are
![[Screenshot 2025-06-26 183342.png]]

Therefore, $D = \{r_{\theta} | \theta \in [0, 2\pi)\} \cup \{j_{\theta} | \theta \in [0, \pi)\}$.

Alternatively, let $j_0 = j$, then $j_{\theta} = r_{2\theta}j$, so then $D = \{r_{\theta}, r_{\theta}j | \theta \in [0, 2\pi)\}$ with the definitional properties of rotation identity, rotation multiplication, $j^2 = e$, $jr_{\theta} = r_{\theta}^{-1}j$.

# Properties

# Rotation/Flip Identity
- $r_{\theta + 2\pi n} = r_{\theta}$ for $n \in \mathbb{Z}$
- $j_{\theta + \pi n} = j_{\theta}$ for $n \in \mathbb{Z}$

# Multiplication of Rotations and Flips
- $r_{\alpha} r_{\beta} = r_{\alpha + \beta}$
- $r_{\alpha} j_{\beta} = j_{\beta + \alpha/2}$
- $j_{\alpha} r_{\beta} = j_{\alpha - \beta/2}$
- $j_{\alpha} j_{\beta} = r_{2\alpha - 2\beta}$