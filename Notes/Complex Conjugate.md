---
tags:
  - mathematics
  - pre_calculus
---

# Definition

> [!info] Definition 1 (Complex Conjugate)[^1]
> The complex conjugate of a [[Complex Number|complex number]] $a + bi$ is
> $$
> \begin{align}
> \overline{a + bi} = a - bi
> \end{align}
> $$
> Note that $Re(z) = \frac{z + \overline{z}}{2}$, $Im(z) = \frac{z - \overline{z}}{2i}$

Multiplying a [[Complex Number]] by its conjugate results in a number without the [[Imaginary Unit]].

Reflection across the real line.

# Properties

For a complex numbers $z, w$

- $\overline{\overline{z}} = z$
- $\overline{z} + \overline{w} = \overline{z + w}$
- $\overline{z} \overline{w} = \overline{zw}$
- $(\overline{z})^n = \overline{z^n}$, for $n \in \mathbb{N}$
- $z \in \mathbb{R} \iff \overline{z} = z$
- $z \overline{z}$ is real and non-negative, and $z \overline{z} = 0 \iff z = 0$[^2]
- Also written $z^*$ (common in physics and signal processing).[^sigworth]
- **In Fourier transforms** ([[Fourier Transform]]) it encodes reflection and time reversal: for real $f$, $\hat f(-k) = \overline{\hat f(k)}$ (Hermitian symmetry), and the reversed signal $g(t) = f(-t)$ has $\hat g(k) = \hat f(-k) = \overline{\hat f(k)}$.
- $\overline{e^{z}} = e^{\bar z}$ ([[Complex Exponential Function]]).

[^1]: [szprecalculus07042013.pdf](zotero://open-pdf/library/items/J3667KH4?page=300)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=23)
[^sigworth]: [Sigworth, p. 2](zotero://open-pdf/library/items/6DH254TU?page=2&annotation=2P2WC9SS)
