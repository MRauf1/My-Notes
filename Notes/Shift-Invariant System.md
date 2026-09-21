---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Shift-Invariant System)[^1]
> A [[Linear Map|linear system]] whose form of response does not change as the position of the input stimulus is translated: shifting the input by some amount shifts the output by the same amount, leaving its shape unchanged.

# Properties
- Because every possible shifted stimulus produces the same response shape, only shifted, the system's entire [[Imaging Matrix|system matrix]] can be filled in from the response to a single stimulus (e.g. one line or one point), rather than requiring the response to every individual stimulus to be measured separately as for a general [[Linear Map|linear system]].
- A harmonic (sinusoidal) input at a given frequency produces a harmonic output at the same frequency: the output is a scaled, and in general phase-shifted, copy of the input frequency, never a different frequency.
- Fully characterized by its [[Optical Transfer Function]] in the frequency domain, or equivalently by its [[Point Spread Function]] (or, for one-dimensional stimuli, [[Line Spread Function]]) in the spatial domain.
- The optics of the human eye are approximately shift-invariant near the [[Fovea]], which licenses inferring the eye's complete [[Retinal Image Formation|imaging behavior]] from a single measured point or line response.

[^1]: [Foundations of Vision (Wandell)](zotero://open-pdf/library/items/YYQVJZJ3?page=19&annotation=HTIZEXPP)
