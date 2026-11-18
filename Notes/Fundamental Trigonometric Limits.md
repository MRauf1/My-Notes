---
tags:
  - mathematics
  - calculus
---

# Definition

> [!abstract] Theorem 1 (Fundamental Trigonometric Limits)[^1]
> With $\theta$ in radians,
> $$
> \begin{align}
> \lim_{\theta \to 0} \frac{\sin\theta}{\theta} = 1, \qquad \lim_{\theta \to 0} \frac{\cos\theta - 1}{\theta} = 0
> \end{align}
> $$

# Properties
- These are exactly the two limits needed to compute the [[Derivative of Sine Function]] and [[Derivative of Cosine Function]] from the definition of the [[Derivative]] via the [[Sum and Difference Identities]].
- Scaled forms: $\lim_{x \to 0} \frac{\sin(kx)}{x} = k$, by substituting $\theta = kx$.
- The result needs radian measure; in degrees the first limit is $\pi/180$.

# Questions
> [!question]- What is the proof idea of $\lim_{\theta \to 0} \frac{\sin\theta}{\theta} = 1$?
> For $0 < \theta < \pi/2$, comparing areas (or arc length with chord and tangent segment) in the unit circle gives $\sin\theta < \theta < \tan\theta$, hence $\cos\theta < \frac{\sin\theta}{\theta} < 1$. Since $\cos\theta \to 1$, the [[Limit of Function Squeeze Theorem]] gives the right-hand limit $1$. Then $\frac{\sin\theta}{\theta}$ is an [[Even Function]], so the left-hand limit agrees ([[One-Sided Limit of Even Function]]).

> [!question]- How does the second limit follow from the first?
> Multiply by the conjugate: $\frac{\cos\theta - 1}{\theta} = \frac{\cos^2\theta - 1}{\theta(\cos\theta + 1)} = -\frac{\sin\theta}{\theta} \cdot \frac{\sin\theta}{\cos\theta + 1} \to -1 \cdot \frac{0}{2} = 0$ ([[Pythagorean Identities]]).

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=223)
