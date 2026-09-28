---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Convolution Formula[^1]
> Let $X_1, X_2$ be continuous random variables with joint pdf $f_{X_1, X_2}(x_1, x_2)$, $-\infty < x_i < \infty$. Then $Y = X_1 + X_2$ has pdf
> $$
> \begin{align}
> f_Y(y) = \int_{-\infty}^\infty f_{X_1, X_2}(y - x_2, x_2)\,dx_2
> \end{align}
> $$

It follows from the [[Random Vector Transformation]] $Y_1 = X_1 + X_2$, $Y_2 = X_2$ (Jacobian $1$) followed by integrating out $y_2$, or by differentiating the cdf from the [[Cumulative Distribution Function Method]].

# Properties
- If $X_1, X_2$ are [[Independent Random Variable|independent]], $f_Y(y) = \int f_{X_1}(y - x) f_{X_2}(x)\,dx = (f_{X_1} * f_{X_2})(y)$, the convolution of the marginal pdfs; correspondingly [[Moment Generating Function|mgfs]] and [[Characteristic Function (Probability)|characteristic functions]] multiply.
- Discrete analogue: $p_Y(y) = \sum_{x_2} p_{X_1, X_2}(y - x_2, x_2)$.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=124)
