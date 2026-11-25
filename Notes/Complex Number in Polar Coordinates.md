---
tags:
  - mathematics
  - complex_analysis
---

# Definition

> [!info] Definition 1 ([[Complex Number]] in [[Polar Coordinate System]])
> $$
> \begin{align}
> z = r \cos(\theta) + i\ r \sin(\theta)
> \end{align}
> $$
> $r$ is the [[Absolute Value of Complex Number]] of $z$, denoted by $|z|$.
> $\theta$ is the [[Argument (Complex Number)]] of $z$, denoted as $arg(z)$ (on the [[Domain]] of all reals) or $Arg(z)$ ([[Principal Branch of Argument]]) on the [[Domain]] $[- \pi, \pi)$.

[[Multiplication]] of $z_2$ by $z_1$ rotates $z_2$ by $arg(z_1)$ and scales it by $|z_1|$.

# Properties
- **Exponential form**: $z = A e^{i\theta}$ with $A = |z|$ and $\theta = \arg z$ ([[Euler's Identity]]).[^sigworth]
- **Computing the angle**: the formula $\theta = \tan^{-1}(b/a)$ for $z = a + bi$ is correct only when $a > 0$. In general $\theta = \operatorname{atan2}(b, a)$: add $\pi$ when $a < 0$, and take $\theta = \pm\pi/2$ when $a = 0$, $b \neq 0$; e.g. $z = -1$ has $\tan^{-1}(0/{-1}) = 0$ but $\arg z = \pi$.

[^sigworth]: [Sigworth, p. 2](zotero://open-pdf/library/items/6DH254TU?page=2&annotation=JJXYSK44)
