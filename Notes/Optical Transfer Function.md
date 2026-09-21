---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Optical Transfer Function)[^1]
> For a [[Shift-Invariant System|shift-invariant]] imaging system, the complex-valued function of spatial frequency that defines the system's complete response to harmonic (sinusoidal) inputs: its value at each frequency encodes both the amplitude scale factor and the phase shift the system induces in the harmonic component at that frequency.

# Properties
- Follows from the fact that a harmonic input to a shift-invariant system produces a harmonic output at the same frequency, only scaled in amplitude and shifted in phase — the optical transfer function records exactly that scale and phase shift as a function of frequency.
- An equivalent, frequency-domain description of a [[Shift-Invariant System|shift-invariant system]] to its spatial-domain [[Point Spread Function]] or [[Line Spread Function]].
- Reduces to the real-valued [[Modulation Transfer Function]] when the system's pointspread (or linespread) function is even-symmetric, since this introduces no phase shift.

[^1]: [Foundations of Vision (Wandell)](zotero://open-pdf/library/items/YYQVJZJ3?page=25&annotation=IGIBNTTI)
