---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Point Spread Function)[^1]
> For an imaging system, the image produced in response to a point source of light — i.e., the system's response to a point (impulse) input.

# Properties
- By the additivity and homogeneity that define a [[Linear Map|linear system]] ($T(u+v) = T(u) + T(v)$, $T(av) = aT(v)$), any two-dimensional input image can be described as a weighted sum of points, so the pointspread function together with these properties is enough to predict the system's response to any two-dimensional image.
- If the system is also [[Shift-Invariant System|shift-invariant]], a single measured pointspread function determines the response to a point at every other position as well, since these differ only by a shift.
- The [[Line Spread Function]] can always be computed from the pointspread function, since a line is a sum of points along one orientation; the converse only holds when the pointspread function is known to be circularly symmetric, in which case it can be uniquely recovered from the linespread function.
- An asymmetric pointspread function — narrower along one orientation than another — produces [[Astigmatism]], with better spatial resolution in the narrow direction.
- In the human eye, the pointspread function is limited chiefly by [[Diffraction]] at small [[Pupil|pupil]] diameters and by imperfections of the [[Cornea]] and [[Eye Lens]] at larger pupil diameters.

[^1]: [Foundations of Vision (Wandell)](zotero://open-pdf/library/items/YYQVJZJ3?page=32&annotation=IAMHV494)
