---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Line Spread Function)[^1]
> For an imaging system, the image produced in response to a thin line source of light.

# Properties
- Can always be derived from the [[Point Spread Function]], since a line is the sum of many points arranged along one orientation, by the additivity of a [[Linear Map|linear system]].
- The converse does not generally hold: no combination of lines all oriented in the same direction can form a point, so the pointspread function cannot be recovered from a single linespread measurement — unless the pointspread function is known a priori to be circularly symmetric, in which case a unique pointspread function can be deduced from the linespread function.
- For a [[Shift-Invariant System|shift-invariant]] system, measuring the linespread function at a single position is sufficient to fill in the system's entire [[Imaging Matrix|system matrix]], since the response at every other position is just a shifted copy.
- If the linespread function is even-symmetric, the system introduces no phase shift into harmonic inputs, so the system can be described completely by the real-valued [[Modulation Transfer Function]] rather than the complex-valued [[Optical Transfer Function]].
- In the human eye, the observed linespread degrades from being diffraction-limited at small [[Pupil|pupil]] diameters to being limited mainly by imperfections of the [[Cornea]] and [[Eye Lens]] as the pupil widens.

[^1]: [Foundations of Vision (Wandell)](zotero://open-pdf/library/items/YYQVJZJ3?page=19&annotation=GWQ4X7HQ)
