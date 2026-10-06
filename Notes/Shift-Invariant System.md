---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Shift-Invariant System)[^1]
> A [[Linear Map|linear system]] whose form of response does not change as the position of the input stimulus is translated: shifting the input by some amount shifts the output by the same amount, leaving its shape unchanged.

> [!info] Definition (Linear Translation Invariant (LTI) System)[^2]
> A [[Linear System (Signal Processing)|linear system]] $f$ such that translating the input by $n_0, m_0$ translates the output by the same amount:
> $$
> \begin{align}
> \ell_{\text{out}}[n - n_0, m - m_0] = f\left(\ell_{\text{in}}[n - n_0, m - m_0]\right)
> \end{align}
> $$
> for any $n_0, m_0$, i.e. the system is [[Equivariant Function|equivariant]] with respect to translation. Linearity and translation invariance force the system to be a [[Convolution|convolution]] of the input with some convolution kernel $h$.

Motivated by the fact that we typically do not know where in the image a given item will appear, so the image should be processed in a spatially invariant manner, with the same processing at every pixel.

![[Hierarchy of Systems.png]]

# Properties
- The convolution kernel of an LTI system is its [[Impulse Response]].
- Because every possible shifted stimulus produces the same response shape, only shifted, the system's entire [[Imaging Matrix|system matrix]] can be filled in from the response to a single stimulus (e.g. one line or one point), rather than requiring the response to every individual stimulus to be measured separately as for a general [[Linear Map|linear system]].
- A harmonic (sinusoidal) input at a given frequency produces a harmonic output at the same frequency: the output is a scaled, and in general phase-shifted, copy of the input frequency, never a different frequency.
- Fully characterized by its [[Optical Transfer Function]] in the frequency domain, or equivalently by its [[Point Spread Function]] (or, for one-dimensional stimuli, [[Line Spread Function]]) in the spatial domain.
- The optics of the human eye are approximately shift-invariant near the [[Fovea]], which licenses inferring the eye's complete [[Retinal Image Formation|imaging behavior]] from a single measured point or line response.

- In deep learning terms, such a system is translation-[[Equivariant Function|equivariant]], and is implemented by a [[Convolutional Layer]].

[^1]: [Foundations of Vision (Wandell)](zotero://open-pdf/library/items/YYQVJZJ3?page=19&annotation=HTIZEXPP)
[^2]: [MIT Vision Book - Linear Image Filtering](https://visionbook.mit.edu/linear_image_filtering.html)
