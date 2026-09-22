---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Shear Transformation)[^1]
> A [[Geometric Transformation]] that pushes points sideways by an amount proportional to their coordinate along a perpendicular axis, like pushing a deck of cards so the bottom card stays put while higher cards slide farther:
> $$
> \begin{align}
> \text{shear-x}(s) = \begin{bmatrix} 1 & s \\ 0 & 1 \end{bmatrix}, \qquad \text{shear-y}(s) = \begin{bmatrix} 1 & 0 \\ s & 1 \end{bmatrix}
> \end{align}
> $$
> extended to 3D by shearing along one axis based on the other two, e.g. $\text{shear-x}(d_y, d_z) = \begin{bmatrix} 1 & d_y & d_z \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$.

# Properties
- A shear maps a square outline to a parallelogram and a circle to an ellipse.
- Equivalent to tilting one coordinate axis while leaving the other fixed: $\text{shear-x}(\tan\varphi)$ tilts the vertical axis clockwise by angle $\varphi$, and the analogous horizontal-axis shear rotates it counterclockwise by $\varphi$.
- A 2D [[Rotation Matrix|rotation]] can be decomposed into a product of three shear matrices (Paeth, 1990), which is useful for raster image rotation because shearing a raster is efficient (shifting each row or column by a rounded amount) and leaves no gaps in the result, at the cost of some jagginess.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=126&annotation=JBR7Z6TQ)
